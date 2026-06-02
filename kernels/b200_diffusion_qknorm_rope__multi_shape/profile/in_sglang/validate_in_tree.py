#!/usr/bin/env python3
"""In-SGLang in-tree-placement validation (the #19 AC-13 method, torch.compile-safe path).

With whatever SGLang is on PYTHONPATH, this calls SGLang's OWN public
``fused_inplace_qknorm_rope`` (a ``register_custom_op`` — torch.compile-friendly) over the 10
production shapes, checks correctness vs the split oracle, and records the median CUDA-event
latency. Run it twice — once with the CANDIDATE SGLang checkout (my candidate ``.cuh`` dropped
into ``python/sglang/jit_kernel/csrc/diffusion/qknorm_rope.cuh``) and once with the BASELINE
SGLang — and compare the medians. Because BOTH go through SGLang's identical ``register_custom_op``
wrapper, the ratio is the pure DEVICE delta (NOT a custom-op-removal artifact), and the candidate
keeps torch.compile compatibility.

Usage:
  PYTHONPATH=<sglang>/python python validate_in_tree.py measure  <out.json>
  python validate_in_tree.py compare <baseline.json> <candidate.json>
"""

from __future__ import annotations

import importlib.util
import json
import math
import statistics
import sys
from pathlib import Path

KERNEL_DIR = Path(__file__).resolve().parents[2]  # profile/in_sglang/ -> kernel folder


def _load_correctness():
    spec = importlib.util.spec_from_file_location(
        "kda_in_tree_corr", KERNEL_DIR / "tests" / "test_correctness.py"
    )
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def _measure(out_path: str) -> int:
    import torch

    t = _load_correctness()
    # SGLang's OWN public op (register_custom_op), built from whatever .cuh is in this checkout.
    from sglang.jit_kernel.diffusion.qknorm_rope import fused_inplace_qknorm_rope as op

    def call(fn, inp, case):
        fn(inp["q"], inp["k"], inp["q_weight"], inp["k_weight"], inp["cos_sin_cache"],
           inp["positions"], is_neox=case["is_neox"], eps=case["eps"],
           head_dim=case["head_dim"], rope_dim=case["rope_dim"])

    def median_us(fn, warmup, iters):
        for _ in range(warmup):
            fn()
        torch.cuda.synchronize()
        s = []
        for _ in range(iters):
            a = torch.cuda.Event(enable_timing=True)
            b = torch.cuda.Event(enable_timing=True)
            a.record(); fn(); b.record(); torch.cuda.synchronize()
            s.append(a.elapsed_time(b) * 1e3)  # ms -> us
        return statistics.median(s)

    out = {}
    for case in t.make_cases():
        # correctness: SGLang's op (in place) vs the split oracle, on identical seeded inputs
        ci = t._make_inputs(case)
        q, k = ci["q"], ci["k"]
        call(op, ci, case)
        eq, ek = t._run_oracle(t._make_inputs(case), case)
        ok = (
            not torch.isnan(q).any() and not torch.isnan(k).any()
            and torch.allclose(q.float(), eq.float(), atol=t.ATOL, rtol=t.RTOL)
            and torch.allclose(k.float(), ek.float(), atol=t.ATOL, rtol=t.RTOL)
        )
        ti = t._make_inputs(case)
        med = median_us(lambda: call(op, ti, case), int(case.get("warmup", 25)), int(case.get("iters", 100)))
        out[case["name"]] = {"oracle_ok": bool(ok), "median_us": round(med, 4),
                             "bucket": case["bucket"], "num_tokens": case["num_tokens"]}
        print(f"{case['name']:>44s}  oracle_ok={bool(ok)}  median={med:.2f}us")
    Path(out_path).write_text(json.dumps(out, indent=2))
    n_ok = sum(v["oracle_ok"] for v in out.values())
    print(f"\n[measure] {n_ok}/{len(out)} shapes oracle_ok; wrote {out_path}")
    return 0 if n_ok == len(out) else 1


def _compare(base_path: str, cand_path: str) -> int:
    base = json.loads(Path(base_path).read_text())
    cand = json.loads(Path(cand_path).read_text())
    speedups = []
    print(f"{'shape':>44s}  {'bucket':>6s}  base_us  cand_us  speedup")
    for name in base:
        b, c = base[name]["median_us"], cand[name]["median_us"]
        sp = b / c if c > 0 else float("nan")
        speedups.append(sp)
        print(f"{name:>44s}  {base[name]['bucket']:>6s}  {b:7.2f}  {c:7.2f}  {sp:.4f}x")
    if not all(cand[n]["oracle_ok"] for n in cand):
        print("WARNING: some candidate shapes failed correctness!")
    geo = math.exp(sum(math.log(s) for s in speedups) / len(speedups))
    print(f"\n[compare] in-SGLang (register_custom_op preserved) device geomean = {geo:.4f}x "
          f"over {len(speedups)} shapes")
    return 0


def main() -> int:
    if len(sys.argv) >= 3 and sys.argv[1] == "measure":
        return _measure(sys.argv[2])
    if len(sys.argv) >= 4 and sys.argv[1] == "compare":
        return _compare(sys.argv[2], sys.argv[3])
    print(__doc__)
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
