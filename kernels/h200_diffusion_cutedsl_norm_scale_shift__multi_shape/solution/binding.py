"""Dispatch + build glue for the native-CUDA norm-scale-shift kernels (H200).

Public callables are ``torch.library.custom_op``s in the ``kda_nss::``
namespace with the exact SGLang signatures, mirroring the vendored baseline's
own custom-op registration so the benchmark compares identical host stacks
(custom-op dispatch + internal output allocation on both sides).

Only verified captured-production operand patterns take the native CUDA fast
path; everything else falls back (fail-closed) to the vendored SGLang baseline
in ``baseline/`` — never to a live SGLang checkout.

Build goes through the snapshot's own jit_kernel / tvm-ffi stack
(``load_jit``), compiling the workspace-owned ``solution/csrc/norm_scale_shift.cuh``
with SGLang-default flags (no ``--use_fast_math``); the source hash is embedded
in the jit module name so editing the kernel forces a rebuild.

Per-thread vector width is a per-combo dispatch choice. Hopper default is
16 bytes (one 128-bit transaction per thread; promoted H200 siblings favored
128-bit and Hopper has no wider load). bf16-only combos are also instantiated
at 32 bytes (two 128-bit transactions, halves the block size) and can be
selected with ``KDA_VEC_BYTES_BF16=32`` for measured sweeps; combos with any
fp32 operand stream stay at 16 bytes (B200 evidence: wider footprint collapses
occupancy on fat operand streams).
"""

import hashlib
import importlib.util
import os
import sys
from collections import Counter
from pathlib import Path
from typing import Optional, Tuple

import torch

_THIS_DIR = Path(__file__).resolve().parent
_TASK_DIR = _THIS_DIR.parent
_CUH = _THIS_DIR / "csrc" / "norm_scale_shift.cuh"

# Tuning levers (benchmark/profile-driven on H200; see docs/dispatch.md).
USE_PDL = False           # upstream baseline has no comparable PDL path
TWO_PASS_VARIANCE = True  # baseline's contract-exact layer statistics
VEC_BYTES_BF16 = int(os.environ.get("KDA_VEC_BYTES_BF16", "16"))
VEC_BYTES_FP32_OPERANDS = 16
assert VEC_BYTES_BF16 in (16, 32), "bf16 vector width must be 16 or 32 bytes"
# Early-issue the scale/shift global loads before the statistics reductions
# (raw storage-dtype registers, expanded at the epilogue). NCU r1 on the
# fp32-row bucket showed nvcc sinks these loads to the epilogue, exposing their
# latency after both reduction barriers (short_scoreboard 2.4x the CuTe
# baseline at identical geometry/regs/bytes). A zero-register
# prefetch.global.L1 variant was measured and rejected (LSU flood, 620us vs
# 381us). Applies to row/token scale/shift combos only.
EARLY_SCALE_SHIFT = os.environ.get("KDA_EARLY_OPS", "0") == "1"

_BF16 = torch.bfloat16
_FP32 = torch.float32


def _src_hash() -> str:
    return hashlib.sha1(_CUH.read_bytes()).hexdigest()[:12]


_SRC_HASH = _src_hash()


def _load_baseline_binding():
    name = "kda_baseline_binding"
    if name in sys.modules:
        return sys.modules[name]
    spec = importlib.util.spec_from_file_location(name, _TASK_DIR / "baseline" / "binding.py")
    assert spec is not None and spec.loader is not None
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


_baseline = _load_baseline_binding()
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

_ALIGN = 32  # bytes; covers both vector-width configurations


def _aligned(t: torch.Tensor) -> bool:
    return t.data_ptr() % _ALIGN == 0


def _classify_operand(t, B: int, S: int, D: int, device: torch.device):
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
    elems = vec_bytes // 2  # bf16 activations on the native path
    block = D // elems if D % elems == 0 else 0
    return (
        D % 256 == 0
        and D <= 8192
        and block % 32 == 0
        and 32 <= block <= 1024
    )


# ---------------------------------------------------------------------------
# JIT module (one compile; production template combos exported, bf16-only
# combos in both vector widths for measured selection)
# ---------------------------------------------------------------------------

_NS = "kda_norm_scale_shift"
_CLS = {"absent": 0, "scalar": 1, "row": 2, "token": 3}
_CPP_DT = {_BF16: "bf16_t", _FP32: "fp32_t"}


def _combo_vec_bytes(sc_dtype, gate_dtype, has_wb) -> int:
    if sc_dtype == _FP32 or gate_dtype == _FP32 or has_wb:
        return VEC_BYTES_FP32_OPERANDS
    return VEC_BYTES_BF16


def _flags(vec_bytes: int, early: bool) -> str:
    tp = "true" if TWO_PASS_VARIANCE else "false"
    pdl = "true" if USE_PDL else "false"
    eo = "true" if early else "false"
    return f"false, {tp}, {pdl}, {eo}, {vec_bytes}"  # kIsRms=false (layer-only fast path)


def _wrapper_table():
    """(entry, sc_class, sc_dtype, gate_class, gate_dtype, has_wb) -> {(vec, early): (export, symbol)}."""
    t = {}

    def add(key, base_name, symbol_fmt, widths):
        # Early scale/shift load variants exist only for row/token operand
        # classes (the kernel rejects the scalar class at compile time).
        earlies = (False, True) if key[1] in ("row", "token") else (False,)
        t[key] = {
            (vec, eo): (
                f"{base_name}_v{vec}{'_eo' if eo else ''}",
                symbol_fmt.format(flags=_flags(vec, eo)),
            )
            for vec in widths
            for eo in earlies
        }

    both = (16, 32)
    narrow = (16,)

    for sc_class in ("row", "token"):
        for sc_dt in (_BF16, _FP32):
            key = ("nss", sc_class, sc_dt, "absent", None, False)
            widths = both if sc_dt == _BF16 else narrow
            add(
                key,
                f"nss_{sc_class}_{_CPP_DT[sc_dt][:-2]}",
                f"{_NS}::NormScaleShiftKernel<bf16_t, {_CPP_DT[sc_dt]}, "
                f"{_CLS[sc_class]}, {{flags}}>::run",
                widths,
            )
    add(
        ("srnss", "row", _BF16, "row", _BF16, False),
        "srnss_grow_bf16_row_bf16",
        f"{_NS}::ScaleResidualNormScaleShiftKernel<bf16_t, bf16_t, bf16_t, "
        f"{_CLS['row']}, {_CLS['row']}, {{flags}}>::run",
        both,
    )
    for sc_class, sc_dt, export, widths in (
        ("row", _BF16, "srnss_gnone_row_bf16", both),
        ("row", _FP32, "srnss_gnone_row_fp32", narrow),
        ("token", _FP32, "srnss_gnone_token_fp32", narrow),
    ):
        add(
            ("srnss", sc_class, sc_dt, "absent", None, False),
            export,
            f"{_NS}::ScaleResidualNormScaleShiftKernel<bf16_t, bf16_t, "
            f"{_CPP_DT[sc_dt]}, {_CLS['absent']}, {_CLS[sc_class]}, {{flags}}>::run_nogate",
            widths,
        )
    for gate_class, export in (
        ("row", "srnss_grow_fp32_wb_scalar_bf16"),
        ("token", "srnss_gtoken_fp32_wb_scalar_bf16"),
    ):
        add(
            ("srnss", "scalar", _BF16, gate_class, _FP32, True),
            export,
            f"{_NS}::ScaleResidualNormScaleShiftAffineKernel<bf16_t, fp32_t, "
            f"fp32_t, bf16_t, {_CLS[gate_class]}, {_CLS['scalar']}, {{flags}}>::run",
            narrow,
        )
    return t


_WRAPPERS = _wrapper_table()

# Production buckets measured persistently below the per-row floor on H200 and
# routed to the vendored baseline per the task's regression policy (see
# docs/dispatch.md). NCU evidence: identical geometry/regs/bytes but exposed
# operand-load latency (short_scoreboard 2.4x baseline); both occupancy-neutral
# fixes measured worse (prefetch.global.L1 flooded the LSU: 620us vs 381us;
# early raw loads cost 40 regs -> 2 CTAs/SM: 489us vs 381us).
_ROUTED_TO_BASELINE = {
    ("nss", "row", _FP32, "absent", None, False),
}

_MOD = None


def _module():
    global _MOD
    if _MOD is None:
        # Profiling-only hook (e.g. KDA_EXTRA_CUDA_CFLAGS=-lineinfo for ncu
        # SASS->source mapping). Shipped builds never set it; the module name
        # encodes the extra flags so profiling builds cannot shadow clean ones.
        extra = os.environ.get("KDA_EXTRA_CUDA_CFLAGS", "").split()
        tag = f"x{abs(hash(tuple(extra))) % 10**8}" if extra else "clean"
        wrappers = sorted({entry for combos in _WRAPPERS.values() for entry in combos.values()})
        _MOD = _baseline.snapshot_load_jit(
            "kda_nss",
            _SRC_HASH,
            tag,
            cuda_files=[str(_CUH)],
            cuda_wrappers=wrappers,
            extra_cuda_cflags=extra,
            extra_include_paths=[str(_THIS_DIR / "csrc")],
        )
    return _MOD


def _native_fn(key, vec_bytes: int):
    combos = _WRAPPERS.get(key)
    if combos is None:
        return None
    entry = combos.get((vec_bytes, EARLY_SCALE_SHIFT and key[1] in ("row", "token")))
    if entry is None:
        return None
    return getattr(_module(), entry[0])


def _fallback(reason: str):
    DISPATCH_STATS["fallback"] += 1
    DISPATCH_STATS[f"fallback:{reason}"] += 1


# ---------------------------------------------------------------------------
# Dispatch implementations (exact SGLang signatures)
# ---------------------------------------------------------------------------


def _nss_impl(x, weight, bias, scale, shift, norm_type, eps=1e-5):
    if not (
        isinstance(x, torch.Tensor)
        and x.is_cuda
        and x.ndim == 3
        and x.shape[0] == 1  # only captured-production batch geometry is verified native
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
    if key in _ROUTED_TO_BASELINE:
        DISPATCH_STATS["routed"] += 1
        DISPATCH_STATS["routed:nss_row_fp32"] += 1
        return _BASELINE_NSS(x, weight, bias, scale, shift, norm_type, eps)
    vec = _combo_vec_bytes(scale.dtype, None, False)
    if not _geometry_ok(D, vec):
        _fallback("nss:geometry")
        return _BASELINE_NSS(x, weight, bias, scale, shift, norm_type, eps)
    fn = _native_fn(key, vec)
    if fn is None:
        _fallback("nss:combo")
        return _BASELINE_NSS(x, weight, bias, scale, shift, norm_type, eps)
    DISPATCH_STATS["native"] += 1
    y = torch.empty_like(x)
    fn(y.view(B * S, D), x.view(B * S, D), sc[1], sh[1], float(eps))
    return y


def _srnss_impl(residual, x, gate, weight, bias, scale, shift, norm_type, eps=1e-5):
    if not (
        isinstance(x, torch.Tensor)
        and isinstance(residual, torch.Tensor)
        and x.is_cuda
        and x.ndim == 3
        and x.shape[0] == 1  # only captured-production batch geometry is verified native
        and norm_type == "layer"
        and residual.shape == x.shape
        and residual.dtype == x.dtype
    ):
        _fallback("srnss:contract")
        return _BASELINE_SRNSS(residual, x, gate, weight, bias, scale, shift, norm_type, eps)
    B, S, D = x.shape
    if not (_activation_ok(x, D) and _activation_ok(residual, D)):
        _fallback("srnss:activation")
        return _BASELINE_SRNSS(residual, x, gate, weight, bias, scale, shift, norm_type, eps)

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
            and weight.is_cuda
            and weight.device == x.device
            and bias.device == x.device
        )
        if not wb_ok:
            _fallback("srnss:weight_bias")
            return _BASELINE_SRNSS(residual, x, gate, weight, bias, scale, shift, norm_type, eps)

    if not (isinstance(scale, torch.Tensor) and isinstance(shift, torch.Tensor)):
        _fallback("srnss:operand")  # baseline raises its own validation error
        return _BASELINE_SRNSS(residual, x, gate, weight, bias, scale, shift, norm_type, eps)
    g = _classify_operand(gate, B, S, D, x.device)
    sc = _classify_operand(scale, B, S, D, x.device)
    sh = _classify_operand(shift, B, S, D, x.device)
    if g is None or sc is None or sh is None or sc[0] != sh[0] or scale.dtype != shift.dtype:
        _fallback("srnss:operand")
        return _BASELINE_SRNSS(residual, x, gate, weight, bias, scale, shift, norm_type, eps)
    gate_dtype = gate.dtype if isinstance(gate, torch.Tensor) else None
    key = ("srnss", sc[0], scale.dtype, g[0], gate_dtype, has_wb)
    vec = _combo_vec_bytes(scale.dtype, gate_dtype, has_wb)
    if not _geometry_ok(D, vec):
        _fallback("srnss:geometry")
        return _BASELINE_SRNSS(residual, x, gate, weight, bias, scale, shift, norm_type, eps)
    fn = _native_fn(key, vec)
    if fn is None:
        _fallback("srnss:combo")
        return _BASELINE_SRNSS(residual, x, gate, weight, bias, scale, shift, norm_type, eps)
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
# Public entry points: custom ops mirroring the baseline's registration
# (`mutates_args=()` + `register_fake`) so both benchmark sides carry
# identical host stacks.
# ---------------------------------------------------------------------------


@torch.library.custom_op("kda_nss::fused_norm_scale_shift", mutates_args=())
def fused_norm_scale_shift(
    x: torch.Tensor,
    weight: Optional[torch.Tensor],
    bias: Optional[torch.Tensor],
    scale: torch.Tensor,
    shift: torch.Tensor,
    norm_type: str,
    eps: float = 1e-5,
) -> torch.Tensor:
    return _nss_impl(x, weight, bias, scale, shift, norm_type, eps)


@fused_norm_scale_shift.register_fake
def _nss_fake(x, weight, bias, scale, shift, norm_type, eps=1e-5):
    return x.new_empty(x.shape)


@torch.library.custom_op("kda_nss::fused_scale_residual_norm_scale_shift", mutates_args=())
def fused_scale_residual_norm_scale_shift(
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
    return _srnss_impl(residual, x, gate, weight, bias, scale, shift, norm_type, eps)


@fused_scale_residual_norm_scale_shift.register_fake
def _srnss_fake(residual, x, gate, weight, bias, scale, shift, norm_type, eps=1e-5):
    return x.new_empty(x.shape), x.new_empty(x.shape)


def build() -> None:
    """Force the JIT build (used by the remote driver to pay compile cost upfront)."""
    _module()
