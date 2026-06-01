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
    # Registry single-callable: route to the correct wrapped entry point by callsite,
    # preserving BOTH contracts. The two functions have distinct signatures:
    #   triton_one_pass_rms_norm(x, w, eps=1e-6)            -> (x, w[, eps]) ; eps is a float
    #   norm_infer(x, weight, bias, eps, is_rms_norm=False, out=None)  -> weight+bias tensors + required eps
    if {"is_rms_norm", "bias", "weight", "out"} & set(kwargs):
        return norm_infer(*args, **kwargs)
    if "w" in kwargs:
        return triton_one_pass_rms_norm(*args, **kwargs)
    if len(args) >= 4:  # (x, weight, bias, eps, ...) -> LayerNorm/RMSNorm via norm_infer
        return norm_infer(*args, **kwargs)
    if len(args) == 3:
        # 3 positional args are either norm_infer(x, weight, bias) -- bias is a Tensor
        # or None -- or rms(x, w, eps) -- eps is a float. A valid 3-positional norm_infer
        # also carries eps as a kwarg (norm_infer requires eps), so route the bias forms
        # (None or Tensor) AND the eps-kwarg form to norm_infer; only a bare float/non-None
        # 3rd arg with no eps kwarg is rms's positional eps.
        import torch

        if "eps" in kwargs or args[2] is None or isinstance(args[2], torch.Tensor):
            return norm_infer(*args, **kwargs)  # (x, weight, bias|None[, eps kwarg]) -> norm_infer
        return triton_one_pass_rms_norm(*args, **kwargs)  # (x, w, eps_float) -> RMSNorm
    return triton_one_pass_rms_norm(*args, **kwargs)  # (x, w) -> RMSNorm


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
