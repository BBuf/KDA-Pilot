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

Kernel variant is chosen by ``KDA_CAND_VARIANT``:
- ``warp`` (default): ``QKNormRopeKernel`` — warp-per-(token,head), a faithful port
  of the SGLang baseline.
- ``staged``: ``QKNormRopeStagedKernel`` — CTA-per-token with cos/sin staged once
  into shared memory and reused across the token's heads (large-shape device lever).

``KDA_CAND_PDL`` (``0``/``1``) overrides the PDL template flag (default = the
baseline's ``is_arch_support_pdl()``). Call-invariant values (torch handle, PDL
mode) are resolved once and cached to keep the per-call path lean.
"""

from __future__ import annotations

import os
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
        env = os.environ.get("KDA_CAND_PDL")
        if env is not None:
            _use_pdl_cached = env == "1"
        else:
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


# Evidence-gated dispatch (Round 5 device-fair + NCU): the CTA-per-token staging kernel
# wins on the large bucket (1.10-1.26x) but not on small shapes (tiny-grid; host-dispatch
# bound). So route the production config by token count; small + everything non-production
# or non-contiguous falls back to the proven SGLang baseline. Production token counts are
# small <=195 and large >=4096, so any threshold in (195, 4096) splits the buckets.
_LARGE_MIN_TOKENS = 512


def _dispatch_variant(num_tokens: int) -> Optional[str]:
    """Choose the candidate variant for the production config, or None -> baseline.

    KDA_CAND_VARIANT (warp|staged) overrides the route for experiments.
    """
    override = os.environ.get("KDA_CAND_VARIANT")
    if override is not None:
        return override
    return "staged" if num_tokens >= _LARGE_MIN_TOKENS else None


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
    is_production = (
        hd == 128
        and rd == 128
        and not is_neox
        and q.dtype == _torch_mod().bfloat16
        and q.is_contiguous()
        and k.is_contiguous()
    )
    if is_production:
        variant = _dispatch_variant(q.size(0))
        if variant is not None:
            module = _get_module_loader()(hd, rd, is_neox, _use_pdl(), q.dtype, variant)
            return module.qknorm_rope(q, k, q_weight, k_weight, cos_sin_cache, positions, eps)
    # Non-production / unsupported layout / small bucket -> SGLang baseline fallback
    # (explicit, before the C++ TensorMatcher).
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
