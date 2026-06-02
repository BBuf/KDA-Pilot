#!/usr/bin/env python3
"""Single-kernel NCU profiling entrypoint.

Usage: KDA_PROFILE=1 python profile/prof_entry.py <case_name>

Builds the inputs for one captured production shape, warms up (which JIT-builds
and caches the kernel with -lineinfo when KDA_PROFILE=1), asserts the CUDA route,
then issues a final launch for NCU to capture. Profile a specific kernel with,
e.g.:  ncu --set full -k "rope_kernel" -c 1 -s 5 -o reports/full python profile/prof_entry.py <case>
"""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import torch

KDIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(KDIR / "src"))


def _load_tests():
    spec = importlib.util.spec_from_file_location("kda_tc_prof", KDIR / "tests" / "test_correctness.py")
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def main() -> int:
    if len(sys.argv) < 2:
        print("usage: prof_entry.py <case_name>", file=sys.stderr)
        return 2
    name = sys.argv[1]
    tc = _load_tests()
    cases = {c["name"]: c for c in tc.make_cases()}
    if name not in cases:
        print(f"unknown case {name!r}; have {sorted(cases)}", file=sys.stderr)
        return 2
    case = cases[name]
    import wrapper as W  # cached module shared with the register/candidate path

    for _ in range(8):  # warmup: JIT build + cache + steady state
        tc.candidate(case)
        torch.cuda.synchronize()
    assert W._LAST_DISPATCH[case["api"]] == "cuda", f"expected CUDA route, got {W._LAST_DISPATCH}"
    # The launch(es) NCU captures (skip the warmups with `-s`):
    tc.candidate(case)
    torch.cuda.synchronize()
    print(f"profiled {name}: route={W._LAST_DISPATCH[case['api']]}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
