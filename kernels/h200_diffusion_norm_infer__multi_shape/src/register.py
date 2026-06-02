"""Registration for the h200_diffusion_norm_infer__multi_shape KDA task.

Exposes the two public SGLang callable names (``norm_infer`` and
``triton_one_pass_rms_norm``) backed by the zero-overhead native-CUDA
dispatcher in ``norm_dispatch.py`` (re-exported by ``wrapper.py``).

``EXPORTS`` is the contract consumed by
``scripts/export_kda_kernels/export.py``: it maps each public SGLang callable
name to the wrapper that replaces it after promotion into ``kda_kernels``. The
export tool reads ``EXPORTS`` by ``exec``-ing this file in a bare namespace
(no ``__file__``, possibly no sglang/torch), so the bindings below are guarded
to keep the dict's keys readable in that environment; the callables themselves
are resolved at runtime where the GPU stack is available.
"""

from __future__ import annotations

import pathlib
import sys
from typing import Any

KERNEL_SLUG = "h200_diffusion_norm_infer__multi_shape"
OP_TYPE = "layer_or_rms_norm_infer"

# Make the task src dir importable when loaded as a standalone file. Guarded
# because the export tool exec()s this file without __file__ defined.
try:
    _SRC = str(pathlib.Path(__file__).resolve().parent)
    if _SRC not in sys.path:
        sys.path.insert(0, _SRC)
except NameError:
    pass

try:
    from norm_dispatch import norm_infer, triton_one_pass_rms_norm
except Exception:  # pragma: no cover - export-time read without the GPU stack
    norm_infer = None  # type: ignore[assignment]
    triton_one_pass_rms_norm = None  # type: ignore[assignment]

# Public SGLang callable name -> replacement wrapper. Read by the export tool.
EXPORTS = {
    "norm_infer": norm_infer,
    "triton_one_pass_rms_norm": triton_one_pass_rms_norm,
}

# Distinctive keyword args of each entry point, used to disambiguate the generic
# wrapper. norm_infer has weight/bias/is_rms_norm/out; rms has w.
_NORM_INFER_KW = frozenset({"weight", "bias", "is_rms_norm", "out"})


def optimized_wrapper(*args: Any, **kwargs: Any) -> Any:
    """Generic entry that routes to the correct public function by its distinctive
    parameters. Prefer the explicit ``EXPORTS`` functions; this rejects genuinely
    ambiguous calls rather than silently choosing one."""
    # norm_infer: norm_infer(x, weight, bias, eps[, is_rms_norm, out]) -- eps is required.
    # It is selected by a distinctive kwarg (weight/bias/is_rms_norm/out), or >=4 positional
    # (x, weight, bias, eps), or exactly 3 positional + `eps=` (x, weight, bias, eps=...) --
    # the one-pass RMS 3-positional form passes eps POSITIONALLY (x, w, eps), never as a kwarg,
    # so "3 positional + eps kwarg" is unambiguously norm_infer.
    if _NORM_INFER_KW & kwargs.keys() or len(args) >= 4 or (len(args) == 3 and "eps" in kwargs):
        return norm_infer(*args, **kwargs)
    # RMSNorm: triton_one_pass_rms_norm(x, w, eps=1e-6) -- valid with 2 or 3 positional args
    # (default eps), `(x, w, eps=...)`, or explicit `w=`.
    if "w" in kwargs or len(args) in (2, 3):
        return triton_one_pass_rms_norm(*args, **kwargs)
    raise TypeError(
        "optimized_wrapper: ambiguous call; call the explicit entry point "
        "norm_infer(x, weight, bias, eps, ...) or "
        "triton_one_pass_rms_norm(x, w, eps) instead."
    )


def register() -> dict[str, Any]:
    return {
        "name": KERNEL_SLUG,
        "op_type": OP_TYPE,
        "callable": optimized_wrapper,
        "exports": dict(EXPORTS),
        "version": "dev",
        "source": __file__,
    }
