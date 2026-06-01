#!/usr/bin/env python3
"""NCU profiling harness for the native CUDA rotary candidate.

Selects one captured bucket (env KDA_PROFILE in {std, ltx2_large, ltx2_mid, ltx2_small}),
builds the extension, warms up, then issues a few timed candidate launches for ncu to
capture. ncu should filter to the candidate kernels and skip the warmup launches:

  ncu --set full --kernel-name regex:'rope_std_kernel|ltx2_split_kernel' \
      --launch-skip 12 --launch-count 3 --target-processes all \
      -o profile/ncu-v1/reports/<bucket> python profile/ncu-v1/harness/profile_entry.py
"""
from __future__ import annotations
import importlib.util
import os
from pathlib import Path

import torch

KDIR = Path(__file__).resolve().parents[3]  # kernel folder root


def _load(name, rel):
    spec = importlib.util.spec_from_file_location(name, KDIR / rel)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


tc = _load("tc", "tests/test_correctness.py")
wrapper = _load("wr", "src/wrapper.py")

BUCKET = os.environ.get("KDA_PROFILE", "std")
NAME = {
    "std": "std__hunyuanvideo__B1S27030H24D128",
    "ltx2_large": "ltx2__two__B1S24576h64",
    "ltx2_mid": "ltx2__ti2v__B1S6144h64",
    "ltx2_small": "ltx2__ti2v__B1S126h32",
}[BUCKET]
case = {c["name"]: c for c in tc.make_cases()}[NAME]
inp = case["build"]()
which = "standard" if case["kind"] == "standard" else "ltx2"


def call():
    if case["kind"] == "standard":
        return wrapper.apply_rotary_embedding(inp["x"], inp["cos"], inp["sin"], inp["interleaved"])
    return wrapper.apply_ltx2_split_rotary_emb(inp["x"], inp["cos"], inp["sin"])


wrapper.build()  # compile the extension BEFORE any profiled launch
for _ in range(12):  # warmup launches (ncu --launch-skip 12 skips these)
    call()
torch.cuda.synchronize()
for _ in range(3):   # profiled launches
    call()
torch.cuda.synchronize()
assert wrapper.last_dispatch_path(which) == "cuda", f"{NAME} did not take cuda path"
print(f"profiled bucket={BUCKET} name={NAME} path={wrapper.last_dispatch_path(which)}")
