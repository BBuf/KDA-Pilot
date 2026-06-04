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


def _required_remote_gpu_id() -> str:
    """The recorded GPU selection contract: REMOTE_GPU_ID must be set and must
    match the first CUDA_VISIBLE_DEVICES entry. Abort before any case loads."""

    remote_id = os.environ.get("REMOTE_GPU_ID", "").strip()
    if not remote_id:
        raise SystemExit(
            "ABORT: REMOTE_GPU_ID is not set. Select an idle GPU per the ion-b200 "
            "skill, export REMOTE_GPU_ID, and set CUDA_VISIBLE_DEVICES to match."
        )
    cvd = os.environ.get("CUDA_VISIBLE_DEVICES", "")
    first = cvd.split(",")[0].strip() if cvd else ""
    if first != remote_id:
        raise SystemExit(
            f"ABORT: CUDA_VISIBLE_DEVICES (first entry {first!r}) does not match "
            f"REMOTE_GPU_ID ({remote_id!r}); refusing to record benchmark rows."
        )
    return remote_id


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


def _query_gpu_state(gpu: str, gpu_uuid: str) -> dict:
    """Structured snapshot of the selected GPU: utilization, memory, and the
    compute-app rows (gpu_uuid, pid, used_memory MiB) bound to that UUID.

    PID-namespace caveat: inside the container os.getpid() does not match the
    host PIDs reported by nvidia-smi, so per-PID self-attribution is impossible;
    classification therefore reasons about app COUNTS, not identities.
    """

    state: dict = {"uuid": gpu_uuid, "util_pct": None, "mem_used_mib": None,
                   "compute_apps": [], "query_error": None}
    util = _nvidia_smi("utilization.gpu", gpu)
    mem = _nvidia_smi("memory.used", gpu)
    try:
        state["util_pct"] = int(util)
        state["mem_used_mib"] = int(mem)
    except ValueError:
        state["query_error"] = f"unparseable util/mem: {util!r}/{mem!r}"
    try:
        out = subprocess.run(
            ["nvidia-smi", "--query-compute-apps=gpu_uuid,pid,used_memory",
             "--format=csv,noheader,nounits"],
            capture_output=True, text=True, timeout=30, check=True,
        )
        for line in out.stdout.strip().splitlines():
            parts = [p.strip() for p in line.split(",")]
            if len(parts) >= 3 and parts[0] == gpu_uuid:
                state["compute_apps"].append((parts[0], parts[1], parts[2]))
    except Exception as exc:  # noqa: BLE001
        state["query_error"] = f"compute-apps query failed: {exc!r}"
    return state


_START_MAX_UTIL_PCT = 5
_START_MAX_MEM_MIB = 2048
# End ceiling: same conservative bound. The benchmark's own end footprint was
# measured at ~1.1 GiB (one compute app); anything above the ceiling cannot be
# attributed to this process alone (no PID self-attribution in the container),
# so it is treated as contamination.
_END_MAX_MEM_MIB = 2048


def _describe_state(state: dict) -> str:
    apps = ";".join(f"pid={p} mem={m}MiB" for _, p, m in state["compute_apps"]) or "none"
    return (f"util={state['util_pct']}% mem={state['mem_used_mib']}MiB "
            f"apps=[{apps}]" + (f" err={state['query_error']}" if state["query_error"] else ""))


def _classify_start_state(state: dict) -> tuple[bool, str]:
    """Idle-at-start: queries succeeded, NO compute apps at all, utilization and
    memory both under conservative idle thresholds. High utilization is rejected
    even when no compute app is listed."""

    detail = _describe_state(state)
    if state["query_error"]:
        return False, detail
    if state["compute_apps"]:
        return False, detail
    if state["util_pct"] is None or state["util_pct"] > _START_MAX_UTIL_PCT:
        return False, detail
    if state["mem_used_mib"] is None or state["mem_used_mib"] > _START_MAX_MEM_MIB:
        return False, detail
    return True, detail


def _classify_end_state(state: dict) -> tuple[bool, str]:
    """Idle-at-end: this benchmark process is expected to be the single compute
    app on the card (PID-namespace caveat above), so ANY additional app means a
    foreign process joined mid-run. Memory is gated too: with zero apps, used
    memory above the end ceiling is memory-only contamination; with one app,
    memory above the ceiling cannot be proven to belong to this benchmark alone.
    Utilization is not gated at end — it is this process's own rolling work —
    but is recorded with explicit attribution."""

    detail = _describe_state(state) + " (end: util attributed to this benchmark process)"
    if state["query_error"]:
        return False, detail
    if len(state["compute_apps"]) > 1:
        return False, detail + " <- foreign compute app joined"
    if state["mem_used_mib"] is None or state["mem_used_mib"] > _END_MAX_MEM_MIB:
        return False, detail + " <- memory above end ceiling (foreign or unattributable)"
    return True, detail


def _gate_selftest() -> int:
    """Mocked-state checks for the gate logic (no GPU required)."""

    clean = {"uuid": "U", "util_pct": 0, "mem_used_mib": 12, "compute_apps": [], "query_error": None}
    busy_util = dict(clean, util_pct=99)  # the round-0 review counterexample
    busy_mem = dict(clean, mem_used_mib=150_000)
    foreign = dict(clean, compute_apps=[("U", "1234", "5000")])
    errored = dict(clean, query_error="boom")
    one_app_end = dict(clean, util_pct=50, mem_used_mib=1148, compute_apps=[("U", "1234", "1100")])
    two_apps_end = dict(clean, compute_apps=[("U", "1", "10"), ("U", "2", "10")])
    end_mem_only_contamination = dict(clean, mem_used_mib=6000)  # no apps, high memory
    end_one_app_high_mem = dict(clean, util_pct=50, mem_used_mib=6000,
                                compute_apps=[("U", "1234", "6000")])

    assert _classify_start_state(clean)[0] is True
    assert _classify_start_state(busy_util)[0] is False, "util=99 with no foreign pid must NOT be idle"
    assert _classify_start_state(busy_mem)[0] is False
    assert _classify_start_state(foreign)[0] is False
    assert _classify_start_state(errored)[0] is False
    assert _classify_end_state(one_app_end)[0] is True, "the benchmark's own ~1.1GiB end footprint stays admissible"
    assert _classify_end_state(two_apps_end)[0] is False
    assert _classify_end_state(errored)[0] is False
    assert _classify_end_state(end_mem_only_contamination)[0] is False, \
        "memory-only end contamination (no apps, high mem) must be rejected"
    assert _classify_end_state(end_one_app_high_mem)[0] is False, \
        "one-app high-memory end must be rejected (no PID self-attribution)"
    print("GATE_SELFTEST_PASS")
    return 0


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
    parser.add_argument("--gate-selftest", action="store_true",
                        help="run the mocked-state idle-gate logic checks and exit")
    args = parser.parse_args()

    if args.gate_selftest:
        return _gate_selftest()

    # GPU-selection contract first: abort before loading or timing anything.
    gpu_phys = _required_remote_gpu_id()

    if not torch.cuda.is_available():
        raise SystemExit("CUDA device required (run inside the remote container).")

    correctness = _load_correctness_module()
    cases = [c for c in correctness.make_cases() if c.get("bench")]
    if not cases:
        raise SystemExit("No bench=True cases configured.")

    register = correctness._register_module()

    gpu_uuid = _nvidia_smi("uuid", gpu_phys)
    gpu_name = _nvidia_smi("name", gpu_phys)
    # A just-exited CUDA process (e.g. a test run in the same session) can
    # linger in nvidia-smi for a few seconds; retry briefly before aborting.
    idle_before, idle_before_detail = _classify_start_state(_query_gpu_state(gpu_phys, gpu_uuid))
    for _ in range(3):
        if idle_before:
            break
        time.sleep(5)
        idle_before, idle_before_detail = _classify_start_state(_query_gpu_state(gpu_phys, gpu_uuid))
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

    idle_after, idle_after_detail = _classify_end_state(_query_gpu_state(gpu_phys, gpu_uuid))
    if not idle_after:
        raise SystemExit(
            f"ABORT: GPU {gpu_phys} foreign activity at end ({idle_after_detail}); "
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
