"""Benchmark adapter for b200_tilert_rmsnorm (generated).
Exposes baseline (PyTorch golden) / candidate (CUDA) ABI calls. The activation
input synthesis mirrors harness/tilert_oracle.py case_rmsnorm."""
from __future__ import annotations
import os, sys, torch
TASK_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if TASK_DIR not in sys.path: sys.path.insert(0, TASK_DIR)
from baseline.rmsnorm import rmsnorm_baseline, make_inputs  # noqa: E402

try:
    from solution.binding import rmsnorm_candidate  # noqa: E402 (KDA agent writes this)
except Exception:
    rmsnorm_candidate = None

def call_baseline(inp):   return rmsnorm_baseline(**inp)
def call_candidate(inp):
    assert rmsnorm_candidate is not None, "solution/binding.py:rmsnorm_candidate missing"
    return rmsnorm_candidate(**inp)
