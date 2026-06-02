#!/usr/bin/env python3
"""Benchmark harness for ``h200_diffusion_norm_infer__multi_shape``.

Reuses ``tests/test_correctness.py`` (cases / baseline / candidate). Times the
six captured production shapes (the ``perf`` group) and records full per-shape
statistics plus evidence fields into ``benchmark.csv``.

Two modes:
  --lock      Measure ONLY the SGLang baseline and write immutable locked
              numbers to ``docs/baseline_locked.json`` (run once on an idle
              H200; later candidate runs compare against these).
  (default)   Measure the candidate, compare against the locked baseline,
              and append per-shape + geomean rows to ``benchmark.csv``.

Timing: wall-clock (perf_counter + cuda sync) is the PRIMARY latency — it is the
production-visible cost and exposes any Python dispatcher tax on the small
launch-bound shapes. CUDA-event GPU time is also recorded for roofline bandwidth.

All GPU work must run inside the ``sglang_bbuf`` container on an idle remote
H200 with ``CUDA_VISIBLE_DEVICES`` pinned to the selected ``REMOTE_GPU_ID``.

Usage (inside the container):
  python benchmark.py --lock --host ion8-h200
  python benchmark.py --candidate-version <git-sha-or-tag> --host ion8-h200
"""

from __future__ import annotations

import argparse
import csv
import importlib.util
import json
import math
import os
import statistics
import subprocess
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Callable

try:
    import torch
except ImportError:  # pragma: no cover
    torch = None  # type: ignore

KERNEL_SLUG = "h200_diffusion_norm_infer__multi_shape"
KERNEL_DIR = Path(__file__).resolve().parent
BASELINE_LOCK = KERNEL_DIR / "docs" / "baseline_locked.json"
CSV_PATH = KERNEL_DIR / "benchmark.csv"

CSV_HEADER = [
    "ts", "mode", "shape", "dtype", "metric",
    "baseline_us", "candidate_us", "speedup_x",
    "median_us", "mean_us", "std_us", "min_us", "p10_us", "p90_us",
    "gpu_time_us", "achieved_gbps",
    "host", "gpu_id", "gpu_model", "sglang_commit", "candidate_version",
    "warmup", "iters", "command", "slug", "notes", "remote_kda_dir",
]


def _load_correctness():
    test_py = KERNEL_DIR / "tests" / "test_correctness.py"
    spec = importlib.util.spec_from_file_location("kda_correctness_scaffold", test_py)
    assert spec is not None and spec.loader is not None, test_py
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def _sync() -> None:
    if torch is not None and torch.cuda.is_available():
        torch.cuda.synchronize()


def _bytes_moved(case: dict[str, Any]) -> int:
    """Read(x) + write(y) + weight/bias (counted once)."""
    elem = torch.tensor([], dtype=case["dtype"]).element_size()
    M, N = case["M"], case["N"]
    total = 2 * M * N * elem  # read x + write y
    if case["has_weight"]:
        total += N * elem
    if case["has_bias"]:
        total += N * elem
    return total


def _time_walls(fn: Callable[[dict], Any], case: dict, *, warmup: int, iters: int):
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


def _time_gpu_us(fn: Callable[[dict], Any], case: dict, *, iters: int) -> float:
    if torch is None or not torch.cuda.is_available():
        return float("nan")
    starts = [torch.cuda.Event(enable_timing=True) for _ in range(iters)]
    ends = [torch.cuda.Event(enable_timing=True) for _ in range(iters)]
    _sync()
    for i in range(iters):
        starts[i].record()
        fn(case)
        ends[i].record()
    _sync()
    times = [s.elapsed_time(e) * 1e3 for s, e in zip(starts, ends)]  # ms->us
    return statistics.median(times)


def _summary(samples: list[float]) -> dict[str, float]:
    ordered = sorted(samples)

    def pct(p: float) -> float:
        idx = min(len(ordered) - 1, max(0, round((len(ordered) - 1) * p)))
        return ordered[idx]

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


def _gpu_model() -> str:
    if torch is not None and torch.cuda.is_available():
        try:
            return torch.cuda.get_device_name(0)
        except Exception:
            pass
    return "unknown"


def _sglang_commit() -> str:
    try:
        import sglang
        repo = Path(sglang.__file__).resolve().parents[2]
        out = subprocess.run(
            ["git", "-C", str(repo), "rev-parse", "--short", "HEAD"],
            capture_output=True, text=True, timeout=10,
        )
        if out.returncode == 0:
            return out.stdout.strip()
    except Exception:
        pass
    return "unknown"


def _now() -> str:
    return datetime.now(timezone.utc).isoformat()


def _ensure_header():
    if not CSV_PATH.exists() or CSV_PATH.stat().st_size == 0:
        with CSV_PATH.open("w", newline="") as f:
            csv.writer(f).writerow(CSV_HEADER)


def _row(**kw) -> list[Any]:
    # Every row records the task-owned remote artifact root.
    kw.setdefault("remote_kda_dir", os.environ.get("REMOTE_KDA_DIR", ""))
    return [kw.get(c, "") for c in CSV_HEADER]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--lock", action="store_true",
                    help="Measure only the baseline and write docs/baseline_locked.json")
    ap.add_argument("--group", default="perf")
    ap.add_argument("--host", default=os.environ.get("KDA_HOST", "unknown"))
    ap.add_argument("--candidate-version", default="dev")
    ap.add_argument("--warmup", type=int, default=None)
    ap.add_argument("--iters", type=int, default=None)
    args = ap.parse_args()

    if torch is None or not torch.cuda.is_available():
        raise SystemExit("CUDA required: run inside the sglang_bbuf container on an idle H200.")

    correctness = _load_correctness()
    cases = [c for c in correctness.make_cases() if c["group"] == args.group]
    if not cases:
        raise SystemExit(f"No cases in group {args.group!r}.")

    gpu_id = os.environ.get("CUDA_VISIBLE_DEVICES", os.environ.get("REMOTE_GPU_ID", "unknown"))
    gpu_model = _gpu_model()
    sglang_commit = _sglang_commit()
    command = "python benchmark.py " + (" ".join(_argv_tail()))
    _ensure_header()

    if args.lock:
        locked: dict[str, Any] = {
            "_meta": {"ts": _now(), "host": args.host, "gpu_id": gpu_id,
                      "gpu_model": gpu_model, "sglang_commit": sglang_commit}
        }
        with CSV_PATH.open("a", newline="") as f:
            w = csv.writer(f)
            for case in cases:
                warmup = args.warmup or int(case.get("warmup", 25))
                iters = args.iters or int(case.get("iters", 100))
                walls = _time_walls(correctness.baseline, case, warmup=warmup, iters=iters)
                gpu_us = _time_gpu_us(correctness.baseline, case, iters=iters)
                s = _summary(walls)
                gbps = _bytes_moved(case) / (gpu_us * 1e-6) / 1e9 if gpu_us > 0 else float("nan")
                locked[case["name"]] = {"median_us": s["median_us"], "gpu_time_us": gpu_us,
                                        "dtype": str(case["dtype"]), "M": case["M"], "N": case["N"]}
                w.writerow(_row(ts=_now(), mode="baseline_lock", shape=case["name"],
                                dtype=str(case["dtype"]), metric="median_us",
                                baseline_us=f"{s['median_us']:.4f}",
                                median_us=f"{s['median_us']:.4f}", mean_us=f"{s['mean_us']:.4f}",
                                std_us=f"{s['std_us']:.4f}", min_us=f"{s['min_us']:.4f}",
                                p10_us=f"{s['p10_us']:.4f}", p90_us=f"{s['p90_us']:.4f}",
                                gpu_time_us=f"{gpu_us:.4f}", achieved_gbps=f"{gbps:.1f}",
                                host=args.host, gpu_id=gpu_id, gpu_model=gpu_model,
                                sglang_commit=sglang_commit, candidate_version="baseline",
                                warmup=warmup, iters=iters, command=command, slug=KERNEL_SLUG))
                print(f"[lock] {case['name']:32s} median={s['median_us']:.3f}us gpu={gpu_us:.3f}us {gbps:.0f}GB/s")
        BASELINE_LOCK.write_text(json.dumps(locked, indent=2))
        print(f"Locked baseline -> {BASELINE_LOCK}")
        return 0

    # Candidate-compare mode.
    if not BASELINE_LOCK.exists():
        raise SystemExit("No locked baseline. Run with --lock first.")
    locked = json.loads(BASELINE_LOCK.read_text())
    speedups = []
    with CSV_PATH.open("a", newline="") as f:
        w = csv.writer(f)
        for case in cases:
            if case["name"] not in locked:
                print(f"[skip] {case['name']} not in locked baseline")
                continue
            warmup = args.warmup or int(case.get("warmup", 25))
            iters = args.iters or int(case.get("iters", 100))
            walls = _time_walls(correctness.candidate, case, warmup=warmup, iters=iters)
            gpu_us = _time_gpu_us(correctness.candidate, case, iters=iters)
            s = _summary(walls)
            base_med = float(locked[case["name"]]["median_us"])
            speedup = base_med / s["median_us"] if s["median_us"] > 0 else float("nan")
            speedups.append(speedup)
            gbps = _bytes_moved(case) / (gpu_us * 1e-6) / 1e9 if gpu_us > 0 else float("nan")
            w.writerow(_row(ts=_now(), mode="candidate_vs_locked", shape=case["name"],
                            dtype=str(case["dtype"]), metric="median_us",
                            baseline_us=f"{base_med:.4f}", candidate_us=f"{s['median_us']:.4f}",
                            speedup_x=f"{speedup:.4f}", median_us=f"{s['median_us']:.4f}",
                            mean_us=f"{s['mean_us']:.4f}", std_us=f"{s['std_us']:.4f}",
                            min_us=f"{s['min_us']:.4f}", p10_us=f"{s['p10_us']:.4f}",
                            p90_us=f"{s['p90_us']:.4f}", gpu_time_us=f"{gpu_us:.4f}",
                            achieved_gbps=f"{gbps:.1f}", host=args.host, gpu_id=gpu_id,
                            gpu_model=gpu_model, sglang_commit=sglang_commit,
                            candidate_version=args.candidate_version, warmup=warmup,
                            iters=iters, command=command, slug=KERNEL_SLUG))
            print(f"[cand] {case['name']:32s} base={base_med:.3f} cand={s['median_us']:.3f} "
                  f"speedup={speedup:.3f}x gpu={gpu_us:.3f}us {gbps:.0f}GB/s")
        geo = _geom_mean(speedups)
        w.writerow(_row(ts=_now(), mode="geomean", shape="all_perf_shapes",
                        metric="geomean_speedup_x", speedup_x=f"{geo:.4f}",
                        host=args.host, gpu_id=gpu_id, gpu_model=gpu_model,
                        sglang_commit=sglang_commit, candidate_version=args.candidate_version,
                        command=command, slug=KERNEL_SLUG))
        print(f"[geomean] speedup_x = {geo:.4f}")
    return 0


def _argv_tail():
    import sys
    return sys.argv[1:]


if __name__ == "__main__":
    raise SystemExit(main())
