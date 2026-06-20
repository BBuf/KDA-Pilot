"""Benchmark adapter for b200_tilert_sparse_index (generated).
Exposes baseline (PyTorch golden) / candidate (CUDA) ABI calls. The activation
input synthesis mirrors harness/tilert_oracle.py case_sparse_index."""
from __future__ import annotations
import os, sys, torch
TASK_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if TASK_DIR not in sys.path: sys.path.insert(0, TASK_DIR)
from baseline.sparse_index import sparse_index_baseline, make_inputs  # noqa: E402

try:
    from solution.binding import sparse_index_candidate  # noqa: E402 (KDA agent writes this)
except Exception:
    sparse_index_candidate = None

def call_baseline(inp):   return sparse_index_baseline(**inp)
def call_candidate(inp):
    assert sparse_index_candidate is not None, "solution/binding.py:sparse_index_candidate missing"
    return sparse_index_candidate(**inp)
