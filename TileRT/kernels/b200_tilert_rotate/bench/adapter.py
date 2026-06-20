"""Benchmark adapter for b200_tilert_rotate (generated).
Exposes baseline (PyTorch golden) / candidate (CUDA) ABI calls. The activation
input synthesis mirrors harness/tilert_oracle.py case_rotate."""
from __future__ import annotations
import os, sys, torch
TASK_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if TASK_DIR not in sys.path: sys.path.insert(0, TASK_DIR)
from baseline.rotate import rotate_baseline, make_inputs  # noqa: E402

try:
    from solution.binding import rotate_candidate  # noqa: E402 (KDA agent writes this)
except Exception:
    rotate_candidate = None

def call_baseline(inp):   return rotate_baseline(**inp)
def call_candidate(inp):
    assert rotate_candidate is not None, "solution/binding.py:rotate_candidate missing"
    return rotate_candidate(**inp)
