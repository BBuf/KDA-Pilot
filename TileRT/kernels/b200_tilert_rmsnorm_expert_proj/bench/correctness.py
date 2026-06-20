#!/usr/bin/env python3
"""Correctness: candidate vs PyTorch baseline on every workload shape
(see ../../docs/tilert_correctness_contract.md). Generated."""
import json, os, sys, torch
BENCH = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, BENCH)
import adapter
from baseline.rmsnorm_expert_proj import make_inputs  # noqa

def main():
    dev = torch.device("cuda")
    rows = json.load(open(os.path.join(BENCH, "workloads.json")))
    ok = True
    for r in rows:
        inp = make_inputs(r["shapes"], dev)
        ref = adapter.call_baseline(inp)
        out = adapter.call_candidate(inp)
        ref = ref[-1] if isinstance(ref, (tuple, list)) else ref
        out = out[-1] if isinstance(out, (tuple, list)) else out
        rel = (out.float() - ref.float()).norm() / (ref.float().norm() + 1e-9)
        passed = rel < r.get("rtol", 0.02)
        ok &= bool(passed)
        print(f"[{r['id']}] rel={rel:.2e} {'OK' if passed else 'FAIL'}")
    print("CORRECTNESS", "PASS" if ok else "FAIL"); sys.exit(0 if ok else 1)
if __name__ == "__main__": main()
