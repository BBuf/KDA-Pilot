#!/usr/bin/env bash
# Run inside the container on an idle H200 (CUDA_VISIBLE_DEVICES set).
# Round 1: LN kernel is now double-precision internally; re-profile LN and add the
# required `--set source --section SourceCounters` reports for the representative kernels.
set -e
cd "$(dirname "$0")"
mkdir -p reports analysis
PERF=gpu__dram_throughput.avg.pct_of_peak_sustained_elapsed,sm__throughput.avg.pct_of_peak_sustained_elapsed,gpu__time_duration.sum,sm__warps_active.avg.pct_of_peak_sustained_active,launch__waves_per_multiprocessor,launch__grid_size
SRC=smsp__sass_inst_executed_op_global_ld.sum,smsp__sass_inst_executed_op_global_st.sum,l1tex__t_sectors_pipe_lsu_mem_global_op_ld.sum,l1tex__t_sectors_pipe_lsu_mem_global_op_st.sum

for B in rms_huge rms_small ln; do
  echo "==== $B (perf + source-counter metrics) ===="
  ncu --target-processes all --kernel-name-base demangled \
      --kernel-name "regex:rms_norm_bf16_n128|layer_norm_fp32" \
      --metrics "$PERF,$SRC" --launch-count 1 \
      python harness/prof.py "$B" 2>&1 \
    | grep -E "rms_norm_bf16_n128|layer_norm_fp32|dram_throughput|sm__throughput|gpu__time_duration|sm__warps_active|launch__waves|launch__grid_size|sass_inst_executed_op_global|t_sectors_pipe_lsu_mem_global" \
    | sed 's/^[[:space:]]*//'
done

# --set full (refresh LN for the double kernel; refresh RMS huge-M).
ncu --set full --target-processes all --kernel-name-base demangled \
    --kernel-name "regex:layer_norm_fp32" --launch-count 1 \
    -o reports/ln_full -f python harness/prof.py ln >/dev/null 2>&1 && echo "FULL_OK reports/ln_full.ncu-rep"
ncu --set full --target-processes all --kernel-name-base demangled \
    --kernel-name "regex:rms_norm_bf16_n128" --launch-count 1 \
    -o reports/rms_huge_full -f python harness/prof.py rms_huge >/dev/null 2>&1 && echo "FULL_OK reports/rms_huge_full.ncu-rep"

# --set source --section SourceCounters (the required source-counter reports).
ncu --set source --section SourceCounters --target-processes all --kernel-name-base demangled \
    --kernel-name "regex:rms_norm_bf16_n128" --launch-count 1 \
    -o reports/rms_huge_source -f python harness/prof.py rms_huge >/dev/null 2>&1 && echo "SOURCE_OK reports/rms_huge_source.ncu-rep"
ncu --set source --section SourceCounters --target-processes all --kernel-name-base demangled \
    --kernel-name "regex:layer_norm_fp32" --launch-count 1 \
    -o reports/ln_source -f python harness/prof.py ln >/dev/null 2>&1 && echo "SOURCE_OK reports/ln_source.ncu-rep"
