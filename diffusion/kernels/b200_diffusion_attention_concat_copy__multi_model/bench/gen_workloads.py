#!/usr/bin/env python3
"""Generate + validate the frozen bench/workloads.json (top-level JSON list).

Each row carries a full self-describing schema: per-tensor
shape/dtype/stride/layout plus scalar op_type/order/h_local/h_full/h_start/
num_rep/seed/atol/rtol/production. bench/cases.py builds tensors deterministically
from these recipes; bench/adapter.py and bench/correctness.py reuse them so the
baseline, candidate, and oracle see identical inputs.

slice_heads_then_concat uses the model head contract: the full-head prefix
has the model head count h_full (24 FLUX.2 / 32 JoyAI) and is sliced to
h_local = h_full // sp_size (12 / 16 at sp_size=2) at h_start = sp_rank * h_local.
The 48/64-head synthetic-profiler variant (output heads = profiled 24/32) is kept
only as production=false regression. copy_contiguous sources are non-contiguous
head-sliced views (full_heads > output heads). Tolerances are bit-exact (0,0).

Usage:
  python3 gen_workloads.py            # (re)write workloads.json (validated)
  python3 gen_workloads.py --check    # fail if stale OR schema-invalid (freeze + schema guard)
"""

from __future__ import annotations

import argparse
import json
import os
import sys

HEAD_DIM = 128
SP_SIZE = 2  # default sequence-parallel degree used to build the frozen slice grid
DTYPES = ("bfloat16", "float16", "float32")
ORDERS = ("AB", "BA")
OP_TYPES = ("copy_contiguous", "concat_sequence", "slice_heads_then_concat")

WORKLOADS_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "workloads.json")


def _contig_stride(shape):
    s = [1] * len(shape)
    for i in range(len(shape) - 2, -1, -1):
        s[i] = s[i + 1] * shape[i + 1]
    return s


def _head_sliced_stride(B, S, full_heads, D):
    # strides (elements) of a [B, S, h, D] view sliced over the heads dim of a
    # contiguous [B, S, full_heads, D] tensor.
    return [S * full_heads * D, full_heads * D, D, 1]


def _contig_tensor(shape, dtype):
    return {"shape": list(shape), "dtype": dtype, "stride": _contig_stride(shape), "layout": "contiguous"}


def concat_row(rid, production, preset, a_shape, b_shape, order, num_rep, dtype="bfloat16", seed=0, note=""):
    B, Sa, H, D = a_shape
    Sb = b_shape[1]
    out_shape = [B, Sa + Sb, H, D]
    return {
        "id": rid, "production": production, "function": "concat_sequence",
        "op_type": "concat_sequence", "order": order,
        "h_local": H, "h_full": H, "h_start": 0, "num_rep": num_rep,
        "seed": seed, "dtype": dtype, "atol": 0, "rtol": 0,
        "tensors": {"a": _contig_tensor(a_shape, dtype), "b": _contig_tensor(b_shape, dtype)},
        "output_shape": out_shape,
        "inject_nonfinite": False,
        "source": {"preset": preset, "note": note},
    }


def copy_row(rid, production, preset, shape, full_heads, head_start, dtype="bfloat16",
             seed=0, inject_nonfinite=False, note=""):
    B, S, H, D = shape
    a = {"shape": list(shape), "dtype": dtype, "stride": _head_sliced_stride(B, S, full_heads, D),
         "layout": "head_sliced_view", "full_heads": full_heads, "head_start": head_start}
    return {
        "id": rid, "production": production, "function": "copy_contiguous",
        "op_type": "copy_contiguous", "order": "AB",
        "h_local": H, "h_full": full_heads, "h_start": head_start, "num_rep": 0,
        "seed": seed, "dtype": dtype, "atol": 0, "rtol": 0,
        "tensors": {"a": a},
        "output_shape": list(shape),
        "inject_nonfinite": inject_nonfinite,
        "source": {"preset": preset, "note": note},
    }


def slice_row(rid, production, preset, prefix_len, shard_len, h_full, h_local, sp_rank,
              order, dtype="bfloat16", seed=0, inject_nonfinite=False, note=""):
    h_start = sp_rank * h_local
    B = 1
    prefix_shape = [B, prefix_len, h_full, HEAD_DIM]   # contiguous full-head prefix
    shard_shape = [B, shard_len, h_local, HEAD_DIM]    # contiguous shard
    scratch_shape = [B, prefix_len, h_local, HEAD_DIM]
    out_shape = [B, prefix_len + shard_len, h_local, HEAD_DIM]
    return {
        "id": rid, "production": production, "function": "slice_heads_then_concat",
        "op_type": "slice_heads_then_concat", "order": order,
        "h_local": h_local, "h_full": h_full, "h_start": h_start, "num_rep": prefix_len,
        "seed": seed, "dtype": dtype, "atol": 0, "rtol": 0,
        "tensors": {"prefix": dict(_contig_tensor(prefix_shape, dtype), full_heads=h_full),
                    "shard": _contig_tensor(shard_shape, dtype)},
        "scratch_shape": scratch_shape,
        "output_shape": out_shape,
        "inject_nonfinite": inject_nonfinite,
        "source": {"preset": preset, "sp_size": h_full // h_local, "sp_rank": sp_rank, "note": note},
    }


def build_workloads():
    rows = []

    # ---------------- PRODUCTION (headline geomean) ----------------
    # concat_sequence (profiled cat operand order; num_rep = replicated prefix/suffix length)
    rows.append(concat_row("flux_concat_512_4096_h24", True, "flux2-klein-base",
                           [1, 512, 24, 128], [1, 4096, 24, 128], "AB", num_rep=512, seed=1001,
                           note="FLUX.2 cat([prefix512, shard4096]) -> [1,4608,24,128]"))
    rows.append(concat_row("joyai_concat_8048_1004_h32", True, "joyai-edit",
                           [1, 8048, 32, 128], [1, 1004, 32, 128], "AB", num_rep=1004, seed=1002,
                           note="JoyAI cat([shard8048, suffix1004]) -> [1,9052,32,128]"))

    # copy_contiguous (non-contiguous head-sliced source; full_heads > output heads)
    rows.append(copy_row("flux_copy_4608_h24", True, "flux2-klein-base",
                        [1, 4608, 24, 128], full_heads=48, head_start=0, seed=1101))
    rows.append(copy_row("joyai_copy_8048_h32", True, "joyai-edit",
                        [1, 8048, 32, 128], full_heads=64, head_start=0, seed=1102))
    rows.append(copy_row("joyai_copy_1004_h32", True, "joyai-edit",
                        [1, 1004, 32, 128], full_heads=64, head_start=0, seed=1103))

    # slice_heads_then_concat — model head contract: h_full = model heads (24/32),
    # h_local = h_full / sp_size (12/16 at sp_size=2).
    rows.append(slice_row("flux_slice_concat_512_4096_hf24_hl12_r0_AB", True, "flux2-klein-base",
                        prefix_len=512, shard_len=4096, h_full=24, h_local=12, sp_rank=0, order="AB",
                        seed=1201, note="FLUX.2 prefix-first; h_full=24 sliced to h_local=12 -> [1,4608,12,128]"))
    rows.append(slice_row("joyai_slice_concat_1004_8048_hf32_hl16_r0_BA", True, "joyai-edit",
                        prefix_len=1004, shard_len=8048, h_full=32, h_local=16, sp_rank=0, order="BA",
                        seed=1202, note="JoyAI suffix model; h_full=32 sliced to h_local=16 -> [1,9052,16,128]"))

    # ---------------- REGRESSION (production=false) ----------------
    # slice opposite order
    rows.append(slice_row("flux_slice_concat_hf24_hl12_r0_BA", False, "flux2-klein-base",
                        512, 4096, 24, 12, 0, "BA", seed=2001, note="opposite order"))
    rows.append(slice_row("joyai_slice_concat_hf32_hl16_r0_AB", False, "joyai-edit",
                        1004, 8048, 32, 16, 0, "AB", seed=2002, note="opposite order"))
    # slice nonzero sp_rank (h_start = h_local)
    rows.append(slice_row("flux_slice_concat_hf24_hl12_r1_AB", False, "flux2-klein-base",
                        512, 4096, 24, 12, 1, "AB", seed=2003, note="sp_rank=1, h_start=12"))
    rows.append(slice_row("joyai_slice_concat_hf32_hl16_r1_BA", False, "joyai-edit",
                        1004, 8048, 32, 16, 1, "BA", seed=2004, note="sp_rank=1, h_start=16"))
    # complete the order x rank cross product for the model-grid slice rows
    rows.append(slice_row("flux_slice_concat_hf24_hl12_r1_BA", False, "flux2-klein-base",
                        512, 4096, 24, 12, 1, "BA", seed=2005, note="sp_rank=1, h_start=12, opposite order"))
    rows.append(slice_row("joyai_slice_concat_hf32_hl16_r1_AB", False, "joyai-edit",
                        1004, 8048, 32, 16, 1, "AB", seed=2006, note="sp_rank=1, h_start=16, opposite order"))
    # synthetic profiler-shape variant: output heads match the profiled 24/32 (full_heads 48/64).
    rows.append(slice_row("flux_slice_concat_synth_hf48_hl24_r0_AB", False, "flux2-klein-base",
                        512, 4096, 48, 24, 0, "AB", seed=2051,
                        note="synthetic: output heads = profiled 24 (full_heads 48); regression only"))
    rows.append(slice_row("joyai_slice_concat_synth_hf64_hl32_r0_BA", False, "joyai-edit",
                        1004, 8048, 64, 32, 0, "BA", seed=2052,
                        note="synthetic: output heads = profiled 32 (full_heads 64); regression only"))
    # concat opposite orders
    rows.append(concat_row("flux_concat_512_4096_h24_BA", False, "flux2-klein-base",
                          [1, 512, 24, 128], [1, 4096, 24, 128], "BA", num_rep=512, seed=2101, note="opposite order"))
    rows.append(concat_row("joyai_concat_8048_1004_h32_BA", False, "joyai-edit",
                          [1, 8048, 32, 128], [1, 1004, 32, 128], "BA", num_rep=1004, seed=2102, note="opposite order"))
    # copy with nonzero head_start
    rows.append(copy_row("flux_copy_4608_h24_start24", False, "flux2-klein-base",
                       [1, 4608, 24, 128], full_heads=48, head_start=24, seed=2201, note="head_start=24"))
    # non-finite preservation
    rows.append(copy_row("nonfinite_copy_small", False, "synthetic",
                       [1, 8, 4, 128], full_heads=8, head_start=2, seed=2301, inject_nonfinite=True,
                       note="NaN/Inf preservation"))
    rows.append(slice_row("nonfinite_slice_concat_small", False, "synthetic",
                        prefix_len=4, shard_len=8, h_full=4, h_local=2, sp_rank=1, order="AB",
                        seed=2302, inject_nonfinite=True, note="NaN/Inf preservation"))
    # degenerate lengths
    rows.append(slice_row("degenerate_prefix1_slice_concat", False, "synthetic",
                        prefix_len=1, shard_len=3, h_full=4, h_local=1, sp_rank=2, order="BA",
                        seed=2401, note="prefix length 1, single head, sp_size 4"))
    rows.append(concat_row("degenerate_tiny_concat", False, "synthetic",
                          [1, 1, 1, 128], [1, 2, 1, 128], "AB", num_rep=1, seed=2402, note="tiny"))
    # dtype coverage (lossless => bit-exact at any dtype)
    rows.append(copy_row("fp16_copy_small", False, "synthetic",
                       [1, 64, 8, 128], full_heads=16, head_start=8, dtype="float16", seed=2501))
    rows.append(concat_row("fp32_concat_small", False, "synthetic",
                          [1, 17, 8, 128], [1, 31, 8, 128], "AB", num_rep=17, dtype="float32", seed=2502))

    return rows


# --------------------------------------------------------------------------
# Schema validator + workload audit. Pure dict checks, no torch.
# --------------------------------------------------------------------------
_ROW_SCALARS = ("id", "production", "function", "op_type", "order", "h_local", "h_full",
                "h_start", "num_rep", "seed", "dtype", "atol", "rtol", "output_shape", "tensors")
_TENSOR_FIELDS = ("shape", "dtype", "stride", "layout")


def _err(errs, rid, msg):
    errs.append(f"{rid}: {msg}")


def validate_workloads(rows):
    """Return a list of schema/contract violations (empty == valid)."""
    errs = []
    if not isinstance(rows, list):
        return ["workloads.json must be a top-level JSON list"]
    seen_ids = set()
    for r in rows:
        rid = r.get("id", "<no-id>")
        for f in _ROW_SCALARS:
            if f not in r:
                _err(errs, rid, f"missing required field '{f}'")
        if rid in seen_ids:
            _err(errs, rid, "duplicate id")
        seen_ids.add(rid)
        if r.get("op_type") not in OP_TYPES:
            _err(errs, rid, f"bad op_type {r.get('op_type')!r}")
        if r.get("order") not in ORDERS:
            _err(errs, rid, f"bad order {r.get('order')!r}")
        if r.get("dtype") not in DTYPES:
            _err(errs, rid, f"bad dtype {r.get('dtype')!r}")
        if r.get("atol") != 0 or r.get("rtol") != 0:
            _err(errs, rid, "lossless ops require atol=rtol=0")
        # per-tensor metadata
        for name, t in (r.get("tensors") or {}).items():
            for f in _TENSOR_FIELDS:
                if f not in t:
                    _err(errs, rid, f"tensor '{name}' missing '{f}'")
            if t.get("dtype") != r.get("dtype"):
                _err(errs, rid, f"tensor '{name}' dtype != row dtype")
            shape = t.get("shape")
            if isinstance(shape, list) and len(shape) == 4:
                exp = (_head_sliced_stride(shape[0], shape[1], t.get("full_heads", shape[2]), shape[3])
                       if t.get("layout") == "head_sliced_view" else _contig_stride(shape))
                if t.get("stride") != exp:
                    _err(errs, rid, f"tensor '{name}' stride {t.get('stride')} != expected {exp} for layout {t.get('layout')}")
        op = r.get("op_type")
        hl, hf, hs = r.get("h_local"), r.get("h_full"), r.get("h_start")
        if op == "copy_contiguous":
            a = (r.get("tensors") or {}).get("a", {})
            if a.get("layout") != "head_sliced_view":
                _err(errs, rid, "copy source must be a non-contiguous head_sliced_view")
            if a.get("full_heads", 0) <= a.get("shape", [0, 0, 0, 0])[2]:
                _err(errs, rid, "copy source full_heads must exceed output heads (non-contiguous)")
        elif op == "concat_sequence":
            t = r.get("tensors") or {}
            if "a" not in t or "b" not in t:
                _err(errs, rid, "concat needs tensors a and b")
            else:
                if t["a"]["shape"][2] != hl or t["b"]["shape"][2] != hl:
                    _err(errs, rid, "concat head counts must equal h_local")
                if t["a"]["shape"][1] + t["b"]["shape"][1] != r["output_shape"][1]:
                    _err(errs, rid, "concat Sa+Sb != output seq")
            if hs != 0 or hf != hl:
                _err(errs, rid, "concat requires h_start=0 and h_full==h_local")
        elif op == "slice_heads_then_concat":
            t = r.get("tensors") or {}
            pref, shard = t.get("prefix", {}), t.get("shard", {})
            if pref.get("shape", [0, 0, 0, 0])[2] != hf:
                _err(errs, rid, "slice prefix heads must equal h_full")
            if shard.get("shape", [0, 0, 0, 0])[2] != hl:
                _err(errs, rid, "slice shard heads must equal h_local")
            if hf <= hl:
                _err(errs, rid, "slice requires a real head slice: h_full > h_local (pre-sliced prefix rejected)")
            if hl <= 0:
                _err(errs, rid, "h_local must be > 0")
            if hs % hl != 0:
                _err(errs, rid, f"h_start ({hs}) must be a multiple of h_local ({hl})")
            if hs + hl > hf:
                _err(errs, rid, "h_start + h_local must be <= h_full")
            if pref.get("shape", [0, 0])[1] + shard.get("shape", [0, 0])[1] != r["output_shape"][1]:
                _err(errs, rid, "slice P+Sshard != output seq")

    # exact production-contract audit: each required row must exist with the exact tuple
    # (op_type, preset, order, h_full, h_local, h_start, output_shape).
    required = {
        "flux_concat_512_4096_h24": ("concat_sequence", "flux2-klein-base", "AB", 24, 24, 0, [1, 4608, 24, 128]),
        "joyai_concat_8048_1004_h32": ("concat_sequence", "joyai-edit", "AB", 32, 32, 0, [1, 9052, 32, 128]),
        "flux_copy_4608_h24": ("copy_contiguous", "flux2-klein-base", "AB", 48, 24, 0, [1, 4608, 24, 128]),
        "joyai_copy_8048_h32": ("copy_contiguous", "joyai-edit", "AB", 64, 32, 0, [1, 8048, 32, 128]),
        "joyai_copy_1004_h32": ("copy_contiguous", "joyai-edit", "AB", 64, 32, 0, [1, 1004, 32, 128]),
        "flux_slice_concat_512_4096_hf24_hl12_r0_AB":
            ("slice_heads_then_concat", "flux2-klein-base", "AB", 24, 12, 0, [1, 4608, 12, 128]),
        "joyai_slice_concat_1004_8048_hf32_hl16_r0_BA":
            ("slice_heads_then_concat", "joyai-edit", "BA", 32, 16, 0, [1, 9052, 16, 128]),
    }
    by_id = {r.get("id"): r for r in rows}
    prod_ids = {r.get("id") for r in rows if r.get("production")}
    for rid, want in required.items():
        if rid not in prod_ids:
            _err(errs, "<production>", f"required production row '{rid}' missing or not marked production")
            continue
        r = by_id[rid]
        got = (r.get("op_type"), r.get("source", {}).get("preset"), r.get("order"),
               r.get("h_full"), r.get("h_local"), r.get("h_start"), r.get("output_shape"))
        if got != want:
            _err(errs, rid, f"production contract mismatch: got {got} != required {want}")
    # secondary: the model-grid slice rows must cover both orders x {rank0, rank1} per model
    slice_matrix = {(r["source"].get("preset"), r["order"], r["h_start"])
                    for r in rows if r["op_type"] == "slice_heads_then_concat" and r["h_full"] in (24, 32)}
    for preset, hl in (("flux2-klein-base", 12), ("joyai-edit", 16)):
        for order in ("AB", "BA"):
            for hs in (0, hl):
                if (preset, order, hs) not in slice_matrix:
                    _err(errs, "<slice-matrix>", f"missing slice row {preset} order={order} h_start={hs}")
    return errs


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true", help="fail if workloads.json is stale or schema-invalid")
    args = ap.parse_args()

    data = build_workloads()
    errs = validate_workloads(data)
    if errs:
        print("SCHEMA VALIDATION FAILED:", file=sys.stderr)
        for e in errs:
            print("  -", e, file=sys.stderr)
        return 1
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
        # also validate the on-disk file independently
        disk_errs = validate_workloads(json.loads(current))
        if disk_errs:
            print("on-disk workloads.json is schema-invalid:", file=sys.stderr)
            for e in disk_errs:
                print("  -", e, file=sys.stderr)
            return 1
        print(f"workloads.json up to date and schema-valid ({len(data)} rows)")
        return 0

    with open(WORKLOADS_PATH, "w") as f:
        f.write(rendered)
    n_prod = sum(1 for r in data if r["production"])
    print(f"wrote {WORKLOADS_PATH}: {len(data)} rows ({n_prod} production); schema-valid")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
