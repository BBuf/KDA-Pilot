#!/usr/bin/env python3
from __future__ import annotations

import argparse
from pathlib import Path

from _knowledge_root import knowledge_root


def match_text(text: str, terms: list[str], *, any_term: bool) -> bool:
    haystack = text.lower()
    needles = [term.lower() for term in terms]
    if any_term:
        return any(term in haystack for term in needles)
    return all(term in haystack for term in needles)


def line_has_term(line: str, terms: list[str]) -> bool:
    haystack = line.lower()
    return any(term.lower() in haystack for term in terms)


def main() -> int:
    parser = argparse.ArgumentParser(description="Search every materialized PR review.diff in the local corpus")
    parser.add_argument("terms", nargs="+", help="terms to search for")
    parser.add_argument("--any", action="store_true", help="match diffs containing any term instead of all terms")
    parser.add_argument("--limit", type=int, default=200)
    args = parser.parse_args()

    root = knowledge_root()
    diff_paths = sorted((root / "evidence" / "pull-bundles").glob("*/*/review.diff"))
    hits = 0
    matched_diffs: set[Path] = set()
    for diff_path in diff_paths:
        try:
            text = diff_path.read_text(encoding="utf-8", errors="replace")
        except OSError:
            continue
        if not match_text(text, args.terms, any_term=args.any):
            continue
        lines = text.splitlines()
        for lineno, line in enumerate(lines, start=1):
            if not line_has_term(line, args.terms):
                continue
            print(f"{diff_path.relative_to(root)}:{lineno}: {line[:500]}")
            hits += 1
            matched_diffs.add(diff_path)
            if hits >= args.limit:
                print(f"hits={hits} matched_diffs={len(matched_diffs)} searched_diffs={len(diff_paths)} truncated=true")
                return 0
    print(f"hits={hits} matched_diffs={len(matched_diffs)} searched_diffs={len(diff_paths)} truncated=false")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
