"""Baseline wrapper for `qwen38_nvfp4__fp4_w4a4_skinny_gemm`.

OPS keys match bench/workloads.json. Weights/weight scales are metadata_only in
the payloads: reconstruct once in RECONSTRUCT from the recorded shapes (random
e2m1 bytes + e4m3 block scales are a valid stand-in for timing; correctness rows
that ship real tensors pin the quantize ops, and the GEMM is validated against
the baseline itself on identical inputs).
"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "tools"))
from baseline_loader import load  # noqa: E402

COPIED = {"sglang.srt.layers.quantization.modelopt_quant": "srt/layers/quantization/modelopt_quant.py"}

def _sym(module, attr):
    return load(module, attr, __file__, COPIED.get(module, ""))

OPS = {
    "qwen38_fp4_gemm": lambda **kw: _sym("sglang.srt.layers.quantization.modelopt_quant", "fp4_gemm")(**kw),
    "qwen38_fp4_quantize": lambda **kw: _sym("flashinfer", "fp4_quantize")(**kw),
    "qwen38_silu_fp4_quantize": lambda **kw: _sym("flashinfer", "silu_and_mul_scaled_nvfp4_experts_quantize")(**kw),
}
RECONSTRUCT: dict = {}
