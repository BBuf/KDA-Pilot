#!/usr/bin/env python3
"""Extract per-kernel GPU-time shares + CPU-op provenance from a torch trace.

Produces the ``kernel_shapes_<label>.json`` rows that ``build_e2e_tasks.py``
consumes:

```json
{"label": "...", "total_gpu_us": 1.0, "rows": [
  {"kernel": "<gpu kernel name>", "category": "<coarse bucket>",
   "pct_of_gpu": 12.3, "count": 456, "total_us": 1234.5,
   "top_cpu_ops": ["sglang::foo", ...],
   "samples": [{"cpu_op": "sglang::foo", "dur_us": 3.1,
                "shape_args": {"Input Dims": "[[1, 7168], ...]"}}]}]}
```

Provenance is resolved through the profiler's ``correlation`` id (kernel ->
launching runtime call) and then to the innermost enclosing ``cpu_op`` on the
launching thread, which is how the kernel gets named after a clean
``sglang`` / ``sgl_kernel`` / ``jit_kernel`` Python interface.

Usage (one trace per cookbook scenario label):

```bash
python3 extract_kernel_shapes.py \
    --trace TP-0.trace.json.gz --label random_low --out-dir shapes/
```
"""

from __future__ import annotations

import argparse
import gzip
import io
import json
import pathlib
import re
from bisect import bisect_right
from collections import defaultdict

# Coarse category buckets. Order matters: the first match wins, and the
# comm / vendor-fused-MoE buckets must be reachable so build_e2e_tasks.py can
# exclude them.
CATEGORIES: list[tuple[str, str]] = [
    (r"all_reduce|allreduce|all_to_all|alltoall|reduce_scatter|all_gather|nccl|"
     r"cross_device_reduce|custom_all_reduce|multimem", "comm"),
    (r"moe::dev|routingcustom|finalizekernel|activationkernel", "moe"),
    (r"bmm_|mxe2m1|mxe4m3|fused_experts|fused_moe|marlin|moe_sum|moe_align|"
     r"topk|route_radix|moe_front|situ", "moe"),
    (r"fmha|flash_fwd|flashinfer|batchprefill|batchdecode|paged|attn_res|"
     r"kda_|mla|attention", "attention"),
    (r"quant|scale_shift", "quant_gemm"),
    (r"gemm|nvjet|cutlass|sgemm|scaled_mm|tgv", "quant_gemm"),
    (r"rmsnorm|rms_norm|layernorm|norm", "norm"),
    (r"rope|rotary", "rope"),
    (r"memcpy|memset|copy", "memory"),
    (r"elementwise|vectorized|silu|gelu|add", "elementwise"),
]


def categorize(name: str) -> str:
    low = name.lower()
    for pattern, cat in CATEGORIES:
        if re.search(pattern, low):
            return cat
    return "other"


def load_events(path: pathlib.Path) -> list[dict]:
    """Load traceEvents, tolerating a truncated file.

    A trace whose server was killed mid-export leaves an unfinished gzip
    stream; the events written before the cut are still usable for GPU-time
    shares and CPU-op provenance, so decompress as far as possible and close
    the JSON at the last complete event.
    """
    opener = gzip.open if path.suffix == ".gz" else open
    chunks: list[str] = []
    truncated = False
    with opener(path, "rt", errors="replace") as handle:  # type: ignore[operator]
        while True:
            try:
                chunk = handle.read(64 << 20)
            except EOFError:
                truncated = True
                break
            if not chunk:
                break
            chunks.append(chunk)
    text = "".join(chunks)
    try:
        return json.load(io.StringIO(text)).get("traceEvents", [])
    except json.JSONDecodeError:
        truncated = True
    start = text.find('"traceEvents"')
    if start < 0:
        raise SystemExit(f"{path}: no traceEvents and unrecoverable truncation")
    start = text.index("[", start)
    cut = text.rindex("}", start)
    events = json.loads(text[start : cut + 1] + "]")
    if truncated:
        print(f"  note: {path.name} is truncated; recovered {len(events)} events")
    return events


def build_cpu_op_index(events: list[dict]) -> dict[int, list[tuple]]:
    """Per-thread sorted (start, end, name, shape_args) for cpu_op rows."""
    per_thread: dict[int, list[tuple]] = defaultdict(list)
    for event in events:
        if event.get("ph") != "X" or event.get("cat") != "cpu_op":
            continue
        start = event.get("ts")
        dur = event.get("dur") or 0.0
        if start is None:
            continue
        args = event.get("args") or {}
        shape_args = {
            key: str(args[key])[:400]
            for key in ("Input Dims", "Input type", "Concrete Inputs")
            if key in args
        }
        per_thread[event.get("tid")].append(
            (start, start + dur, event.get("name", ""), shape_args)
        )
    for rows in per_thread.values():
        rows.sort(key=lambda row: row[0])
    return per_thread


def innermost_cpu_op(index: dict[int, list[tuple]], tid, ts) -> tuple | None:
    """Smallest cpu_op on `tid` whose span contains `ts` (the launch site)."""
    rows = index.get(tid)
    if not rows or ts is None:
        return None
    cut = bisect_right(rows, (ts, float("inf"), "", {}))
    best = None
    # cpu_op nesting is shallow; scanning a bounded window back is enough.
    for start, end, name, shape_args in reversed(rows[max(0, cut - 400) : cut]):
        if start <= ts <= end and (best is None or (end - start) < best[0]):
            best = (end - start, name, shape_args)
    return (best[1], best[2]) if best else None


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--trace", required=True)
    parser.add_argument("--label", required=True)
    parser.add_argument("--out-dir", required=True)
    parser.add_argument("--max-samples", type=int, default=3)
    parser.add_argument(
        "--min-pct",
        type=float,
        default=0.05,
        help="drop kernels below this %% of GPU time (keeps the file small)",
    )
    parser.add_argument(
        "--provenance-from",
        help=(
            "optional kernel_shapes_*.json from a CPU+GPU trace: fills "
            "top_cpu_ops/samples per kernel name. Lets the per-scenario shares "
            "come from small GPU-only traces (a CPU+GPU trace at serving "
            "concurrency is large enough that its export trips the request "
            "watchdog) while the kernel -> Python interface mapping, which is "
            "scenario-independent, comes from one short CPU+GPU window."
        ),
    )
    args = parser.parse_args()

    provenance: dict[str, dict] = {}
    if args.provenance_from:
        for row in json.loads(pathlib.Path(args.provenance_from).read_text())["rows"]:
            if row.get("top_cpu_ops") or row.get("samples"):
                provenance[row["kernel"]] = row

    events = load_events(pathlib.Path(args.trace))
    cpu_index = build_cpu_op_index(events)

    # correlation id -> launching runtime call (ts, tid)
    launch_by_corr: dict[int, tuple] = {}
    for event in events:
        if event.get("ph") != "X" or event.get("cat") not in (
            "cuda_runtime",
            "cuda_driver",
        ):
            continue
        corr = (event.get("args") or {}).get("correlation")
        if corr is not None:
            launch_by_corr[corr] = (event.get("ts"), event.get("tid"))

    stats: dict[str, dict] = defaultdict(
        lambda: {"total_us": 0.0, "count": 0, "cpu_ops": defaultdict(float), "samples": []}
    )
    total_gpu_us = 0.0
    for event in events:
        if event.get("ph") != "X" or event.get("cat") not in ("kernel", "gpu_memcpy"):
            continue
        name = event.get("name", "")
        dur = event.get("dur") or 0.0
        total_gpu_us += dur
        entry = stats[name]
        entry["total_us"] += dur
        entry["count"] += 1
        corr = (event.get("args") or {}).get("correlation")
        launch = launch_by_corr.get(corr) if corr is not None else None
        resolved = innermost_cpu_op(cpu_index, launch[1], launch[0]) if launch else None
        if resolved:
            cpu_op, shape_args = resolved
            entry["cpu_ops"][cpu_op] += dur
            if len(entry["samples"]) < args.max_samples:
                entry["samples"].append(
                    {
                        "cpu_op": cpu_op,
                        "dur_us": round(dur, 3),
                        "shape_args": shape_args,
                    }
                )

    rows = []
    for name, entry in stats.items():
        pct = 100.0 * entry["total_us"] / total_gpu_us if total_gpu_us else 0.0
        if pct < args.min_pct:
            continue
        top_cpu_ops = [
            op
            for op, _ in sorted(entry["cpu_ops"].items(), key=lambda kv: -kv[1])[:5]
        ]
        samples = entry["samples"]
        if not top_cpu_ops and name in provenance:
            top_cpu_ops = provenance[name].get("top_cpu_ops", [])
            samples = provenance[name].get("samples", [])
        rows.append(
            {
                "kernel": name,
                "category": categorize(name),
                "pct_of_gpu": round(pct, 4),
                "count": entry["count"],
                "total_us": round(entry["total_us"], 2),
                "top_cpu_ops": top_cpu_ops,
                "samples": samples,
            }
        )
    rows.sort(key=lambda row: -row["pct_of_gpu"])

    out_dir = pathlib.Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / f"kernel_shapes_{args.label}.json"
    out_path.write_text(
        json.dumps(
            {
                "label": args.label,
                "trace": str(args.trace),
                "total_gpu_us": round(total_gpu_us, 2),
                "rows": rows,
            },
            indent=2,
        )
    )
    print(f"{out_path}: {len(rows)} kernels, {total_gpu_us / 1000:.1f} ms GPU time")
    for row in rows[:10]:
        provenance = row["top_cpu_ops"][0] if row["top_cpu_ops"] else "-"
        print(f"  {row['pct_of_gpu']:5.1f}%  {row['kernel'][:64]:64s} {provenance}")


if __name__ == "__main__":
    main()
