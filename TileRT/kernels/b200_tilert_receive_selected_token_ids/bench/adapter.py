"""Benchmark adapter for b200_tilert_receive_selected_token_ids (generated).
Exposes baseline (PyTorch golden) / candidate (CUDA) ABI calls. The activation
input synthesis mirrors harness/tilert_oracle.py case_receive_selected_token_ids."""
from __future__ import annotations
import os, sys, torch
TASK_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if TASK_DIR not in sys.path: sys.path.insert(0, TASK_DIR)
from baseline.receive_selected_token_ids import receive_selected_token_ids_baseline, make_inputs  # noqa: E402

try:
    from solution.binding import receive_selected_token_ids_candidate  # noqa: E402 (KDA agent writes this)
except Exception:
    receive_selected_token_ids_candidate = None

def call_baseline(inp):   return receive_selected_token_ids_baseline(**inp)
def call_candidate(inp):
    assert receive_selected_token_ids_candidate is not None, "solution/binding.py:receive_selected_token_ids_candidate missing"
    return receive_selected_token_ids_candidate(**inp)
