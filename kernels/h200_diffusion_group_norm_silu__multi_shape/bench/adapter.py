"""Task adapter for bench/benchmark.py (the standard template).

Calling convention — exactly the template contract:

* `make_case` preallocates one output tensor per side
  (`{"y": torch.empty_like(x)}`); `call_baseline` / `call_candidate` write
  into those buffers through destination-passing local ABIs and never
  allocate output tensors in the timed path. The template's output-poisoning
  check is therefore fully effective on BOTH sides every trial.
* Baseline side: `baseline/binding.py`'s destination-passing wrappers drive
  the copied Triton kernels with the caller's buffer (launcher bodies
  replicated verbatim; internal scratch allocations kept as upstream wrote
  them). The wrappers REFUSE the upstream eager fallback, so a non-Triton
  baseline can never be timed silently.
* Candidate side: `solution/binding.py::group_norm_silu_candidate_into`
  (solution-owned CUDA kernels for every regime).
* Wrapper rows (`apply_group_norm_silu`): the GroupNorm/SiLU modules are
  built in `make_case` (outside timing); BOTH sides unpack the module
  attributes inside the timed call for parity with the upstream wrapper.
* Both call paths run under `torch.no_grad()` (the template disables grad in
  the worker; `make_case` asserts it) so the baseline's grad-mode eager
  fallback can never be measured silently.

Harness validation mode: setting `GNS_BENCH_CANDIDATE=baseline` wires
`call_candidate` to the baseline destination-passing wrapper. Both sides then
time identical code — the A/A run must report geomean ~= 1.0. This mode
exists only to validate the harness; real candidate runs leave it unset.
"""

from __future__ import annotations

import os
import sys
from pathlib import Path
from typing import Any

import torch
from torch import nn

TASK_ROOT = Path(__file__).resolve().parents[1]
if str(TASK_ROOT) not in sys.path:
    sys.path.insert(0, str(TASK_ROOT))

from baseline.binding import (  # noqa: E402
    group_norm_silu_baseline_apply_into,
    group_norm_silu_baseline_into,
    triton_path_active,
)

_AA_MODE = os.environ.get("GNS_BENCH_CANDIDATE", "") == "baseline"

# The standalone contract forbids any sglang import at benchmark runtime; the
# copied baseline and the solution loader must never pull it in transitively.
_LEAKED = sorted(m for m in sys.modules if m == "sglang" or m.startswith("sglang."))
if _LEAKED:
    raise ImportError(f"purity violation: sglang modules loaded: {_LEAKED[:5]}")

_candidate_fn = None


def _candidate():
    """Load the solution kernel callable once per process (build cost lands
    outside the timed region: first call happens in make_case/correctness)."""
    global _candidate_fn
    if _candidate_fn is None:
        from solution.binding import group_norm_silu_candidate_into

        _candidate_fn = group_norm_silu_candidate_into
        leaked = sorted(
            m for m in sys.modules if m == "sglang" or m.startswith("sglang.")
        )
        if leaked:
            raise ImportError(
                f"purity violation after solution import: {leaked[:5]}"
            )
    return _candidate_fn


class Case:
    """Plain attribute container (the template loads this module via
    spec_from_file_location without registering it in sys.modules, which
    breaks dataclass annotation introspection under Python 3.12)."""

    def __init__(
        self,
        inputs: dict[str, Any],
        baseline_outputs: dict[str, Any],
        candidate_outputs: dict[str, Any],
        tolerance: dict[str, float] | None = None,
    ) -> None:
        self.inputs = inputs
        self.baseline_outputs = baseline_outputs
        self.candidate_outputs = candidate_outputs
        self.tolerance = tolerance or {}


_DTYPES = {"float16": torch.float16, "bfloat16": torch.bfloat16, "float32": torch.float32}


def make_case(workload: dict, *, device: torch.device, seed: int) -> Case:
    assert not torch.is_grad_enabled(), (
        "harness must run under no_grad: the upstream baseline silently routes "
        "to eager F.group_norm+silu when grad is enabled"
    )
    del seed  # the template seeds torch's RNG before calling make_case

    shape = tuple(workload["shapes"]["x"])
    dtype = _DTYPES[workload.get("dtype", "float16")]
    num_groups = int(workload["num_groups"])
    eps = float(workload["eps"])
    channels = shape[1]

    x = torch.randn(shape, device=device, dtype=dtype)
    weight = torch.randn(channels, device=device, dtype=dtype)
    bias = torch.randn(channels, device=device, dtype=dtype)

    inputs: dict[str, Any] = {
        "x": x,
        "weight": weight,
        "bias": bias,
        "num_groups": num_groups,
        "eps": eps,
    }

    function = workload.get("function", "triton_group_norm_silu")
    if function == "apply_group_norm_silu":
        norm = nn.GroupNorm(num_groups, channels, eps=eps, affine=True)
        norm = norm.to(device=device, dtype=dtype)
        with torch.no_grad():
            norm.weight.copy_(weight)
            norm.bias.copy_(bias)
        norm.requires_grad_(False)
        inputs["norm"] = norm
        inputs["activation"] = nn.SiLU()
    elif function != "triton_group_norm_silu":
        raise ValueError(f"unknown workload function: {function}")

    # Production rows must exercise the baseline's real Triton path; refuse to
    # measure a case where the upstream gate would route to eager.
    if workload.get("production", True) and not triton_path_active(
        x, weight, bias, num_groups
    ):
        raise RuntimeError(
            f"baseline would take the eager fallback for workload "
            f"{workload.get('id')}: shape={shape} dtype={dtype}"
        )

    if not _AA_MODE:
        _candidate()  # trigger JIT build here, outside the timed region

    return Case(
        inputs=inputs,
        baseline_outputs={"y": torch.empty_like(x)},
        candidate_outputs={"y": torch.empty_like(x)},
        tolerance={
            "atol": float(workload.get("atol", 3e-3)),
            "rtol": float(workload.get("rtol", 3e-3)),
        },
    )


def _baseline_into(workload: dict, inputs: dict, out: torch.Tensor) -> None:
    if workload.get("function") == "apply_group_norm_silu":
        group_norm_silu_baseline_apply_into(
            inputs["x"], inputs["norm"], inputs["activation"], out
        )
    else:
        group_norm_silu_baseline_into(
            inputs["x"],
            inputs["weight"],
            inputs["bias"],
            inputs["num_groups"],
            inputs["eps"],
            out,
        )


def call_baseline(workload: dict, inputs: dict, outputs: dict) -> None:
    _baseline_into(workload, inputs, outputs["y"])


def call_candidate(workload: dict, inputs: dict, outputs: dict) -> None:
    if _AA_MODE:
        _baseline_into(workload, inputs, outputs["y"])
        return
    if workload.get("function") == "apply_group_norm_silu":
        # Module-attribute extraction stays inside the timed call for parity
        # with the baseline wrapper, which unpacks the same attributes per call.
        norm = inputs["norm"]
        _candidate()(
            inputs["x"],
            norm.weight,
            norm.bias,
            int(norm.num_groups),
            float(norm.eps),
            outputs["y"],
        )
    else:
        _candidate()(
            inputs["x"],
            inputs["weight"],
            inputs["bias"],
            inputs["num_groups"],
            inputs["eps"],
            outputs["y"],
        )
