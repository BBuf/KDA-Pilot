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
def _fp4_gemm(kw: dict) -> dict:
    """Two scalars the shape capture cannot see, and the orientation mm_fp4 wants.

    `fp4_gemm(input, weight, input_sf, weight_sf, alpha, out_dtype, out_features)`
    takes its output dtype and width as plain values, so a shape-only row arrives
    without them: `sglang::fp4_gemm() is missing value for argument 'out_dtype'`.
    Both are recoverable here - the width is the weight's N, and every row in this
    capture records a bf16 output.

    The production call site (`modelopt_quant.py`, the `enable_flashinfer_fp4_gemm`
    branch) then hands `mm_fp4` `layer.weight.T` and
    `layer.weight_scale_interleaved.T`: transposed *views* of the stored `[N, K/2]`
    tensors, so the kernel sees `[K/2, N]` with stride `[1, K/2]`. That stride is
    load-bearing - a contiguous `[K/2, N]` copy has stride `[N, 1]` and the CuTe
    wrapper rejects it with "Mismatched mB.strides[1] ... expected to be 1". Take
    the view.
    """
    import torch

    for name in ("alpha", "global_scale", "a_global_sf"):
        value = kw.get(name)
        if torch.is_tensor(value) and value.is_floating_point():
            value.abs_().clamp_(min=1e-4)
    kw.setdefault("out_dtype", torch.bfloat16)
    kw.setdefault("out_features", int(kw["weight"].shape[0]))
    kw["weight"] = kw["weight"].t()
    kw["weight_sf"] = kw["weight_sf"].t()
    return kw


def _quantize(kw: dict) -> dict:
    """Positive global scale, and a `mask` that means what the kernel reads it as.

    A global scale is a positive fp32 factor; a negative draw makes the reference
    output meaningless rather than merely different.

    `mask` is the per-batch count of valid rows -- `silu_and_mul_scaled_nvfp4_
    experts_quantize` skips rows past it. A generic integer draw put it far past
    the row count, so rows past `T` were never written and the gate ended up
    comparing uninitialised allocator memory, which differs between two
    allocations: the reference failed its own bit-exact check. The valid count is
    the row's token count, which is `a.shape[-2]`.
    """
    import torch

    for name in ("global_scale", "a_global_sf", "alpha"):
        value = kw.get(name)
        if torch.is_tensor(value) and value.is_floating_point():
            value.abs_().clamp_(min=1e-4)
    mask, a = kw.get("mask"), kw.get("a")
    if torch.is_tensor(mask) and torch.is_tensor(a):
        mask.fill_(int(a.shape[-2] if a.dim() >= 3 else a.shape[0]))
    return kw


RECONSTRUCT = {
    "qwen38_fp4_gemm": _fp4_gemm,
    "qwen38_fp4_quantize": _quantize,
    "qwen38_silu_fp4_quantize": _quantize,
}
