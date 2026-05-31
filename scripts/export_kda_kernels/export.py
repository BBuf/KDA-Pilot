#!/usr/bin/env python3
"""Promote a KDA kernel task into kda_kernels/.

Usage:
  scripts/export_kda_kernels/export.py <task-slug>
  scripts/export_kda_kernels/export.py --list
  scripts/export_kda_kernels/export.py --revert <task-slug>

`<task-slug>` is the folder name under `kernels/`, for example
`b200_diffusion_qknorm_rope__multi_shape`. Both b200 and h200 slugs of the
same family are accepted; the family they share is what gets wired into
kda_kernels, so promoting either is enough (and promoting both is a no-op
the second time).

What the export does:

1. Copies `kernels/<task-slug>/src/*` into
   `kda_kernels/_impls/<task-slug>/`. CUDA sources (`.cu`, `.cuh`, `.cpp`,
   `.h`), Python wrappers, and any extra helpers ride along.
2. Reads the task's `src/register.py` for its `EXPORTS` dict. Each
   `(function_name, callable)` pair is a promised swap target.
3. Rewrites the matching kda_kernels stub file at the kernel-family
   target (e.g. `kda_kernels/diffusion/qknorm_rope.py`) so that each
   promoted function imports from the new impl subpackage and the
   corresponding `KDA_OPTIMIZED_<fn>` flag flips to True.
4. Stamps `KDA_TASK_<fn>`, `KDA_COMMIT_<fn>`, `KDA_DATE_<fn>`, and (when
   present in the task's `benchmark.csv` last row) `KDA_SPEEDUP_<fn>`.

Re-running export.py for the same task overwrites the impl copy with the
current task src/. Use `--revert <task-slug>` to undo (the stub falls back
to re-exporting the sglang baseline with `KDA_OPTIMIZED_<fn> = False`).
"""

from __future__ import annotations

import argparse
import csv
import datetime as _dt
import importlib.util
import shutil
import subprocess
import sys
from collections import defaultdict
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
KDA = REPO / "kda_kernels"
IMPLS = KDA / "_impls"
KERNELS = REPO / "kernels"

# Owning task family -> list of (sglang_module, sglang_function,
# kda_module, kda_function).
FAMILY_TO_SWAPS: dict[str, list[tuple[str, str, str, str]]] = {
    "qknorm_rope": [
        ("sglang.jit_kernel.diffusion.qknorm_rope", "fused_inplace_qknorm_rope",
         "kda_kernels.diffusion.qknorm_rope", "fused_inplace_qknorm_rope"),
    ],
    "norm_infer": [
        ("sglang.jit_kernel.diffusion.triton.norm", "norm_infer",
         "kda_kernels.diffusion.norm_infer", "norm_infer"),
        ("sglang.jit_kernel.diffusion.triton.rmsnorm_onepass", "triton_one_pass_rms_norm",
         "kda_kernels.diffusion.norm_infer", "triton_one_pass_rms_norm"),
    ],
    "group_norm_silu": [
        ("sglang.jit_kernel.diffusion.triton.group_norm_silu", "triton_group_norm_silu",
         "kda_kernels.diffusion.group_norm_silu", "triton_group_norm_silu"),
        ("sglang.jit_kernel.diffusion.group_norm_silu", "apply_group_norm_silu",
         "kda_kernels.diffusion.group_norm_silu", "apply_group_norm_silu"),
    ],
    "rotary_embedding": [
        ("sglang.jit_kernel.diffusion.triton.rotary", "apply_rotary_embedding",
         "kda_kernels.diffusion.rotary_embedding", "apply_rotary_embedding"),
        ("sglang.jit_kernel.diffusion.triton.ltx2_rotary", "apply_ltx2_split_rotary_emb",
         "kda_kernels.diffusion.rotary_embedding", "apply_ltx2_split_rotary_emb"),
    ],
    "fuse_scale_shift": [
        ("sglang.jit_kernel.diffusion.triton.scale_shift", "fuse_scale_shift_kernel",
         "kda_kernels.diffusion.fuse_scale_shift", "fuse_scale_shift_kernel"),
        ("sglang.jit_kernel.diffusion.triton.scale_shift", "fuse_layernorm_scale_shift_gate_select01_kernel",
         "kda_kernels.diffusion.fuse_scale_shift", "fuse_layernorm_scale_shift_gate_select01_kernel"),
        ("sglang.jit_kernel.diffusion.triton.scale_shift", "fuse_residual_layernorm_scale_shift_gate_select01_kernel",
         "kda_kernels.diffusion.fuse_scale_shift", "fuse_residual_layernorm_scale_shift_gate_select01_kernel"),
    ],
    "cutedsl_norm_tanh_mul_add": [
        ("sglang.jit_kernel.diffusion.cutedsl.norm_tanh_mul_add_norm_scale", "fused_norm_tanh_mul_add",
         "kda_kernels.diffusion.cutedsl_norm_tanh_mul_add", "fused_norm_tanh_mul_add"),
        ("sglang.jit_kernel.diffusion.cutedsl.norm_tanh_mul_add_norm_scale", "fused_norm_tanh_mul_add_norm_scale",
         "kda_kernels.diffusion.cutedsl_norm_tanh_mul_add", "fused_norm_tanh_mul_add_norm_scale"),
    ],
    "cutedsl_norm_scale_shift": [
        ("sglang.jit_kernel.diffusion.cutedsl.scale_residual_norm_scale_shift", "fused_norm_scale_shift",
         "kda_kernels.diffusion.cutedsl_norm_scale_shift", "fused_norm_scale_shift"),
        ("sglang.jit_kernel.diffusion.cutedsl.scale_residual_norm_scale_shift", "fused_scale_residual_norm_scale_shift",
         "kda_kernels.diffusion.cutedsl_norm_scale_shift", "fused_scale_residual_norm_scale_shift"),
    ],
}


def family_of(task_slug: str) -> str:
    if "_diffusion_" not in task_slug or "__multi_shape" not in task_slug:
        raise SystemExit(
            f"task slug {task_slug!r} is not a diffusion multi-shape task"
        )
    family = task_slug.split("_diffusion_", 1)[1].split("__multi_shape", 1)[0]
    if family not in FAMILY_TO_SWAPS:
        raise SystemExit(f"unknown family {family!r} (slug={task_slug!r})")
    return family


def last_speedup(task_dir: Path) -> str:
    csv_path = task_dir / "benchmark.csv"
    if not csv_path.exists():
        return ""
    try:
        with csv_path.open() as f:
            rows = list(csv.reader(f))
        for row in reversed(rows):
            for cell in row:
                if cell.endswith("x") and any(c.isdigit() for c in cell):
                    return cell
    except Exception:  # noqa: BLE001
        pass
    return ""


def read_exports(src_dir: Path) -> set[str]:
    """Return the set of function names listed in src/register.py's EXPORTS dict."""
    register_py = src_dir / "register.py"
    if not register_py.exists():
        return set()
    ns: dict[str, object] = {}
    try:
        code = register_py.read_text()
        exec(compile(code, str(register_py), "exec"), ns)  # noqa: S102
    except Exception as exc:  # noqa: BLE001
        print(
            f"warning: failed to read EXPORTS from {register_py}: {exc!r}",
            file=sys.stderr,
        )
        return set()
    exports = ns.get("EXPORTS")
    if isinstance(exports, dict):
        return {str(k) for k in exports}
    return set()


def copy_src_to_impls_legacy(task_dir: Path, task_slug: str) -> Path:
    """Deprecated path that used to copy into kda_kernels/_impls/<slug>/.
    Kept as a no-op shim so any external caller doesn't crash; the new
    `copy_src(task_dir, family)` writes straight into the family package.
    """
    return KDA / "_impls" / task_slug


def regenerate_stub(family: str, task_slug: str, exports: set[str]) -> list[Path]:
    """Write the kda_kernels family package __init__.py for `family`.

    Functions in `exports` get an import line from the promoted impl
    (`kda_kernels.diffusion.<family>.wrapper`) and `KDA_OPTIMIZED_<fn> = True`.
    Others fall back to re-exporting the sglang baseline with
    `KDA_OPTIMIZED_<fn> = False`.

    The promoted impl directory `kda_kernels/diffusion/<family>/` receives a
    copy of every file from `kernels/<task-slug>/src/` (CUDA `.cu`, `.cuh`,
    `.cpp`, `.h`, the Python wrapper, build glue, etc.) so the family
    package is self-contained at runtime.
    """
    written: list[Path] = []
    # All entries of a family share one kda_module (the family package).
    kda_mod = FAMILY_TO_SWAPS[family][0][2]
    sgl_entries = [(sgl_mod, kda_fn) for sgl_mod, _sgl_fn, _km, kda_fn in FAMILY_TO_SWAPS[family]]

    commit = "unknown"
    try:
        commit = subprocess.check_output(
            ["git", "rev-parse", "HEAD"], cwd=REPO, text=True
        ).strip()
    except subprocess.CalledProcessError:
        pass
    date = _dt.date.today().isoformat()
    speedup = last_speedup(KERNELS / task_slug)

    rel = kda_mod.replace(".", "/") + "/__init__.py"
    path = REPO / rel
    family_dir = path.parent
    family_dir.mkdir(parents=True, exist_ok=True)

    lines: list[str] = [
        f'"""kda_kernels.diffusion.{family} — CUDA-only KDA-optimized overlay.\n\n',
        'This package contributes the following swap functions:\n\n',
    ]
    lines.extend(f"  - `{sgl_mod}:{fn}`\n" for sgl_mod, fn in sgl_entries)
    lines.extend([
        '\n',
        'Stub status: each function is either re-exported from SGLang\n',
        '(`KDA_OPTIMIZED_<fn> = False`) or pulled from a promoted KDA impl\n',
        '(`KDA_OPTIMIZED_<fn> = True`). Promotion is driven by\n',
        '`scripts/export_kda_kernels/export.py <task-slug>`.\n',
        '"""\n\n',
    ])

    imports: list[str] = []
    flags: list[str] = []
    stamps: list[str] = []
    for sgl_mod, kda_fn in sgl_entries:
        if kda_fn in exports:
            imports.append(
                f"from kda_kernels.diffusion.{family}.wrapper import "
                f"{kda_fn}  # noqa: F401\n"
            )
            flags.append(f"KDA_OPTIMIZED_{kda_fn} = True\n")
            stamps.append(
                f"KDA_TASK_{kda_fn} = {task_slug!r}\n"
                f"KDA_COMMIT_{kda_fn} = {commit!r}\n"
                f"KDA_DATE_{kda_fn} = {date!r}\n"
                f"KDA_SPEEDUP_{kda_fn} = {speedup!r}\n"
            )
        else:
            imports.append(f"from {sgl_mod} import {kda_fn}  # noqa: F401\n")
            flags.append(f"KDA_OPTIMIZED_{kda_fn} = False\n")
    body = "".join(lines + imports + ["\n"] + flags + (["\n"] + stamps if stamps else []))
    path.write_text(body, encoding="utf-8")
    written.append(path)
    return written


def copy_src(task_dir: Path, family: str) -> Path:
    """Copy task `src/` into `kda_kernels/diffusion/<family>/`.

    The whole task src/ tree (CUDA sources, wrapper.py, headers, build
    glue) lands directly inside the family package so the runtime
    `from kda_kernels.diffusion.<family>.wrapper import <fn>` line
    resolves without an extra hop. Existing files in the family
    directory other than the auto-generated __init__.py and KDA_STATUS.md
    are wiped first to keep promotions deterministic.
    """
    family_dir = KDA / "diffusion" / family
    family_dir.mkdir(parents=True, exist_ok=True)
    # Wipe everything except __init__.py (will be rewritten) and KDA_STATUS.md.
    for entry in family_dir.iterdir():
        if entry.name in ("__init__.py", "KDA_STATUS.md"):
            continue
        if entry.is_dir():
            shutil.rmtree(entry)
        else:
            entry.unlink()
    src_dir = task_dir / "src"
    for entry in src_dir.iterdir():
        target = family_dir / entry.name
        if entry.is_dir():
            shutil.copytree(entry, target)
        else:
            shutil.copy2(entry, target)
    return family_dir


def family_promoted(family: str) -> bool:
    """True when the family package's __init__.py has any
    `KDA_OPTIMIZED_<fn> = True` flag."""
    init = KDA / "diffusion" / family / "__init__.py"
    if not init.exists():
        return False
    return " = True" in init.read_text(encoding="utf-8")


def cmd_list() -> int:
    for slug in sorted(
        p.name for p in KERNELS.iterdir() if p.is_dir() and "_diffusion_" in p.name
    ):
        family = family_of(slug) if "_diffusion_" in slug and "__multi_shape" in slug else ""
        marker = " [exported]" if family and family_promoted(family) else ""
        print(f"  {slug}{marker}")
    return 0


def cmd_revert(task_slug: str) -> int:
    family = family_of(task_slug)
    family_dir = KDA / "diffusion" / family
    if family_dir.exists():
        for entry in family_dir.iterdir():
            if entry.name in ("__init__.py", "KDA_STATUS.md"):
                continue
            if entry.is_dir():
                shutil.rmtree(entry)
            else:
                entry.unlink()
        print(f"wiped CUDA sources under kda_kernels/diffusion/{family}/")
    regenerate_stub(family, task_slug, exports=set())
    print(f"reset kda_kernels stubs for family={family}")
    return 0


def write_status_md(family_dir: Path, task_slug: str, exports: set[str]) -> None:
    commit = "unknown"
    try:
        commit = subprocess.check_output(
            ["git", "rev-parse", "HEAD"], cwd=REPO, text=True
        ).strip()
    except subprocess.CalledProcessError:
        pass
    date = _dt.date.today().isoformat()
    speedup = last_speedup(KERNELS / task_slug)
    lines = [
        f"# kda_kernels promotion status — {family_dir.name}\n",
        "\n",
        f"| Field | Value |\n",
        f"|---|---|\n",
        f"| Task slug | `{task_slug}` |\n",
        f"| Commit (kernel-pilot) | `{commit}` |\n",
        f"| Promotion date | {date} |\n",
        f"| Reported geomean speedup | {speedup or '_(unset)_'} |\n",
        f"| Promoted functions | {', '.join(sorted(exports)) or '_(none)_'} |\n",
        "\n",
        "## Files\n",
        "\n",
    ]
    for entry in sorted(family_dir.iterdir()):
        if entry.name in ("__init__.py", "KDA_STATUS.md", "__pycache__"):
            continue
        lines.append(f"- `{entry.name}`\n")
    (family_dir / "KDA_STATUS.md").write_text("".join(lines), encoding="utf-8")


def cmd_export(task_slug: str) -> int:
    task_dir = KERNELS / task_slug
    if not task_dir.exists():
        raise SystemExit(f"no such task: {task_dir}")
    family = family_of(task_slug)
    src_dir = task_dir / "src"
    if not src_dir.exists():
        raise SystemExit(f"task {task_slug} has no src/")
    print(f"== exporting task={task_slug} family={family} ==")
    family_dir = copy_src(task_dir, family)
    exports = read_exports(src_dir)
    if not exports:
        print(
            "warning: src/register.py has no EXPORTS dict; "
            "stubs will fall back to sglang baseline",
            file=sys.stderr,
        )
    written = regenerate_stub(family, task_slug, exports)
    write_status_md(family_dir, task_slug, exports)
    for p in written:
        print(f"  updated {p.relative_to(REPO)}")
    print(f"  copied src/ -> {family_dir.relative_to(REPO)}/")
    print(f"  wrote {family_dir.relative_to(REPO)}/KDA_STATUS.md")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("task_slug", nargs="?", help="kernels/<slug> to promote")
    g.add_argument("--list", action="store_true")
    g.add_argument("--revert", metavar="TASK_SLUG", help="undo a promotion")
    args = ap.parse_args()
    if args.list:
        return cmd_list()
    if args.revert:
        return cmd_revert(args.revert)
    return cmd_export(args.task_slug)


if __name__ == "__main__":
    raise SystemExit(main())
