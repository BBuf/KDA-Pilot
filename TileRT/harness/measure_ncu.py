"""≥3× stable ncu measurement driver for TileRT reference latencies (task B5).

Runs `ncu` N (>=3) independent times on `run_once.py --op <op> --seq <seq>`,
parses `gpu__time_duration.avg` (real on-GPU kernel time, us) and
`dram__throughput...pct_of_peak` for the target kernel, and reports
min / median / max + dispersion. Only the MEDIAN over >=3 runs is the target
that goes into a task's config.toml [reference] / docs/tilert_reference.md.

    python measure_ncu.py --op head_proj --seq 1 --kernel HeadProj --runs 3

Profile on an otherwise-idle B200. Requires ncu on PATH (CUDA 13 toolkit).
"""
import argparse
import csv
import io
import statistics
import subprocess
import sys

METRICS = (
    "gpu__time_duration.avg,"
    "dram__throughput.avg.pct_of_peak_sustained_elapsed,"
    "dram__bytes.sum"
)


DUR_COL = "gpu__time_duration.avg"
HBM_COL = "dram__throughput.avg.pct_of_peak_sustained_elapsed"


def one_run(op, seq, kernel, dev):
    cmd = [
        "ncu", "--clock-control", "none",
        "--kernel-name", f"regex:{kernel}",
        "--launch-count", "1",
        "--metrics", METRICS,
        "--csv", "--page", "raw",
        sys.executable, "run_once.py", "--op", op, "--seq", str(seq), "--dev", dev,
    ]
    p = subprocess.run(cmd, capture_output=True, text=True)
    out = p.stdout
    # --page raw CSV is WIDE: a header row, then a units row, then 1 data row/kernel.
    start = out.find('"ID"')
    if start < 0:
        return None, "no CSV: " + p.stderr[-400:]
    rows = list(csv.reader(io.StringIO(out[start:])))
    if len(rows) < 3:
        return None, "csv<3 rows: " + p.stderr[-300:]
    header = rows[0]
    units = rows[1]
    try:
        di, hi = header.index(DUR_COL), header.index(HBM_COL)
    except ValueError:
        return None, "metric col missing"
    dur_unit = units[di] if di < len(units) else ""
    # first data row = ID is an integer
    for r in rows[2:]:
        if not r or not r[0].strip().isdigit():
            continue
        try:
            dur = float(r[di].replace(",", ""))
            hbm = float(r[hi].replace(",", ""))
        except (ValueError, IndexError):
            continue
        if dur_unit == "ns":
            dur /= 1000.0      # ns -> us
        elif dur_unit == "ms":
            dur *= 1000.0
        return (dur, hbm), None
    return None, "no data row"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--op", required=True)
    ap.add_argument("--seq", type=int, default=1)
    ap.add_argument("--kernel", required=True, help="ExecutorImpl name regex, e.g. HeadProj")
    ap.add_argument("--runs", type=int, default=3)
    ap.add_argument("--dev", default="cuda:0")
    a = ap.parse_args()

    durs, hbms = [], []
    for i in range(a.runs):
        res, err = one_run(a.op, a.seq, a.kernel, a.dev)
        if res is None:
            print(f"run{i}: PARSE/RUN FAIL: {err}")
            continue
        d, h = res     # one_run already normalizes duration to us
        durs.append(d); hbms.append(h)
        print(f"run{i}: dur={d:.3f}us hbm={h}")

    if len(durs) >= 1:
        med = statistics.median(durs)
        disp = (max(durs) - min(durs)) / med * 100 if med else 0
        hmed = statistics.median([x for x in hbms if x is not None]) if any(hbms) else None
        print(f"\n[{a.op} seq{a.seq} {a.kernel}] n={len(durs)} "
              f"min={min(durs):.3f} median={med:.3f} max={max(durs):.3f} us "
              f"disp={disp:.1f}%  hbm_median={hmed}")
    else:
        print("no successful runs")


if __name__ == "__main__":
    main()
