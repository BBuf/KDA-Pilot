#!/usr/bin/env python3
"""Baseline-vs-candidate benchmark for ``h200_diffusion_norm_infer__multi_shape``.

Times ONLY the six captured production shapes (the performance set). For each
shape it: (1) verifies candidate correctness vs the SGLang baseline using the
dynamic FP64-referenced tolerance from ``tests/test_correctness.py`` and confirms
the CUDA fast path actually ran, then (2) times baseline and candidate with the
SAME method (warmup + per-call perf_counter + cuda sync), inputs built ONCE, the
CUDA extension warm-compiled first (JIT/build time excluded). Appends per-shape
rows + a geomean row to ``benchmark.csv`` with host/GPU/commit metadata.

Run on an idle H200 inside the container, e.g.:
  KDA_RUN_CORRECTNESS=1 CUDA_VISIBLE_DEVICES=<idle> PYTHONPATH=<sglang>/python:tests \
    KDA_HOST=ion-h200-8 KDA_GPU_ID=<idle> KDA_COMMIT=<kp_commit> python benchmark.py
"""

from __future__ import annotations

import csv
import math
import os
import statistics
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Callable

import torch

KERNEL_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(KERNEL_DIR / "tests"))

import test_correctness as T  # noqa: E402  (provides cases/build/reference/checks)


def _sync() -> None:
    if torch.cuda.is_available():
        torch.cuda.synchronize()


def _time(fn: Callable[[], Any], warmup: int, iters: int) -> list[float]:
    for _ in range(warmup):
        fn()
    _sync()
    samples = []
    for _ in range(iters):
        t0 = time.perf_counter()
        fn()
        _sync()
        samples.append((time.perf_counter() - t0) * 1e6)  # microseconds
    return samples


def _summary(samples: list[float]) -> dict[str, float]:
    o = sorted(samples)

    def pct(p: float) -> float:
        return o[min(len(o) - 1, max(0, round((len(o) - 1) * p)))]

    return dict(median=statistics.median(o), mean=statistics.mean(o),
                std=statistics.pstdev(o) if len(o) > 1 else 0.0, mn=o[0],
                p10=pct(0.10), p90=pct(0.90))


def _geom(vals: list[float]) -> float:
    v = [x for x in vals if math.isfinite(x) and x > 0]
    return math.exp(sum(math.log(x) for x in v) / len(v)) if v else float("nan")


def main() -> int:
    assert torch.cuda.is_available(), "benchmark must run on a CUDA H200"
    gpu_model = torch.cuda.get_device_name(0)
    host = os.environ.get("KDA_HOST", "unknown")
    gpu_id = os.environ.get("KDA_GPU_ID", os.environ.get("CUDA_VISIBLE_DEVICES", "?"))
    commit = os.environ.get("KDA_COMMIT", "uncommitted")
    meta = f"host={host} gpu_id={gpu_id} gpu={gpu_model} kp_commit={commit} sglang={T.install_platform_shim.__module__}"

    # Bind callables once (no per-iter module reload), warm the CUDA build.
    mod = T._load_register_module()
    mod.build()
    base_norm_infer, base_rms = T.get_baselines()

    cases = [c for c in T.make_cases() if c["kind"] == "perf"]
    rows = []
    speedups = []
    for case in cases:
        inp = T.build_inputs(case)
        if case["fn"] == "norm_infer":
            base_call = lambda: base_norm_infer(inp["x"], inp["weight"], inp["bias"], inp["eps"], inp["is_rms_norm"])
            cand_call = lambda: mod.norm_infer(inp["x"], inp["weight"], inp["bias"], inp["eps"], inp["is_rms_norm"])
        else:
            base_call = lambda: base_rms(inp["x"], inp["weight"], inp["eps"])
            cand_call = lambda: mod.triton_one_pass_rms_norm(inp["x"], inp["weight"], inp["eps"])

        # Correctness gate (candidate must match baseline within dynamic tolerance,
        # and the CUDA fast path must have run) before any timing is recorded.
        base_out = base_call()
        cand_out = cand_call()
        ref = T.reference(case, inp)
        T._check_accuracy(case, cand_out, base_out, ref)
        path = mod.last_dispatch(case["fn"])
        assert path == "cuda", f"{case['name']}: expected cuda fast path, got {path}"

        b = _summary(_time(base_call, case["warmup"], case["iters"]))
        c = _summary(_time(cand_call, case["warmup"], case["iters"]))
        sp = b["median"] / c["median"] if c["median"] > 0 else float("nan")
        speedups.append(sp)
        rows.append((case["name"], b, c, sp))
        print(f"{case['name']:42s} base={b['median']:9.3f}us cand={c['median']:9.3f}us "
              f"speedup={sp:6.3f}x  (cand p10={c['p10']:.3f} p90={c['p90']:.3f})")

    geo = _geom(speedups)
    print(f"\nGEOMEAN per-shape median-latency speedup (all 6 captured shapes): {geo:.4f}x")
    print(f"meta: {meta}")

    ts = datetime.now(timezone.utc).isoformat()
    with (KERNEL_DIR / "benchmark.csv").open("a", newline="") as f:
        w = csv.writer(f)
        for name, b, c, sp in rows:
            w.writerow([ts, "cuda_vs_sglang_baseline", name, "median_us",
                        f"{b['median']:.6f}", f"{c['median']:.6f}",
                        f"{sp:.6f}x" if math.isfinite(sp) else "",
                        (f"base[mean={b['mean']:.3f},std={b['std']:.3f},min={b['mn']:.3f},p10={b['p10']:.3f},p90={b['p90']:.3f}] "
                         f"cand[mean={c['mean']:.3f},std={c['std']:.3f},min={c['mn']:.3f},p10={c['p10']:.3f},p90={c['p90']:.3f}] {meta}")])
        w.writerow([ts, "geomean", "all_6_captured_shapes", "geomean_speedup_x", "", "",
                    f"{geo:.6f}x", meta])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
