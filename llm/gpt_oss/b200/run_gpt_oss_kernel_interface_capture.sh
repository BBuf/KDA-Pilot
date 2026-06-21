#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR=$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)
ROOT=${ROOT:-$(cd -- "${SCRIPT_DIR}/../.." && pwd)}

export ROOT
export MODEL_SLUG=${MODEL_SLUG:-gpt_oss}
export MODEL=${MODEL:-openai/gpt-oss-120b}
export CUDA_VISIBLE_DEVICES=${CUDA_VISIBLE_DEVICES:-0,1,2,3,4,5,6,7}
export TP_SIZE=${TP_SIZE:-8}
export MEM_FRACTION_STATIC=${MEM_FRACTION_STATIC:-0.8}
export DISABLE_CUDA_GRAPH=${DISABLE_CUDA_GRAPH:-1}
export SERVER_ARGS_EXTRA=${SERVER_ARGS_EXTRA:---reasoning-parser gpt-oss --tool-call-parser gpt-oss --enforce-disable-flashinfer-allreduce-fusion --attention-backend triton --moe-runner-backend triton --disable-flashinfer-autotune}

exec "${ROOT}/scripts/run_kernel_interface_capture.sh"
