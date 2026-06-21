#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR=$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)
ROOT=${ROOT:-$(cd -- "${SCRIPT_DIR}/../.." && pwd)}

export ROOT
export MODEL_SLUG=${MODEL_SLUG:-qwen_36}
export MODEL=${MODEL:-Qwen/Qwen3.6-35B-A3B-FP8}
export CUDA_VISIBLE_DEVICES=${CUDA_VISIBLE_DEVICES:-0}
export TP_SIZE=${TP_SIZE:-1}
export MEM_FRACTION_STATIC=${MEM_FRACTION_STATIC:-0.7}
export PYTORCH_CUDA_ALLOC_CONF=${PYTORCH_CUDA_ALLOC_CONF:-expandable_segments:True}
export SGLANG_ENABLE_SPEC_V2=${SGLANG_ENABLE_SPEC_V2:-1}
export SERVER_ARGS_EXTRA=${SERVER_ARGS_EXTRA:---reasoning-parser qwen3 --tool-call-parser qwen3_coder --speculative-algorithm EAGLE --speculative-num-steps 3 --speculative-eagle-topk 1 --speculative-num-draft-tokens 4 --mm-attention-backend fa4 --attention-backend triton --disable-flashinfer-autotune}

exec "${ROOT}/scripts/run_kernel_interface_capture.sh"
