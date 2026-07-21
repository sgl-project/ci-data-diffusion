#!/usr/bin/env bash
set -euo pipefail

# Set HF_TOKEN in the environment before running. Do not hardcode it here.
# Reproduces faithful LTX-2.3 official-repo video key frames with the same
# CI-sized sampling params. The default path keeps the official batched
# guided-denoiser and AttentionFunction.DEFAULT semantics with max_batch_size=1.
# Pass --skip-v2a-cross-attn-for-video-gt to reproduce older legacy GT behavior.
OUT_DIR=${1:-/tmp/mmgen-official-ltx23-report}
SCRIPT_DIR=$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)
export PYTHONPATH=/tmp/mmgen-official-code/LTX-2/packages/ltx-core/src:/tmp/mmgen-official-code/LTX-2/packages/ltx-pipelines/src:/sgl-workspace/sglang/python:$PYTHONPATH
cd /sgl-workspace/sglang/python
python3 "$SCRIPT_DIR/gen_official_ltx23.py" \
  --out-dir "$OUT_DIR" \
  --case-ids ltx_2.3_two_stage_t2v_2gpus ltx_2.3_one_stage_ti2v ltx_2_3_hq_pipeline \
  "${@:2}"
