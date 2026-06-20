"""Benchmark adapter for b200_tilert_padded_allreduce_add (generated).
Exposes baseline (PyTorch golden) / candidate (CUDA) ABI calls. The activation
input synthesis mirrors harness/tilert_oracle.py case_padded_allreduce_add."""
from __future__ import annotations
import os, sys, torch
TASK_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if TASK_DIR not in sys.path: sys.path.insert(0, TASK_DIR)
from baseline.padded_allreduce_add import padded_allreduce_add_baseline, make_inputs  # noqa: E402

try:
    from solution.binding import padded_allreduce_add_candidate  # noqa: E402 (KDA agent writes this)
except Exception:
    padded_allreduce_add_candidate = None

def call_baseline(inp):   return padded_allreduce_add_baseline(**inp)
def call_candidate(inp):
    assert padded_allreduce_add_candidate is not None, "solution/binding.py:padded_allreduce_add_candidate missing"
    return padded_allreduce_add_candidate(**inp)
