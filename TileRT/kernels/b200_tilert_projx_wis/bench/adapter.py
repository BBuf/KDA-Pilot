"""Benchmark adapter for b200_tilert_projx_wis (generated).
Exposes baseline (PyTorch golden) / candidate (CUDA) ABI calls. The activation
input synthesis mirrors harness/tilert_oracle.py case_projx_wis."""
from __future__ import annotations
import os, sys, torch
TASK_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if TASK_DIR not in sys.path: sys.path.insert(0, TASK_DIR)
from baseline.projx_wis import projx_wis_baseline, make_inputs  # noqa: E402

try:
    from solution.binding import projx_wis_candidate  # noqa: E402 (KDA agent writes this)
except Exception:
    projx_wis_candidate = None

def call_baseline(inp):   return projx_wis_baseline(**inp)
def call_candidate(inp):
    assert projx_wis_candidate is not None, "solution/binding.py:projx_wis_candidate missing"
    return projx_wis_candidate(**inp)
