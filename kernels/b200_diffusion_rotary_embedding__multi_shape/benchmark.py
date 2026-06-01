#!/usr/bin/env python3
"""Benchmark harness for ``b200_diffusion_rotary_embedding__multi_shape``.

Uses **CUDA-event single-call timing** (records the kernel launch + execution per
sample, the latency-relevant metric for these bandwidth/launch-bound RoPE kernels)
with warmup that EXCLUDES Triton JIT/autotune and the CUDA-extension JIT build.
Reuses the case builders from ``tests/test_correctness.py``. Both wrapped entry
points are out-of-place (verified in interface.md), so inputs are not mutated.

Round 0 recorded IMMUTABLE BASELINE numbers (``--baseline-only``). With the native
CUDA candidate present, it also times the candidate (asserting the CUDA fast path
actually ran for production signatures) and reports per-shape speedup + geomean.

Evidence integrity:
- Candidate is treated as absent ONLY under ``--baseline-only``; any other candidate
  import/build/exec error FAILS the run (never silently downgrades to baseline-only).
- For production signatures the candidate MUST take the CUDA path (`_LAST_DISPATCH`),
  else the run fails (a silent fallback would invalidate the speedup claim).
- Provenance (host/GPU id/model/idle-before/idle-after/commit/cmd/REMOTE_KDA_DIR) is
  written into every CSV row, captured before AND after the timed work.

Usage (inside sglang_bbuf on an idle B200):
    CUDA_VISIBLE_DEVICES=<id> python benchmark.py [--warmup 50] [--iters 300] [--baseline-only]
"""

from __future__ import annotations

import argparse
import csv
import importlib.util
import math
import os
import statistics
import subprocess
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Callable, Optional

import torch

KERNEL_SLUG = "b200_diffusion_rotary_embedding__multi_shape"
KERNEL_DIR = Path(__file__).resolve().parent


def _load(name: str, relpath: str):
    path = KERNEL_DIR / relpath
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec is not None and spec.loader is not None, path
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def _make_callables(tc, wrapper, case: dict[str, Any], inp: dict[str, Any], baseline_only: bool):
    """Return (baseline_call, candidate_call_or_None) bound to fixed inputs.

    Candidate is None only when baseline_only is set; otherwise any failure raises.
    """
    if case["kind"] == "standard":
        b = tc._sglang_standard()
        baseline_call = lambda: b(inp["x"], inp["cos"], inp["sin"], inp["interleaved"])
        cand_fn = lambda: wrapper.apply_rotary_embedding(inp["x"], inp["cos"], inp["sin"], inp["interleaved"])
        which = "standard"
    else:
        b = tc._sglang_ltx2()
        baseline_call = lambda: b(inp["x"], inp["cos"], inp["sin"])
        cand_fn = lambda: wrapper.apply_ltx2_split_rotary_emb(inp["x"], inp["cos"], inp["sin"])
        which = "ltx2"
    if baseline_only:
        return baseline_call, None
    cand_fn()  # probe (build + run); any error propagates and fails the run
    if case.get("optimization") and wrapper.last_dispatch_path(which) != "cuda":
        raise RuntimeError(
            f"{case['name']}: candidate did NOT take the cuda path "
            f"(got {wrapper.last_dispatch_path(which)}); refusing to report a fallback as a candidate"
        )
    return baseline_call, cand_fn


def _time_cuda_events(fn: Callable[[], Any], warmup: int, iters: int) -> dict[str, float]:
    for _ in range(warmup):  # excludes Triton JIT/autotune + extension build
        fn()
    torch.cuda.synchronize()
    start = torch.cuda.Event(enable_timing=True)
    end = torch.cuda.Event(enable_timing=True)
    samples = []
    for _ in range(iters):
        start.record()
        fn()
        end.record()
        torch.cuda.synchronize()
        samples.append(start.elapsed_time(end) * 1e3)  # ms -> us
    return _summary(samples)


def _summary(samples: list[float]) -> dict[str, float]:
    ordered = sorted(samples)

    def pct(p: float) -> float:
        idx = min(len(ordered) - 1, max(0, round((len(ordered) - 1) * p)))
        return ordered[idx]

    return {
        "median_us": statistics.median(ordered), "mean_us": statistics.mean(ordered),
        "std_us": statistics.pstdev(ordered) if len(ordered) > 1 else 0.0,
        "min_us": ordered[0], "p10_us": pct(0.10), "p90_us": pct(0.90),
    }


def _geomean(values: list[float]) -> float:
    cleaned = [v for v in values if math.isfinite(v) and v > 0]
    return math.exp(sum(math.log(v) for v in cleaned) / len(cleaned)) if cleaned else float("nan")


_IDLE_UTIL_MAX = 10.0   # percent; compute-idle threshold
_IDLE_MEM_MAX = 2000.0  # MB; "no other process" threshold (checked only BEFORE our own context)


def _parse_idle(gpu_id: str):
    out = subprocess.run(
        ["nvidia-smi", "-i", str(gpu_id),
         "--query-gpu=utilization.gpu,memory.used", "--format=csv,noheader,nounits"],
        capture_output=True, text=True, timeout=20,
    ).stdout.strip()
    parts = [p.strip() for p in out.replace("\n", " ").split(",")]
    return float(parts[0]), float(parts[1]), out  # util%, mem MB, raw


def _gate_idle_before(gpu_id: Optional[str]) -> str:
    """Hard-fail if the selected GPU is not idle (another process / busy) before timing."""
    if not gpu_id:
        return "n/a (KDA_GPU_ID unset)"
    util, mem, raw = _parse_idle(gpu_id)
    if util > _IDLE_UTIL_MAX or mem > _IDLE_MEM_MAX:
        raise RuntimeError(
            f"GPU {gpu_id} NOT idle before timing (util={util}% mem={mem}MB > "
            f"{_IDLE_UTIL_MAX}%/{_IDLE_MEM_MAX}MB); refusing to record measurements on a busy GPU"
        )
    return raw


def _settle_idle_after(gpu_id: Optional[str], timeout_s: int = 20) -> str:
    """Wait for the GPU compute to drain to idle (util ~0) after timing; fail if it never settles.

    Memory is NOT gated here: our own live CUDA context legitimately holds memory until exit.
    """
    if not gpu_id:
        return "n/a (KDA_GPU_ID unset)"
    last = ""
    for _ in range(timeout_s):
        util, mem, raw = _parse_idle(gpu_id)
        last = raw
        if util <= _IDLE_UTIL_MAX:
            return raw
        time.sleep(1)
    raise RuntimeError(f"GPU {gpu_id} did not settle to idle after timing (last={last})")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--warmup", type=int, default=50)
    ap.add_argument("--iters", type=int, default=300)
    ap.add_argument("--baseline-only", action="store_true")
    args = ap.parse_args()

    gpu_id = os.environ.get("KDA_GPU_ID")
    idle_before = _gate_idle_before(gpu_id)  # FIRST, before any CUDA/torch context init
    assert torch.cuda.is_available(), "needs CUDA"
    tc = _load("kda_rope_correctness", "tests/test_correctness.py")
    wrapper = _load("kda_rope_wrapper", "src/wrapper.py") if not args.baseline_only else None
    cases = [c for c in tc.make_cases() if c.get("optimization")]

    gpu_model = os.environ.get("KDA_GPU_MODEL") or torch.cuda.get_device_name(0)
    base_prov = (
        f"host={os.environ.get('KDA_HOST','?')} gpu_id={gpu_id or '?'} gpu={gpu_model} "
        f"sglang_commit={os.environ.get('KDA_SGLANG_COMMIT','?')} "
        f"candidate_source={os.environ.get('KDA_CANDIDATE_SOURCE','src/csrc/rotary_embedding_kernel.cu')} "
        f"kp_commit={os.environ.get('KDA_KP_COMMIT','?')} "
        f"remote_kda_dir={os.environ.get('KDA_REMOTE_KDA_DIR','?')} "
        f"idle_before=[{idle_before}] "
        f"warmup={args.warmup} iters={args.iters} timing=cuda_event_single_call "
        f"cmd={os.environ.get('KDA_CMD','?')}"
    )

    # ---- time everything first (so idle_after is captured post-work for every row) ----
    results = []
    speedups = []
    for case in cases:
        inp = case["build"]()
        base_call, cand_call = _make_callables(tc, wrapper, case, inp, args.baseline_only)
        b = _time_cuda_events(base_call, args.warmup, args.iters)
        c = _time_cuda_events(cand_call, args.warmup, args.iters) if cand_call else None
        speedup = (b["median_us"] / c["median_us"]) if c and c["median_us"] > 0 else float("nan")
        if c:
            speedups.append(speedup)
        results.append((case, b, c, speedup))
        line = f"{case['name']:<34} baseline_median={b['median_us']:.3f}us"
        line += f" cand_median={c['median_us']:.3f}us speedup={speedup:.4f}x" if c else " (baseline-only)"
        print(line, flush=True)
    idle_after = _settle_idle_after(gpu_id)  # wait for compute to drain to idle (fail if it never does)
    if speedups:
        print(f"# geomean speedup (unique signatures) = {_geomean(speedups):.4f}x over {len(speedups)} shapes")

    # ---- write rows with full provenance (incl. settled idle_after) ----
    prov = base_prov + f" idle_after=[{idle_after}](util-gated; mem incl. own live context)"
    csv_path = KERNEL_DIR / "benchmark.csv"
    new = (not csv_path.exists()) or csv_path.stat().st_size == 0
    with csv_path.open("a", newline="") as f:
        w = csv.writer(f)
        if new:
            w.writerow(["timestamp_utc", "kind", "shape", "metric", "baseline_us", "candidate_us", "speedup_x", "notes"])
        for case, b, c, speedup in results:
            note = (f"{prov} baseline_mean={b['mean_us']:.3f} baseline_std={b['std_us']:.3f} "
                    f"baseline_min={b['min_us']:.3f} baseline_p10={b['p10_us']:.3f} baseline_p90={b['p90_us']:.3f}")
            if c:
                note += (f" cand_mean={c['mean_us']:.3f} cand_std={c['std_us']:.3f} cand_min={c['min_us']:.3f} "
                         f"cand_p10={c['p10_us']:.3f} cand_p90={c['p90_us']:.3f}")
            w.writerow([
                datetime.now(timezone.utc).isoformat(), case["kind"], case["name"], "median_us",
                f"{b['median_us']:.4f}", f"{c['median_us']:.4f}" if c else "",
                f"{speedup:.4f}" if c else "", note,
            ])
        if speedups:
            w.writerow([datetime.now(timezone.utc).isoformat(), "geomean", "all_unique_signatures",
                        "geomean_speedup_x", "", "", f"{_geomean(speedups):.4f}", f"{prov} n={len(speedups)}"])
    print(f"# wrote {len(cases)} rows to {csv_path}; idle_after={idle_after}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
