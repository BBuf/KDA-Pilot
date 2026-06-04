"""Registration entry point for the h200_diffusion_cutedsl_norm_tanh_mul_add
KDA task. Lazily loads the candidate wrapper (which JIT-compiles the native
CUDA fast path through SGLang's jit_kernel stack on first use)."""

from __future__ import annotations

import importlib.util
from pathlib import Path
from typing import Any


KERNEL_SLUG = "h200_diffusion_cutedsl_norm_tanh_mul_add__multi_shape"
OP_TYPE = "cutedsl_norm_tanh_mul_add"

# Flipped to True once the native CUDA candidate is wired in. The correctness
# harness skips candidate tests while this is False.
CANDIDATE_READY = True

_IMPL = None


def _load_impl():
    global _IMPL
    if _IMPL is None:
        wrapper_py = Path(__file__).resolve().parent / "wrapper.py"
        spec = importlib.util.spec_from_file_location(
            f"kda_kernel_{KERNEL_SLUG}_wrapper", wrapper_py
        )
        assert spec is not None and spec.loader is not None, wrapper_py
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        _IMPL = module
    return _IMPL


def optimized_wrapper(*args: Any, **kwargs: Any) -> Any:
    return _load_impl().optimized_wrapper(*args, **kwargs)


def dispatch_decision(*args: Any, **kwargs: Any) -> str:
    """Expose the wrapper's routing decision (fast_single | fast_dual |
    fallback_single | fallback_dual) for branch-contract tests."""

    return _load_impl().dispatch_decision(*args, **kwargs)


def register() -> dict[str, Any]:
    return {
        "name": KERNEL_SLUG,
        "op_type": OP_TYPE,
        "callable": optimized_wrapper,
        "version": "dev",
        "source": __file__,
    }


EXPORTS = {
    "fused_norm_tanh_mul_add": optimized_wrapper,
    "fused_norm_tanh_mul_add_norm_scale": optimized_wrapper,
}
