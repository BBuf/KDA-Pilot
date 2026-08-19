"""Baseline wrapper for `minimax_h3__sm103_block_sparse_attention`.

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

COPIED = {'sglang.multimodal_gen.runtime.layers.attention.backends.sdpa': '', 'sglang.multimodal_gen.runtime.layers.attention.backends.flash_attn': ''}


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
}


# Arguments the capture could not serialize (a triton dtype, a plan struct) are rebuilt
# here, once per task, so every workload row becomes runnable. The harness calls
# RECONSTRUCT[op](kwargs) before dispatch.
def _impl(module: str, cls: str):
    """Build the attention backend instance the bound method needs.

    The capture records `self` as a repr - an attention impl is not serializable - so the
    row cannot supply it. Every constructor argument is derivable from the row itself:
    head counts and head size from the query/key shapes, the softmax scale from the head
    size. `causal=False` because this is a video DiT: MiniMax-H3 attends bidirectionally
    over the whole latent sequence, which is exactly why a block-sparse selector has
    something to choose from.
    """
    def build(kw: dict) -> dict:
        if "self" in kw and not isinstance(kw["self"], dict):
            return kw
        import importlib
        q, k = kw["query"], kw["key"]
        head_size = int(q.shape[-1])
        obj = getattr(importlib.import_module(module), cls)(
            num_heads=int(q.shape[-2]), head_size=head_size, causal=False,
            softmax_scale=head_size ** -0.5, num_kv_heads=int(k.shape[-2]))
        kw["self"] = obj
        kw.setdefault("attn_metadata", None)
        return kw
    return build


SDPA = "sglang.multimodal_gen.runtime.layers.attention.backends.sdpa"
FA = "sglang.multimodal_gen.runtime.layers.attention.backends.flash_attn"

# Arguments the capture could not serialize (a triton dtype, a plan struct, the instance
# behind a bound method) are rebuilt here, once per task, so every workload row becomes
# runnable. The harness calls RECONSTRUCT[op](kwargs) before dispatch.
RECONSTRUCT = {
    "diffusion_attention_cudnn_sdpa": _impl(SDPA, "DynamicCudnnSDPAImpl"),
    "diffusion_attention_sdpa": _impl(SDPA, "SDPAImpl"),
    "diffusion_attention_fa4": _impl(FA, "FlashAttentionImpl"),
}
