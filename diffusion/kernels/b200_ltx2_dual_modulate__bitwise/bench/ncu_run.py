"""Reproducible NCU replay harness for b200_ltx2_dual_modulate__bitwise.

Builds a single frozen workload (selected by id from `bench/workloads.json`) through the
same `bench/adapter.py` used by the benchmark, warms the candidate once, then runs ONLY
the candidate entry point for `--iters` iterations and synchronizes. This is the exact
target meant to be profiled by Nsight Compute, e.g.:

    CUDA_VISIBLE_DEVICES=5 ncu --set basic -k regex:affine -c 1 \
      -o profile/ncu/video_s32640 \
      python bench/ncu_run.py --workload-id ltx23_hq_pr29392_stage2_video_explicit_s32640_d4096_bcast1 --iters 1

No SGLang import at runtime (the adapter asserts this).
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

_BENCH_DIR = Path(__file__).resolve().parent
if str(_BENCH_DIR) not in sys.path:
    sys.path.insert(0, str(_BENCH_DIR))

import torch

import adapter  # bench/adapter.py (same directory)


def _load_workload(workload_id: str) -> dict:
    workloads = json.loads((_BENCH_DIR / "workloads.json").read_text())
    for w in workloads:
        if str(w.get("id")) == workload_id:
            return w
    ids = ", ".join(str(w.get("id")) for w in workloads)
    raise SystemExit(f"workload id {workload_id!r} not found. Available: {ids}")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--workload-id", required=True, help="id from bench/workloads.json")
    parser.add_argument("--iters", type=int, default=1, help="candidate iterations to run")
    parser.add_argument("--device", default="cuda:0")
    parser.add_argument("--seed", type=int, default=0)
    args = parser.parse_args()

    if not torch.cuda.is_available():
        raise SystemExit("CUDA is required")
    device = torch.device(args.device)
    torch.cuda.set_device(device)
    torch.manual_seed(args.seed)
    torch.set_grad_enabled(False)

    workload = _load_workload(args.workload_id)
    case = adapter.make_case(workload, device=device, seed=args.seed)
    inputs = case["inputs"]
    outputs = case["candidate_outputs"]

    adapter.call_candidate(workload, inputs, outputs)  # warm / build
    torch.cuda.synchronize()
    for _ in range(max(1, args.iters)):
        adapter.call_candidate(workload, inputs, outputs)
    torch.cuda.synchronize()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
