"""Baseline wrapper for `qwen38_nvfp4__fp8_verify_skinny_gemm`."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "tools"))
from baseline_loader import load  # noqa: E402

COPIED = {
    "sglang.kernels.ops.gemm.sm120_fp8_gemv": "kernels/ops/gemm/sm120_fp8_gemv.py",
    "sglang.srt.layers.quantization.fp8_utils": "srt/layers/quantization/fp8_utils.py",
}

def _sym(module, attr):
    return load(module, attr, __file__, COPIED.get(module, ""))

OPS = {
    "qwen38_fp8_gemv": lambda **kw: _sym("sglang.kernels.ops.gemm.sm120_fp8_gemv", "sm120_fp8_gemv")(**kw),
    "qwen38_fp8_linear": lambda **kw: _sym("sglang.srt.layers.quantization.fp8_utils", "apply_fp8_linear")(**kw),
}
RECONSTRUCT: dict = {}
