"""Parse an NCU .ncu-rep with the ncu_report Python module (sm_100 names).

Writes a per-kernel-instance CSV plus a human summary to stdout. Metric names
follow external/ncu-report-skill/reference/08-b200-metric-names.md; every
access is defensive (missing metrics print as empty).

    python bench/ncu_extract.py reports/full.ncu-rep --out analysis/full.csv
"""

from __future__ import annotations

import argparse
import csv
import glob
import sys
from pathlib import Path


def _import_ncu_report():
    candidates = glob.glob("/usr/local/cuda/nsight-compute-*/extras/python")
    candidates += glob.glob("/opt/nvidia/nsight-compute/*/extras/python")
    for c in sorted(candidates, reverse=True):
        if (Path(c) / "ncu_report.py").exists():
            sys.path.insert(0, c)
            break
    import ncu_report  # noqa: E402

    return ncu_report


METRICS = [
    "gpu__time_duration.sum",
    "launch__grid_size",
    "launch__block_size",
    "launch__registers_per_thread",
    "launch__waves_per_multiprocessor",
    "sm__maximum_warps_per_active_cycle_pct",
    "sm__throughput.avg.pct_of_peak_sustained_elapsed",
    "gpu__compute_memory_throughput.avg.pct_of_peak_sustained_elapsed",
    "l1tex__throughput.avg.pct_of_peak_sustained_active",
    "lts__throughput.avg.pct_of_peak_sustained_elapsed",
    "dram__bytes_read.sum",
    "dram__bytes_write.sum",
    "dram__bytes_read.sum.per_second",
    "dram__bytes_write.sum.per_second",
    "dram__bytes_read.sum.pct_of_peak_sustained_elapsed",
    "dram__bytes_write.sum.pct_of_peak_sustained_elapsed",
    "smsp__issue_active.avg.pct_of_peak_sustained_active",
    "sm__warps_active.avg.pct_of_peak_sustained_active",
]

STALL_PREFIX = "smsp__average_warps_issue_stalled_"
STALL_SUFFIX = "_per_issue_active.ratio"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("report")
    ap.add_argument("--out", default="")
    args = ap.parse_args()

    ncu_report = _import_ncu_report()
    rep = ncu_report.load_report(args.report)
    rows = []
    for ri in range(rep.num_ranges()):
        rng = rep.range_by_idx(ri)
        for ai in range(rng.num_actions()):
            action = rng.action_by_idx(ai)
            row = {"kernel": action.name(), "instance": ai}
            names = set(action.metric_names())
            for m in METRICS:
                if m in names:
                    try:
                        row[m] = action[m].value()
                    except Exception:
                        row[m] = ""
                else:
                    row[m] = ""
            stalls = {}
            for n in names:
                if n.startswith(STALL_PREFIX) and n.endswith(STALL_SUFFIX):
                    reason = n[len(STALL_PREFIX):-len(STALL_SUFFIX)]
                    try:
                        stalls[reason] = action[n].value()
                    except Exception:
                        pass
            top = sorted(stalls.items(), key=lambda kv: -kv[1])[:5]
            row["top_stalls"] = "; ".join(f"{k}={v:.2f}" for k, v in top)
            rows.append(row)

    if args.out:
        out = Path(args.out)
        out.parent.mkdir(parents=True, exist_ok=True)
        with out.open("w", newline="") as fh:
            writer = csv.DictWriter(fh, fieldnames=list(rows[0].keys()))
            writer.writeheader()
            writer.writerows(rows)

    for row in rows:
        dur_ns = row.get("gpu__time_duration.sum") or 0
        rd = row.get("dram__bytes_read.sum") or 0
        wr = row.get("dram__bytes_write.sum") or 0
        dur_s = float(dur_ns) * 1e-9 if dur_ns else 0
        bw = (float(rd) + float(wr)) / dur_s / 1e12 if dur_s else 0
        print(f"== {row['kernel'][:90]} #{row['instance']}")
        print(
            f"   dur={float(dur_ns)/1e3 if dur_ns else 0:.1f}us grid={row.get('launch__grid_size')}"
            f" block={row.get('launch__block_size')} regs={row.get('launch__registers_per_thread')}"
            f" waves={row.get('launch__waves_per_multiprocessor')}"
        )
        print(
            f"   dram r+w={float(rd)/1e9 if rd else 0:.2f}+{float(wr)/1e9 if wr else 0:.2f} GB"
            f" -> {bw:.2f} TB/s; mem_SOL={row.get('gpu__compute_memory_throughput.avg.pct_of_peak_sustained_elapsed')}"
            f" dram_rd_pct={row.get('dram__bytes_read.sum.pct_of_peak_sustained_elapsed')}"
            f" sm_SOL={row.get('sm__throughput.avg.pct_of_peak_sustained_elapsed')}"
        )
        print(f"   occ={row.get('sm__warps_active.avg.pct_of_peak_sustained_active')}"
              f" issue={row.get('smsp__issue_active.avg.pct_of_peak_sustained_active')}"
              f" stalls: {row['top_stalls']}")


if __name__ == "__main__":
    main()
