#!/usr/bin/env python3
"""Generate or verify bench/workloads.json from the retained live capture.

The production workload set is NOT hand-written: it is derived row-for-row
from the retained pre-reset capture JSONL stored in this repository's git
history (160 live HunyuanVideo VAE rows captured on ion-b200), per
docs/diffusion_benchmark_shape_coverage.md. The canonical regression grid rows
from docs/diffusion_correctness_contract.md ride along as non-production rows.

Usage:
    python3 bench/gen_workloads.py            # write bench/workloads.json
    python3 bench/gen_workloads.py --check    # verify the frozen file matches
                                              # a fresh derivation (exit != 0
                                              # on any mismatch)
"""

from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
import sys
from pathlib import Path

BENCH_DIR = Path(__file__).resolve().parent
TASK_DIR = BENCH_DIR.parent
WORKLOADS_PATH = BENCH_DIR / "workloads.json"

# Retained live capture: pre-reset git history of this repository.
CAPTURE_REV = "35bc2c6b4~1"
CAPTURE_PATH = (
    "kernels/b200_diffusion_group_norm_silu__multi_shape/docs/captured_shapes_b200.jsonl"
)
EXPECTED_CAPTURE_ROWS = 160

# Production parameters not embedded in the capture rows, fixed by
# docs/diffusion_benchmark_shape_coverage.md for this family:
# "Dtype is fp16. num_groups=32, eps=1e-6 for the Triton entry point" and the
# HunyuanVideo VAE GroupNorm modules use the same eps.
PROD_NUM_GROUPS = 32
PROD_EPS = 1e-6
PROD_DTYPE = "float16"
PROD_TOL = {"float16": (3e-3, 3e-3)}

# Canonical regression grid (docs/diffusion_correctness_contract.md). The
# upstream test grid uses eps=1e-5.
GRID_SHAPES = [
    ("image_2d", (2, 64, 32, 32)),
    ("video_3d", (1, 64, 4, 16, 16)),
    ("token_2d", (4, 128)),
    ("large_tile", (1, 128, 20, 256, 256)),
]
GRID_DTYPES = ["float16", "bfloat16", "float32"]
GRID_EPS = 1e-5
GRID_NUM_GROUPS = 32
GRID_TOL = {
    "float16": (3e-3, 3e-3),
    "bfloat16": (7e-2, 2e-2),
    "float32": (1e-5, 1e-5),
}

KERNEL_TO_FUNCTION = {
    "group_norm_silu.apply_group_norm_silu": "apply_group_norm_silu",
    "group_norm_silu.triton_group_norm_silu": "triton_group_norm_silu",
}
FUNCTION_SHORT = {
    "apply_group_norm_silu": "apply",
    "triton_group_norm_silu": "triton",
}


def contiguous_strides(shape: tuple[int, ...]) -> tuple[int, ...]:
    strides = [1] * len(shape)
    for i in range(len(shape) - 2, -1, -1):
        strides[i] = strides[i + 1] * shape[i + 1]
    return tuple(strides)


def channels_last_3d_strides(shape: tuple[int, ...]) -> tuple[int, ...]:
    _n, c, d, h, w = shape
    return (c * d * h * w, 1, h * w * c, w * c, c)


def load_capture_rows() -> list[dict]:
    out = subprocess.run(
        ["git", "show", f"{CAPTURE_REV}:{CAPTURE_PATH}"],
        capture_output=True,
        text=True,
        check=True,
        cwd=TASK_DIR,
    ).stdout
    rows = [json.loads(line) for line in out.splitlines() if line.strip()]
    if len(rows) != EXPECTED_CAPTURE_ROWS:
        raise RuntimeError(
            f"expected {EXPECTED_CAPTURE_ROWS} capture rows, got {len(rows)}"
        )
    return rows


def classify_layout(shape: tuple[int, ...], strides: tuple[int, ...], contiguous: bool):
    if contiguous:
        if strides != contiguous_strides(shape):
            raise RuntimeError(f"contiguous row with unexpected strides: {shape} {strides}")
        return "contiguous"
    if len(shape) == 5 and strides == channels_last_3d_strides(shape):
        return "channels_last_3d"
    raise RuntimeError(f"unrecognized non-contiguous layout: {shape} {strides}")


def production_workloads() -> list[dict]:
    workloads = []
    seen_ids = set()
    for row in sorted(load_capture_rows(), key=lambda r: r["call_idx"]):
        kernel = row["kernel"]
        function = KERNEL_TO_FUNCTION[kernel]
        x_meta = row["args"][0]
        shape = tuple(x_meta["shape"])
        strides = tuple(x_meta["strides"])
        dtype = x_meta["dtype"].replace("torch.", "")
        if dtype != PROD_DTYPE:
            raise RuntimeError(f"unexpected production dtype {dtype}")
        # Harden the capture-row assumptions instead of silently trusting them:
        # captured kwargs must be empty or agree with the documented
        # num_groups/eps; the remaining positional args must look like the
        # expected weight/bias tensors (triton entry) or module markers
        # (apply entry).
        kwargs = row.get("kwargs") or {}
        if kwargs:
            if kwargs.get("num_groups", PROD_NUM_GROUPS) != PROD_NUM_GROUPS:
                raise RuntimeError(f"capture num_groups mismatch: {kwargs}")
            if abs(kwargs.get("eps", PROD_EPS) - PROD_EPS) > 0.0:
                raise RuntimeError(f"capture eps mismatch: {kwargs}")
        extra = row["args"][1:]
        if function == "triton_group_norm_silu":
            for meta in extra[:2]:
                if not (
                    isinstance(meta, dict)
                    and tuple(meta["shape"]) == (shape[1],)
                    and meta["dtype"].replace("torch.", "") == PROD_DTYPE
                ):
                    raise RuntimeError(f"unexpected triton weight/bias meta: {meta}")
        else:
            if extra[:2] != ["<GroupNorm>", "<SiLU>"]:
                raise RuntimeError(f"unexpected apply module markers: {extra}")
        layout = classify_layout(shape, strides, x_meta["contiguous"])
        layout_tag = "C" if layout == "contiguous" else "NC"
        atol, rtol = PROD_TOL[dtype]
        wid = (
            f"hv_{FUNCTION_SHORT[function]}_"
            + "x".join(str(s) for s in shape)
            + f"_{layout_tag}"
        )
        if wid in seen_ids:
            raise RuntimeError(f"duplicate workload id {wid}")
        seen_ids.add(wid)
        workloads.append(
            {
                "id": wid,
                "production": True,
                "function": function,
                "shapes": {
                    "x": list(shape),
                    "layout": layout,
                    "strides": list(strides),
                    "dtype": dtype,
                    "num_groups": PROD_NUM_GROUPS,
                    "eps": PROD_EPS,
                },
                "atol": atol,
                "rtol": rtol,
                "source": {
                    "preset": row["model"],
                    "host": row["host"],
                    "arch": row["arch"],
                    "call_idx": row["call_idx"],
                    "capture_rev": CAPTURE_REV,
                },
            }
        )
    return workloads


def grid_workloads() -> list[dict]:
    workloads = []
    for name, shape in GRID_SHAPES:
        for dtype in GRID_DTYPES:
            atol, rtol = GRID_TOL[dtype]
            workloads.append(
                {
                    "id": f"grid_{name}_{dtype}",
                    "production": False,
                    "function": "triton_group_norm_silu",
                    "shapes": {
                        "x": list(shape),
                        "layout": "contiguous",
                        "strides": list(contiguous_strides(shape)),
                        "dtype": dtype,
                        "num_groups": GRID_NUM_GROUPS,
                        "eps": GRID_EPS,
                    },
                    "atol": atol,
                    "rtol": rtol,
                    "source": {"contract": "docs/diffusion_correctness_contract.md"},
                }
            )
    return workloads


def derive() -> list[dict]:
    return production_workloads() + grid_workloads()


def file_sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="verify frozen file")
    args = parser.parse_args()

    derived = derive()
    n_prod = sum(1 for w in derived if w["production"])
    if args.check:
        if not WORKLOADS_PATH.exists():
            print(f"FAIL: {WORKLOADS_PATH} missing", file=sys.stderr)
            return 1
        frozen = json.loads(WORKLOADS_PATH.read_text())
        if frozen != derived:
            frozen_ids = [w.get("id") for w in frozen]
            derived_ids = [w.get("id") for w in derived]
            print("FAIL: frozen workloads.json does not match fresh derivation", file=sys.stderr)
            print(f"  frozen rows: {len(frozen)}  derived rows: {len(derived)}", file=sys.stderr)
            for fid in derived_ids:
                if fid not in frozen_ids:
                    print(f"  missing id: {fid}", file=sys.stderr)
            for fid in frozen_ids:
                if fid not in derived_ids:
                    print(f"  extra id: {fid}", file=sys.stderr)
            return 1
        print(
            f"OK: workloads.json matches derivation ({n_prod} production + "
            f"{len(derived) - n_prod} grid rows); sha256={file_sha256(WORKLOADS_PATH)}"
        )
        return 0

    WORKLOADS_PATH.write_text(json.dumps(derived, indent=1) + "\n")
    print(
        f"wrote {WORKLOADS_PATH} ({n_prod} production + {len(derived) - n_prod} "
        f"grid rows); sha256={file_sha256(WORKLOADS_PATH)}"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
