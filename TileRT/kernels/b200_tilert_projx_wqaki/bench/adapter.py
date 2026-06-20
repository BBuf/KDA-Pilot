"""Benchmark adapter for b200_tilert_projx_wqaki (generated).
Exposes baseline (PyTorch golden) / candidate (CUDA) ABI calls. The activation
input synthesis mirrors harness/tilert_oracle.py case_projx_wqaki."""
from __future__ import annotations
import os, sys, torch
TASK_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if TASK_DIR not in sys.path: sys.path.insert(0, TASK_DIR)
from baseline.projx_wqaki import projx_wqaki_baseline, make_inputs  # noqa: E402

try:
    from solution.binding import projx_wqaki_candidate  # noqa: E402 (KDA agent writes this)
except Exception:
    projx_wqaki_candidate = None

def call_baseline(inp):   return projx_wqaki_baseline(**inp)
def call_candidate(inp):
    assert projx_wqaki_candidate is not None, "solution/binding.py:projx_wqaki_candidate missing"
    return projx_wqaki_candidate(**inp)
