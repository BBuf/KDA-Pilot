"""Registration entrypoint for the h200_diffusion_norm_infer__multi_shape task.

``norm_infer`` and ``triton_one_pass_rms_norm`` preserve the recovered SGLang
callsite contracts and route the captured production signatures to the
workspace-owned native CUDA kernels, falling back to the SGLang baseline
otherwise (see ``wrapper.py`` / ``interface.md``).

``EXPORTS`` is read (keys only) by ``scripts/export_kda_kernels/export.py`` to
decide which functions to promote; the regenerated kda_kernels stub imports the
promoted names directly from ``wrapper.py``. The wrapper is imported lazily so
this file ``exec``s cleanly even where torch/sglang are absent (e.g. a local
export run that only needs the EXPORTS keys).
"""

from __future__ import annotations

import sys
from pathlib import Path
from typing import Any

# Make ``wrapper`` importable when this file is loaded as a standalone module by
# the KDA correctness/benchmark harness or by export.py (which exec's it in a
# bare namespace -- guard against contexts without ``__file__``).
try:
    _SRC_DIR = str(Path(__file__).resolve().parent)
    if _SRC_DIR not in sys.path:
        sys.path.insert(0, _SRC_DIR)
except NameError:
    pass

KERNEL_SLUG = "h200_diffusion_norm_infer__multi_shape"
OP_TYPE = "layer_or_rms_norm_infer"


def norm_infer(*args: Any, **kwargs: Any) -> Any:
    from wrapper import norm_infer as _impl

    return _impl(*args, **kwargs)


def triton_one_pass_rms_norm(*args: Any, **kwargs: Any) -> Any:
    from wrapper import triton_one_pass_rms_norm as _impl

    return _impl(*args, **kwargs)


def last_dispatch(which: str) -> Any:
    from wrapper import last_dispatch as _impl

    return _impl(which)


def supported_norm_infer(*args: Any, **kwargs: Any) -> Any:
    from wrapper import supported_norm_infer as _impl

    return _impl(*args, **kwargs)


def supported_rms(*args: Any, **kwargs: Any) -> Any:
    from wrapper import supported_rms as _impl

    return _impl(*args, **kwargs)


def build() -> None:
    from wrapper import build as _impl

    _impl()


def optimized_wrapper(*args: Any, **kwargs: Any) -> Any:
    # Registry single-callable: routes to the standard LayerNorm/RMSNorm entry.
    return norm_infer(*args, **kwargs)


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
    "norm_infer": norm_infer,
    "triton_one_pass_rms_norm": triton_one_pass_rms_norm,
}
