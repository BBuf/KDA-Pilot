#!/usr/bin/env python3
from __future__ import annotations

import argparse
import subprocess
from pathlib import Path

from _knowledge_root import knowledge_root
from clone_index_repos_support import extract_repos_from_index, repo_dir


def main() -> int:
    parser = argparse.ArgumentParser(description="Clone every GitHub repo referenced by knowledge/index.json")
    parser.add_argument("--index", type=Path, default=knowledge_root() / "index.json")
    parser.add_argument("--dest", type=Path, default=knowledge_root() / "external-repos")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    repos = extract_repos_from_index(args.index)
    args.dest.mkdir(parents=True, exist_ok=True)

    for repo in repos:
        target = repo_dir(args.dest, repo)
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
