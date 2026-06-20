"""Benchmark adapter for b200_tilert_mtp_preprocess (generated).
Exposes baseline (PyTorch golden) / candidate (CUDA) ABI calls. The activation
input synthesis mirrors harness/tilert_oracle.py case_mtp_preprocess."""
from __future__ import annotations
import os, sys, torch
TASK_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if TASK_DIR not in sys.path: sys.path.insert(0, TASK_DIR)
from baseline.mtp_preprocess import mtp_preprocess_baseline, make_inputs  # noqa: E402

try:
    from solution.binding import mtp_preprocess_candidate  # noqa: E402 (KDA agent writes this)
except Exception:
    mtp_preprocess_candidate = None

def call_baseline(inp):   return mtp_preprocess_baseline(**inp)
def call_candidate(inp):
    assert mtp_preprocess_candidate is not None, "solution/binding.py:mtp_preprocess_candidate missing"
    return mtp_preprocess_candidate(**inp)
