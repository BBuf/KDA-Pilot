#!/usr/bin/env python3
"""Coverage validator for bench/workloads.json and docs/benchmark_preset_audit.md.

The requirement table below is hand-derived from the
``diffusion_cutedsl_norm_scale_shift__multi_shape`` section of
``../../docs/diffusion_benchmark_shape_coverage.md`` (independent of
bench/gen_workloads.py, which derives rows from the captured-call JSONL).
Exit code is non-zero if any retained live shape row is missing from the
production workload set, if required workload fields are absent, if the
regression grid loses required edge coverage, or if the preset audit does not
give every current benchmark preset an explicit status.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

TASK_DIR = Path(__file__).resolve().parents[1]
NSS = "fused_norm_scale_shift"
SRNSS = "fused_scale_residual_norm_scale_shift"

# (model, function, S, D, scale_dtype or None for "any")
REQUIRED_PRODUCTION = [
    ("qwen", NSS, 19, 3072, None),
    ("qwen", NSS, 47, 3072, None),
    ("qwen", NSS, 4096, 3072, None),
    ("qwen", SRNSS, 19, 3072, None),
    ("qwen", SRNSS, 47, 3072, None),
    ("qwen", SRNSS, 4096, 3072, None),
    ("qwen-edit", NSS, 189, 3072, None),
    ("qwen-edit", NSS, 195, 3072, None),
    ("qwen-edit", SRNSS, 189, 3072, None),
    ("qwen-edit", SRNSS, 195, 3072, None),
    ("firered-edit-1.0", NSS, 8424, 3072, None),
    ("firered-edit-1.0", SRNSS, 8424, 3072, None),
    ("joyai-edit", NSS, 997, 4096, None),
    ("joyai-edit", NSS, 1004, 4096, None),
    ("joyai-edit", NSS, 7904, 4096, None),
    ("hunyuanvideo", NSS, 55, 3072, None),
    ("hunyuanvideo", NSS, 27030, 3072, None),
    ("hunyuanvideo", NSS, 27085, 3072, None),
    ("hunyuanvideo", SRNSS, 55, 3072, None),
    ("hunyuanvideo", SRNSS, 27030, 3072, None),
    # wan-ti2v: both bf16 and fp32 full-shape scale/shift variants
    ("wan-ti2v", NSS, 18144, 3072, "bfloat16"),
    ("wan-ti2v", NSS, 18144, 3072, "float32"),
    ("wan-ti2v", SRNSS, 18144, 3072, "float32"),
    ("wan-ti2v", SRNSS, 18144, 3072, "bfloat16"),  # scalar bf16 scale on the affine row
    # wan-t2v: fp32 [1,1,5120] at S=37800 and bf16 [1,1,5120] at S=75600
    ("wan-t2v", NSS, 37800, 5120, "float32"),
    ("wan-t2v", NSS, 75600, 5120, "bfloat16"),
    ("wan-t2v", SRNSS, 37800, 5120, "float32"),
    ("wan-t2v", SRNSS, 37800, 5120, "bfloat16"),
    # wan-i2v: fp32 at S=37044 and bf16 at S=74088
    ("wan-i2v", NSS, 37044, 5120, "float32"),
    ("wan-i2v", NSS, 74088, 5120, "bfloat16"),
    ("wan-i2v", SRNSS, 37044, 5120, "float32"),
    ("wan-i2v", SRNSS, 37044, 5120, "bfloat16"),
    ("mova-720p", NSS, 101, 1536, None),
    ("mova-720p", NSS, 44100, 5120, None),
    ("mova-720p", NSS, 176400, 5120, None),
    ("mova-720p", SRNSS, 101, 1536, None),
    ("mova-720p", SRNSS, 44100, 5120, None),
    # helios: fused_norm_scale_shift only; bf16 row at S=8640, fp32 row at S=11040
    ("helios", NSS, 8640, 5120, "bfloat16"),
    ("helios", NSS, 11040, 5120, "float32"),
    ("firered-edit-1.1", NSS, 189, 3072, None),
    ("firered-edit-1.1", NSS, 195, 3072, None),
    ("firered-edit-1.1", NSS, 8424, 3072, None),
    ("firered-edit-1.1", SRNSS, 189, 3072, None),
    ("firered-edit-1.1", SRNSS, 195, 3072, None),
    ("firered-edit-1.1", SRNSS, 8424, 3072, None),
]

REQUIRED_ROW_FIELDS = (
    "id", "production", "function", "models", "norm_type", "eps",
    "shapes", "strides", "seed_component", "atol", "rtol",
)

# Edge coverage the non-headline regression grid must keep
# (predicate name -> lambda over grid rows).
GRID_REQUIREMENTS = {
    "fp16 activation": lambda r: r["shapes"]["x"]["dtype"] == "float16",
    "fp32 activation": lambda r: r["shapes"]["x"]["dtype"] == "float32",
    "rms norm": lambda r: r["norm_type"] == "rms",
    "affine weight+bias": lambda r: r["shapes"]["weight"] is not None,
    "scalar [1] scale": lambda r: r["shapes"]["scale"]["layout"] == "1",
    "layout D": lambda r: r["shapes"]["scale"]["layout"] == "D",
    "layout BD": lambda r: r["shapes"]["scale"]["layout"] == "BD",
    "layout B1D": lambda r: r["shapes"]["scale"]["layout"] == "B1D",
    "layout BSD scale": lambda r: r["shapes"]["scale"]["layout"] == "BSD",
    "layout BF1D": lambda r: r["shapes"]["scale"]["layout"] == "BF1D",
    "batch > 1": lambda r: r["shapes"]["B"] > 1,
    "residual variant": lambda r: r["function"] == SRNSS,
    "per-token gate": lambda r: (r["shapes"].get("gate") or {}).get("layout") == "BSD",
}

CURRENT_PRESETS = [
    "flux", "flux2", "qwen", "qwen-edit", "zimage", "wan-t2v", "wan-ti2v",
    "ltx2", "ltx23-ti2v-two-stage", "wan-i2v", "ltx23-one-stage",
    "ltx23-two-stage", "ltx23-two-stage-cfg-parallel", "hunyuanvideo",
    "mova-720p", "helios", "joyai-edit", "firered-edit-1.0",
    "firered-edit-1.1", "hunyuan3d-shape",
]
STATUS_TOKENS = ("captured", "no-call", "blocked")


def check_workloads(path: Path) -> list[str]:
    errors: list[str] = []
    rows = json.loads(path.read_text())
    for row in rows:
        missing = [f for f in REQUIRED_ROW_FIELDS if f not in row]
        if missing:
            errors.append(f"workload {row.get('id', '<no id>')} missing fields: {missing}")
    ids = [r["id"] for r in rows]
    if len(ids) != len(set(ids)):
        errors.append("duplicate workload ids present")

    production = [r for r in rows if r.get("production")]
    for model, function, s, d, scale_dtype in REQUIRED_PRODUCTION:
        def _match(r):
            sh = r["shapes"]
            if r["function"] != function or model not in r["models"]:
                return False
            if sh["S"] != s or sh["D"] != d:
                return False
            if scale_dtype is not None and sh["scale"]["dtype"] != scale_dtype:
                return False
            return True
        if not any(_match(r) for r in production):
            errors.append(
                f"missing required production row: model={model} function={function} "
                f"S={s} D={d} scale_dtype={scale_dtype or 'any'}"
            )

    grid = [r for r in rows if not r.get("production")]
    if not grid:
        errors.append("regression grid rows are missing entirely")
    for name, pred in GRID_REQUIREMENTS.items():
        if not any(pred(r) for r in grid):
            errors.append(f"regression grid lost edge coverage: {name}")
    return errors


def check_preset_audit(path: Path) -> list[str]:
    errors: list[str] = []
    if not path.exists():
        return [f"preset audit file missing: {path}"]
    text = path.read_text()
    for preset in CURRENT_PRESETS:
        # find the audit line for this preset
        lines = [ln for ln in text.splitlines() if f"`{preset}`" in ln]
        if not lines:
            errors.append(f"preset audit missing entry for `{preset}`")
            continue
        if not any(any(tok in ln for tok in STATUS_TOKENS) for ln in lines):
            errors.append(f"preset audit entry for `{preset}` has no explicit status")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--workloads", type=Path, default=TASK_DIR / "bench" / "workloads.json")
    parser.add_argument("--audit", type=Path, default=TASK_DIR / "docs" / "benchmark_preset_audit.md")
    args = parser.parse_args()

    errors = check_workloads(args.workloads) + check_preset_audit(args.audit)
    if errors:
        for err in errors:
            print(f"FAIL: {err}", file=sys.stderr)
        return 1
    print(
        f"OK: workload coverage and preset audit pass "
        f"({args.workloads.name}, {args.audit.name})"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
