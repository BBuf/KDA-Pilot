#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR=$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)
ROOT=${ROOT:-$(cd -- "${SCRIPT_DIR}/../.." && pwd)}

export ROOT
export MODEL_SLUG=${MODEL_SLUG:-intern_s2_preview}
export MODEL=${MODEL:-internlm/Intern-S2-Preview-FP8}
export CUDA_VISIBLE_DEVICES=${CUDA_VISIBLE_DEVICES:-0,1,2,3}
export TP_SIZE=${TP_SIZE:-4}
export MEM_FRACTION_STATIC=${MEM_FRACTION_STATIC:-0.65}
export DISABLE_CUDA_GRAPH=${DISABLE_CUDA_GRAPH:-1}
export SERVER_ARGS_EXTRA=${SERVER_ARGS_EXTRA:---disable-cuda-graph --disable-piecewise-cuda-graph --trust-remote-code --reasoning-parser qwen3 --tool-call-parser qwen3_coder --quantization fp8 --attention-backend triton --disable-flashinfer-autotune --enforce-disable-flashinfer-allreduce-fusion}

exec "${ROOT}/scripts/run_kernel_interface_capture.sh"
