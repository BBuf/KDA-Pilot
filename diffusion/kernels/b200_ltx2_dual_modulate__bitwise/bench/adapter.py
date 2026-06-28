"""Benchmark adapter for b200_ltx2_dual_modulate__bitwise.

Both the baseline and the candidate are full-operation TVM-FFI CUDA modules taking
`(x, params/temb/table, eps, y0, y1)`; the adapter just constructs tensors and
dispatches. Neither call allocates the output tensors (preallocated in make_case).
`compare_outputs` enforces BITWISE equality with `torch.equal` (this task's
contract), overriding the template's allclose default. No sglang import.
"""

from __future__ import annotations

import sys
from pathlib import Path

_TASK_ROOT = Path(__file__).resolve().parents[1]
if str(_TASK_ROOT) not in sys.path:
    sys.path.insert(0, str(_TASK_ROOT))

import torch

from baseline.build import load_baseline_module
from solution.build import load_candidate_module

assert not any(
    name == "sglang" or name.startswith("sglang.") for name in sys.modules
), "standalone contract violation: sglang imported at benchmark runtime"

_DTYPES = {
    "bfloat16": torch.bfloat16,
    "float16": torch.float16,
    "float32": torch.float32,
}

_EXPLICIT = "dual_modulate"
_CA = "ca_dual_modulate_from_temb"

_baseline = load_baseline_module()
_candidate = load_candidate_module()

_BASELINE_FNS = {
    _EXPLICIT: _baseline.ltx2_dual_modulate_baseline,
    _CA: _baseline.ltx2_ca_dual_modulate_from_temb_baseline,
}
_CANDIDATE_FNS = {
    _EXPLICIT: _candidate.ltx2_dual_modulate_candidate,
    _CA: _candidate.ltx2_ca_dual_modulate_from_temb_candidate,
}


def _randn(shape, dtype, device):
    return torch.randn(shape, device=device, dtype=dtype)


def _validate_against_spec(name: str, tensor: torch.Tensor, spec: dict) -> None:
    if list(tensor.shape) != list(spec["shape"]):
        raise ValueError(
            f"{name}: constructed shape {tuple(tensor.shape)} != frozen spec {spec['shape']}"
        )
    want_stride = spec.get("stride")
    if want_stride is not None and list(tensor.stride()) != list(want_stride):
        raise ValueError(
            f"{name}: constructed stride {tuple(tensor.stride())} != frozen spec {want_stride}"
        )


def _make_explicit_params(shapes, device):
    """scale0/shift0/scale1/shift1 are recorded as views with stride [4D, 4D, 1]
    (slices of a packed [B, 1, 4D] parent). Reproduce that layout so the frozen
    strides match and the broadcast-over-S path is exercised."""
    spec = shapes["scale0"]
    b, mid, d = spec["shape"]
    dtype = _DTYPES[spec["dtype"]]
    want_stride = spec.get("stride")
    packed_last = want_stride[0] if want_stride else d
    parent = _randn((b, mid, packed_last), dtype, device)
    out = {}
    for i, name in enumerate(("scale0", "shift0", "scale1", "shift1")):
        out[name] = parent[:, :, i * d : (i + 1) * d]
        _validate_against_spec(name, out[name], shapes[name])
    return out


def make_case(workload: dict, *, device: torch.device, seed: int) -> dict:
    del seed  # benchmark.py already seeded the global generators
    fn = workload["function"]
    shapes = workload["shapes"]
    x = _randn(shapes["x"]["shape"], _DTYPES[shapes["x"]["dtype"]], device)
    _validate_against_spec("x", x, shapes["x"])
    eps = float(workload.get("eps", 1e-6))

    if fn == _EXPLICIT:
        inputs = {"x": x, "eps": eps, **_make_explicit_params(shapes, device)}
    elif fn == _CA:
        temb = _randn(shapes["temb_scale_shift"]["shape"],
                      _DTYPES[shapes["temb_scale_shift"]["dtype"]], device)
        _validate_against_spec("temb_scale_shift", temb, shapes["temb_scale_shift"])
        table = _randn(shapes["scale_shift_table"]["shape"],
                       _DTYPES[shapes["scale_shift_table"]["dtype"]], device)
        _validate_against_spec("scale_shift_table", table, shapes["scale_shift_table"])
        inputs = {"x": x, "eps": eps, "temb_scale_shift": temb, "scale_shift_table": table}
    else:
        raise ValueError(f"unknown function {fn!r}")

    return {
        "inputs": inputs,
        "baseline_outputs": [torch.empty_like(x), torch.empty_like(x)],
        "candidate_outputs": [torch.empty_like(x), torch.empty_like(x)],
        "tolerance": {"atol": float(workload.get("atol", 0.0)), "rtol": float(workload.get("rtol", 0.0))},
    }


def _dispatch(fns, workload, inputs, outputs) -> None:
    fn = workload["function"]
    impl = fns[fn]
    if fn == _EXPLICIT:
        impl(inputs["x"], inputs["scale0"], inputs["shift0"], inputs["scale1"],
             inputs["shift1"], inputs["eps"], outputs[0], outputs[1])
    else:
        impl(inputs["x"], inputs["temb_scale_shift"], inputs["scale_shift_table"],
             inputs["eps"], outputs[0], outputs[1])


def call_baseline(workload: dict, inputs, outputs) -> None:
    _dispatch(_BASELINE_FNS, workload, inputs, outputs)


def call_candidate(workload: dict, inputs, outputs) -> None:
    _dispatch(_CANDIDATE_FNS, workload, inputs, outputs)


def compare_outputs(workload, baseline_outputs, candidate_outputs, tolerance) -> dict:
    """Bitwise gate: every output tensor must be torch.equal (atol=rtol=0)."""
    for i, (b, c) in enumerate(zip(baseline_outputs, candidate_outputs)):
        if b.shape != c.shape or b.dtype != c.dtype:
            return {"ok": False, "max_abs": float("inf"), "max_rel": float("inf"),
                    "message": f"output {i} shape/dtype mismatch"}
        if not torch.equal(b, c):
            diff = (b.to(torch.float32) - c.to(torch.float32)).abs()
            return {"ok": False, "max_abs": float(diff.max()), "max_rel": float("nan"),
                    "message": f"output {i} not bitwise equal (torch.equal failed)"}
    return {"ok": True, "max_abs": 0.0, "max_rel": 0.0, "message": "bitwise equal"}
