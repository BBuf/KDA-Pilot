#!/usr/bin/env python3
"""Single-workload kernel driver for Nsight Compute capture.

Builds the tensors for one workload row from bench/workloads.json (same
construction path as the benchmark) and launches one side a fixed number of
times, so `ncu` can attach and capture the kernels in isolation:

    CUDA_VISIBLE_DEVICES=$REMOTE_GPU_ID ncu --set full --target-processes all \
        -o report python bench/profile_one.py --id hunyuanvideo_s27030_c3072_bcast2d \
        --side candidate --iters 5

Profiling-only tool; benchmark timing never goes through this file.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

import torch

_BENCH_DIR = Path(__file__).resolve().parent
_TASK_ROOT = _BENCH_DIR.parent
if str(_TASK_ROOT) not in sys.path:
    sys.path.insert(0, str(_TASK_ROOT))

import bench.adapter as adapter  # noqa: E402


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--id", required=True)
    parser.add_argument("--side", choices=("baseline", "candidate"), default="candidate")
    parser.add_argument("--iters", type=int, default=5)
    parser.add_argument("--device", default="cuda:0")
    args = parser.parse_args()

    device = torch.device(args.device)
    torch.cuda.set_device(device)
    torch.set_grad_enabled(False)

    rows = json.loads((_BENCH_DIR / "workloads.json").read_text())
    spec = next((r for r in rows if r["id"] == args.id), None)
    if spec is None:
        print(f"unknown workload id {args.id!r}", file=sys.stderr)
        return 2

    torch.manual_seed(spec.get("seed", 0))
    torch.cuda.manual_seed_all(spec.get("seed", 0))
    case = adapter.make_case(spec, device=device, seed=spec.get("seed", 0))
    call = adapter.call_baseline if args.side == "baseline" else adapter.call_candidate
    outputs = case["baseline_outputs"] if args.side == "baseline" else case["candidate_outputs"]

    # one warmup (JIT/caches), then the captured launches
    call(spec, case["inputs"], outputs)
    torch.cuda.synchronize()
    for _ in range(args.iters):
        call(spec, case["inputs"], outputs)
    torch.cuda.synchronize()
    print(f"profiled {args.side} of {args.id}: {args.iters} launches")
    return 0


if __name__ == "__main__":
    sys.exit(main())
