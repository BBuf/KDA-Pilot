"""Build the candidate-owned CUTLASS SM120 FP8 contraction."""

from __future__ import annotations

import hashlib
import importlib.util
from pathlib import Path

from torch.utils.cpp_extension import load


_ROOT = Path(__file__).resolve().parent
_FLASHINFER = importlib.util.find_spec("flashinfer")
if _FLASHINFER is None or _FLASHINFER.origin is None:
    raise ImportError("flashinfer's staged CUTLASS headers are required")
_DATA = Path(_FLASHINFER.origin).resolve().parent / "data"
_SOURCES = (_ROOT / "cutlass_fp8.cpp", _ROOT / "cutlass_fp8_cuda.cu")
_HASH = hashlib.sha256()
for _source in _SOURCES:
    _HASH.update(_source.name.encode())
    _HASH.update(_source.read_bytes())

_extension = load(
    name=f"qwen38_cutlass_fp8_sm120_{_HASH.hexdigest()[:12]}",
    sources=[str(source) for source in _SOURCES],
    extra_include_paths=[
        str(_DATA / "cutlass/include"),
        str(_DATA / "cutlass/tools/util/include"),
    ],
    extra_cflags=["-O3"],
    extra_cuda_cflags=[
        "-O3",
        "-lineinfo",
        "-gencode=arch=compute_120f,code=sm_120f",
        "-DCUTLASS_ENABLE_GDC_FOR_SM100",
        "--expt-relaxed-constexpr",
        "-static-global-template-stub=false",
        "-U__CUDA_NO_HALF_OPERATORS__",
        "-U__CUDA_NO_HALF_CONVERSIONS__",
        "-U__CUDA_NO_BFLOAT16_CONVERSIONS__",
        "-U__CUDA_NO_HALF2_OPERATORS__",
    ],
)

fp8_m1 = _extension.fp8_m1
fp8_m9 = _extension.fp8_m9
