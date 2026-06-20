"""Single-launch driver for ncu profiling of one TileRT op/shape.

Builds the op via tilert_oracle.CASES (which already does one tilert_forward to
compute the correctness rel error), then issues exactly ONE more launch of the
real kernel for ncu to capture. Use with `--kernel-name regex:<ExecutorImpl>` and
`--launch-count 1` so ncu profiles a single matching kernel.

    ncu --clock-control none --kernel-name regex:HeadProj --launch-count 1 \
        --metrics gpu__time_duration.avg,\
dram__throughput.avg.pct_of_peak_sustained_elapsed,dram__bytes.sum \
        python run_once.py --op head_proj --seq 1
"""
import argparse
import torch

import tilert_oracle as O


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--op", required=True)
    ap.add_argument("--seq", type=int, default=1)
    ap.add_argument("--dev", default="cuda:0")
    a = ap.parse_args()
    r = O.CASES[a.op](seq=a.seq, dev=a.dev)
    torch.cuda.synchronize()
    print(f"built {a.op} seq{a.seq}: rel({r.get('compare','?')})={r['rel']:.2e}")
    # the single launch ncu will profile:
    r["call"]()
    torch.cuda.synchronize()
    print("launched once")


if __name__ == "__main__":
    main()
