#!/usr/bin/env python3
"""Extract >threshold GPU-kernel shape/meta rows from torch profiler traces.

The output is intentionally conservative: every retained row is backed by a GPU
kernel event whose cumulative name-level GPU time exceeds the threshold. Shape
provenance is recorded per sample from Kineto CPU op metadata when available.
"""

import argparse
import bisect
import csv
import glob
import gzip
import json
import os
from collections import Counter, defaultdict


SHAPE_KEYS = (
    "Input Dims",
    "Input dims",
    "Input Shapes",
    "Input shapes",
    "input_shapes",
    "Input type",
    "Input Types",
    "Input Strides",
    "Concrete Inputs",
)

EXTERNAL_ID_KEYS = (
    "External id",
    "external id",
    "External ID",
    "external_id",
    "correlation",
    "Correlation ID",
    "correlation_id",
)

TIMESTAMP_LOOKBACK_RECORDS = int(os.environ.get("KERNEL_SHAPE_LOOKBACK_RECORDS", "8192"))


def open_json(path):
    opener = gzip.open if path.endswith(".gz") else open
    with opener(path, "rb") as f:
        return json.loads(f.read().decode("utf-8", "replace"))


def find_traces(path):
    if os.path.isfile(path):
        return [path]
    patterns = (
        "*.pt.trace.json.gz",
        "*.trace.json.gz",
        "*.pt.trace.json",
        "*.trace.json",
        "*.json.gz",
        "*.json",
    )
    out = []
    for pat in patterns:
        out.extend(glob.glob(os.path.join(path, "**", pat), recursive=True))
    return sorted(set(out), key=os.path.getmtime)


def events_from_trace(path):
    obj = open_json(path)
    events = obj.get("traceEvents", obj) if isinstance(obj, dict) else obj
    return events if isinstance(events, list) else []


def get_external_id(event):
    args = event.get("args") or {}
    for key in EXTERNAL_ID_KEYS:
        value = args.get(key)
        if value is not None:
            return str(value)
    return None


def has_shape(args):
    return any(k in args for k in SHAPE_KEYS)


def compact_shape_args(args):
    out = {}
    for key in SHAPE_KEYS:
        if key in args:
            out[key] = args[key]
    return out


def classify_kernel(name):
    low = name.lower()
    if any(x in low for x in ("deep_ep", "deepep")):
        return "moe_comm"
    if any(x in low for x in ("nccl", "allreduce", "all_reduce", "allgather", "all_gather", "reducescatter", "reduce_scatter", "alltoall", "all_to_all")):
        return "comm"
    if any(x in low for x in ("moe", "expert", "grouped_gemm", "group_gemm", "fused_moe", "topk", "cutlass_grouped")):
        return "moe"
    if any(x in low for x in ("mxfp4", "nvfp4", "mxfp8", "fp4", "fp8", "int8", "scaled_mm", "w8a8", "w4a", "marlin", "machete", "quant", "deep_gemm", "nvjet", "e2m1", "mxint4")):
        return "quant_gemm"
    if any(x in low for x in ("gemm", "cublas", "cutlass", "matmul", "sgemm", "hgemm", "tensorop")):
        return "gemm"
    if any(x in low for x in ("rmsnorm", "rms_norm", "layernorm", "layer_norm", "norm")):
        return "norm"
    if any(x in low for x in ("rope", "rotary")):
        return "rope"
    if any(x in low for x in ("flash", "fmha", "mha", "mla", "attn", "attention", "paged", "gqa", "sparse_decode")):
        return "attention"
    if "cudnn" in low:
        return "cudnn"
    if any(x in low for x in ("silu", "gelu", "elementwise", "copy", "cast", "reduce", "scatter", "gather", "softmax", "sampling")):
        return "memory_bound"
    return "other"


def is_sglang_relevant(name, cpu_names):
    low = name.lower()
    joined = " ".join(cpu_names).lower()

    # Keep framework/backend kernels that are actionable for SGLang kernel work.
    # Drop generic PyTorch native memory movement even if it crosses the 2% line.
    generic_torch_native = (
        "at::native::elementwise_kernel",
        "direct_copy_kernel_cuda",
        "catarraybatchedcopy",
    )
    if any(x in low for x in generic_torch_native) and not any(
        x in joined for x in ("sglang", "srt")
    ):
        return False

    relevant_kernel_markers = (
        "sgl",
        "triton",
        "flashinfer",
        "cutlass",
        "cute",
        "deep_ep",
        "deepep",
        "moe",
        "expert",
        "mxfp4",
        "nvfp4",
        "fp8",
        "e2m1",
        "mxint4",
        "per_token_quant",
        "scaled_mm",
        "nvjet",
        "bmm_",
        "fused_a_gemm_kernel",
        "grouped_gemm",
        "fast_hadamard",
        "all_reduce_one_shot",
        "all_reduce_two_shot",
        "gqa_share_sparse_decode",
        "sparse_decode",
        "fmha",
        "flash",
        "rms",
        "rotary",
        "rope",
        "paged",
        "attention",
    )
    if any(x in low for x in relevant_kernel_markers):
        return True

    relevant_cpu_markers = (
        "sglang",
        "srt",
        "moe",
        "attention",
        "rms",
        "rotary",
        "triton",
        "flashinfer",
        "deepep",
        "deep_ep",
    )
    return any(x in joined for x in relevant_cpu_markers)


def load_index(trace_paths):
    kernels = []
    cpu_by_ext = {}
    cpu_shape_events = []
    for trace_path in trace_paths:
        for event in events_from_trace(trace_path):
            if not isinstance(event, dict):
                continue
            cat = str(event.get("cat", "")).lower()
            name = str(event.get("name", ""))
            args = event.get("args") or {}
            if cat == "kernel":
                kernels.append(
                    {
                        "trace": trace_path,
                        "name": name,
                        "dur": float(event.get("dur") or 0),
                        "ts": float(event.get("ts") or 0),
                        "pid": event.get("pid"),
                        "tid": event.get("tid"),
                        "external_id": get_external_id(event),
                        "args": args,
                    }
                )
                continue
            if cat in ("cpu_op", "user_annotation", "python_function", "operator", ""):
                ext = get_external_id(event)
                record = {
                    "trace": trace_path,
                    "name": name,
                    "ts": float(event.get("ts") or 0),
                    "dur": float(event.get("dur") or 0),
                    "pid": event.get("pid"),
                    "tid": event.get("tid"),
                    "external_id": ext,
                    "shape_args": compact_shape_args(args),
                    "args": args,
                }
                if ext is not None:
                    cpu_by_ext.setdefault(ext, record)
                if has_shape(args):
                    cpu_shape_events.append(record)
    cpu_shape_events.sort(key=lambda x: (x["trace"], x["ts"], x["dur"]))
    return kernels, cpu_by_ext, cpu_shape_events


def build_cpu_shape_index(cpu_shape_events):
    by_trace = defaultdict(list)
    for rec in cpu_shape_events:
        by_trace[rec["trace"]].append(rec)

    starts_by_trace = {}
    max_dur_by_trace = {}
    for trace, records in by_trace.items():
        starts_by_trace[trace] = [rec["ts"] for rec in records]
        max_dur_by_trace[trace] = max((max(rec["dur"], 0) for rec in records), default=0)
    return by_trace, starts_by_trace, max_dur_by_trace


def find_cpu_match(
    kernel,
    cpu_by_ext,
    cpu_shape_by_trace,
    cpu_shape_starts_by_trace,
    max_shape_dur_by_trace,
):
    ext = kernel.get("external_id")
    ext_rec = None
    if ext is not None and ext in cpu_by_ext:
        ext_rec = cpu_by_ext[ext]
        if ext_rec.get("shape_args"):
            return ext_rec, f"external_id={ext}"

    ts = kernel["ts"]
    trace = kernel["trace"]
    records = cpu_shape_by_trace.get(trace, [])
    starts = cpu_shape_starts_by_trace.get(trace, [])
    idx = bisect.bisect_right(starts, ts)

    # Timestamp matching is a fallback for traces where Kineto did not preserve
    # a direct kernel-to-CPU external id. Bound the backward scan with the
    # maximum shape-bearing CPU op duration for this trace instead of scanning
    # every shape record in every trace for each kernel sample.
    max_shape_dur = max_shape_dur_by_trace.get(trace, 0)
    candidates = []
    checked = 0
    for i in range(idx - 1, -1, -1):
        if checked >= TIMESTAMP_LOOKBACK_RECORDS:
            break
        rec = records[i]
        checked += 1
        if max_shape_dur and ts - rec["ts"] > max_shape_dur:
            break
        if rec["ts"] <= ts <= rec["ts"] + max(rec["dur"], 0):
            candidates.append(rec)
    if candidates:
        candidates.sort(key=lambda r: (r["dur"], -r["ts"]))
        return candidates[0], "timestamp_enclosure"

    if idx:
        return records[idx - 1], "nearest_preceding_shape_cpu_op"
    if ext_rec is not None:
        return ext_rec, f"external_id={ext}"
    return None, "missing"


def json_dumps(value):
    return json.dumps(value, ensure_ascii=False, sort_keys=True)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("trace", help="trace file or profile directory")
    ap.add_argument("--threshold", type=float, default=2.0)
    ap.add_argument("--model", required=True)
    ap.add_argument("--dataset", required=True)
    ap.add_argument("--concurrency", required=True)
    ap.add_argument("--label", required=True)
    ap.add_argument("--out-json", required=True)
    ap.add_argument("--out-csv", required=True)
    ap.add_argument("--out-md", required=True)
    args = ap.parse_args()

    trace_paths = find_traces(args.trace)
    if not trace_paths:
        raise SystemExit(f"no trace files found under {args.trace}")

    kernels, cpu_by_ext, cpu_shape_events = load_index(trace_paths)
    (
        cpu_shape_by_trace,
        cpu_shape_starts_by_trace,
        max_shape_dur_by_trace,
    ) = build_cpu_shape_index(cpu_shape_events)
    if not kernels:
        raise SystemExit(f"no GPU kernel events found under {args.trace}")

    total_gpu_us = sum(k["dur"] for k in kernels)
    by_name = defaultdict(list)
    for k in kernels:
        by_name[k["name"]].append(k)

    rows = []
    for name, evs in by_name.items():
        total_us = sum(e["dur"] for e in evs)
        pct = 100.0 * total_us / total_gpu_us if total_gpu_us else 0.0
        if pct <= args.threshold:
            continue
        samples = []
        cpu_counter = Counter()
        shape_status = "missing"
        for ev in sorted(evs, key=lambda x: x["dur"], reverse=True)[:8]:
            rec, method = find_cpu_match(
                ev,
                cpu_by_ext,
                cpu_shape_by_trace,
                cpu_shape_starts_by_trace,
                max_shape_dur_by_trace,
            )
            if rec:
                cpu_counter[rec["name"]] += 1
                if rec.get("shape_args"):
                    shape_status = "ok"
                samples.append(
                    {
                        "kernel_dur_us": ev["dur"],
                        "kernel_external_id": ev.get("external_id"),
                        "cpu_op": rec["name"],
                        "shape_args": rec.get("shape_args") or {},
                        "provenance": method,
                    }
                )
            else:
                samples.append(
                    {
                        "kernel_dur_us": ev["dur"],
                        "kernel_external_id": ev.get("external_id"),
                        "cpu_op": None,
                        "shape_args": {},
                        "provenance": method,
                    }
                )
        cpu_names = [x for x, _ in cpu_counter.most_common(5)]
        sglang_relevant = is_sglang_relevant(name, cpu_names)
        if not sglang_relevant:
            continue
        rows.append(
            {
                "model": args.model,
                "dataset": args.dataset,
                "concurrency": args.concurrency,
                "label": args.label,
                "kernel": name,
                "category": classify_kernel(name),
                "calls": len(evs),
                "total_us": total_us,
                "pct_of_gpu": pct,
                "mean_us": total_us / max(len(evs), 1),
                "shape_status": shape_status,
                "top_cpu_ops": cpu_names,
                "samples": samples,
                "sglang_relevant": sglang_relevant,
                "trace_files": trace_paths,
            }
        )
    rows.sort(key=lambda r: r["total_us"], reverse=True)

    os.makedirs(os.path.dirname(os.path.abspath(args.out_json)) or ".", exist_ok=True)
    payload = {
        "model": args.model,
        "dataset": args.dataset,
        "concurrency": args.concurrency,
        "label": args.label,
        "threshold_strictly_greater_than_pct": args.threshold,
        "total_gpu_us": total_gpu_us,
        "trace_files": trace_paths,
        "rows": rows,
    }
    with open(args.out_json, "w") as f:
        json.dump(payload, f, indent=2, ensure_ascii=False, sort_keys=True)
        f.write("\n")

    with open(args.out_csv, "w", newline="") as f:
        w = csv.writer(f, delimiter="\t")
        w.writerow(
            [
                "model",
                "label",
                "dataset",
                "concurrency",
                "pct_of_gpu",
                "calls",
                "mean_us",
                "category",
                "shape_status",
                "sglang_relevant",
                "kernel",
                "top_cpu_ops",
                "sample_shape_provenance",
                "sample_shapes_json",
            ]
        )
        for r in rows:
            sample = r["samples"][0] if r["samples"] else {}
            w.writerow(
                [
                    r["model"],
                    r["label"],
                    r["dataset"],
                    r["concurrency"],
                    f"{r['pct_of_gpu']:.4f}",
                    r["calls"],
                    f"{r['mean_us']:.2f}",
                    r["category"],
                    r["shape_status"],
                    r["sglang_relevant"],
                    r["kernel"],
                    " | ".join(r["top_cpu_ops"]),
                    sample.get("provenance", ""),
                    json_dumps(sample.get("shape_args", {})),
                ]
            )

    lines = [
        f"# Kernel Shape Inventory — {args.label}",
        "",
        f"- Model: `{args.model}`",
        f"- Dataset: `{args.dataset}`",
        f"- Concurrency: `{args.concurrency}`",
        f"- Threshold: GPU kernel name share `> {args.threshold:.1f}%`",
        f"- Total GPU kernel time: `{total_gpu_us/1000:.1f} ms`",
        f"- Trace files: `{len(trace_paths)}`",
        "",
        "| % GPU | Calls | Category | Shape | SGLang relevant | Kernel | Shape provenance |",
        "|---:|---:|---|---|---|---|---|",
    ]
    for r in rows:
        sample = r["samples"][0] if r["samples"] else {}
        shape = sample.get("shape_args") or {}
        shape_text = json_dumps(shape)
        if len(shape_text) > 180:
            shape_text = shape_text[:177] + "..."
        provenance = sample.get("provenance", "missing")
        cpu = sample.get("cpu_op") or ""
        prov_text = f"{provenance}: `{cpu}` {shape_text}"
        lines.append(
            f"| {r['pct_of_gpu']:.2f} | {r['calls']} | {r['category']} | {r['shape_status']} | "
            f"{r['sglang_relevant']} | `{r['kernel']}` | {prov_text} |"
        )
    lines.append("")
    lines.append("The CSV/JSON siblings contain full sample metadata and trace paths.")
    with open(args.out_md, "w") as f:
        f.write("\n".join(lines) + "\n")

    print(f"trace_files={len(trace_paths)} total_gpu_ms={total_gpu_us/1000:.1f} rows={len(rows)}")
    print(f"shape_ok={sum(1 for r in rows if r['shape_status'] == 'ok')} shape_missing={sum(1 for r in rows if r['shape_status'] != 'ok')}")


if __name__ == "__main__":
    main()
