#!/usr/bin/env python3
from __future__ import annotations

import argparse
from pathlib import Path

import yaml

from _kb import id_map, parse_markdown
from _knowledge_root import knowledge_root


def render_page(path: Path, *, frontmatter_only: bool, body_only: bool) -> str:
    page = parse_markdown(path)
    if frontmatter_only:
        return yaml.safe_dump(page.meta, sort_keys=False, allow_unicode=True)
    if body_only:
        return page.body
    return path.read_text(encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Fetch a KernelPilot PR evidence page by id or path")
    parser.add_argument("page")
    parser.add_argument("--follow-sources", action="store_true", help="Deprecated no-op kept for compatibility; PR pages are the source.")
    parser.add_argument("--frontmatter-only", action="store_true")
    parser.add_argument("--body-only", action="store_true")
    args = parser.parse_args()

    root = knowledge_root()
    pages = id_map()
    page = pages.get(args.page)
    path = page.path if page else root / args.page
    if not path.exists():
        raise SystemExit(f"page not found: {args.page}")
    print(render_page(path, frontmatter_only=args.frontmatter_only, body_only=args.body_only), end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
