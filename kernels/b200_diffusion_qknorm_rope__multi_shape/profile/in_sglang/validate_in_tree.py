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

    def stats_us(fn, warmup, iters):
        for _ in range(warmup):
            fn()
        torch.cuda.synchronize()
        s = []
        for _ in range(iters):
            a = torch.cuda.Event(enable_timing=True)
            b = torch.cuda.Event(enable_timing=True)
            a.record(); fn(); b.record(); torch.cuda.synchronize()
            s.append(a.elapsed_time(b) * 1e3)  # ms -> us
        s.sort()

        def pct(p):
            return s[min(len(s) - 1, max(0, round((len(s) - 1) * p)))]

        return {
            "median_us": round(statistics.median(s), 4),
            "mean_us": round(statistics.mean(s), 4),
            "std_us": round(statistics.pstdev(s) if len(s) > 1 else 0.0, 4),
            "min_us": round(s[0], 4),
            "p10_us": round(pct(0.10), 4),
            "p90_us": round(pct(0.90), 4),
        }

    import sglang as _sgl
    print(f"[measure] sglang at {_sgl.__file__}")
    out = {"_provenance": {"sglang_file": _sgl.__file__}}
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
        st = stats_us(lambda: call(op, ti, case), int(case.get("warmup", 25)), int(case.get("iters", 100)))
        out[case["name"]] = {"oracle_ok": bool(ok), "bucket": case["bucket"],
                             "num_tokens": case["num_tokens"], **st}
        print(f"{case['name']:>44s}  oracle_ok={bool(ok)}  median={st['median_us']:.2f}us  p10={st['p10_us']:.2f}  p90={st['p90_us']:.2f}")
    Path(out_path).write_text(json.dumps(out, indent=2))
    shapes = {k: v for k, v in out.items() if not k.startswith("_")}
    n_ok = sum(v["oracle_ok"] for v in shapes.values())
    print(f"\n[measure] {n_ok}/{len(shapes)} shapes oracle_ok; wrote {out_path}")
    return 0 if n_ok == len(shapes) else 1


def _shapes(d: dict) -> dict:
    return {k: v for k, v in d.items() if not k.startswith("_")}


def _compare(base_path: str, cand_path: str, check_base: str | None = None,
             check_cand: str | None = None, regress_pct: float = 3.0) -> int:
    """Compare run2 (recorded) measurements; optionally cross-check against run1.

    Promotion gate (DEC: parity-or-speedup, no material per-shape regression):
    a shape regresses MATERIALLY when cand is more than ``regress_pct``%% slower than
    base in the recorded run AND the run1 cross-check (when given) confirms a >
    ``regress_pct``%% regression on the same shape (filters one-run shared-box
    artifacts). Exit 1 on any material regression, failed correctness on EITHER side
    (a baseline-side failure means the baseline checkout/PYTHONPATH is invalid and the
    whole comparison is inadmissible), incomplete run1 cross-check coverage (when run1
    files are provided they must contain every recorded-run shape — a truncated or
    mismatched cross-check must never be able to dismiss a recorded regression), or
    geomean < 1.0.
    """
    base = _shapes(json.loads(Path(base_path).read_text()))
    cand = _shapes(json.loads(Path(cand_path).read_text()))
    run1 = None
    run1_missing: list[str] = []
    if check_base and check_cand:
        b1 = _shapes(json.loads(Path(check_base).read_text()))
        c1 = _shapes(json.loads(Path(check_cand).read_text()))
        # Fail closed: the cross-check files must cover every recorded-run shape.
        run1_missing = sorted(n for n in base if n not in b1 or n not in c1)
        run1 = {n: (b1[n]["median_us"] / c1[n]["median_us"]) for n in b1 if n in c1}
    speedups, material = [], []
    print(f"{'shape':>44s}  {'bucket':>6s}  base_us  cand_us  speedup")
    for name in base:
        b, c = base[name]["median_us"], cand[name]["median_us"]
        sp = b / c if c > 0 else float("nan")
        speedups.append(sp)
        flag = ""
        if sp < 1.0 - regress_pct / 100.0:
            r1 = None if run1 is None else run1.get(name)
            # A shape absent from the run1 files counts as CONFIRMED (fail closed) —
            # missing cross-check coverage must never dismiss a recorded regression.
            confirmed = run1 is None or r1 is None or r1 < 1.0 - regress_pct / 100.0
            if confirmed:
                material.append(name)
                flag = "  << MATERIAL REGRESSION" + (
                    " (confirmed by run1)" if run1 is not None and r1 is not None else "")
            else:
                flag = "  (regression in run2 only — not confirmed by run1)"
        print(f"{name:>44s}  {base[name]['bucket']:>6s}  {b:7.2f}  {c:7.2f}  {sp:.4f}x{flag}")
    bad_base = [n for n in base if not base[n]["oracle_ok"]]
    bad_corr = [n for n in cand if not cand[n]["oracle_ok"]]
    if run1_missing:
        print(f"FAIL: run1 cross-check files are missing shapes {run1_missing} — a "
              f"truncated/mismatched cross-check makes this comparison inadmissible")
    if bad_base:
        print(f"FAIL: BASELINE correctness failed on {bad_base} — the baseline "
              f"checkout/PYTHONPATH is invalid and this comparison is inadmissible")
    if bad_corr:
        print(f"FAIL: candidate correctness failed on {bad_corr}")
    geo = math.exp(sum(math.log(s) for s in speedups) / len(speedups))
    print(f"\n[compare] in-SGLang (register_custom_op preserved) device geomean = {geo:.4f}x "
          f"over {len(speedups)} shapes; material-regression threshold = {regress_pct:.1f}%")
    gate_ok = not material and not bad_base and not bad_corr and not run1_missing and geo >= 1.0
    print(f"[compare] PROMOTION_GATE {'PASS' if gate_ok else 'FAIL'}"
          + (f" (material regressions: {material})" if material else ""))
    return 0 if gate_ok else 1


def main() -> int:
    if len(sys.argv) >= 3 and sys.argv[1] == "measure":
        return _measure(sys.argv[2])
    if len(sys.argv) >= 4 and sys.argv[1] == "compare":
        check_base = sys.argv[4] if len(sys.argv) >= 6 else None
        check_cand = sys.argv[5] if len(sys.argv) >= 6 else None
        return _compare(sys.argv[2], sys.argv[3], check_base, check_cand)
    print(__doc__)
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
