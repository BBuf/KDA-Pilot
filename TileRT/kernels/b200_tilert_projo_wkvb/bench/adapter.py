"""Benchmark adapter for b200_tilert_projo_wkvb (generated).
Exposes baseline (PyTorch golden) / candidate (CUDA) ABI calls. The activation
input synthesis mirrors harness/tilert_oracle.py case_projo_wkvb."""
from __future__ import annotations
import os, sys, torch
TASK_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if TASK_DIR not in sys.path: sys.path.insert(0, TASK_DIR)
from baseline.projo_wkvb import projo_wkvb_baseline, make_inputs  # noqa: E402

try:
    from solution.binding import projo_wkvb_candidate  # noqa: E402 (KDA agent writes this)
except Exception:
    projo_wkvb_candidate = None

def call_baseline(inp):   return projo_wkvb_baseline(**inp)
def call_candidate(inp):
    assert projo_wkvb_candidate is not None, "solution/binding.py:projo_wkvb_candidate missing"
    return projo_wkvb_candidate(**inp)
