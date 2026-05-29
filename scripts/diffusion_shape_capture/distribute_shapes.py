"""Refresh diffusion task shape ledgers from live capture JSONL files.

The output is intentionally empirical only: every workload row in the generated
task docs and prompt sections comes from a captured call record. Analytical or
model-config-derived shapes are not carried forward.

Usage:
    python3 scripts/diffusion_shape_capture/distribute_shapes.py \
      --input /tmp/shapes_b200.jsonl \
      --input /tmp/shapes_h200_8.jsonl \
      --input /tmp/shapes_h200_9.jsonl
"""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any

REPO_ROOT = Path(__file__).resolve().parents[2]
KERNELS_DIR = REPO_ROOT / "kernels"

DEFAULT_CAPTURE_FILES = [
    Path("/tmp/shapes_h200_8.jsonl"),
    Path("/tmp/shapes_h200_9.jsonl"),
    Path("/tmp/shapes_b200.jsonl"),
]

SWEEP_START_RE = re.compile(r"\[sweep\] preset=(\S+) host=(\S+) arch=(\S+) ")
SWEEP_STATUS_RE = re.compile(
    r"\[sweep\] preset=(\S+) exit=\d+ status=(\S+) new_shape_lines=(\d+) "
)

KERNEL_TO_FAMILY = {
    "qknorm_rope.fused_inplace_qknorm_rope": "diffusion_qknorm_rope__multi_shape",
    "norm.rms_norm_fn": "diffusion_rms_norm_fn__multi_shape",
    "norm.norm_infer": "diffusion_norm_infer__multi_shape",
    "rmsnorm_onepass.triton_one_pass_rms_norm": "diffusion_norm_infer__multi_shape",
    "group_norm_silu.triton_group_norm_silu": "diffusion_group_norm_silu__multi_shape",
    "group_norm_silu.apply_group_norm_silu": "diffusion_group_norm_silu__multi_shape",
    "rotary.apply_rotary_embedding": "diffusion_rotary_embedding__multi_shape",
    "ltx2_rotary.apply_ltx2_split_rotary_emb": "diffusion_rotary_embedding__multi_shape",
    "scale_shift.fuse_scale_shift_kernel": "diffusion_fuse_scale_shift__multi_shape",
    "scale_shift.fuse_layernorm_scale_shift_gate_select01_kernel": "diffusion_fuse_scale_shift__multi_shape",
    "scale_shift.fuse_residual_layernorm_scale_shift_gate_select01_kernel": "diffusion_fuse_scale_shift__multi_shape",
    "norm_tanh_mul_add_norm_scale.fused_norm_tanh_mul_add": "diffusion_cutedsl_norm_tanh_mul_add__multi_shape",
    "norm_tanh_mul_add_norm_scale.fused_norm_tanh_mul_add_norm_scale": "diffusion_cutedsl_norm_tanh_mul_add__multi_shape",
    "scale_residual_norm_scale_shift.fused_norm_scale_shift": "diffusion_cutedsl_norm_scale_shift__multi_shape",
    "scale_residual_norm_scale_shift.fused_scale_residual_norm_scale_shift": "diffusion_cutedsl_norm_scale_shift__multi_shape",
}

FAMILIES = sorted(set(KERNEL_TO_FAMILY.values()))
ARCHS = ("b200", "h200")

MODEL_NAMES = {
    "flux": "black-forest-labs/FLUX.1-dev",
    "flux2": "black-forest-labs/FLUX.2-dev",
    "qwen": "Qwen/Qwen-Image-2512",
    "qwen-edit": "Qwen/Qwen-Image-Edit-2511",
    "zimage": "Tongyi-MAI/Z-Image-Turbo",
    "wan-t2v": "Wan-AI/Wan2.2-T2V-A14B-Diffusers",
    "wan-ti2v": "Wan-AI/Wan2.2-TI2V-5B-Diffusers",
    "ltx2": "Lightricks/LTX-2",
    "ltx23-ti2v-two-stage": "Lightricks/LTX-2.3",
    "wan-i2v": "Wan-AI/Wan2.2-I2V-A14B-Diffusers",
    "ltx23-one-stage": "Lightricks/LTX-2.3",
    "ltx23-two-stage": "Lightricks/LTX-2.3",
    "ltx23-two-stage-cfg-parallel": "Lightricks/LTX-2.3",
    "hunyuanvideo": "hunyuanvideo-community/HunyuanVideo",
    "mova-720p": "OpenMOSS-Team/MOVA-720p",
    "helios": "BestWishYsh/Helios-Base",
    "joyai-edit": "jdopensource/JoyAI-Image-Edit-Diffusers",
    "firered-edit-1.0": "FireRedTeam/FireRed-Image-Edit-1.0",
    "firered-edit-1.1": "FireRedTeam/FireRed-Image-Edit-1.1",
    "hunyuan3d-shape": "tencent/Hunyuan3D-2",
}


def load_successful_pairs(paths: list[Path]) -> set[tuple[str, str]]:
    ok_pairs: set[tuple[str, str]] = set()
    for path in paths:
        if not path.exists():
            continue
        current_arch_by_preset: dict[str, str] = {}
        with path.open(errors="replace") as f:
            for raw in f:
                start_match = SWEEP_START_RE.search(raw)
                if start_match:
                    preset, _host, arch = start_match.groups()
                    current_arch_by_preset[preset] = arch
                    continue
                status_match = SWEEP_STATUS_RE.search(raw)
                if not status_match:
                    continue
                preset, status, new_shape_lines_raw = status_match.groups()
                arch = current_arch_by_preset.get(preset)
                new_shape_lines = int(new_shape_lines_raw)
                if arch and status == "ok" and new_shape_lines > 2:
                    ok_pairs.add((arch, preset))
    return ok_pairs


def load_records(paths: list[Path], ok_pairs: set[tuple[str, str]] | None = None) -> list[dict[str, Any]]:
    records: list[dict[str, Any]] = []
    for path in paths:
        if not path.exists():
            continue
        with path.open() as f:
            for raw in f:
                raw = raw.strip()
                if not raw or not raw.startswith("{"):
                    continue
                try:
                    rec = json.loads(raw)
                except json.JSONDecodeError:
                    continue
                if rec.get("event") or not rec.get("kernel"):
                    continue
                if rec.get("kernel") not in KERNEL_TO_FAMILY:
                    continue
                if ok_pairs is not None:
                    pair = (rec.get("arch"), rec.get("model"))
                    if pair not in ok_pairs:
                        continue
                records.append(rec)
    return records


def norm_for_signature(value: Any) -> Any:
    if isinstance(value, dict):
        if "shape" in value and "dtype" in value:
            return (
                "T",
                tuple(value["shape"]),
                value["dtype"],
                tuple(value.get("strides") or []),
                value.get("contiguous"),
            )
        return tuple(sorted((k, norm_for_signature(v)) for k, v in value.items()))
    if isinstance(value, list):
        return tuple(norm_for_signature(v) for v in value)
    return value


def shape_signature(rec: dict[str, Any]) -> tuple[Any, Any, Any]:
    args = rec.get("args") or []
    kwargs = rec.get("kwargs") or {}
    return (
        rec.get("kernel"),
        norm_for_signature(args),
        tuple(sorted((k, norm_for_signature(v)) for k, v in kwargs.items())),
    )


def dtype_name(dtype: str | None) -> str:
    if not dtype:
        return "unknown"
    return dtype.replace("torch.", "")


def shape_text(value: Any) -> str | None:
    if isinstance(value, dict) and "shape" in value:
        suffix = "C" if value.get("contiguous") else "NC"
        return f"`{value['shape']}/{dtype_name(value.get('dtype'))}{suffix}`"
    return None


def describe(value: Any) -> str:
    shape = shape_text(value)
    if shape is not None:
        return shape
    if isinstance(value, list):
        return "[" + ", ".join(describe(v) for v in value) + "]"
    if isinstance(value, dict):
        return "{" + ", ".join(f"{k}={describe(v)}" for k, v in value.items()) + "}"
    return f"`{value}`"


def tensor_items(rec: dict[str, Any]) -> list[tuple[str, dict[str, Any]]]:
    items: list[tuple[str, dict[str, Any]]] = []
    for idx, arg in enumerate(rec.get("args") or []):
        if isinstance(arg, dict) and "shape" in arg:
            items.append((f"arg{idx}", arg))
    for key, value in (rec.get("kwargs") or {}).items():
        if isinstance(value, dict) and "shape" in value:
            items.append((key, value))
    return items


def scalar_items(rec: dict[str, Any]) -> list[tuple[str, Any]]:
    items: list[tuple[str, Any]] = []
    for idx, arg in enumerate(rec.get("args") or []):
        if not (isinstance(arg, dict) and "shape" in arg):
            items.append((f"arg{idx}", arg))
    for key, value in (rec.get("kwargs") or {}).items():
        if not (isinstance(value, dict) and "shape" in value):
            items.append((key, value))
    return items


def tensor_md(rec: dict[str, Any]) -> str:
    parts = []
    for name, value in tensor_items(rec):
        parts.append(f"{name}={describe(value)}")
    return " ; ".join(parts) or "(none)"


def scalar_md(rec: dict[str, Any]) -> str:
    return " ; ".join(f"{name}={describe(value)}" for name, value in scalar_items(rec)) or "(none)"


def model_name(model: str | None) -> str:
    return MODEL_NAMES.get(model or "", model or "unknown")


def workload_header_for_family(family: str) -> str:
    if family == "diffusion_qknorm_rope__multi_shape":
        return "| Preset | Model | Kernel | dtype | q shape | k shape | weights/cache/positions | flags | Evidence |"
    if family == "diffusion_rms_norm_fn__multi_shape":
        return "| Preset | Model | Kernel | dtype | x shape | weight/bias/residual | flags | Evidence |"
    if family == "diffusion_norm_infer__multi_shape":
        return "| Preset | Model | Kernel | dtype | x shape | weight/bias | flags | Evidence |"
    if family == "diffusion_group_norm_silu__multi_shape":
        return "| Preset | Model | Kernel | dtype | x shape | affine tensors | group/eps | Evidence |"
    if family == "diffusion_rotary_embedding__multi_shape":
        return "| Preset | Model | Kernel | dtype | x shape | cos/sin/cache shapes | flags | Evidence |"
    if family == "diffusion_fuse_scale_shift__multi_shape":
        return "| Preset | Model | Kernel | dtype | x shape | modulation tensors | flags | Evidence |"
    if family == "diffusion_cutedsl_norm_tanh_mul_add__multi_shape":
        return "| Preset | Model | Kernel | dtype | x shape | scale/shift/norm tensors | flags | Evidence |"
    if family == "diffusion_cutedsl_norm_scale_shift__multi_shape":
        return "| Preset | Model | Kernel | dtype | x shape | residual/scale/shift tensors | flags | Evidence |"
    return "| Preset | Model | Kernel | dtype | tensors | flags | Evidence |"


def workload_separator(header: str) -> str:
    columns = header.count("|") - 1
    return "|" + "|".join("---" for _ in range(columns)) + "|"


def primary_dtype(rec: dict[str, Any]) -> str:
    tensors = tensor_items(rec)
    if not tensors:
        return "unknown"
    return dtype_name(tensors[0][1].get("dtype"))


def split_tensors(rec: dict[str, Any], family: str) -> tuple[str, str]:
    tensors = tensor_items(rec)
    by_name = {name: value for name, value in tensors}
    if family == "diffusion_qknorm_rope__multi_shape":
        q = describe(by_name["q"]) if "q" in by_name else (
            describe(tensors[0][1]) if tensors else "(none)"
        )
        k = describe(by_name["k"]) if "k" in by_name else (
            describe(tensors[1][1]) if len(tensors) > 1 else "(none)"
        )
        rest = " ; ".join(
            f"{name}={describe(value)}"
            for name, value in tensors
            if name not in {"q", "k"}
        )
        return q, k, rest or "(none)"
    first = f"{tensors[0][0]}={describe(tensors[0][1])}" if tensors else "(none)"
    rest = " ; ".join(f"{name}={describe(value)}" for name, value in tensors[1:])
    return first, rest or "(none)"


def workload_row(rec: dict[str, Any], family: str) -> str:
    preset = rec.get("model") or "unknown"
    model = model_name(preset)
    kernel = rec.get("kernel") or "unknown"
    dtype = primary_dtype(rec)
    evidence = f"{rec.get('host', 'unknown')} call {rec.get('call_idx', '?')}"
    flags = scalar_md(rec)
    if family == "diffusion_qknorm_rope__multi_shape":
        q, k, rest = split_tensors(rec, family)
        return f"| {preset} | {model} | `{kernel}` | {dtype} | {q} | {k} | {rest} | {flags} | {evidence} |"
    first, rest = split_tensors(rec, family)
    return f"| {preset} | {model} | `{kernel}` | {dtype} | {first} | {rest} | {flags} | {evidence} |"


def prompt_workload_block(family: str, arch: str, recs: list[dict[str, Any]]) -> str:
    header = workload_header_for_family(family)
    lines = [
        "These workload cases are empirical-only. They are the unique kernel call",
        "signatures observed from successful `status=ok` runs while sweeping every",
        "preset listed by the current `bench_diffusion_denoise.py --list-models`",
        "source under the SGLang diffusion benchmark skill. Do not add",
        "model-config-derived or analytical shapes to this table.",
        "",
    ]
    if not recs:
        lines.extend(
            [
                "No live call signatures were captured for this kernel family on this",
                f"{arch.upper()} sweep. Treat the workload shape set as empty until a",
                "future full-preset rerun records entries in the captured JSONL.",
                "",
            ]
        )
    else:
        lines.extend([header, workload_separator(header)])
        for rec in recs:
            lines.append(workload_row(rec, family))
        lines.append("")
    models = sorted({rec.get("model", "unknown") for rec in recs})
    hosts = sorted({rec.get("host", "unknown") for rec in recs})
    lines.extend(
        [
            "Shape collection methodology: all entries above come directly from",
            "`kernel_shape_capture.py` JSONL records collected while running the",
            "full SGLang diffusion benchmark preset list on `ion-b200`, `ion8-h200`,",
            "and/or `ion9-h200`. Each accepted preset had `status=ok`, a valid",
            "denoise/refinement perf dump, and more than install-only capture lines.",
            "Each preset run used `--backend=sglang` through the benchmark helper and",
            "model weights were deleted from the Hugging Face cache immediately after",
            "that preset completed.",
            "",
            f"- Captured presets for this task/arch: `{models}`",
            f"- Capture hosts for this task/arch: `{hosts}`",
            f"- Raw evidence: `docs/captured_shapes_{arch}.jsonl`",
            f"- Summary: `docs/captured_shapes_{arch}.md`",
            "",
            "Humanize/RLCR instruction: do not determine, derive, broaden, or",
            "reinterpret optimization shapes during plan generation. The workload",
            "shape set is exactly the rows in this prompt and the matching",
            f"`docs/captured_shapes_{arch}.jsonl`; use those shapes verbatim.",
        ]
    )
    return "\n".join(lines)


def replace_workload_section(prompt_path: Path, family: str, arch: str, recs: list[dict[str, Any]]) -> None:
    text = prompt_path.read_text()
    start_marker = "## Workload Cases (Production Shapes)"
    end_marker = "## Canonical Regression Shapes"
    start = text.index(start_marker) + len(start_marker)
    end = text.index(end_marker)
    block = "\n\n" + prompt_workload_block(family, arch, recs) + "\n\n"
    prompt_path.write_text(text[:start] + block + text[end:])


def write_task_docs(task_slug: str, arch: str, recs: list[dict[str, Any]]) -> None:
    folder = KERNELS_DIR / task_slug
    if not folder.exists():
        return
    docs = folder / "docs"
    docs.mkdir(parents=True, exist_ok=True)
    raw_path = docs / f"captured_shapes_{arch}.jsonl"
    with raw_path.open("w") as f:
        for rec in recs:
            f.write(json.dumps(rec, sort_keys=True) + "\n")

    md_path = docs / f"captured_shapes_{arch}.md"
    with md_path.open("w") as md:
        md.write(f"# Captured shapes for `{task_slug}`\n\n")
        md.write("Every row below is a live SGLang diffusion benchmark capture. ")
        md.write("No analytical fallback shapes are included.\n\n")
        if not recs:
            md.write("No live call signatures were captured for this kernel family.\n")
            return
        md.write("| Preset | Kernel | Tensor shapes | Other args | Evidence |\n")
        md.write("|---|---|---|---|---|\n")
        for rec in recs:
            md.write(
                f"| {rec.get('model')} | `{rec.get('kernel')}` | {tensor_md(rec)} | "
                f"{scalar_md(rec)} | {rec.get('host')} call {rec.get('call_idx')} |\n"
            )
        md.write("\nLegend: `<shape>/<dtype>/C|NC` where `C`=contiguous, `NC`=non-contiguous.\n")


def write_top_ledger(grouped: dict[str, dict[str, list[dict[str, Any]]]]) -> None:
    top = KERNELS_DIR / "diffusion_shapes_ledger.md"
    with top.open("w") as f:
        f.write("# Diffusion Shape Ledger (live SGLang benchmark captures)\n\n")
        f.write(
            "This ledger contains only shapes captured from real SGLang diffusion "
            "benchmark preset runs. Derived/model-config-only shapes are excluded.\n\n"
        )
        for family in FAMILIES:
            f.write(f"## `{family}`\n\n")
            for arch in ARCHS:
                recs = grouped[family][arch]
                f.write(f"### `{arch}`\n\n")
                if not recs:
                    f.write("No live call signatures captured.\n\n")
                    continue
                f.write("| Preset | Kernel | Tensor shapes | Other args | Evidence |\n")
                f.write("|---|---|---|---|---|\n")
                for rec in recs:
                    f.write(
                        f"| {rec.get('model')} | `{rec.get('kernel')}` | {tensor_md(rec)} | "
                        f"{scalar_md(rec)} | {rec.get('host')} call {rec.get('call_idx')} |\n"
                    )
                f.write("\n")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--input",
        action="append",
        type=Path,
        default=None,
        help="Capture JSONL input. May be repeated. Defaults to /tmp/shapes_*.jsonl.",
    )
    parser.add_argument(
        "--sweep-log",
        action="append",
        type=Path,
        default=None,
        help="Sweep log used to keep only records from presets with status=ok.",
    )
    args = parser.parse_args()

    inputs = args.input or DEFAULT_CAPTURE_FILES
    ok_pairs = load_successful_pairs(args.sweep_log or []) if args.sweep_log else None
    records = load_records(inputs, ok_pairs=ok_pairs)
    print(f"Loaded {len(records)} capture records from {[str(p) for p in inputs]}")
    if ok_pairs is not None:
        print(f"Kept records from {len(ok_pairs)} successful arch/preset pairs")

    grouped: dict[str, dict[str, list[dict[str, Any]]]] = {
        family: {arch: [] for arch in ARCHS} for family in FAMILIES
    }
    seen: dict[str, dict[str, set[tuple[Any, Any, Any]]]] = {
        family: {arch: set() for arch in ARCHS} for family in FAMILIES
    }
    for rec in records:
        family = KERNEL_TO_FAMILY[rec["kernel"]]
        arch = rec.get("arch")
        if arch not in ARCHS:
            continue
        sig = shape_signature(rec)
        if sig in seen[family][arch]:
            continue
        seen[family][arch].add(sig)
        grouped[family][arch].append(rec)

    for family in FAMILIES:
        for arch in ARCHS:
            recs = sorted(
                grouped[family][arch],
                key=lambda r: (str(r.get("model")), str(r.get("kernel")), int(r.get("call_idx") or 0)),
            )
            grouped[family][arch] = recs
            task_slug = f"{arch}_{family}"
            write_task_docs(task_slug, arch, recs)
            prompt_path = KERNELS_DIR / task_slug / "prompt.md"
            if prompt_path.exists():
                replace_workload_section(prompt_path, family, arch, recs)
            print(f"{task_slug}: {len(recs)} unique live signatures")

    write_top_ledger(grouped)
    print(f"Wrote {KERNELS_DIR / 'diffusion_shapes_ledger.md'}")


if __name__ == "__main__":
    main()
