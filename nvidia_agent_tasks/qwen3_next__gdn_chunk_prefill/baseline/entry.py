"""Baseline wrapper for `qwen3_next__gdn_chunk_prefill`.

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

COPIED = {'sglang.kernels.ops.attention.fla.wy_fast': 'kernels/ops/attention/fla/wy_fast.py', 'sglang.kernels.ops.attention.fla.chunk_delta_h': 'kernels/ops/attention/fla/chunk_delta_h.py', 'sglang.kernels.ops.attention.fla.chunk_o': 'kernels/ops/attention/fla/chunk_o.py', 'sglang.kernels.ops.attention.fla.chunk': 'kernels/ops/attention/fla/chunk.py', 'sglang.kernels.ops.mamba.causal_conv1d_triton': '', 'sglang.srt.layers.attention.linear.kernels.gdn_triton': ''}


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
    "gdn_recompute_w_u":
        lambda **kw: _call("sglang.kernels.ops.attention.fla.wy_fast", "recompute_w_u_fwd", kw),
    "gdn_chunk_delta_h":
        lambda **kw: _call("sglang.kernels.ops.attention.fla.chunk_delta_h", "chunk_gated_delta_rule_fwd_h", kw),
    "gdn_chunk_o":
        lambda **kw: _call("sglang.kernels.ops.attention.fla.chunk_o", "chunk_fwd_o", kw),
    "gdn_chunk_prefill":
        lambda **kw: _call("sglang.kernels.ops.attention.fla.chunk", "chunk_gated_delta_rule_fwd", kw),
    "gdn_decode_causal_conv1d_update":
        lambda **kw: _call("sglang.kernels.ops.mamba.causal_conv1d_triton", "causal_conv1d_update", kw),
    "gdn_decode_packed_triton":
        lambda **kw: _call("sglang.srt.layers.attention.linear.kernels.gdn_triton", "TritonGDNKernel.packed_decode", kw),
}
