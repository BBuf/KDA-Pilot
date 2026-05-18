#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
import subprocess
from pathlib import Path
from typing import Any

from _knowledge_root import knowledge_root


GITHUB_RE = re.compile(r"github\.com[:/]+([^/\s]+)/([^/\s#?]+)")


def walk_strings(value: Any):
    if isinstance(value, str):
        yield value
    elif isinstance(value, list):
        for item in value:
            yield from walk_strings(item)
    elif isinstance(value, dict):
        for item in value.values():
            yield from walk_strings(item)


def normalize_repo(owner: str, repo: str) -> str:
    repo = repo.removesuffix(".git").rstrip("/")
    return f"{owner}/{repo}"


def extract_repos(index: dict[str, Any]) -> list[str]:
    repos: set[str] = set()
    for framework in index.get("frameworks") or []:
        repo = framework.get("repo")
        if isinstance(repo, str) and "/" in repo:
            repos.add(repo.removesuffix(".git"))

    for text in walk_strings(index):
        for match in GITHUB_RE.finditer(text):
            repos.add(normalize_repo(match.group(1), match.group(2)))

    return sorted(repos, key=str.lower)


def main() -> int:
    parser = argparse.ArgumentParser(description="Clone every GitHub repo referenced by knowledge/index.json")
    parser.add_argument("--index", type=Path, default=knowledge_root() / "index.json")
    parser.add_argument("--dest", type=Path, default=knowledge_root() / "external-repos")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    index = json.loads(args.index.read_text(encoding="utf-8"))
    repos = extract_repos(index)
    args.dest.mkdir(parents=True, exist_ok=True)

    for repo in repos:
        target = args.dest / repo.replace("/", "__")
        url = f"https://github.com/{repo}.git"
        if args.dry_run:
            print(f"{repo}\t{target}")
            continue
        if (target / ".git").is_dir():
            print(f"exists\t{repo}\t{target}")
            continue
        print(f"clone\t{repo}\t{target}")
        subprocess.run(["git", "clone", url, str(target)], check=True)

    print(f"repos={len(repos)} dest={args.dest}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
