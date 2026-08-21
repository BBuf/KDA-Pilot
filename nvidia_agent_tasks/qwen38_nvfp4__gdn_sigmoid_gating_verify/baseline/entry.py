"""Baseline wrapper for `qwen38_nvfp4__gdn_sigmoid_gating_verify`."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "tools"))
from baseline_loader import load  # noqa: E402

COPIED = {
    "sglang.kernels.ops.attention.fla.fused_sigmoid_gating_recurrent": "kernels/ops/attention/fla/fused_sigmoid_gating_recurrent.py",
    "sglang.kernels.ops.attention.triton_gdn_fused_proj": "kernels/ops/attention/triton_gdn_fused_proj.py",
    "sglang.kernels.ops.mamba.causal_conv1d_triton": "kernels/ops/mamba/causal_conv1d_triton.py",
}

def _sym(module, attr):
    return load(module, attr, __file__, COPIED.get(module, ""))

OPS = {
    "qwen38_gdn_gating_update": lambda **kw: _sym("sglang.kernels.ops.attention.fla.fused_sigmoid_gating_recurrent", "fused_sigmoid_gating_delta_rule_update")(**kw),
    "qwen38_qkvzba_split": lambda **kw: _sym("sglang.kernels.ops.attention.triton_gdn_fused_proj", "fused_qkvzba_split_reshape_cat_contiguous")(**kw),
    "qwen38_conv1d_update": lambda **kw: _sym("sglang.kernels.ops.mamba.causal_conv1d_triton", "causal_conv1d_update")(**kw),
}
def _conv1d_update(kw: dict) -> dict:
    """Give `causal_conv1d_update` the shape it reads its batch and length from.

    The row records `x=[T, dim]`, taken from the `is_target_verify` branch of
    `GDNAttnBackend`, which hands the kernel a transposed `mixed_qkv`. The kernel
    reads `batch, dim, seqlen` off `x`, so the 2-D tensor reads as `batch=T,
    seqlen=1`: with the one recorded `conv_state` slot, rows `1..T-1` address slots
    that do not exist and the output comes back NaN/Inf. The verify window is one
    sequence of T draft tokens, which is `x = [1, dim, T]` - the documented
    multiple-token form, and the orientation production passes. Taken as a view:
    the kernel wants `stride(1) == 1`, which the transposed view has and a
    contiguous `[1, dim, T]` would not.

    Nothing else is added. Production also passes `conv_state_indices`,
    `intermediate_conv_window`, `intermediate_state_indices`, `num_accept_tokens`
    and the `retrieve_next_token` / `retrieve_next_sibling` /
    `retrieve_parent_token` draft-tree triple, and this capture recorded none of
    them. Reconstructing that set from the shapes is not safe - the triple is
    topology, not geometry, and a guessed version wrote outside its buffers (the
    tell was a *cached* weight tensor changing value after the first call while
    every input checksummed identical). The form below is complete, in-bounds and
    reproducible; it models a fully-accepted window rather than partial
    acceptance, which is the same kernel work. See docs/capture_gaps.md.
    """
    x = kw["x"]
    state = kw["conv_state"]
    if x.dim() != 2 or state.dim() != 3:
        raise ValueError(
            "expected x=[T, dim] and conv_state=[slots, dim, width], got %s and %s"
            % (tuple(x.shape), tuple(state.shape)))
    if state.shape[0] != 1:
        # A capture with a real batch would carry the recorded slot mapping.
        raise ValueError("expected a single conv-state slot, recorded %d" % state.shape[0])
    if state.shape[1] != x.shape[1]:
        raise ValueError("conv_state dim %d does not match x dim %d"
                         % (state.shape[1], x.shape[1]))
    kw["x"] = x.unsqueeze(0).transpose(1, 2)
    return kw


# An index argument selects rows of the pool named here. Drawn at random it points
# anywhere, and these kernels index without bounds-checking.
_INDEX_ARGS = {
    "initial_state_indices": "initial_state_source",
    "conv_state_indices": "conv_state",
    "cache_indices": "ssm_states",
}


def _common(kw: dict) -> dict:
    """Repair the three argument kinds a random draw cannot stand in for.

    * index arguments are clamped into their pool, because these kernels index
      without bounds-checking;
    * `cu_seqlens` is rebuilt as an actual prefix sum -- the kernel walks it to
      find each sequence's slice of the packed activation, so unsorted values read
      outside the buffer. That surfaces as `CUDA error: an illegal memory access`,
      and because the error is asynchronous and sticky it gets reported against
      whichever row runs next rather than the one that caused it;
    * `dt_bias` is a positive fp32 bias, so the magnitude is taken.
    """
    import torch

    for name, pool in _INDEX_ARGS.items():
        index, target = kw.get(name), kw.get(pool)
        if torch.is_tensor(index) and torch.is_tensor(target):
            index.clamp_(0, target.shape[0] - 1)
    tokens = None
    for name in ("mixed_qkvz", "x", "q", "a"):
        value = kw.get(name)
        if torch.is_tensor(value):
            tokens = int(value.shape[-2] if value.dim() >= 3 else value.shape[0])
            break
    for name, value in kw.items():
        if "cu_seqlens" in name and torch.is_tensor(value) and tokens is not None:
            segments = value.numel() - 1
            if segments >= 1:
                bounds = [(tokens * i) // segments for i in range(segments + 1)]
                value.copy_(torch.tensor(bounds, dtype=value.dtype, device=value.device))
    bias = kw.get("dt_bias")
    if torch.is_tensor(bias) and bias.is_floating_point():
        bias.abs_()
    return kw


def _split_geometry(kw: dict) -> dict:
    """The four head-geometry ints `fused_qkvzba_split_*` takes.

    They are ints, so a tensor-only shape capture never saw them:
    `fused_qkvzba_split_reshape_cat_contiguous() missing 4 required positional
    arguments`. Rather than hardcode the model config they are derived from the
    recorded packed widths, and the arithmetic is asserted -- a future capture at a
    different geometry then fails loudly instead of being silently mis-split.

    `mixed_qkvz` packs q and k at `num_heads_qk x head_qk` plus v and z at
    `num_heads_v x head_v`; `mixed_ba` packs b and a at one scalar per v-head.
    """
    kw = _common(kw)
    qkvz = int(kw["mixed_qkvz"].shape[-1])
    num_heads_v = int(kw["mixed_ba"].shape[-1]) // 2
    head_qk = head_v = 128
    num_heads_qk = num_heads_v // 3  # 48 v-heads to 16 qk-heads at this geometry
    expected = 2 * num_heads_qk * head_qk + 2 * num_heads_v * head_v
    if expected != qkvz:
        raise ValueError(
            "qkvz width %d does not match a %dx%d + %dx%d split (computed %d)"
            % (qkvz, num_heads_qk, head_qk, num_heads_v, head_v, expected))
    kw.update(num_heads_qk=num_heads_qk, num_heads_v=num_heads_v,
              head_qk=head_qk, head_v=head_v)
    return kw



import sys as _sys, os as _os
_sys.path.insert(0, _os.path.join(_os.path.dirname(_os.path.abspath(__file__)), "..", "..", "tools"))
from derive_inputs import derive as _derive  # noqa: E402  shared address-argument repair


_TASK_FIX = {
    "qwen38_gdn_gating_update": _common,
    "qwen38_qkvzba_split": _split_geometry,
    "qwen38_conv1d_update": lambda kw: _conv1d_update(_common(kw)),
}


def _repair(op):
    """`derive()` first - it repairs the address-like arguments every row has - then the
    task's own hook for what only this task knows."""
    task_hook = _TASK_FIX.get(op)

    def run(kw):
        kw = _derive(kw)
        return task_hook(kw) if task_hook else kw

    return run


RECONSTRUCT = {op: _repair(op) for op in set(list(_TASK_FIX) + ['qwen38_gdn_gating_update', 'qwen38_qkvzba_split', 'qwen38_conv1d_update', 'initial_state_indices', 'conv_state_indices', 'cache_indices'])}
