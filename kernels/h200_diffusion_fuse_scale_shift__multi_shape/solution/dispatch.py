"""Deterministic dispatcher for the fused scale-shift kernel family.

Routes each public call to a native CUDA variant when the signature is
in-contract for one, otherwise to the vendored Triton baseline (baseline/).
The route taken by the most recent call is observable via consume_last_route()
so the harnesses can assert routing behavior.

Gate design: a few cheap per-call checks (kept lean — heavy per-call gates
have previously erased launch-bound wins); any gate exception degrades to
fallback so out-of-contract inputs hit the baseline's own error behavior.

Env switches: KDA_NATIVE=0 forces fallback-only; KDA_PDL=1 builds/launches
with programmatic dependent launch (off by default; validate before keeping).
"""

from __future__ import annotations

import os
import sys
from pathlib import Path

import torch

_KERNEL_DIR = Path(__file__).resolve().parents[1]
if str(_KERNEL_DIR) not in sys.path:
    sys.path.insert(0, str(_KERNEL_DIR))

from baseline import scale_shift as _baseline  # noqa: E402

OP_SCALE_SHIFT = "scale_shift"
OP_SELECT01 = "select01"
OP_RESIDUAL = "residual_select01"

_NATIVE_ENABLED = os.environ.get("KDA_NATIVE", "1") == "1"
_USE_PDL = os.environ.get("KDA_PDL", "0") == "1"

_FLOAT_DTYPES = (torch.bfloat16, torch.float16, torch.float32)
_MAX_GRID_Y = 65535
_LN_THREADS = 256
_LN_MAX_ITER = 4

# Production buckets the dispatcher intentionally routes to the baseline for
# performance (recorded honestly as fallback, counted 1.0x). Filled only by
# benchmark-evidence decisions; format: {op: {bucket_key, ...}}.
PERF_FALLBACK: dict[str, set] = {OP_SCALE_SHIFT: set(), OP_SELECT01: set(), OP_RESIDUAL: set()}

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
    return {
        OP_SCALE_SHIFT: _NATIVE_ENABLED,
        OP_SELECT01: _NATIVE_ENABLED,
        OP_RESIDUAL: _NATIVE_ENABLED,
    }


def _vec_elems(dtype: torch.dtype) -> int:
    return 16 // (4 if dtype == torch.float32 else 2)


def _aligned16(*values: int) -> bool:
    return all(v % 16 == 0 for v in values)


# ---------------------------------------------------------------------------
# Family A: fuse_scale_shift_kernel
# ---------------------------------------------------------------------------

def _classify_operand(t: torch.Tensor, B: int, L: int, C: int):
    """Mirror the baseline wrapper's broadcast resolution for scale/shift.

    Returns (kind, view) where kind is "splat" (1-element) or "strided"
    ((B, L, C) expand view with c-stride 1), or None if unsupported natively.
    """
    if t.dim() == 0 or (t.dim() == 1 and t.numel() == 1):
        return "splat", t.reshape(1)
    if t.dim() == 2:
        blc = t[:, None, :]
    elif t.dim() == 3:
        blc = t
    else:
        return None
    try:
        view = blc.expand(B, L, C)
    except RuntimeError:
        return None
    sb, sl, sc = view.stride()
    esize = t.element_size()
    if sc != 1:
        return None
    if not _aligned16(t.data_ptr(), sb * esize, sl * esize):
        return None
    return "strided", view


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
    if not _NATIVE_ENABLED or dispatcher_hint == "fallback":
        _set_route("fallback", "native-disabled")
        return _baseline.fuse_scale_shift_kernel(
            x, scale, shift, scale_constant=scale_constant, block_l=block_l, block_c=block_c
        )
    try:
        plan = _plan_scale_shift(x, scale, shift)
    except Exception:  # noqa: BLE001 - any gate surprise degrades to fallback
        plan = None
    if plan is None:
        _set_route("fallback", "out-of-contract")
        return _baseline.fuse_scale_shift_kernel(
            x, scale, shift, scale_constant=scale_constant, block_l=block_l, block_c=block_c
        )

    kind, detail = plan
    if kind == "both-splat":
        # Mirror the baseline wrapper exactly, including its early-copy when
        # both scalars are zero (that path short-circuits scale_constant).
        scale_view, shift_view = detail
        output = torch.empty_like(x)
        if x.numel() == 0:
            _set_route("native", "empty")
            return output
        if not (
            scale_view.any().to("cpu", non_blocking=True)
            or shift_view.any().to("cpu", non_blocking=True)
        ):
            _set_route("native", "both-splat-zero-copy")
            output.copy_(x)
            return output
        from solution import jit_build

        module = jit_build.scale_shift_module(
            x.dtype, scale_view.dtype, shift_view.dtype, True, True, False, _USE_PDL
        )
        module.fuse_scale_shift(x, scale_view, shift_view, output, float(scale_constant), 0)
        _set_route("native", "elementwise:both-splat")
        return output

    scale_kind, scale_view, shift_kind, shift_view, num_frames, variant = detail
    output = torch.empty_like(x)
    if x.numel() == 0:
        _set_route("native", "empty")
        return output
    from solution import jit_build

    module = jit_build.scale_shift_module(
        x.dtype,
        scale_view.dtype,
        shift_view.dtype,
        scale_kind == "splat",
        shift_kind == "splat",
        scale_kind == "frame",
        _USE_PDL,
    )
    module.fuse_scale_shift(x, scale_view, shift_view, output, float(scale_constant), num_frames)
    _set_route("native", variant)
    return output


def _plan_scale_shift(x, scale, shift):
    """Return a launch plan or None (fallback)."""
    if not (x.is_cuda and x.dim() == 3 and x.is_contiguous()):
        return None
    if x.dtype not in _FLOAT_DTYPES:
        return None
    if scale.dtype not in _FLOAT_DTYPES or shift.dtype not in _FLOAT_DTYPES:
        return None
    # The 16-byte packet loader converts whole scale/shift packets per x
    # packet, which requires the modulation dtype to be at least as wide as
    # the x dtype (e.g. fp32 x with bf16 scale would need a fractional packet).
    if (scale.element_size() < x.element_size()
            or shift.element_size() < x.element_size()):
        return None
    if not (scale.is_cuda and shift.is_cuda):
        return None
    B, L, C = x.shape
    if B * L > _MAX_GRID_Y:
        return None
    if C % _vec_elems(x.dtype) != 0 or C == 0:
        return None
    if not _aligned16(x.data_ptr()):
        return None

    if scale.dim() == 4:
        # Per-frame scale (B, F, 1, C); shift must be per-token reshapeable.
        if scale.shape[0] != B or scale.shape[2] != 1 or scale.shape[3] != C:
            return None
        F = scale.shape[1]
        if F <= 0 or L % F != 0 or not scale.is_contiguous():
            return None
        if shift.numel() != B * L * C or shift.dim() not in (3, 4):
            return None
        shift_blc = shift.reshape(B, L, C)
        sh = _classify_operand(shift_blc, B, L, C)
        if sh is None or sh[0] != "strided":
            return None
        scale_2d = scale.reshape(B * F, C)
        if not _aligned16(scale_2d.data_ptr()):
            return None
        return "mixed", ("frame", scale_2d, "strided", sh[1], F, "elementwise:frame4d")

    s = _classify_operand(scale, B, L, C)
    h = _classify_operand(shift, B, L, C)
    if s is None or h is None:
        return None
    if s[0] == "splat" and h[0] == "splat":
        return "both-splat", (s[1], h[1])
    variant = f"elementwise:{s[0][0]}{h[0][0]}"  # ss/sh combinations
    return "mixed", (s[0], s[1], h[0], h[1], 0, variant)


# ---------------------------------------------------------------------------
# Family B: LayerNorm + select01 (+ residual)
# ---------------------------------------------------------------------------

def _plan_select01(x, weight, bias, mods, index, residual=None, residual_gate=None):
    if not (x.is_cuda and x.dim() == 3 and x.is_contiguous()):
        return None
    if x.dtype not in _FLOAT_DTYPES:
        return None
    B, L, C = x.shape
    vec = _vec_elems(x.dtype)
    if C % vec != 0 or C == 0 or C > _LN_THREADS * vec * _LN_MAX_ITER:
        return None
    if B * L == 0:
        return None
    if not _aligned16(x.data_ptr()):
        return None

    mod_stride = None
    for t in mods:
        if not (t.is_cuda and t.dim() == 2 and t.shape[0] == B and t.shape[1] == C):
            return None
        if t.dtype != x.dtype or t.stride(1) != 1:
            return None
        if mod_stride is None:
            mod_stride = t.stride(0)
        elif t.stride(0) != mod_stride:
            return None
        if not _aligned16(t.data_ptr(), t.stride(0) * t.element_size()):
            return None

    for t in (weight, bias):
        if t is None:
            continue
        if not (t.is_cuda and t.dim() == 1 and t.shape[0] == C and t.dtype == x.dtype
                and t.is_contiguous() and _aligned16(t.data_ptr())):
            return None

    if not (index.is_cuda and index.dim() == 2 and index.shape[0] == B and index.shape[1] == L):
        return None
    if index.dtype == torch.bool:
        index = index.to(torch.int32)  # tiny cast; preserves the !=0 selection
    if index.dtype not in (torch.int32, torch.int64):
        return None

    if residual is not None:
        for t in (residual, residual_gate):
            if not (t.is_cuda and t.shape == x.shape and t.dtype == x.dtype
                    and t.is_contiguous() and _aligned16(t.data_ptr())):
                return None
    return index


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
    mods = (scale0, shift0, gate0, scale1, shift1, gate1)
    if _NATIVE_ENABLED and dispatcher_hint != "fallback":
        try:
            idx = _plan_select01(x, weight, bias, mods, index)
        except Exception:  # noqa: BLE001
            idx = None
        if idx is not None:
            from solution import jit_build

            out = torch.empty_like(x)
            gate_out = torch.empty_like(x)
            module = jit_build.ln_select01_module(
                x.dtype, weight is not None, bias is not None, False, _USE_PDL
            )
            sent = x  # sentinel for absent optional tensors (never read)
            module.fuse_ln_select01(
                x, sent, sent,
                weight if weight is not None else sent,
                bias if bias is not None else sent,
                scale0, shift0, gate0, scale1, shift1, gate1,
                idx, out, sent, gate_out, float(eps),
            )
            _set_route("native", "ln_select01")
            return out, gate_out
    _set_route("fallback", "out-of-contract" if _NATIVE_ENABLED else "native-disabled")
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
    mods = (scale0, shift0, gate0, scale1, shift1, gate1)
    if _NATIVE_ENABLED and dispatcher_hint != "fallback":
        try:
            idx = _plan_select01(x, weight, bias, mods, index, residual, residual_gate)
        except Exception:  # noqa: BLE001
            idx = None
        if idx is not None:
            from solution import jit_build

            out = torch.empty_like(x)
            residual_out = torch.empty_like(x)
            gate_out = torch.empty_like(x)
            module = jit_build.ln_select01_module(
                x.dtype, weight is not None, bias is not None, True, _USE_PDL
            )
            sent = x
            module.fuse_ln_select01(
                x, residual, residual_gate,
                weight if weight is not None else sent,
                bias if bias is not None else sent,
                scale0, shift0, gate0, scale1, shift1, gate1,
                idx, out, residual_out, gate_out, float(eps),
            )
            _set_route("native", "ln_select01_residual")
            return out, residual_out, gate_out
    _set_route("fallback", "out-of-contract" if _NATIVE_ENABLED else "native-disabled")
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
