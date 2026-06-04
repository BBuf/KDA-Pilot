"""Build glue for the native CUDA kernels.

Uses sglang.jit_kernel.utils (load_jit / make_cpp_args) strictly as a BUILD
utility, with an ABSOLUTE cuda_files path so the workspace .cuh compiles in
place and nothing is written into the SGLang checkout. Compile flags are the
jit_kernel defaults (arch define, -std=c++20, -O3, --expt-relaxed-constexpr;
no --use_fast_math).
"""

from __future__ import annotations

from pathlib import Path

CUH_PATH = str(Path(__file__).resolve().parent / "scale_shift_kda.cuh")

_MODULE_CACHE: dict = {}


def _jit_utils():
    # Imported lazily: build utility only (never the live Triton baselines).
    from sglang.jit_kernel import utils as jit_utils

    return jit_utils


def scale_shift_module(
    dtype_x,
    dtype_scale,
    dtype_shift,
    scale_splat: bool,
    shift_splat: bool,
    frame_mode: bool,
    use_pdl: bool,
):
    key = ("scale_shift", dtype_x, dtype_scale, dtype_shift,
           scale_splat, shift_splat, frame_mode, use_pdl)
    mod = _MODULE_CACHE.get(key)
    if mod is None:
        utils = _jit_utils()
        args = utils.make_cpp_args(
            dtype_x, dtype_scale, dtype_shift, scale_splat, shift_splat,
            frame_mode, use_pdl,
        )
        mod = utils.load_jit(
            "fuse_scale_shift_kda",
            *args,
            cuda_files=[CUH_PATH],
            cuda_wrappers=[("fuse_scale_shift", f"FuseScaleShiftKernel<{args}>::run")],
        )
        _MODULE_CACHE[key] = mod
    return mod


def ln_select01_module(
    dtype_x,
    has_weight: bool,
    has_bias: bool,
    has_residual: bool,
    use_pdl: bool,
):
    key = ("ln_select01", dtype_x, has_weight, has_bias, has_residual, use_pdl)
    mod = _MODULE_CACHE.get(key)
    if mod is None:
        utils = _jit_utils()
        args = utils.make_cpp_args(dtype_x, has_weight, has_bias, has_residual, use_pdl)
        mod = utils.load_jit(
            "fuse_ln_select01_kda",
            *args,
            cuda_files=[CUH_PATH],
            cuda_wrappers=[("fuse_ln_select01", f"FuseLNSelect01Kernel<{args}>::run")],
        )
        _MODULE_CACHE[key] = mod
    return mod
