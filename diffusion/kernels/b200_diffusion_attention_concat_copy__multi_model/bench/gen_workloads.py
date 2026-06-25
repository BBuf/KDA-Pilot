#!/usr/bin/env python3
"""Generate the frozen bench/workloads.json for the attention concat/copy/slice task.

Each row carries a *construction recipe* (not raw tensors); bench/adapter.py and
bench/correctness.py build tensors deterministically from these fields, so the
baseline, candidate, and oracle all see identical inputs.

Production rows mirror the `diffusion_attention_concat_copy__multi_model` section
of diffusion_benchmark_shape_coverage.md (FLUX.2 + JoyAI shapes). Regression rows
add both source orders, nonzero sp_rank head offsets, non-finite preservation,
degenerate lengths, and fp16/fp32 dtype coverage.

Memory-movement modeling notes:
- `copy_contiguous` sources are NON-CONTIGUOUS head-sliced views (full_heads >
  heads), so `.contiguous()` performs real work (a contiguous prefix slice with
  B=1 would be a no-op).
- `slice_heads_then_concat` uses a FULL-head prefix (`full_heads = sp_size *
  h_local`) sliced to `h_local = full_heads // sp_size` at `h_start = sp_rank *
  h_local`; pre-slicing the prefix would degenerate it to plain concat.
- Tolerances are bit-exact (atol=rtol=0): these ops are lossless.

Usage:
  python3 gen_workloads.py            # (re)write workloads.json
  python3 gen_workloads.py --check    # fail if workloads.json is stale (freeze guard)
"""

from __future__ import annotations

import argparse
import json
import os
import sys

HEAD_DIM = 128
SP_SIZE = 2  # DEC-1 default: full prefix = SP_SIZE * h_local; test sp_rank 0 and 1.

WORKLOADS_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "workloads.json")


def concat_row(rid, production, preset, a_shape, b_shape, order, dtype="bfloat16", seed=0, note=""):
    sa, sb = a_shape[1], b_shape[1]
    out_seq = sa + sb  # order only swaps which segment is written first; total length is the same
    out_shape = [a_shape[0], out_seq, a_shape[2], a_shape[3]]
    return {
        "id": rid,
        "production": production,
        "op_type": "concat_sequence",
        "order": order,
        "dtype": dtype,
        "seed": seed,
        "tensors": {"a": {"shape": a_shape}, "b": {"shape": b_shape}},
        "output_shape": out_shape,
        "atol": 0, "rtol": 0,
        "source": {"preset": preset, "note": note},
    }


def copy_row(rid, production, preset, shape, full_heads, head_start, dtype="bfloat16",
             seed=0, inject_nonfinite=False, note=""):
    return {
        "id": rid,
        "production": production,
        "op_type": "copy_contiguous",
        "order": "AB",  # unused for copy
        "dtype": dtype,
        "seed": seed,
        # source `a` is a non-contiguous head-sliced view of a [B, S, full_heads, D] tensor
        "tensors": {"a": {"shape": shape, "source_kind": "head_sliced_view",
                          "full_heads": full_heads, "head_start": head_start}},
        "output_shape": list(shape),
        "h_start": head_start, "h_local": shape[2],
        "inject_nonfinite": inject_nonfinite,
        "atol": 0, "rtol": 0,
        "source": {"preset": preset, "note": note},
    }


def slice_concat_row(rid, production, preset, prefix_len, shard_len, h_local, sp_size, sp_rank,
                     order, dtype="bfloat16", seed=0, inject_nonfinite=False, note=""):
    full_heads = sp_size * h_local
    h_start = sp_rank * h_local
    B = 1
    prefix_shape = [B, prefix_len, full_heads, HEAD_DIM]
    shard_shape = [B, shard_len, h_local, HEAD_DIM]
    scratch_shape = [B, prefix_len, h_local, HEAD_DIM]
    out_shape = [B, prefix_len + shard_len, h_local, HEAD_DIM]
    return {
        "id": rid,
        "production": production,
        "op_type": "slice_heads_then_concat",
        "order": order,
        "dtype": dtype,
        "seed": seed,
        "tensors": {"prefix": {"shape": prefix_shape, "full_heads": full_heads},
                    "shard": {"shape": shard_shape}},
        "h_start": h_start, "h_local": h_local,
        "scratch_shape": scratch_shape,
        "output_shape": out_shape,
        "inject_nonfinite": inject_nonfinite,
        "atol": 0, "rtol": 0,
        "source": {"preset": preset, "sp_size": sp_size, "sp_rank": sp_rank, "note": note},
    }


def build_workloads():
    rows = []

    # ---------------- PRODUCTION (headline geomean) ----------------
    # concat_sequence (orders match the profiled cat operand order)
    rows.append(concat_row("flux_concat_512_4096_h24", True, "flux2-klein-base",
                           [1, 512, 24, 128], [1, 4096, 24, 128], "AB", seed=1001,
                           note="FLUX.2 cat([prefix512, shard4096]) -> [1,4608,24,128]"))
    rows.append(concat_row("joyai_concat_8048_1004_h32", True, "joyai-edit",
                           [1, 8048, 32, 128], [1, 1004, 32, 128], "AB", seed=1002,
                           note="JoyAI cat([shard8048, suffix1004]) -> [1,9052,32,128]"))

    # copy_contiguous (non-contiguous head-sliced source; full_heads = 2*heads, start=0)
    rows.append(copy_row("flux_copy_4608_h24", True, "flux2-klein-base",
                        [1, 4608, 24, 128], full_heads=48, head_start=0, seed=1101))
    rows.append(copy_row("joyai_copy_8048_h32", True, "joyai-edit",
                        [1, 8048, 32, 128], full_heads=64, head_start=0, seed=1102))
    rows.append(copy_row("joyai_copy_1004_h32", True, "joyai-edit",
                        [1, 1004, 32, 128], full_heads=64, head_start=0, seed=1103))

    # slice_heads_then_concat (full-head prefix sliced to h_local; profiled orders)
    rows.append(slice_concat_row("flux_slice_concat_512_4096_h24_sp2_r0_AB", True, "flux2-klein-base",
                                prefix_len=512, shard_len=4096, h_local=24, sp_size=SP_SIZE, sp_rank=0,
                                order="AB", seed=1201,
                                note="FLUX.2 prefix-first cat([slice(prefix512,h0:24 of 48), shard4096])"))
    rows.append(slice_concat_row("joyai_slice_concat_1004_8048_h32_sp2_r0_BA", True, "joyai-edit",
                                prefix_len=1004, shard_len=8048, h_local=32, sp_size=SP_SIZE, sp_rank=0,
                                order="BA", seed=1202,
                                note="JoyAI suffix model: cat([shard8048, slice(suffix1004,h0:32 of 64)])"))

    # ---------------- REGRESSION (production=false) ----------------
    # opposite source order
    rows.append(slice_concat_row("flux_slice_concat_512_4096_h24_sp2_r0_BA", False, "flux2-klein-base",
                                512, 4096, 24, SP_SIZE, 0, "BA", seed=2001, note="opposite order"))
    rows.append(slice_concat_row("joyai_slice_concat_1004_8048_h32_sp2_r0_AB", False, "joyai-edit",
                                1004, 8048, 32, SP_SIZE, 0, "AB", seed=2002, note="opposite order"))
    # nonzero sp_rank head offset (h_start = h_local)
    rows.append(slice_concat_row("flux_slice_concat_512_4096_h24_sp2_r1_AB", False, "flux2-klein-base",
                                512, 4096, 24, SP_SIZE, 1, "AB", seed=2003, note="sp_rank=1, h_start=24"))
    rows.append(slice_concat_row("joyai_slice_concat_1004_8048_h32_sp2_r1_BA", False, "joyai-edit",
                                1004, 8048, 32, SP_SIZE, 1, "BA", seed=2004, note="sp_rank=1, h_start=32"))
    # concat opposite orders
    rows.append(concat_row("flux_concat_512_4096_h24_BA", False, "flux2-klein-base",
                          [1, 512, 24, 128], [1, 4096, 24, 128], "BA", seed=2101, note="opposite order"))
    rows.append(concat_row("joyai_concat_8048_1004_h32_BA", False, "joyai-edit",
                          [1, 8048, 32, 128], [1, 1004, 32, 128], "BA", seed=2102, note="opposite order"))
    # copy with nonzero head_start
    rows.append(copy_row("flux_copy_4608_h24_start24", False, "flux2-klein-base",
                       [1, 4608, 24, 128], full_heads=48, head_start=24, seed=2201, note="head_start=24"))
    # non-finite preservation (NaN/Inf must be copied bit-for-bit)
    rows.append(copy_row("nonfinite_copy_small", False, "synthetic",
                       [1, 8, 4, 128], full_heads=8, head_start=2, seed=2301, inject_nonfinite=True,
                       note="NaN/Inf preservation"))
    rows.append(slice_concat_row("nonfinite_slice_concat_small", False, "synthetic",
                                prefix_len=4, shard_len=8, h_local=2, sp_size=2, sp_rank=1, order="AB",
                                seed=2302, inject_nonfinite=True, note="NaN/Inf preservation"))
    # degenerate lengths
    rows.append(slice_concat_row("degenerate_prefix1_slice_concat", False, "synthetic",
                                prefix_len=1, shard_len=3, h_local=1, sp_size=4, sp_rank=2, order="BA",
                                seed=2401, note="prefix length 1, single head, sp_size 4"))
    rows.append(concat_row("degenerate_tiny_concat", False, "synthetic",
                          [1, 1, 1, 128], [1, 2, 1, 128], "AB", seed=2402, note="tiny"))
    # dtype coverage (lossless => bit-exact at any dtype)
    rows.append(copy_row("fp16_copy_small", False, "synthetic",
                       [1, 64, 8, 128], full_heads=16, head_start=8, dtype="float16", seed=2501))
    rows.append(concat_row("fp32_concat_small", False, "synthetic",
                          [1, 17, 8, 128], [1, 31, 8, 128], "AB", dtype="float32", seed=2502))

    return {
        "schema_version": 1,
        "task": "b200_diffusion_attention_concat_copy__multi_model",
        "head_dim": HEAD_DIM,
        "dtype_default": "bfloat16",
        "abi": {
            "op_types": {"copy_contiguous": 0, "concat_sequence": 1, "slice_heads_then_concat": 2},
            "orders": {"AB": 0, "BA": 1},
            "note": "op_type/order ints match baseline/binding.py OP_*/ORDER_* and solution/kernel.cu.",
        },
        "workloads": rows,
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true", help="fail if workloads.json is stale")
    args = ap.parse_args()

    data = build_workloads()
    rendered = json.dumps(data, indent=2) + "\n"

    if args.check:
        if not os.path.exists(WORKLOADS_PATH):
            print("workloads.json missing", file=sys.stderr)
            return 1
        with open(WORKLOADS_PATH) as f:
            current = f.read()
        if current != rendered:
            print("workloads.json is STALE — re-run gen_workloads.py", file=sys.stderr)
            return 1
        print("workloads.json is up to date")
        return 0

    with open(WORKLOADS_PATH, "w") as f:
        f.write(rendered)
    n_prod = sum(1 for r in data["workloads"] if r["production"])
    print(f"wrote {WORKLOADS_PATH}: {len(data['workloads'])} rows ({n_prod} production)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
