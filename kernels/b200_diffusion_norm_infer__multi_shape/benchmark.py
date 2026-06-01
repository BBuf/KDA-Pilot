#!/usr/bin/env python3
"""Schema-compliant benchmark for ``b200_diffusion_norm_infer__multi_shape``.

Times the SGLang baseline vs the optimized candidate on the SIX production shapes
(``case["production"]``) on the currently selected GPU, and appends rows to
``benchmark.csv`` following ``docs/schemas.md``:

- PRIMARY metric: wrapper-inclusive wall-clock (``perf_counter`` + ``cuda.synchronize``)
  -> ``metric_kind=wall_clock``; this captures dispatcher/wrapper overhead.
- SECONDARY metric: kernel-only time via CUDA events -> ``metric_kind=kernel_event``.

Per (shape, metric_kind): one row with baseline_us, candidate_us, speedup_x, and a
``key=value`` notes field (mean/p10/p90/std, iters, warmup, gpu, host, container,
candidate id). A production-only geometric-mean row is written for each metric_kind.
Full provenance (sglang/cuda/torch versions, source hash, command) is recorded in
``solutions.jsonl`` joined by ``candidate_id``.

Force the CUDA path with ``KDA_REQUIRE_CUDA=1`` (otherwise the candidate falls back
to the baseline and the comparison is meaningless). Reuses the correctness harness's
``make_cases`` / ``baseline`` / ``candidate``.
"""

from __future__ import annotations

import csv
import hashlib
import importlib.util
import math
import os
import socket
import statistics
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Callable

try:
    import torch
except ImportError:  # pragma: no cover
    torch = None


KERNEL_SLUG = "b200_diffusion_norm_infer__multi_shape"
KERNEL_DIR = Path(__file__).resolve().parent
_CUH = KERNEL_DIR / "src" / "norm_cuda" / "diffusion_norm_infer.cuh"


def _load_correctness_module():
    test_py = KERNEL_DIR / "tests" / "test_correctness.py"
    spec = importlib.util.spec_from_file_location("kda_correctness_scaffold", test_py)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def _sync() -> None:
    if torch is not None and torch.cuda.is_available():
        torch.cuda.synchronize()


def _provenance() -> dict[str, str]:
    gpu_model = "unknown"
    cuda_ver = "unknown"
    torch_ver = "unknown"
    if torch is not None and torch.cuda.is_available():
        gpu_model = torch.cuda.get_device_name(0)
        cuda_ver = str(torch.version.cuda)
        torch_ver = str(torch.__version__)
    src_hash = "unknown"
    if _CUH.exists():
        src_hash = hashlib.sha256(_CUH.read_bytes()).hexdigest()[:16]
    return {
        "candidate_id": os.environ.get("KDA_CANDIDATE_ID", "cand-0001"),
        "gpu_model": gpu_model.replace(" ", "_"),
        "gpu_id": os.environ.get("CUDA_VISIBLE_DEVICES", "?"),
        "host": os.environ.get("KDA_HOST", socket.gethostname()),
        "container": os.environ.get("KDA_CONTAINER", "sglang_bbuf"),
        "sglang_commit": os.environ.get("KDA_SGLANG_COMMIT", "unset")[:12],
        "cuda": cuda_ver,
        "torch": torch_ver,
        "source_hash": src_hash,
    }


def _time_call_wall(fn: Callable[[dict], Any], case: dict, *, warmup: int, iters: int) -> list[float]:
    for _ in range(warmup):
        fn(case)
    _sync()
    samples = []
    for _ in range(iters):
        start = time.perf_counter()
        fn(case)
        _sync()
        samples.append((time.perf_counter() - start) * 1e6)
    return samples


def _time_call_events(fn: Callable[[dict], Any], case: dict, *, warmup: int, iters: int) -> list[float]:
    """Kernel-only GPU time via CUDA events (excludes Python/launch overhead)."""
    for _ in range(warmup):
        fn(case)
    _sync()
    samples = []
    for _ in range(iters):
        start_evt = torch.cuda.Event(enable_timing=True)
        end_evt = torch.cuda.Event(enable_timing=True)
        start_evt.record()
        fn(case)
        end_evt.record()
        end_evt.synchronize()
        samples.append(start_evt.elapsed_time(end_evt) * 1e3)  # ms -> us
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


def _row(writer, *, candidate_id, case_name, metric, baseline_us, candidate_us, speedup, notes):
    writer.writerow([
        datetime.now(timezone.utc).isoformat(),
        candidate_id,
        case_name,
        metric,
        f"{baseline_us:.6f}" if baseline_us is not None else "",
        f"{candidate_us:.6f}" if candidate_us is not None else "",
        f"{speedup:.6f}x" if (speedup is not None and math.isfinite(speedup)) else "",
        notes,
    ])


def main() -> int:
    correctness = _load_correctness_module()
    cases = [c for c in correctness.make_cases() if c.get("production")]
    if not cases:
        raise SystemExit("No production cases found.")
    prov = _provenance()
    cid = prov["candidate_id"]
    prov_note = (
        f"gpu_model={prov['gpu_model']} gpu_id={prov['gpu_id']} host={prov['host']} "
        f"container={prov['container']} slug={KERNEL_SLUG} cand={cid}"
    )

    timers = [("wall_clock", _time_call_wall), ("kernel_event", _time_call_events)]
    speedups_by_kind: dict[str, list[float]] = {k: [] for k, _ in timers}

    csv_path = KERNEL_DIR / "benchmark.csv"
    with csv_path.open("a", newline="") as f:
        writer = csv.writer(f)
        for case in cases:
            name = case.get("name", "unknown")
            warmup = int(case.get("warmup", 25))
            iters = int(case.get("iters", 100))
            for kind, timer in timers:
                b = _summary(timer(correctness.baseline, case, warmup=warmup, iters=iters))
                c = _summary(timer(correctness.candidate, case, warmup=warmup, iters=iters))
                spd = (b["median_us"] / c["median_us"]) if c["median_us"] > 0 else float("nan")
                speedups_by_kind[kind].append(spd)
                notes = (
                    f"metric_kind={kind} baseline_mean_us={b['mean_us']:.3f} "
                    f"cand_mean_us={c['mean_us']:.3f} cand_std_us={c['std_us']:.3f} "
                    f"cand_p10_us={c['p10_us']:.3f} cand_p90_us={c['p90_us']:.3f} "
                    f"cand_min_us={c['min_us']:.3f} warmup={warmup} iters={iters} {prov_note}"
                )
                _row(writer, candidate_id=cid, case_name=name, metric="median_us",
                     baseline_us=b["median_us"], candidate_us=c["median_us"], speedup=spd, notes=notes)
                print(f"{name:32s} [{kind:12s}] baseline={b['median_us']:.2f}us "
                      f"cand={c['median_us']:.2f}us speedup={spd:.3f}x")
        for kind, _ in timers:
            geo = _geom_mean(speedups_by_kind[kind])
            _row(writer, candidate_id="geomean", case_name="production_geomean", metric="geomean_speedup_x",
                 baseline_us=None, candidate_us=None, speedup=geo,
                 notes=f"metric_kind={kind} n_shapes={len(cases)} {prov_note}")
            print(f"GEOMEAN [{kind}] = {geo:.4f}x over {len(cases)} production shapes")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
