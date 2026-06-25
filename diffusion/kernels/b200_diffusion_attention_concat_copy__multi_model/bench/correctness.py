#!/usr/bin/env python3
"""Bit-exact correctness suite for the attention concat/copy/slice task.

These ops are lossless memory movement, so every production and regression row
must match an independent PyTorch oracle BIT-FOR-BIT (atol=rtol=0), including
NaN/Inf preservation. Output buffers are poisoned before each call so a skipped
or partial launch is caught; a negative-control self-test proves the poison
detector works.

Usage:
  python3 bench/correctness.py                      # both impls, auto device
  python3 bench/correctness.py --impl baseline --device cpu   # CPU dry-run (no GPU candidate)
  python3 bench/correctness.py --impl candidate     # candidate only (needs CUDA build)
"""

from __future__ import annotations

import argparse
import os
import sys

TASK_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if TASK_ROOT not in sys.path:
    sys.path.insert(0, TASK_ROOT)

import torch  # noqa: E402

import cases  # noqa: E402  (same directory as this script)

POISON = 12345.0  # distinctive finite sentinel, representable in fp16/bf16/fp32; randn oracle values never reach it


def _poison(t):
    t.fill_(POISON)
    return t


def _load_impl(name):
    if name == "baseline":
        from baseline.binding import attention_concat_copy_baseline
        return attention_concat_copy_baseline
    if name == "candidate":
        from solution.binding import attention_concat_copy_candidate
        return attention_concat_copy_candidate
    raise ValueError(name)


def run(impls, device):
    data = cases.load_workloads()
    workloads = data["workloads"]
    fns = {name: _load_impl(name) for name in impls}

    n_pass = 0
    n_fail = 0
    failures = []

    for w in workloads:
        inp = cases.make_inputs(w, device=device)
        ref = cases.oracle(w, inp)
        for name, fn in fns.items():
            out = cases.alloc_output(w, device)
            scratch = cases.alloc_scratch(w, device)
            _poison(out)
            if scratch is not None:
                _poison(scratch)
            fn(inp.op_type, inp.order, inp.h_start, inp.h_local,
               inp.source_a, inp.source_b, scratch, out)
            torch.cuda.synchronize() if device.type == "cuda" else None
            if cases.bitwise_equal(out, ref):
                n_pass += 1
            else:
                n_fail += 1
                cnt, idx = cases.first_mismatch(out, ref)
                failures.append(f"{w['id']} [{name}]: {cnt} mismatching elements (first flat idx {idx})")

    # --- negative control: poison, do NOT call the kernel, expect a detected mismatch ---
    neg_ok = True
    nc = next((x for x in workloads if x["op_type"] == "slice_heads_then_concat"), workloads[0])
    inp = cases.make_inputs(nc, device=device)
    ref = cases.oracle(nc, inp)
    out = _poison(cases.alloc_output(nc, device))
    if cases.bitwise_equal(out, ref):
        neg_ok = False  # poison was somehow already equal to oracle -> detector is blind

    print(f"device={device}  impls={','.join(impls)}")
    print(f"PASS={n_pass}  FAIL={n_fail}  rows={len(workloads)}")
    print(f"negative_control: {'OK (poison detected)' if neg_ok else 'BROKEN (poison not detected)'}")
    for f in failures:
        print("  FAIL:", f)
    return 0 if (n_fail == 0 and neg_ok) else 1


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--impl", choices=["baseline", "candidate", "both"], default="both")
    ap.add_argument("--device", default="auto")
    args = ap.parse_args()

    if args.device == "auto":
        device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    else:
        device = torch.device(args.device)

    impls = ["baseline", "candidate"] if args.impl == "both" else [args.impl]
    return run(impls, device)


if __name__ == "__main__":
    raise SystemExit(main())
