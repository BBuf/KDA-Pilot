"""Benchmark adapter for b200_tilert_projq_wqb (generated).
Exposes baseline (PyTorch golden) / candidate (CUDA) ABI calls. The activation
input synthesis mirrors harness/tilert_oracle.py case_projq_wqb."""
from __future__ import annotations
import os, sys, torch
TASK_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if TASK_DIR not in sys.path: sys.path.insert(0, TASK_DIR)
from baseline.projq_wqb import projq_wqb_baseline, make_inputs  # noqa: E402

try:
    from solution.binding import projq_wqb_candidate  # noqa: E402 (KDA agent writes this)
except Exception:
    projq_wqb_candidate = None

def call_baseline(inp):   return projq_wqb_baseline(**inp)
def call_candidate(inp):
    assert projq_wqb_candidate is not None, "solution/binding.py:projq_wqb_candidate missing"
    return projq_wqb_candidate(**inp)
