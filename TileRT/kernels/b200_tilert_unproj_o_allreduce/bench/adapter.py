"""Benchmark adapter for b200_tilert_unproj_o_allreduce (generated).
Exposes baseline (PyTorch golden) / candidate (CUDA) ABI calls. The activation
input synthesis mirrors harness/tilert_oracle.py case_unproj_o_allreduce."""
from __future__ import annotations
import os, sys, torch
TASK_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if TASK_DIR not in sys.path: sys.path.insert(0, TASK_DIR)
from baseline.unproj_o_allreduce import unproj_o_allreduce_baseline, make_inputs  # noqa: E402

try:
    from solution.binding import unproj_o_allreduce_candidate  # noqa: E402 (KDA agent writes this)
except Exception:
    unproj_o_allreduce_candidate = None

def call_baseline(inp):   return unproj_o_allreduce_baseline(**inp)
def call_candidate(inp):
    assert unproj_o_allreduce_candidate is not None, "solution/binding.py:unproj_o_allreduce_candidate missing"
    return unproj_o_allreduce_candidate(**inp)
