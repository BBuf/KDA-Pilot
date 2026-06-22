#!/usr/bin/env bash
set -euo pipefail

ROOT=${ROOT:-/data/bbuf/kda-pilot/llm}
MODEL_SLUG=${MODEL_SLUG:-llama4}
MODEL=${MODEL:-LLM-Research/Llama-4-Scout-17B-16E-Instruct}

export SGLANG_USE_MODELSCOPE=${SGLANG_USE_MODELSCOPE:-true}
export MODELSCOPE_CACHE=${MODELSCOPE_CACHE:-/data/bbuf/.cache/modelscope}

export WEIGHT_CACHE=${WEIGHT_CACHE:-${MODELSCOPE_CACHE}/models/LLM-Research/Llama-4-Scout-17B-16E-Instruct}
export LOCK_CACHE=${LOCK_CACHE:-${MODELSCOPE_CACHE}/.lock/LLM-Research___Llama-4-Scout-17B-16E-Instruct}

export ROOT MODEL_SLUG MODEL
export SGLANG_REPO=${SGLANG_REPO:-/data/bbuf/repos/sglang-main}
export CUDA_VISIBLE_DEVICES=${CUDA_VISIBLE_DEVICES:-0,1,2,3,4,5,6,7}
export PORT=${PORT:-31006}
export TP_SIZE=${TP_SIZE:-8}
export MEM_FRACTION_STATIC=${MEM_FRACTION_STATIC:-0.8}
export CHUNKED_PREFILL_SIZE=${CHUNKED_PREFILL_SIZE:-8192}
export MAX_RUNNING_REQUESTS=${MAX_RUNNING_REQUESTS:-80}
export DISABLE_CUDA_GRAPH=${DISABLE_CUDA_GRAPH:-1}
export CLEAN_WEIGHTS=${CLEAN_WEIGHTS:-1}

export SERVER_ARGS_EXTRA=${SERVER_ARGS_EXTRA:-"--enable-multimodal --context-length 65536 --dtype bfloat16 --trust-remote-code --attention-backend triton --mm-attention-backend fa4 --disable-flashinfer-autotune --enforce-disable-flashinfer-allreduce-fusion --skip-server-warmup"}

"${ROOT}/scripts/run_kernel_interface_capture.sh"
