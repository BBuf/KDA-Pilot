"""Benchmark adapter for b200_tilert_flash_sparse_mla (generated).
Exposes baseline (PyTorch golden) / candidate (CUDA) ABI calls. The activation
input synthesis mirrors harness/tilert_oracle.py case_flash_sparse_mla."""
from __future__ import annotations
import os, sys, torch
TASK_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if TASK_DIR not in sys.path: sys.path.insert(0, TASK_DIR)
from baseline.flash_sparse_mla import flash_sparse_mla_baseline, make_inputs  # noqa: E402

try:
    from solution.binding import flash_sparse_mla_candidate  # noqa: E402 (KDA agent writes this)
except Exception:
    flash_sparse_mla_candidate = None

def call_baseline(inp):   return flash_sparse_mla_baseline(**inp)
def call_candidate(inp):
    assert flash_sparse_mla_candidate is not None, "solution/binding.py:flash_sparse_mla_candidate missing"
    return flash_sparse_mla_candidate(**inp)
