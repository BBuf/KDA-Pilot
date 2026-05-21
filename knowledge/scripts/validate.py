#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

import yaml

from _kb import iter_pages, parse_markdown
from _knowledge_root import knowledge_root
from clone_index_repos_support import extract_repos


PULL_BUNDLE_ROOT = Path("evidence") / "pull-bundles"
DIFF_NAME = "review.diff"
UPSTREAM_NAME = "upstream.json"
ORIGIN_NAME = "ORIGIN.yaml"
DISCUSSION_NAME = "discussion.md"
SNAPSHOT_DIR = "source-snapshot"


def source_pr_bundle(root: Path, repo: str, number: object, fallback_repo_id: str) -> Path:
    repo_id = fallback_repo_id.lower()
    return root / PULL_BUNDLE_ROOT / repo_id / f"gh-{number}"


def main() -> int:
    root = knowledge_root()
    errors: list[str] = []
    index_repos = 0
    index_path = root / "index.json"
    if index_path.exists():
        try:
            index_data = json.loads(index_path.read_text(encoding="utf-8"))
        except Exception as exc:  # noqa: BLE001
            errors.append(f"{index_path.relative_to(root)}: invalid json: {exc}")
            index_data = {}
        stack = [index_data]
        while stack:
            value = stack.pop()
            if isinstance(value, dict):
                if "ncu_signals" in value:
                    errors.append(f"{index_path.relative_to(root)}: ncu_signals is not allowed")
                for stale_key in ("page", "deep_reference", "pr_reference"):
                    if stale_key in value:
                        errors.append(f"{index_path.relative_to(root)}: {stale_key} is not allowed")
                stack.extend(value.values())
            elif isinstance(value, list):
                stack.extend(value)
        index_repos = len(extract_repos(index_data))
    pages = iter_pages()
    ids: dict[str, str] = {}
    for page in pages:
        if not page.meta:
            errors.append(f"{page.relpath}: missing YAML frontmatter")
            continue
        page_id = page.meta.get("id")
        if page_id:
            if page_id in ids:
                errors.append(f"{page.relpath}: duplicate id {page_id} also in {ids[page_id]}")
            ids[str(page_id)] = page.relpath
        else:
            errors.append(f"{page.relpath}: missing id")

    for page in pages:
        if not page.relpath.startswith("sources/prs/"):
            errors.append(f"{page.relpath}: non-PR page indexed")

    source_prs = 0
    complete_source_pr_bundles = 0
    for source in (root / "sources/prs").glob("*/*.md"):
        source_prs += 1
        page = parse_markdown(source)
        repo = str(page.meta.get("repo", ""))
        number = page.meta.get("pr")
        artifact_dir = page.meta.get("artifact_dir")
        if artifact_dir:
            bundle = root / artifact_dir
        else:
            bundle = source_pr_bundle(root, repo, number, source.parent.name)
        missing = []
        for required in (DIFF_NAME, UPSTREAM_NAME, ORIGIN_NAME):
            if not (bundle / required).is_file():
                missing.append(required)
        if not (bundle / SNAPSHOT_DIR).is_dir():
            missing.append(f"{SNAPSHOT_DIR}/")
        if missing:
            errors.append(f"{source.relative_to(root)}: incomplete evidence bundle {bundle.relative_to(root)} missing {', '.join(missing)}")
        else:
            complete_source_pr_bundles += 1

    ledgers = list((root / "candidates").glob("*.yaml"))
    candidate_prs = 0
    for ledger in ledgers:
        try:
            data = yaml.safe_load(ledger.read_text(encoding="utf-8"))
        except Exception as exc:  # noqa: BLE001
            errors.append(f"{ledger.relative_to(root)}: invalid yaml: {exc}")
            continue
        entries = data.get("candidates")
        if entries is None:
            entries = data.get("prs", [])
        for entry in entries or []:
            if str(entry.get("decision", "")).lower() == "exclude":
                continue
            candidate_prs += 1
            number = entry.get("pr", entry.get("number"))
            label = f"{entry.get('repo', ledger.stem)}#{number}"
            artifact_dir = entry.get("artifact_dir")
            if not artifact_dir:
                continue
            bundle = root / artifact_dir
            for required in (DIFF_NAME, ORIGIN_NAME):
                if not (bundle / required).is_file():
                    errors.append(f"{artifact_dir}: {label} missing {required}")
            if not (bundle / SNAPSHOT_DIR).is_dir():
                errors.append(f"{artifact_dir}: {label} missing {SNAPSHOT_DIR}/")

    discussion_files = 0
    for discussion in (root / PULL_BUNDLE_ROOT).glob(f"*/*/{DISCUSSION_NAME}"):
        discussion_files += 1
        text = discussion.read_text(encoding="utf-8")
        lines = [line for line in text.splitlines() if line.strip()]
        if not lines:
            errors.append(f"{discussion.relative_to(root)}: empty discussion.md")
            continue
        for line in lines:
            if not line.startswith("- "):
                errors.append(f"{discussion.relative_to(root)}: discussion.md must be a plain bullet list")
                break

    summary = {
        "pages": len(pages),
        "ids": len(ids),
        "pull_bundles": len(list((root / PULL_BUNDLE_ROOT).glob("*/*"))),
        "source_prs": source_prs,
        "complete_source_pr_bundles": complete_source_pr_bundles,
        "discussion_files": discussion_files,
        "candidate_prs": candidate_prs,
        "candidate_ledgers": len(ledgers),
        "index_repos": index_repos,
        "errors": len(errors),
    }
    print(json.dumps(summary, indent=2, ensure_ascii=False))
    for error in errors:
        print(f"ERROR: {error}")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
