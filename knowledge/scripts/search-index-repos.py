#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
import subprocess
from pathlib import Path

from _knowledge_root import knowledge_root
from clone_index_repos_support import extract_repos_from_index, repo_dir


def main() -> int:
    parser = argparse.ArgumentParser(description="Search all repositories cloned from knowledge/index.json")
    parser.add_argument("terms", nargs="+", help="terms passed to ripgrep")
    parser.add_argument("--dest", type=Path, default=knowledge_root() / "external-repos")
    parser.add_argument("--limit-per-repo", type=int, default=80)
    args = parser.parse_args()

    index_path = knowledge_root() / "index.json"
    repos = extract_repos_from_index(index_path)
    missing = [repo for repo in repos if not (repo_dir(args.dest, repo) / ".git").is_dir()]
    if missing:
        print("missing cloned repos; run `python3 scripts/clone-index-repos.py` first")
        for repo in missing:
            print(repo)
        return 2

    pattern = "|".join(re.escape(term) for term in args.terms)
    total_hits = 0
    for repo in repos:
        target = repo_dir(args.dest, repo)
        cmd = [
            "rg",
            "-n",
            "-i",
            "--hidden",
            "--glob",
            "!.git",
            "--max-count",
            str(args.limit_per_repo),
            pattern,
            str(target),
        ]
        print(f"\n# {repo}")
        completed = subprocess.run(cmd, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if completed.stdout:
            print(completed.stdout, end="")
            total_hits += len(completed.stdout.splitlines())
        if completed.returncode not in (0, 1):
            print(completed.stderr, end="")
            return completed.returncode
    print(f"\nrepos={len(repos)} hits={total_hits}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
