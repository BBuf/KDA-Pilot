#!/usr/bin/env python3
"""Generate bench/workloads.json from the retained HunyuanVideo capture JSONL.

The retained capture (96 rows) lives in pre-reset git history and is the
authoritative workload source for this task:

    git -C ../.. show \
        02b54f9f2:kernels/h200_diffusion_group_norm_silu__multi_shape/docs/captured_shapes_h200.jsonl \
        | python3 bench/gen_workloads.py --source - --out bench/workloads.json

Capture facts this generator validates before emitting anything:
  * exactly 96 rows: 48 under `group_norm_silu.triton_group_norm_silu`
    (args = x, weight[C], bias[C]; kwargs = num_groups=32, eps=1e-6) and 48
    under `group_norm_silu.apply_group_norm_silu` (args = x, <GroupNorm>,
    <SiLU>), with identical x-shape sets — the wrapper rows record the same
    physical calls one frame up the stack;
  * every row: fp16, contiguous, model=hunyuanvideo, 5-D [1, C, T, H, W].

Emitted workloads:
  * 48 production rows (`production: true`) timed through the local
    triton-equivalent entry — the headline set (one per unique x signature);
  * 4 representative wrapper diagnostic rows (`production: false`) timed
    through the local apply-equivalent entry (module construction outside
    timing); wrapper coverage beyond these lives in bench/correctness.py.

Every capture row id (entry, call_idx) is accounted for in the workload
metadata so coverage can be re-audited mechanically.
"""

from __future__ import annotations

import argparse
import json
import sys
from collections import defaultdict

TRITON_KERNEL = "group_norm_silu.triton_group_norm_silu"
APPLY_KERNEL = "group_norm_silu.apply_group_norm_silu"
NUM_GROUPS = 32
EPS = 1e-06
# fp16 comparison tolerance from docs/diffusion_correctness_contract.md.
FP16_ATOL = 3e-3
FP16_RTOL = 3e-3


def load_rows(source: str) -> list[dict]:
    fh = sys.stdin if source == "-" else open(source, "r", encoding="utf-8")
    with fh:
        return [json.loads(line) for line in fh if line.strip()]


def x_signature(row: dict) -> tuple:
    x = row["args"][0]
    return (tuple(x["shape"]), x["dtype"], bool(x["contiguous"]))


def group_size(shape: tuple[int, ...]) -> int:
    channels_per_group = shape[1] // NUM_GROUPS
    spatial = 1
    for dim in shape[2:]:
        spatial *= dim
    return channels_per_group * spatial


def size_bucket(gs: int) -> str:
    # Informational labels only (prior-round bucket boundaries); the candidate
    # dispatcher re-derives its own thresholds from fresh measurements.
    if gs < (1 << 16):
        return "small"
    if gs < 900_000:
        return "large"
    return "giant"


def validate(rows: list[dict]) -> tuple[dict, dict]:
    assert len(rows) == 96, f"expected 96 capture rows, got {len(rows)}"
    by_kernel: dict[str, list[dict]] = defaultdict(list)
    for row in rows:
        by_kernel[row["kernel"]].append(row)
    assert set(by_kernel) == {TRITON_KERNEL, APPLY_KERNEL}, sorted(by_kernel)
    assert len(by_kernel[TRITON_KERNEL]) == 48, len(by_kernel[TRITON_KERNEL])
    assert len(by_kernel[APPLY_KERNEL]) == 48, len(by_kernel[APPLY_KERNEL])

    triton_sigs: dict[tuple, list[dict]] = defaultdict(list)
    apply_sigs: dict[tuple, list[dict]] = defaultdict(list)
    for row in by_kernel[TRITON_KERNEL]:
        triton_sigs[x_signature(row)].append(row)
    for row in by_kernel[APPLY_KERNEL]:
        apply_sigs[x_signature(row)].append(row)
    assert len(triton_sigs) == 48 and len(apply_sigs) == 48
    assert set(triton_sigs) == set(apply_sigs), "entry x-shape sets diverge"

    for row in rows:
        x = row["args"][0]
        assert x["dtype"] == "torch.float16", row
        assert x["contiguous"] is True, row
        assert row["model"] == "hunyuanvideo", row
        shape = x["shape"]
        assert len(shape) == 5 and shape[0] == 1, row
        assert shape[1] % NUM_GROUPS == 0, row
        if row["kernel"] == TRITON_KERNEL:
            kw = row["kwargs"]
            assert kw["num_groups"] == NUM_GROUPS and kw["eps"] == EPS, row
            w, b = row["args"][1], row["args"][2]
            assert w["shape"] == [shape[1]] and b["shape"] == [shape[1]], row
            assert w["dtype"] == b["dtype"] == "torch.float16", row
    return triton_sigs, apply_sigs


def shape_tag(shape: tuple[int, ...]) -> str:
    return "x".join(str(d) for d in shape)


def build_workloads(triton_sigs: dict, apply_sigs: dict) -> list[dict]:
    ordered = sorted(triton_sigs, key=lambda sig: (group_size(sig[0]), sig[0]))
    workloads = []
    for sig in ordered:
        shape, dtype, _contig = sig
        gs = group_size(shape)
        workloads.append(
            {
                "id": f"prod__triton__{shape_tag(shape)}__f16__g{NUM_GROUPS}",
                "function": "triton_group_norm_silu",
                "production": True,
                "shapes": {"x": list(shape)},
                "dtype": "float16",
                "num_groups": NUM_GROUPS,
                "eps": EPS,
                "contiguous": True,
                "atol": FP16_ATOL,
                "rtol": FP16_RTOL,
                "capture": {
                    "group_size": gs,
                    "size_bucket": size_bucket(gs),
                    "triton_call_idx": sorted(
                        r["call_idx"] for r in triton_sigs[sig]
                    ),
                    "apply_call_idx": sorted(
                        r["call_idx"] for r in apply_sigs[sig]
                    ),
                    "capture_count": len(triton_sigs[sig]) + len(apply_sigs[sig]),
                    "entries_observed": ["triton", "apply"],
                },
            }
        )

    # Wrapper-path diagnostics: smallest, two interior, and largest group_size.
    picks = [ordered[0], ordered[len(ordered) // 3], ordered[2 * len(ordered) // 3], ordered[-1]]
    for sig in picks:
        shape, _dtype, _contig = sig
        gs = group_size(shape)
        workloads.append(
            {
                "id": f"diag__apply__{shape_tag(shape)}__f16__g{NUM_GROUPS}",
                "function": "apply_group_norm_silu",
                "production": False,
                "shapes": {"x": list(shape)},
                "dtype": "float16",
                "num_groups": NUM_GROUPS,
                "eps": EPS,
                "contiguous": True,
                "atol": FP16_ATOL,
                "rtol": FP16_RTOL,
                "capture": {
                    "group_size": gs,
                    "size_bucket": size_bucket(gs),
                    "note": "wrapper-path diagnostic; same physical call as the "
                    "matching prod__triton row, timed via the apply wrapper",
                },
            }
        )
    return workloads


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", required=True, help="capture JSONL path or '-' for stdin")
    parser.add_argument("--out", required=True, help="output workloads.json path")
    args = parser.parse_args()

    rows = load_rows(args.source)
    triton_sigs, apply_sigs = validate(rows)
    workloads = build_workloads(triton_sigs, apply_sigs)

    # bench/benchmark.py (the standard template) requires workloads.json to be
    # a bare JSON list; task-level provenance lives in workloads_meta.json.
    with open(args.out, "w", encoding="utf-8") as fh:
        json.dump(workloads, fh, indent=1)
        fh.write("\n")
    meta = {
        "task": "h200_diffusion_group_norm_silu__multi_shape",
        "target_gpu": "NVIDIA H200",
        "source": {
            "capture_jsonl": "git show 02b54f9f2:kernels/h200_diffusion_group_norm_silu__multi_shape/docs/captured_shapes_h200.jsonl",
            "capture_rows": len(rows),
            "model": "hunyuanvideo",
            "capture_host": "ion8-h200",
            "generator": "bench/gen_workloads.py",
        },
        "headline": {
            "metric": "equal-weight geometric mean of baseline_median/candidate_median",
            "set": "production==true rows (48 unique x signatures, triton entry)",
        },
    }
    meta_path = args.out.rsplit(".", 1)[0] + "_meta.json"
    with open(meta_path, "w", encoding="utf-8") as fh:
        json.dump(meta, fh, indent=1)
        fh.write("\n")

    prod = [w for w in workloads if w["production"]]
    print(f"wrote {args.out}: {len(prod)} production + {len(workloads) - len(prod)} diagnostic workloads")
    channels = sorted({w["shapes"]["x"][1] for w in prod})
    temporal = sorted({w["shapes"]["x"][2] for w in prod})
    spatial = sorted({(w["shapes"]["x"][3], w["shapes"]["x"][4]) for w in prod})
    print(f"channels: {channels}")
    print(f"temporal depths: {temporal}")
    print(f"spatial pairs: {spatial}")
    buckets = defaultdict(int)
    for w in prod:
        buckets[w["capture"]["size_bucket"]] += 1
    print(f"bucket counts: {dict(buckets)}")


if __name__ == "__main__":
    main()
