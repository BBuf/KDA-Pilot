"""Deterministic dispatcher for the fused scale-shift kernel family.

Routes each public call to a native CUDA variant when the signature is
in-contract for one, otherwise to the vendored Triton baseline (baseline/).
The route taken by the most recent call is observable via consume_last_route()
so the harnesses can assert routing behavior.

Native kernels land incrementally; until an op's native path exists,
native_status() reports False for it and every call falls back.
"""

from __future__ import annotations

import sys
from pathlib import Path

_KERNEL_DIR = Path(__file__).resolve().parents[1]
if str(_KERNEL_DIR) not in sys.path:
    sys.path.insert(0, str(_KERNEL_DIR))

from baseline import scale_shift as _baseline  # noqa: E402

OP_SCALE_SHIFT = "scale_shift"
OP_SELECT01 = "select01"
OP_RESIDUAL = "residual_select01"

# Production buckets the dispatcher intentionally routes to the baseline for
# performance (recorded honestly as fallback, counted 1.0x). Filled only by
# benchmark-evidence decisions; format: {op: {bucket_key, ...}}.
PERF_FALLBACK: dict[str, set] = {OP_SCALE_SHIFT: set(), OP_SELECT01: set(), OP_RESIDUAL: set()}

# The most recent routing decision: (route, detail) where route is
# "native" or "fallback".
_LAST_ROUTE: tuple[str, str] | None = None


def _set_route(route: str, detail: str) -> None:
    global _LAST_ROUTE
    _LAST_ROUTE = (route, detail)


def consume_last_route() -> tuple[str, str] | None:
    global _LAST_ROUTE
    r = _LAST_ROUTE
    _LAST_ROUTE = None
    return r


def native_status() -> dict[str, bool]:
    """Which ops currently have a native CUDA path wired in."""
    return {OP_SCALE_SHIFT: False, OP_SELECT01: False, OP_RESIDUAL: False}


# ---------------------------------------------------------------------------
# Public entry points (signatures mirror the recovered baseline contract).
# ---------------------------------------------------------------------------

def fuse_scale_shift_kernel(
    x,
    scale,
    shift,
    scale_constant: float = 1.0,
    block_l: int = 128,
    block_c: int = 128,
    *,
    dispatcher_hint: str | None = None,
):
    _set_route("fallback", "native-kernel-not-built")
    return _baseline.fuse_scale_shift_kernel(
        x, scale, shift, scale_constant=scale_constant, block_l=block_l, block_c=block_c
    )


def fuse_layernorm_scale_shift_gate_select01_kernel(
    x,
    weight,
    bias,
    scale0,
    shift0,
    gate0,
    scale1,
    shift1,
    gate1,
    index,
    eps,
    *,
    dispatcher_hint: str | None = None,
):
    _set_route("fallback", "native-kernel-not-built")
    return _baseline.fuse_layernorm_scale_shift_gate_select01_kernel(
        x, weight, bias, scale0, shift0, gate0, scale1, shift1, gate1, index, eps
    )


def fuse_residual_layernorm_scale_shift_gate_select01_kernel(
    x,
    residual,
    residual_gate,
    weight,
    bias,
    scale0,
    shift0,
    gate0,
    scale1,
    shift1,
    gate1,
    index,
    eps,
    *,
    dispatcher_hint: str | None = None,
):
    _set_route("fallback", "native-kernel-not-built")
    return _baseline.fuse_residual_layernorm_scale_shift_gate_select01_kernel(
        x, residual, residual_gate, weight, bias,
        scale0, shift0, gate0, scale1, shift1, gate1, index, eps,
    )


_OP_TO_FN = {
    OP_SCALE_SHIFT: fuse_scale_shift_kernel,
    OP_SELECT01: fuse_layernorm_scale_shift_gate_select01_kernel,
    OP_RESIDUAL: fuse_residual_layernorm_scale_shift_gate_select01_kernel,
}

# Most-specific first: a residual call cannot bind to the select01 signature
# (too many args) and vice versa (missing required args), and the 3-tensor
# elementwise call binds to neither of the larger signatures.
_BIND_ORDER = (OP_RESIDUAL, OP_SELECT01, OP_SCALE_SHIFT)

import inspect as _inspect  # noqa: E402

_OP_SIGNATURES = {op: _inspect.signature(fn) for op, fn in _OP_TO_FN.items()}


def _resolve_op(args, kwargs) -> str:
    """Identify which public entry point a generic call targets via signature binding."""
    for op in _BIND_ORDER:
        try:
            _OP_SIGNATURES[op].bind(*args, **kwargs)
            return op
        except TypeError:
            continue
    raise TypeError(
        "optimized_wrapper: arguments do not match any wrapped entry point "
        f"(args={len(args)}, kwargs={sorted(kwargs)})"
    )


def optimized_wrapper(*args, **kwargs):
    """Generic entry point per interface.md: routes to the matching public op."""
    return _OP_TO_FN[_resolve_op(args, kwargs)](*args, **kwargs)
