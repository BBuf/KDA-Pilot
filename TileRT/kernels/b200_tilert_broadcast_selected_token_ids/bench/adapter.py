"""Benchmark adapter for b200_tilert_broadcast_selected_token_ids (generated).
Exposes baseline (PyTorch golden) / candidate (CUDA) ABI calls. The activation
input synthesis mirrors harness/tilert_oracle.py case_broadcast_selected_token_ids."""
from __future__ import annotations
import os, sys, torch
TASK_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if TASK_DIR not in sys.path: sys.path.insert(0, TASK_DIR)
from baseline.broadcast_selected_token_ids import broadcast_selected_token_ids_baseline, make_inputs  # noqa: E402

try:
    from solution.binding import broadcast_selected_token_ids_candidate  # noqa: E402 (KDA agent writes this)
except Exception:
    broadcast_selected_token_ids_candidate = None

def call_baseline(inp):   return broadcast_selected_token_ids_baseline(**inp)
def call_candidate(inp):
    assert broadcast_selected_token_ids_candidate is not None, "solution/binding.py:broadcast_selected_token_ids_candidate missing"
    return broadcast_selected_token_ids_candidate(**inp)
