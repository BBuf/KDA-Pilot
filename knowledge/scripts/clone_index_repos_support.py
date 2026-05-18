from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any


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


def extract_repos_from_index(index_path: Path) -> list[str]:
    return extract_repos(json.loads(index_path.read_text(encoding="utf-8")))


def repo_dir(dest: Path, repo: str) -> Path:
    return dest / repo.replace("/", "__")
