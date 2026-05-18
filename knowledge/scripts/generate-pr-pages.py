#!/usr/bin/env python3
from __future__ import annotations

import argparse
from pathlib import Path

import yaml

from _knowledge_root import knowledge_root


def list_value(values) -> str:
    if not values:
        return "[]"
    return "[" + ", ".join(str(v) for v in values) + "]"


def render_pr(repo_id: str, entry: dict) -> str:
    number = entry.get("pr", entry.get("number"))
    repo = entry.get("repo") or entry.get("repo_full_name")
    if not repo:
        repo_map = {
            "cutlass": "NVIDIA/cutlass",
            "sglang": "sgl-project/sglang",
            "vllm": "vllm-project/vllm",
            "flashinfer": "flashinfer-ai/flashinfer",
            "pytorch": "pytorch/pytorch",
            "deepgemm": "deepseek-ai/DeepGEMM",
        }
        repo = repo_map.get(repo_id, repo_id)
    changed_paths = entry.get("changed_paths")
    if changed_paths is None:
        changed_paths = entry.get("files_changed") or []
    page_id = f"pr-{repo_id}-{number}"
    paths = changed_paths
    frontmatter = {
        "id": page_id,
        "repo": repo,
        "pr": number,
        "title": entry.get("title", f"PR-{number}"),
        "author": entry.get("author", "unknown"),
        "date": entry.get("date", "unknown"),
        "url": entry.get("url", f"https://github.com/{repo}/pull/{number}"),
        "source_category": "upstream-code",
        "architectures": entry.get("architectures") or ["sm100"],
        "tags": entry.get("tags") or [],
        "techniques": entry.get("techniques") or [],
        "hardware_features": entry.get("hardware_features") or [],
        "kernel_types": entry.get("kernel_types") or [],
        "languages": entry.get("languages") or [],
        "captured_at": entry.get("captured_at", "2026-05-16"),
        "status": entry.get("status", "merged"),
        "merge_sha": entry.get("merge_sha", "unknown"),
        "inclusion_reason": entry.get("inclusion_reason", entry.get("decision", "include")),
        "changed_paths": paths,
        "artifact_dir": entry.get("artifact_dir"),
    }
    body = [
        f"# {frontmatter['title']}",
        "",
        f"- Repository: `{repo}`",
        f"- PR: [{number}]({frontmatter['url']})",
        f"- Decision: `{entry.get('decision', 'include')}`",
        f"- Reason: {frontmatter['inclusion_reason']}",
        "",
        "## Changed Paths",
        "",
    ]
    body.extend(f"- `{path}`" for path in paths[:40])
    if entry.get("artifact_dir"):
        body.extend(["", "## Artifact Bundle", "", f"`{entry['artifact_dir']}`"])
    return "---\n" + yaml.safe_dump(frontmatter, sort_keys=False, allow_unicode=True) + "---\n" + "\n".join(body) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo", default=None, help="candidate repo id")
    parser.add_argument("--overwrite", action="store_true", help="rewrite existing PR source pages")
    args = parser.parse_args()
    root = knowledge_root()
    count = 0
    skipped = 0
    for ledger in sorted((root / "candidates").glob("*.yaml")):
        repo_id = ledger.stem
        if args.repo and repo_id != args.repo:
            continue
        data = yaml.safe_load(ledger.read_text(encoding="utf-8")) or {}
        out_dir = root / "sources/prs" / repo_id
        out_dir.mkdir(parents=True, exist_ok=True)
        entries = data.get("candidates")
        if entries is None:
            entries = data.get("prs", [])
        for entry in entries:
            if entry.get("decision") == "exclude":
                continue
            number = entry.get("pr", entry.get("number"))
            path = out_dir / f"PR-{number}.md"
            if path.exists() and not args.overwrite:
                skipped += 1
                continue
            path.write_text(render_pr(repo_id, entry), encoding="utf-8")
            count += 1
    print(f"generated {count} PR source pages; skipped {skipped} existing pages")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
