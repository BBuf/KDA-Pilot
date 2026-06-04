"""Native CUDA fast path for the fused scale-shift / select01 modulation kernels.

Ships as python/sglang/jit_kernel/diffusion/scale_shift_kda.py with the device
code at python/sglang/jit_kernel/csrc/diffusion/scale_shift_kda.cuh. The public
entry points in triton/scale_shift.py call try_native_*() first and keep their
original Triton bodies as the fallback, so callable names, module paths, and
the CustomOp/torch.compile registrations above them stay unchanged.

try_native_*() returns the result tensor(s) when the signature is in-contract
for the CUDA kernels, or None to let the caller's original path run. Any gate
exception also degrades to None, preserving the baseline's error behavior.

Toggle: SGLANG_SCALE_SHIFT_KDA=0 disables the native path (module attribute
ENABLED is also flippable at runtime for A/B benchmarking).
"""

from __future__ import annotations

import os

import torch

from sglang.jit_kernel.utils import cache_once, load_jit, make_cpp_args

ENABLED = os.environ.get("SGLANG_SCALE_SHIFT_KDA", "1") == "1"
_USE_PDL = os.environ.get("SGLANG_SCALE_SHIFT_KDA_PDL", "0") == "1"

_FLOAT_DTYPES = (torch.bfloat16, torch.float16, torch.float32)
_MAX_GRID_Y = 65535
_LN_THREADS = 256
_LN_MAX_ITER = 4


@cache_once
def _scale_shift_module(dtype_x, dtype_scale, dtype_shift, scale_splat: bool,
                        shift_splat: bool, frame_mode: bool, use_pdl: bool):
    args = make_cpp_args(dtype_x, dtype_scale, dtype_shift, scale_splat,
                         shift_splat, frame_mode, use_pdl)
    return load_jit(
        "scale_shift_kda",
        *args,
        cuda_files=["diffusion/scale_shift_kda.cuh"],
        cuda_wrappers=[("fuse_scale_shift", f"FuseScaleShiftKernel<{args}>::run")],
    )


@cache_once
def _ln_select01_module(dtype_x, has_weight: bool, has_bias: bool,
                        has_residual: bool, use_pdl: bool):
    args = make_cpp_args(dtype_x, has_weight, has_bias, has_residual, use_pdl)
    return load_jit(
        "ln_select01_kda",
        *args,
        cuda_files=["diffusion/scale_shift_kda.cuh"],
        cuda_wrappers=[("fuse_ln_select01", f"FuseLNSelect01Kernel<{args}>::run")],
    )


def _vec_elems(dtype: torch.dtype) -> int:
    return 16 // (4 if dtype == torch.float32 else 2)


def _aligned16(*values: int) -> bool:
    return all(v % 16 == 0 for v in values)


def _classify_operand(t: torch.Tensor, B: int, L: int, C: int):
    """Mirror the Triton wrapper's broadcast resolution for scale/shift."""
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


def _plan_scale_shift(x, scale, shift):
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
        return ("frame", scale_2d, "strided", sh[1], F)

    s = _classify_operand(scale, B, L, C)
    h = _classify_operand(shift, B, L, C)
    if s is None or h is None:
        return None
    if s[0] == "splat" and h[0] == "splat":
        # The original wrapper has a dedicated both-scalar path (including a
        # zero-check copy short-circuit); keep that behavior by declining.
        return None
    return (s[0], s[1], h[0], h[1], 0)


def try_native_fuse_scale_shift(x, scale, shift, scale_constant=1.0):
    if not ENABLED:
        return None
    try:
        plan = _plan_scale_shift(x, scale, shift)
    except Exception:  # noqa: BLE001 - gate surprises fall back to Triton
        plan = None
    if plan is None:
        return None
    scale_kind, scale_view, shift_kind, shift_view, num_frames = plan
    output = torch.empty_like(x)
    if x.numel() == 0:
        return output
    module = _scale_shift_module(
        x.dtype, scale_view.dtype, shift_view.dtype,
        scale_kind == "splat", shift_kind == "splat", scale_kind == "frame",
        _USE_PDL,
    )
    module.fuse_scale_shift(x, scale_view, shift_view, output,
                            float(scale_constant), num_frames)
    return output


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

    if not (index.is_cuda and index.dim() == 2 and index.shape[0] == B
            and index.shape[1] == L):
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


def try_native_layernorm_select01(x, weight, bias, scale0, shift0, gate0,
                                  scale1, shift1, gate1, index, eps):
    if not ENABLED:
        return None
    mods = (scale0, shift0, gate0, scale1, shift1, gate1)
    try:
        idx = _plan_select01(x, weight, bias, mods, index)
    except Exception:  # noqa: BLE001
        idx = None
    if idx is None:
        return None
    out = torch.empty_like(x)
    gate_out = torch.empty_like(x)
    module = _ln_select01_module(
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
    return out, gate_out


def try_native_residual_layernorm_select01(x, residual, residual_gate, weight,
                                           bias, scale0, shift0, gate0, scale1,
                                           shift1, gate1, index, eps):
    if not ENABLED:
        return None
    mods = (scale0, shift0, gate0, scale1, shift1, gate1)
    try:
        idx = _plan_select01(x, weight, bias, mods, index, residual, residual_gate)
    except Exception:  # noqa: BLE001
        idx = None
    if idx is None:
        return None
    out = torch.empty_like(x)
    residual_out = torch.empty_like(x)
    gate_out = torch.empty_like(x)
    module = _ln_select01_module(
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
    return out, residual_out, gate_out
