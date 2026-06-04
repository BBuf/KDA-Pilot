"""NCU profiling entry: run one unique captured signature in a tight loop.

Used as the python entrypoint under ``ncu --set full`` / ``--set source``.
Builds deterministic inputs for the selected case, runs warmup iterations
(JIT build + compile outside the profiled window when combined with
``ncu --launch-skip``), then the measured iterations.

    CUDA_VISIBLE_DEVICES=0 KDA_EXTRA_CUDA_CFLAGS=-lineinfo \
      ncu --set full --launch-skip 20 --launch-count 3 -o reports/full \
      python bench/profile_case.py --case <case_id> --impl candidate --iters 30
"""

from __future__ import annotations

import argparse
import importlib.util
import sys
from pathlib import Path

BENCH_DIR = Path(__file__).resolve().parent


def _load(name, path):
    if name in sys.modules:
        return sys.modules[name]
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--case", required=True)
    ap.add_argument("--impl", choices=["baseline", "candidate"], default="candidate")
    ap.add_argument("--iters", type=int, default=30)
    ap.add_argument("--seed", type=int, default=20260604)
    args = ap.parse_args()

    import torch

    lib = _load("kda_correctness_lib", BENCH_DIR / "correctness.py")
    sm = _load("kda_shapes", BENCH_DIR / "shapes.py")
    cases, _ = sm.load_unique_cases()
    case = next((c for c in cases if c.case_id == args.case), None)
    if case is None:
        raise SystemExit(f"unknown case id {args.case}")

    nss, srnss = lib.implementations(args.impl)
    tensors, norm_type, eps = sm.build_inputs(case, device="cuda", seed=args.seed)
    if case.sig.kernel == sm.NSS:
        x, weight, bias, scale, shift = tensors

        def call():
            return nss(x, weight, bias, scale, shift, norm_type, eps)

    else:
        residual, x, gate, weight, bias, scale, shift = tensors

        def call():
            return srnss(residual, x, gate, weight, bias, scale, shift, norm_type, eps)

    for _ in range(args.iters):
        call()
    torch.cuda.synchronize()
    print(f"profiled {args.impl} {case.case_id} x{args.iters}")


if __name__ == "__main__":
    main()
