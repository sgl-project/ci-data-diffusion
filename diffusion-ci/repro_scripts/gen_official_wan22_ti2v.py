#!/usr/bin/env python3
"""Generate Wan2.2 TI2V official-repo GT for the SGLang CI case.

This script intentionally uses the Wan2.2 official repository, because the
Diffusers WanPipeline path does not accept the TI2V image input for this case.

Run inside the SGLang container from /sgl-workspace/sglang/python, with
PYTHONPATH pointing at the official Wan2.2 checkout.
"""

from __future__ import annotations

import argparse
import json
import os
import sys
from pathlib import Path

from diffusers.utils import load_image
from huggingface_hub import snapshot_download

from sglang.multimodal_gen.test.scripts.gen_official_diffusion_gt import (
    _final_request_for_case,
    _flatten_output,
    _install_wan_official_compat_modules,
    _postprocess_frames,
    _save_gt_frames,
)
from sglang.multimodal_gen.test.server.gpu_cases import ONE_GPU_CASES


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--out-dir", required=True)
    parser.add_argument(
        "--wan-official-repo-dir",
        default=os.environ.get("WAN_OFFICIAL_REPO_DIR", "/tmp/mmgen-official-code/Wan2.2"),
    )
    parser.add_argument("--checkpoint-dir", default=None)
    parser.add_argument("--offload-model", action="store_true")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    case = next(case for case in ONE_GPU_CASES if case.id == "wan2_2_ti2v_5b")
    req, _sampling_params, server_args, output_size = _final_request_for_case(case)

    repo_dir = Path(args.wan_official_repo_dir).resolve()
    if not (repo_dir / "wan" / "textimage2video.py").exists():
        raise FileNotFoundError(f"Expected official Wan2.2 repo at {repo_dir}")

    _install_wan_official_compat_modules()
    sys.path.insert(0, str(repo_dir))
    try:
        from wan.configs import WAN_CONFIGS
        from wan.textimage2video import WanTI2V
    finally:
        sys.path.pop(0)

    checkpoint_dir = args.checkpoint_dir or snapshot_download(
        "Wan-AI/Wan2.2-TI2V-5B",
        allow_patterns=[
            "*.json",
            "*.safetensors",
            "*.pth",
            "google/umt5-xxl/*",
        ],
    )
    cfg = WAN_CONFIGS["ti2v-5B"]
    image_path = req.image_path[0] if isinstance(req.image_path, list) else req.image_path
    image = load_image(image_path)

    pipe = WanTI2V(
        config=cfg,
        checkpoint_dir=checkpoint_dir,
        device_id=0,
        rank=0,
        t5_fsdp=False,
        dit_fsdp=False,
        use_sp=False,
        t5_cpu=False,
        convert_model_dtype=False,
    )
    output = pipe.generate(
        input_prompt=req.prompt,
        img=image,
        size=(int(req.width), int(req.height)),
        max_area=int(req.width) * int(req.height),
        frame_num=int(req.num_frames),
        shift=float(server_args.pipeline_config.flow_shift),
        sample_solver="unipc",
        sampling_steps=int(req.num_inference_steps),
        guide_scale=float(req.guidance_scale),
        n_prompt=req.negative_prompt or cfg.sample_neg_prompt,
        seed=int(req.seed),
        offload_model=bool(args.offload_model),
    )
    frames = _flatten_output(output)
    frames = _postprocess_frames(frames, case, req, is_video=True)
    saved_files = _save_gt_frames(frames, case, out_dir, is_video=True, req=req)

    manifest = {
        "generator": "official-wan2.2-repo",
        "case_id": case.id,
        "model_path": case.server_args.model_path,
        "official_repo_dir": str(repo_dir),
        "checkpoint_dir": checkpoint_dir,
        "output_size": output_size,
        "saved_files": saved_files,
        "call_kwargs": {
            "prompt": req.prompt,
            "image_path": image_path,
            "size": [int(req.width), int(req.height)],
            "max_area": int(req.width) * int(req.height),
            "frame_num": int(req.num_frames),
            "shift": float(server_args.pipeline_config.flow_shift),
            "sample_solver": "unipc",
            "sampling_steps": int(req.num_inference_steps),
            "guide_scale": float(req.guidance_scale),
            "seed": int(req.seed),
        },
    }
    (out_dir / "official_wan22_ti2v_manifest.json").write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
