"""Benchmark adapter for b200_tilert_eh_proj_allreduce (generated).
Exposes baseline (PyTorch golden) / candidate (CUDA) ABI calls. The activation
input synthesis mirrors harness/tilert_oracle.py case_eh_proj_allreduce."""
from __future__ import annotations
import os, sys, torch
TASK_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if TASK_DIR not in sys.path: sys.path.insert(0, TASK_DIR)
from baseline.eh_proj_allreduce import eh_proj_allreduce_baseline, make_inputs  # noqa: E402

try:
    from solution.binding import eh_proj_allreduce_candidate  # noqa: E402 (KDA agent writes this)
except Exception:
    eh_proj_allreduce_candidate = None

def call_baseline(inp):   return eh_proj_allreduce_baseline(**inp)
def call_candidate(inp):
    assert eh_proj_allreduce_candidate is not None, "solution/binding.py:eh_proj_allreduce_candidate missing"
    return eh_proj_allreduce_candidate(**inp)
