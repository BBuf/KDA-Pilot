"""Registration for the b200_diffusion_qknorm_rope__multi_shape KDA task.

``optimized_wrapper`` preserves the SGLang ``fused_inplace_qknorm_rope`` callsite
contract exactly (positional ``q, k, q_weight, k_weight, cos_sin_cache,
positions``; keyword-only ``is_neox``, ``eps``, ``head_dim``, ``rope_dim``;
returns ``None`` and mutates ``q`` and ``k`` in place).

For the production config (head_dim=128, rope_dim=128, is_neox=False, bf16) it
builds and calls a WORKSPACE-OWNED native CUDA kernel
(``src/qknorm_rope_candidate.cuh``) through SGLang's own jit_kernel/tvm-ffi stack
(``load_jit`` + ``make_cpp_args`` + ``cache_once``), with compile flags matching
the diffusion baseline (no ``--use_fast_math``; no ``torch.utils.cpp_extension``).
Any other signature falls back to the SGLang baseline.

The `.cuh` defines two kernels: ``QKNormRopeKernel`` (warp-per-(token,head), a faithful
port of the SGLang baseline) and ``QKNormRopeStagedKernel`` (CTA-per-token with the
cos/sin row staged once into shared memory and reused across the token's heads — the
large-shape device lever). The registered public callable is an exact-shape, fail-closed
dispatcher: it uses the staged kernel only for the captured large production shapes and
falls back to the SGLang baseline for everything else. It reads no environment variables;
call-invariant values (torch handle, PDL mode) are resolved once and cached.
"""

from __future__ import annotations

from pathlib import Path
from typing import Any, Callable, Optional


KERNEL_SLUG = "b200_diffusion_qknorm_rope__multi_shape"
OP_TYPE = "qknorm_rope_inplace"

# Absolute path so SGLang load_jit (which joins under csrc/) resolves to the
# workspace .cuh: pathlib resets the join on an absolute right-hand operand.
_CANDIDATE_CUH = str(Path(__file__).resolve().parent / "qknorm_rope_candidate.cuh")

_KERNEL_CLASS = {"warp": "QKNormRopeKernel", "staged": "QKNormRopeStagedKernel"}

# Lazily-resolved, call-invariant handles (resolved once, then reused).
_torch = None
_baseline_callable: Optional[Callable[..., None]] = None
_use_pdl_cached: Optional[bool] = None
_module_loader: Optional[Callable[..., Any]] = None


def _torch_mod():
    global _torch
    if _torch is None:
        import torch

        _torch = torch
    return _torch


def _sglang_baseline() -> Callable[..., None]:
    global _baseline_callable
    if _baseline_callable is None:
        from sglang.jit_kernel.diffusion.qknorm_rope import fused_inplace_qknorm_rope

        _baseline_callable = fused_inplace_qknorm_rope
    return _baseline_callable


def _use_pdl() -> bool:
    global _use_pdl_cached
    if _use_pdl_cached is None:
        from sglang.jit_kernel.utils import is_arch_support_pdl

        _use_pdl_cached = bool(is_arch_support_pdl())
    return _use_pdl_cached


def _get_module_loader():
    """Return a cache_once-memoized loader (SGLang's own memoization)."""
    global _module_loader
    if _module_loader is None:
        from sglang.jit_kernel.utils import cache_once, load_jit, make_cpp_args

        @cache_once
        def _load(head_dim, rope_dim, is_neox, use_pdl, dtype, variant):
            args = make_cpp_args(head_dim, rope_dim, is_neox, use_pdl, dtype)
            kernel_class = _KERNEL_CLASS[variant]
            return load_jit(
                f"qknorm_rope_cand_{variant}",
                *args,
                cuda_files=[_CANDIDATE_CUH],
                cuda_wrappers=[("qknorm_rope", f"{kernel_class}<{args}>::run")],
            )

        _module_loader = _load
    return _module_loader


# Exact captured production shapes (num_tokens, num_heads). The CTA-per-token staging
# kernel wins ONLY on the large bucket (device-fair 1.10-1.26x; NCU long_scoreboard
# 11.9->9.29). The staged kernel fires only for these exact large rows; the small rows
# and any non-captured / non-production / non-contiguous signature route to the proven
# SGLang baseline (fail-closed). The public callable reads no environment variables.
_STAGED_ROWS = frozenset({(7904, 32), (4096, 24), (8424, 24), (4096, 30), (4128, 30)})
_BASELINE_ROWS = frozenset({(19, 24), (47, 24), (195, 24), (189, 24), (32, 30)})


def _use_staged(num_tokens: int, num_heads: int, head_dim: int, rope_dim: int, is_neox: bool) -> bool:
    """True only for the exact large captured production shapes."""
    return (
        head_dim == 128
        and rope_dim == 128
        and not is_neox
        and (num_tokens, num_heads) in _STAGED_ROWS
    )


def _should_dispatch_staged(q, k, q_weight, k_weight, cos_sin_cache, positions, is_neox, hd, rd) -> bool:
    """Full fail-closed gate: exact large captured shape AND the production dtype/layout
    contract. Anything else returns False (-> SGLang baseline fallback)."""
    t = _torch_mod()
    return (
        _use_staged(q.size(0), q.size(1), hd, rd, is_neox)
        and q.dtype == t.bfloat16
        and k.dtype == t.bfloat16
        and q_weight.dtype == t.bfloat16
        and k_weight.dtype == t.bfloat16
        and cos_sin_cache.dtype == t.float32
        and positions.dtype == t.int64
        and q.is_contiguous()
        and k.is_contiguous()
    )


def optimized_wrapper(
    q: Any,
    k: Any,
    q_weight: Any,
    k_weight: Any,
    cos_sin_cache: Any,
    positions: Any,
    *,
    is_neox: bool,
    eps: float = 1e-6,
    head_dim: int = 0,
    rope_dim: int = 0,
) -> None:
    hd = head_dim or q.size(-1)
    rd = rope_dim or cos_sin_cache.size(-1)
    if _should_dispatch_staged(q, k, q_weight, k_weight, cos_sin_cache, positions, is_neox, hd, rd):
        module = _get_module_loader()(hd, rd, is_neox, _use_pdl(), q.dtype, "staged")
        return module.qknorm_rope(q, k, q_weight, k_weight, cos_sin_cache, positions, eps)
    # Everything else (small bucket, non-captured shape, non-production config, or
    # non-contiguous layout) falls back to the SGLang baseline BEFORE the C++ matcher.
    return _sglang_baseline()(
        q,
        k,
        q_weight,
        k_weight,
        cos_sin_cache,
        positions,
        is_neox=is_neox,
        eps=eps,
        head_dim=head_dim,
        rope_dim=rope_dim,
    )


def register() -> dict[str, Any]:
    return {
        "name": KERNEL_SLUG,
        "op_type": OP_TYPE,
        "callable": optimized_wrapper,
        "version": "dev",
        "source": __file__,
    }
