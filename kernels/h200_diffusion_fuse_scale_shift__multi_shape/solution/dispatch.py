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


def _resolve_op(args, kwargs) -> str:
    """Identify which public entry point a generic call targets."""
    if "residual" in kwargs or len(args) >= 12:
        return OP_RESIDUAL
    if "index" in kwargs or "scale0" in kwargs or len(args) >= 10:
        return OP_SELECT01
    return OP_SCALE_SHIFT


def optimized_wrapper(*args, **kwargs):
    """Generic entry point per interface.md: routes to the matching public op."""
    return _OP_TO_FN[_resolve_op(args, kwargs)](*args, **kwargs)
