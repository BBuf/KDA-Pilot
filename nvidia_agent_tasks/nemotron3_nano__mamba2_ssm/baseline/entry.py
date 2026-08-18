"""Baseline wrapper for `nemotron3_nano__mamba2_ssm`.

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

COPIED = {'sglang.kernels.ops.mamba.causal_conv1d_triton': 'kernels/ops/mamba/causal_conv1d_triton.py', 'sglang.kernels.ops.mamba.triton_ops.ssd_chunk_state': 'kernels/ops/mamba/triton_ops/ssd_chunk_state.py', 'sglang.kernels.ops.mamba.triton_ops.ssd_state_passing': 'kernels/ops/mamba/triton_ops/ssd_state_passing.py', 'sglang.kernels.ops.mamba.triton_ops.ssd_chunk_scan': 'kernels/ops/mamba/triton_ops/ssd_chunk_scan.py', 'sglang.kernels.ops.mamba.triton_ops.ssd_combined': 'kernels/ops/mamba/triton_ops/ssd_combined.py'}


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
    "causal_conv1d_decode":
        lambda **kw: _call("sglang.kernels.ops.mamba.causal_conv1d_triton", "causal_conv1d_update", kw),
    "mamba2_chunk_cumsum":
        lambda **kw: _call("sglang.kernels.ops.mamba.triton_ops.ssd_chunk_state", "_chunk_cumsum_fwd", kw),
    "mamba2_chunk_state":
        lambda **kw: _call("sglang.kernels.ops.mamba.triton_ops.ssd_chunk_state", "_chunk_state_fwd", kw),
    "causal_conv1d_prefill":
        lambda **kw: _call("sglang.kernels.ops.mamba.causal_conv1d_triton", "causal_conv1d_fn", kw),
    "mamba2_state_passing":
        lambda **kw: _call("sglang.kernels.ops.mamba.triton_ops.ssd_state_passing", "_state_passing_fwd", kw),
    "mamba2_chunk_scan":
        lambda **kw: _call("sglang.kernels.ops.mamba.triton_ops.ssd_chunk_scan", "_chunk_scan_fwd", kw),
    "mamba2_chunk_state_varlen":
        lambda **kw: _call("sglang.kernels.ops.mamba.triton_ops.ssd_chunk_state", "chunk_state_varlen", kw),
    "mamba2_chunk_scan_combined_fwd":
        lambda **kw: _call("sglang.kernels.ops.mamba.triton_ops.ssd_combined", "_mamba_chunk_scan_combined_fwd", kw),
    "mamba2_chunk_scan_combined":
        lambda **kw: _call("sglang.kernels.ops.mamba.triton_ops.ssd_combined", "mamba_chunk_scan_combined", kw),
}
