#!/usr/bin/env python3
"""Single-kernel NCU profiling entrypoint.

Usage: KDA_PROFILE=1 python profile/prof_entry.py <case_name> [candidate|baseline]

Builds the inputs for one captured production shape, warms up (which JIT-builds
and caches the kernel with -lineinfo when KDA_PROFILE=1), asserts the CUDA route
(candidate side only), then issues a final launch for NCU to capture. Profile a
specific kernel with, e.g.:

  ncu --set full -k "rope_kernel" -s 8 -c 1 -o reports/full \
      python profile/prof_entry.py <case> candidate
  ncu --metrics gpu__time_duration.sum -s 8 -c 1 -o reports/dur \
      python profile/prof_entry.py <case> baseline

The ``baseline`` side runs the SGLang Triton public function (kernel names
``_rotary_embedding_kernel`` / ``_ltx2_split_rotary_kernel``); the ``candidate``
side runs the wrapped native kernels (``standard_rope_kernel`` /
``ltx2_split_rope_kernel``).
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
        print("usage: prof_entry.py <case_name> [candidate|baseline]", file=sys.stderr)
        return 2
    name = sys.argv[1]
    side = sys.argv[2] if len(sys.argv) > 2 else "candidate"
    if side not in ("candidate", "baseline"):
        print(f"unknown side {side!r}; use candidate|baseline", file=sys.stderr)
        return 2
    tc = _load_tests()
    cases = {c["name"]: c for c in tc.make_cases()}
    if name not in cases:
        print(f"unknown case {name!r}; have {sorted(cases)}", file=sys.stderr)
        return 2
    case = cases[name]
    run = tc.candidate if side == "candidate" else tc.baseline

    for _ in range(8):  # warmup: JIT build (+ Triton autotune for baseline) + steady state
        run(case)
        torch.cuda.synchronize()
    if side == "candidate":
        import wrapper as W  # cached module shared with the register/candidate path

        assert W._LAST_DISPATCH[case["api"]] == "cuda", f"expected CUDA route, got {W._LAST_DISPATCH}"
    # The launch(es) NCU captures (skip the warmups with `-s`):
    run(case)
    torch.cuda.synchronize()
    print(f"profiled {name}: side={side}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
