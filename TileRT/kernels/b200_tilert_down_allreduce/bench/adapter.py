"""Benchmark adapter for b200_tilert_down_allreduce (generated).
Exposes baseline (PyTorch golden) / candidate (CUDA) ABI calls. The activation
input synthesis mirrors harness/tilert_oracle.py case_down_allreduce."""
from __future__ import annotations
import os, sys, torch
TASK_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if TASK_DIR not in sys.path: sys.path.insert(0, TASK_DIR)
from baseline.down_allreduce import down_allreduce_baseline, make_inputs  # noqa: E402

try:
    from solution.binding import down_allreduce_candidate  # noqa: E402 (KDA agent writes this)
except Exception:
    down_allreduce_candidate = None

def call_baseline(inp):   return down_allreduce_baseline(**inp)
def call_candidate(inp):
    assert down_allreduce_candidate is not None, "solution/binding.py:down_allreduce_candidate missing"
    return down_allreduce_candidate(**inp)
