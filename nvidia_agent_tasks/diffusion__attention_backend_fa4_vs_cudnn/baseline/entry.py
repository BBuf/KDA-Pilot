"""Baseline wrapper for `diffusion__attention_backend_fa4_vs_cudnn`.

The harness (`tools/bench_harness.py`) calls `OPS[<op>](**row_args)`. Each entry loads
the symbol from the installed SGLang and checks its source hash against the copy in this
directory, so a drifted environment is reported instead of silently benchmarked - see
`tools/baseline_loader.py`.

Write `solution/entry.py` with the same `OPS` keys to have the harness A/B it.
"""

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "tools"))
from baseline_loader import load  # noqa: E402

COPIED = {'sglang.multimodal_gen.runtime.layers.attention.backends.sdpa': '', 'sglang.multimodal_gen.runtime.layers.attention.backends.flash_attn': '', 'sglang.kernels.ops.diffusion.norm_scale_shift_native': ''}


def _sym(module, attr):
    rel = COPIED.get(module, "")
    return load(module, attr, __file__, rel)


def _call(module, attr, kwargs):
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


OPS = {
    "diffusion_attention_cudnn_sdpa":
        lambda **kw: _call("sglang.multimodal_gen.runtime.layers.attention.backends.sdpa", "DynamicCudnnSDPAImpl.forward", kw),
    "diffusion_attention_fa4":
        lambda **kw: _call("sglang.multimodal_gen.runtime.layers.attention.backends.flash_attn", "FlashAttentionImpl.forward", kw),
    "diffusion_attention_sdpa":
        lambda **kw: _call("sglang.multimodal_gen.runtime.layers.attention.backends.sdpa", "SDPAImpl.forward", kw),
    "diffusion_fused_scale_residual_norm_scale_shift":
        lambda **kw: _call("sglang.kernels.ops.diffusion.norm_scale_shift_native", "try_fused_scale_residual_norm_scale_shift", kw),
    "diffusion_fused_norm_scale_shift":
        lambda **kw: _call("sglang.kernels.ops.diffusion.norm_scale_shift_native", "try_fused_norm_scale_shift", kw),
}
