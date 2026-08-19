"""Baseline wrapper for `glm45__fp8_fused_moe`.

The harness (`tools/bench_harness.py`) calls `OPS[<op>](**row_args)`. Each entry loads
the symbol from the installed SGLang and checks its source hash against the copy in this
directory, so a drifted environment is reported instead of silently benchmarked - see
`tools/baseline_loader.py`.

Two entry points are timed, because a candidate can replace either level:

* `triton_fused_moe_gemm`  - the expert GEMM itself, in its FP8 arm
  (`use_fp8_w8a8=True`, per-output-channel weight scales, activations quantized per
  token before the tile loop);
* `moe_fused_experts_fp8`  - the whole `fused_experts_impl` dispatch: activation quant,
  up GEMM, SiLU-and-mul, down GEMM and the weighted sum. This is the level the
  production MoE runner calls, and the level at which a fused CUDA implementation can
  remove the intermediate traffic between the two GEMMs.

Write `solution/entry.py` with the same `OPS` keys to have the harness A/B it.
"""

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "tools"))
from baseline_loader import load  # noqa: E402

COPIED = {
    'sglang.kernels.ops.moe.fused_moe_triton_kernels': 'kernels/ops/moe/fused_moe_triton_kernels.py',
    'sglang.kernels.ops.moe.moe_align': 'kernels/ops/moe/moe_align.py',
    'sglang.srt.layers.moe.moe_runner.triton_utils.fused_moe':
        'srt/layers/moe/moe_runner/triton_utils/fused_moe.py',
}


_PUBLISHED = False


def _publish_runtime_config() -> None:
    """`fused_experts_impl` reads the `exec` config namespace, which only exists inside a
    running server ("config namespace 'exec' not published"). Publishing a default
    ServerArgs is the standalone equivalent: it sets no MoE-specific knob, it only makes
    the namespace exist, so the kernel takes exactly the branches it takes in the server.
    """
    global _PUBLISHED
    if _PUBLISHED:
        return
    import dataclasses

    from sglang.srt import runtime_context
    from sglang.srt.server_args import ServerArgs
    if not runtime_context._CONTEXT.is_config_namespace_published("exec"):
        # ServerArgs.__post_init__ resolves the model on the hub, which a kernel benchmark
        # has no business doing; build the dataclass at its declared defaults instead, so
        # every namespace exists with the value the server would use when nothing is set.
        sa = ServerArgs.__new__(ServerArgs)
        for f in dataclasses.fields(ServerArgs):
            if f.default is not dataclasses.MISSING:
                v = f.default
            elif f.default_factory is not dataclasses.MISSING:
                v = f.default_factory()
            else:
                v = None
            setattr(sa, f.name, v)
        sa.model_path = "unused-for-kernel-benchmarks"
        runtime_context.publish(sa, role="engine")
    _PUBLISHED = True


def _sym(module, attr):
    rel = COPIED.get(module, "")
    return load(module, attr, __file__, rel)


def _call(module, attr, kwargs):
    _publish_runtime_config()
    fn = _sym(module, attr)
    try:
        return fn(**kwargs)
    except TypeError as exc:
        raise RuntimeError(
            "%s.%s could not be called with the recorded arguments: %s\n"
            "The workload row carries only what the capture could serialize. Arguments that "
            "are large tensors (expert weights, KV pools) or non-tensor plan objects are "
            "recorded as metadata in bench/tensors/*/meta.json under 'metadata_only', with "
            "their shape/dtype/quantization flags - reconstruct them here, once, and the "
            "whole row set becomes runnable." % (module, attr, exc)) from exc


K = "sglang.kernels.ops.moe.fused_moe_triton_kernels"
D = "sglang.srt.layers.moe.moe_runner.triton_utils.fused_moe"

OPS = {
    "triton_fused_moe_gemm": lambda **kw: _call(K, "invoke_fused_moe_kernel", kw),
    "moe_fused_experts_fp8": lambda **kw: _call(D, "fused_experts_impl", kw),
    "triton_moe_act_and_mul": lambda **kw: _call(K, "act_and_mul_triton", kw),
    "triton_moe_sum_reduce": lambda **kw: _call(K, "moe_sum_reduce_triton", kw),
    "moe_align_block_size": lambda **kw: _call("sglang.kernels.ops.moe.moe_align",
                                               "moe_align_block_size", kw),
}


def _gemm_fix(kw: dict) -> dict:
    """`compute_type` is a triton dtype - the capture records the type name only.

    The FP8 arm also needs `A_scale` present: `invoke_fused_moe_kernel` quantizes the
    activation into it when it is passed as an empty per-token buffer, and reads it as
    the scale when it is not. The recorded shape is restored here rather than in the row,
    so the row keeps carrying exactly what the model passed.
    """
    import torch
    import triton.language as tl

    a = kw.get("A")
    dt = a.dtype if torch.is_tensor(a) else torch.bfloat16
    kw["compute_type"] = {torch.bfloat16: tl.bfloat16,
                          torch.float16: tl.float16}.get(dt, tl.bfloat16)
    kw.setdefault("bias", None)
    return kw


def _experts_fix(kw: dict) -> dict:
    """`fused_experts_impl` takes plain Python for everything the capture cannot serialize."""
    kw.setdefault("inplace", False)
    kw.setdefault("activation", "silu")
    kw.setdefault("apply_router_weight_on_input", False)
    kw.setdefault("no_combine", False)
    return kw


RECONSTRUCT = {
    "triton_fused_moe_gemm": _gemm_fix,
    "moe_fused_experts_fp8": _experts_fix,
}
