"""Benchmark adapter for b200_tilert_qkv_rope (generated).
Exposes baseline (PyTorch golden) / candidate (CUDA) ABI calls. The activation
input synthesis mirrors harness/tilert_oracle.py case_qkv_rope."""
from __future__ import annotations
import os, sys, torch
TASK_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if TASK_DIR not in sys.path: sys.path.insert(0, TASK_DIR)
from baseline.qkv_rope import qkv_rope_baseline, make_inputs  # noqa: E402

try:
    from solution.binding import qkv_rope_candidate  # noqa: E402 (KDA agent writes this)
except Exception:
    qkv_rope_candidate = None

def call_baseline(inp):   return qkv_rope_baseline(**inp)
def call_candidate(inp):
    assert qkv_rope_candidate is not None, "solution/binding.py:qkv_rope_candidate missing"
    return qkv_rope_candidate(**inp)
