"""Benchmark adapter for b200_tilert_expert_down_allreduce (generated).
Exposes baseline (PyTorch golden) / candidate (CUDA) ABI calls. The activation
input synthesis mirrors harness/tilert_oracle.py case_expert_down_allreduce."""
from __future__ import annotations
import os, sys, torch
TASK_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if TASK_DIR not in sys.path: sys.path.insert(0, TASK_DIR)
from baseline.expert_down_allreduce import expert_down_allreduce_baseline, make_inputs  # noqa: E402

try:
    from solution.binding import expert_down_allreduce_candidate  # noqa: E402 (KDA agent writes this)
except Exception:
    expert_down_allreduce_candidate = None

def call_baseline(inp):   return expert_down_allreduce_baseline(**inp)
def call_candidate(inp):
    assert expert_down_allreduce_candidate is not None, "solution/binding.py:expert_down_allreduce_candidate missing"
    return expert_down_allreduce_candidate(**inp)
