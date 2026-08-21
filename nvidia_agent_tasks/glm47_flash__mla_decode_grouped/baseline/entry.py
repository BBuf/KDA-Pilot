"""Baseline wrapper for `glm47_flash__mla_decode_grouped`.

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

COPIED = {"sglang.kernels.ops.attention.decode_attention":
          "kernels/ops/attention/decode_attention.py"}


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
    "triton_decode_attention_grouped":
        lambda **kw: _call("sglang.kernels.ops.attention.decode_attention",
                           "decode_attention_fwd_grouped", kw),
}

# The kernel writes through `o` and returns None. Without this the gate has nothing to
# compare and would print `correct=None` next to a speedup - a hole a candidate could
# drive through by returning nothing at all.
OUTPUT_ARGS = {"triton_decode_attention_grouped": ("o",)}


import sys as _sys, os as _os  # noqa: E402

_sys.path.insert(0, _os.path.join(_os.path.dirname(_os.path.abspath(__file__)), "..", "..", "tools"))
from derive_inputs import derive as _derive  # noqa: E402  shared address-argument repair

RECONSTRUCT = {"triton_decode_attention_grouped": _derive}
