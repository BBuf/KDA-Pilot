#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re

from _kb import as_list, iter_pages, load_aliases, normalize_term, page_text


def matches_filter(values: list[str], expected: str | None, aliases: dict[str, str]) -> bool:
    if not expected:
        return True
    needle = normalize_term(expected, aliases)
    normalized = {normalize_term(value, aliases) for value in values}
    return needle in normalized


def matches_repo(value: str, expected: str | None) -> bool:
    if not expected:
        return True
    value_low = value.lower()
    expected_low = expected.lower()
    return value_low == expected_low or value_low.rsplit("/", 1)[-1] == expected_low


def topic_values(meta: dict) -> list[str]:
    values: list[str] = []
    for key in ("tags", "techniques", "hardware_features", "kernel_types", "symptoms"):
        values.extend(as_list(meta.get(key)))
    return values


def score_page(text: str, terms: list[str]) -> int:
    low = text.lower()
    score = 0
    for term in terms:
        term_low = term.lower()
        if term_low in low:
            score += 10
        for token in re.findall(r"[a-zA-Z0-9_.+-]+", term_low):
            if token and token in low:
                score += 1
    return score


def main() -> int:
    parser = argparse.ArgumentParser(description="Search KernelPilot PR diff evidence pages")
    parser.add_argument("query", nargs="*", help="keyword query")
    parser.add_argument("--type", dest="type_filter")
    parser.add_argument("--tag")
    parser.add_argument("--repo")
    parser.add_argument("--language")
    parser.add_argument("--architecture")
    parser.add_argument("--kernel-type")
    parser.add_argument("--symptom")
    parser.add_argument("--confidence")
    parser.add_argument("--limit", type=int, default=20)
    parser.add_argument("--compact", action="store_true")
    parser.add_argument("--paths-only", action="store_true")
    args = parser.parse_args()

    aliases = load_aliases()
    terms = [normalize_term(term, aliases) for term in args.query]
    rows = []
    for page in iter_pages():
        meta = page.meta
        if args.type_filter and page.kind != args.type_filter and meta.get("type") != args.type_filter:
            continue
        if not matches_repo(str(meta.get("repo", "")), args.repo):
            continue
        if not matches_filter(topic_values(meta), args.tag, aliases):
            continue
        if not matches_filter(as_list(meta.get("languages")), args.language, aliases):
            continue
        if not matches_filter(as_list(meta.get("architectures")), args.architecture, aliases):
            continue
        if not matches_filter(as_list(meta.get("kernel_types")), args.kernel_type, aliases):
            continue
        if not matches_filter(as_list(meta.get("symptoms")), args.symptom, aliases):
            continue
        if args.confidence and meta.get("confidence") != args.confidence:
            continue
        text = page_text(page)
        score = score_page(text, terms) if terms else 1
        if score <= 0:
            continue
        rows.append((score, page))

    rows.sort(key=lambda item: (-item[0], item[1].relpath))
    rows = rows[: args.limit]
    if args.paths_only:
        for _, page in rows:
            print(page.relpath)
        return 0
    if args.compact:
        for score, page in rows:
            tags = ",".join(as_list(page.meta.get("tags"))[:5])
            artifact_dir = page.meta.get("artifact_dir", "-")
            print(f"{page.id or '-'} | PR | score={score} | {page.relpath} | {artifact_dir} | {tags} | {page.title}")
        return 0
    print("| ID | Score | Path | Evidence Bundle | Title | Tags |")
    print("| --- | ---: | --- | --- | --- | --- |")
    for score, page in rows:
        tags = ", ".join(as_list(page.meta.get("tags"))[:8])
        artifact_dir = page.meta.get("artifact_dir", "-")
        print(f"| `{page.id or '-'}` | {score} | `{page.relpath}` | `{artifact_dir}` | {page.title} | {tags} |")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
