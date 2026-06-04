#!/usr/bin/env python3
"""Single-shape profiling harness: run the CUDA candidate for one captured case.

Usage: python profile_one.py <case_name> [num_launches]
Used under Nsight Compute (ncu --launch-skip N --launch-count 1) to profile a
warmed launch of the candidate kernel for one representative shape bucket.
"""

from __future__ import annotations

import importlib.util
import os
import sys

import torch

KDIR = os.path.dirname(os.path.abspath(__file__))


def _load(name, rel):
    spec = importlib.util.spec_from_file_location(name, os.path.join(KDIR, rel))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def main() -> int:
    corr = _load("corr", os.path.join("tests", "test_correctness.py"))
    name = sys.argv[1]
    n = int(sys.argv[2]) if len(sys.argv) > 2 else 8
    cases = {c["name"]: c for c in corr.make_cases()}
    if name not in cases:
        raise SystemExit(f"unknown case {name}; have {sorted(cases)}")
    case = cases[name]
    out = None
    for _ in range(n):
        out = corr.candidate(case)
    torch.cuda.synchronize()
    print("profiled", name, tuple(out.shape), out.dtype)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
