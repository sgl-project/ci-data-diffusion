from __future__ import annotations

import html
import json
import re
import shutil
import time
from dataclasses import asdict
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw

from sglang.multimodal_gen.test.test_utils import (
    compute_clip_embedding,
    compute_clip_similarity,
    compute_mean_abs_diff,
    compute_psnr,
    compute_ssim,
    get_consistency_thresholds,
)


NATIVE_DIRS = [
    Path("/tmp/mmgen-native-report-latest"),
    Path("/tmp/mmgen-native-ltx23-report"),
]
OFFICIAL_DIRS = [
    Path("/tmp/mmgen-official-report-latest"),
    Path("/tmp/mmgen-official-wan22-ti2v-correct"),
    Path("/tmp/mmgen-official-image-refresh"),
    Path("/tmp/mmgen-official-ltx23-report"),
]
OUT_ROOT = Path("/tmp/mmgen-ci-official-vs-sglang-report-final")
OUT_DIR = OUT_ROOT / "out"

IMAGE_RE = re.compile(r"^(.+)_(\d+)gpu\.(jpg|jpeg|png|webp)$")
VIDEO_RE = re.compile(r"^(.+)_(\d+)gpu_frame_(0|mid|last)\.png$")

NATIVE_ONLY_CASES = {
    "flux_2_t2i_customized_vae_path": (
        "custom VAE path is not reproduced by the official script; existing official artifact used "
        "Flux2Pipeline with the default VAE, not --vae-path=fal/FLUX.2-Tiny-AutoEncoder"
    ),
    "wan2_1_t2v_1_3b_lora_1gpu": (
        "Wan dynamic LoRA/set_lora CI path is not an official-repo baseline; existing artifact was "
        "Diffusers WanPipeline + load_lora_weights, not Wan official repo and not dynamic-load semantics"
    ),
    "qwen_image_t2i_cache_dit_enabled": "cache_dit has no upstream official implementation",
    "flux_2_ti2i_multi_image_cache_dit": "cache_dit has no upstream official implementation",
    "wan2_1_t2v_1.3b_teacache_enabled": "teacache/cache path has no upstream official implementation",
    "layerwise_offload": "offload behavior has no upstream official implementation",
    "wan2_1_t2v_1.3b_text_encoder_cpu_offload": "offload behavior has no upstream official implementation",
    "wan2_1_t2v_1.3b_frame_interp_2x": "postprocess frame interpolation has no upstream official implementation",
    "wan2_1_t2v_1.3b_upscaling_4x": "postprocess upscaling has no upstream official implementation",
    "wan2_1_t2v_1.3b_frame_interp_2x_upscaling_4x": "postprocess frame interpolation/upscaling has no upstream official implementation",
    "flux_2_image_t2i_upscaling_4x": "postprocess upscaling has no upstream official implementation",
}

OFFICIAL_NOTES = {
    "wan2_2_ti2v_5b": "Official reference overlaid from Wan2.2 official repo; previous Diffusers path did not inject image.",
    "flux_2_image_t2i": "Official reference refreshed with current official Diffusers script.",
    "qwen_image_edit_2509_ti2i": "Official reference refreshed with current official Diffusers script.",
    "ltx_2.3_two_stage_t2v_2gpus": "Official LTX repo generation attempted on H200 with official 22B checkpoint; OOM before a valid official sample.",
    "ltx_2.3_one_stage_ti2v": "Official LTX repo generation attempted on H200 with official 22B checkpoint; OOM before a valid official sample.",
}


def parse_file(path: Path) -> dict | None:
    name = path.name
    m = VIDEO_RE.match(name)
    if m:
        return {
            "case_id": m.group(1),
            "num_gpus": int(m.group(2)),
            "kind": "video",
            "frame": m.group(3),
            "path": path,
        }
    m = IMAGE_RE.match(name)
    if m:
        return {
            "case_id": m.group(1),
            "num_gpus": int(m.group(2)),
            "kind": "image",
            "frame": "image",
            "path": path,
        }
    return None


def collect_files(dirs: list[Path]) -> dict[str, list[dict]]:
    result: dict[str, list[dict]] = {}
    for d in dirs:
        if not d.exists():
            continue
        for path in sorted(d.iterdir()):
            if not path.is_file():
                continue
            parsed = parse_file(path)
            if parsed is None:
                continue
            key = (parsed["case_id"], parsed["num_gpus"], parsed["kind"], parsed["frame"])
            result[str(key)] = [parsed]
    cases: dict[str, list[dict]] = {}
    for entries in result.values():
        entry = entries[-1]
        cases.setdefault(entry["case_id"], []).append(entry)
    for entries in cases.values():
        entries.sort(key=lambda x: (x["num_gpus"], x["kind"], {"0": 0, "mid": 1, "last": 2, "image": 0}[x["frame"]]))
    return cases


def load_rgb(path: Path) -> np.ndarray:
    return np.array(Image.open(path).convert("RGB"))


def save_compare(case_id: str, native_path: Path, official_path: Path | None) -> str:
    native = Image.open(native_path).convert("RGB")
    images = [native]
    labels = ["sglang"]
    if official_path is not None and official_path.exists():
        images.append(Image.open(official_path).convert("RGB"))
        labels.append("official")
    max_h = max(img.height for img in images)
    scaled = []
    for img in images:
        if img.height != max_h:
            w = int(round(img.width * max_h / img.height))
            img = img.resize((w, max_h), Image.Resampling.LANCZOS)
        scaled.append(img)
    label_h = 28
    gap = 8 if len(scaled) > 1 else 0
    width = sum(img.width for img in scaled) + gap * (len(scaled) - 1)
    canvas = Image.new("RGB", (width, max_h + label_h), "white")
    draw = ImageDraw.Draw(canvas)
    x = 0
    for img, label in zip(scaled, labels, strict=True):
        draw.text((x + 6, 7), label, fill=(20, 20, 20))
        canvas.paste(img, (x, label_h))
        x += img.width + gap
    out_name = f"{case_id}__{native_path.stem}.compare.jpg"
    canvas.save(OUT_DIR / out_name, quality=82)
    return out_name


def ltx_official_failures() -> dict[str, str]:
    manifest = Path("/tmp/mmgen-official-ltx23-report/official_ltx23_manifest.json")
    if not manifest.exists():
        return {}
    data = json.loads(manifest.read_text(encoding="utf-8"))
    failures = {}
    for failure in data.get("failures", []):
        failures[failure["case_id"]] = f"{failure.get('error_type')}: {failure.get('error')}"
    return failures


def metric_pass(metric: dict, thresholds) -> bool:
    return (
        metric["clip_similarity"] >= thresholds.clip_threshold
        and metric["ssim"] >= thresholds.ssim_threshold
        and metric["psnr"] >= thresholds.psnr_threshold
        and metric["mean_abs_diff"] <= thresholds.mean_abs_diff_threshold
    )


def main() -> None:
    if OUT_ROOT.exists():
        shutil.rmtree(OUT_ROOT)
    OUT_DIR.mkdir(parents=True, exist_ok=True)

    native_cases = collect_files(NATIVE_DIRS)
    official_cases = collect_files(OFFICIAL_DIRS)
    ltx_failures = ltx_official_failures()

    rows = []
    per_file = []

    for case_id in sorted(native_cases):
        native_entries = native_cases[case_id]
        official_entries = official_cases.get(case_id, [])
        is_video = native_entries[0]["kind"] == "video"
        thresholds = get_consistency_thresholds(case_id, is_video=is_video)
        status = "official_comparable"
        note = OFFICIAL_NOTES.get(case_id, "")
        if case_id in NATIVE_ONLY_CASES:
            status = "native_only_excluded"
            note = NATIVE_ONLY_CASES[case_id]
        elif case_id in ltx_failures:
            status = "official_oom"
            note = OFFICIAL_NOTES.get(case_id, "") + " " + ltx_failures[case_id].split(".")[0] + "."
        elif not official_entries:
            status = "official_missing"
            note = "No official reference artifact found."

        file_rows = []
        compare_files = []
        case_pass = None

        official_by_frame = {entry["frame"]: entry for entry in official_entries}
        for native in native_entries:
            official = official_by_frame.get(native["frame"])
            official_path = None if official is None else official["path"]
            compare_name = save_compare(case_id, native["path"], official_path if status == "official_comparable" else None)
            compare_files.append(compare_name)

            metric = {
                "case_id": case_id,
                "file": native["path"].name,
                "official_file": None if official_path is None else official_path.name,
                "status": status,
                "shape_match": None,
                "clip_similarity": None,
                "ssim": None,
                "psnr": None,
                "mean_abs_diff": None,
                "passed": None,
            }
            if status == "official_comparable" and official_path is not None:
                native_arr = load_rgb(native["path"])
                official_arr = load_rgb(official_path)
                metric["native_shape"] = list(native_arr.shape)
                metric["official_shape"] = list(official_arr.shape)
                metric["shape_match"] = native_arr.shape == official_arr.shape
                if metric["shape_match"]:
                    native_emb = compute_clip_embedding(native_arr)
                    official_emb = compute_clip_embedding(official_arr)
                    metric["clip_similarity"] = compute_clip_similarity(native_emb, official_emb)
                    metric["ssim"] = compute_ssim(native_arr, official_arr)
                    metric["psnr"] = compute_psnr(native_arr, official_arr)
                    metric["mean_abs_diff"] = compute_mean_abs_diff(native_arr, official_arr)
                    metric["passed"] = metric_pass(metric, thresholds)
                else:
                    metric["passed"] = False
            per_file.append(metric)
            file_rows.append(metric)

        comparable_metrics = [m for m in file_rows if m["passed"] is not None]
        if comparable_metrics:
            case_pass = all(bool(m["passed"]) for m in comparable_metrics)

        def agg(name: str, reducer):
            vals = [m[name] for m in comparable_metrics if m[name] is not None]
            return None if not vals else reducer(vals)

        rows.append(
            {
                "case_id": case_id,
                "status": status,
                "passed": case_pass,
                "num_files": len(native_entries),
                "min_clip": agg("clip_similarity", min),
                "min_ssim": agg("ssim", min),
                "min_psnr": agg("psnr", min),
                "max_mad": agg("mean_abs_diff", max),
                "thresholds": asdict(thresholds),
                "note": note.strip(),
                "compares": compare_files,
                "files": file_rows,
            }
        )

    summary = {
        "generated_at": time.strftime("%Y-%m-%d %H:%M:%S %Z"),
        "total_cases": len(rows),
        "official_comparable": sum(1 for r in rows if r["status"] == "official_comparable"),
        "official_pass": sum(1 for r in rows if r["status"] == "official_comparable" and r["passed"] is True),
        "official_fail": sum(1 for r in rows if r["status"] == "official_comparable" and r["passed"] is False),
        "native_only_excluded": sum(1 for r in rows if r["status"] == "native_only_excluded"),
        "official_oom": sum(1 for r in rows if r["status"] == "official_oom"),
        "official_missing": sum(1 for r in rows if r["status"] == "official_missing"),
    }

    (OUT_DIR / "case_summary_with_clip.json").write_text(
        json.dumps({"summary": summary, "cases": rows}, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )
    (OUT_DIR / "per_file_metrics_with_clip.json").write_text(
        json.dumps(per_file, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )

    def fmt(value, digits=4):
        if value is None:
            return "-"
        return f"{value:.{digits}f}"

    def status_class(row):
        if row["status"] == "official_comparable" and row["passed"] is True:
            return "pass"
        if row["status"] == "official_comparable" and row["passed"] is False:
            return "fail"
        if row["status"] == "native_only_excluded":
            return "excluded"
        return "pending"

    cards = []
    for row in rows:
        thumbs = "".join(
            f'<a href="{html.escape(name)}"><img src="{html.escape(name)}" loading="lazy"></a>'
            for name in row["compares"]
        )
        cards.append(
            f"""
            <tr class="{status_class(row)}">
              <td><code>{html.escape(row['case_id'])}</code></td>
              <td>{html.escape(row['status'])}</td>
              <td>{'PASS' if row['passed'] is True else 'FAIL' if row['passed'] is False else '-'}</td>
              <td>{fmt(row['min_clip'])}</td>
              <td>{fmt(row['min_ssim'])}</td>
              <td>{fmt(row['min_psnr'])}</td>
              <td>{fmt(row['max_mad'])}</td>
              <td>{html.escape(row['note'])}</td>
              <td class="thumbs">{thumbs}</td>
            </tr>
            """
        )

    html_text = f"""
<!doctype html>
<html>
<head>
<meta charset="utf-8">
<title>SGLang vs Official GT Report</title>
<style>
body {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif; margin: 24px; color: #202124; }}
h1 {{ font-size: 24px; margin: 0 0 8px; }}
.meta {{ color: #5f6368; margin-bottom: 18px; }}
.summary {{ display: flex; flex-wrap: wrap; gap: 10px; margin: 14px 0 20px; }}
.pill {{ border: 1px solid #dadce0; border-radius: 6px; padding: 8px 10px; background: #fff; }}
table {{ border-collapse: collapse; width: 100%; table-layout: fixed; }}
th, td {{ border-top: 1px solid #e0e0e0; padding: 8px; vertical-align: top; font-size: 13px; }}
th {{ text-align: left; position: sticky; top: 0; background: #f8f9fa; z-index: 1; }}
tr.pass {{ background: #f4fbf4; }}
tr.fail {{ background: #fff4f4; }}
tr.excluded {{ background: #f8f9fa; }}
tr.pending {{ background: #fff9e6; }}
code {{ font-size: 12px; }}
.thumbs {{ width: 420px; }}
.thumbs img {{ max-width: 190px; max-height: 150px; margin: 0 6px 6px 0; border: 1px solid #dadce0; }}
.notes {{ max-width: 1000px; line-height: 1.45; }}
</style>
</head>
<body>
<h1>SGLang vs Official GT Report</h1>
<div class="meta">Generated at {html.escape(summary['generated_at'])}. No ground-truth files were overwritten.</div>
<div class="summary">
  <div class="pill">Total cases: {summary['total_cases']}</div>
  <div class="pill">Official comparable: {summary['official_comparable']}</div>
  <div class="pill">Pass: {summary['official_pass']}</div>
  <div class="pill">Fail: {summary['official_fail']}</div>
  <div class="pill">Native-only excluded: {summary['native_only_excluded']}</div>
  <div class="pill">Official OOM/pending: {summary['official_oom']}</div>
  <div class="pill">Official missing: {summary['official_missing']}</div>
</div>
<div class="notes">
  <p>Policy applied: cache_dit, teacache, offload, and postprocess cases are excluded from official pass/fail because there is no upstream official implementation for those paths.</p>
  <p>Wan2.2 TI2V uses the corrected official Wan2.2 repository output. FLUX.2 image T2I and Qwen Image Edit 2509 use refreshed official references.</p>
  <p>LTX 2.3 representative native cases are included. Official LTX repo generation was attempted with the official 22B checkpoint, but H200 ran out of memory before producing valid samples, so those rows are pending rather than failed.</p>
</div>
<table>
<thead>
<tr>
  <th style="width: 240px;">Case</th>
  <th style="width: 150px;">Status</th>
  <th style="width: 60px;">Pass</th>
  <th style="width: 80px;">Min CLIP</th>
  <th style="width: 80px;">Min SSIM</th>
  <th style="width: 80px;">Min PSNR</th>
  <th style="width: 80px;">Max MAD</th>
  <th>Note</th>
  <th style="width: 430px;">Comparison</th>
</tr>
</thead>
<tbody>
{''.join(cards)}
</tbody>
</table>
</body>
</html>
"""
    (OUT_DIR / "index.html").write_text(html_text, encoding="utf-8")
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
