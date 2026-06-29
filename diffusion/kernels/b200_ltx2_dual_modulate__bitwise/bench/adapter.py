"""Benchmark adapter for b200_ltx2_dual_modulate__bitwise.

The baseline is the real SGLang LTX2.3 production expression under CUDA bf16
autocast. The visible dual-modulation outputs are fp32 tensors for the live
rows; candidate kernels must match those bits and must not depend on repeated
C++ exceptions or dtype-mismatch fallback in the hot path.
"""

from __future__ import annotations

import sys
from pathlib import Path

_TASK_ROOT = Path(__file__).resolve().parents[1]
if str(_TASK_ROOT) not in sys.path:
    sys.path.insert(0, str(_TASK_ROOT))

import torch

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

_CANDIDATE_FNS = None


def _production_autocast(device: torch.device):
    return torch.autocast(
        device_type=device.type,
        dtype=torch.bfloat16,
        enabled=device.type == "cuda",
    )


def _load_candidate_fns():
    global _CANDIDATE_FNS
    if _CANDIDATE_FNS is not None:
        return _CANDIDATE_FNS
    try:
        from solution.build import load_candidate_module  # type: ignore
    except Exception as exc:  # noqa: BLE001
        raise RuntimeError(
            "solution candidate is intentionally empty. Generate solution/build.py "
            "and solution/kernel.cu with the two dual-modulation entry points "
            f"before calling the candidate. Import error: {exc}"
        ) from exc
    candidate = load_candidate_module()
    _CANDIDATE_FNS = {
        _EXPLICIT: candidate.ltx2_dual_modulate_candidate,
        _CA: candidate.ltx2_ca_dual_modulate_from_temb_candidate,
    }
    return _CANDIDATE_FNS


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


def _contig_stride(shape) -> list:
    st = [1] * len(shape)
    for i in range(len(shape) - 2, -1, -1):
        st[i] = st[i + 1] * shape[i + 1]
    return st


def _from_spec(spec: dict, device) -> torch.Tensor:
    """Build a tensor matching the frozen spec's shape AND stride. Contiguous specs
    use a plain randn; any non-contiguous spec (the packed [B,1,D] production params,
    or [B,D]/[B,S,D] layouts) is reproduced exactly via as_strided over a randn parent
    of sufficient storage."""
    shape = list(spec["shape"])
    dtype = _DTYPES[spec["dtype"]]
    stride = spec.get("stride")
    if stride is None or list(stride) == _contig_stride(shape):
        return _randn(shape, dtype, device)
    storage = 1 + sum((s - 1) * st for s, st in zip(shape, stride) if s > 0)
    return _randn((storage,), dtype, device).as_strided(shape, list(stride))


def make_case(workload: dict, *, device: torch.device, seed: int) -> dict:
    del seed  # benchmark.py already seeded the global generators
    fn = workload["function"]
    shapes = workload["shapes"]
    x = _from_spec(shapes["x"], device)
    _validate_against_spec("x", x, shapes["x"])
    eps = float(workload.get("eps", 1e-6))

    if fn == _EXPLICIT:
        inputs = {"x": x, "eps": eps}
        for name in ("scale0", "shift0", "scale1", "shift1"):
            inputs[name] = _from_spec(shapes[name], device)
            _validate_against_spec(name, inputs[name], shapes[name])
    elif fn == _CA:
        temb = _from_spec(shapes["temb_scale_shift"], device)
        _validate_against_spec("temb_scale_shift", temb, shapes["temb_scale_shift"])
        table = _from_spec(shapes["scale_shift_table"], device)
        _validate_against_spec("scale_shift_table", table, shapes["scale_shift_table"])
        inputs = {"x": x, "eps": eps, "temb_scale_shift": temb, "scale_shift_table": table}
    else:
        raise ValueError(f"unknown function {fn!r}")

    return {
        "inputs": inputs,
        "baseline_outputs": [
            torch.empty_like(x, dtype=torch.float32),
            torch.empty_like(x, dtype=torch.float32),
        ],
        "candidate_outputs": [
            torch.empty_like(x, dtype=torch.float32),
            torch.empty_like(x, dtype=torch.float32),
        ],
        "tolerance": {"atol": float(workload.get("atol", 0.0)), "rtol": float(workload.get("rtol", 0.0))},
    }


def _bcast_param(param: torch.Tensor) -> torch.Tensor:
    return param.unsqueeze(1) if param.dim() == 2 else param


def _reference_explicit(inputs):
    x = inputs["x"]
    with _production_autocast(x.device):
        normed = torch.nn.functional.rms_norm(x, (x.shape[-1],), eps=inputs["eps"])
        y0 = normed * (1 + _bcast_param(inputs["scale0"])) + _bcast_param(inputs["shift0"])
        y1 = normed * (1 + _bcast_param(inputs["scale1"])) + _bcast_param(inputs["shift1"])
    return y0, y1


def _reference_ca(inputs):
    x = inputs["x"]
    temb = inputs["temb_scale_shift"]
    table = inputs["scale_shift_table"]
    B, _, D = x.shape
    temb_seq = temb.shape[1]
    with _production_autocast(x.device):
        combined = (
            table.to(dtype=temb.dtype, device=temb.device).reshape(1, 1, 4, D)
            + temb.reshape(B, temb_seq, 4, D)
        )
        scale0, shift0, scale1, shift1 = combined.unbind(dim=2)
        normed = torch.nn.functional.rms_norm(x, (D,), eps=inputs["eps"])
        y0 = normed * (1 + scale0) + shift0
        y1 = normed * (1 + scale1) + shift1
    return y0, y1


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
    fn = workload["function"]
    if fn == _EXPLICIT:
        y0, y1 = _reference_explicit(inputs)
    elif fn == _CA:
        y0, y1 = _reference_ca(inputs)
    else:
        raise ValueError(f"unknown function {fn!r}")
    outputs[0].copy_(y0)
    outputs[1].copy_(y1)


def call_candidate(workload: dict, inputs, outputs) -> None:
    with _production_autocast(inputs["x"].device):
        _dispatch(_load_candidate_fns(), workload, inputs, outputs)


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
