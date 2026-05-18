from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import yaml

from _knowledge_root import knowledge_root, relpath


FRONTMATTER_RE = re.compile(r"\A---\n(.*?)\n---\n?", re.S)


@dataclass
class Page:
    path: Path
    relpath: str
    meta: dict[str, Any]
    body: str

    @property
    def id(self) -> str:
        return str(self.meta.get("id") or "")

    @property
    def title(self) -> str:
        return str(self.meta.get("title") or self.path.stem)

    @property
    def kind(self) -> str:
        if self.relpath.startswith("sources/"):
            return str(self.meta.get("source_type") or self.meta.get("source_category") or "source")
        return str(self.meta.get("type") or "page")


def parse_markdown(path: Path) -> Page:
    text = path.read_text(encoding="utf-8")
    match = FRONTMATTER_RE.match(text)
    if not match:
        return Page(path, relpath(path), {}, text)
    meta = yaml.safe_load(match.group(1)) or {}
    body = text[match.end() :]
    return Page(path, relpath(path), meta, body)


def iter_pages() -> list[Page]:
    root = knowledge_root()
    bases = [root / "sources" / "prs"]
    pages: list[Page] = []
    for base in bases:
        if not base.exists():
            continue
        for path in sorted(base.rglob("*.md")):
            pages.append(parse_markdown(path))
    return pages


def load_aliases() -> dict[str, str]:
    path = knowledge_root() / "data/aliases.yaml"
    if not path.exists():
        return {}
    data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    aliases: dict[str, str] = {}
    for canonical, values in data.items():
        aliases[str(canonical).lower()] = str(canonical).lower()
        for value in values or []:
            aliases[str(value).lower()] = str(canonical).lower()
    return aliases


def normalize_term(value: str, aliases: dict[str, str]) -> str:
    key = value.lower().replace("_", "-")
    return aliases.get(key, aliases.get(value.lower(), key))


def as_list(value: Any) -> list[str]:
    if value is None:
        return []
    if isinstance(value, list):
        return [str(item) for item in value]
    return [str(value)]


def page_text(page: Page) -> str:
    values = [page.title, page.id, page.relpath, page.body]
    for value in page.meta.values():
        if isinstance(value, (str, int, float)):
            values.append(str(value))
        elif isinstance(value, list):
            values.extend(str(item) for item in value)
    return "\n".join(values)


def id_map() -> dict[str, Page]:
    out: dict[str, Page] = {}
    for page in iter_pages():
        if page.id:
            out[page.id] = page
        out[page.relpath] = page
    return out
