"""Dispatch + build glue for the native-CUDA norm-scale-shift kernels.

Public callables preserve the exact SGLang signatures
(``fused_norm_scale_shift(x, weight, bias, scale, shift, norm_type, eps)`` and
``fused_scale_residual_norm_scale_shift(residual, x, gate, weight, bias, scale,
shift, norm_type, eps)``). Only verified captured-production operand patterns
take the native CUDA fast path; everything else falls back (fail-closed) to the
vendored SGLang baseline in ``baseline/`` — never to a live SGLang checkout.

Build/export goes through the snapshot's own jit_kernel / tvm-ffi stack
(``load_jit`` + ``make_cpp_args``-style template strings), compiling the
workspace-owned ``src/csrc/norm_scale_shift.cuh`` with SGLang-default flags
(no ``torch.utils.cpp_extension``, no ``--use_fast_math``). The source hash is
embedded in the jit module name so editing the kernel forces a rebuild.
"""

from __future__ import annotations

import hashlib
import importlib.util
import sys
from collections import Counter
from pathlib import Path
from typing import Optional

import torch

_THIS_DIR = Path(__file__).resolve().parent
_KERNEL_DIR = _THIS_DIR.parent
_CUH = _THIS_DIR / "csrc" / "norm_scale_shift.cuh"

# Tuning levers (benchmark/profile-driven; see docs/draft.md direction table).
USE_PDL = False          # validated separately; pilot evidence says default off
TWO_PASS_VARIANCE = False  # single-pass fused stats by default
VEC_BYTES = 32           # 256-bit vectors on Blackwell

_BF16 = torch.bfloat16
_FP32 = torch.float32


def _src_hash() -> str:
    return hashlib.sha1(_CUH.read_bytes()).hexdigest()[:12]


_SRC_HASH = _src_hash()


def _load_baseline_entry():
    name = "kda_baseline_entry"
    if name in sys.modules:
        return sys.modules[name]
    spec = importlib.util.spec_from_file_location(
        name, _KERNEL_DIR / "baseline" / "entry.py"
    )
    assert spec is not None and spec.loader is not None
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


_baseline = _load_baseline_entry()
# Install the snapshot alias NOW so any later `sglang.jit_kernel` import in this
# process (including our own load_jit build below) resolves to the pinned
# snapshot, never to an installed SGLang checkout.
_baseline.loader.install_baseline()
# Captured once at import so fallback never recurses after symbol swaps.
_BASELINE_NSS = _baseline.fused_norm_scale_shift
_BASELINE_SRNSS = _baseline.fused_scale_residual_norm_scale_shift

DISPATCH_STATS: Counter = Counter()


def dispatch_stats() -> Counter:
    return DISPATCH_STATS


# ---------------------------------------------------------------------------
# Operand classification (mirrors the baseline's broadcast normalization, but
# as zero-copy views + stride checks instead of expand()).
# ---------------------------------------------------------------------------

_ALIGN = 32  # bytes; AlignedVector chunk alignment requirement


def _aligned(t: torch.Tensor) -> bool:
    return t.data_ptr() % _ALIGN == 0


def _classify_operand(t: Optional[torch.Tensor], B: int, S: int, D: int):
    """Return (class_name, canonical_view) or None if not natively supported.

    Classes: "absent" (None), "scalar" ([1]), "row" ([D] broadcast across all
    rows), "token" ([B*S, D] per-row values). Per-batch (B>1) and 4-D frame
    layouts are not on the native path (fail-closed fallback).
    """
    if t is None:
        return "absent", None
    if not isinstance(t, torch.Tensor) or t.dtype not in (_BF16, _FP32):
        return None
    if t.ndim >= 1 and t.stride(-1) != 1:
        return None
    if t.ndim == 1:
        if t.numel() == 1:
            return ("scalar", t) if _aligned(t) else None
        if t.shape[0] == D:
            return ("row", t) if _aligned(t) else None
        return None
    if t.ndim == 2:
        if t.shape == (1, D):
            v = t.reshape(D)
            return ("row", v) if v.is_contiguous() and _aligned(v) else None
        return None
    if t.ndim == 3:
        s0, s1, s2 = t.shape
        if s2 != D or s0 != 1 or B != 1:
            return None
        if s1 == 1:
            v = t.reshape(D)
            return ("row", v) if v.is_contiguous() and _aligned(v) else None
        if s1 == S:
            if not t.is_contiguous():
                return None
            v = t.reshape(B * S, D)
            return ("token", v) if _aligned(v) else None
        return None
    return None  # 4-D frame mode and anything else -> baseline


def _activation_ok(t: torch.Tensor, D: int) -> bool:
    return (
        isinstance(t, torch.Tensor)
        and t.is_cuda
        and t.dtype == _BF16
        and t.ndim == 3
        and t.is_contiguous()
        and _aligned(t)
        and t.shape[-1] == D
    )


def _geometry_ok(D: int) -> bool:
    elems = VEC_BYTES // 2  # bf16 activations
    block = D // elems
    return (
        D % 256 == 0
        and D <= 8192
        and D % elems == 0
        and block % 32 == 0
        and 32 <= block <= 1024
    )


# ---------------------------------------------------------------------------
# JIT module (one compile, all production template combos exported)
# ---------------------------------------------------------------------------

_NS = "kda_norm_scale_shift"
_CLS = {"absent": 0, "scalar": 1, "row": 2, "token": 3}
_CPP_DT = {_BF16: "bf16_t", _FP32: "fp32_t"}


def _flags() -> str:
    tp = "true" if TWO_PASS_VARIANCE else "false"
    pdl = "true" if USE_PDL else "false"
    return f"false, {tp}, {pdl}, {VEC_BYTES}"  # kIsRms=false (layer-only v1)


def _wrapper_table():
    f = _flags()
    t = {}
    # (entry, sc_class, sc_dtype, gate_class, gate_dtype, has_wb) -> (export, symbol)
    for sc_class in ("row", "token"):
        for sc_dt in (_BF16, _FP32):
            name = f"nss_{sc_class}_{_CPP_DT[sc_dt][:-2]}"
            sym = (
                f"{_NS}::NormScaleShiftKernel<bf16_t, {_CPP_DT[sc_dt]}, "
                f"{_CLS[sc_class]}, {f}>::run"
            )
            t[("nss", sc_class, sc_dt, "absent", None, False)] = (name, sym)
    # srnss, no weight/bias
    t[("srnss", "row", _BF16, "row", _BF16, False)] = (
        "srnss_grow_bf16_row_bf16",
        f"{_NS}::ScaleResidualNormScaleShiftKernel<bf16_t, bf16_t, bf16_t, "
        f"{_CLS['row']}, {_CLS['row']}, {f}>::run",
    )
    for sc_class, sc_dt, export in (
        ("row", _BF16, "srnss_gnone_row_bf16"),
        ("row", _FP32, "srnss_gnone_row_fp32"),
        ("token", _FP32, "srnss_gnone_token_fp32"),
    ):
        t[("srnss", sc_class, sc_dt, "absent", None, False)] = (
            export,
            f"{_NS}::ScaleResidualNormScaleShiftKernel<bf16_t, bf16_t, "
            f"{_CPP_DT[sc_dt]}, {_CLS['absent']}, {_CLS[sc_class]}, {f}>::run_nogate",
        )
    # srnss with fp32 [D] weight/bias (wan family): scalar bf16 scale/shift
    for gate_class, export in (
        ("row", "srnss_grow_fp32_wb_scalar_bf16"),
        ("token", "srnss_gtoken_fp32_wb_scalar_bf16"),
    ):
        t[("srnss", "scalar", _BF16, gate_class, _FP32, True)] = (
            export,
            f"{_NS}::ScaleResidualNormScaleShiftAffineKernel<bf16_t, fp32_t, "
            f"fp32_t, bf16_t, {_CLS[gate_class]}, {_CLS['scalar']}, {f}>::run",
        )
    return t


_WRAPPERS = _wrapper_table()
_MOD = None


def _module():
    global _MOD
    if _MOD is None:
        from sglang.jit_kernel.utils import load_jit  # snapshot's build stack

        _MOD = load_jit(
            "kda_nss",
            _SRC_HASH,
            cuda_files=[str(_CUH)],
            cuda_wrappers=sorted(set(_WRAPPERS.values())),
            extra_include_paths=[str(_THIS_DIR / "csrc")],
        )
    return _MOD


def _native_fn(key):
    entry = _WRAPPERS.get(key)
    if entry is None:
        return None
    return getattr(_module(), entry[0])


def _fallback(reason: str):
    DISPATCH_STATS["fallback"] += 1
    DISPATCH_STATS[f"fallback:{reason}"] += 1


# ---------------------------------------------------------------------------
# Public callables (exact SGLang signatures)
# ---------------------------------------------------------------------------


def fused_norm_scale_shift(x, weight, bias, scale, shift, norm_type, eps=1e-5):
    if not (
        isinstance(x, torch.Tensor)
        and x.is_cuda
        and x.ndim == 3
        and norm_type == "layer"
        and weight is None
        and bias is None
    ):
        _fallback("nss:contract")
        return _BASELINE_NSS(x, weight, bias, scale, shift, norm_type, eps)
    B, S, D = x.shape
    if not (_activation_ok(x, D) and _geometry_ok(D)):
        _fallback("nss:activation")
        return _BASELINE_NSS(x, weight, bias, scale, shift, norm_type, eps)
    sc = _classify_operand(scale, B, S, D)
    sh = _classify_operand(shift, B, S, D)
    if (
        sc is None
        or sh is None
        or sc[0] != sh[0]
        or sc[0] not in ("row", "token")
        or scale.dtype != shift.dtype
    ):
        _fallback("nss:operand")
        return _BASELINE_NSS(x, weight, bias, scale, shift, norm_type, eps)
    fn = _native_fn(("nss", sc[0], scale.dtype, "absent", None, False))
    if fn is None:
        _fallback("nss:combo")
        return _BASELINE_NSS(x, weight, bias, scale, shift, norm_type, eps)
    DISPATCH_STATS["native"] += 1
    y = torch.empty_like(x)
    fn(y.view(B * S, D), x.view(B * S, D), sc[1], sh[1], float(eps))
    return y


def fused_scale_residual_norm_scale_shift(
    residual, x, gate, weight, bias, scale, shift, norm_type, eps=1e-5
):
    if not (
        isinstance(x, torch.Tensor)
        and isinstance(residual, torch.Tensor)
        and x.is_cuda
        and x.ndim == 3
        and norm_type == "layer"
        and residual.shape == x.shape
        and residual.dtype == x.dtype
    ):
        _fallback("srnss:contract")
        return _BASELINE_SRNSS(
            residual, x, gate, weight, bias, scale, shift, norm_type, eps
        )
    B, S, D = x.shape
    if not (
        _activation_ok(x, D)
        and _activation_ok(residual, D)
        and _geometry_ok(D)
    ):
        _fallback("srnss:activation")
        return _BASELINE_SRNSS(
            residual, x, gate, weight, bias, scale, shift, norm_type, eps
        )

    has_wb = weight is not None or bias is not None
    if has_wb:
        wb_ok = (
            isinstance(weight, torch.Tensor)
            and isinstance(bias, torch.Tensor)
            and weight.dtype == _FP32
            and bias.dtype == _FP32
            and weight.shape == (D,)
            and bias.shape == (D,)
            and weight.is_contiguous()
            and bias.is_contiguous()
            and _aligned(weight)
            and _aligned(bias)
        )
        if not wb_ok:
            _fallback("srnss:weight_bias")
            return _BASELINE_SRNSS(
                residual, x, gate, weight, bias, scale, shift, norm_type, eps
            )

    g = _classify_operand(gate, B, S, D)
    sc = _classify_operand(scale, B, S, D)
    sh = _classify_operand(shift, B, S, D)
    if (
        g is None
        or sc is None
        or sh is None
        or sc[0] != sh[0]
        or (scale is not None and shift is not None and scale.dtype != shift.dtype)
    ):
        _fallback("srnss:operand")
        return _BASELINE_SRNSS(
            residual, x, gate, weight, bias, scale, shift, norm_type, eps
        )
    gate_dtype = gate.dtype if isinstance(gate, torch.Tensor) else None
    key = ("srnss", sc[0], scale.dtype, g[0], gate_dtype, has_wb)
    fn = _native_fn(key)
    if fn is None:
        _fallback("srnss:combo")
        return _BASELINE_SRNSS(
            residual, x, gate, weight, bias, scale, shift, norm_type, eps
        )
    DISPATCH_STATS["native"] += 1
    y = torch.empty_like(x)
    res_out = torch.empty_like(x)
    y2, ro2 = y.view(B * S, D), res_out.view(B * S, D)
    r2, x2 = residual.view(B * S, D), x.view(B * S, D)
    e = float(eps)
    if has_wb:
        fn(y2, ro2, r2, x2, g[1], weight, bias, sc[1], sh[1], e)
    elif g[0] == "absent":
        fn(y2, ro2, r2, x2, sc[1], sh[1], e)
    else:
        fn(y2, ro2, r2, x2, g[1], sc[1], sh[1], e)
    return y, res_out
