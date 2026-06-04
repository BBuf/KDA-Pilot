"""Adapter for bench/benchmark.py: tensor construction and the two ABI calls.

Both sides are exposed through the same allocation-return ABI (the upstream
entry points are torch custom ops that allocate outputs internally; see
``docs/benchmark_method.md``). Outputs are passed as mutable dicts and the
returned tensors are stored into them, so the template's compare logic reads
the same objects on both sides with identical wrapper overhead.
"""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import torch

TASK_DIR = Path(__file__).resolve().parents[1]
NSS = "fused_norm_scale_shift"
SRNSS = "fused_scale_residual_norm_scale_shift"

DTYPES = {
    "bfloat16": torch.bfloat16,
    "float16": torch.float16,
    "float32": torch.float32,
}

_BINDINGS: dict[str, object] = {}


def _load_binding(name: str, rel_path: str):
    # Reuse the process-wide module first: the benchmark's non-isolated mode
    # re-imports this adapter per workload with a fresh _BINDINGS cache, and
    # re-executing a binding would re-register its torch.library custom ops.
    module = _BINDINGS.get(name) or sys.modules.get(name)
    if module is None:
        path = TASK_DIR / rel_path
        spec = importlib.util.spec_from_file_location(name, path)
        if spec is None or spec.loader is None:
            raise RuntimeError(f"cannot import {path}")
        module = importlib.util.module_from_spec(spec)
        sys.modules[name] = module
        spec.loader.exec_module(module)
    _BINDINGS[name] = module
    return module


def baseline_binding():
    return _load_binding("kda_baseline_binding", "baseline/binding.py")


def candidate_binding():
    return _load_binding("kda_candidate_binding", "solution/binding.py")


def operand_shape(layout: str, B: int, S: int, D: int, F: int | None) -> tuple[int, ...]:
    if layout == "1":
        return (1,)
    if layout == "D":
        return (D,)
    if layout == "1D":
        return (1, D)
    if layout == "BD":
        return (B, D)
    if layout == "11D":
        return (1, 1, D)
    if layout == "1SD":
        return (1, S, D)
    if layout == "B1D":
        return (B, 1, D)
    if layout == "BSD":
        return (B, S, D)
    if layout == "BF1D":
        if not F:
            raise ValueError("BF1D layout requires F")
        return (B, F, 1, D)
    raise ValueError(f"unknown operand layout: {layout}")


def build_operand(spec, B: int, S: int, D: int, default_F: int | None, device) -> torch.Tensor | None:
    if spec is None:
        return None
    F = spec.get("F", default_F)
    shape = operand_shape(spec["layout"], B, S, D, F)
    return torch.randn(shape, dtype=DTYPES[spec["dtype"]], device=device)


def build_inputs(workload: dict, device) -> dict:
    shapes = workload["shapes"]
    B, S, D = shapes["B"], shapes["S"], shapes["D"]
    F = shapes.get("F")
    x = torch.randn((B, S, D), dtype=DTYPES[shapes["x"]["dtype"]], device=device)
    inputs = {
        "x": x,
        "weight": build_operand(shapes.get("weight"), B, S, D, F, device),
        "bias": build_operand(shapes.get("bias"), B, S, D, F, device),
        "scale": build_operand(shapes["scale"], B, S, D, F, device),
        "shift": build_operand(shapes["shift"], B, S, D, F, device),
        "norm_type": workload["norm_type"],
        "eps": float(workload["eps"]),
    }
    if workload["function"] == SRNSS:
        inputs["residual"] = torch.randn_like(x)
        inputs["gate"] = build_operand(shapes.get("gate"), B, S, D, F, device)
    return inputs


def make_case(workload: dict, *, device, seed: int):
    del seed  # the harness seeds torch RNG before calling make_case
    inputs = build_inputs(workload, device)
    if workload["function"] == NSS:
        baseline_outputs = {"y": None}
        candidate_outputs = {"y": None}
    elif workload["function"] == SRNSS:
        baseline_outputs = {"y": None, "res_out": None}
        candidate_outputs = {"y": None, "res_out": None}
    else:
        raise ValueError(f"unknown function {workload['function']}")
    return {
        "inputs": inputs,
        "baseline_outputs": baseline_outputs,
        "candidate_outputs": candidate_outputs,
        "tolerance": {"atol": float(workload["atol"]), "rtol": float(workload["rtol"])},
    }


def _call(module, workload: dict, inputs: dict, outputs: dict) -> None:
    if workload["function"] == NSS:
        outputs["y"] = module.fused_norm_scale_shift(
            inputs["x"], inputs["weight"], inputs["bias"],
            inputs["scale"], inputs["shift"], inputs["norm_type"], inputs["eps"],
        )
    else:
        y, res_out = module.fused_scale_residual_norm_scale_shift(
            inputs["residual"], inputs["x"], inputs["gate"],
            inputs["weight"], inputs["bias"],
            inputs["scale"], inputs["shift"], inputs["norm_type"], inputs["eps"],
        )
        outputs["y"] = y
        outputs["res_out"] = res_out


def call_baseline(workload: dict, inputs, outputs) -> None:
    _call(baseline_binding(), workload, inputs, outputs)


def call_candidate(workload: dict, inputs, outputs) -> None:
    _call(candidate_binding(), workload, inputs, outputs)
