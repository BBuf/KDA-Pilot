#!/usr/bin/env python3
"""Benchmark runner: same-process interleaved A/B (vendored baseline vs candidate).

Both sides are called through the identical thin local entry ABI (a plain
Python function call into baseline/ or solution/dispatch). Below that ABI the
HOST LAUNCH STACKS legitimately differ (Triton Python wrapper + JIT dispatch
vs dispatcher gate + tvm-ffi call) — that difference is measured and reported
SEPARATELY from device time (see the three views below); the in-SGLang
in-tree drop-in remains the final arbiter for integration-path claims.
Three timing views per shape:

- sync_wall:  per-call wall time with a device synchronize after each call
              (end-to-end latency view: host submit + device + sync).
- device_ev:  per-call CUDA-event elapsed time (device-side view; the
              device-vs-host decomposition uses sync_wall - device_ev).
- amort_wall: per-block amortized wall time of back-to-back calls with one
              trailing synchronize (pipelined-submission view; on tiny shapes
              this exposes pure host submission cost).

Per shape it reports median/mean/std/min/p10/p90 for both sides and appends a
single CSV row per (shape, metric) to benchmark.csv (schema below) plus a raw
JSON log. GPU idleness is checked before and after the run; rows from a
non-idle GPU are marked valid=False.

Usage (inside the remote container, idle GPU selected via CUDA_VISIBLE_DEVICES):
  python bench/benchmark.py --gpu-id $REMOTE_GPU_ID --tag <candidate_id> [--filter SUBSTR]
"""

from __future__ import annotations

import argparse
import csv
import json
import os
import shlex
import socket
import statistics
import subprocess
import sys
import time
from pathlib import Path

KERNEL_DIR = Path(__file__).resolve().parents[1]
if str(KERNEL_DIR) not in sys.path:
    sys.path.insert(0, str(KERNEL_DIR))

import torch  # noqa: E402

from bench import cases as cases_mod  # noqa: E402
from bench import ledger  # noqa: E402

BENCH_CSV = KERNEL_DIR / "benchmark.csv"

CSV_FIELDS = [
    "ts", "host", "gpu_id", "gpu_name", "shape_id", "op", "route", "metric",
    "candidate_id", "candidate_commit", "warmup", "iters",
    "base_median_us", "base_mean_us", "base_std_us", "base_min_us", "base_p10_us", "base_p90_us",
    "cand_median_us", "cand_mean_us", "cand_std_us", "cand_min_us", "cand_p10_us", "cand_p90_us",
    "speedup_median", "valid", "idle_before", "idle_after", "command", "evidence_path", "notes",
]


def _runtime():
    from baseline import scale_shift as baseline_mod
    from solution import dispatch

    baseline_fns = {
        cases_mod.OP_SCALE_SHIFT: baseline_mod.fuse_scale_shift_kernel,
        cases_mod.OP_SELECT01: baseline_mod.fuse_layernorm_scale_shift_gate_select01_kernel,
        cases_mod.OP_RESIDUAL: (
            baseline_mod.fuse_residual_layernorm_scale_shift_gate_select01_kernel
        ),
    }
    dispatch_fns = {
        cases_mod.OP_SCALE_SHIFT: dispatch.fuse_scale_shift_kernel,
        cases_mod.OP_SELECT01: dispatch.fuse_layernorm_scale_shift_gate_select01_kernel,
        cases_mod.OP_RESIDUAL: (
            dispatch.fuse_residual_layernorm_scale_shift_gate_select01_kernel
        ),
    }
    return baseline_fns, dispatch_fns, dispatch


# ---------------------------------------------------------------------------
# GPU idleness
# ---------------------------------------------------------------------------

def gpu_snapshot(gpu_id: str, baseline_pids: set[int] | None = None) -> dict:
    """Query nvidia-smi for the physical GPU.

    Idleness rule: before the run (baseline_pids=None) the GPU must have NO
    compute processes at all. After the run, the only allowed NEW process vs
    the before-snapshot is our own CUDA context. Note: inside a container,
    nvidia-smi reports HOST pids while os.getpid() is namespace-local, so
    self-identification must go through the before/after pid-set delta, not
    pid equality.
    """
    snap = {"gpu_id": gpu_id, "procs": None, "util": None, "mem_used_mib": None,
            "idle": None, "error": ""}
    try:
        out = subprocess.run(
            ["nvidia-smi", "-i", gpu_id,
             "--query-gpu=utilization.gpu,memory.used,name",
             "--format=csv,noheader,nounits"],
            capture_output=True, text=True, timeout=20, check=True,
        ).stdout.strip()
        util, mem, name = [s.strip() for s in out.split(",")[:3]]
        snap.update(util=int(util), mem_used_mib=int(mem), gpu_name=name)
        out = subprocess.run(
            ["nvidia-smi", "-i", gpu_id,
             "--query-compute-apps=pid", "--format=csv,noheader"],
            capture_output=True, text=True, timeout=20, check=True,
        ).stdout.strip()
        pids = [int(p) for p in out.splitlines() if p.strip()]
        snap["procs"] = pids
        if baseline_pids is None:
            snap["idle"] = len(pids) == 0
        else:
            new_pids = set(pids) - set(baseline_pids)
            snap["idle"] = len(new_pids) <= 1  # the single new context is ours
    except Exception as exc:  # noqa: BLE001 - report, don't crash the bench
        snap["error"] = f"{type(exc).__name__}: {exc}"
        snap["idle"] = None
    return snap


# ---------------------------------------------------------------------------
# Timing primitives (samples in microseconds)
# ---------------------------------------------------------------------------

def _stats(samples: list[float]) -> dict:
    s = sorted(samples)
    n = len(s)

    def pct(p: float) -> float:
        return s[min(n - 1, max(0, round((n - 1) * p)))]

    return {
        "median_us": statistics.median(s),
        "mean_us": statistics.fmean(s),
        "std_us": statistics.pstdev(s) if n > 1 else 0.0,
        "min_us": s[0],
        "p10_us": pct(0.10),
        "p90_us": pct(0.90),
        "n": n,
    }


def time_pair_sync_wall(fn_a, fn_b, args, kwargs, iters: int):
    a, b = [], []
    for i in range(iters):
        first, store_first, second, store_second = (
            (fn_a, a, fn_b, b) if i % 2 == 0 else (fn_b, b, fn_a, a)
        )
        t0 = time.perf_counter()
        first(*args, **kwargs)
        torch.cuda.synchronize()
        store_first.append((time.perf_counter() - t0) * 1e6)
        t0 = time.perf_counter()
        second(*args, **kwargs)
        torch.cuda.synchronize()
        store_second.append((time.perf_counter() - t0) * 1e6)
    return a, b


def time_pair_device_events(fn_a, fn_b, args, kwargs, iters: int):
    evs = [[torch.cuda.Event(enable_timing=True) for _ in range(4)] for _ in range(iters)]
    a, b = [], []
    for i in range(iters):
        e0, e1, e2, e3 = evs[i]
        if i % 2 == 0:
            e0.record(); fn_a(*args, **kwargs); e1.record()
            e2.record(); fn_b(*args, **kwargs); e3.record()
        else:
            e0.record(); fn_b(*args, **kwargs); e1.record()
            e2.record(); fn_a(*args, **kwargs); e3.record()
    torch.cuda.synchronize()
    for i in range(iters):
        e0, e1, e2, e3 = evs[i]
        first = e0.elapsed_time(e1) * 1e3  # ms -> us
        second = e2.elapsed_time(e3) * 1e3
        if i % 2 == 0:
            a.append(first); b.append(second)
        else:
            b.append(first); a.append(second)
    return a, b


def time_pair_amortized(fn_a, fn_b, args, kwargs, blocks: int, block_size: int):
    a, b = [], []
    for i in range(blocks):
        order = (fn_a, a, fn_b, b) if i % 2 == 0 else (fn_b, b, fn_a, a)
        for fn, store in (order[:2], order[2:]):
            torch.cuda.synchronize()
            t0 = time.perf_counter()
            for _ in range(block_size):
                fn(*args, **kwargs)
            torch.cuda.synchronize()
            store.append((time.perf_counter() - t0) * 1e6 / block_size)
    return a, b


# ---------------------------------------------------------------------------
# Per-case benchmark
# ---------------------------------------------------------------------------

def bench_case(case, device, *, warmup: int, iters: int, tag: str, notes: str) -> dict:
    baseline_fns, dispatch_fns, dispatch = _runtime()
    base_fn = baseline_fns[case.op]
    cand_fn = dispatch_fns[case.op]
    args, kwargs = case.build(device)

    # Route of the candidate path (recorded; fallback rows count as ~1.0x).
    cand_fn(*args, **kwargs)
    route = dispatch.consume_last_route()
    route_str = f"{route[0]}:{route[1]}" if route else "unknown"

    # Warmup both sides (covers Triton autotune on the baseline 4D path).
    for i in range(max(warmup, 8)):
        (base_fn if i % 2 == 0 else cand_fn)(*args, **kwargs)
    torch.cuda.synchronize()

    if iters <= 0:  # auto: target ~60ms of samples per side, clamped
        probe = time_pair_sync_wall(base_fn, cand_fn, args, kwargs, 5)
        med = statistics.median(probe[0])
        iters = int(min(max(60_000.0 / max(med, 1.0), 50), 1500))

    res = {}
    b, c = time_pair_sync_wall(base_fn, cand_fn, args, kwargs, iters)
    res["sync_wall"] = (_stats(b), _stats(c))
    b, c = time_pair_device_events(base_fn, cand_fn, args, kwargs, iters)
    res["device_ev"] = (_stats(b), _stats(c))
    blocks = max(10, min(40, iters // 10))
    b, c = time_pair_amortized(base_fn, cand_fn, args, kwargs, blocks, 10)
    res["amort_wall"] = (_stats(b), _stats(c))

    out = {"shape_id": case.case_id, "op": case.op, "route": route_str,
           "warmup": warmup, "iters": iters, "tag": tag, "notes": notes, "metrics": {}}
    for metric, (bs, cs) in res.items():
        out["metrics"][metric] = {
            "base": bs, "cand": cs,
            "speedup_median": bs["median_us"] / cs["median_us"] if cs["median_us"] else 0.0,
        }
    return out


def append_csv_rows(result: dict, *, env: dict, command: str, evidence_path: str) -> None:
    new_file = not BENCH_CSV.exists() or BENCH_CSV.stat().st_size == 0
    with open(BENCH_CSV, "a", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=CSV_FIELDS)
        if new_file:
            w.writeheader()
        for metric, m in result["metrics"].items():
            row = {
                "ts": env["ts"], "host": env["host"], "gpu_id": env["gpu_id"],
                "gpu_name": env["gpu_name"], "shape_id": result["shape_id"],
                "op": result["op"], "route": result["route"], "metric": metric,
                "candidate_id": result["tag"], "candidate_commit": env["commit"],
                "warmup": result["warmup"], "iters": result["iters"],
                "speedup_median": f"{m['speedup_median']:.4f}",
                "valid": env["valid"], "idle_before": env["idle_before"],
                "idle_after": env["idle_after"], "command": command,
                "evidence_path": evidence_path, "notes": result["notes"],
            }
            for side, key in (("base", "base"), ("cand", "cand")):
                for stat in ("median_us", "mean_us", "std_us", "min_us", "p10_us", "p90_us"):
                    row[f"{key}_{stat}"] = f"{m[side][stat]:.2f}"
            w.writerow(row)


def geomean_report(csv_path: Path, metric: str, candidate_id: str | None) -> dict:
    import math

    rows = []
    with open(csv_path) as fh:
        for row in csv.DictReader(fh):
            if row["metric"] != metric:
                continue
            if candidate_id and row["candidate_id"] != candidate_id:
                continue
            rows.append(row)
    latest: dict[str, dict] = {}
    for row in rows:  # keep the last row per shape (file is append-ordered)
        latest[row["shape_id"]] = row
    if not latest:
        return {"error": "no matching rows"}
    invalid = [k for k, v in latest.items() if v["valid"] != "True"]
    valid_latest = {k: v for k, v in latest.items() if v["valid"] == "True"}
    if not valid_latest:
        return {"error": "all latest rows are invalid", "invalid_rows": invalid}
    speedups = {k: float(v["speedup_median"]) for k, v in valid_latest.items()}
    gm = math.exp(sum(math.log(s) for s in speedups.values()) / len(speedups))
    return {
        "metric": metric, "candidate_id": candidate_id, "n_shapes": len(speedups),
        "geomean_speedup": round(gm, 4),
        "per_shape": {k: round(v, 4) for k, v in sorted(speedups.items())},
        "invalid_rows": invalid,  # excluded from the geomean above
    }


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--suite", default="production", choices=["production", "grid"])
    ap.add_argument("--filter", default="")
    ap.add_argument("--gpu-id", default=os.environ.get("REMOTE_GPU_ID", "0"),
                    help="PHYSICAL GPU id for nvidia-smi idleness checks")
    ap.add_argument("--warmup", type=int, default=30)
    ap.add_argument("--iters", type=int, default=0, help="0 = auto (~60ms/side)")
    ap.add_argument("--tag", default="dev", help="candidate id recorded in the CSV")
    ap.add_argument("--notes", default="")
    ap.add_argument("--geomean", action="store_true",
                    help="report geomean from benchmark.csv and exit")
    ap.add_argument("--metric", default="sync_wall",
                    choices=["sync_wall", "device_ev", "amort_wall"])
    ap.add_argument("--candidate-id", default=None, help="filter for --geomean")
    args = ap.parse_args()

    if args.geomean:
        print(json.dumps(geomean_report(BENCH_CSV, args.metric, args.candidate_id), indent=2))
        return 0

    if not torch.cuda.is_available():
        print("ERROR: CUDA device required", file=sys.stderr)
        return 2

    snap_before = gpu_snapshot(args.gpu_id)
    device = torch.device("cuda")
    gpu_name = torch.cuda.get_device_name(device)
    print(f"gpu: {gpu_name} (physical id {args.gpu_id})  idle_before={snap_before['idle']}")

    case_list = [c for c in cases_mod.all_cases((args.suite,)) if args.filter in c.case_id]
    print(f"benchmarking {len(case_list)} cases (suite={args.suite}, tag={args.tag})")

    results = []
    for case in case_list:
        r = bench_case(case, device, warmup=args.warmup, iters=args.iters,
                       tag=args.tag, notes=args.notes)
        results.append(r)
        m = r["metrics"]
        print(f"  {r['shape_id']:60s} route={r['route']:32s} "
              f"sync {m['sync_wall']['base']['median_us']:9.1f} -> "
              f"{m['sync_wall']['cand']['median_us']:9.1f} us "
              f"({m['sync_wall']['speedup_median']:.3f}x) | "
              f"dev {m['device_ev']['base']['median_us']:9.1f} -> "
              f"{m['device_ev']['cand']['median_us']:9.1f} us "
              f"({m['device_ev']['speedup_median']:.3f}x)")

    snap_after = gpu_snapshot(args.gpu_id, baseline_pids=set(snap_before.get("procs") or []))
    valid = bool(snap_before.get("idle")) and bool(snap_after.get("idle"))

    ts = time.strftime("%Y-%m-%d_%H-%M-%S")
    report_dir = Path(os.environ.get("REMOTE_KDA_DIR", KERNEL_DIR / "bench" / "reports"))
    report_dir = report_dir / "bench_logs" if "REMOTE_KDA_DIR" in os.environ else report_dir
    report_dir.mkdir(parents=True, exist_ok=True)
    evidence_name = f"bench_{args.tag}_{ts}.json"
    evidence_path = report_dir / evidence_name
    # CSV rows carry the repo-relative mirror path (remote logs are synced back
    # under bench/reports/remote_r0/); the raw write location is in the JSON.
    evidence_rel = f"bench/reports/remote_r0/{evidence_name}" \
        if "REMOTE_KDA_DIR" in os.environ else str(evidence_path)

    env = {
        "ts": ts, "host": socket.gethostname(), "gpu_id": args.gpu_id,
        "gpu_name": gpu_name, "commit": ledger.git_head(), "valid": valid,
        "idle_before": snap_before.get("idle"), "idle_after": snap_after.get("idle"),
    }
    command = "python " + " ".join(shlex.quote(a) for a in sys.argv)
    for r in results:
        append_csv_rows(r, env=env, command=command, evidence_path=evidence_rel)

    evidence_path.write_text(json.dumps(
        {"env": env, "snap_before": snap_before, "snap_after": snap_after,
         "command": command, "torch": torch.__version__, "results": results}, indent=1))
    print(f"valid={valid}  csv={BENCH_CSV}  evidence={evidence_path}")
    if not valid:
        print("WARNING: GPU not idle before/after — rows marked invalid", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
