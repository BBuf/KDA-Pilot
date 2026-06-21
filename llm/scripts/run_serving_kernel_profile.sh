#!/usr/bin/env bash
set -euo pipefail

CONFIG=${1:?usage: run_serving_kernel_profile.sh path/to/profile_config.sh}
source "${CONFIG}"

: "${FOLDER:?profile config must set FOLDER}"
: "${MODEL:?profile config must set MODEL}"
: "${SERVER_ARGS:?profile config must set SERVER_ARGS array}"

ROOT=${ROOT:-/data/bbuf/kda-pilot/llm}
RUN="${ROOT}/${FOLDER}/b200"
PORT=${PORT:-30000}
HOST=${HOST:-127.0.0.1}
SHAREGPT="${ROOT}/sharegpt/ShareGPT_V3_unfiltered_cleaned_split.json"
EXTRACTOR="${ROOT}/scripts/extract_kernel_shapes.py"
MODEL_CACHE_KEY=${MODEL_CACHE_KEY:-${MODEL//\//--}}
WEIGHT_CACHE=${WEIGHT_CACHE:-/root/.cache/huggingface/hub/models--${MODEL_CACHE_KEY}}
LOCK_CACHE=${LOCK_CACHE:-/root/.cache/huggingface/hub/.locks/models--${MODEL_CACHE_KEY}}
WORKLOAD_LABELS=${WORKLOAD_LABELS:-all}
CLEANUP_NAME=${CLEANUP_NAME:-${MODEL}}
EXTRA_MODEL_IDS=${EXTRA_MODEL_IDS:-}

mkdir -p "${RUN}/bench" "${RUN}/profile" "${RUN}/docs" "${RUN}/kernels" "${RUN}/logs" "${ROOT}/sharegpt"

export RUN MODEL PORT

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
        "model": os.environ["MODEL"],
        "stage": os.environ["STAGE"],
        "detail": os.environ["DETAIL"],
        "updated_at": time.strftime("%Y-%m-%d %H:%M:%S %Z"),
        "run_dir": str(run),
    }
)
path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
with (run / "status.md").open("a") as f:
    f.write(f"- {payload['updated_at']}: {payload['stage']} - {payload['detail']}\n")
PY
}

wait_ready() {
  python3 - <<PY
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
    local_dir_use_symlinks=False,
)
if Path(path) != target:
    target.write_bytes(Path(path).read_bytes())
print(target)
PY
}

should_run_label() {
  local label="$1"
  local requested=" ${WORKLOAD_LABELS//,/ } "
  if [[ "${WORKLOAD_LABELS}" == "all" || -z "${WORKLOAD_LABELS}" ]]; then
    return 0
  fi
  [[ "${requested}" == *" ${label} "* ]]
}

extract_shapes() {
  local label="$1"
  local dataset="$2"
  local level="$3"
  local profile_dir="${RUN}/profile/${label}"
  local out_base="${RUN}/docs/kernel_shapes_${label}"
  python3 "${EXTRACTOR}" "${profile_dir}" \
    --threshold 2.0 \
    --model "${MODEL}" \
    --dataset "${dataset}" \
    --concurrency "${level}" \
    --label "${label}" \
    --out-json "${out_base}.json" \
    --out-csv "${out_base}.tsv" \
    --out-md "${out_base}.md" \
    > "${RUN}/logs/extract_${label}.log" 2>&1
}

start_profile() {
  local label="$1"
  local profile_dir="$2"
  local profile_log="${RUN}/logs/profile_${label}.log"
  PROFILE_DIR="${profile_dir}" LABEL="${label}" python3 - <<'PY' > "${profile_log}" 2>&1
import json
import os
import urllib.request

port = int(os.environ["PORT"])
payload = {
    "output_dir": os.environ["PROFILE_DIR"],
    "profile_prefix": os.environ["LABEL"],
    "num_steps": 10,
    "activities": ["CPU", "GPU"],
    "record_shapes": True,
    "with_stack": False,
}
req = urllib.request.Request(
    f"http://127.0.0.1:{port}/start_profile",
    data=json.dumps(payload).encode(),
    headers={"Content-Type": "application/json"},
    method="POST",
)
with urllib.request.urlopen(req, timeout=30) as resp:
    body = resp.read().decode("utf-8", "replace")
print(f"start_profile status={resp.status} body={body.strip()} payload={payload}")
PY
}

wait_profile_files() {
  local label="$1"
  local profile_dir="$2"
  PROFILE_DIR="${profile_dir}" LABEL="${label}" python3 - <<'PY'
import glob
import os
import sys
import time

profile_dir = os.environ["PROFILE_DIR"]
label = os.environ["LABEL"]
patterns = [
    os.path.join(profile_dir, "**", f"{label}-*.trace.json*"),
    os.path.join(profile_dir, "**", "*.trace.json*"),
]
for _ in range(300):
    files = []
    for pat in patterns:
        files.extend(glob.glob(pat, recursive=True))
    files = sorted(set(files))
    if files:
        print("\n".join(files))
        sys.exit(0)
    time.sleep(1)
print(f"no profiler trace file found under {profile_dir}", file=sys.stderr)
sys.exit(1)
PY
}

run_bench() {
  local dataset="$1"
  local level="$2"
  local conc="$3"
  local prompts="$4"
  local label="${dataset}_${level}"
  if ! should_run_label "${label}"; then
    write_status "skip_benchmark" "${label}: skipped by WORKLOAD_LABELS=${WORKLOAD_LABELS}"
    return
  fi

  local bench_log="${RUN}/bench/bench_${label}.log"
  local output_file="${RUN}/bench/${label}.jsonl"
  local profile_dir="${RUN}/profile/${label}"

  rm -rf "${profile_dir}"
  rm -f "${output_file}" "${bench_log}" \
    "${RUN}/logs/extract_${label}.log" \
    "${RUN}/docs/kernel_shapes_${label}.json" \
    "${RUN}/docs/kernel_shapes_${label}.tsv" \
    "${RUN}/docs/kernel_shapes_${label}.md"
  mkdir -p "${profile_dir}"

  write_status "benchmark" "${label}: dataset=${dataset}, num_prompts=${prompts}, max_concurrency=${conc}"
  start_profile "${label}" "${profile_dir}"
  local args=(
    python3 -m sglang.bench_serving
    --backend sglang
    --host "${HOST}"
    --port "${PORT}"
    --model "${MODEL}"
    --num-prompts "${prompts}"
    --max-concurrency "${conc}"
    --output-file "${output_file}"
    --disable-tqdm
  )
  if [[ "${dataset}" == "random" ]]; then
    args+=(--dataset-name random --random-input-len 1000 --random-output-len 1000)
  else
    args+=(--dataset-name sharegpt --dataset-path "${SHAREGPT}")
  fi
  "${args[@]}" > "${bench_log}" 2>&1
  wait_profile_files "${label}" "${profile_dir}" > "${RUN}/logs/profile_files_${label}.log" 2>&1
  write_status "extract" "${label}: extracting >2% kernel shapes/meta"
  extract_shapes "${label}" "${dataset}" "${level}"
}

cleanup_server() {
  if [[ -n "${SERVER_PID:-}" ]]; then
    kill "${SERVER_PID}" >/dev/null 2>&1 || true
  fi
}

cleanup_one_weight_cache() {
  local cache="$1"
  local lock="$2"
  local reason="$3"
  local label="$4"
  local size="absent"
  if [[ -d "${cache}" ]]; then
    size=$(du -sh "${cache}" 2>/dev/null | awk '{print $1}')
    rm -rf "${cache}"
  fi
  rm -rf "${lock}" || true
  write_status "weights_cleanup" "${label}: ${cache}: deleted ${reason}, size_before=${size}; lock=${lock}"
}

cleanup_weights() {
  local reason="$1"
  cleanup_one_weight_cache "${WEIGHT_CACHE}" "${LOCK_CACHE}" "${reason}" "primary"
  local extra_id extra_key extra_cache extra_lock
  for extra_id in ${EXTRA_MODEL_IDS//,/ }; do
    [[ -n "${extra_id}" ]] || continue
    extra_key=${extra_id//\//--}
    extra_cache="/root/.cache/huggingface/hub/models--${extra_key}"
    extra_lock="/root/.cache/huggingface/hub/.locks/models--${extra_key}"
    cleanup_one_weight_cache "${extra_cache}" "${extra_lock}" "${reason}" "extra:${extra_id}"
  done
}

on_exit() {
  local rc=$?
  cleanup_server
  if [[ "${rc}" != "0" ]]; then
    write_status "failed_or_interrupted" "exit_code=${rc}; cleaning partial weights"
    cleanup_weights "after failed/interrupted ${CLEANUP_NAME} run"
  fi
  exit "${rc}"
}
trap on_exit EXIT

export CUDA_VISIBLE_DEVICES=${CUDA_VISIBLE_DEVICES:-0,1,2,3,4,5,6,7}
export HF_HUB_DISABLE_XET=${HF_HUB_DISABLE_XET:-1}
export SGLANG_TORCH_PROFILER_DIR="${RUN}/profile"
export SGLANG_PROFILE_RECORD_SHAPES=1
export SGLANG_PROFILE_WITH_STACK=0

ensure_sharegpt

SERVER_LOG="${RUN}/logs/server.log"
export SERVER_LOG

write_status "server_start" "CUDA_VISIBLE_DEVICES=${CUDA_VISIBLE_DEVICES}; command=${SERVER_ARGS[*]}"
"${SERVER_ARGS[@]}" > "${SERVER_LOG}" 2>&1 &
SERVER_PID=$!
export SERVER_PID
printf "%s\n" "${SERVER_PID}" > "${RUN}/server.pid"

wait_ready
write_status "server_ready" "pid=${SERVER_PID}, port=${PORT}"

run_bench random low 1 10
run_bench random mid 32 300
run_bench random high 100 500
run_bench sharegpt low 1 10
run_bench sharegpt mid 32 300
run_bench sharegpt high 100 500

write_status "completed" "${CLEANUP_NAME} benchmark/profile/shape extraction complete"
cleanup_server
SERVER_PID=""
cleanup_weights "after completed run"
