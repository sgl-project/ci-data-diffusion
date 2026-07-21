#!/usr/bin/env bash
set -euo pipefail

# Set HF_TOKEN in the environment before running. Do not hardcode it here.
OUT_DIR=${1:-/tmp/mmgen-official-wan21}
WAN_REPO=${WAN_OFFICIAL_REPO_DIR:-/tmp/mmgen-official-code/Wan2.1}
cd /sgl-workspace/sglang/python
python3 -m sglang.multimodal_gen.test.scripts.gen_official_diffusion_gt \
  --suite 1-gpu \
  --out-dir "$OUT_DIR" \
  --case-ids wan2_1_t2v_1.3b \
  --wan-official-repo-dir "$WAN_REPO" \
  --dtype bf16 \
  --device-map none \
  --generator-device cuda
