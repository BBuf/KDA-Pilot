"""Symmetric same-process interleaved A/B benchmark for the diffusion norm kernels.

Both legs run in ONE process on ONE pinned GPU, resolved once before the timed
loop, interleaved per iteration (order swapped every iteration) to cancel clock
and contention drift. Every sample records wall time (perf_counter around
call+synchronize) AND device time (CUDA events), so each row decomposes into
device vs host components.

Leg topology is declared explicitly and asserted equal before any timing: the
baseline leg is the copied Triton implementation (baseline/triton_norm_baseline.py,
provenance in docs/baseline_source.md) and the candidate leg is the local
dispatcher (src/norm_dispatch.py). Neither local leg carries a custom-op layer;
the registration-preserving comparison happens at the in-SGLang dispatch-toggle
arbiter, not here. A topology mismatch aborts the run.

GPU idle gating: REMOTE_GPU_ID must equal the first CUDA_VISIBLE_DEVICES entry;
the physical GPU must show zero compute apps, zero utilization, and near-zero
memory before CUDA initialization, and at most this process's own context after
the run. Gate states are recorded in every CSV row.

Usage (inside the sglang_bbuf container, from the synced task folder):
    REMOTE_GPU_ID=0 CUDA_VISIBLE_DEVICES=0 python3 benchmark_symmetric.py \
        --sglang-commit 84e1108312 --candidate-version normv5 \
        --warmup 30 --iters 200 --csv benchmark.csv

Self-test (no GPU): python3 benchmark_symmetric.py --self-test-symmetry
"""

from __future__ import annotations

import argparse
import csv
import datetime
import json
import os
import pathlib
import shutil
import statistics
import subprocess
import sys
import time

TASK_DIR = pathlib.Path(__file__).resolve().parent
SLUG = "h200_diffusion_norm_infer__multi_shape"

CSV_COLUMNS = [
    "ts", "mode", "shape", "dtype", "metric", "baseline_us", "candidate_us",
    "speedup_x", "median_us", "mean_us", "std_us", "min_us", "p10_us", "p90_us",
    "gpu_time_us", "achieved_gbps", "host", "gpu_id", "gpu_model",
    "sglang_commit", "candidate_version", "warmup", "iters", "command", "slug",
    "notes", "remote_kda_dir",
    # decomposition schema (continuation round)
    "integration_path", "registration_preserved", "device_us", "wall_us",
    "host_delta_us", "interleaved",
]

# The six captured production shapes (docs/captured_shapes_h200.jsonl) — frozen.
SHAPES = [
    {"name": "helios__f32__M8640N5120", "kind": "ln", "m": 8640, "n": 5120, "dtype": "float32"},
    {"name": "hunyuan__bf16__M648720D128", "kind": "rms", "m": 648720, "n": 128, "dtype": "bfloat16"},
    {"name": "hunyuan__bf16__M1320D128", "kind": "rms", "m": 1320, "n": 128, "dtype": "bfloat16"},
    {"name": "hunyuan__bf16__M650040D128", "kind": "rms", "m": 650040, "n": 128, "dtype": "bfloat16"},
    {"name": "zimage__bf16__M16384D128", "kind": "rms", "m": 16384, "n": 128, "dtype": "bfloat16"},
    {"name": "zimage__bf16__M4096D128", "kind": "rms", "m": 4096, "n": 128, "dtype": "bfloat16"},
]


class LegTopologyMismatch(SystemExit):
    """Raised (exit code 3) when the A/B legs do not share a host topology."""


def assert_symmetric_topology(meta_a: dict, meta_b: dict) -> None:
    """Both legs must share the same host-layer class: same call protocol, same
    registration story, same allocation policy. Implementation-owned guard code
    inside each leg is allowed (it ships with that implementation); an extra
    wrapper/registration layer on one side only is not."""
    keys = ("call_protocol", "registration", "allocation", "process")
    diff = {k: (meta_a.get(k), meta_b.get(k)) for k in keys if meta_a.get(k) != meta_b.get(k)}
    if diff:
        raise LegTopologyMismatch(
            f"asymmetric host topology between legs, refusing to benchmark: {diff}"
        )


LOCAL_TOPOLOGY = {
    "call_protocol": "plain-python-callable",
    "registration": "none-local",
    "allocation": "fresh-output-per-call",
    "process": "same-process-interleaved",
}


def _percentile(sorted_vals, frac):
    if not sorted_vals:
        return float("nan")
    idx = min(len(sorted_vals) - 1, max(0, int(round(frac * (len(sorted_vals) - 1)))))
    return sorted_vals[idx]


def summarize(samples):
    s = sorted(samples)
    return {
        "median": statistics.median(s),
        "mean": statistics.fmean(s),
        "std": statistics.pstdev(s) if len(s) > 1 else 0.0,
        "min": s[0],
        "p10": _percentile(s, 0.10),
        "p90": _percentile(s, 0.90),
    }


def gpu_pin_or_die():
    remote_gpu_id = os.environ.get("REMOTE_GPU_ID", "")
    cvd = os.environ.get("CUDA_VISIBLE_DEVICES", "")
    first = cvd.split(",")[0].strip() if cvd else ""
    if not remote_gpu_id or remote_gpu_id != first:
        sys.exit(
            f"GPU pin mismatch: REMOTE_GPU_ID={remote_gpu_id!r} must equal the "
            f"first CUDA_VISIBLE_DEVICES entry {first!r}"
        )
    return remote_gpu_id


def gpu_state(physical_id: str) -> dict:
    out = subprocess.run(
        ["nvidia-smi", "--query-gpu=utilization.gpu,memory.used",
         "--format=csv,noheader,nounits", "-i", physical_id],
        capture_output=True, text=True, check=True,
    ).stdout.strip()
    util, mem = [int(v.strip()) for v in out.split(",")]
    apps = subprocess.run(
        ["nvidia-smi", "--query-compute-apps=pid", "--format=csv,noheader", "-i", physical_id],
        capture_output=True, text=True, check=True,
    ).stdout.strip()
    n_apps = len([l for l in apps.splitlines() if l.strip()])
    return {"util": util, "mem_mib": mem, "apps": n_apps}


def ensure_csv_schema(csv_path: pathlib.Path) -> None:
    """Extend an existing ledger in place to the superset schema (old rows are
    padded with empty values for the new decomposition columns)."""
    if not csv_path.exists():
        with open(csv_path, "w", newline="") as f:
            csv.writer(f).writerow(CSV_COLUMNS)
        return
    with open(csv_path, newline="") as f:
        rows = list(csv.reader(f))
    if not rows:
        with open(csv_path, "w", newline="") as f:
            csv.writer(f).writerow(CSV_COLUMNS)
        return
    header = rows[0]
    if header == CSV_COLUMNS:
        return
    missing = [c for c in CSV_COLUMNS if c not in header]
    if not missing:
        return
    backup_dir = csv_path.parent / ".humanize"
    backup_dir.mkdir(exist_ok=True)
    stamp = datetime.datetime.now(datetime.timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    shutil.copy2(csv_path, backup_dir / f"benchmark.csv.bak-{stamp}")
    new_header = header + missing
    assert new_header == CSV_COLUMNS or set(new_header) == set(CSV_COLUMNS), (
        "unexpected legacy schema; refusing to migrate automatically"
    )
    with open(csv_path, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(new_header)
        for r in rows[1:]:
            w.writerow(r + [""] * (len(new_header) - len(r)))


def append_row(csv_path: pathlib.Path, row: dict) -> None:
    with open(csv_path, newline="") as f:
        header = next(csv.reader(f))
    with open(csv_path, "a", newline="") as f:
        csv.writer(f).writerow([row.get(c, "") for c in header])


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--mode", default="device-fair", choices=["device-fair"])
    ap.add_argument("--shapes", default="all",
                    help="comma list of shape names or 'all'")
    ap.add_argument("--warmup", type=int, default=30)
    ap.add_argument("--iters", type=int, default=200)
    ap.add_argument("--csv", default=str(TASK_DIR / "benchmark.csv"))
    ap.add_argument("--no-csv", action="store_true")
    ap.add_argument("--sglang-commit", default="")
    ap.add_argument("--candidate-version", default="normv5")
    ap.add_argument("--remote-kda-dir", default=os.environ.get("REMOTE_KDA_DIR", ""))
    ap.add_argument("--host", default=os.environ.get("KDA_HOST", "ion8-h200"))
    ap.add_argument("--notes", default="")
    ap.add_argument("--self-test-symmetry", action="store_true",
                    help="verify the topology guard trips on a mismatched leg pair (no GPU)")
    args = ap.parse_args()

    if args.self_test_symmetry:
        assert_symmetric_topology(dict(LOCAL_TOPOLOGY), dict(LOCAL_TOPOLOGY))
        bad = dict(LOCAL_TOPOLOGY, registration="custom-op-on-this-leg-only")
        try:
            assert_symmetric_topology(dict(LOCAL_TOPOLOGY), bad)
        except LegTopologyMismatch as e:
            print(f"symmetry guard OK (tripped as expected): {e}")
            return
        sys.exit("symmetry guard FAILED to trip on a mismatched leg pair")

    physical_id = gpu_pin_or_die()
    state_before = gpu_state(physical_id)
    if state_before["apps"] != 0 or state_before["util"] != 0 or state_before["mem_mib"] > 150:
        sys.exit(f"GPU {physical_id} not idle before run: {state_before}")

    import torch  # after the idle gate so the gate sees a context-free card

    sys.path.insert(0, str(TASK_DIR))
    sys.path.insert(0, str(TASK_DIR / "src"))
    from baseline.triton_norm_baseline import (
        baseline_norm_infer,
        baseline_one_pass_rms_norm,
    )
    import norm_dispatch  # src/norm_dispatch.py (candidate dispatcher)

    legs_meta = {"baseline": dict(LOCAL_TOPOLOGY), "candidate": dict(LOCAL_TOPOLOGY)}
    assert_symmetric_topology(legs_meta["baseline"], legs_meta["candidate"])

    wanted = [s["name"] for s in SHAPES] if args.shapes == "all" else [
        w.strip() for w in args.shapes.split(",") if w.strip()
    ]
    shapes = [s for s in SHAPES if s["name"] in wanted]
    unknown = set(wanted) - {s["name"] for s in shapes}
    if unknown:
        sys.exit(f"unknown shape names: {sorted(unknown)}")

    csv_path = pathlib.Path(args.csv)
    if not args.no_csv:
        ensure_csv_schema(csv_path)

    dev = "cuda"
    torch.manual_seed(0)
    command = " ".join(["python3"] + sys.argv)
    gpu_model = torch.cuda.get_device_name(0)
    ts_run = datetime.datetime.now(datetime.timezone.utc).isoformat()

    def wall_call(fn):
        """Per-call wall time: perf_counter around call + synchronize. No event
        instrumentation, so medians are directly comparable to the locked
        baseline methodology (docs/baseline_locked.json)."""
        t0 = time.perf_counter()
        fn()
        torch.cuda.synchronize()
        return (time.perf_counter() - t0) * 1e6

    BATCH = 32

    def device_batch(fn):
        """Stream-saturated per-call device time: one event pair around BATCH
        back-to-back enqueues with no intervening sync. While the stream is
        busy, the host enqueue gap is hidden, so elapsed/BATCH converges to the
        kernel duration for long kernels and to the enqueue/kernel rate limit
        for short ones — the production back-to-back throughput view."""
        ev_a = torch.cuda.Event(enable_timing=True)
        ev_b = torch.cuda.Event(enable_timing=True)
        ev_a.record()
        for _ in range(BATCH):
            fn()
        ev_b.record()
        torch.cuda.synchronize()
        return ev_a.elapsed_time(ev_b) * 1e3 / BATCH

    # No-op controls: instrumentation floors for both passes.
    noop = lambda: None
    for _ in range(10):
        wall_call(noop)
        device_batch(noop)
    control = {
        "wall_floor_us": statistics.median([wall_call(noop) for _ in range(50)]),
        "device_floor_us": statistics.median([device_batch(noop) for _ in range(20)]),
    }
    print(f"[control] instrumentation floors: wall={control['wall_floor_us']:.2f}us "
          f"device(batched/call)={control['device_floor_us']:.3f}us")

    results = []
    for spec in shapes:
        m, n = spec["m"], spec["n"]
        dtype = getattr(torch, spec["dtype"])
        x = torch.randn(m, n, device=dev, dtype=dtype)
        w = torch.randn(n, device=dev, dtype=dtype)
        if spec["kind"] == "ln":
            b = torch.randn(n, device=dev, dtype=dtype)
            run_base = lambda: baseline_norm_infer(x, w, b, eps=1e-6, is_rms_norm=False)
            run_cand = lambda: norm_dispatch.norm_infer(x, w, b, eps=1e-6, is_rms_norm=False)
            bytes_moved = 2 * m * n * x.element_size() + 2 * n * x.element_size()
        else:
            run_base = lambda: baseline_one_pass_rms_norm(x, w, 1e-6)
            run_cand = lambda: norm_dispatch.triton_one_pass_rms_norm(x, w, 1e-6)
            bytes_moved = 2 * m * n * x.element_size() + n * x.element_size()

        # Output sanity before timing: never benchmark a wrong candidate.
        out_b, out_c = run_base(), run_cand()
        if torch.isnan(out_c).any() or torch.isinf(out_c).any():
            sys.exit(f"{spec['name']}: candidate output has NaN/Inf, refusing to time")
        tol = 1e-5 if dtype == torch.float32 else 5e-2
        torch.testing.assert_close(out_c, out_b, atol=tol, rtol=tol)
        del out_b, out_c

        for _ in range(args.warmup):
            run_base()
            run_cand()
        torch.cuda.synchronize()

        # Pass 1: per-call wall time, interleaved per iteration, order swapped.
        wall = {"baseline": [], "candidate": []}
        for i in range(args.iters):
            order = (("baseline", run_base), ("candidate", run_cand)) if i % 2 == 0 \
                else (("candidate", run_cand), ("baseline", run_base))
            for leg, fn in order:
                wall[leg].append(wall_call(fn))

        # Pass 2: batched device time, interleaved per sample, order swapped.
        devt = {"baseline": [], "candidate": []}
        n_dev_samples = max(10, args.iters // 10)
        for i in range(n_dev_samples):
            order = (("baseline", run_base), ("candidate", run_cand)) if i % 2 == 0 \
                else (("candidate", run_cand), ("baseline", run_base))
            for leg, fn in order:
                devt[leg].append(device_batch(fn))

        row_common = {
            "ts": ts_run, "shape": spec["name"], "dtype": f"torch.{spec['dtype']}",
            "metric": "median_us", "host": args.host, "gpu_id": physical_id,
            "gpu_model": gpu_model, "sglang_commit": args.sglang_commit,
            "warmup": args.warmup, "iters": args.iters, "command": command,
            "slug": SLUG, "remote_kda_dir": args.remote_kda_dir,
            "interleaved": "true",
        }
        per_leg = {}
        for leg, integration, version in (
            ("baseline", "local_copied_triton_baseline", "baseline-copy@" + (args.sglang_commit or "unknown")),
            ("candidate", "local_dispatcher_tvmffi", args.candidate_version),
        ):
            st = summarize(wall[leg])
            dev_med = statistics.median(devt[leg])
            # Host component of a solo call: python wrapper + exposed enqueue
            # gap + synchronize, i.e. wall minus the stream-saturated kernel rate.
            host_med = st["median"] - dev_med
            per_leg[leg] = {"wall": st, "device": dev_med, "host": host_med}
            results.append({
                **row_common, "mode": "symmetric_leg",
                "candidate_version": version,
                "integration_path": integration,
                "registration_preserved": "none-local-both-legs",
                "median_us": f"{st['median']:.4f}", "mean_us": f"{st['mean']:.4f}",
                "std_us": f"{st['std']:.4f}", "min_us": f"{st['min']:.4f}",
                "p10_us": f"{st['p10']:.4f}", "p90_us": f"{st['p90']:.4f}",
                "gpu_time_us": f"{dev_med:.4f}", "device_us": f"{dev_med:.4f}",
                "wall_us": f"{st['median']:.4f}", "host_delta_us": f"{host_med:.4f}",
                "achieved_gbps": f"{bytes_moved / dev_med / 1e3:.1f}",
                "notes": args.notes,
            })
        b_med = per_leg["baseline"]["wall"]["median"]
        c_med = per_leg["candidate"]["wall"]["median"]
        dev_ratio = per_leg["baseline"]["device"] / per_leg["candidate"]["device"]
        results.append({
            **row_common, "mode": "symmetric_device_fair",
            "candidate_version": args.candidate_version,
            "integration_path": "local_symmetric_pair",
            "registration_preserved": "none-local-both-legs",
            "baseline_us": f"{b_med:.4f}", "candidate_us": f"{c_med:.4f}",
            "speedup_x": f"{b_med / c_med:.4f}",
            "device_us": f"{per_leg['candidate']['device']:.4f}",
            "wall_us": f"{c_med:.4f}",
            "host_delta_us": f"{per_leg['candidate']['host']:.4f}",
            "notes": json.dumps({
                "device_speedup_x": round(dev_ratio, 4),
                "baseline_device_us": round(per_leg["baseline"]["device"], 4),
                "baseline_host_delta_us": round(per_leg["baseline"]["host"], 4),
                "control_floor": {k: round(v, 4) for k, v in control.items()},
            }),
        })
        print(
            f"{spec['name']:30s} base wall={b_med:9.2f}us dev={per_leg['baseline']['device']:8.2f}us | "
            f"cand wall={c_med:9.2f}us dev={per_leg['candidate']['device']:8.2f}us | "
            f"wall x{b_med / c_med:5.3f} dev x{dev_ratio:5.3f}"
        )
        del x, w
        if spec["kind"] == "ln":
            del b
        torch.cuda.empty_cache()

    state_after = gpu_state(physical_id)
    if state_after["apps"] > 1:
        print(f"WARNING: GPU {physical_id} shows {state_after['apps']} compute apps "
              f"after the run (expected <=1: this process) — rows marked invalid")
        for r in results:
            r["notes"] = (r.get("notes", "") + " | INVALID: gpu-not-exclusive-after").strip(" |")
    gate = json.dumps({"before": state_before, "after": state_after})
    for r in results:
        r["notes"] = (r["notes"] + " | idle_gate=" + gate) if r.get("notes") else "idle_gate=" + gate

    if not args.no_csv:
        for r in results:
            append_row(csv_path, r)
        print(f"appended {len(results)} rows to {csv_path}")


if __name__ == "__main__":
    main()
