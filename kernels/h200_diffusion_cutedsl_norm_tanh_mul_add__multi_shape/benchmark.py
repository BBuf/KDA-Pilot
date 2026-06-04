#!/usr/bin/env python3
"""Benchmark harness for ``h200_diffusion_cutedsl_norm_tanh_mul_add__multi_shape``.

Reuses ``tests/test_correctness.py`` (cases / baseline / candidate callables) and
times the 4 captured production signatures (``bench=True`` cases), recording full
per-shape statistics plus evidence fields into ``benchmark.csv``.

Modes:
  --lock      Measure ONLY the vendored pinned baseline and write immutable
              locked numbers to ``docs/baseline_locked.json`` (run once on an
              idle H200; later candidate runs compare against these).
  (default)   Measure the candidate vs the locked baseline AND run a
              same-process interleaved A/B (baseline and candidate alternating
              within one loop, both through the identical harness path), then
              append per-shape + geomean rows to ``benchmark.csv``.

Timing methodology (per the task's benchmark requirements):
  - JIT/module-load/compile warmup happens before any timed region (warmup
    calls; both sides are warmed in candidate mode).
  - Wall-clock (perf_counter + cuda sync) is the PRIMARY latency: the
    production-visible cost including the Python wrapper/dispatch tax.
  - CUDA-event GPU time is recorded per shape for the DEVICE side of the
    device-vs-host decomposition (host_overhead_us = wall_median - gpu_median)
    and for roofline bandwidth (achieved_gbps over modeled bytes).
  - The interleaved A/B cross-checks the sequential numbers within-process.
  - GPU state (utilization / memory / other compute processes) is captured
    before and after; the run REFUSES to start on a busy GPU.

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
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Callable

try:
    import torch
except ImportError:  # pragma: no cover
    torch = None  # type: ignore

KERNEL_SLUG = "h200_diffusion_cutedsl_norm_tanh_mul_add__multi_shape"
BASELINE_PIN = "0689ba84b88c991684b0f99ee9b50c3ce485b483"
KERNEL_DIR = Path(__file__).resolve().parent
BASELINE_LOCK = KERNEL_DIR / "docs" / "baseline_locked.json"
CSV_PATH = KERNEL_DIR / "benchmark.csv"

CSV_HEADER = [
    "ts", "mode", "shape", "dtype", "metric",
    "baseline_us", "candidate_us", "speedup_x",
    "median_us", "mean_us", "std_us", "min_us", "p10_us", "p90_us",
    "gpu_time_us", "host_overhead_us", "achieved_gbps",
    "host", "gpu_id", "gpu_model", "sglang_commit", "baseline_pin",
    "candidate_version", "warmup", "iters", "command", "slug", "notes",
    "remote_kda_dir",
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


def _mode_elems(mode: str, B: int, S: int, D: int) -> int:
    return {"BSD": B * S * D, "1SD": S * D, "B1D": B * D, "11D": D}[mode]


def _bytes_moved(case: dict[str, Any]) -> int:
    """Modeled global-memory traffic per call (roofline denominator).

    single: read x + read scale + read shift + read weight(+bias) + write y.
    dual:   + read weight2(+bias2) + read scale2 + write y2 (the kernel keeps
    y in registers for the second norm — no y re-read).
    """

    elem = {"bfloat16": 2, "float16": 2, "float32": 4}[case["dtype"]]
    B, S, D = case["B"], case["S"], case["D"]
    full = B * S * D
    total = full  # read x
    total += _mode_elems(case["scale_mode"], B, S, D)  # read scale
    total += _mode_elems(case["shift_mode"], B, S, D)  # read shift
    if case["affine_mode"] == "D":
        total += 2 * D  # weight + bias (bias only loaded for layer; count once)
    total += full  # write y
    if case["entry"] == "dual":
        if case["affine_mode"] == "D":
            total += 2 * D
        total += _mode_elems(case["scale_mode"], B, S, D)  # read scale2
        total += full  # write y2
    return total * elem


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
    times = [s.elapsed_time(e) * 1e3 for s, e in zip(starts, ends)]  # ms -> us
    return statistics.median(times)


def _time_interleaved(
    fn_a: Callable[[dict], Any],
    fn_b: Callable[[dict], Any],
    case: dict,
    *,
    warmup: int,
    iters: int,
):
    """Same-process interleaved A/B: A and B alternate within one loop so both
    see identical GPU clock/thermal/allocator state. Both callables go through
    the identical harness path (symmetric wrappers)."""

    for _ in range(warmup):
        fn_a(case)
        fn_b(case)
    _sync()
    sa: list[float] = []
    sb: list[float] = []
    for _ in range(iters):
        t0 = time.perf_counter()
        fn_a(case)
        _sync()
        sa.append((time.perf_counter() - t0) * 1e6)
        t1 = time.perf_counter()
        fn_b(case)
        _sync()
        sb.append((time.perf_counter() - t1) * 1e6)
    return sa, sb


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
            return torch.cuda.get_device_name(torch.cuda.current_device())
        except Exception:
            pass
    return "unknown"


def _physical_gpu_id() -> str:
    return os.environ.get("CUDA_VISIBLE_DEVICES", os.environ.get("REMOTE_GPU_ID", "unknown"))


def _gpu_state() -> str:
    """utilization/memory/process snapshot of the selected physical GPU."""

    gpu_id = _physical_gpu_id()
    try:
        util = subprocess.run(
            ["nvidia-smi", "-i", gpu_id, "--query-gpu=utilization.gpu,memory.used",
             "--format=csv,noheader,nounits"],
            capture_output=True, text=True, timeout=10,
        ).stdout.strip()
        procs = subprocess.run(
            ["nvidia-smi", "-i", gpu_id, "--query-compute-apps=pid,used_memory",
             "--format=csv,noheader"],
            capture_output=True, text=True, timeout=10,
        ).stdout.strip()
        nproc = len([line for line in procs.splitlines() if line.strip()])
        return f"gpu{gpu_id} util/memMiB={util} other_compute_procs={nproc}"
    except Exception as exc:  # pragma: no cover
        return f"gpu{gpu_id} state-unavailable ({exc})"


def _assert_gpu_idle(allow_busy: bool) -> None:
    """Refuse to benchmark on a GPU with other active compute processes."""

    gpu_id = _physical_gpu_id()
    try:
        procs = subprocess.run(
            ["nvidia-smi", "-i", gpu_id, "--query-compute-apps=pid", "--format=csv,noheader"],
            capture_output=True, text=True, timeout=10,
        ).stdout.strip()
    except Exception:
        return  # cannot determine; proceed (state is still recorded)
    others = [p for p in procs.splitlines() if p.strip() and int(p.strip()) != os.getpid()]
    if others and not allow_busy:
        raise SystemExit(
            f"GPU {gpu_id} has active compute processes {others}; refusing to "
            "benchmark on a busy GPU (pass --allow-busy only with explicit approval)."
        )


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


def _ensure_header() -> None:
    if not CSV_PATH.exists() or CSV_PATH.stat().st_size == 0:
        with CSV_PATH.open("w", newline="") as f:
            csv.writer(f).writerow(CSV_HEADER)


def _row(**kw) -> list[Any]:
    kw.setdefault("remote_kda_dir", os.environ.get("REMOTE_KDA_DIR", ""))
    kw.setdefault("baseline_pin", BASELINE_PIN[:9])
    kw.setdefault("slug", KERNEL_SLUG)
    return [kw.get(c, "") for c in CSV_HEADER]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--lock", action="store_true",
                    help="Measure only the vendored baseline and write docs/baseline_locked.json")
    ap.add_argument("--host", default=os.environ.get("KDA_HOST", "unknown"))
    ap.add_argument("--candidate-version", default="dev")
    ap.add_argument("--warmup", type=int, default=None)
    ap.add_argument("--iters", type=int, default=None)
    ap.add_argument("--allow-busy", action="store_true",
                    help="Override the idle-GPU refusal (requires explicit approval)")
    args = ap.parse_args()

    if torch is None or not torch.cuda.is_available():
        raise SystemExit("CUDA required: run inside the sglang_bbuf container on an idle H200.")
    _assert_gpu_idle(args.allow_busy)

    correctness = _load_correctness()
    cases = [c for c in correctness.make_cases() if c.get("bench")]
    if not cases:
        raise SystemExit("No bench=True production cases recovered.")

    gpu_id = _physical_gpu_id()
    gpu_model = _gpu_model()
    sglang_commit = _sglang_commit()
    command = "python benchmark.py " + " ".join(sys.argv[1:])
    state_before = _gpu_state()
    print(f"[gpu-state-before] {state_before}")
    _ensure_header()

    if args.lock:
        locked: dict[str, Any] = {
            "_meta": {
                "ts": _now(), "host": args.host, "gpu_id": gpu_id,
                "gpu_model": gpu_model, "sglang_commit": sglang_commit,
                "baseline_pin": BASELINE_PIN, "command": command,
                "gpu_state_before": state_before,
            }
        }
        with CSV_PATH.open("a", newline="") as f:
            w = csv.writer(f)
            for case in cases:
                warmup = args.warmup or int(case.get("warmup", 25))
                iters = args.iters or int(case.get("iters", 100))
                walls = _time_walls(correctness.baseline, case, warmup=warmup, iters=iters)
                gpu_us = _time_gpu_us(correctness.baseline, case, iters=iters)
                s = _summary(walls)
                host_us = s["median_us"] - gpu_us
                gbps = _bytes_moved(case) / (gpu_us * 1e-6) / 1e9 if gpu_us > 0 else float("nan")
                locked[case["name"]] = {
                    "median_us": s["median_us"], "gpu_time_us": gpu_us,
                    "host_overhead_us": host_us, "achieved_gbps": gbps,
                    "dtype": case["dtype"], "B": case["B"], "S": case["S"],
                    "D": case["D"], "entry": case["entry"],
                    "warmup": warmup, "iters": iters,
                }
                w.writerow(_row(
                    ts=_now(), mode="baseline_lock", shape=case["name"],
                    dtype=case["dtype"], metric="median_us",
                    baseline_us=f"{s['median_us']:.4f}",
                    median_us=f"{s['median_us']:.4f}", mean_us=f"{s['mean_us']:.4f}",
                    std_us=f"{s['std_us']:.4f}", min_us=f"{s['min_us']:.4f}",
                    p10_us=f"{s['p10_us']:.4f}", p90_us=f"{s['p90_us']:.4f}",
                    gpu_time_us=f"{gpu_us:.4f}", host_overhead_us=f"{host_us:.4f}",
                    achieved_gbps=f"{gbps:.1f}", host=args.host, gpu_id=gpu_id,
                    gpu_model=gpu_model, sglang_commit=sglang_commit,
                    candidate_version="baseline(vendored-pin)", warmup=warmup,
                    iters=iters, command=command, notes=state_before,
                ))
                print(f"[lock] {case['name']:48s} median={s['median_us']:9.3f}us "
                      f"gpu={gpu_us:9.3f}us host={host_us:7.3f}us {gbps:7.0f}GB/s")
            state_after = _gpu_state()
            locked["_meta"]["gpu_state_after"] = state_after
            print(f"[gpu-state-after] {state_after}")
        BASELINE_LOCK.write_text(json.dumps(locked, indent=2))
        print(f"Locked baseline -> {BASELINE_LOCK}")
        return 0

    # ---- Candidate mode: vs locked baseline + same-process interleaved A/B ----
    if not getattr(correctness, "_candidate_available", lambda: False)():
        raise SystemExit("Candidate not implemented (src/register.py CANDIDATE_READY is False).")
    if not BASELINE_LOCK.exists():
        raise SystemExit("No locked baseline. Run with --lock first.")
    locked = json.loads(BASELINE_LOCK.read_text())
    speedups: list[float] = []
    ab_speedups: list[float] = []
    with CSV_PATH.open("a", newline="") as f:
        w = csv.writer(f)
        for case in cases:
            if case["name"] not in locked:
                print(f"[skip] {case['name']} not in locked baseline")
                continue
            warmup = args.warmup or int(case.get("warmup", 25))
            iters = args.iters or int(case.get("iters", 100))
            # Sequential candidate timing vs the locked baseline.
            walls = _time_walls(correctness.candidate, case, warmup=warmup, iters=iters)
            gpu_us = _time_gpu_us(correctness.candidate, case, iters=iters)
            s = _summary(walls)
            host_us = s["median_us"] - gpu_us
            base_med = float(locked[case["name"]]["median_us"])
            base_gpu = float(locked[case["name"]]["gpu_time_us"])
            speedup = base_med / s["median_us"] if s["median_us"] > 0 else float("nan")
            dev_speedup = base_gpu / gpu_us if gpu_us > 0 else float("nan")
            speedups.append(speedup)
            gbps = _bytes_moved(case) / (gpu_us * 1e-6) / 1e9 if gpu_us > 0 else float("nan")
            w.writerow(_row(
                ts=_now(), mode="candidate_vs_locked", shape=case["name"],
                dtype=case["dtype"], metric="median_us",
                baseline_us=f"{base_med:.4f}", candidate_us=f"{s['median_us']:.4f}",
                speedup_x=f"{speedup:.4f}", median_us=f"{s['median_us']:.4f}",
                mean_us=f"{s['mean_us']:.4f}", std_us=f"{s['std_us']:.4f}",
                min_us=f"{s['min_us']:.4f}", p10_us=f"{s['p10_us']:.4f}",
                p90_us=f"{s['p90_us']:.4f}", gpu_time_us=f"{gpu_us:.4f}",
                host_overhead_us=f"{host_us:.4f}", achieved_gbps=f"{gbps:.1f}",
                host=args.host, gpu_id=gpu_id, gpu_model=gpu_model,
                sglang_commit=sglang_commit, candidate_version=args.candidate_version,
                warmup=warmup, iters=iters, command=command,
                notes=f"device_speedup_x={dev_speedup:.4f} (locked gpu {base_gpu:.3f}us)",
            ))
            # Same-process interleaved A/B cross-check.
            sa, sb = _time_interleaved(
                correctness.baseline, correctness.candidate, case,
                warmup=max(5, warmup // 2), iters=iters,
            )
            med_a, med_b = statistics.median(sa), statistics.median(sb)
            ab_speedup = med_a / med_b if med_b > 0 else float("nan")
            ab_speedups.append(ab_speedup)
            w.writerow(_row(
                ts=_now(), mode="interleaved_ab", shape=case["name"],
                dtype=case["dtype"], metric="median_us",
                baseline_us=f"{med_a:.4f}", candidate_us=f"{med_b:.4f}",
                speedup_x=f"{ab_speedup:.4f}", host=args.host, gpu_id=gpu_id,
                gpu_model=gpu_model, sglang_commit=sglang_commit,
                candidate_version=args.candidate_version, warmup=max(5, warmup // 2),
                iters=iters, command=command,
                notes="same-process alternating; symmetric harness path",
            ))
            print(f"[cand] {case['name']:48s} locked={base_med:.3f} cand={s['median_us']:.3f} "
                  f"seq={speedup:.3f}x ab={ab_speedup:.3f}x dev={dev_speedup:.3f}x "
                  f"gpu={gpu_us:.3f}us {gbps:.0f}GB/s")
        geo = _geom_mean(speedups)
        geo_ab = _geom_mean(ab_speedups)
        w.writerow(_row(
            ts=_now(), mode="geomean", shape="all_production_shapes",
            metric="geomean_speedup_x", speedup_x=f"{geo:.4f}",
            host=args.host, gpu_id=gpu_id, gpu_model=gpu_model,
            sglang_commit=sglang_commit, candidate_version=args.candidate_version,
            command=command, notes=f"interleaved_ab_geomean={geo_ab:.4f}",
        ))
        state_after = _gpu_state()
        print(f"[gpu-state-after] {state_after}")
        print(f"[geomean] sequential={geo:.4f}x interleaved={geo_ab:.4f}x")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
