#!/usr/bin/env bash
# One-time baseline parity run (real SGLang op vs vendored snapshot), executed
# INSIDE the sglang_bbuf container on ion-b200. Three separate processes; never
# mixes the real package and the snapshot alias in one interpreter.
set -euo pipefail

RKD=/home/sglang-omni/bbuf/kda_runs/b200_diffusion_cutedsl_norm_scale_shift__multi_shape/2026-06-04_15-19-43
WS="$RKD/workspace"
GPU="${REMOTE_GPU_ID:-0}"

cd "$WS"
mkdir -p "$RKD/logs" "$RKD/parity"

nvidia-smi --query-gpu=index,name,utilization.gpu,memory.used --format=csv,noheader \
  > "$RKD/logs/parity_gpu_before.txt"

echo "[parity] side=real (imports installed SGLang)"
CUDA_VISIBLE_DEVICES=$GPU python bench/parity_check.py --side real \
  --out "$RKD/parity/real" > "$RKD/logs/parity_real.log" 2>&1

echo "[parity] side=copy (snapshot alias, no SGLang import)"
CUDA_VISIBLE_DEVICES=$GPU python bench/parity_check.py --side copy \
  --out "$RKD/parity/copy" > "$RKD/logs/parity_copy.log" 2>&1

echo "[parity] compare"
CUDA_VISIBLE_DEVICES=$GPU python bench/parity_check.py \
  --compare "$RKD/parity/real" "$RKD/parity/copy" \
  > "$RKD/logs/parity_compare.log" 2>&1
rc=$?

nvidia-smi --query-gpu=index,name,utilization.gpu,memory.used --format=csv,noheader \
  > "$RKD/logs/parity_gpu_after.txt"

echo "--- compare log ---"
cat "$RKD/logs/parity_compare.log"
echo "--- gpu before ---"; cat "$RKD/logs/parity_gpu_before.txt"
echo "--- gpu after ---"; cat "$RKD/logs/parity_gpu_after.txt"
exit $rc
