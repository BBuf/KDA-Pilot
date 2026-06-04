"""Benchmark adapter for b200_diffusion_group_norm_silu__multi_shape.

Supplies tensor construction and the two ABI calls for the standard
standalone benchmark template (bench/benchmark.py). Both upstream entry points
(`triton_group_norm_silu`, `apply_group_norm_silu`) route to the SAME local
destination-passing call on each side (per-row `function` metadata is recorded
in the workload and results); wrapper overhead is therefore identical across
rows and across sides:

    baseline : baseline.group_norm_silu_baseline   (copied upstream Triton)
    candidate: solution.binding.group_norm_silu_candidate (CUDA tvm-ffi)

A/A harness-validity mode: set GNS_CANDIDATE_ALIAS_BASELINE=1 to alias the
candidate call to the baseline implementation (used once before tuning to
verify the harness reports geomean ~1.0; recorded in docs/benchmark_method.md).
"""

from __future__ import annotations

import os
import sys
from types import SimpleNamespace

import torch

TASK_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if TASK_DIR not in sys.path:
    sys.path.insert(0, TASK_DIR)

from baseline import group_norm_silu_baseline  # noqa: E402

_ALIAS_BASELINE = os.environ.get("GNS_CANDIDATE_ALIAS_BASELINE", "0") == "1"

if not _ALIAS_BASELINE:
    from solution.binding import group_norm_silu_candidate  # noqa: E402
else:  # A/A mode: candidate IS the baseline implementation
    group_norm_silu_candidate = group_norm_silu_baseline

_DTYPES = {
    "float16": torch.float16,
    "bfloat16": torch.bfloat16,
    "float32": torch.float32,
}


def _make_input(shapes: dict, device: torch.device) -> torch.Tensor:
    shape = tuple(shapes["x"])
    dtype = _DTYPES[shapes["dtype"]]
    layout = shapes["layout"]
    x = torch.randn(shape, device=device, dtype=torch.float32).to(dtype)
    if layout == "channels_last_3d":
        x = x.contiguous(memory_format=torch.channels_last_3d)
    elif layout != "contiguous":
        raise ValueError(f"unknown layout {layout!r}")
    expected = tuple(shapes["strides"])
    if tuple(x.stride()) != expected:
        raise RuntimeError(
            f"constructed strides {tuple(x.stride())} != captured {expected}"
        )
    return x


def make_case(workload: dict, *, device: torch.device, seed: int):
    shapes = workload["shapes"]
    dtype = _DTYPES[shapes["dtype"]]
    channels = shapes["x"][1]

    x = _make_input(shapes, device)
    weight = torch.randn(channels, device=device, dtype=torch.float32).to(dtype)
    bias = torch.randn(channels, device=device, dtype=torch.float32).to(dtype)

    # The upstream baseline returns a CONTIGUOUS tensor for every supported
    # input (it materializes x.contiguous() first); both sides therefore write
    # a preallocated contiguous output.
    baseline_out = torch.empty(tuple(shapes["x"]), device=device, dtype=dtype)
    candidate_out = torch.empty_like(baseline_out)

    return SimpleNamespace(
        inputs=(x, weight, bias, int(shapes["num_groups"]), float(shapes["eps"])),
        baseline_outputs=(baseline_out,),
        candidate_outputs=(candidate_out,),
        tolerance={"atol": float(workload["atol"]), "rtol": float(workload["rtol"])},
    )


def call_baseline(workload: dict, inputs, outputs) -> None:
    x, weight, bias, num_groups, eps = inputs
    group_norm_silu_baseline(x, weight, bias, num_groups, eps, outputs[0])


def call_candidate(workload: dict, inputs, outputs) -> None:
    x, weight, bias, num_groups, eps = inputs
    group_norm_silu_candidate(x, weight, bias, num_groups, eps, outputs[0])


def describe_paths(workload: dict, inputs, outputs) -> dict:
    """Optional reporting hook: per-row dispatch metadata for the result
    record (untimed; called with the same tensors used for timing)."""
    x, weight, bias, num_groups, _eps = inputs
    if _ALIAS_BASELINE:
        return {
            "candidate_path": "baseline_alias",
            "candidate_regime": "baseline_alias",
            "matched_status": "baseline_equivalent",
        }
    from solution.binding import describe_dispatch

    return describe_dispatch(x, weight, bias, num_groups, outputs[0])
