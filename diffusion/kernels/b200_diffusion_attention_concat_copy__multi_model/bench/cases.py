"""Shared, deterministic tensor construction + independent oracle for the
attention concat/copy/slice task. Used by both bench/correctness.py and
bench/adapter.py so the baseline, candidate, and oracle all see identical inputs.

Construction recipes come from bench/workloads.json (see bench/gen_workloads.py).
All ops are lossless memory movement, so the oracle is computed with plain
PyTorch indexing / contiguous / cat and compared bit-exactly (incl. NaN/Inf).
"""

from __future__ import annotations

import json
import os
from types import SimpleNamespace

import torch

_DTYPES = {"bfloat16": torch.bfloat16, "float16": torch.float16, "float32": torch.float32}
# integer reinterpretation for bit-exact comparison (same #bits as the float dtype)
_INT_VIEW = {torch.bfloat16: torch.int16, torch.float16: torch.int16, torch.float32: torch.int32}

# selector ints — must match baseline/binding.py OP_*/ORDER_* and solution/kernel.cu
OP = {"copy_contiguous": 0, "concat_sequence": 1, "slice_heads_then_concat": 2}
ORDER = {"AB": 0, "BA": 1}

WORKLOADS_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "workloads.json")


def load_workloads():
    with open(WORKLOADS_PATH) as f:
        rows = json.load(f)
    import gen_workloads  # same directory; pure stdlib schema validator
    errs = gen_workloads.validate_workloads(rows)
    if errs:
        raise ValueError("workloads.json failed schema validation:\n  " + "\n  ".join(errs))
    return rows


def _rand(shape, dtype, device, gen):
    return torch.randn(*shape, generator=gen, device=device, dtype=torch.float32).to(dtype)


def _inject_nonfinite(t):
    """Write NaN / +Inf / -Inf sentinels into a few cells in-place. Works on
    non-contiguous views (uses index assignment, not .view)."""
    t[0, 0, 0, 0] = float("nan")
    if t.shape[-1] > 1:
        t[0, 0, 0, 1] = float("inf")
    if t.shape[-1] > 2:
        t[0, 0, 0, 2] = float("-inf")
    return t


def make_inputs(w, device, seed=None):
    """Build the source tensors for one workload. Returns a SimpleNamespace with
    the positional ABI args (op_type, order, h_start, h_local, source_a, source_b)
    plus `keepalive` (storage backing any non-contiguous views) and `dtype`."""
    dtype = _DTYPES[w["dtype"]]
    op = OP[w["op_type"]]
    order = ORDER[w["order"]]
    h_start = int(w.get("h_start", 0))
    h_local = int(w.get("h_local", 0))
    s = int(w["seed"] if seed is None else seed)
    gen = torch.Generator(device=device).manual_seed(s)
    inject = bool(w.get("inject_nonfinite", False))
    keepalive = []

    if op == OP["copy_contiguous"]:
        spec = w["tensors"]["a"]
        b, seq, heads, d = spec["shape"]
        full_heads = int(spec["full_heads"])
        hstart = int(spec["head_start"])
        full = _rand([b, seq, full_heads, d], dtype, device, gen)  # contiguous backing
        source_a = full[:, :, hstart:hstart + heads, :]            # non-contiguous head-slice view
        assert not source_a.is_contiguous(), "copy_contiguous source must be non-contiguous"
        if inject:
            _inject_nonfinite(source_a)
        keepalive.append(full)
        source_b = None

    elif op == OP["concat_sequence"]:
        a = _rand(w["tensors"]["a"]["shape"], dtype, device, gen)
        bb = _rand(w["tensors"]["b"]["shape"], dtype, device, gen)
        if inject:
            _inject_nonfinite(a)
            _inject_nonfinite(bb)
        source_a, source_b = a, bb

    elif op == OP["slice_heads_then_concat"]:
        prefix = _rand(w["tensors"]["prefix"]["shape"], dtype, device, gen)  # full-head, contiguous
        shard = _rand(w["tensors"]["shard"]["shape"], dtype, device, gen)
        if inject:
            _inject_nonfinite(prefix[:, :, h_start:h_start + h_local, :])  # inside the slice region
            _inject_nonfinite(shard)
        source_a, source_b = prefix, shard

    else:
        raise ValueError(f"unknown op_type {w['op_type']}")

    return SimpleNamespace(
        op_type=op, order=order, h_start=h_start, h_local=h_local,
        source_a=source_a, source_b=source_b, dtype=dtype, keepalive=keepalive,
    )


def alloc_output(w, device):
    return torch.empty(tuple(w["output_shape"]), dtype=_DTYPES[w["dtype"]], device=device)


def alloc_scratch(w, device):
    if "scratch_shape" in w and w["scratch_shape"]:
        return torch.empty(tuple(w["scratch_shape"]), dtype=_DTYPES[w["dtype"]], device=device)
    return None


def oracle(w, inp):
    """Independent PyTorch reference output (lossless). Computed with plain
    indexing / contiguous / cat — NOT via the baseline binding."""
    op = inp.op_type
    if op == OP["copy_contiguous"]:
        return inp.source_a.contiguous()
    if op == OP["concat_sequence"]:
        if inp.order == ORDER["AB"]:
            return torch.cat([inp.source_a, inp.source_b], dim=1)
        return torch.cat([inp.source_b, inp.source_a], dim=1)
    if op == OP["slice_heads_then_concat"]:
        sliced = inp.source_a[:, :, inp.h_start:inp.h_start + inp.h_local, :].contiguous()
        if inp.order == ORDER["AB"]:
            return torch.cat([sliced, inp.source_b], dim=1)
        return torch.cat([inp.source_b, sliced], dim=1)
    raise ValueError(f"unknown op_type {op}")


def bitwise_equal(actual, expected):
    """Bit-exact comparison that treats matching NaN/Inf bit patterns as equal.
    Both tensors must be contiguous, same shape/dtype."""
    if actual.shape != expected.shape or actual.dtype != expected.dtype:
        return False
    iv = _INT_VIEW[actual.dtype]
    a = actual.contiguous().view(iv)
    e = expected.contiguous().view(iv)
    return bool(torch.equal(a, e))


def first_mismatch(actual, expected):
    """Return (count, example_index) of differing elements for diagnostics."""
    iv = _INT_VIEW[actual.dtype]
    a = actual.contiguous().view(iv)
    e = expected.contiguous().view(iv)
    diff = a != e
    n = int(diff.sum().item())
    idx = None
    if n:
        flat = diff.view(-1).nonzero(as_tuple=False)
        if flat.numel():
            idx = int(flat[0].item())
    return n, idx
