"""Benchmark adapter for b200_tilert_rmsnorm_kv (generated).
Exposes baseline (PyTorch golden) / candidate (CUDA) ABI calls. The activation
input synthesis mirrors harness/tilert_oracle.py case_rmsnorm_kv."""
from __future__ import annotations
import os, sys, torch
TASK_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if TASK_DIR not in sys.path: sys.path.insert(0, TASK_DIR)
from baseline.rmsnorm_kv import rmsnorm_kv_baseline, make_inputs  # noqa: E402

try:
    from solution.binding import rmsnorm_kv_candidate  # noqa: E402 (KDA agent writes this)
except Exception:
    rmsnorm_kv_candidate = None

def call_baseline(inp):   return rmsnorm_kv_baseline(**inp)
def call_candidate(inp):
    assert rmsnorm_kv_candidate is not None, "solution/binding.py:rmsnorm_kv_candidate missing"
    return rmsnorm_kv_candidate(**inp)
