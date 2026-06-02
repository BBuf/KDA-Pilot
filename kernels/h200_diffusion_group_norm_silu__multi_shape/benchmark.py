#!/usr/bin/env python3
"""Benchmark harness for ``h200_diffusion_group_norm_silu__multi_shape``.

Reuses ``tests/test_correctness.py`` (make_cases / _make_inputs) and times the SGLang
baseline and (when implemented) the optimized candidate with CUDA events. Per-case
inputs and any nn.GroupNorm module are built ONCE outside the timing loop, so timing
measures only the kernel call. Writes per-shape rows + a geomean row to a CSV.

Usage (on the remote H200 container, GPU pinned via CUDA_VISIBLE_DEVICES):
  python benchmark.py --mode baseline --shapes prod --out benchmark.csv
  python benchmark.py --mode both     --shapes all  --out benchmark.csv

The candidate is skipped gracefully (NotImplementedError) until the kernel is wired.
"""

from __future__ import annotations

import argparse
import csv
import importlib.util
import math
import statistics
from pathlib import Path
from typing import Any, Callable

import torch
import torch.nn as nn

KERNEL_DIR = Path(__file__).resolve().parent


def _load_correctness():
    test_py = KERNEL_DIR / "tests" / "test_correctness.py"
    spec = importlib.util.spec_from_file_location("kda_correctness", test_py)
    assert spec and spec.loader, test_py
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def _baseline_thunk(case: dict[str, Any], C) -> Callable[[], Any]:
    from sglang.jit_kernel.diffusion.group_norm_silu import apply_group_norm_silu
    from sglang.jit_kernel.diffusion.triton.group_norm_silu import triton_group_norm_silu

    x, weight, bias = C._make_inputs(case)
    ng, eps = case["num_groups"], case["eps"]
    if case["entry"] == "apply":
        norm = nn.GroupNorm(ng, x.shape[1], eps=eps, affine=True).to(device=x.device, dtype=x.dtype)
        with torch.no_grad():
            norm.weight.copy_(weight)
            norm.bias.copy_(bias)
        act = nn.SiLU()
        return lambda: apply_group_norm_silu(x, norm, act)
    return lambda: triton_group_norm_silu(x, weight, bias, num_groups=ng, eps=eps)


def _candidate_thunk(case: dict[str, Any], C):
    """Return (thunk_or_None, selected_path). Records which dispatch path the candidate took
    (small / large / baseline_giant / baseline_unsupported) for benchmark provenance."""

    register_py = KERNEL_DIR / "src" / "register.py"
    spec = importlib.util.spec_from_file_location("kda_register_bench", register_py)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    wrapper = module.optimized_wrapper
    x, weight, bias = C._make_inputs(case)
    ng, eps = case["num_groups"], case["eps"]
    path = module.selected_path(x, weight, bias, ng) if hasattr(module, "selected_path") else "?"
    try:
        if case["entry"] == "apply":
            norm = nn.GroupNorm(ng, x.shape[1], eps=eps, affine=True).to(device=x.device, dtype=x.dtype)
            with torch.no_grad():
                norm.weight.copy_(weight)
                norm.bias.copy_(bias)
            act = nn.SiLU()
            thunk = lambda: wrapper(x, norm, act)
        else:
            thunk = lambda: wrapper(x, weight, bias, num_groups=ng, eps=eps)
        thunk()  # probe once; raises NotImplementedError if stubbed
        return thunk, path
    except NotImplementedError:
        return None, path
    except Exception as e:  # surface unexpected wiring errors but do not abort the baseline run
        print(f"  [candidate probe failed for {case['name']}: {e!r}]")
        return None, path


def _time(fn: Callable[[], Any], warmup: int, iters: int) -> list[float]:
    for _ in range(warmup):
        fn()
    torch.cuda.synchronize()
    starts = [torch.cuda.Event(enable_timing=True) for _ in range(iters)]
    ends = [torch.cuda.Event(enable_timing=True) for _ in range(iters)]
    for i in range(iters):
        starts[i].record()
        fn()
        ends[i].record()
    torch.cuda.synchronize()
    return [starts[i].elapsed_time(ends[i]) * 1e3 for i in range(iters)]  # us


def _stats(samples: list[float]) -> dict[str, float]:
    s = sorted(samples)
    n = len(s)

    def pct(p):
        return s[min(n - 1, max(0, round((n - 1) * p)))]

    return {
        "median_us": statistics.median(s),
        "mean_us": statistics.mean(s),
        "std_us": statistics.pstdev(s) if n > 1 else 0.0,
        "min_us": s[0],
        "p10_us": pct(0.10),
        "p90_us": pct(0.90),
    }


def _geomean(xs: list[float]) -> float:
    xs = [x for x in xs if math.isfinite(x) and x > 0]
    return math.exp(sum(math.log(x) for x in xs) / len(xs)) if xs else float("nan")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--mode", choices=["baseline", "both"], default="both")
    ap.add_argument("--shapes", choices=["prod", "all", "regress"], default="prod")
    ap.add_argument("--entry", choices=["triton", "apply", "all"], default="all")
    ap.add_argument("--out", default=str(KERNEL_DIR / "benchmark.csv"))
    ap.add_argument("--warmup", type=int, default=25)
    ap.add_argument("--iters", type=int, default=100)
    ap.add_argument("--version", default="baseline-sglang", help="candidate version/id for provenance")
    ap.add_argument("--host", default="", help="host for provenance")
    ap.add_argument("--gpu", default="", help="gpu id/model for provenance")
    args = ap.parse_args()

    if not torch.cuda.is_available():
        raise SystemExit("CUDA required")

    # Inference context: matches the captured diffusion-VAE callsite and is REQUIRED
    # for both the SGLang Triton baseline fast path and the candidate gate (both check
    # `not torch.is_grad_enabled()`). Without this, both fall back to eager group_norm.
    torch.set_grad_enabled(False)

    C = _load_correctness()
    cases = C.make_cases()
    if args.shapes == "prod":
        cases = [c for c in cases if c["suite"] == "prod"]
    elif args.shapes == "regress":
        cases = [c for c in cases if c["suite"].startswith("regress")]
    if args.entry != "all":
        cases = [c for c in cases if c["entry"] == args.entry]
    if not cases:
        raise SystemExit("No cases selected")

    gpu_name = torch.cuda.get_device_name(0)
    provenance = f"host={args.host} gpu={args.gpu}:{gpu_name} version={args.version} cmd='benchmark.py --mode {args.mode} --shapes {args.shapes} --entry {args.entry} --warmup {args.warmup} --iters {args.iters}'"

    speedups: list[float] = []
    rows: list[list[Any]] = []
    print("===BENCH_START===")
    print(f"cases={len(cases)} mode={args.mode} shapes={args.shapes} entry={args.entry} gpu={gpu_name}")
    for case in cases:
        b_thunk = _baseline_thunk(case, C)
        b = _stats(_time(b_thunk, args.warmup, args.iters))
        c = None
        path = ""
        speedup = float("nan")
        if args.mode == "both":
            c_thunk, path = _candidate_thunk(case, C)
            if c_thunk is not None:
                c = _stats(_time(c_thunk, args.warmup, args.iters))
                speedup = b["median_us"] / c["median_us"] if c["median_us"] > 0 else float("nan")
                speedups.append(speedup)

        def cv(k):
            return f"{c[k]:.3f}" if c else ""

        rows.append([
            case["name"], case["entry"], case["dtype"], path,
            f"{b['median_us']:.3f}", f"{b['mean_us']:.3f}", f"{b['std_us']:.3f}",
            f"{b['min_us']:.3f}", f"{b['p10_us']:.3f}", f"{b['p90_us']:.3f}",
            cv("median_us"), cv("mean_us"), cv("std_us"), cv("min_us"), cv("p10_us"), cv("p90_us"),
            f"{speedup:.4f}" if math.isfinite(speedup) else "",
            provenance,
        ])
        msg = f"{case['name']:>52s} base_med={b['median_us']:9.3f}us"
        if c:
            msg += f" cand_med={c['median_us']:9.3f}us speedup={speedup:.3f}x"
        print(msg)

    out = Path(args.out)
    write_header = not out.exists() or out.stat().st_size == 0
    with out.open("a", newline="") as f:
        w = csv.writer(f)
        if write_header:
            w.writerow(["case", "entry", "dtype", "path",
                        "base_median_us", "base_mean_us", "base_std_us", "base_min_us", "base_p10_us", "base_p90_us",
                        "cand_median_us", "cand_mean_us", "cand_std_us", "cand_min_us", "cand_p10_us", "cand_p90_us",
                        "speedup_x", "provenance"])
        w.writerows(rows)
        if args.mode == "both" and speedups:
            gm = _geomean(speedups)
            w.writerow(["GEOMEAN", args.entry, args.shapes] + [""] * 13 + [f"{gm:.4f}", provenance])
            print(f"GEOMEAN speedup ({args.shapes}/{args.entry}, n={len(speedups)}): {gm:.4f}x")
    print(f"wrote {len(rows)} rows -> {out}")
    print("===BENCH_END===")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
