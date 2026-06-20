"""Benchmark adapter for b200_tilert_expert_select_up_gate_silu (generated).
Exposes baseline (PyTorch golden) / candidate (CUDA) ABI calls. The activation
input synthesis mirrors harness/tilert_oracle.py case_expert_select_up_gate_silu."""
from __future__ import annotations
import os, sys, torch
TASK_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if TASK_DIR not in sys.path: sys.path.insert(0, TASK_DIR)
from baseline.expert_select_up_gate_silu import expert_select_up_gate_silu_baseline, make_inputs  # noqa: E402

try:
    from solution.binding import expert_select_up_gate_silu_candidate  # noqa: E402 (KDA agent writes this)
except Exception:
    expert_select_up_gate_silu_candidate = None

def call_baseline(inp):   return expert_select_up_gate_silu_baseline(**inp)
def call_candidate(inp):
    assert expert_select_up_gate_silu_candidate is not None, "solution/binding.py:expert_select_up_gate_silu_candidate missing"
    return expert_select_up_gate_silu_candidate(**inp)
