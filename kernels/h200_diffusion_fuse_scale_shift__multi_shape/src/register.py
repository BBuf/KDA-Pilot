"""Registration entry point for the h200_diffusion_fuse_scale_shift__multi_shape KDA task.

Exposes the three recovered SGLang public callables through the solution/
dispatcher (native CUDA when in-contract, vendored Triton baseline otherwise).

The module body stays import-light and never touches ``__file__`` at import
time so export tooling can ``exec`` it in a bare namespace and still read
``EXPORTS``; the dispatcher import resolves lazily at call time.
"""

from __future__ import annotations

from typing import Any

KERNEL_SLUG = "h200_diffusion_fuse_scale_shift__multi_shape"
OP_TYPE = "fuse_scale_shift"

_DISPATCH = None


def _dispatch_module():
    global _DISPATCH
    if _DISPATCH is None:
        import sys
        from pathlib import Path

        kernel_dir = str(Path(__file__).resolve().parents[1])
        if kernel_dir not in sys.path:
            sys.path.insert(0, kernel_dir)
        from solution import dispatch as _mod

        _DISPATCH = _mod
    return _DISPATCH


def fuse_scale_shift_kernel(*args: Any, **kwargs: Any) -> Any:
    return _dispatch_module().fuse_scale_shift_kernel(*args, **kwargs)


def fuse_layernorm_scale_shift_gate_select01_kernel(*args: Any, **kwargs: Any) -> Any:
    return _dispatch_module().fuse_layernorm_scale_shift_gate_select01_kernel(
        *args, **kwargs
    )


def fuse_residual_layernorm_scale_shift_gate_select01_kernel(
    *args: Any, **kwargs: Any
) -> Any:
    return _dispatch_module().fuse_residual_layernorm_scale_shift_gate_select01_kernel(
        *args, **kwargs
    )


def optimized_wrapper(*args: Any, **kwargs: Any) -> Any:
    """Generic entry point: routes to the matching public op by signature."""
    return _dispatch_module().optimized_wrapper(*args, **kwargs)


EXPORTS = {
    "fuse_scale_shift_kernel": fuse_scale_shift_kernel,
    "fuse_layernorm_scale_shift_gate_select01_kernel": (
        fuse_layernorm_scale_shift_gate_select01_kernel
    ),
    "fuse_residual_layernorm_scale_shift_gate_select01_kernel": (
        fuse_residual_layernorm_scale_shift_gate_select01_kernel
    ),
}


def register() -> dict[str, Any]:
    return {
        "name": KERNEL_SLUG,
        "op_type": OP_TYPE,
        "callable": optimized_wrapper,
        "version": "dev",
        "source": __file__,
    }
