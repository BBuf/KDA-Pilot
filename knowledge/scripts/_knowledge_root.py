from __future__ import annotations

import os
from pathlib import Path


def knowledge_root() -> Path:
    override = os.environ.get("KERNEL_KNOWLEDGE_ROOT")
    if override:
        return Path(override).expanduser().resolve()
    return Path(__file__).resolve().parents[1]


def relpath(path: Path) -> str:
    root = knowledge_root()
    try:
        return path.resolve().relative_to(root).as_posix()
    except ValueError:
        return path.as_posix()
