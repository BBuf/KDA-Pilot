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


# Idleness thresholds for the selected GPU. The candidate's own CUDA context +
# JIT extension footprint is ~0.6-1.5 GiB; a contending external workload on this
# shared box is ~100+ GiB. MEM_MAX cleanly rejects any GB-scale external job while
# allowing this process's own context. UTIL_MAX rejects active external compute.
IDLE_UTIL_MAX_PCT = 5
IDLE_MEM_MAX_MIB = 2048


def _gpu_idle(gpu_id: str) -> dict:
    """Structured GPU snapshot via nvidia-smi. RAISES on failure/unparsable output
    so a missing/garbled snapshot can never be silently recorded or exported."""
    r = subprocess.run(
        ["nvidia-smi", "-i", str(gpu_id),
         "--query-gpu=utilization.gpu,memory.used,memory.total",
         "--format=csv,noheader,nounits"],
        capture_output=True, text=True, timeout=30,
    )
    if r.returncode != 0:
        raise SystemExit(f"benchmark.py: nvidia-smi -i {gpu_id} failed (rc={r.returncode}): {r.stderr.strip()}")
    vals = [x.strip() for x in r.stdout.strip().split(",")]
    if len(vals) < 3:
        raise SystemExit(f"benchmark.py: unparsable nvidia-smi output: {r.stdout!r}")
    try:
        util, mem, total = int(vals[0]), int(vals[1]), int(vals[2])
    except ValueError:
        raise SystemExit(f"benchmark.py: non-integer nvidia-smi values: {vals}")
    # Count compute processes on this GPU (informational evidence; cross-namespace
    # PIDs are unreliable to attribute, so validation uses util/mem thresholds).
    p = subprocess.run(
        ["nvidia-smi", "-i", str(gpu_id), "--query-compute-apps=pid", "--format=csv,noheader"],
        capture_output=True, text=True, timeout=30,
    )
    procs = len([ln for ln in p.stdout.strip().splitlines() if ln.strip()]) if p.returncode == 0 else -1
    return {"util": util, "mem": mem, "total": total, "procs": procs,
            "raw": f"util={util}% mem_used={mem}MiB procs={procs}"}


def _validate_idle(label: str, d: dict) -> None:
    """Abort (no CSV row written / no export) if the GPU is not idle for this snapshot."""
    if d["util"] > IDLE_UTIL_MAX_PCT or d["mem"] > IDLE_MEM_MAX_MIB:
        raise SystemExit(
            f"benchmark.py: GPU NOT idle {label} ({d['raw']}); thresholds "
            f"util<={IDLE_UTIL_MAX_PCT}% mem<={IDLE_MEM_MAX_MIB}MiB. Discarding run "
            f"(no benchmark.csv row written, nothing to export). Re-run on an idle GPU."
        )


def main() -> int:
    assert torch.cuda.is_available(), "benchmark must run on a CUDA H200"
    gpu_model = torch.cuda.get_device_name(0)
    host = _require_env("KDA_HOST")
    gpu_id = _require_env("KDA_GPU_ID")
    commit = _require_env("KDA_COMMIT")
    cmd = _require_env("KDA_CMD")
    idle_before = _gpu_idle(gpu_id)  # snapshot BEFORE warm build / timing
    _validate_idle("before", idle_before)  # abort early if another job is resident

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

    # Release this process's own tensors, then settle, so the after-snapshot reflects
    # the card (this process's residual ~ CUDA context only) rather than its own
    # just-finished work or retained allocations.
    inp = base_call = cand_call = base_out = cand_out = ref = None  # drop tensor refs
    _sync()
    torch.cuda.empty_cache()
    time.sleep(2.0)
    idle_after = _gpu_idle(gpu_id)  # snapshot AFTER all timing + free + settle
    _validate_idle("after", idle_after)  # abort (no CSV row) if a job is resident now
    geo = _geom(speedups)
    meta = (f"host={host} gpu_id={gpu_id} gpu={gpu_model} kp_commit={commit} "
            f"idle_before=[{idle_before['raw']}] idle_after=[{idle_after['raw']}] cmd=\"{cmd}\"")
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
