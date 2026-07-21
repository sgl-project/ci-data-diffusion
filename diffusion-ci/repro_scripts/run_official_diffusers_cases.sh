#!/usr/bin/env bash
set -euo pipefail

# Set HF_TOKEN in the environment before running. Do not hardcode it here.
OUT_DIR=${1:-/tmp/mmgen-official-diffusers-cases}
cd /sgl-workspace/sglang/python
python3 -m sglang.multimodal_gen.test.scripts.gen_official_diffusion_gt \
  --suite 1-gpu \
  --out-dir "$OUT_DIR" \
  --case-ids flux_2_image_t2i flux_2_klein_image_t2i flux_2_ti2i flux_image_t2i qwen_image_edit_2509_ti2i qwen_image_edit_2511_ti2i qwen_image_edit_ti2i qwen_image_layered_i2i qwen_image_t2i zimage_image_t2i \
  --dtype bf16 \
  --device-map none \
  --generator-device cuda \
  --continue-on-error
