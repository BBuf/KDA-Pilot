"""Native-CUDA fused QK-norm + RoPE candidate wrapper (b200, multi-shape).

The public op mirrors ``sglang.jit_kernel.diffusion.qknorm_rope.fused_inplace_qknorm_rope``
exactly: in-place on ``q`` and ``k``, returns ``None``.

**Lean, custom-op-free dispatch.** For any template-supported, contiguous signature this routes
DIRECTLY to one of this project's two workspace-owned CUDA kernels via SGLang
``load_jit`` / tvm-ffi — **without** going through torch ``register_custom_op``:

  - the exact large captured production rows (``head_dim=128, rope_dim=128, is_neox=False``,
    bf16, int64 positions, one of the 5 captured ``(num_tokens, num_heads, eps)``) ->
    ``QKNormRopeStagedKernel`` (CTA-per-token cos/sin staging, the large-shape device win);
  - every other template-supported contiguous signature -> ``QKNormRopeKernel`` (the
    warp-per-(token,head) faithful port; byte-identical to the SGLang baseline, so correct
    across the whole supported template space, but no device speedup).

A minimal guard keeps it safe: only ``_fast_supported(head_dim, rope_dim, is_neox, dtype)``
(cached) + ``q``/``k`` contiguous are checked per call. Anything outside that (non-contiguous,
non-bf16, out-of-template head_dim/rope_dim/neox) takes a **rare fallback** to the captured
original SGLang baseline (or a PyTorch reference) — these never occur for the production shapes
or the SGLang CI grid, so the common path stays a few cheap comparisons.

Why no ``register_custom_op`` on the common path: once ``kda_kernels.install()`` swaps the
public symbol, callers reach this wrapper through a plain generated dispatcher, so routing
straight to the tvm-ffi kernel here genuinely removes the baseline's per-call custom-op
overhead (the small/dispatch-bound shapes win on host time; the large shapes win on host time
AND device time). This is the production-relevant path; validate it on the literal
``kda_kernels.install()`` benchmark, never on a proxy.

Recursion safety on the (rare) fallback: the SGLang baseline is captured at *import* time (the
``install()`` driver calls ``_preload_kda_impls`` to import this module BEFORE monkey-patching
the public symbol), and ``_resolve_fast_baseline`` rejects any callable that is this wrapper or
a ``kda_kernels`` symbol, so the fallback can never recurse into the swapped op.
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


# SGLang baseline captured at IMPORT time. install() preloads this module before swapping
# the public symbol, so this is the ORIGINAL fast CUDA baseline, not the KDA dispatcher.
# Used only by the rare fallback path.
try:
    from sglang.jit_kernel.diffusion.qknorm_rope import (
        fused_inplace_qknorm_rope as _SGLANG_BASELINE_AT_IMPORT,
    )
except Exception:  # pragma: no cover - sglang not importable off-GPU
    _SGLANG_BASELINE_AT_IMPORT = None


_CSRC_DIR = Path(__file__).resolve().parent
_SRC_CUH = _CSRC_DIR / "qknorm_rope_candidate.cuh"  # workspace-owned source of truth

_SUPPORTED_HEAD_DIMS = (64, 128, 256)

# Exact captured production rows -> the eps each was captured with. The staged kernel is trusted
# ONLY on these exact (num_tokens, num_heads, eps) signatures (all head_dim=128, rope_dim=128,
# is_neox=False, bf16, int64 positions). Other shapes use the warp kernel (still correct).
_STAGED_EPS: dict[tuple[int, int], float] = {
    (7904, 32): 1e-6,  # joyai-edit
    (4096, 24): 1e-6,  # qwen
    (8424, 24): 1e-6,  # qwen-edit
    (4096, 30): 1e-5,  # zimage
    (4128, 30): 1e-5,  # zimage
}

_tls = threading.local()

# Optional explicit fallback delegate. Left None by default (the fallback then uses the captured
# fast SGLang baseline, or the PyTorch semantic reference if none is available). The in-overlay
# double-install test may point this at a callable to exercise the recursion guard.
BASELINE_DELEGATE: Optional[Callable[..., None]] = None


def get_last_dispatch() -> Optional[str]:
    """Dispatch path of the most recent call on this thread: ``"staged"`` (large device win),
    ``"warp"`` (faithful port), or ``"fallback"`` (rare baseline route)."""
    return getattr(_tls, "last_dispatch", None)


def _set_last_dispatch(tag: str) -> None:
    _tls.last_dispatch = tag


# --------------------------------------------------------------------------------------
# Lean dispatch gate
# --------------------------------------------------------------------------------------
@functools.lru_cache(maxsize=None)
def _fast_supported(head_dim: int, rope_dim: int, is_neox: bool, dtype: torch.dtype) -> bool:
    """Signature-only eligibility for this project's CUDA kernels (cached, ~0 per-call cost).

    This is the template gate: head_dim in {64,128,256}, bf16, valid rope_dim, and (for neox) a
    power-of-two rotary-lane count. It does NOT depend on per-call tensor state, so the only
    per-call work in the common path is the cache hit + two contiguity checks.
    """
    if head_dim not in _SUPPORTED_HEAD_DIMS or dtype is not torch.bfloat16:
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


def _is_captured_large(num_tokens: int, num_heads: int, eps: float) -> bool:
    """True only for the exact large captured (num_tokens, num_heads, eps) production rows."""
    expected = _STAGED_EPS.get((num_tokens, num_heads))
    return expected is not None and abs(eps - expected) <= 1e-9


def _use_staged(num_tokens, num_heads, head_dim, rope_dim, is_neox, eps, pos_is_int64) -> bool:
    """True only for the exact production-large signature (the NCU-validated staged path):
    captured (tokens, heads, eps) AND head_dim=128, rope_dim=128, is_neox=False, int64 positions.
    Everything else (incl. a captured shape at a different head_dim/dtype/positions) uses warp."""
    return (
        head_dim == 128
        and rope_dim == 128
        and not is_neox
        and pos_is_int64
        and _is_captured_large(num_tokens, num_heads, eps)
    )


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
# Recursion-safe baseline resolution (rare fallback only)
# --------------------------------------------------------------------------------------
def _resolve_fast_baseline() -> Optional[Callable[..., None]]:
    """Return the original SGLang fast baseline if it is safe to call (i.e. not this wrapper /
    not the installed KDA dispatcher). Returns None to force the PyTorch semantic reference,
    which never recurses."""
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
                      kernel_class: str = "QKNormRopeStagedKernel"):
    """Build the workspace-owned .cuh through SGLang load_jit without touching the SGLang tree.

    load_jit resolves cuda_files as ``(KERNEL_PATH/"csrc"/f).resolve()`` and emits
    ``#include "<resolved-path>"``, so a ``../``-relative path that resolves back to the
    task-owned source compiles it in place; sgl_kernel headers come from DEFAULT_INCLUDE.
    Compile flags match the diffusion baseline (no ``--use_fast_math``). ``kernel_class``
    selects the device kernel: ``QKNormRopeStagedKernel`` (production large) or the
    warp-per-(token,head) ``QKNormRopeKernel`` (faithful port for everything else / the
    device-fair fairness sanity).
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
    marker = f"qknorm_rope_kda_b200_{tag}_{sha}" + ("_li" if lineinfo else "")
    args = make_cpp_args(head_dim, rope_dim, is_neox, is_arch_support_pdl(), dtype)
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
    head_dim = head_dim or q.size(-1)
    rope_dim = rope_dim or cos_sin_cache.size(-1)
    # Lean common path: template-supported (cached) + q/k contiguous -> route straight to this
    # project's CUDA kernel via tvm-ffi (NO torch register_custom_op layer).
    if _fast_supported(head_dim, rope_dim, is_neox, q.dtype) and q.is_contiguous() and k.is_contiguous():
        if _use_staged(q.size(0), q.size(1), head_dim, rope_dim, is_neox, eps, positions.dtype == torch.int64):
            kernel_class, tag = "QKNormRopeStagedKernel", "staged"
        else:
            kernel_class, tag = "QKNormRopeKernel", "warp"
        module = _candidate_module(head_dim, rope_dim, is_neox, q.dtype, kernel_class)
        module.qknorm_rope(q, k, q_weight, k_weight, cos_sin_cache, positions, eps)
        _set_last_dispatch(tag)
        return None
    # Rare fallback: non-contiguous / non-bf16 / out-of-template inputs (never produced by the
    # production shapes or the CI grid). Prefer the captured original SGLang baseline (resolved
    # recursion-safe); the PyTorch semantic reference is the never-recurses safety net.
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


# Public alias under SGLang's callable name. The generated kda_kernels overlay dispatcher
# imports this symbol by name (``getattr(<wrapper module>, "fused_inplace_qknorm_rope")``);
# ``optimized_wrapper`` already mirrors the exact SGLang signature, so this is a straight alias.
fused_inplace_qknorm_rope = optimized_wrapper
