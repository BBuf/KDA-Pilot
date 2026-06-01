#!/usr/bin/env python3
"""Promote a KDA kernel task into kda_kernels/.

Usage:
  scripts/export_kda_kernels/export.py <task-slug>
  scripts/export_kda_kernels/export.py --list
  scripts/export_kda_kernels/export.py --revert <task-slug>

`<task-slug>` is the folder name under `kernels/`, for example
`b200_diffusion_qknorm_rope__multi_shape`. Both b200 and h200 slugs of the
same family are accepted. Exporting both keeps both implementations under the
same kda_kernels family package and the generated dispatcher chooses the right
one at runtime from the CUDA device capability.

What the export does:

1. Copies `kernels/<task-slug>/src/*` into
   `kda_kernels/diffusion/<family>/_impls/<arch>/`. CUDA sources (`.cu`,
   `.cuh`, `.cpp`, `.h`), Python wrappers, and any extra helpers ride along.
2. Reads the task's `src/register.py` for its `EXPORTS` dict. Each
   `(function_name, callable)` pair is a promised swap target.
3. Rewrites the matching kda_kernels family package
   (e.g. `kda_kernels/diffusion/qknorm_rope/`) so that each promoted function
   imports from an architecture-aware dispatcher and the corresponding
   `KDA_OPTIMIZED_<fn>` flag flips to True.
4. Stamps `KDA_TASK_<fn>`, `KDA_COMMIT_<fn>`, `KDA_DATE_<fn>`, and (when
   present in the task's `benchmark.csv` last row) `KDA_SPEEDUP_<fn>`.

Re-running export.py for the same task overwrites that arch's impl copy with
the current task src/. Use `--revert <task-slug>` to undo one arch export; if no
arch remains for a function, the stub falls back to re-exporting the sglang
baseline with `KDA_OPTIMIZED_<fn> = False`.
"""

from __future__ import annotations

import argparse
import csv
import datetime as _dt
import json
import re
import shutil
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
KDA = REPO / "kda_kernels"
KERNELS = REPO / "kernels"
META_FILENAME = "KDA_EXPORTS.json"
ARCH_CAPABILITIES: dict[str, tuple[int, int]] = {
    "b200": (10, 0),  # Blackwell / SM100
    "h200": (9, 0),   # Hopper / SM90
}
ARCH_ORDER = {arch: i for i, arch in enumerate(ARCH_CAPABILITIES)}
FAMILY_TOP_LEVEL_KEEP = {
    "__init__.py",
    "_dispatcher.py",
    "_impls",
    "__pycache__",
}

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


def arch_of(task_slug: str) -> str:
    if "_diffusion_" not in task_slug or "__multi_shape" not in task_slug:
        raise SystemExit(
            f"task slug {task_slug!r} is not a diffusion multi-shape task"
        )
    arch = task_slug.split("_diffusion_", 1)[0]
    if arch not in ARCH_CAPABILITIES:
        known = ", ".join(sorted(ARCH_CAPABILITIES))
        raise SystemExit(f"unknown arch {arch!r} in slug={task_slug!r}; known: {known}")
    return arch


def arch_sort_key(arch: str) -> tuple[int, str]:
    return (ARCH_ORDER.get(arch, 999), arch)


def last_speedup(task_dir: Path) -> str:
    csv_path = task_dir / "benchmark.csv"
    if not csv_path.exists():
        return ""
    def normalize(value: str) -> str:
        value = value.strip()
        if not value:
            return ""
        if value.endswith("x"):
            return value
        try:
            float(value)
        except ValueError:
            return value
        return f"{value}x"

    try:
        with csv_path.open() as f:
            rows = list(csv.DictReader(f))
        for row in reversed(rows):
            label = " ".join(
                str(row.get(key, ""))
                for key in ("case", "shape", "kind", "metric", "bucket")
            ).lower()
            if "geomean" not in label:
                continue
            for key in ("speedup_vs_baseline", "speedup_x", "speedup"):
                value = normalize(str(row.get(key, "")))
                if value:
                    return value
        with csv_path.open() as f:
            raw_rows = list(csv.reader(f))
        for row in reversed(raw_rows):
            for cell in row:
                if cell.endswith("x") and any(c.isdigit() for c in cell):
                    return cell
    except Exception:  # noqa: BLE001
        pass
    return ""


def resolve_commit(commit: str) -> str:
    commit = commit.strip()
    if not commit:
        return ""
    try:
        return subprocess.check_output(
            ["git", "rev-parse", f"{commit}^{{commit}}"],
            cwd=REPO,
            text=True,
        ).strip()
    except subprocess.CalledProcessError:
        return commit


def task_source_commit(task_dir: Path) -> str:
    csv_path = task_dir / "benchmark.csv"
    if not csv_path.exists():
        return ""
    try:
        with csv_path.open() as f:
            rows = list(csv.DictReader(f))
        for row in reversed(rows):
            for key in ("kp_commit", "candidate_commit", "commit"):
                commit = resolve_commit(str(row.get(key, "")))
                if commit:
                    return commit
            for value in row.values():
                match = re.search(r"\bkp_commit=([0-9a-fA-F]{7,40})\b", str(value))
                if match:
                    return resolve_commit(match.group(1))
    except Exception:  # noqa: BLE001
        return ""
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


def family_dir(family: str) -> Path:
    return KDA / "diffusion" / family


def impl_root(family: str) -> Path:
    return family_dir(family) / "_impls"


def impl_dir(family: str, arch: str) -> Path:
    return impl_root(family) / arch


def meta_path(family: str, arch: str) -> Path:
    return impl_dir(family, arch) / META_FILENAME


def load_family_metadata(family: str) -> dict[str, dict[str, object]]:
    root = impl_root(family)
    if not root.exists():
        return {}
    metas: dict[str, dict[str, object]] = {}
    valid_fns = {kda_fn for *_prefix, kda_fn in FAMILY_TO_SWAPS[family]}
    for path in sorted(root.glob(f"*/{META_FILENAME}")):
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except Exception as exc:  # noqa: BLE001
            print(f"warning: failed to read {path}: {exc!r}", file=sys.stderr)
            continue
        arch = str(data.get("arch") or path.parent.name)
        if arch not in ARCH_CAPABILITIES:
            print(f"warning: ignoring unknown arch metadata {path}", file=sys.stderr)
            continue
        if str(data.get("family") or family) != family:
            print(f"warning: ignoring metadata for a different family: {path}", file=sys.stderr)
            continue
        exports = sorted(str(fn) for fn in data.get("exports", []) if str(fn) in valid_fns)
        if not exports:
            continue
        data["arch"] = arch
        data["family"] = family
        data["exports"] = exports
        metas[arch] = data
    return dict(sorted(metas.items(), key=lambda item: arch_sort_key(item[0])))


def exported_arches_by_fn(family: str, metas: dict[str, dict[str, object]]) -> dict[str, list[str]]:
    by_fn: dict[str, list[str]] = {
        kda_fn: [] for *_prefix, kda_fn in FAMILY_TO_SWAPS[family]
    }
    for arch, data in metas.items():
        for fn in data.get("exports", []):
            by_fn[str(fn)].append(arch)
    return {
        fn: sorted(arches, key=arch_sort_key)
        for fn, arches in by_fn.items()
        if arches
    }


def metadata_value(fn_arches: list[str], metas: dict[str, dict[str, object]], key: str) -> object:
    values = {arch: metas[arch].get(key, "") for arch in fn_arches}
    if len(values) == 1:
        return next(iter(values.values()))
    return values


def write_dispatcher(
    family: str,
    by_fn: dict[str, list[str]],
    metas: dict[str, dict[str, object]],
) -> Path:
    """Write the architecture dispatcher for a family with promoted impls."""
    path = family_dir(family) / "_dispatcher.py"
    entries = FAMILY_TO_SWAPS[family]
    impl_modules = {
        fn: {
            arch: f"kda_kernels.diffusion.{family}._impls.{arch}.wrapper"
            for arch in arches
        }
        for fn, arches in by_fn.items()
    }
    supported_arches = sorted(
        {arch for arches in by_fn.values() for arch in arches},
        key=arch_sort_key,
    )

    lines: list[str] = [
        f'"""Runtime architecture dispatcher for kda_kernels.diffusion.{family}.\n\n',
        'Auto-generated by scripts/export_kda_kernels/export.py. The SGLang\n',
        'baseline functions and promoted arch-specific wrappers are imported\n',
        'before kda_kernels.install() swaps SGLang symbols, keeping fallback\n',
        'paths non-recursive.\n',
        '"""\n\n',
        "from __future__ import annotations\n\n",
        "import importlib\n",
        "import os\n",
        "import sys\n",
        "import warnings\n",
        "from pathlib import Path\n",
        "from typing import Any\n\n",
        "try:\n",
        "    import torch\n",
        "except Exception:  # pragma: no cover - torch is always present in runtime envs\n",
        "    torch = None\n\n",
    ]
    for sgl_mod, sgl_fn, _kda_mod, kda_fn in entries:
        lines.extend([
            "try:\n",
            f"    from {sgl_mod} import {sgl_fn} as _BASELINE_{kda_fn}\n",
            "except Exception:  # pragma: no cover - local export/verify may not have sglang\n",
            f"    _BASELINE_{kda_fn} = None\n",
        ])
    lines.extend([
        "\n",
        f"_ARCH_BY_CAPABILITY = { {cap: arch for arch, cap in ARCH_CAPABILITIES.items()}!r}\n",
        f"_SUPPORTED_ARCHES = {tuple(supported_arches)!r}\n",
        f"_IMPL_MODULES = {impl_modules!r}\n",
        "_IMPL_CACHE: dict[tuple[str, str], Any] = {}\n",
        "_IMPL_IMPORT_ERRORS: dict[tuple[str, str], BaseException] = {}\n",
        "_WARNED_IMPORT_ERRORS: set[tuple[str, str]] = set()\n",
        "# Resolved-target cache: (fn_name, device_index) -> bound wrapper callable\n",
        "# (or the _USE_BASELINE sentinel). Filled on the first call per key so the\n",
        "# steady-state hot path skips capability probing, module import, and attribute\n",
        "# lookup -- the per-call dispatch tax that otherwise erases small-shape wins.\n",
        "_USE_BASELINE = object()\n",
        "_TARGET_CACHE: dict[tuple[str, Any], Any] = {}\n",
        "# KDA_FORCE_ARCH is a deploy/debug override, read once at import (not per call).\n",
        "_FORCED_ARCH = os.environ.get('KDA_FORCE_ARCH')\n",
        "if _FORCED_ARCH not in _SUPPORTED_ARCHES:\n",
        "    _FORCED_ARCH = None\n\n",
        "def _impl_dir(arch: str) -> Path:\n",
        "    return Path(__file__).resolve().parent / '_impls' / arch\n\n",
        "def _load_impl(arch: str, module_name: str) -> Any:\n",
        "    key = (arch, module_name)\n",
        "    if key in _IMPL_CACHE:\n",
        "        return _IMPL_CACHE[key]\n",
        "    path = str(_impl_dir(arch))\n",
        "    if path not in sys.path:\n",
        "        sys.path.insert(0, path)\n",
        "    module = importlib.import_module(module_name)\n",
        "    _IMPL_CACHE[key] = module\n",
        "    return module\n\n",
        "def _preload_kda_impls(strict: bool = False) -> None:\n",
        "    \"\"\"Import promoted wrappers before monkey-patching SGLang.\"\"\"\n",
        "    for by_arch in _IMPL_MODULES.values():\n",
        "        for arch, module_name in by_arch.items():\n",
        "            key = (arch, module_name)\n",
        "            if key in _IMPL_CACHE or key in _IMPL_IMPORT_ERRORS:\n",
        "                continue\n",
        "            try:\n",
        "                _load_impl(arch, module_name)\n",
        "            except Exception as exc:  # noqa: BLE001\n",
        "                _IMPL_IMPORT_ERRORS[key] = exc\n",
        "                if strict:\n",
        "                    raise\n",
        "                warnings.warn(\n",
        "                    f'kda_kernels failed to preload {module_name} for {arch}: {exc!r}'\n",
        "                )\n\n",
        "def _iter_tensors(value: Any):\n",
        "    if torch is not None and isinstance(value, torch.Tensor):\n",
        "        yield value\n",
        "    elif isinstance(value, (tuple, list)):\n",
        "        for item in value:\n",
        "            yield from _iter_tensors(item)\n",
        "    elif isinstance(value, dict):\n",
        "        for item in value.values():\n",
        "            yield from _iter_tensors(item)\n\n",
        "def _first_cuda_index(args: tuple[Any, ...], kwargs: dict[str, Any]):\n",
        "    \"\"\"Device index of the first CUDA tensor in the call (positional args fast\n",
        "    path, then nested containers, then kwargs), else None.\"\"\"\n",
        "    for value in args:\n",
        "        if type(value) is torch.Tensor:\n",
        "            if value.is_cuda:\n",
        "                return value.device.index\n",
        "        elif isinstance(value, (tuple, list, dict)):\n",
        "            for tensor in _iter_tensors(value):\n",
        "                if getattr(tensor, 'is_cuda', False):\n",
        "                    return tensor.device.index\n",
        "    for value in kwargs.values():\n",
        "        if type(value) is torch.Tensor:\n",
        "            if value.is_cuda:\n",
        "                return value.device.index\n",
        "        elif isinstance(value, (tuple, list, dict)):\n",
        "            for tensor in _iter_tensors(value):\n",
        "                if getattr(tensor, 'is_cuda', False):\n",
        "                    return tensor.device.index\n",
        "    return None\n\n",
        "def _resolve_target(fn_name: str, idx) -> Any:\n",
        "    \"\"\"Resolve (fn_name, device idx) -> bound wrapper callable, or _USE_BASELINE.\n\n",
        "    Runs the full arch-selection / import path once per cache key; the result is\n",
        "    memoized by the caller so steady-state calls skip all of this work.\n",
        "    \"\"\"\n",
        "    if _FORCED_ARCH is not None:\n",
        "        arch = _FORCED_ARCH\n",
        "    elif torch is None or idx is None:\n",
        "        arch = None\n",
        "    else:\n",
        "        try:\n",
        "            arch = _ARCH_BY_CAPABILITY.get(tuple(torch.cuda.get_device_capability(idx)))\n",
        "        except Exception:\n",
        "            arch = None\n",
        "    module_name = _IMPL_MODULES.get(fn_name, {}).get(arch)\n",
        "    if module_name is None:\n",
        "        return _USE_BASELINE\n",
        "    key = (arch, module_name)\n",
        "    if key in _IMPL_IMPORT_ERRORS:\n",
        "        if key not in _WARNED_IMPORT_ERRORS:\n",
        "            _WARNED_IMPORT_ERRORS.add(key)\n",
        "            warnings.warn(\n",
        "                f'kda_kernels falling back for {fn_name}: {module_name} '\n",
        "                f'failed to preload for {arch}: {_IMPL_IMPORT_ERRORS[key]!r}'\n",
        "            )\n",
        "        return _USE_BASELINE\n",
        "    module = _IMPL_CACHE.get(key)\n",
        "    if module is None:\n",
        "        # Direct kda_kernels use without install(); safe because SGLang has not\n",
        "        # been monkey-patched yet in that usage pattern.\n",
        "        try:\n",
        "            module = _load_impl(arch, module_name)\n",
        "        except Exception as exc:  # noqa: BLE001\n",
        "            _IMPL_IMPORT_ERRORS[key] = exc\n",
        "            warnings.warn(f'kda_kernels falling back for {fn_name}: {exc!r}')\n",
        "            return _USE_BASELINE\n",
        "    return getattr(module, fn_name)\n\n",
    ])
    for _sgl_mod, _sgl_fn, _kda_mod, kda_fn in entries:
        if kda_fn not in by_fn:
            continue
        lines.extend([
            f"def {kda_fn}(*args: Any, **kwargs: Any) -> Any:\n",
            "    idx = _first_cuda_index(args, kwargs)\n",
            f"    ckey = ({kda_fn!r}, idx)\n",
            "    target = _TARGET_CACHE.get(ckey)\n",
            "    if target is None:\n",
            f"        target = _resolve_target({kda_fn!r}, idx)\n",
            "        _TARGET_CACHE[ckey] = target\n",
            "    if target is _USE_BASELINE:\n",
            f"        if _BASELINE_{kda_fn} is None:\n",
            f"            raise RuntimeError('No SGLang baseline available for {kda_fn}')\n",
            f"        return _BASELINE_{kda_fn}(*args, **kwargs)\n",
            "    return target(*args, **kwargs)\n\n",
        ])
    path.write_text("".join(lines), encoding="utf-8")
    return path


def regenerate_stub(family: str) -> list[Path]:
    """Write the kda_kernels family package __init__.py for `family`."""
    written: list[Path] = []
    metas = load_family_metadata(family)
    by_fn = exported_arches_by_fn(family, metas)
    # All entries of a family share one kda_module (the family package).
    kda_mod = FAMILY_TO_SWAPS[family][0][2]

    rel = kda_mod.replace(".", "/") + "/__init__.py"
    path = REPO / rel
    target_dir = path.parent
    target_dir.mkdir(parents=True, exist_ok=True)

    if by_fn:
        written.append(write_dispatcher(family, by_fn, metas))
    else:
        dispatcher = target_dir / "_dispatcher.py"
        if dispatcher.exists():
            dispatcher.unlink()

    lines: list[str] = [
        f'"""kda_kernels.diffusion.{family} — CUDA-only KDA-optimized overlay.\n\n',
        'This package contributes the following swap functions:\n\n',
    ]
    lines.extend(
        f"  - `{sgl_mod}:{sgl_fn}`\n"
        for sgl_mod, sgl_fn, _kda_mod, _kda_fn in FAMILY_TO_SWAPS[family]
    )
    lines.extend([
        '\n',
        'Stub status: each function is either re-exported from SGLang\n',
        '(`KDA_OPTIMIZED_<fn> = False`) or routed through the generated\n',
        'architecture dispatcher (`KDA_OPTIMIZED_<fn> = True`). Promotion is\n',
        'driven by `scripts/export_kda_kernels/export.py <task-slug>`.\n',
        '"""\n\n',
    ])

    imports: list[str] = []
    flags: list[str] = []
    stamps: list[str] = []
    if by_fn:
        imports.append(
            f"from kda_kernels.diffusion.{family}._dispatcher import "
            "_preload_kda_impls  # noqa: F401\n"
        )
    for sgl_mod, sgl_fn, _kda_mod, kda_fn in FAMILY_TO_SWAPS[family]:
        arches = by_fn.get(kda_fn, [])
        if arches:
            imports.append(
                f"from kda_kernels.diffusion.{family}._dispatcher import "
                f"{kda_fn}  # noqa: F401\n"
            )
            flags.append(f"KDA_OPTIMIZED_{kda_fn} = True\n")
            stamps.append(
                f"KDA_ARCHES_{kda_fn} = {tuple(arches)!r}\n"
                f"KDA_TASK_{kda_fn} = {metadata_value(arches, metas, 'task_slug')!r}\n"
                f"KDA_COMMIT_{kda_fn} = {metadata_value(arches, metas, 'commit')!r}\n"
                f"KDA_DATE_{kda_fn} = {metadata_value(arches, metas, 'date')!r}\n"
                f"KDA_SPEEDUP_{kda_fn} = {metadata_value(arches, metas, 'speedup')!r}\n"
            )
        else:
            imports.append(f"from {sgl_mod} import {sgl_fn} as {kda_fn}  # noqa: F401\n")
            flags.append(f"KDA_OPTIMIZED_{kda_fn} = False\n")
    body = "".join(lines + imports + ["\n"] + flags + (["\n"] + stamps if stamps else []))
    path.write_text(body, encoding="utf-8")
    written.append(path)
    return written


def clean_legacy_family_files(target_dir: Path) -> None:
    """Remove the pre-multi-arch top-level impl files, keeping arch impls."""
    for entry in target_dir.iterdir():
        if entry.name in FAMILY_TOP_LEVEL_KEEP:
            continue
        if entry.is_dir():
            shutil.rmtree(entry)
        else:
            entry.unlink()


def copy_src(task_dir: Path, family: str, arch: str) -> Path:
    """Copy task `src/` into `kda_kernels/diffusion/<family>/_impls/<arch>/`.

    The whole task src/ tree (CUDA sources, wrapper.py, headers, build glue)
    lands inside one arch-specific package. Existing files for that arch are
    wiped first to keep promotions deterministic. Other arch exports in the
    same family are left intact.
    """
    target_family_dir = family_dir(family)
    target_family_dir.mkdir(parents=True, exist_ok=True)
    clean_legacy_family_files(target_family_dir)
    root = impl_root(family)
    root.mkdir(parents=True, exist_ok=True)
    (root / "__init__.py").touch()
    target_dir = impl_dir(family, arch)
    if target_dir.exists():
        shutil.rmtree(target_dir)
    target_dir.mkdir(parents=True, exist_ok=True)
    src_dir = task_dir / "src"
    for entry in src_dir.iterdir():
        target = target_dir / entry.name
        if entry.is_dir():
            shutil.copytree(entry, target)
        else:
            shutil.copy2(entry, target)
    return target_dir


def family_promoted(family: str, arch: str | None = None) -> bool:
    """True when any/all requested arch metadata exists for a family."""
    metas = load_family_metadata(family)
    if arch is None:
        return bool(metas)
    return arch in metas


def cmd_list() -> int:
    for slug in sorted(
        p.name for p in KERNELS.iterdir() if p.is_dir() and "_diffusion_" in p.name
    ):
        family = family_of(slug) if "_diffusion_" in slug and "__multi_shape" in slug else ""
        arch = arch_of(slug) if family else ""
        marker = " [exported]" if family and family_promoted(family, arch) else ""
        print(f"  {slug}{marker}")
    return 0


def cmd_revert(task_slug: str) -> int:
    family = family_of(task_slug)
    arch = arch_of(task_slug)
    target_dir = impl_dir(family, arch)
    if target_dir.exists():
        shutil.rmtree(target_dir)
        print(f"wiped CUDA sources under kda_kernels/diffusion/{family}/_impls/{arch}/")
    else:
        print(f"no export found under kda_kernels/diffusion/{family}/_impls/{arch}/")
    written = regenerate_stub(family)
    for p in written:
        print(f"  updated {p.relative_to(REPO)}")
    print(f"reset kda_kernels stubs for family={family} arch={arch}")
    return 0


def write_arch_metadata(target_dir: Path, task_slug: str, family: str, arch: str, exports: set[str]) -> dict[str, object]:
    task_dir = KERNELS / task_slug
    commit = task_source_commit(task_dir) or "unknown"
    try:
        if commit == "unknown":
            commit = subprocess.check_output(
                ["git", "rev-parse", "HEAD"], cwd=REPO, text=True
            ).strip()
    except subprocess.CalledProcessError:
        pass
    date = _dt.date.today().isoformat()
    speedup = last_speedup(task_dir)
    meta: dict[str, object] = {
        "task_slug": task_slug,
        "family": family,
        "arch": arch,
        "capability": list(ARCH_CAPABILITIES[arch]),
        "commit": commit,
        "date": date,
        "speedup": speedup,
        "exports": sorted(exports),
    }
    (target_dir / META_FILENAME).write_text(
        json.dumps(meta, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    return meta


def write_status_md(target_dir: Path, meta: dict[str, object]) -> None:
    exports = [str(fn) for fn in meta.get("exports", [])]
    lines = [
        f"# kda_kernels promotion status — {meta.get('family')} / {meta.get('arch')}\n",
        "\n",
        f"| Field | Value |\n",
        f"|---|---|\n",
        f"| Task slug | `{meta.get('task_slug')}` |\n",
        f"| Arch | `{meta.get('arch')}` |\n",
        f"| CUDA capability | `{tuple(meta.get('capability', []))}` |\n",
        f"| Commit (kernel-pilot) | `{meta.get('commit')}` |\n",
        f"| Promotion date | {meta.get('date')} |\n",
        f"| Reported geomean speedup | {meta.get('speedup') or '_(unset)_'} |\n",
        f"| Promoted functions | {', '.join(sorted(exports)) or '_(none)_'} |\n",
        "\n",
        "## Files\n",
        "\n",
    ]
    for entry in sorted(target_dir.iterdir()):
        if entry.name in ("KDA_STATUS.md", META_FILENAME, "__pycache__"):
            continue
        lines.append(f"- `{entry.name}`\n")
    (target_dir / "KDA_STATUS.md").write_text("".join(lines), encoding="utf-8")


def cmd_export(task_slug: str) -> int:
    task_dir = KERNELS / task_slug
    if not task_dir.exists():
        raise SystemExit(f"no such task: {task_dir}")
    family = family_of(task_slug)
    arch = arch_of(task_slug)
    src_dir = task_dir / "src"
    if not src_dir.exists():
        raise SystemExit(f"task {task_slug} has no src/")
    print(f"== exporting task={task_slug} family={family} arch={arch} ==")
    target_dir = copy_src(task_dir, family, arch)
    exports = read_exports(src_dir)
    if not exports:
        print(
            "warning: src/register.py has no EXPORTS dict; "
            "stubs will fall back to sglang baseline",
            file=sys.stderr,
        )
    meta = write_arch_metadata(target_dir, task_slug, family, arch, exports)
    write_status_md(target_dir, meta)
    written = regenerate_stub(family)
    for p in written:
        print(f"  updated {p.relative_to(REPO)}")
    print(f"  copied src/ -> {target_dir.relative_to(REPO)}/")
    print(f"  wrote {target_dir.relative_to(REPO)}/{META_FILENAME}")
    print(f"  wrote {target_dir.relative_to(REPO)}/KDA_STATUS.md")
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
