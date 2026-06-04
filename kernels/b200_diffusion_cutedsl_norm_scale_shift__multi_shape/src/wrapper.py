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
from typing import Optional, Tuple

import torch

_THIS_DIR = Path(__file__).resolve().parent
_KERNEL_DIR = _THIS_DIR.parent
_CUH = _THIS_DIR / "csrc" / "norm_scale_shift.cuh"

# Tuning levers (benchmark/profile-driven; see docs/draft.md direction table).
USE_PDL = False          # validated separately; pilot evidence says default off
# Layer-norm statistics algorithm. True = two-pass mean-then-variance (the
# baseline's exact, contract-mandated form) — SHIPPED CONFIG. False = the
# single-round Welford/Chan merge: numerically robust, but benchmark run
# r2-v3 measured it SLOWER than two-pass (geomean 1.16x vs 1.31x; the 3-float
# merge with a division in the dependent shuffle chain outweighs the saved
# reduction round), so it stays available only as a documented rejected lever.
TWO_PASS_VARIANCE = True
# Per-combo vector width (bytes of activation data per thread):
# - bf16-only operand combos: 32B (16 elems/thread, block = D/16);
# - combos with any fp32 operand stream (per-token/broadcast scale/shift,
#   fp32 gate, fp32 weight/bias): 16B (8 elems/thread, block = D/8). NCU round
#   r0v1 showed fp32 streams at 16 elems/thread cost 52 regs -> 41% occupancy
#   and long_scoreboard 16% (vs CuTe baseline 82% occ); halving the per-thread
#   footprint restores latency hiding.
VEC_BYTES_BF16 = 32
VEC_BYTES_FP32_OPERANDS = 16

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


def _classify_operand(
    t: Optional[torch.Tensor], B: int, S: int, D: int, device: torch.device
):
    """Return (class_name, canonical_view) or None if not natively supported.

    Classes: "absent" (None), "scalar" ([1]), "row" ([D] broadcast across all
    rows), "token" ([B*S, D] per-row values). Per-batch (B>1) and 4-D frame
    layouts are not on the native path (fail-closed fallback).
    """
    if t is None:
        return "absent", None
    if not isinstance(t, torch.Tensor) or t.dtype not in (_BF16, _FP32):
        return None
    if not t.is_cuda or t.device != device:
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
        and t.numel() > 0
        and t.is_contiguous()
        and _aligned(t)
        and t.shape[-1] == D
    )


def _geometry_ok(D: int, vec_bytes: int) -> bool:
    elems = vec_bytes // 2  # bf16 activations
    block = D // elems if D % elems == 0 else 0
    return (
        D % 256 == 0
        and D <= 8192
        and block % 32 == 0
        and 32 <= block <= 1024
    )


# ---------------------------------------------------------------------------
# JIT module (one compile, all production template combos exported)
# ---------------------------------------------------------------------------

_NS = "kda_norm_scale_shift"
_CLS = {"absent": 0, "scalar": 1, "row": 2, "token": 3}
_CPP_DT = {_BF16: "bf16_t", _FP32: "fp32_t"}


def _combo_vec_bytes(sc_dtype, gate_dtype, has_wb) -> int:
    """Any fp32 operand stream halves the per-thread footprint (see above)."""
    if sc_dtype == _FP32 or gate_dtype == _FP32 or has_wb:
        return VEC_BYTES_FP32_OPERANDS
    return VEC_BYTES_BF16


def _flags(vec_bytes: int) -> str:
    tp = "true" if TWO_PASS_VARIANCE else "false"
    pdl = "true" if USE_PDL else "false"
    return f"false, {tp}, {pdl}, {vec_bytes}"  # kIsRms=false (layer-only v1)


def _wrapper_table():
    t = {}

    def flags(key):
        return _flags(_combo_vec_bytes(key[2], key[4], key[5]))

    # (entry, sc_class, sc_dtype, gate_class, gate_dtype, has_wb) -> (export, symbol)
    for sc_class in ("row", "token"):
        for sc_dt in (_BF16, _FP32):
            key = ("nss", sc_class, sc_dt, "absent", None, False)
            name = f"nss_{sc_class}_{_CPP_DT[sc_dt][:-2]}"
            sym = (
                f"{_NS}::NormScaleShiftKernel<bf16_t, {_CPP_DT[sc_dt]}, "
                f"{_CLS[sc_class]}, {flags(key)}>::run"
            )
            t[key] = (name, sym)
    # srnss, no weight/bias
    key = ("srnss", "row", _BF16, "row", _BF16, False)
    t[key] = (
        "srnss_grow_bf16_row_bf16",
        f"{_NS}::ScaleResidualNormScaleShiftKernel<bf16_t, bf16_t, bf16_t, "
        f"{_CLS['row']}, {_CLS['row']}, {flags(key)}>::run",
    )
    for sc_class, sc_dt, export in (
        ("row", _BF16, "srnss_gnone_row_bf16"),
        ("row", _FP32, "srnss_gnone_row_fp32"),
        ("token", _FP32, "srnss_gnone_token_fp32"),
    ):
        key = ("srnss", sc_class, sc_dt, "absent", None, False)
        t[key] = (
            export,
            f"{_NS}::ScaleResidualNormScaleShiftKernel<bf16_t, bf16_t, "
            f"{_CPP_DT[sc_dt]}, {_CLS['absent']}, {_CLS[sc_class]}, {flags(key)}>::run_nogate",
        )
    # srnss with fp32 [D] weight/bias (wan family): scalar bf16 scale/shift
    for gate_class, export in (
        ("row", "srnss_grow_fp32_wb_scalar_bf16"),
        ("token", "srnss_gtoken_fp32_wb_scalar_bf16"),
    ):
        key = ("srnss", "scalar", _BF16, gate_class, _FP32, True)
        t[key] = (
            export,
            f"{_NS}::ScaleResidualNormScaleShiftAffineKernel<bf16_t, fp32_t, "
            f"fp32_t, bf16_t, {_CLS[gate_class]}, {_CLS['scalar']}, {flags(key)}>::run",
        )
    return t


_WRAPPERS = _wrapper_table()
_MOD = None


def _module():
    global _MOD
    if _MOD is None:
        import os

        from sglang.jit_kernel.utils import load_jit  # snapshot's build stack

        # Profiling-only hook (e.g. KDA_EXTRA_CUDA_CFLAGS=-lineinfo for ncu
        # SASS->source mapping). Shipped builds never set it; the module name
        # encodes the extra flags so profiling builds cannot shadow clean ones.
        extra = os.environ.get("KDA_EXTRA_CUDA_CFLAGS", "").split()
        tag = f"x{abs(hash(tuple(extra))) % 10**8}" if extra else "clean"
        _MOD = load_jit(
            "kda_nss",
            _SRC_HASH,
            tag,
            cuda_files=[str(_CUH)],
            cuda_wrappers=sorted(set(_WRAPPERS.values())),
            extra_cuda_cflags=extra,
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
    if not _activation_ok(x, D):
        _fallback("nss:activation")
        return _BASELINE_NSS(x, weight, bias, scale, shift, norm_type, eps)
    if not (isinstance(scale, torch.Tensor) and isinstance(shift, torch.Tensor)):
        _fallback("nss:operand")  # baseline raises its own validation error
        return _BASELINE_NSS(x, weight, bias, scale, shift, norm_type, eps)
    sc = _classify_operand(scale, B, S, D, x.device)
    sh = _classify_operand(shift, B, S, D, x.device)
    if (
        sc is None
        or sh is None
        or sc[0] != sh[0]
        or sc[0] not in ("row", "token")
        or scale.dtype != shift.dtype
    ):
        _fallback("nss:operand")
        return _BASELINE_NSS(x, weight, bias, scale, shift, norm_type, eps)
    key = ("nss", sc[0], scale.dtype, "absent", None, False)
    if not _geometry_ok(D, _combo_vec_bytes(scale.dtype, None, False)):
        _fallback("nss:geometry")
        return _BASELINE_NSS(x, weight, bias, scale, shift, norm_type, eps)
    fn = _native_fn(key)
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
    if not (_activation_ok(x, D) and _activation_ok(residual, D)):
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
        if not (weight.is_cuda and weight.device == x.device and bias.device == x.device):
            _fallback("srnss:weight_bias")
            return _BASELINE_SRNSS(
                residual, x, gate, weight, bias, scale, shift, norm_type, eps
            )

    if not (isinstance(scale, torch.Tensor) and isinstance(shift, torch.Tensor)):
        _fallback("srnss:operand")  # baseline raises its own validation error
        return _BASELINE_SRNSS(
            residual, x, gate, weight, bias, scale, shift, norm_type, eps
        )
    g = _classify_operand(gate, B, S, D, x.device)
    sc = _classify_operand(scale, B, S, D, x.device)
    sh = _classify_operand(shift, B, S, D, x.device)
    if (
        g is None
        or sc is None
        or sh is None
        or sc[0] != sh[0]
        or scale.dtype != shift.dtype
    ):
        _fallback("srnss:operand")
        return _BASELINE_SRNSS(
            residual, x, gate, weight, bias, scale, shift, norm_type, eps
        )
    gate_dtype = gate.dtype if isinstance(gate, torch.Tensor) else None
    key = ("srnss", sc[0], scale.dtype, g[0], gate_dtype, has_wb)
    if not _geometry_ok(D, _combo_vec_bytes(scale.dtype, gate_dtype, has_wb)):
        _fallback("srnss:geometry")
        return _BASELINE_SRNSS(
            residual, x, gate, weight, bias, scale, shift, norm_type, eps
        )
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


# ---------------------------------------------------------------------------
# Shipping-shaped entry points: the same callables wrapped in a
# `torch.library.custom_op` layer mirroring the SGLang baseline registration
# (`mutates_args=()` + `register_fake`). The in-tree export keeps SGLang's own
# registration; this local layer exists so benchmarks compare candidate and
# baseline through IDENTICAL host stacks (custom-op dispatch on both sides).
# ---------------------------------------------------------------------------

_SHIPPING_OPS = None


def shipping_entry_points():
    """Return (nss_op, srnss_op) wrapped as registered torch custom ops."""
    global _SHIPPING_OPS
    if _SHIPPING_OPS is None:
        # NOTE: this module uses `from __future__ import annotations`, so
        # torch.library's schema inference sees the annotation STRINGS — they
        # must be spelled exactly as `Optional[...]`/`Tuple[...]` (resolvable
        # names), mirroring the baseline's own custom-op signatures.

        @torch.library.custom_op("kda_nss::fused_norm_scale_shift", mutates_args=())
        def _nss_op(
            x: torch.Tensor,
            weight: Optional[torch.Tensor],
            bias: Optional[torch.Tensor],
            scale: torch.Tensor,
            shift: torch.Tensor,
            norm_type: str,
            eps: float = 1e-5,
        ) -> torch.Tensor:
            return fused_norm_scale_shift(x, weight, bias, scale, shift, norm_type, eps)

        @_nss_op.register_fake
        def _nss_fake(x, weight, bias, scale, shift, norm_type, eps=1e-5):
            return x.new_empty(x.shape)

        @torch.library.custom_op(
            "kda_nss::fused_scale_residual_norm_scale_shift", mutates_args=()
        )
        def _srnss_op(
            residual: torch.Tensor,
            x: torch.Tensor,
            gate: Optional[torch.Tensor],
            weight: Optional[torch.Tensor],
            bias: Optional[torch.Tensor],
            scale: torch.Tensor,
            shift: torch.Tensor,
            norm_type: str,
            eps: float = 1e-5,
        ) -> Tuple[torch.Tensor, torch.Tensor]:
            return fused_scale_residual_norm_scale_shift(
                residual, x, gate, weight, bias, scale, shift, norm_type, eps
            )

        @_srnss_op.register_fake
        def _srnss_fake(residual, x, gate, weight, bias, scale, shift, norm_type, eps=1e-5):
            return x.new_empty(x.shape), x.new_empty(x.shape)

        _SHIPPING_OPS = (_nss_op, _srnss_op)
    return _SHIPPING_OPS
