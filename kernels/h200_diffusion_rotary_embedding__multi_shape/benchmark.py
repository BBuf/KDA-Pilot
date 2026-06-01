#!/usr/bin/env python3
"""Isolated benchmark for ``h200_diffusion_rotary_embedding__multi_shape``.

Reuses ``tests/test_correctness.py`` cases/baseline/candidate, then appends a
full-schema row per shape to ``benchmark.csv``: for BOTH baseline and candidate,
median/mean/std/min/p10/p90 (us), plus the geomean of per-shape median speedups
over the 6 deduplicated shapes. Allocation is included in both paths (both return
a new tensor), so the comparison is fair.

Provenance (host / GPU id+model / idle-before+after / commits / oracle
equivalence / command / run dir / candidate id) is read from KDA_* env vars and
written as a leading ``# provenance:`` comment so before/after-optimization runs
are comparable.
"""

from __future__ import annotations

import csv
import importlib.util
import math
import os
import statistics
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Callable

try:
    import torch
except ImportError:  # pragma: no cover
    torch = None


KERNEL_SLUG = "h200_diffusion_rotary_embedding__multi_shape"
KERNEL_DIR = Path(__file__).resolve().parent

_STATS = ("median", "mean", "std", "min", "p10", "p90")


def _load_correctness_module():
    test_py = KERNEL_DIR / "tests" / "test_correctness.py"
    spec = importlib.util.spec_from_file_location("kda_correctness_scaffold", test_py)
    assert spec is not None and spec.loader is not None, test_py
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def _sync() -> None:
    if torch is not None and torch.cuda.is_available():
        torch.cuda.synchronize()


def _time_call(fn: Callable[[dict], Any], case: dict, *, warmup: int, iters: int) -> list[float]:
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
    cleaned = [v for v in values if math.isfinite(v) and v > 0]
    if not cleaned:
        return float("nan")
    return math.exp(sum(math.log(v) for v in cleaned) / len(cleaned))


def _provenance() -> str:
    gpu_model = os.environ.get("KDA_GPU_MODEL", "")
    if not gpu_model and torch is not None and torch.cuda.is_available():
        try:
            gpu_model = torch.cuda.get_device_name(0)
        except Exception:
            gpu_model = ""
    fields = {
        "candidate": os.environ.get("KDA_CANDIDATE", "native_cuda"),
        "kernel_pilot_commit": os.environ.get("KDA_KP_COMMIT", ""),
        "src_hash": os.environ.get("KDA_SRC_HASH", ""),
        "sglang_commit": os.environ.get("KDA_SGLANG_COMMIT", ""),
        "oracle_equiv": os.environ.get("KDA_ORACLE_EQUIV", ""),
        "host": os.environ.get("KDA_HOST", ""),
        "gpu_id": os.environ.get("KDA_GPU_ID", os.environ.get("CUDA_VISIBLE_DEVICES", "")),
        "gpu_model": gpu_model,
        "idle_before": os.environ.get("KDA_IDLE_BEFORE", ""),
        "idle_after": os.environ.get("KDA_IDLE_AFTER", ""),
        "run_dir": os.environ.get("KDA_RUN_DIR", ""),
        "cmd": os.environ.get("KDA_CMD", ""),
    }
    return "# provenance: " + " ".join(f"{k}={v!r}" for k, v in fields.items())


def main() -> int:
    correctness = _load_correctness_module()
    cases = correctness.make_cases()
    if not cases:
        raise SystemExit("No benchmark cases. Fill tests/test_correctness.py first.")

    candidate_id = os.environ.get("KDA_CANDIDATE", "native_cuda")
    csv_path = KERNEL_DIR / "benchmark.csv"
    speedups = []
    header = (
        ["ts", "candidate", "case"]
        + [f"baseline_{s}_us" for s in _STATS]
        + [f"cand_{s}_us" for s in _STATS]
        + ["speedup"]
    )
    with csv_path.open("a", newline="") as f:
        writer = csv.writer(f)
        f.write(_provenance() + "\n")
        writer.writerow(header)
        for case in cases:
            warmup = int(case.get("warmup", 25))
            iters = int(case.get("iters", 100))
            b = _summary(_time_call(correctness.baseline, case, warmup=warmup, iters=iters))
            c = _summary(_time_call(correctness.candidate, case, warmup=warmup, iters=iters))
            speedup = (b["median"] / c["median"]) if c["median"] > 0 else float("nan")
            speedups.append(speedup)
            now = datetime.now(timezone.utc).isoformat()
            row = (
                [now, candidate_id, case.get("name", "unknown")]
                + [f"{b[s]:.6f}" for s in _STATS]
                + [f"{c[s]:.6f}" for s in _STATS]
                + [f"{speedup:.6f}x" if math.isfinite(speedup) else ""]
            )
            writer.writerow(row)
            print(case.get("name", "unknown"), "speedup_x", speedup)
        writer.writerow(
            [datetime.now(timezone.utc).isoformat(), "geomean", "all_configured_shapes"]
            + [""] * (2 * len(_STATS))
            + [f"{_geom_mean(speedups):.6f}x"]
        )
    print("geomean_speedup_x", _geom_mean(speedups))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
