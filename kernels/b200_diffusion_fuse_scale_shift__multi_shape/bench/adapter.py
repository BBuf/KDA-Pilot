"""Benchmark adapter for b200_diffusion_fuse_scale_shift__multi_shape.

Supplies tensor construction and the two ABI calls for bench/benchmark.py.
``call_baseline`` and ``call_candidate`` route through one shared dispatch
helper over pre-resolved function tables, so both sides pay byte-identical
adapter overhead. Neither call allocates output tensors: outputs are
preallocated in ``make_case`` and poisoned/timed by the benchmark template.

The baseline side calls the copied SGLang Triton implementation through the
destination-passing launchers in baseline/binding.py. The candidate side calls
the CUDA module built from solution/kernel.cu via tvm-ffi. No sglang import
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
    "int32": torch.int32,
    "int64": torch.int64,
}

_EP1 = "fuse_scale_shift"
_EP2 = "fuse_layernorm_scale_shift_gate_select01"
_EP3 = "fuse_residual_layernorm_scale_shift_gate_select01"

_candidate_module = load_candidate_module()

_BASELINE_FNS = {
    _EP1: _baseline.fuse_scale_shift,
    _EP2: _baseline.fuse_layernorm_scale_shift_gate_select01,
    _EP3: _baseline.fuse_residual_layernorm_scale_shift_gate_select01,
}
_CANDIDATE_FNS = {
    _EP1: _candidate_module.fuse_scale_shift,
    _EP2: _candidate_module.fuse_layernorm_scale_shift_gate_select01,
    _EP3: _candidate_module.fuse_residual_layernorm_scale_shift_gate_select01,
}


def _randn(shape, dtype, device):
    return torch.randn(shape, device=device, dtype=dtype)


def _validate_against_spec(name: str, tensor: torch.Tensor, spec: dict) -> None:
    """Fail before benchmarking if a constructed tensor diverges from the
    frozen workload metadata (shape/stride/storage offset self-description)."""
    if list(tensor.shape) != list(spec["shape"]):
        raise ValueError(
            f"{name}: constructed shape {tuple(tensor.shape)} != frozen spec {spec['shape']}"
        )
    want_stride = spec.get("stride")
    if want_stride is not None and list(tensor.stride()) != list(want_stride):
        raise ValueError(
            f"{name}: constructed stride {tuple(tensor.stride())} != frozen spec {want_stride}"
        )
    want_offset = spec.get("storage_offset_elems")
    if want_offset is not None and tensor.storage_offset() != want_offset:
        raise ValueError(
            f"{name}: constructed storage offset {tensor.storage_offset()} != frozen spec {want_offset}"
        )


def _make_scale_shift_pair(shapes, device):
    """Build (scale, shift) per the workload's recorded layout."""
    scale_spec, shift_spec = shapes["scale"], shapes["shift"]
    layout = scale_spec.get("layout", "contiguous")
    if layout == "chunk2":
        # Chunked-modulation pattern: one fp32 parent [B, S, 2C]; shift is the
        # first half, scale the second. Both views are non-contiguous with a
        # contiguous last dim and doubled row stride (2SC, 2C, 1).
        b, s, c = scale_spec["shape"]
        parent = _randn((b, s, 2 * c), _DTYPES[scale_spec["dtype"]], device)
        shift = parent[:, :, :c]
        scale = parent[:, :, c:]
        assert not scale.is_contiguous() and not shift.is_contiguous()
        return scale, shift
    scale = _randn(scale_spec["shape"], _DTYPES[scale_spec["dtype"]], device)
    shift = _randn(shift_spec["shape"], _DTYPES[shift_spec["dtype"]], device)
    return scale, shift


def make_case(workload: dict, *, device: torch.device, seed: int) -> dict:
    del seed  # benchmark.py already seeded the global generators
    fn = workload["function"]
    shapes = workload["shapes"]
    x = _randn(shapes["x"]["shape"], _DTYPES[shapes["x"]["dtype"]], device)

    _validate_against_spec("x", x, shapes["x"])

    if fn == _EP1:
        scale, shift = _make_scale_shift_pair(shapes, device)
        _validate_against_spec("scale", scale, shapes["scale"])
        _validate_against_spec("shift", shift, shapes["shift"])
        inputs = {
            "x": x,
            "scale": scale,
            "shift": shift,
            "scale_constant": float(workload["scale_constant"]),
        }
        baseline_outputs = [torch.empty_like(x)]
        candidate_outputs = [torch.empty_like(x)]
    elif fn in (_EP2, _EP3):
        b, s, c = shapes["x"]["shape"]
        mod_dtype = _DTYPES[shapes["mod"]["dtype"]]
        mods = {
            name: _randn(shapes["mod"]["shape"], mod_dtype, device)
            for name in ("scale0", "shift0", "gate0", "scale1", "shift1", "gate1")
        }
        for name, mod in mods.items():
            _validate_against_spec(name, mod, shapes["mod"])
        index = torch.randint(
            0, 2, shapes["index"]["shape"],
            device=device, dtype=_DTYPES[shapes["index"]["dtype"]],
        )
        _validate_against_spec("index", index, shapes["index"])
        weight = bias = None
        if shapes.get("weight"):
            weight = _randn(shapes["weight"]["shape"], _DTYPES[shapes["weight"]["dtype"]], device)
            _validate_against_spec("weight", weight, shapes["weight"])
        if shapes.get("bias"):
            bias = _randn(shapes["bias"]["shape"], _DTYPES[shapes["bias"]["dtype"]], device)
            _validate_against_spec("bias", bias, shapes["bias"])
        inputs = {
            "x": x, "weight": weight, "bias": bias, **mods,
            "index": index, "eps": float(workload["eps"]),
        }
        if fn == _EP3:
            inputs["residual"] = _randn(shapes["residual"]["shape"], _DTYPES[shapes["residual"]["dtype"]], device)
            inputs["residual_gate"] = _randn(shapes["residual_gate"]["shape"], _DTYPES[shapes["residual_gate"]["dtype"]], device)
            _validate_against_spec("residual", inputs["residual"], shapes["residual"])
            _validate_against_spec("residual_gate", inputs["residual_gate"], shapes["residual_gate"])
            n_out = 3
        else:
            n_out = 2
        baseline_outputs = [torch.empty_like(x) for _ in range(n_out)]
        candidate_outputs = [torch.empty_like(x) for _ in range(n_out)]
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
    if fn == _EP1:
        impl(inputs["x"], inputs["scale"], inputs["shift"], inputs["scale_constant"], outputs[0])
    elif fn == _EP2:
        impl(
            inputs["x"], inputs["weight"], inputs["bias"],
            inputs["scale0"], inputs["shift0"], inputs["gate0"],
            inputs["scale1"], inputs["shift1"], inputs["gate1"],
            inputs["index"], inputs["eps"], outputs[0], outputs[1],
        )
    else:
        impl(
            inputs["x"], inputs["residual"], inputs["residual_gate"],
            inputs["weight"], inputs["bias"],
            inputs["scale0"], inputs["shift0"], inputs["gate0"],
            inputs["scale1"], inputs["shift1"], inputs["gate1"],
            inputs["index"], inputs["eps"], outputs[0], outputs[1], outputs[2],
        )


def call_baseline(workload: dict, inputs, outputs) -> None:
    _dispatch(_BASELINE_FNS, workload, inputs, outputs)


def call_candidate(workload: dict, inputs, outputs) -> None:
    _dispatch(_CANDIDATE_FNS, workload, inputs, outputs)
