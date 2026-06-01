#!/bin/bash
# Run from the task cand root. Collects ncu --set full for the 3 representative
# buckets, capturing one isolated steady-state launch of the candidate kernel.
set -u
ND=profile/round0_ncu
mkdir -p "$ND/reports" "$ND/analysis"
for spec in "large_h24 8424 24" "large_h30 4128 30" "tiny 47 24"; do
  set -- $spec; name=$1; T=$2; H=$3
  echo "=== ncu --set full $name (T=$T H=$H) ==="
  ncu --set full --target-processes all \
      --kernel-name regex:fused_qknorm_rope \
      --launch-skip 60 --launch-count 1 \
      -o "$ND/reports/full_$name" -f \
      python "$ND/harness/prof_entry.py" "$T" "$H" \
      > "$ND/reports/log_full_$name.txt" 2>&1
  echo "  rc=$? -> $ND/reports/full_$name.ncu-rep"
done
echo "ALL_FULL_DONE"
