"""Wrapper module imported by the generated kda_kernels architecture dispatcher.

After ``scripts/export_kda_kernels/export.py`` promotes this task, the generated
``kda_kernels/diffusion/norm_infer/_dispatcher.py`` imports
``kda_kernels.diffusion.norm_infer._impls.<arch>.wrapper`` and resolves each
promoted function by name (``getattr(module, "norm_infer")`` etc.). This module
exposes those names; the actual implementation lives in ``norm_dispatch.py``
(co-located in the same ``_impls/<arch>/`` directory after export).
"""

from __future__ import annotations

from norm_dispatch import (  # noqa: F401
    norm_infer,
    triton_one_pass_rms_norm,
)
