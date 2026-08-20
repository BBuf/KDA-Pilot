"""Baseline wrapper for `kimi_k3__tgv_bf16_tiny_gemm`.

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

COPIED = {'sglang.kernels.ops.gemm.cutedsl_bf16_gemm': 'kernels/ops/gemm/cutedsl_bf16_gemm.py', 'sglang.kernels.ops.kimi_k3': '', 'sglang.kernels.ops.gemm.tiny_gemm': 'kernels/ops/gemm/tiny_gemm.py'}


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
    "k3_cutedsl_tgv_bf16_gemm_out":
        lambda **kw: _call("sglang.kernels.ops.gemm.cutedsl_bf16_gemm", "cutedsl_bf16_gemm_out", kw),
    "k3_tiny_gemm":
        lambda **kw: _call("sglang.kernels.ops.kimi_k3", "kimi_k3_tiny_gemm", kw),
    "k3_cutedsl_tgv_bf16_gemm":
        lambda **kw: _call("sglang.kernels.ops.gemm.cutedsl_bf16_gemm", "cutedsl_bf16_gemm", kw),
    "k3_tiny_n_gemm_bf16":
        lambda **kw: _call("sglang.kernels.ops.gemm.tiny_gemm", "tiny_n_gemm_bf16", kw),
    "k3_tiny_k_gemm_bf16":
        lambda **kw: _call("sglang.kernels.ops.gemm.tiny_gemm", "tiny_k_gemm_bf16", kw),
}


# Arguments the capture could not serialize (a triton dtype, a plan struct) are rebuilt
# here, once per task, so every workload row becomes runnable. The harness calls
# RECONSTRUCT[op](kwargs) before dispatch.
import sys as _sys, os as _os
_sys.path.insert(0, _os.path.join(_os.path.dirname(_os.path.abspath(__file__)), "..", "..", "tools"))
from derive_inputs import derive as _derive  # noqa: E402  shared address-argument repair


RECONSTRUCT = {op: _derive for op in ['k3_cutedsl_tgv_bf16_gemm_out', 'k3_tiny_gemm', 'k3_cutedsl_tgv_bf16_gemm', 'k3_tiny_n_gemm_bf16', 'k3_tiny_k_gemm_bf16']}
