"""Parse the targeted-metric NCU CSVs in ../analysis and print a bound table."""
import csv
import os
import sys

ANALYSIS = os.path.join(os.path.dirname(__file__), "..", "analysis")
ORDER = ["ln_base", "ln_cand", "rms_huge_base", "rms_huge_cand", "rms_small_base", "rms_small_cand"]
KEYS = {
    "gpu__time_duration.sum": "dur_ns",
    "dram__throughput.avg.pct_of_peak_sustained_elapsed": "dram",
    "sm__throughput.avg.pct_of_peak_sustained_elapsed": "sm",
    "sm__warps_active.avg.pct_of_peak_sustained_active": "occ",
    "launch__grid_size": "grid",
}

for name in (sys.argv[1:] or ORDER):
    path = os.path.join(ANALYSIS, name + ".csv")
    if not os.path.exists(path):
        continue
    lines = open(path).read().splitlines()
    hi = next((i for i, l in enumerate(lines) if l.startswith('"ID"')), None)
    if hi is None:
        print(f"{name:16s} (no data)")
        continue
    m = {}
    for r in csv.DictReader(lines[hi:]):
        mn = r.get("Metric Name")
        if mn in KEYS:
            m[KEYS[mn]] = r.get("Metric Value", "?")
    dur = m.get("dur_ns", "?").replace(",", "")
    dur_us = f"{float(dur)/1000:.1f}us" if dur not in ("?", "") else "?"
    print(f"{name:16s} dur={dur_us:>8s}  dram={m.get('dram','?'):>6s}%  sm={m.get('sm','?'):>6s}%  occ={m.get('occ','?'):>6s}%  grid={m.get('grid','?')}")
