#!/usr/bin/env bash
# Round-2 evidence pass: SourceCounters NCU reports for the four profile dirs
# that lack them (current shipped config, -lineinfo) + in-SGLang export smoke
# re-run at the current source. Detached-safe; writes its own log.
set -euo pipefail

RKD=/home/sglang-omni/bbuf/kda_runs/b200_diffusion_cutedsl_norm_scale_shift__multi_shape/2026-06-04_15-19-43
WS="$RKD/workspace"
GPU="${REMOTE_GPU_ID:-1}"
EV="$WS/bench/evidence/r2-ncu-source"

cd "$WS"
mkdir -p "$EV"
nvidia-smi --query-gpu=index,name,uuid,utilization.gpu,memory.used --format=csv,noheader,nounits > "$EV/allgpu_before.txt"

run_source() {  # run_dir case_id
  local RUN="$WS/profile/$1" CASE="$2"
  CUDA_VISIBLE_DEVICES=$GPU KDA_EXTRA_CUDA_CFLAGS=-lineinfo \
    ncu --set source --section SourceCounters -k regex:norm_scale_shift_kernel \
    --launch-skip 10 --launch-count 1 -f -o "$RUN/reports/source" \
    python bench/profile_case.py --case "$CASE" --impl candidate --iters 15 \
    > "$RKD/logs/ncu_source_$1.log" 2>&1
  ncu -i "$RUN/reports/source.ncu-rep" --page session > "$RUN/reports/source_session.txt" 2>/dev/null \
    || echo "(session export failed)" > "$RUN/reports/source_session.txt"
  sha256sum "$RUN/reports/source.ncu-rep" >> "$WS/profile/ncu_report_hashes.txt"
  echo "SOURCE_DONE $1"
}

run_source r0v1-nss-s11040-d5120-tokenfp32 nss-b1-s11040-d5120-bf16-s1SD.fp32-s1SD.fp32-eps1e-06
run_source r4f-huge-bf16row nss-b1-s176400-d5120-bf16-s11D.bf16-s11D.bf16-eps1e-06
run_source r4f-tokenfp32 nss-b1-s11040-d5120-bf16-s1SD.fp32-s1SD.fp32-eps1e-06
run_source r4f-tiny-s47 nss-b1-s47-d3072-bf16-s1D.bf16-s1D.bf16-eps1e-06
sort -u "$WS/profile/ncu_report_hashes.txt" -o "$WS/profile/ncu_report_hashes.txt"

echo "=== export smoke re-run at current source ==="
REMOTE_GPU_ID=$GPU bash "$WS/export/run_export_test.sh" > "$RKD/logs/export_rerun_r2.log" 2>&1
tail -22 "$RKD/logs/export_rerun_r2.log"

nvidia-smi --query-gpu=index,name,uuid,utilization.gpu,memory.used --format=csv,noheader,nounits > "$EV/allgpu_after.txt"
echo "R2_EVIDENCE_DONE"
