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
def _fp8_gemv(kw: dict) -> dict:
    """Re-orient the weight for the raw GEMV.

    The capture records this projection the way the checkpoint stores it,
    `[in_features, out_features]`, while `sm120_fp8_gemv` verifies its arguments
    against `{N, K}` (`csrc/gemm/sm120_fp8_gemv.cuh`) *and* templates the kernel on
    the `(N, K)` it reads off the weight. Passing the recorded orientation made the
    kernel compile for the transposed shape and then reject the activation - the
    `gdn_in_proj_qkvz` row records `w=[5120, 16384]`, so it expected
    `x={1, 16384}` and got `{1, 5120}`.

    A transposed view satisfies the shape check but not the kernel's contiguity
    assumption, so the bytes are laid out contiguously in `[N, K]`. That is a copy
    per row build; `apply_fp8_linear` consumes the recorded orientation directly,
    which is why only the raw GEMV pays it.
    """
    w = kw["w_fp8"]
    k = int(kw["x_fp8"].shape[-1])
    if w.shape[-1] == k and w.shape[0] != k:
        return kw
    kw["w_fp8"] = w.t().contiguous()
    return kw


def _positive_scales(kw: dict) -> dict:
    """Scales are positive fp32 factors; a random draw straddles zero.

    `alpha`, `weight_scale` and `input_scale` are quantization scales. Drawn from a
    normal distribution they come out negative about half the time, and cuBLASLt
    then refuses the problem outright: `CUBLAS_STATUS_NOT_SUPPORTED when calling
    cublasLtMatmulAlgoGetHeuristic`, which the harness reports as the baseline
    raising. Taking the magnitude keeps the recorded shape and dtype and makes the
    reference meaningful; the row still says nothing about the real magnitudes,
    which is why the payloads pin the ones that matter.
    """
    import torch

    for name in ("alpha", "weight_scale", "input_scale", "x_scale"):
        value = kw.get(name)
        if torch.is_tensor(value) and value.is_floating_point():
            value.abs_().clamp_(min=1e-4)
    return kw


def _fp8_gemv_inputs(kw: dict) -> dict:
    return _fp8_gemv(_positive_scales(kw))


def _fp8_linear_inputs(kw: dict) -> dict:
    """Lay the weight out the way cuBLASLt's FP8 path requires.

    The row records `weight` as `[K, N]`, which is the orientation
    `apply_fp8_linear` wants -- `weight.t()` fails the matmul outright. But an FP8
    cuBLASLt GEMM is TN-only: it needs the operand column-major, and production
    satisfies that implicitly because `layer.weight` is stored `[N, K]` contiguous
    and the call site passes `layer.weight.T`, i.e. `[K, N]` with stride `[1, K]`.
    Allocating `[K, N]` contiguous instead gives stride `[N, 1]`, and cuBLASLt
    rejects the problem before it looks at any data:
    `CUBLAS_STATUS_NOT_SUPPORTED when calling cublasLtMatmulAlgoGetHeuristic`
    (confirmed independent of the values - a clean in-range FP8 weight fails the
    same way).

    `t().contiguous().t()` reproduces production's layout exactly: same shape, same
    logical contents, stride `[1, K]`.
    """
    kw = _positive_scales(kw)
    weight = kw.get("weight")
    if weight is not None and weight.dim() == 2 and weight.is_contiguous():
        kw["weight"] = weight.t().contiguous().t()
    return kw



import sys as _sys, os as _os
_sys.path.insert(0, _os.path.join(_os.path.dirname(_os.path.abspath(__file__)), "..", "..", "tools"))
from derive_inputs import derive as _derive  # noqa: E402  shared address-argument repair


_TASK_FIX = {
    "qwen38_fp8_gemv": _fp8_gemv_inputs,
    "qwen38_fp8_linear": _fp8_linear_inputs,
}


def _repair(op):
    """`derive()` first - it repairs the address-like arguments every row has - then the
    task's own hook for what only this task knows."""
    task_hook = _TASK_FIX.get(op)

    def run(kw):
        kw = _derive(kw)
        return task_hook(kw) if task_hook else kw

    return run


RECONSTRUCT = {op: _repair(op) for op in set(list(_TASK_FIX) + ['qwen38_fp8_gemv', 'qwen38_fp8_linear', 'qwen38_fp8_gemv', 'qwen38_fp8_linear'])}
