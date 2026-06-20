"""Benchmark adapter for b200_tilert_sparse_select_mla (generated).
Exposes baseline (PyTorch golden) / candidate (CUDA) ABI calls. The activation
input synthesis mirrors harness/tilert_oracle.py case_sparse_select_mla."""
from __future__ import annotations
import os, sys, torch
TASK_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if TASK_DIR not in sys.path: sys.path.insert(0, TASK_DIR)
from baseline.sparse_select_mla import sparse_select_mla_baseline, make_inputs  # noqa: E402

try:
    from solution.binding import sparse_select_mla_candidate  # noqa: E402 (KDA agent writes this)
except Exception:
    sparse_select_mla_candidate = None

def call_baseline(inp):   return sparse_select_mla_baseline(**inp)
def call_candidate(inp):
    assert sparse_select_mla_candidate is not None, "solution/binding.py:sparse_select_mla_candidate missing"
    return sparse_select_mla_candidate(**inp)
