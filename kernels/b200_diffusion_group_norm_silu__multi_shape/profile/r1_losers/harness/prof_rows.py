#!/usr/bin/env python3
"""NCU profile driver: run baseline then candidate once for a workload id."""
import json, os, sys
TASK_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
sys.path.insert(0, TASK_DIR)
sys.path.insert(0, os.path.join(TASK_DIR, "bench"))
import torch
torch.set_grad_enabled(False)
import adapter  # noqa

wid = sys.argv[1]
side = sys.argv[2] if len(sys.argv) > 2 else "both"
rows = json.load(open(os.path.join(TASK_DIR, "bench", "workloads.json")))
row = next(w for w in rows if w["id"] == wid)
case = adapter.make_case(row, device=torch.device("cuda:0"), seed=0x5EED)
# one warmup iteration outside profiling intent (JIT/build/alloc)
if side in ("baseline", "both"):
    adapter.call_baseline(row, case.inputs, case.baseline_outputs)
if side in ("candidate", "both"):
    adapter.call_candidate(row, case.inputs, case.candidate_outputs)
torch.cuda.synchronize()
torch.cuda.profiler.start()
if side in ("baseline", "both"):
    adapter.call_baseline(row, case.inputs, case.baseline_outputs)
if side in ("candidate", "both"):
    adapter.call_candidate(row, case.inputs, case.candidate_outputs)
torch.cuda.synchronize()
torch.cuda.profiler.stop()
print("profiled", wid, side)
