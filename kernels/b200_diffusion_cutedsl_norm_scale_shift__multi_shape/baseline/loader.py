"""Expose the vendored SGLang jit_kernel snapshot as ``sglang.jit_kernel``.

The snapshot under ``upstream_jit_kernel/`` is a verbatim copy of
``python/sglang/jit_kernel`` from the pinned SGLang commit (see
``docs/baseline_source.md``). Its modules import each other through absolute
``sglang.jit_kernel.*`` names; this loader satisfies those imports from the
snapshot without requiring (or touching) an installed SGLang checkout.

Lineage guard: installation refuses to proceed if a real SGLang package is
already imported, and ``assert_snapshot_only()`` verifies that every
``sglang*`` module in ``sys.modules`` resolves into the snapshot directory.
"""

from __future__ import annotations

import importlib
import importlib.util
import sys
import types
from pathlib import Path

SNAPSHOT_ROOT = Path(__file__).resolve().parent / "upstream_jit_kernel"
_JIT_KERNEL_DIR = SNAPSHOT_ROOT / "jit_kernel"
_ALIAS_MARK = "__kda_baseline_alias__"


def _module_file(mod) -> str:
    return getattr(mod, "__file__", None) or ""


def _inside_snapshot(path_str: str) -> bool:
    try:
        return str(Path(path_str).resolve()).startswith(str(SNAPSHOT_ROOT))
    except (OSError, ValueError):
        return False


def install_baseline() -> types.ModuleType:
    """Register the snapshot as ``sglang.jit_kernel`` and return that module."""
    existing = sys.modules.get("sglang")
    if existing is not None and not getattr(existing, _ALIAS_MARK, False):
        raise RuntimeError(
            "A real `sglang` package is already imported; refusing to alias the "
            "baseline snapshot over it. Baseline consumers must run in a process "
            "that never imports SGLang (see docs/baseline_source.md)."
        )
    if existing is None:
        alias = types.ModuleType("sglang")
        alias.__path__ = []  # no filesystem search; submodules registered explicitly
        setattr(alias, _ALIAS_MARK, True)
        sys.modules["sglang"] = alias
    else:
        alias = existing

    if "sglang.utils" not in sys.modules:
        # Single out-of-snapshot symbol used by jit_kernel/utils.py
        # (`from sglang.utils import is_in_ci`). Behavior-equivalent stub:
        # CI detection via environment, False in normal runs.
        stub = types.ModuleType("sglang.utils")
        setattr(stub, _ALIAS_MARK, True)

        def is_in_ci() -> bool:
            import os

            return os.getenv("SGLANG_IS_IN_CI", os.getenv("CI", "")).lower() in (
                "1",
                "true",
                "yes",
            )

        stub.is_in_ci = is_in_ci
        sys.modules["sglang.utils"] = stub
        alias.utils = stub

    if "sglang.jit_kernel" not in sys.modules:
        spec = importlib.util.spec_from_file_location(
            "sglang.jit_kernel",
            _JIT_KERNEL_DIR / "__init__.py",
            submodule_search_locations=[str(_JIT_KERNEL_DIR)],
        )
        assert spec is not None and spec.loader is not None, _JIT_KERNEL_DIR
        mod = importlib.util.module_from_spec(spec)
        sys.modules["sglang.jit_kernel"] = mod
        spec.loader.exec_module(mod)
        alias.jit_kernel = mod
    return sys.modules["sglang.jit_kernel"]


def baseline_module() -> types.ModuleType:
    """Import and return the vendored norm-scale-shift module."""
    install_baseline()
    return importlib.import_module(
        "sglang.jit_kernel.diffusion.cutedsl.scale_residual_norm_scale_shift"
    )


def assert_snapshot_only() -> None:
    """Guard: every imported ``sglang*`` module must come from the snapshot."""
    offenders = []
    for name, mod in list(sys.modules.items()):
        if name != "sglang" and not name.startswith("sglang."):
            continue
        if mod is None:
            continue
        if getattr(mod, _ALIAS_MARK, False):
            continue  # our alias root / stub modules
        file_path = _module_file(mod)
        if file_path:
            if not _inside_snapshot(file_path):
                offenders.append((name, file_path))
            continue
        # Namespace packages (e.g. sglang.jit_kernel.diffusion) carry no
        # __file__; check their search paths instead.
        paths = list(getattr(mod, "__path__", []) or [])
        if not paths or not all(_inside_snapshot(p) for p in paths):
            offenders.append((name, paths))
    if offenders:
        raise RuntimeError(f"Non-snapshot sglang modules present: {offenders}")
