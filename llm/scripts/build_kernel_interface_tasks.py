#!/usr/bin/env python3
"""Build KDA task definitions from runtime SGLang kernel interface captures."""

from __future__ import annotations

import argparse
import json
import re
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


LABEL_ORDER = (
    "random_low",
    "random_mid",
    "random_high",
    "sharegpt_low",
    "sharegpt_mid",
    "sharegpt_high",
)

EXCLUDED_GENERIC_INTERFACES = {
    # Shared dispatcher for many concrete MultiPlatformOp subclasses. SGLang's
    # logger strips `self`, so this log entry cannot distinguish SiluAndMul,
    # RMSNorm, RoPE, TopK, etc. Keep concrete sgl_kernel/jit_kernel/backend
    # interfaces instead of creating one oversized wrapper task.
    "srt.layers.utils.multi_platform.MultiPlatformOp.forward",
}


def slugify(value: str, max_len: int = 160) -> str:
    value = re.sub(r"([A-Z]+)([A-Z][a-z])", r"\1_\2", value)
    value = re.sub(r"([a-z0-9])([A-Z])", r"\1_\2", value)
    out = re.sub(r"[^a-zA-Z0-9]+", "_", value.lower()).strip("_")
    out = re.sub(r"_+", "_", out)
    return (out[:max_len].strip("_") or "kernel")


def md_cell(value: Any, limit: int | None = None) -> str:
    text = str(value).replace("\n", " ").replace("|", "\\|")
    if limit is not None and len(text) > limit:
        text = text[: limit - 3] + "..."
    return text


def json_key(value: Any) -> str:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def category_for(function: str) -> str:
    lower = function.lower()
    if (
        "allreduce" in lower
        or "all_reduce" in lower
        or "allgather" in lower
        or "all_gather" in lower
        or "reduce_scatter" in lower
    ):
        return "comm"
    if "attention" in lower or "flash_attn" in lower or "mla" in lower or "prefill" in lower or "decode" in lower:
        return "attention"
    if "moe" in lower or "expert" in lower:
        return "moe"
    if "norm" in lower or "rms" in lower or "layernorm" in lower:
        return "norm"
    if "rope" in lower or "rotary" in lower:
        return "rope"
    if "topk" in lower or "sample" in lower or "logits" in lower:
        return "sampling"
    if "cache" in lower or "kv" in lower or "radix" in lower:
        return "cache"
    if "gemm" in lower or "scaled_mm" in lower or "bmm" in lower or "matmul" in lower:
        return "quant_gemm" if any(x in lower for x in ("fp8", "fp4", "int8", "quant", "mxfp")) else "gemm"
    if "quant" in lower or "fp8" in lower or "fp4" in lower or "int8" in lower:
        return "quantization"
    return "other"


def task_id_for(function: str) -> str:
    return slugify(function)


def should_keep_interface(function: str) -> bool:
    return function not in EXCLUDED_GENERIC_INTERFACES


def shape_brief(value: Any) -> list[str]:
    out: list[str] = []
    if isinstance(value, dict):
        if value.get("kind") == "tensor":
            parts = [
                f"shape={value.get('shape')}",
                f"dtype={value.get('dtype')}",
                f"device={value.get('device')}",
            ]
            if "is_contiguous" in value:
                parts.append(f"contiguous={value.get('is_contiguous')}")
            name = value.get("name")
            out.append(f"{name}: " + ", ".join(parts) if name else ", ".join(parts))
        if isinstance(value.get("tensors"), list):
            for tensor in value["tensors"]:
                out.extend(shape_brief(tensor))
        for key in ("items",):
            items = value.get(key)
            if isinstance(items, list):
                for item in items[:8]:
                    out.extend(shape_brief(item.get("value", item) if isinstance(item, dict) else item))
        return out
    if isinstance(value, list):
        for item in value[:8]:
            out.extend(shape_brief(item))
    return out


CALL_RE = re.compile(
    r"^\[(?P<ts>\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})\] SGLang Kernel API Call: (?P<function>.+)$"
)
STATUS_RE = re.compile(
    r"^- (?P<ts>\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) UTC: (?P<stage>[^ ]+) - (?P<detail>.*)$"
)
PID_RE = re.compile(r"kernel_api_(?P<pid>\d+)\.log$")


def parse_timestamp(value: str) -> datetime:
    return datetime.strptime(value, "%Y-%m-%d %H:%M:%S").replace(tzinfo=timezone.utc)


def load_label_intervals(status_md: Path) -> list[tuple[datetime, datetime | None, str]]:
    points: list[tuple[datetime, str]] = []
    if status_md.exists():
        for line in status_md.read_text(errors="ignore").splitlines():
            match = STATUS_RE.match(line)
            if not match:
                continue
            stage = match.group("stage")
            detail = match.group("detail")
            if stage != "capture_label":
                continue
            label = detail.strip()
            points.append((parse_timestamp(match.group("ts")), label))

    intervals: list[tuple[datetime, datetime | None, str]] = []
    for idx, (start, label) in enumerate(points):
        end = points[idx + 1][0] if idx + 1 < len(points) else None
        intervals.append((start, end, label))
    return intervals


def label_for(ts: datetime, intervals: list[tuple[datetime, datetime | None, str]]) -> str:
    for start, end, label in intervals:
        if ts >= start and (end is None or ts < end):
            return label
    return "unknown"


def parse_tensor_blocks(lines: list[str]) -> list[dict[str, Any]]:
    tensors = []
    current: dict[str, Any] | None = None
    current_name = ""
    for raw in lines:
        stripped = raw.strip()
        if "Tensor(" in stripped:
            if current is not None:
                tensors.append(current)
            prefix = stripped.split("Tensor(", 1)[0].strip()
            current_name = prefix.rstrip("=")
            current = {"kind": "tensor", "name": current_name}
            continue
        if current is None:
            continue
        if stripped == ")":
            tensors.append(current)
            current = None
            current_name = ""
            continue
        if stripped.startswith("shape="):
            shape_text = stripped.split("=", 1)[1]
            dims = []
            for item in shape_text.strip("()").split(","):
                item = item.strip()
                if not item:
                    continue
                try:
                    dims.append(int(item))
                except ValueError:
                    dims.append(item)
            current["shape"] = dims
        elif stripped.startswith("dtype="):
            current["dtype"] = stripped.split("=", 1)[1].replace("torch.", "")
        elif stripped.startswith("device="):
            current["device"] = stripped.split("=", 1)[1]
        elif stripped.startswith("requires_grad="):
            current["requires_grad"] = stripped.split("=", 1)[1] == "True"
        elif stripped.startswith("is_contiguous="):
            current["is_contiguous"] = stripped.split("=", 1)[1] == "True"
    if current is not None:
        tensors.append(current)
    return tensors


def parse_scalar_lines(lines: list[str]) -> list[str]:
    scalars = []
    for raw in lines:
        stripped = raw.strip()
        if not stripped or stripped in {
            "Positional input arguments:",
            "Keyword input arguments:",
            "Output:",
        }:
            continue
        if "Tensor(" in stripped or stripped in {")", "(", "[", "]", "{" , "}"}:
            continue
        if any(
            stripped.startswith(prefix)
            for prefix in ("shape=", "dtype=", "device=", "requires_grad=", "is_contiguous=")
        ):
            continue
        scalars.append(stripped)
    return scalars[:64]


def parse_api_log_block(
    *,
    capture_file: Path,
    function: str,
    pid: int | None,
    raw_lines: list[str],
    ts: datetime,
    label: str,
) -> dict[str, Any]:
    input_lines = []
    output_lines = []
    target = input_lines
    for line in raw_lines:
        if line.strip() == "Output:":
            target = output_lines
        target.append(line.rstrip())
    args = {
        "kind": "api_arguments",
        "raw": "\n".join(input_lines).strip(),
        "scalars": parse_scalar_lines(input_lines),
        "tensors": parse_tensor_blocks(input_lines),
    }
    result = {
        "kind": "api_result",
        "raw": "\n".join(output_lines).strip(),
        "scalars": parse_scalar_lines(output_lines),
        "tensors": parse_tensor_blocks(output_lines),
    }
    return {
        "args": [args],
        "call_count": 1,
        "capture_file": str(capture_file),
        "function": function,
        "kind": "sglang_kernel_api_log",
        "kwargs": {},
        "label": label,
        "pid": pid,
        "result": result,
        "stack": [],
        "timestamp": ts.isoformat(),
    }


def load_api_logs(capture_dir: Path, status_md: Path) -> list[dict[str, Any]]:
    intervals = load_label_intervals(status_md)
    records: list[dict[str, Any]] = []
    for path in sorted(capture_dir.glob("kernel_api_*.log")):
        pid_match = PID_RE.search(path.name)
        pid = int(pid_match.group("pid")) if pid_match else None
        current_function = None
        current_ts = None
        current_lines: list[str] = []

        def flush_current() -> None:
            if current_function is None or current_ts is None:
                return
            label = label_for(current_ts, intervals)
            if label not in LABEL_ORDER:
                return
            if not should_keep_interface(current_function):
                return
            records.append(
                parse_api_log_block(
                    capture_file=path,
                    function=current_function,
                    pid=pid,
                    raw_lines=current_lines,
                    ts=current_ts,
                    label=label,
                )
            )

        for line in path.read_text(errors="ignore").splitlines():
            match = CALL_RE.match(line)
            if match:
                flush_current()
                current_ts = parse_timestamp(match.group("ts"))
                current_function = match.group("function").strip()
                current_lines = []
            elif current_function is not None:
                if line.startswith("=" * 20):
                    continue
                current_lines.append(line)
        flush_current()
    return records


def load_capture_files(capture_dir: Path, status_md: Path | None = None) -> list[dict[str, Any]]:
    records: list[dict[str, Any]] = []
    for path in sorted(capture_dir.glob("kernel_interface_capture_pid*.json")):
        payload = json.loads(path.read_text())
        for record in payload.get("records", []):
            record["capture_file"] = str(path)
            if should_keep_interface(record.get("function", "")):
                records.append(record)
    if records:
        return records
    if status_md is None:
        status_md = capture_dir.parent / "status.md"
    return load_api_logs(capture_dir, status_md)


def aggregate(records: list[dict[str, Any]], model: str, model_slug: str) -> list[dict[str, Any]]:
    grouped: dict[str, dict[str, Any]] = {}
    seen_variants: dict[str, dict[str, dict[str, Any]]] = defaultdict(dict)
    for record in records:
        function = record["function"]
        task_id = task_id_for(function)
        task = grouped.setdefault(
            task_id,
            {
                "task_id": task_id,
                "category": category_for(function),
                "function": function,
                "hardware": "b200",
                "model": model,
                "model_slug": model_slug,
                "evidence_policy": "runtime capture at SGLang kernel Python interface; args/kwargs are direct call parameters, not profiler CPU-op context",
                "labels": [],
                "total_call_count": 0,
                "variants": [],
                "capture_files": set(),
            },
        )
        label = record.get("label") or "unknown"
        if label not in task["labels"]:
            task["labels"].append(label)
        task["total_call_count"] += int(record.get("call_count") or 0)
        task["capture_files"].add(record.get("capture_file"))
        variant = {
            "args": record.get("args") or [],
            "call_count": record.get("call_count") or 0,
            "exception": record.get("exception"),
            "kind": record.get("kind"),
            "kwargs": record.get("kwargs") or {},
            "label": label,
            "pid": record.get("pid"),
            "result": record.get("result"),
            "stack": record.get("stack") or [],
        }
        key = json_key({"args": variant["args"], "kwargs": variant["kwargs"], "label": label})
        existing_variant = seen_variants[task_id].get(key)
        if existing_variant is None:
            seen_variants[task_id][key] = variant
            task["variants"].append(variant)
        else:
            existing_variant["call_count"] += variant["call_count"]

    tasks = []
    for task in grouped.values():
        task["labels"].sort(key=lambda x: LABEL_ORDER.index(x) if x in LABEL_ORDER else 999)
        task["variant_count"] = len(task["variants"])
        task["capture_files"] = sorted(x for x in task["capture_files"] if x)
        task["shape_briefs"] = sorted(
            set(
                brief
                for variant in task["variants"]
                for brief in shape_brief(variant.get("args", [])) + shape_brief(variant.get("kwargs", {}))
            )
        )[:24]
        task["variants"].sort(
            key=lambda v: (
                LABEL_ORDER.index(v["label"]) if v.get("label") in LABEL_ORDER else 999,
                -int(v.get("call_count") or 0),
                json_key(v.get("args")),
            )
        )
        tasks.append(task)
    tasks.sort(key=lambda t: (-t["total_call_count"], t["category"], t["function"]))
    return tasks


def write_prompt(task_dir: Path, task: dict[str, Any]) -> None:
    task_dir.mkdir(parents=True, exist_ok=True)
    for sub in ("baseline", "solution", "bench", "docs", "profile", "ncu", "tests"):
        path = task_dir / sub
        path.mkdir(exist_ok=True)
        keep = path / ".gitkeep"
        if not keep.exists():
            keep.write_text("")
    (task_dir / "docs" / "evidence.json").write_text(
        json.dumps(task, indent=2, ensure_ascii=False, sort_keys=True) + "\n"
    )
    config = [
        "[task]",
        f"slug = {json.dumps(task['task_id'], ensure_ascii=False)}",
        'arch = "b200"',
        'target_gpu = "NVIDIA B200"',
        f"family = {json.dumps(task['category'], ensure_ascii=False)}",
        f"model = {json.dumps(task['model'], ensure_ascii=False)}",
        f"model_slug = {json.dumps(task['model_slug'], ensure_ascii=False)}",
        "entry_points = [",
        f"  {json.dumps(task['function'], ensure_ascii=False)},",
        "]",
        'evidence_json = "docs/evidence.json"',
        "",
        "[build]",
        'language = "python/cuda"',
        'baseline_entry_point = "baseline/<copied_sglang_interface>::baseline"',
        'candidate_entry_point = "solution/<candidate_interface>::candidate"',
        "",
        "[benchmark]",
        "warmup_runs = 10",
        "iterations = 200",
        "num_trials = 7",
        "use_isolated_runner = true",
        "required_matched_ratio = 1.0",
        "",
        "[source_capture]",
        'method = "SGLANG_KERNEL_API_LOGLEVEL=3"',
        'policy = "runtime SGLang kernel Python interface args/kwargs/result, not torch profiler CPU-op context"',
        f"total_call_count = {int(task['total_call_count'])}",
        f"variant_count = {int(task['variant_count'])}",
    ]
    (task_dir / "config.toml").write_text("\n".join(config) + "\n")

    executed_workload_lines = [f"- `{label}`" for label in LABEL_ORDER]
    observed_workload_lines = [f"- `{label}`" for label in task["labels"]] or ["- none"]
    missing_labels = [label for label in LABEL_ORDER if label not in set(task["labels"])]
    not_observed_workload_lines = [f"- `{label}`" for label in missing_labels] or ["- none"]
    shape_lines = [f"- `{md_cell(x, 180)}`" for x in task["shape_briefs"][:12]] or ["- none"]
    variant_lines = []
    for idx, variant in enumerate(task["variants"][:6], start=1):
        args_text = json.dumps(variant.get("args"), ensure_ascii=False, sort_keys=True)
        kwargs_text = json.dumps(variant.get("kwargs"), ensure_ascii=False, sort_keys=True)
        if len(args_text) > 900:
            args_text = args_text[:897] + "..."
        if len(kwargs_text) > 500:
            kwargs_text = kwargs_text[:497] + "..."
        variant_lines.append(
            f"{idx}. label=`{variant['label']}`, calls=`{variant['call_count']}`\n"
            f"   - args: `{args_text}`\n"
            f"   - kwargs: `{kwargs_text}`"
        )

    prompt = [
        f"# KDA Prompt: {task['task_id']}",
        "",
        "Target GPU: NVIDIA B200.",
        "",
        "Target SGLang kernel Python interface to copy as local baseline:",
        "",
        f"- `{task['function']}`",
        "",
        f"Goal: optimize or replace this interface for the {task['model']} serving shapes",
        "captured on B200. The shapes below come from runtime SGLang kernel API",
        "logging at the Python interface boundary; they are not torch profiler",
        "CPU-op context shapes.",
        "",
        "## Kernel Interface",
        "",
        f"- Model: `{task['model']}`",
        f"- Model folder: `llm/{task['model_slug']}/b200`",
        f"- Category: `{task['category']}`",
        f"- Python interface: `{task['function']}`",
        f"- Captured call count: `{task['total_call_count']}`",
        f"- Captured variants: `{task['variant_count']}`",
        "- Evidence policy: runtime interface capture of args/kwargs/result, not torch-profiler CPU-op shape context.",
        "",
        "## Executed Workload Matrix",
        "",
        "The capture run executed all workload labels below for this model.",
        "A specific interface may still be absent from a workload when the",
        "serving path does not call it for that dataset/concurrency level.",
        "",
        *executed_workload_lines,
        "",
        "## Observed Workloads For This Interface",
        "",
        *observed_workload_lines,
        "",
        "## Not Observed For This Interface",
        "",
        *not_observed_workload_lines,
        "",
        "## Shape Summary",
        "",
        *shape_lines,
        "",
        "## Captured Variants",
        "",
        *variant_lines,
        "",
        "Full structured args/kwargs/result records are in `docs/evidence.json`.",
        "",
        "## Required First Milestone",
        "",
        "1. Copy the upstream SGLang source files needed for this exact interface into `baseline/`.",
        "2. Record upstream URL, commit, and copied files in `docs/baseline_source.md`.",
        "3. Expose the copied baseline through a local low-overhead ABI.",
        "4. Expose the candidate through the exact same ABI in `solution/`.",
        "5. Build correctness tests for every retained captured variant or an explicitly justified representative subset.",
        "6. Benchmark baseline and candidate on an idle B200 with the same shapes, dtypes, devices, contiguity, and scalar parameters.",
        "- Unsupported shapes or parameter combinations must fall back to the recovered SGLang baseline.",
        "",
        "Do not import, patch, or monkey-patch a live SGLang server during correctness or benchmark runs.",
    ]
    (task_dir / "prompt.md").write_text("\n".join(prompt) + "\n")


def write_docs(run_dir: Path, tasks: list[dict[str, Any]], generated_at: str, source_dir: Path) -> None:
    docs_dir = run_dir / "docs"
    docs_dir.mkdir(parents=True, exist_ok=True)
    model_name = tasks[0]["model"] if tasks else "unknown"
    model_slug = tasks[0]["model_slug"] if tasks else run_dir.parent.name
    index_tasks = [
        {
            "task_id": task["task_id"],
            "category": task["category"],
            "function": task["function"],
            "total_call_count": task["total_call_count"],
            "variant_count": task["variant_count"],
            "labels": task["labels"],
            "shape_briefs": task["shape_briefs"],
            "evidence_json": f"../kernels/{task['task_id']}/docs/evidence.json",
        }
        for task in tasks
    ]
    index = {
        "generated_at": generated_at,
        "model": model_name,
        "model_slug": model_slug,
        "source_capture_dir": str(source_dir),
        "task_count": len(tasks),
        "tasks": index_tasks,
    }
    (docs_dir / "kernel_interface_task_index.json").write_text(
        json.dumps(index, indent=2, ensure_ascii=False, sort_keys=True) + "\n"
    )

    category_counts = Counter(task["category"] for task in tasks)
    md = [
        f"# {model_name} B200 Kernel Interface Task Index",
        "",
        f"- Generated at: `{generated_at}`",
        f"- Model slug: `{model_slug}`",
        f"- Source capture dir: `{source_dir}`",
        f"- Task count: `{len(tasks)}`",
        "- Evidence policy: runtime capture at SGLang kernel Python interfaces.",
        "",
        "## Category Counts",
        "",
        "| Category | Tasks |",
        "|---|---:|",
    ]
    for category, count in sorted(category_counts.items()):
        md.append(f"| `{category}` | {count} |")
    md.extend(
        [
            "",
            "## Tasks",
            "",
            "| Task id | Category | Interface | Calls | Variants | Workloads |",
            "|---|---|---|---:|---:|---|",
        ]
    )
    for task in tasks:
        labels = ", ".join(f"`{x}`" for x in task["labels"])
        md.append(
            f"| `{task['task_id']}` | `{task['category']}` | `{md_cell(task['function'], 90)}` | "
            f"{task['total_call_count']} | {task['variant_count']} | {labels} |"
        )
    md.append("")
    (docs_dir / "kernel_interface_task_index.md").write_text("\n".join(md))


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--capture-dir", required=True)
    ap.add_argument("--run-dir", required=True)
    ap.add_argument("--model", default="zai-org/GLM-5.2-FP8")
    ap.add_argument("--model-slug", default="glm_52")
    ap.add_argument("--write-task-cards", action="store_true")
    args = ap.parse_args()

    capture_dir = Path(args.capture_dir)
    run_dir = Path(args.run_dir)
    records = load_capture_files(capture_dir)
    tasks = aggregate(records, args.model, args.model_slug)
    generated_at = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    write_docs(run_dir, tasks, generated_at, capture_dir)
    if args.write_task_cards:
        kernels_dir = run_dir / "kernels"
        for task in tasks:
            write_prompt(kernels_dir / task["task_id"], task)
    print(
        f"records={len(records)} tasks={len(tasks)} "
        f"variants={sum(t['variant_count'] for t in tasks)} "
        f"calls={sum(t['total_call_count'] for t in tasks)}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
