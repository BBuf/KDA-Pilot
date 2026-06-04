#!/usr/bin/env python3
"""Generate the frozen bench/workloads.json for this task.

Production rows come from the captured production call signatures in
``bench/captured_shapes_b200.jsonl`` (43 captured rows -> 39 unique signatures;
tensor shapes for this kernel family are architecture-independent per
``../../docs/diffusion_benchmark_shape_coverage.md``, which is the governing
contract; this generator cross-checks against it via bench/check_workloads.py).
The fresh 2026-06-03 firered-edit-1.1 H200 capture contributes no new unique
signature — its rows coincide with the qwen-edit S=189/195 and firered-edit-1.0
S=8424 signatures — so it is recorded as extra model attribution.

A small non-headline regression grid (production=false) is appended for edge
layouts/dtypes from ``../../docs/diffusion_correctness_contract.md``.

Run once to (re)generate; workloads are frozen before tuning starts.
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

BENCH_DIR = Path(__file__).resolve().parent
CAPTURES = BENCH_DIR / "captured_shapes_b200.jsonl"
OUTPUT = BENCH_DIR / "workloads.json"

NSS = "fused_norm_scale_shift"
SRNSS = "fused_scale_residual_norm_scale_shift"

DTYPE_SHORT = {
    "torch.bfloat16": "bf16",
    "torch.float16": "fp16",
    "torch.float32": "fp32",
}
DTYPE_NAME = {
    "torch.bfloat16": "bfloat16",
    "torch.float16": "float16",
    "torch.float32": "float32",
}


def _layout(shape: list[int], B: int, S: int, D: int) -> str:
    t = tuple(shape)
    if len(t) == 1:
        return "1" if t[0] == 1 else "D"
    if len(t) == 2:
        return ("1D" if t[0] == 1 else "BD") if t[1] == D else "?"
    if len(t) == 3:
        if t[2] != D:
            return "?"
        if t[0] == 1 and t[1] == 1:
            return "11D"
        if t[0] == 1 and t[1] == S:
            return "1SD"
        if t[0] == B and t[1] == 1:
            return "B1D"
        if t[0] == B and t[1] == S:
            return "BSD"
        return "?"
    if len(t) == 4 and t[0] == B and t[2] == 1 and t[3] == D:
        return "BF1D"
    return "?"


def _spec(arg, B, S, D):
    if arg is None:
        return None
    layout = _layout(arg["shape"], B, S, D)
    if layout == "?":
        raise ValueError(f"unclassifiable operand shape {arg['shape']} for B={B} S={S} D={D}")
    spec = {"layout": layout, "dtype": DTYPE_NAME[arg["dtype"]]}
    if layout == "BF1D":
        spec["F"] = arg["shape"][1]
    return spec


def _tag(spec, prefix):
    if spec is None:
        return f"{prefix}none" if prefix == "g" else ""
    short = {"bfloat16": "bf16", "float16": "fp16", "float32": "fp32"}[spec["dtype"]]
    return f"{prefix}{spec['layout']}.{short}"


def _seed_component(workload_id: str) -> int:
    digest = hashlib.sha256(workload_id.encode("utf-8")).digest()
    return int.from_bytes(digest[:2], "little")


def _tolerance(*dtypes):
    present = [d for d in dtypes if d]
    non_fp32 = any(d != "float32" for d in present)
    tol = 5e-2 if non_fp32 else 1e-5
    return tol, tol


def parse_production():
    rows = [json.loads(line) for line in CAPTURES.read_text().splitlines() if line.strip()]
    unique = {}
    for row in rows:
        kernel = row["kernel"].split(".")[-1]
        args = row["args"]
        norm_type, eps = args[-2], float(args[-1])
        tensors = args[:-2]
        if kernel == NSS:
            x, weight, bias, scale, shift = tensors
            residual = gate = None
        elif kernel == SRNSS:
            residual, x, gate, weight, bias, scale, shift = tensors
        else:
            raise ValueError(f"unknown kernel {row['kernel']}")
        B, S, D = x["shape"]
        specs = {
            "x": _spec(x, B, S, D),
            "residual": _spec(residual, B, S, D),
            "gate": _spec(gate, B, S, D),
            "weight": _spec(weight, B, S, D),
            "bias": _spec(bias, B, S, D),
            "scale": _spec(scale, B, S, D),
            "shift": _spec(shift, B, S, D),
        }
        key = (
            kernel, norm_type, eps, B, S, D,
            json.dumps(specs, sort_keys=True),
        )
        entry = unique.setdefault(
            key,
            {"kernel": kernel, "norm_type": norm_type, "eps": eps,
             "B": B, "S": S, "D": D, "specs": specs, "models": set()},
        )
        entry["models"].add(row["model"])

    # firered-edit-1.1 (fresh 2026-06-03 H200 capture) coincides with existing
    # unique signatures; attach attribution per the coverage doc.
    for entry in unique.values():
        s, d = entry["S"], entry["D"]
        if d == 3072 and entry["norm_type"] == "layer" and entry["eps"] == 1e-06:
            sc = entry["specs"]["scale"]
            if s in (189, 195) and sc and sc["layout"] == "1D":
                entry["models"].add("firered-edit-1.1")
            if s == 8424 and sc and sc["layout"] == "11D":
                entry["models"].add("firered-edit-1.1")

    workloads = []
    for entry in unique.values():
        kern_tag = "nss" if entry["kernel"] == NSS else "srnss"
        sp = entry["specs"]
        xs = DTYPE_SHORT["torch." + sp["x"]["dtype"]]
        parts = [f"{kern_tag}-b{entry['B']}-s{entry['S']}-d{entry['D']}-{xs}"]
        if entry["kernel"] == SRNSS:
            parts.append(_tag(sp["gate"], "g"))
        if sp["weight"] is not None:
            parts.append(_tag(sp["weight"], "w"))
        parts.append(_tag(sp["scale"], "s"))
        parts.append(_tag(sp["shift"], "s"))
        parts.append(f"eps{entry['eps']:g}")
        workload_id = "-".join(p for p in parts if p)
        atol, rtol = _tolerance(
            sp["x"]["dtype"],
            sp["scale"]["dtype"] if sp["scale"] else None,
            sp["shift"]["dtype"] if sp["shift"] else None,
        )
        workloads.append({
            "id": workload_id,
            "production": True,
            "function": entry["kernel"],
            "models": sorted(entry["models"]),
            "norm_type": entry["norm_type"],
            "eps": entry["eps"],
            "shapes": {
                "B": entry["B"], "S": entry["S"], "D": entry["D"],
                "x": sp["x"], "residual": sp["residual"], "gate": sp["gate"],
                "weight": sp["weight"], "bias": sp["bias"],
                "scale": sp["scale"], "shift": sp["shift"],
            },
            "strides": "contiguous",
            "seed_component": _seed_component(workload_id),
            "atol": atol,
            "rtol": rtol,
        })
    workloads.sort(key=lambda w: (w["function"], w["models"][0], w["shapes"]["S"], w["id"]))
    return workloads


def grid_rows():
    """Non-headline regression rows for edge layouts/dtypes (correctness contract grid)."""

    def make(idx, function, B, S, D, x_dt, norm, *, F=None, gate=None, wb=None,
             sc=None, sh=None):
        sc = sc or {"layout": "11D", "dtype": x_dt}
        sh = sh or dict(sc)
        specs = {
            "x": {"layout": "BSD", "dtype": x_dt},
            "residual": {"layout": "BSD", "dtype": x_dt} if function == SRNSS else None,
            "gate": gate,
            "weight": {"layout": "D", "dtype": wb} if wb else None,
            "bias": {"layout": "D", "dtype": wb} if wb else None,
            "scale": sc,
            "shift": sh,
        }
        kern_tag = "nss" if function == NSS else "srnss"
        workload_id = f"grid{idx:02d}-{kern_tag}-b{B}-s{S}-d{D}-{x_dt}-{norm}"
        atol, rtol = _tolerance(x_dt, sc["dtype"], sh["dtype"])
        shapes = {"B": B, "S": S, "D": D, "x": specs["x"], "residual": specs["residual"],
                  "gate": specs["gate"], "weight": specs["weight"], "bias": specs["bias"],
                  "scale": specs["scale"], "shift": specs["shift"]}
        if F is not None:
            shapes["F"] = F
        return {
            "id": workload_id, "production": False, "function": function,
            "models": ["regression-grid"], "norm_type": norm, "eps": 1e-5,
            "shapes": shapes, "strides": "contiguous",
            "seed_component": _seed_component(workload_id),
            "atol": atol, "rtol": rtol,
        }

    bf16, fp16, fp32 = "bfloat16", "float16", "float32"
    return [
        make(1, NSS, 1, 1024, 3072, fp16, "rms", sc={"layout": "D", "dtype": fp16}),
        make(2, NSS, 4, 512, 3072, fp32, "layer", wb=fp32, sc={"layout": "BD", "dtype": fp32}),
        make(3, NSS, 1, 1024, 3072, bf16, "layer", sc={"layout": "BSD", "dtype": bf16}),
        make(4, NSS, 4, 512, 3072, bf16, "rms", wb=bf16, sc={"layout": "B1D", "dtype": bf16}),
        make(5, NSS, 1, 1024, 3072, bf16, "layer", sc={"layout": "1", "dtype": bf16}),
        make(6, NSS, 1, 1024, 3072, bf16, "layer", F=8,
             sc={"layout": "BF1D", "dtype": bf16, "F": 8}),
        make(7, SRNSS, 1, 1024, 3072, fp16, "layer"),
        make(8, SRNSS, 4, 512, 3072, bf16, "rms", gate={"layout": "BSD", "dtype": bf16}),
        make(9, SRNSS, 1, 1024, 3072, fp32, "layer", wb=fp32,
             gate={"layout": "1D", "dtype": fp32}, sc={"layout": "1D", "dtype": fp32}),
        make(10, SRNSS, 1, 1024, 3072, bf16, "layer", F=8,
             gate={"layout": "BF1D", "dtype": bf16, "F": 8},
             sc={"layout": "BF1D", "dtype": bf16, "F": 8}),
    ]


def main():
    production = parse_production()
    if len(production) != 39:
        raise SystemExit(f"expected 39 unique production signatures, got {len(production)}")
    rows = production + grid_rows()
    ids = [w["id"] for w in rows]
    if len(ids) != len(set(ids)):
        raise SystemExit("duplicate workload ids")
    OUTPUT.write_text(json.dumps(rows, indent=2) + "\n")
    print(f"wrote {len(rows)} workloads ({len(production)} production) -> {OUTPUT}")


if __name__ == "__main__":
    main()
