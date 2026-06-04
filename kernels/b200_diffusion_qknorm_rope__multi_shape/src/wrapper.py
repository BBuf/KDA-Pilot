"""Native-CUDA fused QK-norm + RoPE candidate wrapper (b200, multi-shape).

The public op mirrors ``sglang.jit_kernel.diffusion.qknorm_rope.fused_inplace_qknorm_rope``
exactly: in-place on ``q`` and ``k``, returns ``None``.

Dispatch is **exact-shape, fail-closed**. The workspace-owned CUDA kernel
``QKNormRopeStagedKernel`` (CTA-per-token, cos/sin staged once into shared memory and
reused across a token's heads) is the only fast path, and it fires ONLY for the exact
large captured production rows where Nsight Compute proved a device win
(``long_scoreboard`` 11.9->9.29, device 109.6->88.1 us; device-fair 1.10-1.26x). Every
other signature — the small captured rows, any non-captured shape, any non-production
dtype/dim/flag/layout — falls back to the SGLang baseline BEFORE the C++ matcher.

This module owns all heavy machinery (``Path(__file__)``, torch, ``load_jit``) so the
sibling ``register.py`` stays import-light and ``exec``-safe. It is the TASK-LOCAL loop
lane only: candidate iteration, correctness, and device-fair A/B run through it. The
SHIPPING integration is the in-tree ``.cuh`` placement inside SGLang's own
``python/sglang/jit_kernel/csrc/diffusion/qknorm_rope.cuh`` (public op and its
``register_custom_op`` byte-unchanged) — see ``docs/sglang_jit_export.md``. The historical
``kda_kernels`` overlay export of this wrapper was measured as a net regression
(host dispatch tax) and is retired for this task; the export tool still exists in the
repo but is no longer this task's promotion path.

Recursion safety (kept as defense-in-depth from the overlay era, and still useful if any
caller rebinds the public symbol): the SGLang baseline is captured at *import* time, so
the small/fallback route calls the original fast baseline rather than a possibly-swapped
public symbol. A thread-local re-entrancy guard, an identity/``__module__`` recursion
check, and a never-recursing PyTorch ``semantic_reference_inplace`` safety net defend
against any rebinding/ordering surprise.
"""

from __future__ import annotations

import functools
import hashlib
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


# SGLang baseline captured at IMPORT time, so the fallback route always holds the ORIGINAL
# fast CUDA baseline even if some caller later rebinds the public symbol (defense-in-depth
# retained from the retired overlay era).
try:
    from sglang.jit_kernel.diffusion.qknorm_rope import (
        fused_inplace_qknorm_rope as _SGLANG_BASELINE_AT_IMPORT,
    )
except Exception:  # pragma: no cover - sglang not importable off-GPU
    _SGLANG_BASELINE_AT_IMPORT = None


_CSRC_DIR = Path(__file__).resolve().parent
_SRC_CUH = _CSRC_DIR / "qknorm_rope_candidate.cuh"  # workspace-owned source of truth

# Exact captured production rows -> the eps each was captured with. The staged kernel is
# trusted ONLY on these exact (num_tokens, num_heads, eps) signatures (all head_dim=128,
# rope_dim=128, is_neox=False, bf16, int64 positions). Keying on eps too keeps the gate
# fail-closed: e.g. (4096, 24) with eps=1e-5 is NOT the qwen production row and falls back.
_STAGED_EPS: dict[tuple[int, int], float] = {
    (7904, 32): 1e-6,  # joyai-edit
    (4096, 24): 1e-6,  # qwen
    (8424, 24): 1e-6,  # qwen-edit
    (4096, 30): 1e-5,  # zimage
    (4128, 30): 1e-5,  # zimage
}

_tls = threading.local()

# Optional explicit fallback delegate. Left None by default (the fallback then uses the
# captured fast SGLang baseline, or the PyTorch semantic reference if none is available).
# Tests may point this at a callable to exercise the recursion guard.
BASELINE_DELEGATE: Optional[Callable[..., None]] = None


def get_last_dispatch() -> Optional[str]:
    """Return the dispatch path taken by the most recent call on this thread
    (``"cuda"`` for the staged kernel, ``"fallback"`` for the baseline route)."""
    return getattr(_tls, "last_dispatch", None)


def _set_last_dispatch(tag: str) -> None:
    _tls.last_dispatch = tag


# --------------------------------------------------------------------------------------
# Exact-shape, fail-closed support gate
# --------------------------------------------------------------------------------------
def _is_captured_large(num_tokens: int, num_heads: int, eps: float) -> bool:
    """True only for the exact large captured (num_tokens, num_heads, eps) production rows."""
    expected = _STAGED_EPS.get((num_tokens, num_heads))
    return expected is not None and abs(eps - expected) <= 1e-9


def _overlaps(a: torch.Tensor, b: torch.Tensor) -> bool:
    """True if two contiguous tensors share any bytes (identical OR partially overlapping).

    Compares byte ranges ``[data_ptr, data_ptr + numel*element_size)``; distinct
    allocations are disjoint, so this also subsumes the identical-pointer case. Callers
    ensure a and b are contiguous (the gate checks contiguity first), so the range is exact.
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
    eps: float,
    head_dim: int,
    rope_dim: int,
) -> bool:
    """True iff the inputs are an exact captured-large production signature eligible for the
    staged CUDA kernel. Anything else returns False -> SGLang baseline fallback, so an
    unsupported or malformed signature can never reach the staged C++ TensorMatcher.

    Beyond the exact (num_tokens, num_heads, eps) key this validates the FULL production
    contract: production template (head_dim/rope_dim/is_neox), device, dtypes, ranks,
    shapes, contiguity, 16-byte alignment of every AlignedVector-loaded tensor, int64
    positions, and q/k byte-overlap rejection.
    """
    # Production template — the staged kernel is only built/validated for this config.
    if head_dim != 128 or rope_dim != 128 or is_neox:
        return False
    if q.dim() != 3:
        return False
    if not _is_captured_large(q.size(0), q.size(1), eps):
        return False
    # Device + dtype contract.
    if q.device.type != "cuda":
        return False
    dev = q.device
    if (k.device != dev or q_weight.device != dev or k_weight.device != dev
            or cos_sin_cache.device != dev or positions.device != dev):
        return False
    if q.dtype is not torch.bfloat16 or k.dtype is not torch.bfloat16:
        return False
    if q_weight.dtype is not torch.bfloat16 or k_weight.dtype is not torch.bfloat16:
        return False
    if cos_sin_cache.dtype is not torch.float32 or positions.dtype is not torch.int64:
        return False
    # Ranks / shapes — wrong-shaped tensors must fall back, not raise inside TensorMatcher.
    if k.shape != q.shape or q.size(-1) != head_dim:
        return False
    if q_weight.dim() != 1 or q_weight.numel() != head_dim:
        return False
    if k_weight.dim() != 1 or k_weight.numel() != head_dim:
        return False
    if cos_sin_cache.dim() != 2 or cos_sin_cache.size(-1) != rope_dim:
        return False
    if positions.dim() != 1 or positions.size(0) != q.size(0):
        return False
    # Contiguity — every tensor the kernel indexes must be contiguous.
    if not (q.is_contiguous() and k.is_contiguous() and q_weight.is_contiguous()
            and k_weight.is_contiguous() and cos_sin_cache.is_contiguous()
            and positions.is_contiguous()):
        return False
    # q/k and the weights are read via AlignedVector (up to 16-byte loads), so all four must
    # be 16-byte aligned; contiguous-but-offset views (e.g. base[1:]) fall back. cos_sin_cache
    # is read scalar via __ldg(float*) and positions are scalar, so natural alignment suffices.
    if (q.data_ptr() % 16) or (k.data_ptr() % 16) or (q_weight.data_ptr() % 16) or (k_weight.data_ptr() % 16):
        return False
    if _overlaps(q, k):  # aliased OR overlapping q/k views -> in-place write order undefined.
        return False
    return True


# --------------------------------------------------------------------------------------
# PyTorch FP32 semantic reference (never-recurses fallback safety net)
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
    """Device/dtype/layout-agnostic FP32 reference; writes the fused result into q and k.
    Used only as a never-recurses safety net when no real SGLang baseline is available."""
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
# Recursion-safe baseline resolution
# --------------------------------------------------------------------------------------
def _resolve_fast_baseline() -> Optional[Callable[..., None]]:
    """Return the original SGLang fast baseline if it is safe to call (i.e. not this
    wrapper / not the installed KDA dispatcher). Returns None to force the PyTorch
    semantic reference, which never recurses."""
    fn = _SGLANG_BASELINE_AT_IMPORT
    if fn is None:
        return None
    if fn is optimized_wrapper or fn is fused_inplace_qknorm_rope:
        return None
    if getattr(fn, "__module__", "").startswith("kda_kernels.diffusion.qknorm_rope"):
        return None
    return fn


# --------------------------------------------------------------------------------------
# Native-CUDA candidate (built via SGLang jit_kernel / tvm-ffi)
# --------------------------------------------------------------------------------------
@cache_once
def _candidate_module(head_dim: int, rope_dim: int, is_neox: bool, dtype: torch.dtype,
                      kernel_class: str = "QKNormRopeStagedKernel",
                      use_pdl: bool | None = None):
    """Build the workspace-owned .cuh through SGLang load_jit without touching the SGLang tree.

    load_jit resolves cuda_files as ``(KERNEL_PATH/"csrc"/f).resolve()`` and emits
    ``#include "<resolved-path>"``, so a ``../``-relative path that resolves back to the
    task-owned source compiles it in place; sgl_kernel headers come from DEFAULT_INCLUDE.
    Compile flags match the diffusion baseline (no ``--use_fast_math``). ``kernel_class``
    selects the device kernel: the production path uses ``QKNormRopeStagedKernel``; the
    device-fair fairness sanity may request the warp-per-(token,head) ``QKNormRopeKernel``.
    ``use_pdl=None`` keeps the production arch default (PDL on for B200); an explicit bool
    builds the PDL-on/off variant for A/B diagnostics only — the dispatch path never sets it.
    """
    from sglang.jit_kernel.utils import (
        KERNEL_PATH,
        is_arch_support_pdl,
        load_jit,
        make_cpp_args,
    )

    if not _SRC_CUH.exists():
        raise FileNotFoundError(f"candidate kernel source missing: {_SRC_CUH}")
    rel = os.path.relpath(_SRC_CUH.resolve(), Path(KERNEL_PATH) / "csrc")
    # The .cuh is pulled in via #include, so fold its content hash into the JIT cache marker
    # to force a rebuild whenever the source changes (load_jit keys its cache on *args).
    sha = hashlib.sha256(_SRC_CUH.read_bytes()).hexdigest()[:12]
    # Opt-in -lineinfo build (KDA_LINEINFO=1) for Nsight Compute SASS->source mapping; kept
    # as a separate cache marker so it never pollutes the timed/benchmark build.
    lineinfo = os.environ.get("KDA_LINEINFO") == "1"
    tag = {"QKNormRopeStagedKernel": "staged", "QKNormRopeKernel": "warp"}.get(kernel_class, "staged")
    pdl = is_arch_support_pdl() if use_pdl is None else bool(use_pdl)
    marker = (f"qknorm_rope_kda_b200_{tag}_{sha}"
              + ("" if pdl else "_nopdl") + ("_li" if lineinfo else ""))
    args = make_cpp_args(head_dim, rope_dim, is_neox, pdl, dtype)
    return load_jit(
        marker,
        *args,
        cuda_files=[rel],
        cuda_wrappers=[("qknorm_rope", f"{kernel_class}<{args}>::run")],
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
            is_neox=is_neox, eps=eps, head_dim=head_dim, rope_dim=rope_dim,
        ):
            module = _candidate_module(head_dim, rope_dim, is_neox, q.dtype)
            module.qknorm_rope(q, k, q_weight, k_weight, cos_sin_cache, positions, eps)
            _set_last_dispatch("cuda")
            return None
        # Fallback: prefer the captured fast SGLang baseline (the small captured rows want
        # the proven CUDA baseline, not a slow PyTorch path); the semantic reference is the
        # never-recurses safety net when no real baseline is resolvable.
        delegate = BASELINE_DELEGATE or _resolve_fast_baseline()
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


# Public alias under SGLang's callable name, kept for ABI parity with the public op:
# task harnesses and tests import this module's ``fused_inplace_qknorm_rope`` by name.
# ``optimized_wrapper`` already mirrors the exact SGLang signature, so this is a straight
# alias (same in-place contract, same re-entrancy guard, same dispatch/fallback behavior).
fused_inplace_qknorm_rope = optimized_wrapper
