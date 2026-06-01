"""Registration for the h200_diffusion_norm_infer__multi_shape KDA task.

Exposes the two public SGLang callable names (``norm_infer`` and
``triton_one_pass_rms_norm``) backed by the zero-overhead native-CUDA
dispatcher in ``norm_dispatch.py``. Unsupported signatures fall back to the
SGLang baseline.
"""

from __future__ import annotations

import pathlib
import sys
from typing import Any

# Allow loading as a standalone file (the harness uses spec_from_file_location).
_SRC = str(pathlib.Path(__file__).resolve().parent)
if _SRC not in sys.path:
    sys.path.insert(0, _SRC)

from norm_dispatch import (  # noqa: E402
    norm_infer,
    triton_one_pass_rms_norm,
)

KERNEL_SLUG = "h200_diffusion_norm_infer__multi_shape"
OP_TYPE = "layer_or_rms_norm_infer"


def optimized_wrapper(*args: Any, **kwargs: Any) -> Any:
    """Route by the recovered callsite contract: the RMSNorm entry takes
    ``(x, w, eps)``; the norm_infer entry takes ``(x, weight, bias, eps, ...)``.
    The two public names are also exported at module scope for direct binding."""
    if "is_rms_norm" in kwargs or len(args) >= 4:
        return norm_infer(*args, **kwargs)
    return triton_one_pass_rms_norm(*args, **kwargs)


def register() -> dict[str, Any]:
    return {
        "name": KERNEL_SLUG,
        "op_type": OP_TYPE,
        "callable": optimized_wrapper,
        "entry_points": {
            "norm_infer": norm_infer,
            "triton_one_pass_rms_norm": triton_one_pass_rms_norm,
        },
        "version": "dev",
        "source": __file__,
    }
