#!/usr/bin/env bash
# NCU profiling round r0v1: two runs per the ncu-report-skill layout.
#   run A: huge bf16 broadcast case (candidate) — how far from the HBM bound?
#   run B: per-token fp32 case (candidate AND baseline) — why device parity/regression?
# Executed inside sglang_bbuf on ion-b200. One directory per run, never reused.
set -euo pipefail

RKD=/home/sglang-omni/bbuf/kda_runs/b200_diffusion_cutedsl_norm_scale_shift__multi_shape/2026-06-04_15-19-43
WS="$RKD/workspace"
GPU="${REMOTE_GPU_ID:-0}"
CASE_A="nss-b1-s176400-d5120-bf16-s11D.bf16-s11D.bf16-eps1e-06"
CASE_B="nss-b1-s11040-d5120-bf16-s1SD.fp32-s1SD.fp32-eps1e-06"
RUN_A="$WS/profile/r0v1-nss-s176400-d5120-bf16row"
RUN_B="$WS/profile/r0v1-nss-s11040-d5120-tokenfp32"

cd "$WS"
nvidia-smi --query-gpu=index,utilization.gpu,memory.used --format=csv,noheader,nounits | sed -n "$((GPU+1))p" > "$RKD/logs/profile_gpu_before.txt"

mkdir -p "$RUN_A"/{harness,reports,analysis} "$RUN_B"/{harness,reports,analysis}
cp bench/profile_case.py "$RUN_A/harness/" && cp bench/profile_case.py "$RUN_B/harness/"

echo "=== run A: candidate full ==="
CUDA_VISIBLE_DEVICES=$GPU KDA_EXTRA_CUDA_CFLAGS=-lineinfo \
  ncu --set full --target-processes all -k 'regex:norm_scale_shift_kernel' \
  --launch-skip 10 --launch-count 3 -f -o "$RUN_A/reports/full" \
  python bench/profile_case.py --case "$CASE_A" --impl candidate --iters 25 > "$RKD/logs/profA_full.log" 2>&1

echo "=== run A: candidate source ==="
CUDA_VISIBLE_DEVICES=$GPU KDA_EXTRA_CUDA_CFLAGS=-lineinfo \
  ncu --set source --section SourceCounters -k 'regex:norm_scale_shift_kernel' \
  --launch-skip 10 --launch-count 1 -f -o "$RUN_A/reports/source" \
  python bench/profile_case.py --case "$CASE_A" --impl candidate --iters 15 > "$RKD/logs/profA_src.log" 2>&1

echo "=== run B: candidate full ==="
CUDA_VISIBLE_DEVICES=$GPU KDA_EXTRA_CUDA_CFLAGS=-lineinfo \
  ncu --set full --target-processes all -k 'regex:norm_scale_shift_kernel' \
  --launch-skip 10 --launch-count 3 -f -o "$RUN_B/reports/full_candidate" \
  python bench/profile_case.py --case "$CASE_B" --impl candidate --iters 25 > "$RKD/logs/profB_cand.log" 2>&1

echo "=== run B: baseline full (CuTe kernel; skip input-gen + warmup launches) ==="
CUDA_VISIBLE_DEVICES=$GPU \
  ncu --set full --target-processes all \
  --launch-skip 28 --launch-count 2 -f -o "$RUN_B/reports/full_baseline" \
  python bench/profile_case.py --case "$CASE_B" --impl baseline --iters 30 > "$RKD/logs/profB_base.log" 2>&1

echo "=== extract ==="
python bench/ncu_extract.py "$RUN_A/reports/full.ncu-rep" --out "$RUN_A/analysis/full.csv"
python bench/ncu_extract.py "$RUN_B/reports/full_candidate.ncu-rep" --out "$RUN_B/analysis/full_candidate.csv"
python bench/ncu_extract.py "$RUN_B/reports/full_baseline.ncu-rep" --out "$RUN_B/analysis/full_baseline.csv"

nvidia-smi --query-gpu=index,utilization.gpu,memory.used --format=csv,noheader,nounits | sed -n "$((GPU+1))p" > "$RKD/logs/profile_gpu_after.txt"
echo "=== gpu before/after ==="
cat "$RKD/logs/profile_gpu_before.txt" "$RKD/logs/profile_gpu_after.txt"
