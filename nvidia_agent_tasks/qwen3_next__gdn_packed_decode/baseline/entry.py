"""Baseline wrapper for `qwen3_next__gdn_packed_decode`.

The harness (`tools/bench_harness.py`) calls `OPS[<op>](**row_args)`. The entry loads the
symbol from the installed SGLang and checks its source hash against the copy in this
directory, so a drifted environment is reported instead of silently benchmarked - see
`tools/baseline_loader.py`.

Write `solution/entry.py` with the same `OPS` key to have the harness A/B it.
"""

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "tools"))
from baseline_loader import load  # noqa: E402

COPIED = {"sglang.srt.layers.attention.linear.kernels.gdn_triton":
          "srt/layers/attention/linear/kernels/gdn_triton.py"}


def _sym(module, attr):
    return load(module, attr, __file__, COPIED.get(module, ""))


def _call(module, attr, kwargs):
    fn = _sym(module, attr)
    try:
        return fn(**kwargs)
    except TypeError as exc:
        raise RuntimeError(
            "%s.%s could not be called with the recorded arguments: %s" % (module, attr, exc)
        ) from exc


OPS = {
    "gdn_decode_packed_triton":
        lambda **kw: _call("sglang.srt.layers.attention.linear.kernels.gdn_triton",
                           "TritonGDNKernel.packed_decode", kw),
}

# The kernel returns `out` *and* advances this batch's slots in `ssm_states` in place.
# Declaring the state as an output is what makes the gate see it: a candidate that gets
# `out` right while advancing the state wrongly is wrong in a way that would otherwise
# only surface as drift on the next token.
OUTPUT_ARGS = {"gdn_decode_packed_triton": ("ssm_states",)}


def _gdn_kernel(kw: dict) -> dict:
    """`packed_decode` is a bound method; the capture records `self` as a repr.

    `TritonGDNKernel` is a stateless dispatcher (its base class declares only abstract
    methods and no constructor state), so instantiating it here reproduces exactly what
    the server calls - there is no per-layer state hiding in the instance.
    """
    if "self" in kw and not isinstance(kw["self"], dict):
        return kw
    from sglang.srt.layers.attention.linear.kernels.gdn_triton import TritonGDNKernel

    kw["self"] = TritonGDNKernel()
    return kw


import sys as _sys, os as _os  # noqa: E402

_sys.path.insert(0, _os.path.join(_os.path.dirname(_os.path.abspath(__file__)), "..", "..", "tools"))
from derive_inputs import derive as _derive  # noqa: E402  shared address-argument repair


def _repair(kw):
    """`derive()` first - it repairs the address-like arguments every row has, and for
    this kernel that means giving each sequence a *distinct* state slot - then the task's
    own hook for what only this task knows."""
    return _gdn_kernel(_derive(kw))


RECONSTRUCT = {"gdn_decode_packed_triton": _repair}
