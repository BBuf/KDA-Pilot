"""solutions.jsonl ledger helpers (search-DAG of candidates with evidence pointers)."""

from __future__ import annotations

import json
import subprocess
import time
from pathlib import Path

KERNEL_DIR = Path(__file__).resolve().parents[1]
SOLUTIONS_JSONL = KERNEL_DIR / "solutions.jsonl"


def git_head() -> str:
    try:
        return subprocess.run(
            ["git", "rev-parse", "HEAD"], cwd=KERNEL_DIR,
            capture_output=True, text=True, check=True,
        ).stdout.strip()
    except Exception:  # noqa: BLE001 - lineage best-effort outside a checkout
        return "unknown"


def append_solution(
    candidate_id: str,
    *,
    parent: str | None,
    status: str,  # e.g. proposed | correct | benchmarked | kept | rejected | fallback
    summary: str,
    evidence: str = "",
    sources: list[str] | None = None,
    extra: dict | None = None,
) -> dict:
    entry = {
        "ts": time.strftime("%Y-%m-%dT%H:%M:%S%z"),
        "candidate_id": candidate_id,
        "parent": parent,
        "status": status,
        "summary": summary,
        "evidence": evidence,
        "sources": sources or [],
        "commit": git_head(),
    }
    if extra:
        entry.update(extra)
    with open(SOLUTIONS_JSONL, "a") as fh:
        fh.write(json.dumps(entry, ensure_ascii=False) + "\n")
    return entry
