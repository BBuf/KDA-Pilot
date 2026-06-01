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
import subprocess
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


def _require_env(name: str) -> str:
    """Fail fast on missing benchmark metadata so an under-documented row can never
    become the exported KDA_SPEEDUP stamp (round-1 review requirement)."""
    v = os.environ.get(name, "").strip()
    if not v:
        raise SystemExit(
            f"benchmark.py: required metadata env {name} is missing/empty; refusing "
            f"to write under-documented benchmark evidence. Set KDA_COMMIT, KDA_HOST, "
            f"KDA_GPU_ID, KDA_CMD."
        )
    return v


def _gpu_idle(gpu_id: str) -> str:
    """Snapshot the selected GPU's util/mem via nvidia-smi (recorded before+after timing)."""
    try:
        r = subprocess.run(
            ["nvidia-smi", "-i", str(gpu_id),
             "--query-gpu=utilization.gpu,memory.used,memory.total",
             "--format=csv,noheader,nounits"],
            capture_output=True, text=True, timeout=30,
        )
        vals = [x.strip() for x in r.stdout.strip().split(",")]
        if len(vals) >= 3:
            return f"util={vals[0]}% mem_used={vals[1]}MiB mem_total={vals[2]}MiB"
        return r.stdout.strip() or f"nvidia-smi_rc={r.returncode}"
    except Exception as exc:  # noqa: BLE001
        return f"unavailable({type(exc).__name__})"


def main() -> int:
    assert torch.cuda.is_available(), "benchmark must run on a CUDA H200"
    gpu_model = torch.cuda.get_device_name(0)
    host = _require_env("KDA_HOST")
    gpu_id = _require_env("KDA_GPU_ID")
    commit = _require_env("KDA_COMMIT")
    cmd = _require_env("KDA_CMD")
    idle_before = _gpu_idle(gpu_id)  # snapshot BEFORE warm build / timing

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

    # Settle so the rolling nvidia-smi util window and memory reflect the idle card
    # (not this process's own just-finished work) before the after-snapshot.
    _sync()
    torch.cuda.empty_cache()
    time.sleep(2.0)
    idle_after = _gpu_idle(gpu_id)  # snapshot AFTER all timing + settle
    geo = _geom(speedups)
    meta = (f"host={host} gpu_id={gpu_id} gpu={gpu_model} kp_commit={commit} "
            f"idle_before=[{idle_before}] idle_after=[{idle_after}] cmd=\"{cmd}\"")
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
