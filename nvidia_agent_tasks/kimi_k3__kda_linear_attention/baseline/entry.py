"""Baseline wrapper for `kimi_k3__kda_linear_attention`.

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

COPIED = {'sglang.kernels.ops.attention.kda_fused_decode': 'kernels/ops/attention/kda_fused_decode.py', 'sglang.kernels.ops.attention.fla.kda': 'kernels/ops/attention/fla/kda.py'}


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
    "k3_kda_fused_decode":
        lambda **kw: _call("sglang.kernels.ops.attention.kda_fused_decode", "kda_fused_decode", kw),
    "k3_kda_chunk_prefill":
        lambda **kw: _call("sglang.kernels.ops.attention.fla.kda", "chunk_kda_fwd", kw),
}


# Arguments the capture could not serialize (a triton dtype, a plan struct) are rebuilt
# here, once per task, so every workload row becomes runnable. The harness calls
# RECONSTRUCT[op](kwargs) before dispatch.
def _kda_segments(kw: dict) -> dict:
    """Derive the segment arguments for a row whose length has no shipped payload.

    `cu_seqlens` and `initial_state_indices` are integer arguments: allocated they come
    out as zeros, which makes the kernel write nothing and the "reference" uninitialized
    memory (the harness catches that and prints NO VALID REFERENCE). For a row that
    carries one sequence of T tokens the correct values are not a guess - they are
    `[0, T]` and the state slot the sequence owns. Rows whose payload does supply the
    real arrays are left untouched.
    """
    import torch

    q = kw.get("q")
    if not torch.is_tensor(q):
        return kw
    total = int(q.shape[1]) if q.dim() == 4 else int(q.shape[0])
    cu = kw.get("cu_seqlens")
    if torch.is_tensor(cu) and int(cu.numel()) == 2 and int(cu[-1]) == 0:
        kw["cu_seqlens"] = torch.tensor([0, total], dtype=cu.dtype, device=cu.device)
    idx = kw.get("initial_state_indices")
    if torch.is_tensor(idx) and idx.numel() and int(idx.max()) == 0 and idx.numel() > 1:
        kw["initial_state_indices"] = torch.arange(idx.numel(), dtype=idx.dtype,
                                                   device=idx.device)
    return kw


# Arguments the capture could not serialize (a triton dtype, a plan struct) are rebuilt
# here, once per task, so every workload row becomes runnable. The harness calls
# RECONSTRUCT[op](kwargs) before dispatch.
RECONSTRUCT = {"k3_kda_chunk_prefill": _kda_segments}
