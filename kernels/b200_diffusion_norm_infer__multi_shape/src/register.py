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
_KERNEL_VERSION = "v2"  # bump to force a JIT rebuild (stale-JIT guard); v2 = per-S RMS kUnroll
# Large-S RMS uses kUnroll>1 (memory-level parallelism hides load latency); small/mid
# RMS keeps kUnroll=1 (one row/warp) to maximize warp count / occupancy.
_RMS_LARGE_S = 100000
_RMS_LARGE_UNROLL = 4
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
# the CUDA allowlist -> they fall back to the SGLang Triton baseline (= parity).
# Evidence: the warp-per-row kernel (incl. the kUnroll=2/4 MLP variant) measured
# ~0.84-0.92x vs the baseline on idle B200 (interleaved); NCU showed memory-latency
# + compute(SM)-leaning (DRAM 38% / Mem 47% / SM 63%, occ 77%), and the one-warp-
# per-row structure cannot match the baseline's 16-row tile for this huge
# bandwidth-streaming regime. Falling back avoids a production regression.
_SUPPORTED_RMS = frozenset({
    (1320, 128), (16384, 128), (4096, 128),             # production small/mid (CUDA wins ~1.5-1.7x)
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
    # AlignedVector<bf16,4> (8-byte) vectorized loads/stores: x and w must be
    # 8-byte-aligned bases, else a contiguous-but-offset view would hit misaligned
    # vector access -> fall back. (The output is allocated fresh -> always aligned.)
    return _valid_affine(w, d, x) and _aligned(x, _RMS_ALIGN) and _aligned(w, _RMS_ALIGN)


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
    k_unroll = _RMS_LARGE_UNROLL if x2d.shape[0] >= _RMS_LARGE_S else 1
    _rms_module(shape[-1], k_unroll, x.dtype).rms_onepass(x2d, w, out2d, eps)
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
