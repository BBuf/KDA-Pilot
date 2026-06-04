"""Extract the six-dimension metric set from the anchor NCU reports into CSV."""

import csv
import glob
import sys
from pathlib import Path

# ncu_report ships with Nsight Compute, not on sys.path by default.
for pattern in (
    "/usr/local/cuda/nsight-compute-*/extras/python",
    "/opt/nvidia/nsight-compute/*/extras/python",
    "/usr/local/NVIDIA-Nsight-Compute*/extras/python",
):
    for p in glob.glob(pattern):
        sys.path.insert(0, p)
import ncu_report  # noqa: E402

ANALYSIS_DIR = Path(__file__).resolve().parent
REPORTS_DIR = ANALYSIS_DIR.parent / "reports"

METRICS = [
    # geometry / duration
    "gpu__time_duration.sum",
    "launch__grid_size",
    "launch__block_size",
    "launch__waves_per_multiprocessor",
    "launch__occupancy_limit_blocks",
    "launch__occupancy_limit_registers",
    "launch__registers_per_thread",
    "sm__maximum_warps_per_active_cycle_pct",
    # occupancy / issue
    "sm__warps_active.avg.pct_of_peak_sustained_active",
    "smsp__issue_active.avg.pct_of_peak_sustained_active",
    "sm__throughput.avg.pct_of_peak_sustained_elapsed",
    # memory
    "dram__throughput.avg.pct_of_peak_sustained_elapsed",
    "dram__bytes.sum",
    "dram__bytes_read.sum",
    "dram__bytes_write.sum",
    "gpu__compute_memory_throughput.avg.pct_of_peak_sustained_elapsed",
    "lts__t_sector_hit_rate.pct",
    "l1tex__t_sector_hit_rate.pct",
    "sm__sass_average_data_bytes_per_sector_mem_global_op_ld.pct",
    # compute pipes
    "sm__inst_executed_pipe_xu.avg.pct_of_peak_sustained_active",
    "sm__inst_executed_pipe_fma.avg.pct_of_peak_sustained_active",
    "sm__inst_executed_pipe_alu.avg.pct_of_peak_sustained_active",
    "sm__inst_executed_pipe_lsu.avg.pct_of_peak_sustained_active",
]
STALL_PREFIX = "smsp__average_warps_issue_stalled_"


def main() -> int:
    rows = []
    stall_rows = []
    for rep_path in sorted(REPORTS_DIR.glob("full_*.ncu-rep")):
        ctx = ncu_report.load_report(str(rep_path))
        for ri in range(ctx.num_ranges()):
            rng = ctx.range_by_idx(ri)
            for ai in range(rng.num_actions()):
                action = rng.action_by_idx(ai)
                tag = rep_path.stem.replace("full_", "")
                base = {"entry": tag, "instance": ai, "kernel": action.name()}
                for m in METRICS:
                    metric = action.metric_by_name(m)
                    base[m] = metric.value() if metric is not None else ""
                rows.append(base)
                for name in action.metric_names():
                    if name.startswith(STALL_PREFIX) and name.endswith("_per_issue_active.ratio"):
                        metric = action.metric_by_name(name)
                        if metric is not None:
                            reason = name[len(STALL_PREFIX):].replace(
                                "_per_issue_active.ratio", ""
                            )
                            stall_rows.append(
                                {"entry": tag, "instance": ai, "stall": reason,
                                 "warps_per_issue": metric.value()}
                            )
    with (ANALYSIS_DIR / "metrics.csv").open("w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)
    with (ANALYSIS_DIR / "stalls.csv").open("w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["entry", "instance", "stall", "warps_per_issue"])
        w.writeheader()
        w.writerows(sorted(stall_rows, key=lambda r: (r["entry"], -float(r["warps_per_issue"]))))
    print(f"wrote {len(rows)} kernel instances, {len(stall_rows)} stall rows")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
