"""Native-CUDA fused QK-norm + RoPE candidate wrapper.

Supported signatures dispatch to a workspace-owned CUDA kernel built through SGLang's
``jit_kernel`` / tvm-ffi stack (``load_jit`` + ``make_cpp_args``). Everything else takes a
device/dtype/layout-agnostic PyTorch FP32 semantic fallback that never raises, except a
re-entrancy / double-install guard.

The public op mirrors ``sglang.jit_kernel.diffusion.qknorm_rope.fused_inplace_qknorm_rope``:
in-place on ``q`` and ``k``, returns ``None``.
"""

from __future__ import annotations

import functools
import os
import threading
from pathlib import Path
from typing import Callable, Optional

import torch

try:  # SGLang's manual cache (matches the diffusion baseline); lru_cache fallback off-GPU.
    from sglang.jit_kernel.utils import cache_once
except Exception:  # pragma: no cover - sglang not importable in CPU-only environments
    def cache_once(fn):
        return functools.lru_cache(maxsize=None)(fn)

_CSRC_DIR = Path(__file__).resolve().parent / "csrc"
_SRC_CUH = _CSRC_DIR / "qknorm_rope_kernel.cuh"  # workspace-owned source of truth

_SUPPORTED_HEAD_DIMS = (64, 128, 256)
_SUPPORTED_DTYPES = (torch.bfloat16,)  # fast path is bf16; fp16/fp32 take the fallback

_tls = threading.local()

# Optional delegate used for the fallback path instead of the semantic reference. Left as the
# semantic reference by default; the in-SGLang export / double-install test may point this at a
# callable to exercise the re-entrancy guard.
BASELINE_DELEGATE: Optional[Callable[..., None]] = None


def get_last_dispatch() -> Optional[str]:
    """Return the dispatch path taken by the most recent call on this thread."""
    return getattr(_tls, "last_dispatch", None)


def _set_last_dispatch(tag: str) -> None:
    _tls.last_dispatch = tag


# --------------------------------------------------------------------------------------
# Support gate
# --------------------------------------------------------------------------------------
@functools.lru_cache(maxsize=None)
def _static_eligible(head_dim: int, rope_dim: int, is_neox: bool, dtype: torch.dtype) -> bool:
    """Signature-only eligibility (cached): the head_dim/rope_dim/is_neox/dtype template gate."""
    if head_dim not in _SUPPORTED_HEAD_DIMS or dtype not in _SUPPORTED_DTYPES:
        return False
    if rope_dim <= 0 or rope_dim > head_dim:
        return False
    elems_per_thread = head_dim // 32
    if elems_per_thread == 0 or rope_dim % elems_per_thread != 0:
        return False
    if is_neox:
        lanes = rope_dim // elems_per_thread
        if lanes < 2 or (lanes & (lanes - 1)):
            return False
    return True


def _overlaps(a: torch.Tensor, b: torch.Tensor) -> bool:
    """True if two contiguous tensors share any bytes (identical OR partially-overlapping views).

    Compares byte ranges ``[data_ptr, data_ptr + numel*element_size)``; distinct allocations are
    disjoint, so this also subsumes the identical-pointer case. Callers must ensure a and b are
    contiguous (the supported() gate checks contiguity first), so the byte range is exact.
    """
    a0 = a.data_ptr()
    a1 = a0 + a.numel() * a.element_size()
    b0 = b.data_ptr()
    b1 = b0 + b.numel() * b.element_size()
    return a0 < b1 and b0 < a1


def supported(
    q: torch.Tensor,
    k: torch.Tensor,
    q_weight: torch.Tensor,
    k_weight: torch.Tensor,
    cos_sin_cache: torch.Tensor,
    positions: torch.Tensor,
    *,
    is_neox: bool,
    head_dim: int,
    rope_dim: int,
) -> bool:
    """True iff the inputs are eligible for the native-CUDA fast path.

    Lean dispatch: the static template gate is cached; per-call work is the minimal set the kernel's
    TensorMatcher / AlignedVector loads require, so unsupported inputs fall back instead of raising.
    Every tensor read via AlignedVector (q, k, q_weight, k_weight) is 16-byte-alignment checked
    (the allocator guarantees >=256B base alignment, but contiguous offset views can break it);
    cos_sin_cache is read scalar via __ldg(float*) and positions are scalar, so their natural
    alignment suffices. Aliasing uses a byte-range overlap check so partially-overlapping q/k views
    (shared storage, different start pointers) also fall back.
    """
    if not _static_eligible(head_dim, rope_dim, is_neox, q.dtype):
        return False
    if q.device.type != "cuda":
        return False
    dev = q.device
    if (k.device != dev or q_weight.device != dev or k_weight.device != dev
            or cos_sin_cache.device != dev or positions.device != dev):
        return False
    if k.dtype is not q.dtype or q_weight.dtype is not q.dtype or k_weight.dtype is not q.dtype:
        return False
    if cos_sin_cache.dtype is not torch.float32 or positions.dtype not in (torch.int32, torch.int64):
        return False
    if q.dim() != 3 or k.shape != q.shape or q.size(-1) != head_dim:
        return False
    if q_weight.dim() != 1 or q_weight.numel() != head_dim or k_weight.dim() != 1 or k_weight.numel() != head_dim:
        return False  # wrong-shaped weights must fall back, not raise inside TensorMatcher
    if cos_sin_cache.dim() != 2 or cos_sin_cache.size(-1) != rope_dim:
        return False
    if positions.dim() != 1 or positions.size(0) != q.size(0):
        return False
    if not (q.is_contiguous() and k.is_contiguous() and q_weight.is_contiguous()
            and k_weight.is_contiguous() and cos_sin_cache.is_contiguous() and positions.is_contiguous()):
        return False
    # q/k AND the weights are read via AlignedVector (up to 16-byte loads in the warp2 path), so all
    # four must be 16-byte aligned; contiguous-but-offset views (e.g. base[1:]) fall back. (cos_sin_cache
    # is read with scalar __ldg(float*) and positions are scalar, so their natural alignment suffices.)
    if (q.data_ptr() % 16) or (k.data_ptr() % 16) or (q_weight.data_ptr() % 16) or (k_weight.data_ptr() % 16):
        return False
    if _overlaps(q, k):  # aliased OR overlapping q/k views -> in-place write order undefined, fall back
        return False
    return True


# --------------------------------------------------------------------------------------
# PyTorch FP32 semantic reference (oracle cross-check + CPU/fp16/fallback)
# --------------------------------------------------------------------------------------
def _qknorm_to_dtype(x: torch.Tensor, w: torch.Tensor, eps: float, head_dim: int) -> torch.Tensor:
    xf = x.float()
    var = xf.square().sum(dim=-1, keepdim=True) / float(head_dim)
    out = xf * torch.rsqrt(var + eps) * w.float().reshape(*([1] * (xf.dim() - 1)), head_dim)
    return out.to(x.dtype)  # intermediate cast mirrors the split oracle's BF16 rounding


def _rope_fp32(x: torch.Tensor, cos: torch.Tensor, sin: torch.Tensor, *, is_neox: bool, rope_dim: int) -> torch.Tensor:
    # x: [N, H, head_dim] FP32 ; cos/sin: [N, rope_dim/2] FP32
    half = rope_dim // 2
    x_rot = x[..., :rope_dim]
    cos = cos[:, None, :]
    sin = sin[:, None, :]
    if is_neox:
        x1 = x_rot[..., :half]
        x2 = x_rot[..., half:rope_dim]
        y1 = x1 * cos - x2 * sin
        y2 = x2 * cos + x1 * sin
        y = torch.cat((y1, y2), dim=-1)
    else:
        x1 = x_rot[..., 0::2]
        x2 = x_rot[..., 1::2]
        y1 = x1 * cos - x2 * sin
        y2 = x2 * cos + x1 * sin
        y = torch.stack((y1, y2), dim=-1).flatten(-2)
    out = x.clone()
    out[..., :rope_dim] = y
    return out


def semantic_reference_inplace(
    q: torch.Tensor,
    k: torch.Tensor,
    q_weight: torch.Tensor,
    k_weight: torch.Tensor,
    cos_sin_cache: torch.Tensor,
    positions: torch.Tensor,
    *,
    is_neox: bool,
    eps: float,
    head_dim: int,
    rope_dim: int,
) -> None:
    """Device/dtype/layout-agnostic FP32 reference; writes the fused result into q and k."""
    qn = _qknorm_to_dtype(q, q_weight, eps, head_dim)
    kn = _qknorm_to_dtype(k, k_weight, eps, head_dim)
    pos = positions.to(device=cos_sin_cache.device, dtype=torch.long).reshape(-1)
    cs = cos_sin_cache.index_select(0, pos).float()
    half = rope_dim // 2
    cos, sin = cs[:, :half], cs[:, half:rope_dim]
    q_out = _rope_fp32(qn.float(), cos, sin, is_neox=is_neox, rope_dim=rope_dim).to(q.dtype)
    k_out = _rope_fp32(kn.float(), cos, sin, is_neox=is_neox, rope_dim=rope_dim).to(k.dtype)
    q.copy_(q_out)
    k.copy_(k_out)


# --------------------------------------------------------------------------------------
# Native-CUDA candidate (built via SGLang jit_kernel / tvm-ffi)
# --------------------------------------------------------------------------------------
@cache_once
def _candidate_module(head_dim: int, rope_dim: int, is_neox: bool, dtype: torch.dtype):
    """Build the workspace-owned .cuh through SGLang load_jit without touching the SGLang tree.

    load_jit resolves cuda_files as ``(KERNEL_PATH/"csrc"/f).resolve()`` and emits
    ``#include "<resolved-path>"``, so a ``../``-relative path that resolves back to the
    task-owned source compiles it in place; sgl_kernel headers come from DEFAULT_INCLUDE.
    """
    from sglang.jit_kernel.utils import (
        KERNEL_PATH,
        is_arch_support_pdl,
        load_jit,
        make_cpp_args,
    )

    import hashlib

    if not _SRC_CUH.exists():
        raise FileNotFoundError(f"candidate kernel source missing: {_SRC_CUH}")
    rel = os.path.relpath(_SRC_CUH.resolve(), Path(KERNEL_PATH) / "csrc")
    # The .cuh is pulled in via #include, so fold its content hash into the JIT cache marker to
    # force a rebuild whenever the source changes (load_jit keys its cache on the *args marker).
    sha = hashlib.sha256(_SRC_CUH.read_bytes()).hexdigest()[:12]
    # Opt-in -lineinfo build (KDA_LINEINFO=1) for Nsight Compute SASS->source mapping; kept as a
    # separate cache marker so it never pollutes the timed/benchmark build. Matches the diffusion
    # baseline flags otherwise (no --use_fast_math).
    lineinfo = os.environ.get("KDA_LINEINFO") == "1"
    marker = f"qknorm_rope_kda_{sha}" + ("_li" if lineinfo else "")
    args = make_cpp_args(head_dim, rope_dim, is_neox, is_arch_support_pdl(), dtype)
    return load_jit(
        marker,
        *args,
        cuda_files=[rel],
        cuda_wrappers=[("qknorm_rope", f"QKNormRopeKernel<{args}>::run")],
        extra_include_paths=[str(_CSRC_DIR)],
        extra_cuda_cflags=["-lineinfo"] if lineinfo else None,
    )


# --------------------------------------------------------------------------------------
# Public entrypoint
# --------------------------------------------------------------------------------------
def optimized_wrapper(
    q: torch.Tensor,
    k: torch.Tensor,
    q_weight: torch.Tensor,
    k_weight: torch.Tensor,
    cos_sin_cache: torch.Tensor,
    positions: torch.Tensor,
    *,
    is_neox: bool,
    eps: float = 1e-6,
    head_dim: int = 0,
    rope_dim: int = 0,
) -> None:
    if getattr(_tls, "in_call", False):
        raise RuntimeError(
            "recursive fused_inplace_qknorm_rope detected (candidate installed as its own "
            "baseline); aborting to avoid infinite recursion"
        )
    head_dim = head_dim or q.size(-1)
    rope_dim = rope_dim or cos_sin_cache.size(-1)
    _tls.in_call = True
    try:
        if supported(
            q, k, q_weight, k_weight, cos_sin_cache, positions,
            is_neox=is_neox, head_dim=head_dim, rope_dim=rope_dim,
        ):
            module = _candidate_module(head_dim, rope_dim, is_neox, q.dtype)
            module.qknorm_rope(q, k, q_weight, k_weight, cos_sin_cache, positions, eps)
            _set_last_dispatch("cuda")
            return None
        delegate = BASELINE_DELEGATE
        if delegate is not None:
            delegate(
                q, k, q_weight, k_weight, cos_sin_cache, positions,
                is_neox=is_neox, eps=eps, head_dim=head_dim, rope_dim=rope_dim,
            )
        else:
            semantic_reference_inplace(
                q, k, q_weight, k_weight, cos_sin_cache, positions,
                is_neox=is_neox, eps=eps, head_dim=head_dim, rope_dim=rope_dim,
            )
        _set_last_dispatch("fallback")
        return None
    finally:
        _tls.in_call = False


# Public alias under SGLang's callable name. The generated kda_kernels overlay
# dispatcher imports this symbol by name (``getattr(<wrapper module>,
# "fused_inplace_qknorm_rope")``); ``optimized_wrapper`` already mirrors the
# exact SGLang signature, so this is a straight alias (same in-place contract,
# same re-entrancy guard, same dispatch/fallback behavior).
fused_inplace_qknorm_rope = optimized_wrapper
