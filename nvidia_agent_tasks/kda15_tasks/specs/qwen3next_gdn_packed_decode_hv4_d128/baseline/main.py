"""Baseline: the SGLang kernel this task is asking a candidate to beat.

`TritonGDNKernel` is a stateless dispatcher - the capture recorded `self` as a repr
because it carries no tensors - so constructing one here is equivalent to the bound
method the model calls.
"""

from sglang.srt.layers.attention.linear.kernels.gdn_triton import TritonGDNKernel

_KERNEL = None


def run(
    mixed_qkv,
    a,
    b,
    A_log,
    dt_bias,
    scale,
    ssm_states,
    cache_indices,
    num_v_heads,
    head_v_dim,
):
    global _KERNEL
    if _KERNEL is None:
        _KERNEL = TritonGDNKernel()
    out = _KERNEL.packed_decode(
        mixed_qkv,
        a,
        b,
        A_log=A_log,
        dt_bias=dt_bias,
        scale=float(scale),
        ssm_states=ssm_states,
        cache_indices=cache_indices,
        num_v_heads=int(num_v_heads),
        head_v_dim=int(head_v_dim),
    )
    # The state pool is the second output, returned by reference so the gate can see it
    # at no cost inside the timed call. Comparing only `out` would pass a candidate that
    # advances the state wrongly - the error would surface as drift on the next token,
    # not here. Each arm gets its own cloned pool, so a candidate that corrupts a slot
    # (or writes a slot it does not own) fails on this output.
    return out, ssm_states
