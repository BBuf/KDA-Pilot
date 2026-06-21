#!/usr/bin/env python3
"""Build resume records for B200 cookbook targets that did not finish.

The completed task index only covers models with all six shape JSON files.
This companion index keeps blocked, failed, gated, profiler-unavailable, and
deferred modality-specific targets visible so a later run can resume from the
right failure mode instead of rediscovering it from chat logs.
"""

from __future__ import annotations

import argparse
import json
import re
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


def slugify(value: str, max_len: int = 64) -> str:
    out = re.sub(r"[^a-zA-Z0-9]+", "_", value.lower()).strip("_")
    out = re.sub(r"_+", "_", out)
    return (out[:max_len].strip("_") or "target")


def md_cell(value: Any, limit: int | None = None) -> str:
    text = str(value)
    text = text.replace("\n", " ").replace("|", "\\|")
    if limit is not None and len(text) > limit:
        text = text[: limit - 3] + "..."
    return text


def split_md_row(line: str) -> list[str]:
    return [part.strip() for part in line.strip().strip("|").split("|")]


def classify_status(status: str) -> str:
    lower = status.lower()
    if "gated" in lower or "401" in lower:
        return "access_gated"
    if "topology" in lower or "nnodes 2" in lower:
        return "topology_blocked"
    if "profiler-unavailable" in lower or "no gpu `kernel` events" in lower:
        return "profiler_unavailable"
    if (
        "during hf download" in lower
        or "hf download failed" in lower
        or "remoteprotocolerror" in lower
        or "failed at" in lower and "download of" in lower
    ):
        return "download_failed"
    if (
        "reached server_ready" in lower
        or "watchdog killed" in lower
        or "cuda graph" in lower
        or "assertionerror" in lower
        or "mismatch in expected n" in lower
        or "cutlass_moe" in lower
    ):
        return "runtime_blocked"
    if "failed" in lower:
        return "launch_failed"
    if "blocked" in lower:
        return "runtime_blocked"
    return "incomplete"


def is_progress_row(parts: list[str]) -> bool:
    if len(parts) != 6:
        return False
    first = parts[0]
    if first in {"Prio", "---:"}:
        return False
    return bool(re.match(r"^(?:S?\d+)$", first))


def parse_progress(progress_md: Path) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    attempted: list[dict[str, Any]] = []
    deferred: list[dict[str, Any]] = []
    section = ""
    lines = progress_md.read_text().splitlines()
    for idx, line in enumerate(lines, start=1):
        if line.startswith("## "):
            section = line[3:].strip()
            continue
        if not line.startswith("|"):
            continue
        parts = split_md_row(line)
        if section in {"Primary Queue", "Secondary B200 Text LLM Queue"} and is_progress_row(parts):
            _, folder, series, page, model, status = parts
            if status.lower().startswith("completed"):
                continue
            attempted.append(
                {
                    "folder": folder.strip("`"),
                    "series": series,
                    "target_cookbook_page": page.strip("`"),
                    "target_model": model.strip("`"),
                    "status_summary": status,
                    "completion_class": classify_status(status),
                    "source_progress_line": idx,
                    "source_progress_file": str(progress_md),
                    "resume_scope": "attempted_text_llm",
                }
            )
        elif section == "Special / Non-Standard Queue" and len(parts) == 4:
            folder, series, page, reason = parts
            if folder == "Folder" or folder.startswith("---"):
                continue
            deferred.append(
                {
                    "folder": folder.strip("`"),
                    "series": series,
                    "target_cookbook_page": page.strip("`"),
                    "target_model": "",
                    "status_summary": reason,
                    "completion_class": "deferred_modality_specific",
                    "source_progress_line": idx,
                    "source_progress_file": str(progress_md),
                    "resume_scope": "deferred_non_text_or_placeholder",
                }
            )

    deferred.extend(parse_additional_targets(lines, progress_md, deferred))
    return attempted, deferred


def parse_additional_targets(
    lines: list[str], progress_md: Path, existing_deferred: list[dict[str, Any]]
) -> list[dict[str, Any]]:
    marker = "Additional B200-marked pages that are not in this text-only queue yet:"
    start = None
    for i, line in enumerate(lines):
        if line.strip() == marker:
            start = i + 1
            break
    if start is None:
        return []

    chunks: list[str] = []
    for line in lines[start:]:
        if not line.strip():
            break
        chunks.append(line.strip())
    text = " ".join(chunks)
    text = text.split("These need", 1)[0].strip().rstrip(".")
    targets = [x.strip().strip(".") for x in text.split(",") if x.strip()]

    existing_text = "\n".join(
        f"{x.get('folder')} {x.get('target_cookbook_page')} {x.get('status_summary')}"
        for x in existing_deferred
    ).lower()
    out: list[dict[str, Any]] = []
    for target in targets:
        normalized = re.sub(r"[^a-z0-9]+", "", target.lower())
        if normalized and normalized in re.sub(r"[^a-z0-9]+", "", existing_text):
            continue
        folder = slugify(target)
        out.append(
            {
                "folder": folder,
                "series": "cookbook-extra",
                "target_cookbook_page": target,
                "target_model": "",
                "status_summary": "not attempted in the text-only random/ShareGPT sweep; needs modality-specific benchmark inputs",
                "completion_class": "deferred_modality_specific",
                "source_progress_line": start + 1,
                "source_progress_file": str(progress_md),
                "resume_scope": "deferred_additional_b200_marked_page",
            }
        )
    return out


def collect_artifacts(root: Path, folder: str) -> list[str]:
    run_dir = root / folder / "b200"
    if not run_dir.exists():
        return []
    files: list[str] = []
    for path in sorted(run_dir.rglob("*")):
        if not path.is_file():
            continue
        rel = path.relative_to(root.parent)
        rel_text = str(rel)
        if path.name.endswith(".pid"):
            continue
        if "/profile/" in rel_text:
            continue
        if path.name in {"incomplete_run.json", "incomplete_run.md"}:
            continue
        files.append(rel_text)
    return files


def load_status_json(root: Path, folder: str) -> dict[str, Any] | None:
    path = root / folder / "b200" / "status.json"
    if not path.exists():
        return None
    try:
        return json.loads(path.read_text())
    except json.JSONDecodeError:
        return {"parse_error": f"failed to parse {path}"}


def enrich_attempted(root: Path, attempted: list[dict[str, Any]]) -> list[dict[str, Any]]:
    enriched = []
    for entry in attempted:
        folder = entry["folder"]
        local_run_dir = root / folder / "b200"
        artifacts = collect_artifacts(root, folder)
        shape_files = sorted((local_run_dir / "docs").glob("kernel_shapes_*.json")) if local_run_dir.exists() else []
        status_json = load_status_json(root, folder)
        item = {
            **entry,
            "local_run_dir": f"llm/{folder}/b200" if local_run_dir.exists() else "",
            "local_artifact_files": artifacts,
            "local_artifact_count": len(artifacts),
            "shape_json_count": len(shape_files),
            "status_json": status_json,
            "weights_cleanup_observed": "cleaned" in entry["status_summary"].lower()
            or bool(status_json and status_json.get("stage") == "weights_cleanup"),
            "resume_hint": resume_hint(entry),
        }
        enriched.append(item)
    return enriched


def resume_hint(entry: dict[str, Any]) -> str:
    cls = entry["completion_class"]
    if cls == "access_gated":
        return "Need HF access token/approval before rerunning; no useful shape artifacts are expected until config probe succeeds."
    if cls == "topology_blocked":
        return "Needs a multi-node topology matching the cookbook command before profiler collection can start."
    if cls == "profiler_unavailable":
        return "Needs a container or torch/profiler path that emits Chrome trace GPU kernel events with names."
    if cls == "download_failed":
        return "Resume from a clean HF cache or retry download; previous partial cache was cleaned."
    if cls == "launch_failed":
        return "Fix launch/import/quantization failure first, then run the six-workload profiler matrix."
    if cls == "runtime_blocked":
        return "Fix runtime kernel/server failure first; no promoted shape rows were captured."
    return "Rerun the six-workload profiler matrix after resolving the recorded status."


def write_local_attempt_docs(root: Path, entries: list[dict[str, Any]]) -> None:
    for entry in entries:
        if not entry["local_run_dir"]:
            continue
        docs_dir = root / entry["folder"] / "b200" / "docs"
        docs_dir.mkdir(parents=True, exist_ok=True)
        (docs_dir / "incomplete_run.json").write_text(
            json.dumps(entry, indent=2, ensure_ascii=False, sort_keys=True) + "\n"
        )
        artifact_lines = [
            f"- `{path}`" for path in entry["local_artifact_files"][:80]
        ] or ["- none"]
        if len(entry["local_artifact_files"]) > 80:
            artifact_lines.append(f"- ... {len(entry['local_artifact_files']) - 80} more")

        md = [
            f"# Incomplete B200 Run: {entry['folder']}",
            "",
            f"- Target model: `{entry['target_model']}`",
            f"- Cookbook page: `{entry['target_cookbook_page']}`",
            f"- Completion class: `{entry['completion_class']}`",
            f"- Shape JSON files captured: `{entry['shape_json_count']}`",
            f"- Weights cleanup observed: `{entry['weights_cleanup_observed']}`",
            f"- Resume hint: {entry['resume_hint']}",
            "",
            "## Status Summary",
            "",
            entry["status_summary"],
            "",
            "## Local Artifacts",
            "",
            *artifact_lines,
            "",
        ]
        (docs_dir / "incomplete_run.md").write_text("\n".join(md))


def write_global_docs(
    docs_dir: Path, generated_at: str, attempted: list[dict[str, Any]], deferred: list[dict[str, Any]]
) -> None:
    class_counts = Counter(x["completion_class"] for x in attempted)
    deferred_counts = Counter(x["completion_class"] for x in deferred)
    payload = {
        "generated_at": generated_at,
        "source": "llm/docs/cookbook_intro_remaining.md",
        "attempted_incomplete_count": len(attempted),
        "deferred_target_count": len(deferred),
        "attempted_by_completion_class": dict(sorted(class_counts.items())),
        "deferred_by_completion_class": dict(sorted(deferred_counts.items())),
        "attempted_incomplete": attempted,
        "deferred_targets": deferred,
    }
    (docs_dir / "incomplete_model_resume.json").write_text(
        json.dumps(payload, indent=2, ensure_ascii=False, sort_keys=True) + "\n"
    )

    md = [
        "# Incomplete Model Resume Index",
        "",
        f"- Generated at: `{generated_at}`",
        f"- Attempted text LLM targets without completed shape collection: `{len(attempted)}`",
        f"- Deferred cookbook targets outside the text-only matrix: `{len(deferred)}`",
        "- Completed models with promoted shape task cards live in `completed_model_task_index.md`.",
        "",
        "## Attempted But Not Completed",
        "",
        "| Folder | Class | Target model | Shape JSONs | Cleaned | Resume artifact | Status summary |",
        "|---|---|---|---:|---|---|---|",
    ]
    for entry in attempted:
        artifact = (
            f"`{entry['local_run_dir']}/docs/incomplete_run.md`" if entry["local_run_dir"] else "none"
        )
        md.append(
            f"| `{md_cell(entry['folder'])}` | `{md_cell(entry['completion_class'])}` | "
            f"`{md_cell(entry['target_model'], 80)}` | {entry['shape_json_count']} | "
            f"`{entry['weights_cleanup_observed']}` | {artifact} | "
            f"{md_cell(entry['status_summary'], 260)} |"
        )

    md.extend(
        [
            "",
            "## Deferred Targets",
            "",
            "| Folder / target | Scope | Page | Reason |",
            "|---|---|---|---|",
        ]
    )
    for entry in deferred:
        md.append(
            f"| `{md_cell(entry['folder'])}` | `{md_cell(entry['resume_scope'])}` | "
            f"`{md_cell(entry['target_cookbook_page'], 80)}` | "
            f"{md_cell(entry['status_summary'], 220)} |"
        )
    md.append("")
    (docs_dir / "incomplete_model_resume.md").write_text("\n".join(md))


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default="llm", help="Path to KDA-Pilot llm directory")
    args = ap.parse_args()

    root = Path(args.root)
    progress_md = root / "docs" / "cookbook_intro_remaining.md"
    docs_dir = root / "docs"
    generated_at = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

    attempted, deferred = parse_progress(progress_md)
    attempted = enrich_attempted(root, attempted)
    write_local_attempt_docs(root, attempted)
    write_global_docs(docs_dir, generated_at, attempted, deferred)

    print(
        f"attempted_incomplete={len(attempted)} "
        f"deferred_targets={len(deferred)} "
        f"with_local_dirs={sum(1 for x in attempted if x['local_run_dir'])}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
