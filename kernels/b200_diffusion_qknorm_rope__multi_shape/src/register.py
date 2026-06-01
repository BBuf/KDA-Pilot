"""Registration for the b200_diffusion_qknorm_rope__multi_shape KDA task.

``optimized_wrapper`` preserves the SGLang ``fused_inplace_qknorm_rope`` callsite
contract exactly (positional ``q, k, q_weight, k_weight, cos_sin_cache,
positions``; keyword-only ``is_neox``, ``eps``, ``head_dim``, ``rope_dim``;
returns ``None`` and mutates ``q`` and ``k`` in place).

For now it routes to the SGLang baseline, which is the correct-by-construction
starting point and the fallback target. The specialized B200 kernel will be
wired in behind a shape gate, falling back to this baseline for any signature it
does not support.
"""

from __future__ import annotations

from typing import Any, Callable, Optional


KERNEL_SLUG = "b200_diffusion_qknorm_rope__multi_shape"
OP_TYPE = "qknorm_rope_inplace"

# Resolved once and reused, so the fallback adds no per-call import overhead in
# the small-shape latency path.
_baseline_callable: Optional[Callable[..., None]] = None


def _sglang_baseline() -> Callable[..., None]:
    global _baseline_callable
    if _baseline_callable is None:
        from sglang.jit_kernel.diffusion.qknorm_rope import fused_inplace_qknorm_rope

        _baseline_callable = fused_inplace_qknorm_rope
    return _baseline_callable


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
