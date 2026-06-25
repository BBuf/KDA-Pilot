"""Benchmark adapter for b200_diffusion_causal_conv3d_cat_pad__multi_shape.

Supplies tensor construction and the two ABI calls for bench/benchmark.py. Both
``call_baseline`` and ``call_candidate`` are thin, pure-Python forwarders that
allocate nothing in the timed path: outputs are preallocated in ``make_case``
and poisoned/timed by the benchmark template. The only per-side difference is
that the Triton baseline takes the 6-int padding as a list (its faithful
upstream signature) while the CUDA candidate takes the same 6 ints positionally;
both are trivial argument forwards, so wrapper overhead is equivalent.

The baseline side calls the copied SGLang Triton kernel through the
destination-passing launcher in baseline/binding.py. The candidate side calls
the CUDA module built from solution/kernel.cu via tvm-ffi. No ``sglang`` import
anywhere in this process (asserted below).
"""

from __future__ import annotations

import sys
from pathlib import Path

_TASK_ROOT = Path(__file__).resolve().parents[1]
if str(_TASK_ROOT) not in sys.path:
    sys.path.insert(0, str(_TASK_ROOT))

import torch

import baseline.binding as _baseline
from solution.build import load_candidate_module

assert not any(
    name == "sglang" or name.startswith("sglang.") for name in sys.modules
), "standalone contract violation: sglang imported at benchmark runtime"

_DTYPES = {
    "bfloat16": torch.bfloat16,
    "float16": torch.float16,
    "float32": torch.float32,
}

_candidate_module = load_candidate_module()
_BASELINE_FN = _baseline.fused_causal_conv3d_cat_pad
_CANDIDATE_FN = _candidate_module.causal_conv3d_cat_pad_candidate


def _build_tensor(spec: dict, device: torch.device) -> torch.Tensor:
    """Build an input tensor. Contiguous by default; if ``stride`` (and optional
    ``storage_offset_elems``) is recorded in the frozen workload, materialize a
    tensor with that exact layout holding random values (for regression rows)."""
    dtype = _DTYPES[spec["dtype"]]
    shape = spec["shape"]
    ref = torch.randn(shape, device=device, dtype=dtype)
    stride = spec.get("stride")
    if stride is None:
        return ref
    offset = int(spec.get("storage_offset_elems", 0))
    storage_numel = offset + 1 + sum((s - 1) * st for s, st in zip(shape, stride))
    base = torch.empty(storage_numel, device=device, dtype=dtype)
    strided = torch.as_strided(base, shape, stride, storage_offset=offset)
    strided.copy_(ref)
    return strided


def make_case(workload: dict, *, device: torch.device, seed: int) -> dict:
    del seed  # benchmark.py already seeded the global generators per trial
    shapes = workload["shapes"]
    x = _build_tensor(shapes["x"], device)
    cache = _build_tensor(shapes["cache"], device)
    padding = [int(p) for p in workload["padding"]]
    width_left, width_right, height_top, height_bottom, depth_left, depth_right = padding

    n, c, t, h, w = x.shape
    out_shape = (
        n,
        c,
        t + depth_left + depth_right,
        h + height_top + height_bottom,
        w + width_left + width_right,
    )
    inputs = {"x": x, "cache": cache, "padding": padding}
    baseline_outputs = [torch.empty(out_shape, device=device, dtype=x.dtype)]
    candidate_outputs = [torch.empty(out_shape, device=device, dtype=x.dtype)]
    return {
        "inputs": inputs,
        "baseline_outputs": baseline_outputs,
        "candidate_outputs": candidate_outputs,
        "tolerance": {
            "atol": float(workload.get("atol", 0.0)),
            "rtol": float(workload.get("rtol", 0.0)),
        },
    }


def call_baseline(workload: dict, inputs, outputs) -> None:
    _BASELINE_FN(inputs["x"], inputs["cache"], inputs["padding"], outputs[0])


def call_candidate(workload: dict, inputs, outputs) -> None:
    p = inputs["padding"]
    _CANDIDATE_FN(inputs["x"], inputs["cache"], p[0], p[1], p[2], p[3], p[4], p[5], outputs[0])


def _as_list(x):
    return list(x) if isinstance(x, (list, tuple)) else [x]


def compare_outputs(workload, baseline_outputs, candidate_outputs, tolerance):
    """Bitwise A/B comparison for this exact cat+pad copy op.

    The op performs no arithmetic, so baseline and candidate must be bit-identical
    (NaN/Inf payloads and signed zeros included). The benchmark template's default
    comparator uses float tolerance and rejects any NaN/Inf, which is wrong here;
    this override compares raw element bits via an integer view. ``tolerance`` is
    ignored on purpose (the contract is atol=0, rtol=0)."""
    del tolerance
    base = _as_list(baseline_outputs)
    cand = _as_list(candidate_outputs)
    if len(base) != len(cand):
        return {"ok": False, "max_abs": float("inf"), "max_rel": float("inf"),
                "message": f"output count mismatch: baseline={len(base)} candidate={len(cand)}"}
    for idx, (lhs, rhs) in enumerate(zip(base, cand)):
        if tuple(lhs.shape) != tuple(rhs.shape):
            return {"ok": False, "max_abs": float("inf"), "max_rel": float("inf"),
                    "message": f"output {idx} shape mismatch: {tuple(lhs.shape)} vs {tuple(rhs.shape)}"}
        if lhs.dtype != rhs.dtype:
            return {"ok": False, "max_abs": float("inf"), "max_rel": float("inf"),
                    "message": f"output {idx} dtype mismatch: {lhs.dtype} vs {rhs.dtype}"}
        es = lhs.element_size()
        iview = {2: torch.int16, 4: torch.int32, 8: torch.int64}.get(es)
        if iview is None:
            return {"ok": False, "max_abs": float("inf"), "max_rel": float("inf"),
                    "message": f"output {idx} unsupported element size {es}"}
        li = lhs.detach().contiguous().view(iview)
        ri = rhs.detach().contiguous().view(iview)
        if not torch.equal(li, ri):
            mism = li != ri
            n = int(mism.sum().item())
            nz = mism.flatten().nonzero(as_tuple=False)
            first = int(nz[0].item()) if nz.numel() else -1
            return {"ok": False, "max_abs": float("inf"), "max_rel": float("inf"),
                    "message": f"output {idx}: {n} bitwise mismatch(es) (exact copy required); first flat index {first}"}
    return {"ok": True, "max_abs": 0.0, "max_rel": 0.0, "message": ""}
