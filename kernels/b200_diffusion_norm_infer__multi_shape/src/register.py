"""Registration + dispatcher for the b200_diffusion_norm_infer__multi_shape task.

Two wrapped SGLang entry points are optimized behind one router:
- ``norm_infer(x, weight, bias, eps, is_rms_norm=False, out=None)``  (LayerNorm/RMSNorm)
- ``triton_one_pass_rms_norm(x, w, eps=1e-6)``                       (tiled one-pass RMSNorm)

``optimized_wrapper`` routes by ``dispatcher_hint`` (or infers from the call
shape) to the matching optimized path, and falls back to the SGLang baseline
for any shape/dtype/layout/device/norm-type/flag it does not support.

Native-CUDA kernels live in ``norm_cuda/diffusion_norm_infer.cuh`` and are built
through the SGLang jit_kernel / tvm-ffi stack (``load_jit``). Build/run happen on
the GPU host; this module stays importable without torch/sglang (lazy imports).

Validation note: set ``KDA_REQUIRE_CUDA=1`` to make the CUDA path raise on any
failure instead of silently falling back (so a broken build can't masquerade as a
passing test by falling back to the baseline). Unset, the dispatcher falls back.
Code here carries no plan/workflow terminology.
"""

from __future__ import annotations

import os
from pathlib import Path
from typing import Any, Optional


KERNEL_SLUG = "b200_diffusion_norm_infer__multi_shape"
OP_TYPE = "layer_or_rms_norm_infer"

_CUDA_ENABLED = True
_HERE = Path(__file__).resolve().parent
_CUH = str(_HERE / "norm_cuda" / "diffusion_norm_infer.cuh")
_INCLUDE = str(_HERE / "norm_cuda")
_KERNEL_VERSION = "v4"  # bump to force a JIT rebuild (stale-JIT guard); v4 = half-warp shuffle masks in the tiled RMS reduction (odd-tail safety)
# Large-S RMS routes to the tiled multi-row kernel (two row-pairs per warp with
# both pair loads in flight + persistent whole-wave grid: hides load latency and
# avoids the 40k-CTA launch wave); small/mid RMS keeps the one-warp-per-row
# kernel (kUnroll=1) to maximize warp count / occupancy at low row counts.
_RMS_LARGE_S = 100000
_RMS_TILED_ROWS = 32
_RMS_TILED_SCHEDULING = 1  # persistent occupancy-derived whole-wave grid
_LN_MAX_N = 5120  # informational: float4 LN kernel covers N<=kLNThreads*4*kLNMaxVec=5120; routing is gated by the _SUPPORTED_LN allowlist below, not this constant

# Configured-shape allowlists. CUDA routes ONLY these exact (M,N)/(S,D) shapes;
# every other shape falls back to the SGLang baseline (interface.md contract).
# Entries = the production shapes + the CI-configured correctness coverage that
# must exercise CUDA (regression/fused grid M=B*S in {6,12,128,256} x N in
# {512,3072}; NaN/Inf + preallocated-out shapes). Under KDA_FULL_REGRESSION the
# extra grid shapes are not listed and correctly fall back.
_SUPPORTED_LN = frozenset({
    (8640, 5120),                                       # helios production
    (6, 512), (6, 3072), (12, 512), (12, 3072),         # CI regression / fused grid
    (128, 512), (128, 3072), (256, 512), (256, 3072),   # CI regression / fused grid
    (64, 1024), (256, 1024),                            # NaN/Inf + preallocated-out coverage
})
# NO-GO (round 4): the two large-S production shapes (648720, 650040) are NOT in
# the CUDA allowlist and fell back to the SGLang Triton baseline (= parity):
# the warp-per-row kernel (incl. the kUnroll=2/4 MLP variant) measured
# ~0.84-0.92x vs the baseline (interleaved, idle B200) and was memory-latency
# bound (long-scoreboard ~56%). REOPENED with the tiled multi-row kernel
# (RmsNormTiledKernel<128,32,bf16>, persistent grid): beats the pinned Triton
# baseline 1.10-1.11x wall / 1.14-1.16x kernel-event on BOTH huge shapes in two
# independent interleaved runs (paired-bootstrap CI95 lower bounds > 1.09;
# benchmark.csv cand-0010-tile-r32-persistent + -rep2). Note the measured
# context-dependence: in cache-flushed NCU isolation the Triton baseline is
# faster; in production-like back-to-back execution (dirty-L2 steady state,
# which is how diffusion denoise runs this op) the tiled kernel wins — the
# steady-state interleaved lane is the promotion arbiter (docs/dispatch.md,
# profile/tile_r32_r2/REPORT.md).
_SUPPORTED_RMS = frozenset({
    (1320, 128), (16384, 128), (4096, 128),             # production small/mid (CUDA wins ~1.5-1.7x)
    (648720, 128), (650040, 128),                       # production huge-S (tiled CUDA wins ~1.10x wall / ~1.15x kernel)
    (6, 128), (128, 128), (768, 128), (64, 128),        # regression-small + NaN/Inf coverage
})

_MODULE_CACHE: dict = {}


def _require_cuda() -> bool:
    return os.environ.get("KDA_REQUIRE_CUDA") == "1"


# --- SGLang baselines (lazy import; the source of truth for fallback) --------
def _baseline_norm_infer(x, weight, bias, eps, is_rms_norm=False, out=None):
    from sglang.jit_kernel.diffusion.triton.norm import norm_infer

    return norm_infer(x, weight, bias, eps, is_rms_norm=is_rms_norm, out=out)


def _baseline_rms_onepass(x, w, eps=1e-6):
    from sglang.jit_kernel.diffusion.triton.rmsnorm_onepass import (
        triton_one_pass_rms_norm,
    )

    return triton_one_pass_rms_norm(x, w, eps)


# --- JIT module builders (cached per dtype/dim) ------------------------------
def _ln_module(dtype):
    key = ("ln", str(dtype))
    mod = _MODULE_CACHE.get(key)
    if mod is None:
        from sglang.jit_kernel.utils import load_jit, make_cpp_args

        args = make_cpp_args(dtype)
        mod = load_jit(
            "b200_diffnorm_ln",
            _KERNEL_VERSION,
            *args,
            cuda_files=[_CUH],
            cuda_wrappers=[("norm_infer_ln", f"LayerNormInferKernel<{args}>::run")],
            extra_include_paths=[_INCLUDE],
        )
        _MODULE_CACHE[key] = mod
    return mod


def _rms_module(dim, k_unroll, dtype):
    key = ("rms", int(dim), int(k_unroll), str(dtype))
    mod = _MODULE_CACHE.get(key)
    if mod is None:
        from sglang.jit_kernel.utils import load_jit, make_cpp_args

        args = make_cpp_args(int(dim), int(k_unroll), dtype)
        mod = load_jit(
            "b200_diffnorm_rms",
            _KERNEL_VERSION,
            *args,
            cuda_files=[_CUH],
            cuda_wrappers=[("rms_onepass", f"RmsNormOnepassKernel<{args}>::run")],
            extra_include_paths=[_INCLUDE],
        )
        _MODULE_CACHE[key] = mod
    return mod


def _rms_tiled_module(dim, rows_per_cta, dtype):
    key = ("rms_tiled", int(dim), int(rows_per_cta), str(dtype))
    mod = _MODULE_CACHE.get(key)
    if mod is None:
        from sglang.jit_kernel.utils import load_jit, make_cpp_args

        args = make_cpp_args(int(dim), int(rows_per_cta), dtype)
        mod = load_jit(
            "b200_diffnorm_rms_tiled",
            _KERNEL_VERSION,
            *args,
            cuda_files=[_CUH],
            cuda_wrappers=[("rms_tiled", f"RmsNormTiledKernel<{args}>::run")],
            extra_include_paths=[_INCLUDE],
        )
        _MODULE_CACHE[key] = mod
    return mod


def tiled_rms_onepass(x, w, eps: float = 1e-6, *, rows_per_cta: int = 16, scheduling: int = 0):
    """Direct harness entry to the tiled multi-row RMSNorm (D=128, bf16).

    Production traffic reaches the same kernel through ``optimized_wrapper`` →
    ``_cuda_rms_onepass`` (allowlisted huge-S shapes route to the tiled module
    there); THIS function is the raise-on-misuse side door used by the
    validation/benchmark harnesses so a broken build or out-of-contract input
    can never masquerade as a pass via fallback. ``scheduling``: 0 = one CTA
    per tile, 1 = persistent occupancy-derived whole-wave grid.

    Raises on anything outside the kernel's contract (bf16, 2-D, D=128,
    contiguous, matching 1-D weight) instead of falling back — a broken or
    misused build must fail loudly in the harnesses."""
    import torch

    if rows_per_cta not in (16, 32):
        raise ValueError(f"rows_per_cta must be 16 or 32, got {rows_per_cta}")
    if scheduling not in (0, 1):
        raise ValueError(f"scheduling must be 0 (plain) or 1 (persistent), got {scheduling}")
    if x.dim() != 2 or x.shape[-1] != 128:
        raise ValueError(f"tiled RMS expects a 2-D [S, 128] input, got {tuple(x.shape)}")
    if x.dtype != torch.bfloat16:
        raise ValueError(f"tiled RMS is bf16-only, got {x.dtype}")
    if not x.is_contiguous():
        raise ValueError("tiled RMS expects a contiguous input")
    if w.dim() != 1 or w.shape[0] != 128 or w.dtype != x.dtype or w.device != x.device or not w.is_contiguous():
        raise ValueError("tiled RMS expects a contiguous bf16 weight of shape (128,) on the input device")
    # Same 16-byte base-alignment gate as the production dispatcher: the tiled
    # kernel uses AlignedVector<bf16,8> (16 B) accesses, and a contiguous OFFSET
    # view can be only 8-byte aligned — that must raise here, not launch.
    if x.data_ptr() % _RMS_TILED_ALIGN != 0 or w.data_ptr() % _RMS_TILED_ALIGN != 0:
        raise ValueError(
            "tiled RMS requires 16-byte-aligned x and w base pointers "
            "(a contiguous-but-offset view can violate this; route such inputs "
            "through the dispatcher, which falls back to the baseline)"
        )

    out = torch.empty_like(x)
    _rms_tiled_module(x.shape[-1], rows_per_cta, x.dtype).rms_tiled(x, w, out, eps, scheduling)
    return out


# --- Support predicates (CUDA routes ONLY configured shapes; else fall back) ---
# norm_infer -> CUDA iff: fp32, 2-D, contiguous, is_rms_norm=False, (M,N) in
#   _SUPPORTED_LN, and weight+bias are non-None, contiguous, shape==(N,), on the
#   same device, same dtype as x.
# rms_onepass -> CUDA iff: bf16, contiguous, (S,D) in _SUPPORTED_RMS, and w is
#   non-None, contiguous, shape==(D,), same device, same dtype as x.
# Everything else (other shapes, fp16/bf16 LN, is_rms_norm=True, non-contiguous,
# non-CUDA, mismatched/missing weight device/dtype/shape, D!=128, fp32 RMS, ...)
# falls back to the SGLang baseline. Verified by test_correctness.py::test_fallback_routing.
def _is_cuda_contig_2d(t) -> bool:
    return t is not None and getattr(t, "is_cuda", False) and t.dim() == 2 and t.is_contiguous()


# Vectorized-load alignment: the LN kernel reinterprets pointers as float4* (16 B);
# the RMS kernel loads AlignedVector<bf16,4> (8 B). A tensor can be is_contiguous()
# yet be a VIEW with a non-zero storage offset whose data_ptr() is NOT aligned to
# the vector width (e.g. base[1:].view(M, N)); an aligned vector load from such a
# base faults or returns wrong data, so it must fall back to the Triton baseline.
# Because every supported row stride is a multiple of the vector width (LN N%4==0 ->
# N*4 B multiple of 16; RMS D=128 -> D*2=256 B multiple of 8), a vector-aligned BASE
# pointer makes every row aligned, so checking the base data_ptr() is sufficient.
_LN_ALIGN = 16
_RMS_ALIGN = 8
_RMS_TILED_ALIGN = 16  # tiled large-S kernel loads AlignedVector<bf16,8> (16 B)


def _aligned(t, nbytes: int) -> bool:
    return t is None or (t.data_ptr() % nbytes == 0)


def _valid_affine(t, n, x) -> bool:
    return (
        t is not None
        and t.is_contiguous()
        and tuple(t.shape) == (n,)
        and t.device == x.device
        and t.dtype == x.dtype
    )


def _valid_out(out, x) -> bool:
    # `out` is part of the public norm_infer contract: accept only None or an
    # output that exactly matches x (shape/device/dtype) and is contiguous,
    # otherwise fall back (the CUDA launcher's TensorMatcher would reject it).
    return out is None or (
        tuple(out.shape) == tuple(x.shape)
        and out.device == x.device
        and out.dtype == x.dtype
        and out.is_contiguous()
    )


def _norm_infer_supported(x, weight, bias, is_rms_norm, out=None) -> bool:
    import torch

    if not (_is_cuda_contig_2d(x) and x.dtype == torch.float32 and not is_rms_norm):
        return False
    m, n = int(x.shape[0]), int(x.shape[1])
    if (m, n) not in _SUPPORTED_LN:
        return False
    # float4 (16-byte) vectorized loads/stores: x, weight, bias and a caller-provided
    # out must all be 16-byte-aligned bases, else a contiguous-but-offset view would
    # hit misaligned vector access -> fall back. (out=None is allocated fresh -> aligned.)
    return (
        _valid_affine(weight, n, x)
        and _valid_affine(bias, n, x)
        and _valid_out(out, x)
        and _aligned(x, _LN_ALIGN)
        and _aligned(weight, _LN_ALIGN)
        and _aligned(bias, _LN_ALIGN)
        and _aligned(out, _LN_ALIGN)
    )


def _rms_onepass_supported(x, w) -> bool:
    import torch

    # Require exactly 2-D so a flattened higher-rank tensor (e.g. (1,6,128)) is
    # NOT treated as the configured 2-D (S,D) shape.
    if not (
        x is not None
        and getattr(x, "is_cuda", False)
        and x.dim() == 2
        and x.is_contiguous()
        and x.dtype == torch.bfloat16
    ):
        return False
    s, d = int(x.shape[0]), int(x.shape[1])
    if (s, d) not in _SUPPORTED_RMS:
        return False
    # Vectorized loads/stores: the one-warp-per-row kernel uses AlignedVector<bf16,4>
    # (8-byte) accesses; the tiled large-S kernel uses AlignedVector<bf16,8> (16-byte)
    # accesses. x and w must be aligned bases for the route the shape will take, else
    # a contiguous-but-offset view would hit misaligned vector access -> fall back.
    # (The output is allocated fresh -> always aligned.)
    align = _RMS_TILED_ALIGN if s >= _RMS_LARGE_S else _RMS_ALIGN
    return _valid_affine(w, d, x) and _aligned(x, align) and _aligned(w, align)


# --- CUDA paths --------------------------------------------------------------
def _cuda_norm_infer(x, weight, bias, eps, is_rms_norm=False, out=None):
    import torch

    if out is None:
        out = torch.empty_like(x)
    _ln_module(x.dtype).norm_infer_ln(x, weight, bias, out, eps)
    return out


def _cuda_rms_onepass(x, w, eps=1e-6):
    import torch

    shape = x.shape
    x2d = x.reshape(-1, shape[-1])
    out = torch.empty_like(x)
    out2d = out.reshape(-1, shape[-1])
    if x2d.shape[0] >= _RMS_LARGE_S:
        _rms_tiled_module(shape[-1], _RMS_TILED_ROWS, x.dtype).rms_tiled(
            x2d, w, out2d, eps, _RMS_TILED_SCHEDULING
        )
    else:
        _rms_module(shape[-1], 1, x.dtype).rms_onepass(x2d, w, out2d, eps)
    return out


# --- Public optimized entry points (preserve the SGLang signatures) ----------
def optimized_norm_infer(x, weight, bias, eps, is_rms_norm: bool = False, out=None):
    if _CUDA_ENABLED and _norm_infer_supported(x, weight, bias, is_rms_norm, out):
        if _require_cuda():
            return _cuda_norm_infer(x, weight, bias, eps, is_rms_norm=is_rms_norm, out=out)
        try:
            return _cuda_norm_infer(x, weight, bias, eps, is_rms_norm=is_rms_norm, out=out)
        except Exception:
            pass  # safe baseline fallback
    return _baseline_norm_infer(x, weight, bias, eps, is_rms_norm=is_rms_norm, out=out)


def optimized_triton_one_pass_rms_norm(x, w, eps: float = 1e-6):
    if _CUDA_ENABLED and _rms_onepass_supported(x, w):
        if _require_cuda():
            return _cuda_rms_onepass(x, w, eps)
        try:
            return _cuda_rms_onepass(x, w, eps)
        except Exception:
            pass
    return _baseline_rms_onepass(x, w, eps)


def _infer_hint(args: tuple, kwargs: dict) -> str:
    """Infer which wrapped entry point a hintless call targets, from the two
    distinct public signatures. Both take a 1-D weight tensor as the 2nd
    positional arg, so the 2nd arg's shape CANNOT disambiguate them:
        norm_infer(x, weight, bias, eps, is_rms_norm=False, out=None)  # 3rd positional is `bias`
        triton_one_pass_rms_norm(x, w, eps=1e-6)                       # 2 positional (+ float eps)
    Disambiguate by signature-unique parameter names, positional arity, and the
    3rd positional's type (bias tensor/None vs eps float) -- never by weight shape.
    """
    # 1) Parameter names unique to exactly one signature are decisive.
    if {"weight", "bias", "is_rms_norm", "out"} & kwargs.keys():
        return "norm_infer"
    if "w" in kwargs:
        return "rms_onepass"
    # 2) Only norm_infer takes a 4th positional (eps); a 3rd positional is `bias`
    #    (tensor/None) for norm_infer but `eps` (a float) for the one-pass RMS.
    if len(args) >= 4:
        return "norm_infer"
    if len(args) == 3:
        return "rms_onepass" if isinstance(args[2], (int, float)) else "norm_infer"
    # 3) Exactly two positionals with no disambiguating kwargs: norm_infer requires
    #    bias+eps (no defaults), so a bare (x, w[, eps=...]) call is one-pass RMS.
    if len(args) == 2:
        return "rms_onepass"
    # 4) Too few positionals to classify; default to the layer-norm path.
    return "norm_infer"


def optimized_wrapper(*args: Any, dispatcher_hint: Optional[str] = None, **kwargs: Any) -> Any:
    hint = dispatcher_hint or _infer_hint(args, kwargs)
    if hint == "rms_onepass":
        return optimized_triton_one_pass_rms_norm(*args, **kwargs)
    if hint == "norm_infer":
        return optimized_norm_infer(*args, **kwargs)
    raise ValueError(f"unknown dispatcher_hint {hint!r}")


def register() -> dict[str, Any]:
    return {
        "name": KERNEL_SLUG,
        "op_type": OP_TYPE,
        "callable": optimized_wrapper,
        "version": "dev",
        "source": __file__,
    }
