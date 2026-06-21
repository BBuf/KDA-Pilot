#!/usr/bin/env python3
"""Build KDA task indexes from completed LLM shape inventories.

The source inventories are the per-workload `kernel_shapes_*.json` files
created from real SGLang serving profiler traces. This script is deliberately
conservative: only rows with an external-id-bound CPU op shape are promoted to
kernel task candidates. Timestamp-only fallbacks are kept in the audit report
but are not treated as reliable task definitions.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


LABELS = (
    "random_low",
    "random_mid",
    "random_high",
    "sharegpt_low",
    "sharegpt_mid",
    "sharegpt_high",
)


def json_dumps(value: Any) -> str:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def slugify(value: str, max_len: int = 48) -> str:
    out = re.sub(r"[^a-zA-Z0-9]+", "_", value.lower()).strip("_")
    out = re.sub(r"_+", "_", out)
    return (out[:max_len].strip("_") or "kernel")


def kernel_alias(kernel: str, category: str) -> str:
    text = kernel
    text = re.sub(r"<.*", "", text)
    text = text.replace("void ", "")
    text = text.split("(")[0]
    if "::" in text:
        text = text.split("::")[-1]
    text = text.rsplit(" ", 1)[-1]
    if not text or len(text) < 4:
        text = category
    return slugify(text)


def sample_has_shape(sample: dict[str, Any]) -> bool:
    return bool(sample.get("shape_args"))


def sample_has_external_shape(sample: dict[str, Any]) -> bool:
    provenance = str(sample.get("provenance") or "")
    return provenance.startswith("external_id=") and sample_has_shape(sample)


def compact_shape_sample(sample: dict[str, Any]) -> dict[str, Any]:
    shape = sample.get("shape_args") or {}
    return {
        "cpu_op": sample.get("cpu_op"),
        "provenance": sample.get("provenance"),
        "kernel_dur_us": sample.get("kernel_dur_us"),
        "shape_args": shape,
    }


def row_strength(row: dict[str, Any]) -> tuple[str, list[dict[str, Any]]]:
    samples = row.get("samples") or []
    strong = [compact_shape_sample(s) for s in samples if sample_has_external_shape(s)]
    if strong:
        return "strong_external_id_shape", strong
    weak = [compact_shape_sample(s) for s in samples if sample_has_shape(s)]
    if weak:
        return "weak_timestamp_shape", weak
    return "empty_shape", []


def load_workload(path: Path) -> dict[str, Any]:
    with path.open() as f:
        return json.load(f)


def task_id_for(row: dict[str, Any]) -> str:
    kernel = row["kernel"]
    category = row.get("category") or "other"
    digest = hashlib.sha1(kernel.encode("utf-8")).hexdigest()[:10]
    return f"{slugify(category, 24)}__{kernel_alias(kernel, str(category))}__{digest}"


def merge_sample(samples: list[dict[str, Any]], sample: dict[str, Any], limit: int = 12) -> None:
    key = json_dumps(
        {
            "cpu_op": sample.get("cpu_op"),
            "shape_args": sample.get("shape_args"),
        }
    )
    for existing in samples:
        existing_key = json_dumps(
            {
                "cpu_op": existing.get("cpu_op"),
                "shape_args": existing.get("shape_args"),
            }
        )
        if existing_key == key:
            return
    if len(samples) < limit:
        samples.append(sample)


def analyze_model(model_dir: Path) -> dict[str, Any]:
    docs = model_dir / "docs"
    workloads: dict[str, dict[str, Any]] = {}
    for label in LABELS:
        path = docs / f"kernel_shapes_{label}.json"
        if not path.exists():
            raise FileNotFoundError(path)
        payload = load_workload(path)
        workloads[label] = payload

    task_map: dict[str, dict[str, Any]] = {}
    skipped_rows: list[dict[str, Any]] = []
    workload_summary: dict[str, dict[str, Any]] = {}

    for label, payload in workloads.items():
        rows = payload.get("rows") or []
        summary = {
            "row_count": len(rows),
            "strong_rows": 0,
            "weak_rows": 0,
            "empty_shape_rows": 0,
            "total_gpu_us": payload.get("total_gpu_us"),
            "threshold_strictly_greater_than_pct": payload.get(
                "threshold_strictly_greater_than_pct"
            ),
            "dataset": payload.get("dataset"),
            "concurrency": payload.get("concurrency"),
        }
        for row in rows:
            strength, samples = row_strength(row)
            if strength == "strong_external_id_shape":
                summary["strong_rows"] += 1
                tid = task_id_for(row)
                task = task_map.setdefault(
                    tid,
                    {
                        "task_id": tid,
                        "kernel": row["kernel"],
                        "category": row.get("category") or "other",
                        "model": row.get("model") or payload.get("model"),
                        "model_slug": model_dir.parent.name,
                        "hardware": "b200",
                        "evidence_policy": "promoted only from external_id-bound torch-profiler shape samples",
                        "workloads": [],
                        "shape_samples": [],
                        "source_json": [],
                    },
                )
                task["workloads"].append(
                    {
                        "label": label,
                        "dataset": row.get("dataset"),
                        "concurrency": row.get("concurrency"),
                        "pct_of_gpu": row.get("pct_of_gpu"),
                        "calls": row.get("calls"),
                        "mean_us": row.get("mean_us"),
                        "total_us": row.get("total_us"),
                        "top_cpu_ops": row.get("top_cpu_ops") or [],
                    }
                )
                source = str((docs / f"kernel_shapes_{label}.json").relative_to(model_dir.parents[1]))
                if source not in task["source_json"]:
                    task["source_json"].append(source)
                for sample in samples:
                    merge_sample(task["shape_samples"], sample)
            else:
                if strength == "weak_timestamp_shape":
                    summary["weak_rows"] += 1
                else:
                    summary["empty_shape_rows"] += 1
                skipped_rows.append(
                    {
                        "label": label,
                        "category": row.get("category"),
                        "kernel": row.get("kernel"),
                        "pct_of_gpu": row.get("pct_of_gpu"),
                        "reason": strength,
                        "top_cpu_ops": row.get("top_cpu_ops") or [],
                    }
                )
        workload_summary[label] = summary

    tasks = sorted(
        task_map.values(),
        key=lambda t: (
            -max(w["pct_of_gpu"] or 0 for w in t["workloads"]),
            t["category"],
            t["task_id"],
        ),
    )
    for task in tasks:
        task["workload_count"] = len(task["workloads"])
        task["max_pct_of_gpu"] = max(w["pct_of_gpu"] or 0 for w in task["workloads"])
        task["total_calls"] = sum(w["calls"] or 0 for w in task["workloads"])
        task["labels"] = sorted({w["label"] for w in task["workloads"]}, key=LABELS.index)

    zero_row_labels = [label for label, s in workload_summary.items() if s["row_count"] == 0]
    weak_or_empty_only = [
        label
        for label, s in workload_summary.items()
        if s["row_count"] > 0 and s["strong_rows"] == 0
    ]

    return {
        "model_slug": model_dir.parent.name,
        "model": next(iter(workloads.values())).get("model"),
        "platform": "b200",
        "model_dir": str(model_dir),
        "workload_summary": workload_summary,
        "task_candidates": tasks,
        "skipped_rows": skipped_rows,
        "audit": {
            "zero_row_labels": zero_row_labels,
            "weak_or_empty_only_labels": weak_or_empty_only,
            "strong_task_count": len(tasks),
            "strong_row_count": sum(s["strong_rows"] for s in workload_summary.values()),
            "weak_row_count": sum(s["weak_rows"] for s in workload_summary.values()),
            "empty_shape_row_count": sum(s["empty_shape_rows"] for s in workload_summary.values()),
            "row_count": sum(s["row_count"] for s in workload_summary.values()),
        },
    }


def write_model_md(model: dict[str, Any], out: Path) -> None:
    lines = [
        f"# LLM Kernel Task Index: {model['model_slug']} / B200",
        "",
        f"- Model: `{model['model']}`",
        "- Evidence threshold: GPU kernel name share strictly `> 2%`.",
        "- Promotion rule: only rows with an external-id-bound non-empty torch-profiler shape are task candidates.",
        "- Weak timestamp/nearest-preceding fallback rows are retained in audit data but are not promoted.",
        "",
        "## Workload Coverage",
        "",
        "| Workload | Rows | Strong | Weak | Empty shape | Status |",
        "|---|---:|---:|---:|---:|---|",
    ]
    for label in LABELS:
        s = model["workload_summary"][label]
        if s["row_count"] == 0:
            status = "no >2% SGLang/actionable row"
        elif s["strong_rows"] == 0:
            status = "weak/empty only, do not promote"
        elif s["weak_rows"] or s["empty_shape_rows"]:
            status = "partial, promote strong rows only"
        else:
            status = "strong"
        lines.append(
            f"| `{label}` | {s['row_count']} | {s['strong_rows']} | {s['weak_rows']} | {s['empty_shape_rows']} | {status} |"
        )

    lines.extend(
        [
            "",
            "## Task Candidates",
            "",
            "| Task id | Category | Workloads | Max % GPU | Shape samples | Kernel |",
            "|---|---|---|---:|---:|---|",
        ]
    )
    for task in model["task_candidates"]:
        kernel = task["kernel"]
        if len(kernel) > 96:
            kernel = kernel[:93] + "..."
        labels = ", ".join(f"`{x}`" for x in task["labels"])
        lines.append(
            f"| `{task['task_id']}` | `{task['category']}` | {labels} | {task['max_pct_of_gpu']:.2f} | {len(task['shape_samples'])} | `{kernel}` |"
        )

    lines.extend(
        [
            "",
            "Full shape samples and skipped weak/empty rows are in `kernel_task_index.json`.",
        ]
    )
    out.write_text("\n".join(lines) + "\n")


def write_prompt(task_dir: Path, model: dict[str, Any], task: dict[str, Any]) -> None:
    task_dir.mkdir(parents=True, exist_ok=True)
    for sub in ("baseline", "solution", "bench", "docs", "profile", "ncu"):
        d = task_dir / sub
        d.mkdir(exist_ok=True)
        keep = d / ".gitkeep"
        if not keep.exists():
            keep.write_text("")

    evidence_path = task_dir / "docs" / "evidence.json"
    evidence_path.write_text(json.dumps(task, indent=2, ensure_ascii=False, sort_keys=True) + "\n")

    cfg = {
        "task_id": task["task_id"],
        "model_slug": model["model_slug"],
        "model": model["model"],
        "hardware": "b200",
        "category": task["category"],
        "evidence_json": "docs/evidence.json",
        "source_model_index": "../../docs/kernel_task_index.json",
    }
    config_lines = []
    for key, value in cfg.items():
        config_lines.append(f'{key} = {json.dumps(value, ensure_ascii=False)}')
    (task_dir / "config.toml").write_text("\n".join(config_lines) + "\n")

    shape_lines = []
    for idx, sample in enumerate(task["shape_samples"][:4], start=1):
        shape = json_dumps(sample.get("shape_args") or {})
        if len(shape) > 700:
            shape = shape[:697] + "..."
        shape_lines.append(
            f"{idx}. `{sample.get('cpu_op')}` via `{sample.get('provenance')}`: `{shape}`"
        )
    if not shape_lines:
        shape_lines = ["No promoted shape samples. This task should not have been generated."]

    workload_lines = []
    for w in sorted(task["workloads"], key=lambda x: LABELS.index(x["label"])):
        workload_lines.append(
            f"- `{w['label']}`: {w['pct_of_gpu']:.2f}% GPU, calls={w['calls']}, mean={w['mean_us']:.2f} us"
        )

    prompt = [
        f"# KDA Prompt: {task['task_id']}",
        "",
        "Develop an optimized SGLang kernel or wrapper path for the profiler-backed",
        f"`{task['category']}` opportunity below on NVIDIA B200. This task is",
        "seeded only from external-id-bound torch-profiler shape samples collected",
        "during real SGLang serving runs.",
        "",
        "## Evidence",
        "",
        f"- Model: `{model['model']}`",
        f"- Model folder: `llm/{model['model_slug']}/b200`",
        f"- Kernel category: `{task['category']}`",
        f"- Max observed GPU share: `{task['max_pct_of_gpu']:.2f}%`",
        f"- Kernel name: `{task['kernel']}`",
        "- Selection rule: kernel name share was strictly `> 2%` in at least one workload, and at least one retained sample has non-empty shape metadata bound by `external_id`.",
        "- Do not use weak timestamp-only fallback rows as correctness or benchmark shape authority.",
        "",
        "## Workload Appearances",
        "",
        *workload_lines,
        "",
        "## Promoted Shape Samples",
        "",
        *shape_lines,
        "",
        "The complete evidence bundle is in `docs/evidence.json`. Recover the current",
        "SGLang baseline before writing optimized code, then build a local correctness",
        "and benchmark harness under this task folder. Use the same ABI for baseline",
        "and candidate code, and keep raw measurements in `benchmark.csv` or `docs/`.",
        "",
        "## Completion Bar",
        "",
        "- Correctness passes for every promoted shape sample and relevant dtype/layout.",
        "- Benchmark compares candidate against the current SGLang baseline on an idle B200.",
        "- NCU or benchmark evidence explains the bottleneck and the final design.",
        "- Unsupported shapes must fall back to the recovered SGLang baseline.",
    ]
    (task_dir / "prompt.md").write_text("\n".join(prompt) + "\n")


def write_global_docs(models: list[dict[str, Any]], docs_dir: Path, generated_at: str) -> None:
    aggregate = {
        "generated_at": generated_at,
        "promotion_rule": "external_id-bound non-empty torch-profiler shape sample",
        "labels": LABELS,
        "model_count": len(models),
        "models": [
            {
                "model_slug": m["model_slug"],
                "model": m["model"],
                "audit": m["audit"],
                "task_count": len(m["task_candidates"]),
                "task_index": f"llm/{m['model_slug']}/b200/docs/kernel_task_index.json",
            }
            for m in models
        ],
    }
    (docs_dir / "completed_model_task_index.json").write_text(
        json.dumps(aggregate, indent=2, ensure_ascii=False, sort_keys=True) + "\n"
    )

    totals = Counter()
    category_counts = Counter()
    for m in models:
        totals["rows"] += m["audit"]["row_count"]
        totals["strong"] += m["audit"]["strong_row_count"]
        totals["weak"] += m["audit"]["weak_row_count"]
        totals["empty"] += m["audit"]["empty_shape_row_count"]
        totals["tasks"] += len(m["task_candidates"])
        for task in m["task_candidates"]:
            category_counts[task["category"]] += 1

    md = [
        "# Completed LLM Model Task Index",
        "",
        f"- Generated at: `{generated_at}`",
        f"- Completed model folders audited: `{len(models)}`",
        f"- Promoted task candidates: `{totals['tasks']}`",
        f"- Strong rows: `{totals['strong']}`",
        f"- Weak fallback rows not promoted: `{totals['weak']}`",
        f"- Empty-shape rows not promoted: `{totals['empty']}`",
        "",
        "## Category Counts",
        "",
        "| Category | Task candidates |",
        "|---|---:|",
    ]
    for cat, count in sorted(category_counts.items()):
        md.append(f"| `{cat}` | {count} |")
    md.extend(
        [
            "",
            "## Models",
            "",
            "| Model slug | Model | Tasks | Strong rows | Weak rows | Empty rows | Scene caveats |",
            "|---|---|---:|---:|---:|---:|---|",
        ]
    )
    for m in models:
        caveats = []
        if m["audit"]["zero_row_labels"]:
            caveats.append("zero rows: " + ", ".join(f"`{x}`" for x in m["audit"]["zero_row_labels"]))
        if m["audit"]["weak_or_empty_only_labels"]:
            caveats.append(
                "weak/empty only: "
                + ", ".join(f"`{x}`" for x in m["audit"]["weak_or_empty_only_labels"])
            )
        caveat_text = "; ".join(caveats) if caveats else "none"
        md.append(
            f"| `{m['model_slug']}` | `{m['model']}` | {len(m['task_candidates'])} | "
            f"{m['audit']['strong_row_count']} | {m['audit']['weak_row_count']} | "
            f"{m['audit']['empty_shape_row_count']} | {caveat_text} |"
        )
    md.append("")
    (docs_dir / "completed_model_task_index.md").write_text("\n".join(md))

    audit = {
        "generated_at": generated_at,
        "policy": {
            "strong_external_id_shape": "promoted",
            "weak_timestamp_shape": "not promoted; possible fallback mismatch",
            "empty_shape": "not promoted",
            "zero_rows": "no kernel passed the strict >2% SGLang/actionable filter",
        },
        "models": [
            {
                "model_slug": m["model_slug"],
                "model": m["model"],
                "workload_summary": m["workload_summary"],
                "audit": m["audit"],
                "skipped_rows": m["skipped_rows"],
            }
            for m in models
        ],
    }
    (docs_dir / "completed_shape_capture_audit.json").write_text(
        json.dumps(audit, indent=2, ensure_ascii=False, sort_keys=True) + "\n"
    )

    audit_md = [
        "# Completed Shape Capture Audit",
        "",
        "This audit checks for shape-capture illusions in the completed B200 LLM sweep.",
        "Only external-id-bound non-empty shape samples are considered strong enough",
        "to seed optimization task definitions.",
        "",
        "| Model slug | Problem scenes | Weak rows | Empty rows | Notes |",
        "|---|---|---:|---:|---|",
    ]
    for m in models:
        problems = []
        if m["audit"]["zero_row_labels"]:
            problems.extend(f"{x}: zero row" for x in m["audit"]["zero_row_labels"])
        if m["audit"]["weak_or_empty_only_labels"]:
            problems.extend(f"{x}: weak/empty only" for x in m["audit"]["weak_or_empty_only_labels"])
        if m["audit"]["empty_shape_row_count"]:
            note = "empty-shape rows excluded"
        elif m["audit"]["weak_row_count"]:
            note = "weak fallback rows excluded"
        else:
            note = "all retained rows have promoted shapes"
        audit_md.append(
            f"| `{m['model_slug']}` | {', '.join(problems) if problems else 'none'} | "
            f"{m['audit']['weak_row_count']} | {m['audit']['empty_shape_row_count']} | {note} |"
        )
    audit_md.append("")
    (docs_dir / "completed_shape_capture_audit.md").write_text("\n".join(audit_md))


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default="llm", help="Path to KDA-Pilot llm directory")
    ap.add_argument("--write-task-cards", action="store_true")
    args = ap.parse_args()

    root = Path(args.root)
    docs_dir = root / "docs"
    model_dirs = []
    for model_dir in sorted(root.glob("*/b200")):
        shape_files = list((model_dir / "docs").glob("kernel_shapes_*.json"))
        if len(shape_files) == len(LABELS):
            model_dirs.append(model_dir)

    models = [analyze_model(model_dir) for model_dir in model_dirs]
    generated_at = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

    for model in models:
        docs = root / model["model_slug"] / "b200" / "docs"
        docs.mkdir(parents=True, exist_ok=True)
        (docs / "kernel_task_index.json").write_text(
            json.dumps(model, indent=2, ensure_ascii=False, sort_keys=True) + "\n"
        )
        write_model_md(model, docs / "kernel_task_index.md")
        if args.write_task_cards:
            kernels_dir = root / model["model_slug"] / "b200" / "kernels"
            for task in model["task_candidates"]:
                write_prompt(kernels_dir / task["task_id"], model, task)

    write_global_docs(models, docs_dir, generated_at)
    print(
        f"audited_models={len(models)} "
        f"task_candidates={sum(len(m['task_candidates']) for m in models)} "
        f"strong_rows={sum(m['audit']['strong_row_count'] for m in models)} "
        f"weak_rows={sum(m['audit']['weak_row_count'] for m in models)} "
        f"empty_rows={sum(m['audit']['empty_shape_row_count'] for m in models)}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
