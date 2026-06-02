"""Wrapper module imported by the generated kda_kernels architecture dispatcher.

After ``scripts/export_kda_kernels/export.py`` promotes this task, the generated
``kda_kernels/diffusion/norm_infer/_dispatcher.py`` imports
``kda_kernels.diffusion.norm_infer._impls.<arch>.wrapper`` and resolves each
promoted function by name (``getattr(module, "norm_infer")`` etc.). This module
exposes those names; the actual implementation lives in ``norm_dispatch.py``
(co-located in the same ``_impls/<arch>/`` directory after export).
"""

from __future__ import annotations

# Relative-first so the promoted module imports by normal package semantics
# (kda_kernels.diffusion.norm_infer._impls.<arch>.wrapper) without relying on a
# sys.path mutation and without colliding with any unrelated top-level
# `norm_dispatch`. The absolute fallback supports loading the task `src/` dir
# directly on sys.path (where there is no parent package).
try:
    from .norm_dispatch import (  # noqa: F401
        norm_infer,
        triton_one_pass_rms_norm,
    )
except ImportError:
    from norm_dispatch import (  # noqa: F401
        norm_infer,
        triton_one_pass_rms_norm,
    )
