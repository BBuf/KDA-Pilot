"""Benchmark adapter for b200_tilert_topk (generated).
Exposes baseline (PyTorch golden) / candidate (CUDA) ABI calls. The activation
input synthesis mirrors harness/tilert_oracle.py case_topk."""
from __future__ import annotations
import os, sys, torch
TASK_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if TASK_DIR not in sys.path: sys.path.insert(0, TASK_DIR)
from baseline.topk import topk_baseline, make_inputs  # noqa: E402

try:
    from solution.binding import topk_candidate  # noqa: E402 (KDA agent writes this)
except Exception:
    topk_candidate = None

def call_baseline(inp):   return topk_baseline(**inp)
def call_candidate(inp):
    assert topk_candidate is not None, "solution/binding.py:topk_candidate missing"
    return topk_candidate(**inp)
