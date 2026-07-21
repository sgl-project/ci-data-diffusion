#!/usr/bin/env bash
set -euo pipefail

# Set HF_TOKEN in the environment before running. Do not hardcode it here.
OUT_DIR=${1:-/tmp/mmgen-official-wan22-ti2v}
WAN_REPO=${WAN_OFFICIAL_REPO_DIR:-/tmp/mmgen-official-code/Wan2.2}
SCRIPT_DIR=$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)
cd /sgl-workspace/sglang/python
PYTHONPATH="$WAN_REPO:$PYTHONPATH" python3 "$SCRIPT_DIR/gen_official_wan22_ti2v.py" \
  --out-dir "$OUT_DIR" \
  --wan-official-repo-dir "$WAN_REPO"
