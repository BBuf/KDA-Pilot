#!/usr/bin/env bash
# Run inside the container on an idle H200 (CUDA_VISIBLE_DEVICES set).
set -e
cd "$(dirname "$0")"
mkdir -p reports analysis
METRICS=gpu__dram_throughput.avg.pct_of_peak_sustained_elapsed,sm__throughput.avg.pct_of_peak_sustained_elapsed,gpu__time_duration.sum,sm__warps_active.avg.pct_of_peak_sustained_active,launch__waves_per_multiprocessor,launch__grid_size

for B in rms_huge rms_small ln; do
  echo "==== $B ===="
  ncu --target-processes all --kernel-name-base demangled \
      --kernel-name "regex:rms_norm_bf16_n128|layer_norm_fp32" \
      --metrics "$METRICS" --launch-count 1 \
      python harness/prof.py "$B" 2>&1 \
    | grep -E "rms_norm_bf16_n128|layer_norm_fp32|dram_throughput|sm__throughput|gpu__time_duration|sm__warps_active|launch__waves|launch__grid_size" \
    | sed 's/^[[:space:]]*//'
done

# Full-set report + source counters for the bandwidth-bound representative (artifact).
ncu --set full --target-processes all --kernel-name-base demangled \
    --kernel-name "regex:rms_norm_bf16_n128" --launch-count 1 \
    -o reports/rms_huge_full -f python harness/prof.py rms_huge >/dev/null 2>&1 \
  && echo "FULL_REPORT_OK reports/rms_huge_full.ncu-rep"
ncu --set full --target-processes all --kernel-name-base demangled \
    --kernel-name "regex:layer_norm_fp32" --launch-count 1 \
    -o reports/ln_full -f python harness/prof.py ln >/dev/null 2>&1 \
  && echo "FULL_REPORT_OK reports/ln_full.ncu-rep"
