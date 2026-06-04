"""Registration entrypoint for the b200_diffusion_cutedsl_norm_scale_shift__multi_shape KDA task.

Exposes the two preserved SGLang public callables (native-CUDA fast path with
vendored-baseline fallback) and the KDA registration metadata. ``wrapper.py``
is loaded by absolute path so this module works whether imported as a package
member or via ``importlib.util.spec_from_file_location`` (as the
correctness/benchmark harness does).

It also stays importable under a bare ``exec`` that does NOT define
``__file__`` (as the KDA export tool does when it only needs the ``EXPORTS``
function-name keys): the wrapper load is deferred and ``EXPORTS`` maps to lazy
proxies in that case.
"""

from __future__ import annotations

import importlib.util
import os
import sys
from typing import Any

KERNEL_SLUG = "b200_diffusion_cutedsl_norm_scale_shift__multi_shape"
OP_TYPE = "cutedsl_norm_scale_shift"


def _load_wrapper():
    wrapper_py = os.path.join(os.path.dirname(os.path.abspath(__file__)), "wrapper.py")
    name = "kda_nss_wrapper"
    if name in sys.modules:
        return sys.modules[name]
    spec = importlib.util.spec_from_file_location(name, wrapper_py)
    assert spec is not None and spec.loader is not None, wrapper_py
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


try:
    _wrapper = _load_wrapper()  # eager when __file__ is available
except Exception:
    _wrapper = None  # bare exec without __file__ (export tool reading keys)


def _resolve(name: str):
    global _wrapper
    if _wrapper is None:
        _wrapper = _load_wrapper()
    return getattr(_wrapper, name)


if _wrapper is not None:
    fused_norm_scale_shift = _wrapper.fused_norm_scale_shift
    fused_scale_residual_norm_scale_shift = (
        _wrapper.fused_scale_residual_norm_scale_shift
    )

    def dispatch_stats():
        return _wrapper.dispatch_stats()

    def shipping_entry_points():
        return _wrapper.shipping_entry_points()

else:

    def fused_norm_scale_shift(*args: Any, **kwargs: Any) -> Any:
        return _resolve("fused_norm_scale_shift")(*args, **kwargs)

    def fused_scale_residual_norm_scale_shift(*args: Any, **kwargs: Any) -> Any:
        return _resolve("fused_scale_residual_norm_scale_shift")(*args, **kwargs)

    def dispatch_stats():
        return _resolve("dispatch_stats")()

    def shipping_entry_points():
        return _resolve("shipping_entry_points")()


# Map preserved SGLang public callable names -> optimized implementations.
EXPORTS = {
    "fused_norm_scale_shift": fused_norm_scale_shift,
    "fused_scale_residual_norm_scale_shift": fused_scale_residual_norm_scale_shift,
}


def optimized_wrapper(*args: Any, **kwargs: Any) -> Any:
    """Single-callable entry preserving BOTH wrapped entry points.

    Routes by signature shape:
    - ``fused_norm_scale_shift(x, weight, bias, scale, shift, norm_type,
      eps=1e-5)`` — 6-7 arguments;
    - ``fused_scale_residual_norm_scale_shift(residual, x, gate, weight,
      bias, scale, shift, norm_type, eps=1e-5)`` — 8-9 arguments (or the
      residual/gate keywords, which only the residual variant accepts).
    """
    if (
        len(args) + len(kwargs) >= 8
        or "residual" in kwargs
        or "gate" in kwargs
    ):
        return fused_scale_residual_norm_scale_shift(*args, **kwargs)
    return fused_norm_scale_shift(*args, **kwargs)


def register() -> dict[str, Any]:
    return {
        "name": KERNEL_SLUG,
        "op_type": OP_TYPE,
        "callable": optimized_wrapper,
        "version": "dev",
        "source": __file__,
        "exports": EXPORTS,
        "dispatch_stats": dispatch_stats,
    }
