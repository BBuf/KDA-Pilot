#!/usr/bin/env python3
"""Isolated benchmark for ``b200_diffusion_qknorm_rope__multi_shape``.

Times the **current SGLang fused baseline** (`fused_inplace_qknorm_rope`, the
kernel this task must beat) against the registered candidate, on a verified-idle
NVIDIA B200, and appends a structured row per shape to ``benchmark.csv``.

The split-path oracle (`fused_inplace_qknorm` + FlashInfer RoPE) is the
*correctness* reference (see ``tests/test_correctness.py``); it is NOT the
benchmark baseline. While the candidate still routes to the fused baseline (the
fallback scaffold), every production-row speedup must measure ~1.0x.

Timing methodology (matches SGLang's ``run_benchmark_no_cudagraph`` intent):
- CUDA-event timing (NOT host ``time.perf_counter``), no CUDA graph capture.
- Inputs built ONCE per case; the in-place op is timed repeatedly (RMS-norm +
  RoPE is magnitude-stable under repetition).
- Reports median/mean/std/min/p10/p90 per shape (microseconds) and an
  equal-weight geomean of per-shape median-latency speedups over the production
  rows. ``KDA_BENCH_INNER`` (default 1) averages that many back-to-back calls per
  recorded sample to amortize event overhead on the smallest shapes.

Usage (inside sglang_bbuf on ion-b200):
  CUDA_VISIBLE_DEVICES=<idle> python benchmark.py            # freeze all rows
  CUDA_VISIBLE_DEVICES=<idle> python benchmark.py --sanity   # quick ~1.0x check
"""

from __future__ import annotations

import csv
import importlib.util
import math
import os
import socket
import statistics
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Callable

try:
    import torch
except ImportError:  # pragma: no cover
    torch = None


KERNEL_SLUG = "b200_diffusion_qknorm_rope__multi_shape"
KERNEL_DIR = Path(__file__).resolve().parent

CSV_COLUMNS = [
    "timestamp", "preset", "bucket", "name",
    "num_tokens", "num_heads", "head_dim", "rope_dim", "is_neox", "eps",
    "dtype", "position_dtype", "ci_fallback",
    "baseline_median_us", "baseline_mean_us", "baseline_std_us",
    "baseline_min_us", "baseline_p10_us", "baseline_p90_us",
    "cand_median_us", "cand_mean_us", "cand_std_us",
    "cand_min_us", "cand_p10_us", "cand_p90_us",
    "speedup_x", "iters", "inner",
    "command", "git_commit", "candidate_source_version",
    "host", "gpu_index", "gpu_name", "cuda_visible_devices",
    "idle_before", "idle_after",
]


def _load_module(rel_path: str, mod_name: str):
    path = KERNEL_DIR / rel_path
    spec = importlib.util.spec_from_file_location(mod_name, path)
    assert spec is not None and spec.loader is not None, path
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def _git(*args: str) -> str:
    try:
        return subprocess.check_output(["git", *args], cwd=str(KERNEL_DIR), stderr=subprocess.DEVNULL).decode().strip()
    except Exception:
        return "unknown"


def _candidate_source_version() -> str:
    """git commit + dirty flag for src/register.py (the candidate seam)."""
    commit = _git("rev-parse", "--short", "HEAD")
    dirty = _git("status", "--porcelain", "--", "src/register.py")
    return f"{commit}{'+dirty' if dirty else ''}"


def _nvidia_smi_snapshot() -> str:
    """Compact per-GPU util/mem snapshot; '' if nvidia-smi is unavailable."""
    try:
        out = subprocess.check_output(
            ["nvidia-smi", "--query-gpu=index,utilization.gpu,memory.used,memory.total",
             "--format=csv,noheader,nounits"],
            stderr=subprocess.DEVNULL,
        ).decode().strip()
        return " | ".join(line.strip().replace(",", " ") for line in out.splitlines())
    except Exception:
        return "unavailable"


def _time_cuda_events(fn: Callable[[], Any], *, warmup: int, iters: int, inner: int) -> list[float]:
    """Per-sample latencies in microseconds using CUDA events."""
    for _ in range(warmup):
        fn()
    torch.cuda.synchronize()

    samples: list[float] = []
    for _ in range(iters):
        start = torch.cuda.Event(enable_timing=True)
        end = torch.cuda.Event(enable_timing=True)
        start.record()
        for _ in range(inner):
            fn()
        end.record()
        torch.cuda.synchronize()
        samples.append((start.elapsed_time(end) * 1e3) / inner)  # ms -> us, per call
    return samples


def _summary(samples: list[float]) -> dict[str, float]:
    ordered = sorted(samples)

    def pct(p: float) -> float:
        index = min(len(ordered) - 1, max(0, round((len(ordered) - 1) * p)))
        return ordered[index]

    return {
        "median": statistics.median(ordered),
        "mean": statistics.mean(ordered),
        "std": statistics.pstdev(ordered) if len(ordered) > 1 else 0.0,
        "min": ordered[0],
        "p10": pct(0.10),
        "p90": pct(0.90),
    }


def _geom_mean(values: list[float]) -> float:
    """Geometric mean; hard-errors on any missing/invalid/nonpositive value."""
    if not values:
        raise ValueError("geom_mean: no production speedups to aggregate")
    for v in values:
        if not math.isfinite(v) or v <= 0:
            raise ValueError(f"geom_mean: invalid speedup {v!r}; refusing to aggregate a broken run")
    return math.exp(sum(math.log(v) for v in values) / len(values))


def _fused_baseline_runner():
    """Resolve the current SGLang fused baseline (the kernel to beat)."""
    from sglang.jit_kernel.diffusion.qknorm_rope import fused_inplace_qknorm_rope
    return fused_inplace_qknorm_rope


def _make_call(fn, inputs: dict, case: dict) -> Callable[[], None]:
    def call() -> None:
        fn(
            inputs["q"], inputs["k"], inputs["q_weight"], inputs["k_weight"],
            inputs["cos_sin_cache"], inputs["positions"],
            is_neox=case["is_neox"], eps=case["eps"],
            head_dim=case["head_dim"], rope_dim=case["rope_dim"],
        )
    return call


def _bench_case(correctness, case, baseline_fn, candidate_fn, *, inner: int) -> tuple[dict, dict, float]:
    warmup = int(case.get("warmup", 25))
    iters = int(case.get("iters", 100))

    base_inputs = correctness._make_inputs(case)
    cand_inputs = correctness._make_inputs(case)
    b = _summary(_time_cuda_events(_make_call(baseline_fn, base_inputs, case), warmup=warmup, iters=iters, inner=inner))
    c = _summary(_time_cuda_events(_make_call(candidate_fn, cand_inputs, case), warmup=warmup, iters=iters, inner=inner))
    speedup = (b["median"] / c["median"]) if c["median"] > 0 else float("nan")
    return b, c, speedup


def main() -> int:
    if torch is None or not torch.cuda.is_available():
        raise SystemExit("CUDA is required. Run inside the sglang_bbuf container on ion-b200.")

    sanity = "--sanity" in sys.argv
    correctness = _load_module("tests/test_correctness.py", "kda_correctness")
    register = _load_module("src/register.py", "kda_register")
    candidate_fn = getattr(register, "optimized_wrapper")
    baseline_fn = _fused_baseline_runner()

    cases = correctness.make_cases()
    cases = [c for c in cases if not c.get("ci_fallback")]  # production rows only for perf
    if not cases:
        raise SystemExit("No production benchmark cases.")

    inner = int(os.environ.get("KDA_BENCH_INNER", "1"))

    if sanity:
        for case in cases[:3]:
            case = {**case, "warmup": 10, "iters": 30}
            _b, _c, sp = _bench_case(correctness, case, baseline_fn, candidate_fn, inner=inner)
            print(f"[sanity] {case['name']:>44s}  candidate/fused-baseline speedup={sp:.4f}x "
                  f"(expect ~1.0x while candidate routes to baseline)")
        return 0

    command = "python " + " ".join(sys.argv)
    git_commit = _git("rev-parse", "HEAD")
    cand_ver = _candidate_source_version()
    host = socket.gethostname()
    gpu_index = os.environ.get("CUDA_VISIBLE_DEVICES", "unset")
    gpu_name = torch.cuda.get_device_name(0)
    cvd = os.environ.get("CUDA_VISIBLE_DEVICES", "unset")
    idle_before = _nvidia_smi_snapshot()

    csv_path = KERNEL_DIR / "benchmark.csv"
    write_header = (not csv_path.exists()) or csv_path.stat().st_size == 0

    speedups: list[float] = []
    rows: list[list[Any]] = []
    for case in cases:
        b, c, speedup = _bench_case(correctness, case, baseline_fn, candidate_fn, inner=inner)
        speedups.append(speedup)
        rows.append([
            datetime.now(timezone.utc).isoformat(), case.get("preset"), case.get("bucket"), case["name"],
            case["num_tokens"], case["num_heads"], case["head_dim"], case["rope_dim"], case["is_neox"], case["eps"],
            case["dtype"], case["position_dtype"], case.get("ci_fallback", False),
            f"{b['median']:.4f}", f"{b['mean']:.4f}", f"{b['std']:.4f}", f"{b['min']:.4f}", f"{b['p10']:.4f}", f"{b['p90']:.4f}",
            f"{c['median']:.4f}", f"{c['mean']:.4f}", f"{c['std']:.4f}", f"{c['min']:.4f}", f"{c['p10']:.4f}", f"{c['p90']:.4f}",
            f"{speedup:.4f}", case.get("iters", 100), inner,
            command, git_commit, cand_ver, host, gpu_index, gpu_name, cvd, idle_before, "",  # idle_after filled below
        ])
        print(f"{case['name']:>44s}  speedup={speedup:.4f}x  fused_baseline={b['median']:.3f}us  cand={c['median']:.3f}us")

    idle_after = _nvidia_smi_snapshot()
    for r in rows:
        r[-1] = idle_after

    geomean = _geom_mean(speedups)  # hard-errors if any row is invalid

    with csv_path.open("a", newline="") as f:
        writer = csv.writer(f)
        if write_header:
            writer.writerow(CSV_COLUMNS)
        writer.writerows(rows)
        summary_row = [""] * len(CSV_COLUMNS)
        summary_row[CSV_COLUMNS.index("name")] = "GEOMEAN_production"
        summary_row[CSV_COLUMNS.index("speedup_x")] = f"{geomean:.4f}"
        summary_row[CSV_COLUMNS.index("command")] = command
        summary_row[CSV_COLUMNS.index("git_commit")] = git_commit
        summary_row[CSV_COLUMNS.index("candidate_source_version")] = cand_ver
        summary_row[CSV_COLUMNS.index("host")] = host
        summary_row[CSV_COLUMNS.index("gpu_name")] = gpu_name
        summary_row[CSV_COLUMNS.index("cuda_visible_devices")] = cvd
        writer.writerow(summary_row)

    print(f"\nproduction geomean speedup = {geomean:.4f}x over {len(speedups)} shapes  (gpu={gpu_name} id={gpu_index})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
