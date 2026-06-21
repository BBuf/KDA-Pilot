#!/usr/bin/env bash
set -euo pipefail

: "${MODEL:?set MODEL to the Hugging Face model id or local model path}"
: "${MODEL_SLUG:?set MODEL_SLUG, for example qwen_36}"

ROOT=${ROOT:-/data/bbuf/kda-pilot/llm}
SGLANG_REPO=${SGLANG_REPO:-/data/bbuf/repos/sglang-main}
RUN="${ROOT}/${MODEL_SLUG}/b200"
PORT=${PORT:-30000}
HOST=${HOST:-127.0.0.1}
SHAREGPT=${SHAREGPT:-"${ROOT}/sharegpt/ShareGPT_V3_unfiltered_cleaned_split.json"}
CAPTURE_DIR="${RUN}/capture"
RESET_RUN=${RESET_RUN:-1}
CLEAN_WEIGHTS=${CLEAN_WEIGHTS:-1}
RESULT_DONE=0

RANDOM_INPUT_LEN=${RANDOM_INPUT_LEN:-1000}
RANDOM_OUTPUT_LEN=${RANDOM_OUTPUT_LEN:-8}
SHAREGPT_OUTPUT_LEN=${SHAREGPT_OUTPUT_LEN:-8}
SHAREGPT_CONTEXT_LEN=${SHAREGPT_CONTEXT_LEN:-8192}
LOW_PROMPTS=${LOW_PROMPTS:-1}
MID_PROMPTS=${MID_PROMPTS:-32}
HIGH_PROMPTS=${HIGH_PROMPTS:-80}
LOW_CONCURRENCY=${LOW_CONCURRENCY:-1}
MID_CONCURRENCY=${MID_CONCURRENCY:-32}
HIGH_CONCURRENCY=${HIGH_CONCURRENCY:-80}
WARMUP_REQUESTS=${WARMUP_REQUESTS:-0}

TP_SIZE=${TP_SIZE:-}
DP_SIZE=${DP_SIZE:-}
ENABLE_DP_ATTENTION=${ENABLE_DP_ATTENTION:-0}
MEM_FRACTION_STATIC=${MEM_FRACTION_STATIC:-0.8}
CHUNKED_PREFILL_SIZE=${CHUNKED_PREFILL_SIZE:-32768}
MAX_RUNNING_REQUESTS=${MAX_RUNNING_REQUESTS:-80}
DISABLE_CUDA_GRAPH=${DISABLE_CUDA_GRAPH:-1}
SERVER_ARGS_EXTRA=${SERVER_ARGS_EXTRA:-}

if [[ "${RESET_RUN}" == "1" ]]; then
  rm -rf "${RUN}/bench" "${RUN}/capture" "${RUN}/docs" "${RUN}/kernels" "${RUN}/logs"
  rm -f "${RUN}/server.pid" "${RUN}/status.json" "${RUN}/status.md"
fi
mkdir -p "${RUN}/bench" "${RUN}/capture" "${RUN}/docs" "${RUN}/kernels" "${RUN}/logs" "${ROOT}/sharegpt"

export MODEL MODEL_SLUG RUN PORT CAPTURE_DIR

hf_cache_name() {
  local model_id="$1"
  if [[ "${model_id}" == /* || "${model_id}" != */* ]]; then
    return 1
  fi
  printf "models--%s\n" "${model_id//\//--}"
}

WEIGHT_CACHE=${WEIGHT_CACHE:-}
LOCK_CACHE=${LOCK_CACHE:-}
if [[ -z "${WEIGHT_CACHE}" ]]; then
  if cache_name=$(hf_cache_name "${MODEL}"); then
    WEIGHT_CACHE="/root/.cache/huggingface/hub/${cache_name}"
    LOCK_CACHE="/root/.cache/huggingface/hub/.locks/${cache_name}"
  fi
fi

write_status() {
  local stage="$1"
  local detail="$2"
  STAGE="$stage" DETAIL="$detail" python3 - <<'PY'
import json
import os
import time
from pathlib import Path

run = Path(os.environ["RUN"])
path = run / "status.json"
payload = {}
if path.exists():
    try:
        payload = json.loads(path.read_text())
    except Exception:
        payload = {}
payload.update(
    {
        "detail": os.environ["DETAIL"],
        "model": os.environ["MODEL"],
        "model_slug": os.environ["MODEL_SLUG"],
        "run_dir": str(run),
        "stage": os.environ["STAGE"],
        "updated_at": time.strftime("%Y-%m-%d %H:%M:%S %Z"),
    }
)
path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
with (run / "status.md").open("a") as f:
    f.write(f"- {payload['updated_at']}: {payload['stage']} - {payload['detail']}\n")
PY
}

wait_ready() {
  python3 - <<'PY'
import os
import sys
import time
import urllib.request

port = int(os.environ["PORT"])
pid = int(os.environ["SERVER_PID"])
log = os.environ["SERVER_LOG"]

for _ in range(5400):
    if os.system(f"kill -0 {pid} >/dev/null 2>&1") != 0:
        print("server exited early", file=sys.stderr)
        try:
            print(open(log, errors="ignore").read()[-20000:])
        except Exception:
            pass
        sys.exit(1)
    for endpoint in ("health", "health_generate"):
        try:
            urllib.request.urlopen(f"http://127.0.0.1:{port}/{endpoint}", timeout=2).read()
            print(f"server ready via /{endpoint}")
            sys.exit(0)
        except Exception:
            pass
    time.sleep(2)

print("server not ready within timeout", file=sys.stderr)
try:
    print(open(log, errors="ignore").read()[-20000:])
except Exception:
    pass
sys.exit(1)
PY
}

ensure_sharegpt() {
  if [[ -s "${SHAREGPT}" ]]; then
    return
  fi
  write_status "dataset_download" "downloading ShareGPT dataset to ${SHAREGPT}"
  SHAREGPT="${SHAREGPT}" python3 - <<'PY'
from pathlib import Path
import os

target = Path(os.environ["SHAREGPT"])
target.parent.mkdir(parents=True, exist_ok=True)
from huggingface_hub import hf_hub_download

path = hf_hub_download(
    repo_id="anon8231489123/ShareGPT_Vicuna_unfiltered",
    repo_type="dataset",
    filename="ShareGPT_V3_unfiltered_cleaned_split.json",
    local_dir=str(target.parent),
)
if Path(path) != target:
    target.write_bytes(Path(path).read_bytes())
print(target)
PY
}

set_label() {
  local label="$1"
  write_status "capture_label" "${label}"
}

run_bench() {
  local dataset="$1"
  local level="$2"
  local conc="$3"
  local prompts="$4"
  local label="${dataset}_${level}"
  local bench_log="${RUN}/bench/bench_${label}.log"
  local output_file="${RUN}/bench/${label}.jsonl"

  set_label "${label}"
  rm -f "${output_file}" "${bench_log}"
  write_status "benchmark" "${label}: dataset=${dataset}, prompts=${prompts}, concurrency=${conc}, output_len=8, warmup=${WARMUP_REQUESTS}"
  local args=(
    python3 -m sglang.bench_serving
    --backend sglang
    --host "${HOST}"
    --port "${PORT}"
    --model "${MODEL}"
    --num-prompts "${prompts}"
    --max-concurrency "${conc}"
    --output-file "${output_file}"
    --warmup-requests "${WARMUP_REQUESTS}"
    --disable-tqdm
  )
  if [[ "${dataset}" == "random" ]]; then
    args+=(
      --dataset-name random
      --random-input-len "${RANDOM_INPUT_LEN}"
      --random-output-len "${RANDOM_OUTPUT_LEN}"
    )
  else
    args+=(
      --dataset-name sharegpt
      --dataset-path "${SHAREGPT}"
      --sharegpt-output-len "${SHAREGPT_OUTPUT_LEN}"
      --sharegpt-context-len "${SHAREGPT_CONTEXT_LEN}"
    )
  fi
  "${args[@]}" > "${bench_log}" 2>&1
  write_status "benchmark_done" "${label}"
}

cleanup_server() {
  if [[ -n "${SERVER_PID:-}" ]]; then
    kill "${SERVER_PID}" >/dev/null 2>&1 || true
    sleep 3
  fi
}

cleanup_weights() {
  local reason="$1"
  if [[ "${CLEAN_WEIGHTS}" != "1" || -z "${WEIGHT_CACHE}" ]]; then
    write_status "weights_cleanup_skipped" "clean_weights=${CLEAN_WEIGHTS}; weight_cache=${WEIGHT_CACHE:-unset}; reason=${reason}"
    return
  fi
  local size="absent"
  if [[ -d "${WEIGHT_CACHE}" ]]; then
    size=$(du -sh "${WEIGHT_CACHE}" 2>/dev/null | awk '{print $1}')
    rm -rf "${WEIGHT_CACHE}"
  fi
  if [[ -n "${LOCK_CACHE}" ]]; then
    rm -rf "${LOCK_CACHE}" || true
  fi
  write_status "weights_cleanup" "${WEIGHT_CACHE}: deleted ${reason}, size_before=${size}; lock=${LOCK_CACHE:-unset}"
}

on_exit() {
  local rc=$?
  cleanup_server
  if [[ "${RESULT_DONE}" != "1" && "${rc}" != "0" ]]; then
    write_status "failed_or_interrupted" "exit_code=${rc}; cleaning partial weights"
    cleanup_weights "after failed/interrupted ${MODEL} kernel-interface capture run"
  fi
  exit "${rc}"
}
trap on_exit EXIT

export CUDA_VISIBLE_DEVICES=${CUDA_VISIBLE_DEVICES:-0,1,2,3,4,5,6,7}
export HF_HUB_DISABLE_XET=${HF_HUB_DISABLE_XET:-1}
export PYTHONPATH="${SGLANG_REPO}/python:${PYTHONPATH:-}"
export SGLANG_KERNEL_API_LOGLEVEL=3
export SGLANG_KERNEL_API_LOGDEST="${CAPTURE_DIR}/kernel_api_%i.log"

ensure_sharegpt
set_label "server_start"

SERVER_LOG="${RUN}/logs/server.log"
export SERVER_LOG

SERVER_ARGS=(
  python3 -m sglang.launch_server
  --model-path "${MODEL}"
  --host 0.0.0.0
  --port "${PORT}"
)
if [[ -n "${TP_SIZE}" ]]; then
  SERVER_ARGS+=(--tp-size "${TP_SIZE}")
fi
if [[ -n "${DP_SIZE}" ]]; then
  SERVER_ARGS+=(--dp-size "${DP_SIZE}")
fi
if [[ "${ENABLE_DP_ATTENTION}" == "1" ]]; then
  SERVER_ARGS+=(--enable-dp-attention)
fi
if [[ -n "${MEM_FRACTION_STATIC}" ]]; then
  SERVER_ARGS+=(--mem-fraction-static "${MEM_FRACTION_STATIC}")
fi
if [[ "${DISABLE_CUDA_GRAPH}" == "1" ]]; then
  SERVER_ARGS+=(--cuda-graph-backend-decode disabled --cuda-graph-backend-prefill disabled)
fi
if [[ -n "${CHUNKED_PREFILL_SIZE}" ]]; then
  SERVER_ARGS+=(--chunked-prefill-size "${CHUNKED_PREFILL_SIZE}")
fi
if [[ -n "${MAX_RUNNING_REQUESTS}" ]]; then
  SERVER_ARGS+=(--max-running-requests "${MAX_RUNNING_REQUESTS}")
fi
if [[ -n "${SERVER_ARGS_EXTRA}" ]]; then
  read -r -a EXTRA_ARGS <<< "${SERVER_ARGS_EXTRA}"
  SERVER_ARGS+=("${EXTRA_ARGS[@]}")
fi

cd "${SGLANG_REPO}"
write_status "server_start" "CUDA_VISIBLE_DEVICES=${CUDA_VISIBLE_DEVICES}; PYTHONPATH=${PYTHONPATH}; command=${SERVER_ARGS[*]}"
"${SERVER_ARGS[@]}" > "${SERVER_LOG}" 2>&1 &
SERVER_PID=$!
export SERVER_PID
printf "%s\n" "${SERVER_PID}" > "${RUN}/server.pid"

wait_ready
write_status "server_ready" "pid=${SERVER_PID}, port=${PORT}"

run_bench random low "${LOW_CONCURRENCY}" "${LOW_PROMPTS}"
run_bench random mid "${MID_CONCURRENCY}" "${MID_PROMPTS}"
run_bench random high "${HIGH_CONCURRENCY}" "${HIGH_PROMPTS}"
run_bench sharegpt low "${LOW_CONCURRENCY}" "${LOW_PROMPTS}"
run_bench sharegpt mid "${MID_CONCURRENCY}" "${MID_PROMPTS}"
run_bench sharegpt high "${HIGH_CONCURRENCY}" "${HIGH_PROMPTS}"

set_label "shutdown"
write_status "capture_matrix_done" "six workload kernel-interface capture complete"
cleanup_server
SERVER_PID=""

python3 "${ROOT}/scripts/build_kernel_interface_tasks.py" \
  --capture-dir "${CAPTURE_DIR}" \
  --run-dir "${RUN}" \
  --model "${MODEL}" \
  --model-slug "${MODEL_SLUG}" \
  --write-task-cards | tee "${RUN}/logs/task_generation.log"

cleanup_weights "after completed ${MODEL} kernel-interface capture run"
write_status "completed" "${MODEL} kernel-interface tasks generated"
RESULT_DONE=1
