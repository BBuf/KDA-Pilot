"""Standalone build + dispatch for the GroupNorm+SiLU candidate kernel.

Builds ``solution/kernel.cu`` with ``tvm_ffi.cpp.load`` (no SGLang import) and
exposes ``group_norm_silu_candidate`` with the task benchmark ABI:

    group_norm_silu_candidate(x, weight, bias, num_groups, eps, out) -> out

The exported CUDA symbol handles fp16/bf16/fp32, 2..5-D inputs (contiguous or
strided), and writes a contiguous output (same as the upstream baseline's
return layout). Inputs outside the supported envelope fall back to the copied
local baseline (baseline-equivalent path) so every workload row remains
correct; the dispatch decision is exposed via ``select_path`` for reporting.
"""

from __future__ import annotations

import functools
import os
import sys
from pathlib import Path

import torch

SOLUTION_DIR = Path(__file__).resolve().parent
TASK_DIR = SOLUTION_DIR.parent
BUILD_DIR = SOLUTION_DIR / ".build"

_SUPPORTED_DTYPES = (torch.float16, torch.bfloat16, torch.float32)

# Contiguous rows with group_size above this floor route to the
# baseline-equivalent path. Evidence (docs/dispatch.md): after three
# NCU-driven optimization rounds (chunk-constant affine, baseline-class exp,
# persistent scratch + generation counters) and a GNS_CHUNK sweep
# (8K/16K/32K/64K/128K), the split path still measured 0.93-0.96x against the
# upstream chunked pipeline on contiguous groups >= ~2.4M elements, while
# contiguous groups <= ~1.7M win 1.1-4.2x. The no-regression promotion gate
# (no production row < 0.97x) routes the losing bucket per user ruling DEC-3.
_CONT_FALLBACK_MIN = int(os.environ.get("GNS_CONT_FALLBACK_MIN", 2_000_000))


def _torch_build_flags() -> tuple[list[str], list[str]]:
    """Include and linker flags so the kernel can use ATen's current stream."""
    from torch.utils import cpp_extension as tce

    includes = list(tce.include_paths())
    ldflags = [f"-L{p}" for p in tce.library_paths()]
    ldflags += ["-ltorch", "-ltorch_cpu", "-ltorch_cuda", "-lc10", "-lc10_cuda"]
    return includes, ldflags


def _arch_flag() -> str:
    major, minor = torch.cuda.get_device_capability()
    return f"-gencode=arch=compute_{major}{minor},code=sm_{major}{minor}"


@functools.lru_cache(maxsize=1)
def _module():
    from tvm_ffi.cpp import load

    include_paths, ldflags = _torch_build_flags()
    BUILD_DIR.mkdir(parents=True, exist_ok=True)
    return load(
        "group_norm_silu_candidate",
        cuda_files=[str(SOLUTION_DIR / "kernel.cu")],
        extra_cflags=["-std=c++20", "-O3"],
        extra_cuda_cflags=[
            _arch_flag(),
            "-std=c++20",
            "-O3",
            "--expt-relaxed-constexpr",
            "-lineinfo",  # SASS<->source mapping for NCU; does not change codegen
        ],
        extra_ldflags=ldflags,
        extra_include_paths=include_paths,
        build_directory=str(BUILD_DIR),
    )


@functools.lru_cache(maxsize=1)
def _kernel_fn():
    mod = _module()
    fn = getattr(mod, "group_norm_silu", None)
    if fn is None:
        fn = mod["group_norm_silu"]
    return fn


@functools.lru_cache(maxsize=1)
def _baseline_fallback():
    # Resolved once per process: routed rows must not pay per-call import /
    # sys.path overhead (measured ~3-6 us, i.e. 4-5% on ~100 us rows).
    if str(TASK_DIR) not in sys.path:
        sys.path.insert(0, str(TASK_DIR))
    from baseline import group_norm_silu_baseline

    return group_norm_silu_baseline


def select_path(
    x: torch.Tensor,
    weight: torch.Tensor,
    bias: torch.Tensor,
    num_groups: int,
) -> str:
    """Pure dispatch decision, reused for per-row reporting."""
    if (
        x.is_cuda
        and not torch.is_grad_enabled()
        and not x.requires_grad
        and x.dtype in _SUPPORTED_DTYPES
        and 2 <= x.dim() <= 5
        and num_groups > 0
        and x.shape[1] % num_groups == 0
        and weight.is_cuda
        and bias.is_cuda
        and weight.dtype == x.dtype
        and bias.dtype == x.dtype
        and weight.dim() == 1
        and bias.dim() == 1
        and weight.shape == bias.shape == (x.shape[1],)
    ):
        spatial = 1
        for s in x.shape[2:]:
            spatial *= int(s)
        group_size = (int(x.shape[1]) // int(num_groups)) * spatial
        if x.is_contiguous() and group_size > _CONT_FALLBACK_MIN:
            return "baseline_fallback"
        return "cuda_kernel"
    return "baseline_fallback"


def group_norm_silu_candidate(
    x: torch.Tensor,
    weight: torch.Tensor,
    bias: torch.Tensor,
    num_groups: int,
    eps: float,
    out: torch.Tensor,
) -> torch.Tensor:
    if select_path(x, weight, bias, num_groups) == "cuda_kernel":
        _kernel_fn()(x, weight, bias, int(num_groups), float(eps), out)
        return out
    return _baseline_fallback()(x, weight, bias, num_groups, eps, out)


_REGIME_NAMES = {0: "generic", 1: "cont_small", 2: "cont_split", 3: "nchw_last"}


def describe_dispatch(
    x: torch.Tensor,
    weight: torch.Tensor,
    bias: torch.Tensor,
    num_groups: int,
    out: torch.Tensor,
) -> dict:
    """Per-row reporting metadata (untimed).

    Single source of truth: ``select_path`` for the Python-level routing and
    the kernel's exported ``group_norm_silu_regime`` helper (the exact C++
    ``select_regime_impl`` the timed call uses) for the CUDA regime. ``out``
    must be the same preallocated output tensor used for timing — the regime
    decision inspects both tensors' geometry/alignment.
    """
    if select_path(x, weight, bias, num_groups) == "baseline_fallback":
        return {
            "candidate_path": "baseline_fallback",
            "candidate_regime": "baseline_fallback",
            "matched_status": "baseline_equivalent",
        }
    mod = _module()
    regime_fn = getattr(mod, "group_norm_silu_regime", None)
    if regime_fn is None:
        regime_fn = mod["group_norm_silu_regime"]
    regime = int(regime_fn(x, weight, bias, int(num_groups), out))
    return {
        "candidate_path": "cuda_kernel",
        "candidate_regime": _REGIME_NAMES.get(regime, f"regime_{regime}"),
        "matched_status": "optimized",
    }


__all__ = ["group_norm_silu_candidate", "select_path", "describe_dispatch"]
