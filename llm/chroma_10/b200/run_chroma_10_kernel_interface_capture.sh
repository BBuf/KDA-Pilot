#!/usr/bin/env bash
set -euo pipefail

ROOT=${ROOT:-/data/bbuf/kda-pilot/llm}
MODEL_SLUG=${MODEL_SLUG:-chroma_10}
MODEL=${MODEL:-FlashLabs/Chroma-4B}
RUN="${ROOT}/${MODEL_SLUG}/b200"
PORT=${PORT:-31007}
HOST=${HOST:-127.0.0.1}
CHROMA_CONTAINER=${CHROMA_CONTAINER:-chroma_sglang_bbuf_capture}
CHROMA_IMAGE=${CHROMA_IMAGE:-flashlabs/chroma:latest}
CHROMA_REPO=${CHROMA_REPO:-/data/bbuf/repos/Chroma-SGLang}
CHROMA_GPU_DEVICE=${CHROMA_GPU_DEVICE:-0}
DOCKER_CMD_TEXT=${DOCKER_CMD_TEXT:-sudo docker}
read -r -a DOCKER_CMD <<< "${DOCKER_CMD_TEXT}"
DP_SIZE=${DP_SIZE:-1}
RESET_RUN=${RESET_RUN:-1}
CLEAN_WEIGHTS=${CLEAN_WEIGHTS:-1}
LOW_REQUESTS=${LOW_REQUESTS:-1}
MID_REQUESTS=${MID_REQUESTS:-4}
HIGH_REQUESTS=${HIGH_REQUESTS:-8}
LOW_CONCURRENCY=${LOW_CONCURRENCY:-1}
MID_CONCURRENCY=${MID_CONCURRENCY:-4}
HIGH_CONCURRENCY=${HIGH_CONCURRENCY:-8}
CHROMA_MAX_TOKENS=${CHROMA_MAX_TOKENS:-32}
RESULT_DONE=0

MODELSCOPE_CACHE=${MODELSCOPE_CACHE:-/data/bbuf/.cache/modelscope}
WEIGHT_CACHE=${WEIGHT_CACHE:-${MODELSCOPE_CACHE}/models/FlashLabs/Chroma-4B}
LOCK_CACHE=${LOCK_CACHE:-${MODELSCOPE_CACHE}/.lock/FlashLabs___Chroma-4B}
TEMP_CACHE=${TEMP_CACHE:-${MODELSCOPE_CACHE}/models/._____temp/FlashLabs/Chroma-4B}
CAPTURE_DIR="${RUN}/capture"

export ROOT MODEL_SLUG MODEL RUN PORT HOST CAPTURE_DIR DOCKER_CMD_TEXT CHROMA_MAX_TOKENS

if [[ "${RESET_RUN}" == "1" ]]; then
  rm -rf "${RUN}/bench" "${RUN}/capture" "${RUN}/docs" "${RUN}/kernels" "${RUN}/logs"
  rm -f "${RUN}/server.pid" "${RUN}/status.json" "${RUN}/status.md"
fi
mkdir -p "${RUN}/bench" "${RUN}/capture" "${RUN}/docs" "${RUN}/kernels" "${RUN}/logs"

write_status() {
  local stage="$1"
  local detail="$2"
  TZ=UTC STAGE="$stage" DETAIL="$detail" python3 - <<'PY'
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

set_label() {
  write_status "capture_label" "$1"
}

cleanup_server() {
  if [[ -n "${SERVER_LOG_PID:-}" ]]; then
    kill "${SERVER_LOG_PID}" >/dev/null 2>&1 || true
  fi
  "${DOCKER_CMD[@]}" rm -f "${CHROMA_CONTAINER}" >/dev/null 2>&1 || true
}

cleanup_weights() {
  local reason="$1"
  if [[ "${CLEAN_WEIGHTS}" != "1" ]]; then
    write_status "weights_cleanup_skipped" "clean_weights=${CLEAN_WEIGHTS}; reason=${reason}"
    return
  fi
  local size="absent"
  if [[ -d "${WEIGHT_CACHE}" ]]; then
    size=$(du -sh "${WEIGHT_CACHE}" 2>/dev/null | awk '{print $1}')
  fi
  rm -rf "${WEIGHT_CACHE}" "${LOCK_CACHE}" "${TEMP_CACHE}"
  write_status "weights_cleanup" "${WEIGHT_CACHE}: deleted ${reason}, size_before=${size}; lock=${LOCK_CACHE}; temp=${TEMP_CACHE}"
}

on_exit() {
  local rc=$?
  cleanup_server
  if [[ "${RESULT_DONE}" != "1" && "${rc}" != "0" ]]; then
    write_status "failed_or_interrupted" "exit_code=${rc}; cleaning partial weights"
    cleanup_weights "after failed/interrupted Chroma kernel-interface capture run"
  fi
  exit "${rc}"
}
trap on_exit EXIT

if [[ ! -d "${WEIGHT_CACHE}" ]]; then
  write_status "missing_weights" "${WEIGHT_CACHE} not found; run modelscope download first"
  exit 1
fi

SERVER_LOG="${RUN}/logs/server.log"
write_status "server_start" "container=${CHROMA_CONTAINER}; image=${CHROMA_IMAGE}; gpu=${CHROMA_GPU_DEVICE}; model=${WEIGHT_CACHE}"
"${DOCKER_CMD[@]}" rm -f "${CHROMA_CONTAINER}" >/dev/null 2>&1 || true
"${DOCKER_CMD[@]}" run -d \
  --name "${CHROMA_CONTAINER}" \
  --gpus "device=${CHROMA_GPU_DEVICE}" \
  --ipc=host \
  --shm-size=64g \
  -p "${PORT}:8000" \
  -v /data/bbuf:/data/bbuf \
  -v "${CHROMA_REPO}:/app/Chroma-SGLang" \
  -w /app/Chroma-SGLang \
  -e CHROMA_MODEL_PATH="${WEIGHT_CACHE}" \
  -e DP_SIZE="${DP_SIZE}" \
  -e PYTHONPATH="${RUN}/scripts:/app/Chroma-SGLang" \
  -e SGLANG_KERNEL_API_LOGLEVEL=3 \
  -e SGLANG_KERNEL_API_LOGDEST="${CAPTURE_DIR}/kernel_api_%i.log" \
  "${CHROMA_IMAGE}" \
  /opt/conda/bin/python3 "${RUN}/scripts/chroma_capture_server.py" > "${RUN}/server.pid"
"${DOCKER_CMD[@]}" logs -f "${CHROMA_CONTAINER}" > "${SERVER_LOG}" 2>&1 &
SERVER_LOG_PID=$!

wait_ready() {
  TZ=UTC python3 - <<'PY'
import os
import sys
import time
import urllib.request

container = os.environ["CHROMA_CONTAINER"]
docker_cmd = os.environ["DOCKER_CMD_TEXT"].split()
port = int(os.environ["PORT"])
log = os.environ["SERVER_LOG"]

for _ in range(5400):
    inspect_cmd = " ".join(docker_cmd + ["inspect", "-f", "'{{.State.Running}}'", container])
    if os.system(f"{inspect_cmd} >/tmp/chroma_state 2>/dev/null") != 0:
        print("container disappeared", file=sys.stderr)
        print(open(log, errors="ignore").read()[-20000:])
        sys.exit(1)
    if open("/tmp/chroma_state").read().strip() != "true":
        print("container exited early", file=sys.stderr)
        print(open(log, errors="ignore").read()[-20000:])
        sys.exit(1)
    try:
        payload = urllib.request.urlopen(f"http://127.0.0.1:{port}/health", timeout=2).read()
        if b"healthy" in payload:
            print("server ready")
            sys.exit(0)
    except Exception:
        pass
    time.sleep(2)

print("server not ready within timeout", file=sys.stderr)
print(open(log, errors="ignore").read()[-20000:])
sys.exit(1)
PY
}

export CHROMA_CONTAINER SERVER_LOG
wait_ready
write_status "server_ready" "port=${PORT}"

run_requests() {
  local label="$1"
  local requests="$2"
  local concurrency="$3"
  local bench_log="${RUN}/bench/bench_${label}.log"
  local output_file="${RUN}/bench/${label}.jsonl"
  set_label "${label}"
  write_status "benchmark" "${label}: audio_prompt=assets/question_audio.wav, requests=${requests}, concurrency=${concurrency}, max_tokens=${CHROMA_MAX_TOKENS}, return_audio=false"
  LABEL="${label}" REQUESTS="${requests}" CONCURRENCY="${concurrency}" OUTPUT_FILE="${output_file}" BENCH_LOG="${bench_log}" TZ=UTC python3 - <<'PY'
import concurrent.futures
import json
import os
import time
import urllib.request

host = os.environ["HOST"]
port = int(os.environ["PORT"])
label = os.environ["LABEL"]
num_requests = int(os.environ["REQUESTS"])
concurrency = int(os.environ["CONCURRENCY"])
max_tokens = int(os.environ["CHROMA_MAX_TOKENS"])
output_file = os.environ["OUTPUT_FILE"]
bench_log = os.environ["BENCH_LOG"]

payload = {
    "model": "chroma",
    "messages": [
        {"role": "system", "content": "You are Chroma, a voice agent developed by FlashLabs."},
        {
            "role": "user",
            "content": [
                {"type": "audio", "audio": "/app/Chroma-SGLang/assets/question_audio.wav"}
            ],
        },
    ],
    "max_tokens": max_tokens,
    "temperature": 1.0,
    "top_p": 1.0,
    "return_audio": False,
}
body = json.dumps(payload).encode()

def one_request(index: int) -> dict:
    req = urllib.request.Request(
        f"http://{host}:{port}/v1/chat/completions",
        data=body,
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    start = time.time()
    with urllib.request.urlopen(req, timeout=600) as resp:
        response_body = resp.read()
    return {
        "index": index,
        "label": label,
        "status": resp.status,
        "latency_s": time.time() - start,
        "response_bytes": len(response_body),
    }

results = []
with concurrent.futures.ThreadPoolExecutor(max_workers=concurrency) as pool:
    futures = [pool.submit(one_request, i) for i in range(num_requests)]
    for fut in concurrent.futures.as_completed(futures):
        results.append(fut.result())

with open(output_file, "w") as f:
    for row in sorted(results, key=lambda x: x["index"]):
        f.write(json.dumps(row, sort_keys=True) + "\n")
with open(bench_log, "w") as f:
    f.write(json.dumps({"label": label, "results": results}, indent=2, sort_keys=True) + "\n")
print(f"{label}: completed {len(results)} requests")
PY
  write_status "benchmark_done" "${label}"
}

run_requests chroma_audio_low "${LOW_REQUESTS}" "${LOW_CONCURRENCY}"
run_requests chroma_audio_mid "${MID_REQUESTS}" "${MID_CONCURRENCY}"
run_requests chroma_audio_high "${HIGH_REQUESTS}" "${HIGH_CONCURRENCY}"

set_label "shutdown"
write_status "capture_matrix_done" "chroma audio workload kernel-interface capture complete"
cleanup_server
SERVER_LOG_PID=""

python3 "${ROOT}/scripts/build_kernel_interface_tasks.py" \
  --capture-dir "${CAPTURE_DIR}" \
  --run-dir "${RUN}" \
  --model "${MODEL}" \
  --model-slug "${MODEL_SLUG}" \
  --label-order chroma_audio_low,chroma_audio_mid,chroma_audio_high \
  --write-task-cards | tee "${RUN}/logs/task_generation.log"

cleanup_weights "after completed Chroma kernel-interface capture run"
write_status "completed" "${MODEL} kernel-interface tasks generated"
RESULT_DONE=1
