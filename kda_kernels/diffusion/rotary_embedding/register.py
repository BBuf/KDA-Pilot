"""Registration entrypoint for the b200_diffusion_rotary_embedding__multi_shape task.

``optimized_wrapper`` preserves the recovered SGLang callsite contract and routes
the captured production signatures to the workspace-owned native CUDA kernels,
falling back to the SGLang baseline otherwise (see ``wrapper.py``).

``EXPORTS`` is read by ``scripts/export_kda_kernels/export.py`` (keys only) to
decide which functions to promote; the regenerated kda_kernels stub imports the
promoted names directly from ``wrapper.py``. The wrapper is imported lazily so this
file ``exec``s cleanly even where torch/sglang are absent (e.g. a local export run).
"""

from __future__ import annotations

import sys
from pathlib import Path
from typing import Any

# Make ``wrapper`` importable when this file is loaded as a standalone module by
# the KDA correctness/benchmark harness. Guard against exec contexts without
# ``__file__`` (export.py reads EXPORTS by exec'ing this file in a bare namespace).
try:
    _SRC_DIR = str(Path(__file__).resolve().parent)
    if _SRC_DIR not in sys.path:
        sys.path.insert(0, _SRC_DIR)
except NameError:
    pass

KERNEL_SLUG = "b200_diffusion_rotary_embedding__multi_shape"
OP_TYPE = "rotary_embedding"


def apply_rotary_embedding(*args: Any, **kwargs: Any) -> Any:
    from wrapper import apply_rotary_embedding as _impl

    return _impl(*args, **kwargs)


def apply_ltx2_split_rotary_emb(*args: Any, **kwargs: Any) -> Any:
    from wrapper import apply_ltx2_split_rotary_emb as _impl

    return _impl(*args, **kwargs)


def optimized_wrapper(*args: Any, **kwargs: Any) -> Any:
    # Registry single-callable: routes to the standard entry point.
    return apply_rotary_embedding(*args, **kwargs)


def register() -> dict[str, Any]:
    return {
        "name": KERNEL_SLUG,
        "op_type": OP_TYPE,
        "callable": optimized_wrapper,
        "version": "dev",
        "source": __file__,
    }


# Only the keys matter to the export tool; the kda_kernels stub imports the
# promoted names directly from wrapper.py. Partial promotion is supported.
EXPORTS = {
    "apply_rotary_embedding": apply_rotary_embedding,
    "apply_ltx2_split_rotary_emb": apply_ltx2_split_rotary_emb,
}
