"""Registration for the b200_diffusion_qknorm_rope__multi_shape KDA task.

``optimized_wrapper`` preserves the SGLang ``fused_inplace_qknorm_rope`` callsite
contract exactly (positional ``q, k, q_weight, k_weight, cos_sin_cache,
positions``; keyword-only ``is_neox``, ``eps``, ``head_dim``, ``rope_dim``;
returns ``None`` and mutates ``q`` and ``k`` in place).

For the production config (head_dim=128, rope_dim=128, is_neox=False, bf16) it
builds and calls a WORKSPACE-OWNED native CUDA kernel
(``src/qknorm_rope_candidate.cuh``) through SGLang's own jit_kernel/tvm-ffi stack
(``load_jit`` + ``make_cpp_args``), with compile flags matching the diffusion
baseline (no ``--use_fast_math``; no ``torch.utils.cpp_extension``). Any other
signature falls back to the SGLang baseline.

``qknorm_rope_candidate.cuh`` is currently a faithful port of the SGLang baseline
``csrc/diffusion/qknorm_rope.cuh`` (source lineage recorded in solutions.jsonl /
interface.md); it is the validated build-path substrate for subsequent device
optimizations. ``KDA_CAND_PDL`` (``0``/``1``) overrides the PDL template flag for
the PDL on/off A/B (default = the baseline's ``is_arch_support_pdl()``).
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

# Memoize the JIT module per (head_dim, rope_dim, is_neox, use_pdl, dtype),
# mirroring SGLang's cache_once semantics without importing sglang at module load
# (so register()/import stays usable on a CPU-only box).
_module_cache: dict = {}
_baseline_callable: Optional[Callable[..., None]] = None


def _sglang_baseline() -> Callable[..., None]:
    global _baseline_callable
    if _baseline_callable is None:
        from sglang.jit_kernel.diffusion.qknorm_rope import fused_inplace_qknorm_rope

        _baseline_callable = fused_inplace_qknorm_rope
    return _baseline_callable


def _candidate_use_pdl() -> bool:
    env = os.environ.get("KDA_CAND_PDL")
    if env is not None:
        return env == "1"
    from sglang.jit_kernel.utils import is_arch_support_pdl

    return bool(is_arch_support_pdl())


def _candidate_module(head_dim: int, rope_dim: int, is_neox: bool, use_pdl: bool, dtype: Any):
    key = (head_dim, rope_dim, bool(is_neox), bool(use_pdl), str(dtype))
    module = _module_cache.get(key)
    if module is None:
        from sglang.jit_kernel.utils import load_jit, make_cpp_args

        args = make_cpp_args(head_dim, rope_dim, is_neox, use_pdl, dtype)
        module = load_jit(
            "qknorm_rope_cand",
            *args,
            cuda_files=[_CANDIDATE_CUH],
            cuda_wrappers=[("qknorm_rope", f"QKNormRopeKernel<{args}>::run")],
        )
        _module_cache[key] = module
    return module


def _is_production_config(head_dim: int, rope_dim: int, is_neox: bool, dtype: Any) -> bool:
    import torch

    return head_dim == 128 and rope_dim == 128 and not is_neox and dtype == torch.bfloat16


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
    if _is_production_config(hd, rd, is_neox, q.dtype):
        module = _candidate_module(hd, rd, is_neox, _candidate_use_pdl(), q.dtype)
        return module.qknorm_rope(q, k, q_weight, k_weight, cos_sin_cache, positions, eps)
    # Unsupported signature -> SGLang baseline (correctness-or-fallback).
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
