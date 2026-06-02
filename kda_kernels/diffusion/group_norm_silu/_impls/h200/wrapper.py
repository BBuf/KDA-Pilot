"""Wrapper module imported by the generated kda_kernels architecture dispatcher.

After ``scripts/export_kda_kernels/export.py`` promotes this task, the generated
``kda_kernels/diffusion/group_norm_silu/_dispatcher.py`` imports
``kda_kernels.diffusion.group_norm_silu._impls.<arch>.wrapper`` and resolves each
promoted function by name (``getattr(module, "triton_group_norm_silu")`` etc.).
This module exposes those names; the implementation lives in
``group_norm_dispatch.py`` (co-located in the same ``_impls/<arch>/`` directory
after export).
"""

from __future__ import annotations

# Relative-first so the promoted module imports by normal package semantics
# (kda_kernels.diffusion.group_norm_silu._impls.<arch>.wrapper) without relying on a
# sys.path mutation. The absolute fallback supports loading the task `src/` dir
# directly on sys.path (where there is no parent package).
try:
    from .group_norm_dispatch import (  # noqa: F401
        apply_group_norm_silu,
        triton_group_norm_silu,
    )
except ImportError:
    from group_norm_dispatch import (  # noqa: F401
        apply_group_norm_silu,
        triton_group_norm_silu,
    )
