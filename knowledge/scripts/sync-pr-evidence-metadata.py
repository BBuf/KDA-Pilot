#!/usr/bin/env python3
"""Sync PR source-page metadata from materialized upstream.json bundles."""

from __future__ import annotations

import argparse
import json
import re
import shutil
from pathlib import Path
from typing import Any

import yaml

from _knowledge_root import knowledge_root


FRONTMATTER_RE = re.compile(r"\A---\s*\n(.*?)\n---\s*\n", re.S)
PULL_BUNDLE_ROOT = Path("evidence") / "pull-bundles"


def parse_page(path: Path) -> tuple[dict[str, Any], str]:
    text = path.read_text(encoding="utf-8")
    match = FRONTMATTER_RE.match(text)
    if not match:
        return {}, text
    meta = yaml.safe_load(match.group(1)) or {}
    return meta, text[match.end() :]


def bundle_path(root: Path, source: Path, meta: dict[str, Any]) -> Path:
    artifact_dir = meta.get("artifact_dir")
    if artifact_dir:
        return root / artifact_dir
    return root / PULL_BUNDLE_ROOT / source.parent.name.lower() / f"gh-{meta.get('pr')}"


def render_page(meta: dict[str, Any], paths: list[str]) -> str:
    title = meta.get("title") or f"PR-{meta.get('pr')}"
    body = [
        f"# {title}",
        "",
        f"- Repository: `{meta.get('repo')}`",
        f"- PR: [{meta.get('pr')}]({meta.get('url')})",
        f"- Decision: `{meta.get('decision', meta.get('inclusion_reason', 'include'))}`",
        f"- Reason: {meta.get('inclusion_reason', 'materialized PR evidence')}",
        "",
        "## Changed Paths",
        "",
    ]
    body.extend(f"- `{path}`" for path in paths[:80])
    body.extend(["", "## Evidence Bundle", "", f"`{meta.get('artifact_dir')}`"])
    return "---\n" + yaml.safe_dump(meta, sort_keys=False, allow_unicode=True, width=200) + "---\n" + "\n".join(body) + "\n"


def load_upstream(bundle: Path) -> dict[str, Any] | None:
    path = bundle / "upstream.json"
    if not path.is_file():
        return None
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return None


def pull_to_meta(meta: dict[str, Any], upstream: dict[str, Any], bundle_rel: str) -> tuple[dict[str, Any], list[str]]:
    pull = upstream.get("pull") or {}
    files = upstream.get("files") or []
    paths = []
    for item in files:
        if isinstance(item, dict) and item.get("filename"):
            paths.append(str(item["filename"]))
        elif isinstance(item, str):
            paths.append(item)
    merged_at = pull.get("merged_at") or meta.get("merged_at") or ""
    head = pull.get("head") or {}
    author = pull.get("user") or {}
    meta = dict(meta)
    meta["repo"] = pull.get("base", {}).get("repo", {}).get("full_name") or meta.get("repo")
    meta["title"] = pull.get("title") or meta.get("title") or f"PR-{meta.get('pr')}"
    meta["author"] = author.get("login") or meta.get("author", "unknown")
    meta["date"] = str(merged_at or meta.get("date") or "")[:10]
    meta["url"] = pull.get("html_url") or meta.get("url")
    meta["status"] = "merged" if merged_at else pull.get("state", meta.get("status", "unknown"))
    meta["merge_sha"] = pull.get("merge_commit_sha") or meta.get("merge_sha", "unknown")
    meta["head_ref_oid"] = head.get("sha") or meta.get("head_ref_oid")
    meta["artifact_dir"] = bundle_rel
    if paths:
        meta["changed_paths"] = paths[:120]
    return meta, paths or [str(path) for path in (meta.get("changed_paths") or [])]


def update_candidate_ledgers(root: Path, page_meta: dict[tuple[str, int], dict[str, Any]], removed: set[tuple[str, int]], start: str) -> int:
    changed = 0
    for ledger_path in sorted((root / "candidates").glob("*.yaml")):
        data = yaml.safe_load(ledger_path.read_text(encoding="utf-8")) or {}
        rows = data.get("prs")
        if rows is None:
            rows = data.get("candidates") or []
        touched = False
        for row in rows:
            repo = row.get("repo") or data.get("repo") or ledger_path.stem
            number = row.get("number", row.get("pr"))
            if number is None:
                continue
            key = (str(repo), int(number))
            if key in page_meta:
                meta = page_meta[key]
                row["title"] = meta.get("title") or row.get("title")
                row["date"] = meta.get("date") or row.get("date")
                row["url"] = meta.get("url") or row.get("url")
                row["repo"] = meta.get("repo") or repo
                row["artifact_dir"] = meta.get("artifact_dir")
                row["changed_paths"] = meta.get("changed_paths") or row.get("changed_paths") or row.get("files_changed") or []
                touched = True
            elif key in removed:
                row["decision"] = "exclude"
                row["reason"] = f"outside PR evidence window or failed materialization; start_date={start}"
                touched = True
        if touched:
            counts = {"include": 0, "exclude": 0, "defer": 0}
            for row in rows:
                decision = str(row.get("decision", "")).lower()
                if decision in counts:
                    counts[decision] += 1
            data["total_candidates"] = len(rows)
            data["included"] = counts["include"]
            data["excluded"] = counts["exclude"]
            data["deferred"] = counts["defer"]
            data["prs"] = rows
            ledger_path.write_text(yaml.safe_dump(data, sort_keys=False, allow_unicode=True, width=200), encoding="utf-8")
            changed += 1
    return changed


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--start", default="2024-01-01")
    parser.add_argument("--remove-stale-bundles", action="store_true")
    args = parser.parse_args()

    root = knowledge_root()
    page_meta: dict[tuple[str, int], dict[str, Any]] = {}
    removed: set[tuple[str, int]] = set()
    updated = pruned = missing = 0

    for source in sorted((root / "sources/prs").glob("*/*.md")):
        meta, _body = parse_page(source)
        repo = str(meta.get("repo") or "")
        number = int(meta.get("pr"))
        bundle = bundle_path(root, source, meta)
        upstream = load_upstream(bundle)
        if not upstream:
            removed.add((repo, number))
            source.unlink()
            missing += 1
            continue
        bundle_rel = str(bundle.relative_to(root))
        meta, paths = pull_to_meta(meta, upstream, bundle_rel)
        key = (str(meta.get("repo") or repo), number)
        date_value = str(meta.get("date") or "")
        if date_value and date_value < args.start:
            removed.add(key)
            source.unlink()
            if args.remove_stale_bundles and bundle.exists():
                shutil.rmtree(bundle)
            pruned += 1
            continue
        page_meta[key] = meta
        source.write_text(render_page(meta, paths), encoding="utf-8")
        updated += 1

    ledgers = update_candidate_ledgers(root, page_meta, removed, args.start)
    print(json.dumps({"updated_pages": updated, "pruned_pages": pruned, "missing_bundle_pages": missing, "updated_ledgers": ledgers}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
