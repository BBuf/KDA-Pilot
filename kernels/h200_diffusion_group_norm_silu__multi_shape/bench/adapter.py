"""Task adapter for bench/benchmark.py (the standard template).

Calling convention (documented in docs/benchmark_method.md; revised after the
pre-freeze review to make the timed glue structurally symmetric):

* Both sides allocate their output tensor per timed call and rebind it into
  the output container (`{"y": ...}`). The copied SGLang baseline does this
  internally (its public entry returns a fresh tensor — upstream production
  behavior, unmodified); the candidate wrapper mirrors it with one
  `torch.empty_like` per call before its destination-passing FFI kernel. Both
  sides therefore pay one caching-allocator allocation per call and no
  device-to-device copies are added to either timed path.
* Output-poisoning semantics for stale-output/skipped-kernel detection live in
  bench/correctness.py, which drives the candidate's destination-passing ABI
  with explicitly poisoned preallocated buffers. (With per-call rebinding the
  template's poison fill targets replaced tensors — equally inert for both
  sides; correctness still compares freshly produced outputs every trial.)
* Both call paths run under `torch.no_grad()` (the template disables grad in
  the worker; `make_case` asserts it) so the baseline's grad-mode eager
  fallback can never be measured silently.

Harness validation mode: setting `GNS_BENCH_CANDIDATE=baseline` wires
`call_candidate` to the baseline callable. Both sides then time identical
code — the A/A run must report geomean ~= 1.0. This mode exists only to
validate the harness before the baseline numbers freeze; real candidate runs
leave the variable unset.
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
    group_norm_silu_baseline,
    group_norm_silu_baseline_apply,
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
        from solution.binding import group_norm_silu_candidate

        _candidate_fn = group_norm_silu_candidate
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
        baseline_outputs={"y": None},
        candidate_outputs={"y": None},
        tolerance={
            "atol": float(workload.get("atol", 3e-3)),
            "rtol": float(workload.get("rtol", 3e-3)),
        },
    )


def _call_baseline_into(workload: dict, inputs: dict, outputs: dict) -> None:
    if workload.get("function") == "apply_group_norm_silu":
        outputs["y"] = group_norm_silu_baseline_apply(
            inputs["x"], inputs["norm"], inputs["activation"]
        )
    else:
        outputs["y"] = group_norm_silu_baseline(
            inputs["x"],
            inputs["weight"],
            inputs["bias"],
            inputs["num_groups"],
            inputs["eps"],
        )


def call_baseline(workload: dict, inputs: dict, outputs: dict) -> None:
    _call_baseline_into(workload, inputs, outputs)


def call_candidate(workload: dict, inputs: dict, outputs: dict) -> None:
    if _AA_MODE:
        _call_baseline_into(workload, inputs, outputs)
        return
    # Per-call output allocation mirrors the baseline's internal behavior
    # (its public entry allocates and returns a fresh tensor each call), so
    # both timed paths carry one caching-allocator allocation per invocation.
    out = torch.empty_like(inputs["x"])
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
            out,
        )
    else:
        _candidate()(
            inputs["x"],
            inputs["weight"],
            inputs["bias"],
            inputs["num_groups"],
            inputs["eps"],
            out,
        )
    outputs["y"] = out
