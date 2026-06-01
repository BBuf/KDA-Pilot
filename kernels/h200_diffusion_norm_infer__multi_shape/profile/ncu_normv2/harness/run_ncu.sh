#!/bin/bash
# Targeted NCU bound analysis for the normv2 candidate vs the SGLang baseline.
# Profiles the post-warmup launch of each kernel with a small metric set that
# names the active limiter (DRAM throughput / compute / occupancy / duration).
set -u
cd "$(dirname "$0")"
OUT=../analysis
mkdir -p "$OUT" ../reports
METRICS="gpu__time_duration.sum,dram__bytes.sum,dram__throughput.avg.pct_of_peak_sustained_elapsed,sm__throughput.avg.pct_of_peak_sustained_elapsed,sm__warps_active.avg.pct_of_peak_sustained_active,launch__grid_size,launch__waves_per_multiprocessor"
KREGEX="rms_norm_warp|layer_norm_block|rms_norm_tiled_onepass|norm_infer_kernel"

run() {  # name kind M N
  ncu --csv --metrics "$METRICS" --target-processes all -k "regex:$KREGEX" \
      --launch-skip 5 --launch-count 1 \
      python profile_entry.py "$2" "$3" "$4" > "$OUT/$1.csv" 2> "$OUT/$1.log" || true
  echo "=== $1 ($2 $3x$4) ==="
  python3 - "$OUT/$1.csv" << 'PY' 2>/dev/null || { echo "  [no csv] tail log:"; tail -4 "$OUT/$1.log"; }
import csv, sys
rows = list(csv.DictReader(open(sys.argv[1])))
if not rows:
    raise SystemExit(1)
kn = rows[0].get("Kernel Name", "?")
print("  kernel:", kn[:60])
for r in rows:
    print(f"  {r.get('Metric Name'):60s} {r.get('Metric Value'):>14s} {r.get('Metric Unit','')}")
PY
}

run ln_cand        ln        8640   5120
run ln_base        ln_base   8640   5120
run rms_huge_cand  rms       648720 128
run rms_huge_base  rms_base  648720 128
run rms_small_cand rms       4096   128
run rms_small_base rms_base  4096   128
echo "DONE"
