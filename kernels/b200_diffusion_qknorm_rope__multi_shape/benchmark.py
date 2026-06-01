#!/usr/bin/env python3
"""Isolated benchmark for ``b200_diffusion_qknorm_rope__multi_shape``.

Reuses the cases and input generator from ``tests/test_correctness.py`` and
times the SGLang split-path oracle (baseline) against the registered candidate
on a verified-idle NVIDIA B200, then appends summary rows to ``benchmark.csv``.

Timing methodology (matches SGLang's ``run_benchmark_no_cudagraph`` intent):
- CUDA-event timing (NOT host ``time.perf_counter``), no CUDA graph capture.
- Inputs are built ONCE per case; the in-place op is then timed repeatedly
  (RMS-norm + RoPE is magnitude-stable under repetition).
- Reports median / mean / std / min / p10 / p90 per shape (microseconds) plus an
  equal-weight geomean of per-shape median-latency speedups.
- ``KDA_BENCH_INNER`` (default 1) averages that many back-to-back op calls per
  recorded sample to amortize event overhead on the smallest shapes.

Run on the remote box, e.g.:
  CUDA_VISIBLE_DEVICES=<idle> python benchmark.py
"""

from __future__ import annotations

import csv
import importlib.util
import math
import os
import statistics
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Callable

try:
    import torch
except ImportError:  # pragma: no cover
    torch = None


KERNEL_SLUG = "b200_diffusion_qknorm_rope__multi_shape"
KERNEL_DIR = Path(__file__).resolve().parent


def _load_module(rel_path: str, mod_name: str):
    path = KERNEL_DIR / rel_path
    spec = importlib.util.spec_from_file_location(mod_name, path)
    assert spec is not None and spec.loader is not None, path
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def _time_cuda_events(fn: Callable[[], Any], *, warmup: int, iters: int, inner: int) -> list[float]:
    """Return per-sample latencies in microseconds using CUDA events."""
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
        "median_us": statistics.median(ordered),
        "mean_us": statistics.mean(ordered),
        "std_us": statistics.pstdev(ordered) if len(ordered) > 1 else 0.0,
        "min_us": ordered[0],
        "p10_us": pct(0.10),
        "p90_us": pct(0.90),
    }


def _geom_mean(values: list[float]) -> float:
    cleaned = [v for v in values if math.isfinite(v) and v > 0]
    if not cleaned:
        return float("nan")
    return math.exp(sum(math.log(v) for v in cleaned) / len(cleaned))


def _provenance() -> str:
    dev = torch.cuda.get_device_name(0) if torch.cuda.is_available() else "no-cuda"
    visible = os.environ.get("CUDA_VISIBLE_DEVICES", "unset")
    return f"gpu={dev} CUDA_VISIBLE_DEVICES={visible} slug={KERNEL_SLUG}"


def main() -> int:
    if torch is None or not torch.cuda.is_available():
        raise SystemExit("CUDA is required. Run inside the sglang_bbuf container on ion-b200.")

    correctness = _load_module("tests/test_correctness.py", "kda_correctness")
    register = _load_module("src/register.py", "kda_register")
    wrapper = getattr(register, "optimized_wrapper")

    cases = correctness.make_cases()
    if not cases:
        raise SystemExit("No benchmark cases. Fill tests/test_correctness.py first.")

    inner = int(os.environ.get("KDA_BENCH_INNER", "1"))
    speedups: list[float] = []
    csv_path = KERNEL_DIR / "benchmark.csv"
    prov = _provenance()

    with csv_path.open("a", newline="") as f:
        writer = csv.writer(f)
        for case in cases:
            warmup = int(case.get("warmup", 25))
            iters = int(case.get("iters", 100))

            base_inputs = correctness._make_inputs(case)

            def run_baseline() -> None:
                correctness._run_oracle(base_inputs, case)

            cand_inputs = correctness._make_inputs(case)

            def run_candidate() -> None:
                wrapper(
                    cand_inputs["q"],
                    cand_inputs["k"],
                    cand_inputs["q_weight"],
                    cand_inputs["k_weight"],
                    cand_inputs["cos_sin_cache"],
                    cand_inputs["positions"],
                    is_neox=case["is_neox"],
                    eps=case["eps"],
                    head_dim=case["head_dim"],
                    rope_dim=case["rope_dim"],
                )

            b = _summary(_time_cuda_events(run_baseline, warmup=warmup, iters=iters, inner=inner))
            c = _summary(_time_cuda_events(run_candidate, warmup=warmup, iters=iters, inner=inner))
            speedup = (b["median_us"] / c["median_us"]) if c["median_us"] > 0 else float("nan")
            speedups.append(speedup)

            now = datetime.now(timezone.utc).isoformat()
            writer.writerow([
                now,
                case.get("preset", "?"),
                case["name"],
                "median_us",
                f"{b['median_us']:.4f}",
                f"{c['median_us']:.4f}",
                f"{speedup:.4f}x" if math.isfinite(speedup) else "",
                (
                    f"bucket={case.get('bucket')} ci_fallback={case.get('ci_fallback')} "
                    f"base[mean={b['mean_us']:.3f} std={b['std_us']:.3f} min={b['min_us']:.3f} "
                    f"p10={b['p10_us']:.3f} p90={b['p90_us']:.3f}] "
                    f"cand[mean={c['mean_us']:.3f} std={c['std_us']:.3f} min={c['min_us']:.3f} "
                    f"p10={c['p10_us']:.3f} p90={c['p90_us']:.3f}] "
                    f"iters={iters} inner={inner} {prov}"
                ),
            ])
            print(f"{case['name']:>48s}  speedup={speedup:.4f}x  base={b['median_us']:.3f}us  cand={c['median_us']:.3f}us")

        production = [s for s, case in zip(speedups, cases) if not case.get("ci_fallback")]
        writer.writerow([
            datetime.now(timezone.utc).isoformat(),
            "geomean",
            "production_shapes",
            "geomean_speedup_x",
            "",
            "",
            f"{_geom_mean(production):.4f}x",
            f"n={len(production)} {prov}",
        ])
        print(f"\nproduction geomean speedup = {_geom_mean(production):.4f}x over {len(production)} shapes")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
