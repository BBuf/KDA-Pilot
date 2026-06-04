"""Registration stub for the h200_diffusion_cutedsl_norm_tanh_mul_add__multi_shape KDA task.

Agents should replace ``optimized_wrapper`` with the recovered
benchmark-compatible candidate during implementation.
"""

from __future__ import annotations

from typing import Any


KERNEL_SLUG = "h200_diffusion_cutedsl_norm_tanh_mul_add__multi_shape"
OP_TYPE = "cutedsl_norm_tanh_mul_add"

# Flipped to True once the native CUDA candidate is wired in. The correctness
# harness skips candidate tests while this is False.
CANDIDATE_READY = False


def optimized_wrapper(*args: Any, **kwargs: Any) -> Any:
    raise NotImplementedError(
        "Fill optimized_wrapper after recovering the SGLang baseline contract."
    )


def register() -> dict[str, Any]:
    return {
        "name": KERNEL_SLUG,
        "op_type": OP_TYPE,
        "callable": optimized_wrapper,
        "version": "dev",
        "source": __file__,
    }
