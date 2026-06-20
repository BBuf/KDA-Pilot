"""Benchmark adapter for b200_tilert_layernorm_rope_rotate (generated).
Exposes baseline (PyTorch golden) / candidate (CUDA) ABI calls. The activation
input synthesis mirrors harness/tilert_oracle.py case_layernorm_rope_rotate."""
from __future__ import annotations
import os, sys, torch
TASK_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if TASK_DIR not in sys.path: sys.path.insert(0, TASK_DIR)
from baseline.layernorm_rope_rotate import layernorm_rope_rotate_baseline, make_inputs  # noqa: E402

try:
    from solution.binding import layernorm_rope_rotate_candidate  # noqa: E402 (KDA agent writes this)
except Exception:
    layernorm_rope_rotate_candidate = None

def call_baseline(inp):   return layernorm_rope_rotate_baseline(**inp)
def call_candidate(inp):
    assert layernorm_rope_rotate_candidate is not None, "solution/binding.py:layernorm_rope_rotate_candidate missing"
    return layernorm_rope_rotate_candidate(**inp)
