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


def _expect_reject(fn, label, errors):
    """fn() must raise (the invalid input must be rejected loudly)."""
    try:
        fn()
    except Exception:
        return
    errors.append(f"{label}: expected rejection but the call succeeded")


def run_negative_matrix(impls, device):
    """Negative tests: invalid workloads must be rejected.

    Validator-level rejections (CPU-safe) cover the workload audit; kernel-level
    rejections (CUDA) cover the candidate's ABI contract checks.
    """
    import gen_workloads as gw
    errors = []

    def vbad(label, row):
        if not gw.validate_workloads([row]):
            errors.append(f"validator did not reject {label}")

    r = gw.concat_row("neg", False, "t", [1, 4, 8, 128], [1, 4, 8, 128], "AB", 4); r["order"] = "ZZ"
    vbad("bad order", r)
    vbad("pre-sliced prefix (h_full==h_local)", gw.slice_row("neg", False, "t", 4, 8, 12, 12, 0, "AB"))
    r = gw.slice_row("neg", False, "t", 512, 4096, 24, 12, 0, "AB"); r["h_start"] = 7
    vbad("misaligned h_start", r)
    r = gw.slice_row("neg", False, "t", 512, 4096, 24, 12, 0, "AB"); r["h_start"] = 24
    vbad("out-of-range h_start", r)
    vbad("contiguous copy source (full_heads<=H)", gw.copy_row("neg", False, "t", [1, 8, 24, 128], 24, 0))

    if device.type == "cuda" and "candidate" in impls:
        from solution.binding import attention_concat_copy_candidate as cand
        dt = torch.bfloat16
        prefix = torch.randn(1, 512, 24, 128, device=device, dtype=dt)   # full-head prefix
        shard = torch.randn(1, 4096, 12, 128, device=device, dtype=dt)
        out = torch.empty(1, 4608, 12, 128, device=device, dtype=dt)
        OP_SLICE = cases.OP["slice_heads_then_concat"]
        _expect_reject(lambda: cand(OP_SLICE, 9, 0, 12, prefix, shard, None, out), "kernel: invalid order", errors)
        _expect_reject(lambda: cand(OP_SLICE, 0, 7, 12, prefix, shard, None, out), "kernel: misaligned h_start", errors)
        _expect_reject(lambda: cand(OP_SLICE, 0, 24, 12, prefix, shard, None, out), "kernel: out-of-range h_start", errors)
        prefix_presliced = torch.randn(1, 512, 12, 128, device=device, dtype=dt)  # full_heads==h_local
        _expect_reject(lambda: cand(OP_SLICE, 0, 0, 12, prefix_presliced, shard, None, out),
                       "kernel: pre-sliced prefix", errors)

        OP_CONCAT = cases.OP["concat_sequence"]
        OP_COPY = cases.OP["copy_contiguous"]
        # sequence-strided (non-dense) concat source must be rejected, not silently copied as dense
        cat_a_strided = torch.randn(1, 8, 8, 128, device=device, dtype=dt)[:, ::2]  # [1,4,8,128], stride(1)=2*H*D
        cat_b = torch.randn(1, 4, 8, 128, device=device, dtype=dt)
        cat_out = torch.empty(1, 8, 8, 128, device=device, dtype=dt)
        _expect_reject(lambda: cand(OP_CONCAT, 0, 0, 8, cat_a_strided, cat_b, None, cat_out),
                       "kernel: sequence-strided concat source", errors)
        # non-dense slice shard / prefix must be rejected
        shard_strided = torch.randn(1, 8192, 12, 128, device=device, dtype=dt)[:, ::2]  # [1,4096,12,128] non-dense
        _expect_reject(lambda: cand(OP_SLICE, 0, 0, 12, prefix, shard_strided, None, out),
                       "kernel: non-dense slice shard", errors)
        prefix_strided = torch.randn(1, 1024, 24, 128, device=device, dtype=dt)[:, ::2]  # [1,512,24,128] non-dense
        _expect_reject(lambda: cand(OP_SLICE, 0, 0, 12, prefix_strided, shard, None, out),
                       "kernel: non-dense slice prefix", errors)
        # contiguous copy source (stride(1)==H*D, no real work) must be rejected
        copy_contig = torch.randn(1, 8, 4, 128, device=device, dtype=dt)
        copy_out = torch.empty(1, 8, 4, 128, device=device, dtype=dt)
        _expect_reject(lambda: cand(OP_COPY, 0, 0, 4, copy_contig, None, None, copy_out),
                       "kernel: contiguous copy source", errors)
        # dtype mismatch (output dtype != source dtype) must be rejected
        out_fp16 = torch.empty(1, 4608, 12, 128, device=device, dtype=torch.float16)
        _expect_reject(lambda: cand(OP_SLICE, 0, 0, 12, prefix, shard, None, out_fp16),
                       "kernel: dtype mismatch", errors)
        # shape mismatch (Sa+Sb != OutSeq) must be rejected
        bad_out = torch.empty(1, 9, 8, 128, device=device, dtype=dt)
        _expect_reject(lambda: cand(OP_CONCAT, 0, 0, 8,
                                    torch.randn(1, 4, 8, 128, device=device, dtype=dt), cat_b, None, bad_out),
                       "kernel: concat shape mismatch", errors)
        # source batch mismatch (output B=1, source B=2) must be rejected
        a_b2 = torch.randn(2, 4, 8, 128, device=device, dtype=dt)
        _expect_reject(lambda: cand(OP_CONCAT, 0, 0, 8, a_b2, cat_b, None, cat_out),
                       "kernel: source batch mismatch", errors)
        # non-dense (padded) output batch stride for B>1 must be rejected
        out_padded = torch.empty(2, 10, 8, 128, device=device, dtype=dt)[:, :8]  # [2,8,8,128], stride(0) padded
        a2 = torch.randn(2, 4, 8, 128, device=device, dtype=dt)
        b2 = torch.randn(2, 4, 8, 128, device=device, dtype=dt)
        _expect_reject(lambda: cand(OP_CONCAT, 0, 0, 8, a2, b2, None, out_padded),
                       "kernel: non-dense output batch stride", errors)
        # cross-CUDA-device inputs must be rejected (needs >=2 visible devices)
        if torch.cuda.device_count() >= 2:
            src_d1 = torch.randn(1, 4, 8, 128, device="cuda:1", dtype=dt)
            shard_d1 = torch.randn(1, 4, 8, 128, device="cuda:1", dtype=dt)
            out_d0 = torch.empty(1, 8, 8, 128, device="cuda:0", dtype=dt)
            _expect_reject(lambda: cand(OP_CONCAT, 0, 0, 8, src_d1, shard_d1, None, out_d0),
                           "kernel: cross-device source vs output", errors)
    return errors


def run(impls, device):
    workloads = cases.load_workloads()  # top-level list of workload rows
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
    neg_matrix = run_negative_matrix(impls, device)
    print(f"negative_matrix: {'OK (all invalid rows rejected)' if not neg_matrix else 'FAILED'}")
    for e in neg_matrix:
        print("  NEG-FAIL:", e)
    return 0 if (n_fail == 0 and neg_ok and not neg_matrix) else 1


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
