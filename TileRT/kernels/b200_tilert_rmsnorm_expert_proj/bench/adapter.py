"""Benchmark adapter for b200_tilert_rmsnorm_expert_proj (generated).
Exposes baseline (PyTorch golden) / candidate (CUDA) ABI calls. The activation
input synthesis mirrors harness/tilert_oracle.py case_rmsnorm_expert_proj."""
from __future__ import annotations
import os, sys, torch
TASK_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if TASK_DIR not in sys.path: sys.path.insert(0, TASK_DIR)
from baseline.rmsnorm_expert_proj import rmsnorm_expert_proj_baseline, make_inputs  # noqa: E402

try:
    from solution.binding import rmsnorm_expert_proj_candidate  # noqa: E402 (KDA agent writes this)
except Exception:
    rmsnorm_expert_proj_candidate = None

def call_baseline(inp):   return rmsnorm_expert_proj_baseline(**inp)
def call_candidate(inp):
    assert rmsnorm_expert_proj_candidate is not None, "solution/binding.py:rmsnorm_expert_proj_candidate missing"
    return rmsnorm_expert_proj_candidate(**inp)
