"""Build and load the eager baseline CUDA module via tvm-ffi.

Compiles baseline/kernel.cu (a thin ATen-eager wrapper exposed through the same
destination-passing tvm-ffi ABI as the candidate) into a tvm-ffi module exposing
``ltx2_rms_adaln_baseline``. Uses the SAME builder, compile flags, and torch
linkage as solution/build.py so baseline and candidate pay symmetric build /
wrapper overhead (diffusion_kernel_rules: symmetric flags). No ``--use_fast_math``
(the recovered upstream baseline is plain eager and does not use it). No sglang
import.
"""

from __future__ import annotations

import functools
import pathlib

import torch

_BASELINE_DIR = pathlib.Path(__file__).resolve().parent
_KERNEL_CU = _BASELINE_DIR / "kernel.cu"


def _gencode_flag() -> str:
    major, minor = torch.cuda.get_device_capability()
    return f"-gencode=arch=compute_{major}{minor},code=sm_{major}{minor}"


def baseline_compile_flags() -> dict:
    """The exact flag sets used to build the baseline (provenance record)."""
    return {
        "extra_cflags": ["-std=c++17", "-O3"],
        "extra_cuda_cflags": ["-std=c++17", "-O3", _gencode_flag()],
        "ldlibs": ["-lc10", "-lc10_cuda", "-ltorch_cpu", "-ltorch_cuda"],
        "use_fast_math": False,
    }


@functools.lru_cache(maxsize=None)
def load_baseline_module():
    from torch.utils import cpp_extension as torch_cpp
    from tvm_ffi.cpp import load

    include_paths = list(torch_cpp.include_paths(device_type="cuda"))
    library_paths = list(torch_cpp.library_paths(device_type="cuda"))
    flags = baseline_compile_flags()
    ldflags = [f"-L{p}" for p in library_paths]
    ldflags += [f"-Wl,-rpath,{p}" for p in library_paths]
    ldflags += flags["ldlibs"]

    return load(
        "ltx2_rms_adaln_baseline",
        cuda_files=[str(_KERNEL_CU)],
        extra_cflags=flags["extra_cflags"],
        extra_cuda_cflags=flags["extra_cuda_cflags"],
        extra_ldflags=ldflags,
        extra_include_paths=include_paths,
        build_directory=str(_BASELINE_DIR / ".build"),
    )
