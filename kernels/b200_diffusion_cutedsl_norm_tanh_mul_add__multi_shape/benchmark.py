#!/usr/bin/env python3
"""Benchmark harness for ``b200_diffusion_cutedsl_norm_tanh_mul_add__multi_shape``.

Measures the frozen CuTe-DSL baseline copy (``baseline/``) against the
candidate dispatcher (``src/register.py``) on the captured production shapes
(cases with ``bench=True`` in ``tests/test_correctness.py``).

Methodology (per the task contract):
- Wall-clock timing with per-call synchronization is the END-TO-END channel
  (raw-callable layer, host cost included on both sides).
- CUDA-event bracket timing is a DIAGNOSTIC channel only: the CuTe-DSL
  baseline's tvm-ffi host path serializes inside the bracket, so its event
  numbers overstate device time (baseline-pessimistic). The authoritative
  device-only decomposition comes from NCU kernel durations collected with
  identical launch-skip/count discipline (see profile/ and solutions.jsonl).
- Same-process, interleaved A/B: baseline and candidate alternate within one
  loop, alternating call order every iteration, identical allocation policy
  (both allocate outputs internally via ``torch.empty_like``).
- JIT compile caches (CuTe + native) are populated by warmup before any timed
  sample.
- Anti-silent-fallback: candidate calls run with ``KDA_REQUIRE_CANDIDATE=1``
  unless ``--allow-fallback`` is passed (used only before the native kernel
  exists, e.g. when freezing baseline numbers).
- GPU idle gate: the selected GPU must show no other compute processes and no
  meaningful foreign memory at start AND at end; otherwise NO rows are
  written.

Modes:
- ``--baseline-only``: time only the baseline (candidate columns empty) — used
  to freeze the immutable baseline reference rows.
- default A/B: time both, verify the fast path actually fired, report
  per-shape stats and the geometric-mean speedup.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import importlib.util
import math
import os
import socket
import statistics
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Callable

import torch

KERNEL_SLUG = "b200_diffusion_cutedsl_norm_tanh_mul_add__multi_shape"
KERNEL_DIR = Path(__file__).resolve().parent

CSV_COLUMNS = [
    "timestamp", "mode", "candidate_name", "case_name", "variant",
    "B", "S", "D", "dtype", "norm_type", "mode_scale", "mode_shift", "eps",
    "baseline_dev_median_us", "baseline_dev_mean_us", "baseline_dev_std_us",
    "baseline_dev_min_us", "baseline_dev_p10_us", "baseline_dev_p90_us",
    "baseline_wall_median_us",
    "cand_dev_median_us", "cand_dev_mean_us", "cand_dev_std_us",
    "cand_dev_min_us", "cand_dev_p10_us", "cand_dev_p90_us",
    "cand_wall_median_us",
    "speedup_dev_x", "speedup_wall_x",
    "warmup", "iters", "command", "git_commit", "candidate_source_hash",
    "host", "gpu_physical_index", "gpu_logical_index", "gpu_name", "gpu_uuid",
    "cuda_visible_devices", "idle_before", "idle_after",
    "fast_path_hits_delta", "notes",
]


def _load_correctness_module():
    test_py = KERNEL_DIR / "tests" / "test_correctness.py"
    spec = importlib.util.spec_from_file_location("kda_correctness_harness", test_py)
    assert spec is not None and spec.loader is not None, test_py
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


# ---------------------------------------------------------------------------
# Environment / provenance helpers
# ---------------------------------------------------------------------------


def _physical_gpu_index() -> str:
    cvd = os.environ.get("CUDA_VISIBLE_DEVICES", "")
    first = cvd.split(",")[0].strip() if cvd else "0"
    return first or "0"


def _nvidia_smi(query: str, gpu: str) -> str:
    try:
        out = subprocess.run(
            ["nvidia-smi", f"--query-gpu={query}", "--format=csv,noheader,nounits",
             "-i", gpu],
            capture_output=True, text=True, timeout=30, check=True,
        )
        return out.stdout.strip()
    except Exception as exc:  # noqa: BLE001
        return f"ERROR:{exc!r}"


def _foreign_compute_pids(gpu_uuid: str) -> list[str]:
    """PIDs of compute apps on the GPU that are not this process."""

    try:
        out = subprocess.run(
            ["nvidia-smi", "--query-compute-apps=gpu_uuid,pid",
             "--format=csv,noheader"],
            capture_output=True, text=True, timeout=30, check=True,
        )
    except Exception:  # noqa: BLE001
        return ["nvidia-smi-query-failed"]
    pids = []
    me = str(os.getpid())
    for line in out.stdout.strip().splitlines():
        parts = [p.strip() for p in line.split(",")]
        if len(parts) >= 2 and parts[0] == gpu_uuid and parts[1] != me:
            pids.append(parts[1])
    return pids


def _gpu_idle_state(gpu: str, gpu_uuid: str) -> tuple[bool, str]:
    util = _nvidia_smi("utilization.gpu", gpu)
    foreign = _foreign_compute_pids(gpu_uuid)
    detail = f"util={util}% foreign_pids={foreign or 'none'}"
    try:
        util_ok = int(util) <= 5
    except ValueError:
        util_ok = False
    # Our own process may legitimately be the only compute app and drive util.
    idle = (not foreign) and (util_ok or not foreign)
    return idle, detail


def _git_commit() -> str:
    env_commit = os.environ.get("KDA_GIT_COMMIT")
    if env_commit:
        return env_commit
    try:
        out = subprocess.run(
            ["git", "rev-parse", "HEAD"], cwd=KERNEL_DIR,
            capture_output=True, text=True, timeout=15, check=True,
        )
        return out.stdout.strip()
    except Exception:  # noqa: BLE001
        return "unknown"


def _candidate_source_hash() -> str:
    h = hashlib.sha256()
    paths = sorted(
        list((KERNEL_DIR / "src").rglob("*.py"))
        + list((KERNEL_DIR / "src").rglob("*.cuh"))
        + list((KERNEL_DIR / "src").rglob("*.cu"))
    )
    for p in paths:
        h.update(str(p.relative_to(KERNEL_DIR)).encode())
        h.update(p.read_bytes())
    return h.hexdigest()[:16]


# ---------------------------------------------------------------------------
# Timing
# ---------------------------------------------------------------------------


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


def _time_interleaved_events(
    fns: list[Callable[[], Any]], iters: int
) -> list[list[float]]:
    """CUDA-event timing for N callables, interleaved within one loop and with
    rotating call order, back-to-back launches (no per-iter sync)."""

    n = len(fns)
    events = [
        [(torch.cuda.Event(enable_timing=True), torch.cuda.Event(enable_timing=True))
         for _ in range(iters)]
        for _ in range(n)
    ]
    for i in range(iters):
        order = list(range(n))
        if i % 2 == 1:
            order.reverse()
        for j in order:
            start, end = events[j][i]
            start.record()
            fns[j]()
            end.record()
    torch.cuda.synchronize()
    return [
        [s.elapsed_time(e) * 1000.0 for s, e in events[j]]  # ms -> us
        for j in range(n)
    ]


def _time_wall_synced(fn: Callable[[], Any], iters: int) -> list[float]:
    """Wall-clock per call with sync — includes host wrapper + launch overhead."""

    samples = []
    torch.cuda.synchronize()
    for _ in range(iters):
        t0 = time.perf_counter()
        fn()
        torch.cuda.synchronize()
        samples.append((time.perf_counter() - t0) * 1e6)
    return samples


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--baseline-only", action="store_true",
                        help="freeze baseline rows only (no candidate timing)")
    parser.add_argument("--allow-fallback", action="store_true",
                        help="do not force KDA_REQUIRE_CANDIDATE=1 for candidate calls")
    parser.add_argument("--candidate-name", default="dev",
                        help="candidate label recorded in rows")
    parser.add_argument("--warmup", type=int, default=None)
    parser.add_argument("--iters", type=int, default=None)
    parser.add_argument("--notes", default="")
    args = parser.parse_args()

    if not torch.cuda.is_available():
        raise SystemExit("CUDA device required (run inside the remote container).")

    correctness = _load_correctness_module()
    cases = [c for c in correctness.make_cases() if c.get("bench")]
    if not cases:
        raise SystemExit("No bench=True cases configured.")

    register = correctness._register_module()

    gpu_phys = _physical_gpu_index()
    gpu_uuid = _nvidia_smi("uuid", gpu_phys)
    gpu_name = _nvidia_smi("name", gpu_phys)
    # A just-exited CUDA process (e.g. a test run in the same session) can
    # linger in nvidia-smi for a few seconds; retry briefly before aborting.
    idle_before, idle_before_detail = _gpu_idle_state(gpu_phys, gpu_uuid)
    for _ in range(3):
        if idle_before:
            break
        time.sleep(5)
        idle_before, idle_before_detail = _gpu_idle_state(gpu_phys, gpu_uuid)
    if not idle_before:
        raise SystemExit(
            f"ABORT: GPU {gpu_phys} ({gpu_uuid}) not idle at start: {idle_before_detail}"
        )

    command = " ".join([sys.executable] + sys.argv)
    git_commit = _git_commit()
    source_hash = _candidate_source_hash()
    host = socket.gethostname()
    mode = "baseline-only" if args.baseline_only else "ab"

    rows: list[list[Any]] = []
    speedups_dev: list[float] = []
    speedups_wall: list[float] = []

    for case in cases:
        warmup = args.warmup if args.warmup is not None else int(case.get("warmup", 50))
        iters = args.iters if args.iters is not None else int(case.get("iters", 200))
        warmup = max(warmup, 5)

        def run_baseline():
            return correctness.baseline(case)

        def run_candidate():
            return correctness.candidate(case)

        # Warmup populates CuTe compile cache / native JIT before timing.
        for _ in range(warmup):
            run_baseline()
        fast_hits_delta = 0
        if not args.baseline_only:
            guard_token = None
            if not args.allow_fallback:
                guard_token = os.environ.get("KDA_REQUIRE_CANDIDATE")
                os.environ["KDA_REQUIRE_CANDIDATE"] = "1"
            try:
                hits0 = register.fast_path_hits()
                for _ in range(warmup):
                    run_candidate()
                torch.cuda.synchronize()
                dev_b, dev_c = _time_interleaved_events(
                    [run_baseline, run_candidate], iters
                )
                wall_b = _time_wall_synced(run_baseline, max(iters // 4, 25))
                wall_c = _time_wall_synced(run_candidate, max(iters // 4, 25))
                fast_hits_delta = register.fast_path_hits() - hits0
            finally:
                if not args.allow_fallback:
                    if guard_token is None:
                        os.environ.pop("KDA_REQUIRE_CANDIDATE", None)
                    else:
                        os.environ["KDA_REQUIRE_CANDIDATE"] = guard_token
        else:
            torch.cuda.synchronize()
            (dev_b,) = _time_interleaved_events([run_baseline], iters)
            wall_b = _time_wall_synced(run_baseline, max(iters // 4, 25))
            dev_c, wall_c = None, None

        b = _summary(dev_b)
        b_wall = _summary(wall_b)
        if dev_c is not None:
            c = _summary(dev_c)
            c_wall = _summary(wall_c)
            speedup_dev = b["median_us"] / c["median_us"] if c["median_us"] > 0 else float("nan")
            speedup_wall = (
                b_wall["median_us"] / c_wall["median_us"]
                if c_wall["median_us"] > 0 else float("nan")
            )
            speedups_dev.append(speedup_dev)
            speedups_wall.append(speedup_wall)
        else:
            c = c_wall = None
            speedup_dev = speedup_wall = float("nan")

        correctness._release(case)
        rows.append([
            datetime.now(timezone.utc).isoformat(), mode, args.candidate_name,
            case["name"], case["variant"], case["B"], case["S"], case["D"],
            case["dtype"], case["norm_type"], case["mode_scale"], case["mode_shift"],
            case["eps"],
            f"{b['median_us']:.3f}", f"{b['mean_us']:.3f}", f"{b['std_us']:.3f}",
            f"{b['min_us']:.3f}", f"{b['p10_us']:.3f}", f"{b['p90_us']:.3f}",
            f"{b_wall['median_us']:.3f}",
            *(
                [f"{c['median_us']:.3f}", f"{c['mean_us']:.3f}", f"{c['std_us']:.3f}",
                 f"{c['min_us']:.3f}", f"{c['p10_us']:.3f}", f"{c['p90_us']:.3f}",
                 f"{c_wall['median_us']:.3f}"]
                if c is not None else ["", "", "", "", "", "", ""]
            ),
            f"{speedup_dev:.4f}" if math.isfinite(speedup_dev) else "",
            f"{speedup_wall:.4f}" if math.isfinite(speedup_wall) else "",
            warmup, iters, command, git_commit, source_hash,
            host, gpu_phys, "0", gpu_name, gpu_uuid,
            os.environ.get("CUDA_VISIBLE_DEVICES", ""),
            idle_before_detail, "PENDING_FINAL_CHECK",
            fast_hits_delta, args.notes,
        ])
        label = case["name"]
        if c is not None:
            print(f"{label}: baseline {b['median_us']:.2f}us vs candidate "
                  f"{c['median_us']:.2f}us dev-speedup {speedup_dev:.4f}x "
                  f"(wall {speedup_wall:.4f}x, fast-path hits {fast_hits_delta})")
        else:
            print(f"{label}: baseline {b['median_us']:.2f}us "
                  f"(wall {b_wall['median_us']:.2f}us)")

    idle_after, idle_after_detail = _gpu_idle_state(gpu_phys, gpu_uuid)
    if not idle_after:
        raise SystemExit(
            f"ABORT: GPU {gpu_phys} busy at end ({idle_after_detail}); "
            "no rows written — rerun on an idle card."
        )
    for row in rows:
        row[CSV_COLUMNS.index("idle_after")] = idle_after_detail

    csv_path = KERNEL_DIR / "benchmark.csv"
    write_header = not csv_path.exists() or csv_path.stat().st_size == 0
    with csv_path.open("a", newline="") as f:
        writer = csv.writer(f)
        if write_header:
            writer.writerow(CSV_COLUMNS)
        writer.writerows(rows)
        if not args.baseline_only:
            writer.writerow([
                datetime.now(timezone.utc).isoformat(), mode, args.candidate_name,
                "GEOMEAN_all_configured_shapes", "", "", "", "", "", "", "", "", "",
                "", "", "", "", "", "", "",
                "", "", "", "", "", "", "",
                f"{_geom_mean(speedups_dev):.4f}", f"{_geom_mean(speedups_wall):.4f}",
                "", "", command, git_commit, source_hash,
                host, gpu_phys, "0", gpu_name, gpu_uuid,
                os.environ.get("CUDA_VISIBLE_DEVICES", ""),
                idle_before_detail, idle_after_detail, "", args.notes,
            ])
    if not args.baseline_only:
        print(f"GEOMEAN dev-speedup: {_geom_mean(speedups_dev):.4f}x "
              f"(wall {_geom_mean(speedups_wall):.4f}x)")
    print(f"rows appended to {csv_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
