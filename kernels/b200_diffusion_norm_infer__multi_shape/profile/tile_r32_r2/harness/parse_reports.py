"""Extract the bound-analysis metrics from the tile_r32_r2 NCU reports into
analysis/metrics.csv (+ stdout summary). Uses the ncu_report Python module that
ships with Nsight Compute; metric names follow the sm_100 spellings (several
older names return None on B200).
"""

from __future__ import annotations

import csv
import sys
from pathlib import Path

for _cand in (
    "/opt/nvidia/nsight-compute/2025.3.1/extras/python",
    "/usr/local/NVIDIA-Nsight-Compute/extras/python",
):
    if Path(_cand).is_dir():
        sys.path.insert(0, _cand)
        break
import ncu_report  # noqa: E402

RUN_DIR = Path(__file__).resolve().parents[1]

METRICS = [
    ("duration_us", "gpu__time_duration.sum", 1e-3),  # ns -> us
    ("dram_throughput_pct", "gpu__dram_throughput.avg.pct_of_peak_sustained_elapsed", 1.0),
    ("dram_bytes_read", "dram__bytes_read.sum", 1.0),
    ("dram_bytes_write", "dram__bytes_write.sum", 1.0),
    ("mem_throughput_pct", "gpu__compute_memory_throughput.avg.pct_of_peak_sustained_elapsed", 1.0),
    ("sm_throughput_pct", "sm__throughput.avg.pct_of_peak_sustained_elapsed", 1.0),
    ("achieved_occupancy_pct", "sm__warps_active.avg.pct_of_peak_sustained_active", 1.0),
    ("registers_per_thread", "launch__registers_per_thread", 1.0),
    ("local_spill_loads", "memory_l1_local_spill_op_ld.sum", 1.0),
    ("local_spill_stores", "memory_l1_local_spill_op_st.sum", 1.0),
    ("grid_size", "launch__grid_size", 1.0),
    ("block_size", "launch__block_size", 1.0),
    ("stall_long_scoreboard_pct", "smsp__average_warps_issue_stalled_long_scoreboard_per_issue_active.ratio", 1.0),
    ("stall_wait_pct", "smsp__average_warps_issue_stalled_wait_per_issue_active.ratio", 1.0),
    ("stall_not_selected", "smsp__average_warps_issue_stalled_not_selected_per_issue_active.ratio", 1.0),
    ("issue_active_pct", "smsp__issue_active.avg.pct_of_peak_sustained_active", 1.0),
    ("l2_hit_rate_pct", "lts__t_sector_hit_rate.pct", 1.0),
]


def _grab(action, name):
    try:
        m = action.metric_by_name(name)
        return None if m is None else m.value()
    except Exception:
        return None


def extract(rep_path: Path, label: str, writer):
    if not rep_path.exists():
        print(f"-- {label}: {rep_path.name} missing, skipped")
        return
    ctx = ncu_report.load_report(str(rep_path))
    for ri in range(ctx.num_ranges()):
        rng = ctx.range_by_idx(ri)
        for ai in range(rng.num_actions()):
            action = rng.action_by_idx(ai)
            print(f"== {label}: {action.name()}")
            for friendly, raw, scale in METRICS:
                v = _grab(action, raw)
                if v is not None:
                    v = v * scale
                writer.writerow([label, action.name(), friendly, raw, v])
                print(f"   {friendly:28s} = {v}")


def main() -> int:
    out = RUN_DIR / "analysis" / "metrics.csv"
    out.parent.mkdir(parents=True, exist_ok=True)
    with out.open("w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["report", "kernel", "metric", "raw_metric", "value"])
        extract(RUN_DIR / "reports" / "full.ncu-rep", "tiled_r32_persistent", writer)
        extract(RUN_DIR / "reports" / "baseline_full.ncu-rep", "triton_baseline", writer)
    print(f"wrote {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
