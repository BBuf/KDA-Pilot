"""Build the candidate-owned SM120 CUDA kernels."""

from __future__ import annotations

import hashlib
from pathlib import Path

from torch.utils.cpp_extension import load


_ROOT = Path(__file__).resolve().parent
_SOURCES = (_ROOT / "fp8_ext.cpp", _ROOT / "fp8_ext_cuda.cu")
_HASH = hashlib.sha256()
for _source in _SOURCES:
    _HASH.update(_source.name.encode())
    _HASH.update(_source.read_bytes())

_extension = load(
    name=f"qwen38_fp8_skinny_sm120_{_HASH.hexdigest()[:12]}",
    sources=[str(source) for source in _SOURCES],
    extra_cflags=["-O3"],
    extra_cuda_cflags=[
        "-O3",
        "-lineinfo",
        "-gencode=arch=compute_120f,code=sm_120f",
        "--expt-relaxed-constexpr",
        "-static-global-template-stub=false",
        "-use_fast_math",
        "-U__CUDA_NO_BFLOAT16_CONVERSIONS__",
    ],
)

fp8_gemv = _extension.fp8_gemv
fp8_linear = _extension.fp8_linear
fp8_quantize = _extension.fp8_quantize
