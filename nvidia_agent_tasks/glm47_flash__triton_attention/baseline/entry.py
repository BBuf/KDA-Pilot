"""Baseline wrapper for `glm47_flash__triton_attention`.

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

COPIED = {'sglang.kernels.ops.attention.decode_attention': 'kernels/ops/attention/decode_attention.py', 'sglang.kernels.ops.attention.extend_attention': 'kernels/ops/attention/extend_attention.py'}


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
    "triton_decode_attention_grouped":
        lambda **kw: _call("sglang.kernels.ops.attention.decode_attention", "decode_attention_fwd_grouped", kw),
    "triton_decode_attention":
        lambda **kw: _call("sglang.kernels.ops.attention.decode_attention", "decode_attention_fwd", kw),
    "triton_extend_attention":
        lambda **kw: _call("sglang.kernels.ops.attention.extend_attention", "extend_attention_fwd", kw),
}


# Arguments the capture could not serialize (a triton dtype, a plan struct) are rebuilt
# here, once per task, so every workload row becomes runnable. The harness calls
# RECONSTRUCT[op](kwargs) before dispatch.
import sys as _sys, os as _os
_sys.path.insert(0, _os.path.join(_os.path.dirname(_os.path.abspath(__file__)), "..", "..", "tools"))
from derive_inputs import derive as _derive  # noqa: E402  shared address-argument repair


RECONSTRUCT = {op: _derive for op in ['triton_decode_attention_grouped', 'triton_decode_attention', 'triton_extend_attention']}
