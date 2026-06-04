"""Benchmark harness for the norm-scale-shift kernel family.

Frozen workloads = the 39 unique captured signatures (bench/shapes.py).
For every case and implementation it reports two timing modes:

- ``endtoend``: per-iteration wall-clock around the public callable with a
  device synchronize per sample (host wrapper + dispatch + kernel);
- ``device``: CUDA-event stream-span around the same call. For
  stream-saturated (large) cases this approximates kernel duration; for
  host-starved (tiny) cases it includes launch-issue latency — NCU owns the
  kernel-duration ground truth there.

Baseline and candidate run interleaved in the same process on the same
pre-allocated inputs, so clock drift and allocator state affect both sides
equally. One-time JIT/build/compile happens during warmup, outside every
timed region. Rows are appended (append-only) to ``benchmark.csv`` with full
provenance. ``--report`` recomputes per-case speedups + the geomean over
unique signatures from the CSV.

Run inside the sglang_bbuf container on an idle B200, e.g.:
  CUDA_VISIBLE_DEVICES=0 python bench/benchmark.py --impl both --gpu-id 0 \
      --run-id baseline-v0
"""

from __future__ import annotations

import argparse
import csv
import importlib.util
import math
import os
import statistics
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

BENCH_DIR = Path(__file__).resolve().parent
KERNEL_DIR = BENCH_DIR.parent
CSV_PATH = KERNEL_DIR / "benchmark.csv"

CSV_COLUMNS = [
    "timestamp", "run_id", "case_id", "kernel", "models", "B", "S", "D",
    "sc_class", "sc_dtype", "gate_class", "gate_dtype", "has_wb", "eps",
    "impl", "mode", "warmup", "iters",
    "median_us", "mean_us", "std_us", "min_us", "p10_us", "p90_us",
    "dispatch_native", "host", "gpu_name", "gpu_uuid", "gpu_physical_index",
    "cuda_visible_devices", "torch_version", "sglang_commit",
    "candidate_src_hash", "idle_before_util", "idle_before_mem_mib",
    "idle_after_util", "idle_after_mem_mib", "command",
]

SGLANG_COMMIT = "edb1b3f8f5ab066af1e9b6ee8e8738fadcfa77e7"


def _load(name: str, path: Path):
    if name in sys.modules:
        return sys.modules[name]
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


def _shapes():
    return _load("kda_shapes", BENCH_DIR / "shapes.py")


def _correctness():
    return _load("kda_correctness_lib", BENCH_DIR / "correctness.py")


def _gpu_state(gpu_id: int):
    """(util%, mem_mib, name, uuid) for the selected PHYSICAL gpu index."""
    try:
        out = subprocess.run(
            ["nvidia-smi", "--query-gpu=index,utilization.gpu,memory.used,name,uuid",
             "--format=csv,noheader,nounits"],
            capture_output=True, text=True, timeout=20,
        ).stdout
        for line in out.strip().splitlines():
            idx, util, mem, name, uuid = [p.strip() for p in line.split(",")]
            if int(idx) == gpu_id:
                return int(util), int(mem), name, uuid
    except Exception:
        pass
    return -1, -1, "?", "?"


def _other_compute_apps(gpu_uuid: str):
    """Compute processes on the selected GPU excluding this benchmark process.

    The post-run device memory necessarily includes this process's own CUDA
    context, so run validity is gated on (a) device utilization reading 0
    after a settle period and (b) NO other process holding the GPU — not on
    the raw memory number. The external pre/post all-GPU snapshots taken by
    the orchestration script (after process exit) are the 0-util/0-mem proof.
    """
    apps = []
    try:
        out = subprocess.run(
            ["nvidia-smi", "--query-compute-apps=gpu_uuid,pid,used_memory",
             "--format=csv,noheader,nounits"],
            capture_output=True, text=True, timeout=20,
        ).stdout
        for line in out.strip().splitlines():
            if not line.strip():
                continue
            uuid, pid, mem = [p.strip() for p in line.split(",")]
            if uuid == gpu_uuid and int(pid) != os.getpid():
                apps.append((int(pid), int(mem)))
    except Exception:
        apps.append((-1, -1))  # fail closed: unknown state counts as dirty
    return apps


def _summary(samples_us):
    ordered = sorted(samples_us)
    n = len(ordered)

    def pct(p):
        return ordered[min(n - 1, max(0, round((n - 1) * p)))]

    return {
        "median_us": statistics.median(ordered),
        "mean_us": statistics.fmean(ordered),
        "std_us": statistics.pstdev(ordered) if n > 1 else 0.0,
        "min_us": ordered[0],
        "p10_us": pct(0.10),
        "p90_us": pct(0.90),
    }


def _case_meta(case):
    sm = _shapes()
    sig = case.sig
    B, S, D = sig.BSD
    sc = sig.operand("scale")
    gate = sig.operand("gate") if sig.kernel == sm.SRNSS else None
    weight = sig.operand("weight")
    return {
        "case_id": case.case_id,
        "kernel": "nss" if sig.kernel == sm.NSS else "srnss",
        "models": "+".join(case.models),
        "B": B, "S": S, "D": D,
        "sc_class": sc.layout_code(B, S, D) if sc else "none",
        "sc_dtype": sc.dtype_abbrev if sc else "none",
        "gate_class": gate.layout_code(B, S, D) if gate is not None else "none",
        "gate_dtype": gate.dtype_abbrev if gate is not None else "none",
        "has_wb": weight is not None,
        "eps": sig.eps,
    }


def _make_call(case, fns, tensors):
    sm = _shapes()
    sig = case.sig
    nss, srnss = fns
    if sig.kernel == sm.NSS:
        x, weight, bias, scale, shift = tensors

        def call():
            return nss(x, weight, bias, scale, shift, sig.norm_type, sig.eps)

    else:
        residual, x, gate, weight, bias, scale, shift = tensors

        def call():
            return srnss(
                residual, x, gate, weight, bias, scale, shift, sig.norm_type, sig.eps
            )

    return call


def run_benchmark(args) -> int:
    import torch

    lib = _correctness()
    sm = _shapes()
    cases, _ = sm.load_unique_cases()
    if args.cases:
        wanted = set(args.cases.split(","))
        cases = [c for c in cases if c.case_id in wanted]
        missing = wanted - {c.case_id for c in cases}
        if missing:
            raise SystemExit(f"unknown case ids: {sorted(missing)}")

    impls = ["baseline", "candidate"] if args.impl == "both" else [args.impl]
    fns = {name: lib.implementations(name) for name in impls}
    if "candidate" in impls:
        reg = lib.candidate_register()
        if args.candidate_layer == "shipping":
            # Symmetric host stacks: candidate behind the same custom-op layer
            # shape as the baseline's registered public op.
            fns["candidate"] = reg.shipping_entry_points()
        reg.dispatch_stats().clear()

    util_b, mem_b, gpu_name, gpu_uuid = _gpu_state(args.gpu_id)
    apps_b = _other_compute_apps(gpu_uuid)
    if util_b != 0 or mem_b != 0 or apps_b:
        print(
            f"RUN REJECTED (idle gate, before): gpu{args.gpu_id} util={util_b}% "
            f"mem={mem_b}MiB other_procs={apps_b}"
        )
        return 2
    host = os.uname().nodename
    command = " ".join(sys.argv)
    rows = []
    sync = torch.cuda.synchronize

    for case in cases:
        meta = _case_meta(case)
        tensors, _, _ = sm.build_inputs(case, device="cuda", seed=args.seed)
        calls = {name: _make_call(case, fns[name], tensors) for name in impls}
        # one-time JIT/build for every impl, outside any timed region
        for name in impls:
            calls[name]()
        sync()
        for mode in args.modes:
            # interleaved A/B: alternate impls inside the same mode pass
            sample_sets = {name: [] for name in impls}
            # warmup every impl, outside the timed region below
            for name in impls:
                for _ in range(args.warmup):
                    calls[name]()
            sync()
            if mode == "endtoend":
                for _ in range(args.iters):
                    for name in impls:
                        t0 = time.perf_counter()
                        calls[name]()
                        sync()
                        sample_sets[name].append((time.perf_counter() - t0) * 1e6)
            else:  # device
                evs = {
                    name: (
                        [torch.cuda.Event(enable_timing=True) for _ in range(args.iters)],
                        [torch.cuda.Event(enable_timing=True) for _ in range(args.iters)],
                    )
                    for name in impls
                }
                for i in range(args.iters):
                    for name in impls:
                        evs[name][0][i].record()
                        calls[name]()
                        evs[name][1][i].record()
                sync()
                for name in impls:
                    sample_sets[name] = [
                        evs[name][0][i].elapsed_time(evs[name][1][i]) * 1e3
                        for i in range(args.iters)
                    ]
            for name in impls:
                stats = _summary(sample_sets[name])
                dispatch_native = ""
                if name == "candidate":
                    counts = lib.candidate_register().dispatch_stats()
                    dispatch_native = str(counts.get("fallback", 0) == 0)
                rows.append({
                    **meta,
                    "timestamp": datetime.now(timezone.utc).isoformat(),
                    "run_id": args.run_id,
                    "impl": name,
                    "mode": mode,
                    "warmup": args.warmup,
                    "iters": args.iters,
                    **{k: f"{v:.3f}" for k, v in stats.items()},
                    "dispatch_native": dispatch_native,
                    "host": host,
                    "gpu_name": gpu_name,
                    "gpu_uuid": gpu_uuid,
                    "gpu_physical_index": args.gpu_id,
                    "cuda_visible_devices": os.environ.get("CUDA_VISIBLE_DEVICES", ""),
                    "torch_version": torch.__version__,
                    "sglang_commit": SGLANG_COMMIT,
                    "candidate_src_hash": _candidate_hash(),
                    "command": command,
                })
            print(
                f"[{case.case_id}][{mode}] "
                + " ".join(
                    f"{n}={_summary(sample_sets[n])['median_us']:.1f}us" for n in impls
                )
            )
        del tensors, calls
        torch.cuda.empty_cache()

    # Settle so the utilization sampling window clears our own tail activity,
    # then gate on util==0 and no OTHER compute process (the remaining device
    # memory is this process's own CUDA context; see _other_compute_apps).
    torch.cuda.empty_cache()
    time.sleep(3)
    util_a, mem_a, _, _ = _gpu_state(args.gpu_id)
    apps_a = _other_compute_apps(gpu_uuid)
    for row in rows:
        row["idle_before_util"] = util_b
        row["idle_before_mem_mib"] = mem_b
        row["idle_after_util"] = util_a
        row["idle_after_mem_mib"] = mem_a

    write_header = not CSV_PATH.exists() or CSV_PATH.stat().st_size == 0
    with CSV_PATH.open("a", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=CSV_COLUMNS)
        if write_header:
            writer.writeheader()
        writer.writerows(rows)
    print(f"appended {len(rows)} rows to {CSV_PATH}")

    if "candidate" in impls:
        counts = lib.candidate_register().dispatch_stats()
        print(f"dispatch stats: {dict(counts)}")
        if counts.get("fallback", 0) > 0:
            print("WARNING: candidate fell back on some production cases!")
            return 1
    if util_a != 0 or apps_a:
        print(
            f"RUN REJECTED (idle gate, after): gpu{args.gpu_id} util={util_a}% "
            f"other_procs={apps_a} (rows were appended for the record; do NOT "
            f"use this run_id as promotion evidence)"
        )
        return 2
    print(
        f"idle gate PASS: gpu{args.gpu_id} before util/mem 0/0, no other procs; "
        f"after util 0, no other procs (own-context mem {mem_a} MiB; external "
        f"post-exit snapshot is the 0/0 proof)"
    )
    return 0


def _candidate_hash() -> str:
    """Joint hash binding the FULL candidate behavior: device source plus the
    wrapper/registration layers whose flags select the shipped configuration."""
    import hashlib

    h = hashlib.sha1()
    for rel in ("src/csrc/norm_scale_shift.cuh", "src/wrapper.py", "src/register.py"):
        p = KERNEL_DIR / rel
        if p.exists():
            h.update(rel.encode())
            h.update(p.read_bytes())
    return h.hexdigest()[:12]


def report(args) -> int:
    """Per-case speedups + geomean over unique signatures from benchmark.csv."""
    by_key = {}
    with CSV_PATH.open() as fh:
        for row in csv.DictReader(fh):
            if args.run_id and row["run_id"] != args.run_id:
                continue
            key = (row["case_id"], row["mode"], row["impl"])
            by_key[key] = float(row["median_us"])  # latest wins
    modes = sorted({k[1] for k in by_key})
    for mode in modes:
        speedups = []
        print(f"\n== mode: {mode} (run_id={args.run_id or 'latest-any'}) ==")
        case_ids = sorted({k[0] for k in by_key if k[1] == mode})
        for cid in case_ids:
            b = by_key.get((cid, mode, "baseline"))
            c = by_key.get((cid, mode, "candidate"))
            if b is None or c is None:
                continue
            s = b / c
            speedups.append(s)
            print(f"  {cid}: baseline={b:.1f}us candidate={c:.1f}us speedup={s:.3f}x")
        if speedups:
            geo = math.exp(sum(math.log(s) for s in speedups) / len(speedups))
            print(f"  -> geomean over {len(speedups)} unique signatures: {geo:.4f}x")
    return 0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--impl", choices=["baseline", "candidate", "both"], default="both")
    ap.add_argument("--modes", nargs="+", default=["endtoend", "device"],
                    choices=["endtoend", "device"])
    ap.add_argument("--warmup", type=int, default=20)
    ap.add_argument("--iters", type=int, default=100)
    ap.add_argument("--seed", type=int, default=20260604)
    ap.add_argument("--gpu-id", type=int, default=int(os.environ.get("REMOTE_GPU_ID", 0)))
    # None by default: report mode aggregates across all runs (latest-any);
    # a timestamped id is synthesized only for actual benchmark runs.
    ap.add_argument("--run-id", default=None)
    ap.add_argument("--cases", default="", help="comma-separated case_id filter")
    ap.add_argument("--candidate-layer", choices=["shipping", "plain"], default="shipping",
                    help="candidate host stack: custom-op-wrapped (symmetric) or plain callable")
    ap.add_argument("--report", action="store_true", help="aggregate csv instead of running")
    args = ap.parse_args()
    if args.report:
        sys.exit(report(args))
    if args.run_id is None:
        args.run_id = datetime.now(timezone.utc).strftime("run-%Y%m%d-%H%M%S")
    sys.exit(run_benchmark(args))


if __name__ == "__main__":
    main()
