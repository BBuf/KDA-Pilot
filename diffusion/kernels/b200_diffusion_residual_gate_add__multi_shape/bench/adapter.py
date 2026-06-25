"""Benchmark adapter for b200_diffusion_residual_gate_add__multi_shape.

Supplies tensor construction and the two ABI calls for bench/benchmark.py.
``call_baseline`` and ``call_candidate`` route through one shared dispatch
helper over pre-resolved function tables, so both sides pay byte-identical
adapter overhead. Neither call allocates output tensors: outputs are
preallocated in ``make_case`` and poisoned/timed by the benchmark template.

The baseline side calls the faithful PyTorch-eager launchers in
baseline/binding.py; the candidate side calls the CUDA module built from
solution/kernel.cu via tvm-ffi. No sglang import anywhere in this process
(asserted below).
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

_EP_RGA = "residual_gate_add"
_EP_BCAST = "broadcast_add_4d"

_candidate_module = load_candidate_module()

_BASELINE_FNS = {
    _EP_RGA: _baseline.residual_gate_add,
    _EP_BCAST: _baseline.broadcast_add_4d,
}
_CANDIDATE_FNS = {
    _EP_RGA: _candidate_module.residual_gate_add,
    _EP_BCAST: _candidate_module.broadcast_add_4d,
}


def _randn(shape, dtype, device):
    return torch.randn(shape, device=device, dtype=dtype)


def _validate_against_spec(name: str, tensor: torch.Tensor, spec: dict) -> None:
    """Fail before benchmarking if a constructed tensor diverges from the frozen
    workload metadata (shape/stride self-description)."""
    if list(tensor.shape) != list(spec["shape"]):
        raise ValueError(
            f"{name}: constructed shape {tuple(tensor.shape)} != frozen spec {spec['shape']}"
        )
    want_stride = spec.get("stride")
    if want_stride is not None and list(tensor.stride()) != list(want_stride):
        raise ValueError(
            f"{name}: constructed stride {tuple(tensor.stride())} != frozen spec {want_stride}"
        )


def make_case(workload: dict, *, device: torch.device, seed: int) -> dict:
    del seed  # benchmark.py already seeded the global generators
    fn = workload["function"]
    shapes = workload["shapes"]

    if fn == _EP_RGA:
        residual = _randn(shapes["residual"]["shape"], _DTYPES[shapes["residual"]["dtype"]], device)
        update = _randn(shapes["update"]["shape"], _DTYPES[shapes["update"]["dtype"]], device)
        gate = _randn(shapes["gate"]["shape"], _DTYPES[shapes["gate"]["dtype"]], device)
        _validate_against_spec("residual", residual, shapes["residual"])
        _validate_against_spec("update", update, shapes["update"])
        _validate_against_spec("gate", gate, shapes["gate"])
        inputs = {"residual": residual, "update": update, "gate": gate}
        baseline_outputs = [torch.empty_like(residual)]
        candidate_outputs = [torch.empty_like(residual)]
    elif fn == _EP_BCAST:
        a = _randn(shapes["a"]["shape"], _DTYPES[shapes["a"]["dtype"]], device)
        b = _randn(shapes["b"]["shape"], _DTYPES[shapes["b"]["dtype"]], device)
        _validate_against_spec("a", a, shapes["a"])
        _validate_against_spec("b", b, shapes["b"])
        inputs = {"a": a, "b": b}
        baseline_outputs = [torch.empty_like(b)]
        candidate_outputs = [torch.empty_like(b)]
    else:
        raise ValueError(f"unknown function {fn!r}")

    return {
        "inputs": inputs,
        "baseline_outputs": baseline_outputs,
        "candidate_outputs": candidate_outputs,
        "tolerance": {"atol": float(workload["atol"]), "rtol": float(workload["rtol"])},
    }


def _dispatch(fns: dict, workload: dict, inputs: dict, outputs) -> None:
    fn = workload["function"]
    impl = fns[fn]
    if fn == _EP_RGA:
        impl(inputs["residual"], inputs["update"], inputs["gate"], outputs[0])
    else:
        impl(inputs["a"], inputs["b"], outputs[0])


def call_baseline(workload: dict, inputs, outputs) -> None:
    _dispatch(_BASELINE_FNS, workload, inputs, outputs)


def call_candidate(workload: dict, inputs, outputs) -> None:
    _dispatch(_CANDIDATE_FNS, workload, inputs, outputs)
