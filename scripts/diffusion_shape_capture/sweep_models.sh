#!/usr/bin/env bash
# Run sequential shape-capture passes for a list of diffusion presets.
#
# Required env from caller:
#   HOST_LABEL       (e.g., ion-b200)
#   ARCH_LABEL       (e.g., b200 or h200)
#   GPU_LIST_1GPU    (e.g., "0,1,2,3,4,5,6,7")  - GPUs usable for 1-GPU presets
#   GPU_LIST_4GPU    (e.g., "0,1,2,3")           - GPUs for 4-GPU presets
#   HF_TOKEN         optional; only used for gated presets such as flux/flux2
#
# Args:
#   $1: comma-separated list of preset slugs, or "all"
#   $2: output JSONL log path

set -uo pipefail

presets_csv="$1"
log_path="$2"

CAP_DIR="${CAP_DIR:-/root/diffusion_shape_capture}"
BENCH_PY="${BENCH_PY:-/root/bench_diffusion_denoise.py}"
SGLANG_DIR="${SGLANG_DIR:-/home/sglang-omni/bbuf/repos/sglang}"

export PYTHONPATH="${CAP_DIR}:${SGLANG_DIR}/python:${PYTHONPATH:-}"
export FLASHINFER_DISABLE_VERSION_CHECK="${FLASHINFER_DISABLE_VERSION_CHECK:-1}"
export TOKENIZERS_PARALLELISM="${TOKENIZERS_PARALLELISM:-false}"
BASE_HF_TOKEN="${HF_TOKEN:-${HUGGINGFACE_HUB_TOKEN:-}}"
if [[ -z "$BASE_HF_TOKEN" && -s /root/.cache/huggingface/token ]]; then
  BASE_HF_TOKEN="$(tr -d '\n' < /root/.cache/huggingface/token)"
fi
export DIFFUSION_SHAPE_LOG="$log_path"
export DIFFUSION_SHAPE_HOST="${HOST_LABEL:-unknown}"
export DIFFUSION_SHAPE_ARCH="${ARCH_LABEL:-unknown}"

mkdir -p "$(dirname "$log_path")" /tmp/diff_cap_out

cd "$SGLANG_DIR"

list_all_presets() {
  python3 "$BENCH_PY" --list-models | awk '
    /^[[:space:]]*Preset[[:space:]]+Nightly[[:space:]]+Model Path/ { in_table=1; next }
    in_table && /^-+$/ { dash_count += 1; next }
    in_table && dash_count == 1 && NF >= 4 { print $1; next }
    in_table && dash_count >= 2 { exit }
  '
}

if [[ -z "$presets_csv" || "$presets_csv" == "all" ]]; then
  mapfile -t presets < <(list_all_presets)
else
  IFS=',' read -ra presets <<< "$presets_csv"
fi

if [[ "${#presets[@]}" -eq 0 ]]; then
  echo "[sweep] ERROR: no presets resolved from BENCH_PY=$BENCH_PY" >&2
  exit 2
fi

GPU_LIST_1GPU_VAL="${GPU_LIST_1GPU:-0}"
GPU_LIST_4GPU_VAL="${GPU_LIST_4GPU:-0,1,2,3}"

needs_4gpu() {
  case "$1" in
    wan-t2v|wan-i2v|mova-720p) return 0 ;;
    *) return 1 ;;
  esac
}

needs_2gpu() {
  case "$1" in
    ltx2|ltx23-ti2v-two-stage|ltx23-one-stage|ltx23-two-stage|ltx23-two-stage-cfg-parallel|joyai-edit|firered-edit-1.0|firered-edit-1.1) return 0 ;;
    *) return 1 ;;
  esac
}

needs_hf_token() {
  case "$1" in
    flux|flux2) return 0 ;;
    *) return 1 ;;
  esac
}

prepare_hf_auth() {
  local preset="$1"
  if needs_hf_token "$preset"; then
    export HF_TOKEN="$BASE_HF_TOKEN"
    export HUGGINGFACE_HUB_TOKEN="$BASE_HF_TOKEN"
  else
    # Public presets should not inherit an expired or under-scoped token.
    unset HF_TOKEN
    unset HUGGINGFACE_HUB_TOKEN
  fi
}

perf_json_ok() {
  local path="$1"
  python3 - "$path" <<'PY'
import json
import sys
from pathlib import Path

path = Path(sys.argv[1])
if not path.exists():
    sys.exit(1)
try:
    data = json.loads(path.read_text())
except Exception:
    sys.exit(1)
if data.get("error") is True:
    sys.exit(1)

has_denoise_step = False
for step in data.get("steps", []):
    name = step.get("name")
    if (
        isinstance(name, str)
        and step.get("duration_ms") is not None
        and (
            name.endswith("DenoisingStage")
            or name.endswith("RefinementStage")
        )
        and "BeforeDenoisingStage" not in name
    ):
        has_denoise_step = True
        break
if data.get("denoise_steps_ms"):
    has_denoise_step = True
if not has_denoise_step:
    sys.exit(1)
sys.exit(0)
PY
}

model_path_for_preset() {
  local preset="$1"
  python3 - "$BENCH_PY" "$preset" <<'PY'
import importlib.util
import sys

bench_py, preset = sys.argv[1], sys.argv[2]
spec = importlib.util.spec_from_file_location("bench_diffusion_denoise_for_cleanup", bench_py)
mod = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(mod)
print(mod.MODELS[preset]["path"])
PY
}

hf_cache_slug() {
  local model_path="$1"
  printf 'models--%s\n' "${model_path//\//--}"
}

cleanup_model_weights() {
  local preset="$1"
  local model_path slug cache_root
  model_path="$(model_path_for_preset "$preset" 2>/dev/null || true)"
  if [[ -z "$model_path" ]]; then
    echo "[cleanup] preset=$preset model_path=unknown skip"
    return 0
  fi
  slug="$(hf_cache_slug "$model_path")"
  if [[ -n "${HUGGINGFACE_HUB_CACHE:-}" ]]; then
    cache_root="$HUGGINGFACE_HUB_CACHE"
  elif [[ -n "${HF_HOME:-}" ]]; then
    cache_root="${HF_HOME%/}/hub"
  else
    cache_root="/root/.cache/huggingface/hub"
  fi
  echo "[cleanup] preset=$preset model=$model_path cache=${cache_root}/${slug}"
  rm -rf "${cache_root:?}/${slug}" \
         "${HF_HOME:?}" \
         "/root/.cache/modelscope/hub/${model_path}" \
         "/tmp/diff_cap_out/${preset}_"* \
         "/tmp/diff_cap_out/${preset}-"* 2>/dev/null || true
}

for preset in "${presets[@]}"; do
  export DIFFUSION_SHAPE_MODEL="$preset"
  before_lines="$(wc -l < "$log_path" 2>/dev/null || echo 0)"
  safe_preset="${preset//[^A-Za-z0-9_]/_}"
  export HF_HOME="/tmp/hfcap_${ARCH_LABEL:-x}_${safe_preset}_$$"
  mkdir -p "$HF_HOME"
  if needs_4gpu "$preset"; then
    export CUDA_VISIBLE_DEVICES="$GPU_LIST_4GPU_VAL"
  elif needs_2gpu "$preset"; then
    first_two="${GPU_LIST_4GPU_VAL}"
    IFS=',' read -ra gpu_parts <<< "$first_two"
    if [[ "${#gpu_parts[@]}" -ge 2 ]]; then
      export CUDA_VISIBLE_DEVICES="${gpu_parts[0]},${gpu_parts[1]}"
    else
      export CUDA_VISIBLE_DEVICES="$GPU_LIST_4GPU_VAL"
    fi
  else
    first_gpu="${GPU_LIST_1GPU_VAL%%,*}"
    if [[ -z "$first_gpu" ]]; then
      first_gpu="${GPU_LIST_4GPU_VAL%%,*}"
    fi
    export CUDA_VISIBLE_DEVICES="$first_gpu"
  fi
  prepare_hf_auth "$preset"
  perf_path="/tmp/diff_cap_out/${preset}_cap.json"
  rm -f "$perf_path"
  echo "============================================================"
  echo "[sweep] preset=$preset host=${HOST_LABEL} arch=${ARCH_LABEL} CUDA_VISIBLE_DEVICES=$CUDA_VISIBLE_DEVICES log=$log_path"
  echo "============================================================"
  # Use a per-preset timeout so a stuck model does not block the sweep.
  timeout --signal=KILL --kill-after=60 1500 python3 "$BENCH_PY" \
    --model "$preset" \
    --label cap \
    --output-dir /tmp/diff_cap_out \
    --no-torch-compile 2>&1 | tail -150
  rc=${PIPESTATUS[0]}
  after_lines="$(wc -l < "$log_path" 2>/dev/null || echo 0)"
  new_lines="$((after_lines - before_lines))"
  if [[ "$rc" -eq 0 && "$new_lines" -gt 0 ]] && perf_json_ok "$perf_path"; then
    status="ok"
  else
    status="failed"
  fi
  echo "[sweep] preset=$preset exit=$rc status=$status new_shape_lines=$new_lines perf=$perf_path"
  cleanup_model_weights "$preset"
done

echo "[sweep] DONE host=${HOST_LABEL} arch=${ARCH_LABEL} log=$log_path"
echo "[sweep] log lines: $(wc -l < "$log_path" 2>/dev/null || echo 0)"
