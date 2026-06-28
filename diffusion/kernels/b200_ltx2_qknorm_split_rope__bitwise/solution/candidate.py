"""Candidate entry point for the bench harness.

Staged design (plan lower bound):
  Stage 1 — RMSNorm: reuse the torch.nn.RMSNorm modules passed in `inputs`, so
            the norm output is bit-identical to the oracle by construction.
  Stage 2 — split RoPE: a single fused bit-exact CUDA kernel (solution/kernel.cu)
            replaces the eager `split_x*cos` + two `addcmul_` ops (fewer launches,
            no intermediate split/out allocations), while preserving the exact
            rounding points.

`run_candidate(inputs, outputs)` writes q_out into outputs[0] and k_out into
outputs[1] (destination-passing; no allocation of the output buffers here).
Imports nothing from sglang.
"""

import sys
from pathlib import Path

_TASK_ROOT = Path(__file__).resolve().parents[1]
if str(_TASK_ROOT) not in sys.path:
    sys.path.insert(0, str(_TASK_ROOT))


def _module():
    from solution.build import load_candidate_module

    return load_candidate_module()


def run_candidate(inputs, outputs):
    # Stage 1: bit-exact RMSNorm via the same torch modules the oracle uses.
    q_normed = inputs["q_norm"](inputs["q"])
    k_normed = inputs["k_norm"](inputs["k"])
    # Stage 2: fused bit-exact split RoPE (custom CUDA kernel), destination-passing.
    mod = _module()
    mod.ltx2_split_rope_candidate(q_normed, inputs["q_cos"], inputs["q_sin"], outputs[0])
    mod.ltx2_split_rope_candidate(k_normed, inputs["k_cos"], inputs["k_sin"], outputs[1])
