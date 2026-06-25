"""Benchmark adapter for the attention concat/copy/slice task.

Implements the bench/benchmark.py adapter API (make_case / call_baseline /
call_candidate / compare_outputs). Tensor construction is delegated to
bench/cases.py so the baseline, candidate, and correctness oracle all build
identical inputs.

The baseline (`baseline/binding.py`, PyTorch/ATen) and candidate
(`solution/binding.py`, CUDA via tvm_ffi.cpp.load) are driven through the
identical positional ABI:
    fn(op_type, order, h_start, h_local, source_a, source_b, scratch, output)
so wrapper overhead is symmetric; CUDA-event timing in the harness measures the
GPU op region only.

compare_outputs is BIT-EXACT (the default tolerance compare rejects NaN/Inf,
but these lossless ops must preserve NaN/Inf bit-for-bit).
"""

from __future__ import annotations

import math
import os
import sys
from types import SimpleNamespace

TASK_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if TASK_ROOT not in sys.path:
    sys.path.insert(0, TASK_ROOT)

import cases  # noqa: E402  (same directory)
from baseline.binding import attention_concat_copy_baseline as _BASELINE  # noqa: E402

# Resolve the candidate handle at import for symmetric overhead. Guarded so the
# adapter can still be imported off-GPU (e.g. to smoke-test make_case); a real
# benchmark run resolves/builds it here, before any timed region.
try:
    from solution.binding import attention_concat_copy_candidate as _CANDIDATE
except Exception:  # pragma: no cover - candidate not built yet / no CUDA
    _CANDIDATE = None


def make_case(workload, *, device, seed):
    inp = cases.make_inputs(workload, device=device, seed=seed)
    baseline_out = cases.alloc_output(workload, device)
    candidate_out = cases.alloc_output(workload, device)
    scratch = cases.alloc_scratch(workload, device)
    inputs = SimpleNamespace(
        op_type=inp.op_type,
        order=inp.order,
        h_start=inp.h_start,
        h_local=inp.h_local,
        source_a=inp.source_a,
        source_b=inp.source_b,
        scratch=scratch,
        keepalive=inp.keepalive,  # keeps non-contiguous-view storage alive
    )
    return {
        "inputs": inputs,
        "baseline_outputs": [baseline_out],
        "candidate_outputs": [candidate_out],
        "tolerance": {"atol": float(workload.get("atol", 0)), "rtol": float(workload.get("rtol", 0))},
    }


def call_baseline(workload, inputs, outputs):
    _BASELINE(inputs.op_type, inputs.order, inputs.h_start, inputs.h_local,
              inputs.source_a, inputs.source_b, inputs.scratch, outputs[0])


# A/A harness-validity switch: when KDA_AA=1 the candidate slot runs the BASELINE,
# so the reported geomean should be ~1.0 (proves the interleaved A/B timing has no
# systematic slot bias). Used only for the validity run, never the headline result.
_AA = os.environ.get("KDA_AA") == "1"


def call_candidate(workload, inputs, outputs):
    if _AA:
        return call_baseline(workload, inputs, outputs)
    if _CANDIDATE is None:
        raise RuntimeError("candidate not available: build solution/ (tvm_ffi.cpp.load) on a CUDA device")
    _CANDIDATE(inputs.op_type, inputs.order, inputs.h_start, inputs.h_local,
               inputs.source_a, inputs.source_b, inputs.scratch, outputs[0])


def compare_outputs(workload, baseline_outputs, candidate_outputs, tolerance):
    """Bit-exact comparison (atol=rtol=0), NaN/Inf-preserving. Candidate must
    equal the baseline bit-for-bit (both are lossless memory movement)."""
    base = baseline_outputs[0]
    cand = candidate_outputs[0]
    if base.shape != cand.shape:
        return {"ok": False, "max_abs": math.inf, "max_rel": math.inf,
                "message": f"shape mismatch {tuple(base.shape)} vs {tuple(cand.shape)}"}
    if base.dtype != cand.dtype:
        return {"ok": False, "max_abs": math.inf, "max_rel": math.inf,
                "message": f"dtype mismatch {base.dtype} vs {cand.dtype}"}
    if cases.bitwise_equal(cand, base):
        return {"ok": True, "max_abs": 0.0, "max_rel": 0.0, "message": ""}
    cnt, idx = cases.first_mismatch(cand, base)
    return {"ok": False, "max_abs": math.inf, "max_rel": math.inf,
            "message": f"bitwise mismatch: {cnt} elements differ (first flat idx {idx})"}
