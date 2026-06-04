#!/usr/bin/env python3
"""torch.compile smoke for the in-tree drop-in (custom-op preservation check).

With whatever SGLang is on PYTHONPATH (baseline checkout or the candidate worktree),
this compiles a function that calls the public ``fused_inplace_qknorm_rope`` custom op
and checks: (1) compilation raises no error under ``fullgraph=True`` (no graph break
through the registered op), (2) the compiled in-place result matches eager within the
task tolerances, on one small and one large captured production row.

Run once per side; the candidate passes when its behavior matches the baseline side
(compiles identically, matches eager identically).

Usage:
  PYTHONPATH=<sglang>/python python compile_smoke.py <label>
"""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

KERNEL_DIR = Path(__file__).resolve().parents[2]


def _load_correctness():
    spec = importlib.util.spec_from_file_location(
        "kda_compile_smoke_corr", KERNEL_DIR / "tests" / "test_correctness.py"
    )
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def main() -> int:
    import torch

    label = sys.argv[1] if len(sys.argv) > 1 else "side"
    t = _load_correctness()
    from sglang.jit_kernel.diffusion.qknorm_rope import fused_inplace_qknorm_rope as op
    import sglang

    print(f"[{label}] sglang at {sglang.__file__}")

    def fn(q, k, qw, kw, cache, pos, is_neox, eps, head_dim, rope_dim):
        op(q, k, qw, kw, cache, pos, is_neox=is_neox, eps=eps,
           head_dim=head_dim, rope_dim=rope_dim)
        return q, k

    cases = {c["name"]: c for c in t.make_cases()}
    # Broad-staged synthetic shape: not a captured row, but inside the in-tree delegation
    # surface (bf16, head_dim=128, rope_dim=128, non-NeoX, num_tokens >= 512) — checks the
    # staged path compiles/matches beyond the captured table.
    cases["synthetic__broad__B1024_H16_D128_R128"] = {
        "name": "synthetic__broad__B1024_H16_D128_R128", "preset": "synthetic",
        "bucket": "broad", "num_tokens": 1024, "num_heads": 16, "head_dim": 128,
        "rope_dim": 128, "is_neox": False, "eps": 1e-6, "dtype": "bfloat16",
        "position_dtype": "int64", "warmup": 5, "iters": 10,
    }
    names = ["qwen__small__B19_H24_D128_R128", "qwen-edit__large__B8424_H24_D128_R128",
             "synthetic__broad__B1024_H16_D128_R128"]
    failures = 0
    for name in names:
        case = cases[name]
        eager_in = t._make_inputs(case)
        comp_in = t._make_inputs(case)  # identical seeded inputs

        fn(eager_in["q"], eager_in["k"], eager_in["q_weight"], eager_in["k_weight"],
           eager_in["cos_sin_cache"], eager_in["positions"], case["is_neox"], case["eps"],
           case["head_dim"], case["rope_dim"])

        compiled = torch.compile(fn, fullgraph=True)
        cq, ck = compiled(comp_in["q"], comp_in["k"], comp_in["q_weight"], comp_in["k_weight"],
                          comp_in["cos_sin_cache"], comp_in["positions"], case["is_neox"],
                          case["eps"], case["head_dim"], case["rope_dim"])
        torch.cuda.synchronize()

        ok = (
            not torch.isnan(cq).any() and not torch.isnan(ck).any()
            and torch.allclose(cq.float(), eager_in["q"].float(), atol=t.ATOL, rtol=t.RTOL)
            and torch.allclose(ck.float(), eager_in["k"].float(), atol=t.ATOL, rtol=t.RTOL)
        )
        failures += 0 if ok else 1
        print(f"[{label}] {name}: fullgraph compile OK, compiled-vs-eager match={ok}")

    print(f"[{label}] COMPILE_SMOKE {'PASS' if failures == 0 else 'FAIL'}")
    return 0 if failures == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
