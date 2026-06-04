#!/usr/bin/env python3
"""Extract per-kernel headline metrics from the r1_losers NCU reports.

Writes analysis/metrics.csv with one row per profiled kernel launch:
name, duration, SM busy, DRAM read/write throughput and pct-of-peak,
achieved occupancy, smem bank-conflict shares, warp-stall leaders.
Uses sm_100 metric names (see ncu-report-skill reference/08).
"""

from __future__ import annotations

import csv
import sys
from pathlib import Path

import ncu_report  # type: ignore

REPORTS = Path(__file__).resolve().parent.parent / "reports"
ANALYSIS = Path(__file__).resolve().parent.parent / "analysis"

METRICS = [
    ("dur_ns", "gpu__time_duration.sum"),  # sm_100 reports nanoseconds
    ("sm_busy_pct", "sm__throughput.avg.pct_of_peak_sustained_elapsed"),
    ("dram_rd_gbps", "dram__bytes_read.sum.per_second"),
    ("dram_wr_gbps", "dram__bytes_write.sum.per_second"),
    ("dram_rd_pct", "dram__bytes_read.sum.pct_of_peak_sustained_elapsed"),
    ("dram_wr_pct", "dram__bytes_write.sum.pct_of_peak_sustained_elapsed"),
    ("occupancy_pct", "sm__warps_active.avg.pct_of_peak_sustained_active"),
    ("l1_conflict_shld", "l1tex__data_bank_conflicts_pipe_lsu_mem_shared_op_ld.sum"),
    ("l1_conflict_shst", "l1tex__data_bank_conflicts_pipe_lsu_mem_shared_op_st.sum"),
    ("grid", "launch__grid_size"),
    ("block", "launch__block_size"),
    ("regs", "launch__registers_per_thread"),
]


def metric(action, name):
    try:
        m = action[name]
    except (KeyError, TypeError):
        m = action.metric_by_name(name) if hasattr(action, "metric_by_name") else None
    if m is None:
        return ""
    try:
        return m.value()
    except Exception:
        return ""


def stall_leaders(action, top=3):
    names = [n for n in action.metric_names() if "warp_issue_stalled" in n and n.endswith("per_warp_active.pct")]
    vals = []
    for n in names:
        try:
            vals.append((float(action[n].value()), n))
        except Exception:
            pass
    vals.sort(reverse=True)
    return "; ".join(f"{n.split('stalled_')[-1].split('_per_warp')[0]}={v:.1f}%" for v, n in vals[:top])


def main() -> int:
    ANALYSIS.mkdir(parents=True, exist_ok=True)
    out = ANALYSIS / "metrics.csv"
    with out.open("w", newline="") as f:
        wr = csv.writer(f)
        wr.writerow(["report", "idx", "kernel"] + [m[0] for m in METRICS] + ["top_stalls"])
        for rep in sorted(REPORTS.glob("*.ncu-rep")):
            ctx = ncu_report.load_report(str(rep))
            for ri in range(ctx.num_ranges()):
                rng = ctx.range_by_idx(ri)
                for ai in range(rng.num_actions()):
                    a = rng.action_by_idx(ai)
                    row = [rep.stem, ai, a.name()]
                    for _, mname in METRICS:
                        row.append(metric(a, mname))
                    row.append(stall_leaders(a))
                    wr.writerow(row)
    print(f"wrote {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
