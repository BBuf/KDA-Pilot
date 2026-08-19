"""Baseline wrapper for `lfm25__triton_fused_moe`.

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

COPIED = {'sglang.kernels.ops.moe.fused_moe_triton_kernels': 'kernels/ops/moe/fused_moe_triton_kernels.py'}


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
    "triton_fused_moe_gemm":
        lambda **kw: _call("sglang.kernels.ops.moe.fused_moe_triton_kernels", "invoke_fused_moe_kernel", kw),
}


def _moe_fix(kw: dict) -> dict:
    """`compute_type` is a triton dtype - the capture records the type name only."""
    import triton.language as tl
    import torch

    a = kw.get("A")
    dt = a.dtype if torch.is_tensor(a) else torch.bfloat16
    kw["compute_type"] = {torch.bfloat16: tl.bfloat16,
                          torch.float16: tl.float16}.get(dt, tl.bfloat16)
    kw.setdefault("bias", None)
    return kw


RECONSTRUCT = {"triton_fused_moe_gemm": _moe_fix}
