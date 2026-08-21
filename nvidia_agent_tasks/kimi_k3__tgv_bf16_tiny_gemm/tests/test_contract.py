"""Contract test for `kimi_k3__tgv_bf16_tiny_gemm` - runs on CPU, no GPU and no SGLang import needed.

    pytest kimi_k3__tgv_bf16_tiny_gemm/tests/test_contract.py      (or: python kimi_k3__tgv_bf16_tiny_gemm/tests/test_contract.py)

It checks the things that make a task runnable at all: the workload rows parse and carry
their provenance, `baseline/entry.py` exposes an OPS entry for every op in the workload,
every file listed in SOURCES.txt is present, and any shipped state chain really chains.
Performance is not measured here - that is `tools/bench_harness.py`.
"""

import glob
import json
import os
import sys

TASK = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ROOT = os.path.dirname(TASK)


def test_workloads_parse_and_carry_provenance():
    files = sorted(glob.glob(os.path.join(TASK, "bench", "workloads*.json")))
    assert files, "no bench/workloads*.json"
    for f in files:
        d = json.load(open(f))
        assert d["ops"], f
        for o in d["ops"]:
            assert o["rows"], o["op"]
            for r in o["rows"]:
                assert r["group"] != "warmup"
                assert r["real_calls"] > 0
                assert r["kept_because"]


def test_entry_covers_every_op():
    sys.path.insert(0, os.path.join(ROOT, "tools"))
    src = open(os.path.join(TASK, "baseline", "entry.py")).read()
    ops = set()
    for f in glob.glob(os.path.join(TASK, "bench", "workloads*.json")):
        ops |= {o["op"] for o in json.load(open(f))["ops"]}
    for op in ops:
        assert '"%s"' % op in src, "baseline/entry.py has no OPS entry for " + op


def test_baseline_sources_present():
    src = os.path.join(TASK, "baseline", "SOURCES.txt")
    listed = [l.split("#", 1)[0].strip() for l in open(src)]
    for rel in [l for l in listed if l]:
        want = os.path.join(TASK, "baseline", os.path.relpath(rel, "python/sglang"))
        assert os.path.exists(want), rel


def test_state_chains_chain():
    try:
        import torch
    except ImportError:
        return
    for chain in glob.glob(os.path.join(TASK, "bench", "tensors*", "**")):
        steps = sorted(glob.glob(os.path.join(chain, "step*")))
        if len(steps) < 2:
            continue
        names = {os.path.basename(f)[len("state_after_"):-3]
                 for f in glob.glob(os.path.join(steps[0], "state_after_*.pt"))}
        assert names, "chain %s has no state_after tensors" % chain
        for n in names:
            for i in range(len(steps) - 1):
                a = torch.load(os.path.join(steps[i], "state_after_%s.pt" % n), map_location="cpu")
                b = torch.load(os.path.join(steps[i + 1], "state_before_%s.pt" % n), map_location="cpu")
                assert a.shape == b.shape and torch.equal(a, b), (chain, n, i)


if __name__ == "__main__":
    for fn in [v for k, v in sorted(globals().items()) if k.startswith("test_")]:
        fn()
        print("ok:", fn.__name__)
    print("all contract checks passed for kimi_k3__tgv_bf16_tiny_gemm")
