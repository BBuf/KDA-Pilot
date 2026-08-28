import hashlib
import importlib.util
from pathlib import Path

from torch.utils.cpp_extension import load

_ROOT = Path(__file__).resolve().parent
_FLASHINFER = importlib.util.find_spec("flashinfer")
if _FLASHINFER is None or _FLASHINFER.origin is None:
    raise ImportError("flashinfer source headers are required to build the CUDA extension")
_DATA = Path(_FLASHINFER.origin).resolve().parent / "data"
_CSRC = _DATA / "csrc"
_CCCL = _DATA / "cccl"
_LOCAL_SOURCES = (_ROOT / "fused_quant.cpp", _ROOT / "fused_quant_cuda.cu")
_SOURCE_HASH = hashlib.sha256()
for _source in _LOCAL_SOURCES:
    _SOURCE_HASH.update(_source.name.encode())
    _SOURCE_HASH.update(_source.read_bytes())

_extension = load(
    # The extension cache is shared across reconstructed submissions. Include
    # the candidate-owned source in the key so a same-named stale binary can
    # never mask a CUDA edit or contaminate a recorded benchmark.
    name=f"qwen38_fused_quant_sm120_{_SOURCE_HASH.hexdigest()[:12]}",
    sources=[
        *(str(source) for source in _LOCAL_SOURCES),
        str(_CSRC / "nv_internal/cpp/common/envUtils.cpp"),
        str(_CSRC / "nv_internal/cpp/common/logger.cpp"),
        str(_CSRC / "nv_internal/cpp/common/stringUtils.cpp"),
        str(_CSRC / "nv_internal/cpp/common/tllmException.cpp"),
    ],
    extra_include_paths=[
        str(_CSRC / "nv_internal"),
        str(_CSRC / "nv_internal/include"),
        str(_CCCL / "cub"),
        str(_CCCL / "libcudacxx/include"),
        str(_CCCL / "thrust"),
        str(_DATA / "include"),
        str(_CSRC),
        str(_DATA / "cutlass/include"),
        str(_DATA / "cutlass/tools/util/include"),
    ],
    extra_cflags=["-O3", "-DENABLE_BF16", "-DENABLE_FP8", "-DENABLE_FP4"],
    extra_cuda_cflags=[
        "-O3",
        "-lineinfo",
        "-gencode=arch=compute_120f,code=sm_120f",
        "--expt-relaxed-constexpr",
        "-static-global-template-stub=false",
        "-use_fast_math",
        "-U__CUDA_NO_HALF_OPERATORS__",
        "-U__CUDA_NO_HALF_CONVERSIONS__",
        "-U__CUDA_NO_BFLOAT16_CONVERSIONS__",
        "-U__CUDA_NO_HALF2_OPERATORS__",
        "-DENABLE_BF16",
        "-DENABLE_FP8",
        "-DENABLE_FP4",
        "-DFLASHINFER_ENABLE_FP4_E2M1",
    ],
)

fused_quant = _extension.fused_quant
small_quant = _extension.small_quant
silu_small = _extension.silu_small
silu_swizzled_4096 = _extension.silu_swizzled_4096
silu_swizzled_half8_4096 = _extension.silu_swizzled_half8_4096
silu_swizzled_4369 = _extension.silu_swizzled_4369
reduce_down_split = _extension.reduce_down_split
