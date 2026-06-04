"""Hermetic loader for the copied SGLang baseline kernel (loop-time A/B lane).

Builds ``baseline/qknorm_rope_baseline.cuh`` — a byte-verbatim copy of SGLang's
``python/sglang/jit_kernel/csrc/diffusion/qknorm_rope.cuh`` (provenance in
``docs/baseline_source.md``) — through the exact same ``load_jit`` entry ABI the
candidate uses in ``src/wrapper.py``. This gives the device-fair A/B two sides that
traverse IDENTICAL wrapper layers (direct JIT module calls, same flags, same include
roots) while leaving every SGLang checkout untouched at benchmark/correctness runtime.

The exported symbol matches the candidate module's: ``module.qknorm_rope(q, k, q_weight,
k_weight, cos_sin_cache, positions, eps)``, launched by ``QKNormRopeKernel<...>::run``
(the upstream warp-per-(token, head) kernel — this copy contains no staged variant).
Compile flags come from SGLang's jit defaults (no ``--use_fast_math``); ``KDA_LINEINFO=1``
opts into a separate ``-lineinfo`` profiling build, mirroring the candidate loader.
"""

from __future__ import annotations

import functools
import hashlib
import os
from pathlib import Path

import torch

try:  # SGLang's manual cache (identical to the candidate wrapper's fallback shim).
    from sglang.jit_kernel.utils import cache_once
except Exception:  # pragma: no cover - sglang not importable in CPU-only environments

    def cache_once(fn):
        return functools.lru_cache(maxsize=None)(fn)


_BASELINE_DIR = Path(__file__).resolve().parent
_BASELINE_CUH = _BASELINE_DIR / "qknorm_rope_baseline.cuh"


@cache_once
def baseline_module(head_dim: int, rope_dim: int, is_neox: bool, dtype: torch.dtype,
                    use_pdl: bool | None = None):
    """Build the copied baseline .cuh via SGLang load_jit (same mechanism as the candidate).

    load_jit resolves cuda_files as ``(KERNEL_PATH/"csrc"/f).resolve()`` and emits
    ``#include "<resolved-path>"``, so a ``../``-relative path that resolves back to this
    task-owned copy compiles it in place; sgl_kernel headers come from DEFAULT_INCLUDE.
    The content hash in the cache marker forces a rebuild whenever the copy is re-synced.
    ``use_pdl=None`` keeps the production arch default (PDL on for B200); an explicit
    bool builds the PDL-on/off variant for A/B diagnostics.
    """
    from sglang.jit_kernel.utils import (
        KERNEL_PATH,
        is_arch_support_pdl,
        load_jit,
        make_cpp_args,
    )

    if not _BASELINE_CUH.exists():
        raise FileNotFoundError(f"baseline kernel copy missing: {_BASELINE_CUH}")
    rel = os.path.relpath(_BASELINE_CUH.resolve(), Path(KERNEL_PATH) / "csrc")
    sha = hashlib.sha256(_BASELINE_CUH.read_bytes()).hexdigest()[:12]
    lineinfo = os.environ.get("KDA_LINEINFO") == "1"
    pdl = is_arch_support_pdl() if use_pdl is None else bool(use_pdl)
    marker = (f"qknorm_rope_kda_b200_baselinecopy_{sha}"
              + ("" if pdl else "_nopdl") + ("_li" if lineinfo else ""))
    args = make_cpp_args(head_dim, rope_dim, is_neox, pdl, dtype)
    return load_jit(
        marker,
        *args,
        cuda_files=[rel],
        cuda_wrappers=[("qknorm_rope", f"QKNormRopeKernel<{args}>::run")],
        extra_include_paths=[str(_BASELINE_DIR)],
        extra_cuda_cflags=["-lineinfo"] if lineinfo else None,
    )


def baseline_inplace_qknorm_rope(
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
    """Public-signature convenience wrapper over the copied baseline (harness symmetry)."""
    head_dim = head_dim or q.size(-1)
    rope_dim = rope_dim or cos_sin_cache.size(-1)
    module = baseline_module(head_dim, rope_dim, is_neox, q.dtype)
    module.qknorm_rope(q, k, q_weight, k_weight, cos_sin_cache, positions, eps)
