"""Local entry points for the vendored SGLang CuTe DSL norm/scale/shift baseline.

The upstream snapshot under ``upstream_jit_kernel/jit_kernel/`` is byte-identical
to SGLang main commit 133254086bf1f5b887c8c99d311719102d58a7eb (see
``docs/baseline_source.md``). Its modules use absolute ``sglang.jit_kernel.*``
imports, so this module installs a synthetic ``sglang`` package alias that
resolves those imports against the snapshot directory. The real SGLang package
must never be imported at harness runtime; ``_install_snapshot_alias`` fails
closed if a non-snapshot ``sglang`` module is already present.
"""

from __future__ import annotations

import importlib
import importlib.util
import sys
import types
from pathlib import Path

_BASELINE_DIR = Path(__file__).resolve().parent
SNAPSHOT_ROOT = _BASELINE_DIR / "upstream_jit_kernel" / "jit_kernel"
SNAPSHOT_COMMIT = "133254086bf1f5b887c8c99d311719102d58a7eb"
_ALIAS_MARKER = "_kda_snapshot_root"


def _install_snapshot_alias() -> None:
    existing = sys.modules.get("sglang")
    if existing is not None:
        if getattr(existing, _ALIAS_MARKER, None) == str(SNAPSHOT_ROOT):
            return  # alias already installed by a previous import
        raise RuntimeError(
            "a real 'sglang' module is already imported; the standalone harness "
            "must only use the vendored snapshot (no SGLang import/patch at runtime)"
        )

    if not SNAPSHOT_ROOT.is_dir():
        raise RuntimeError(f"vendored snapshot missing: {SNAPSHOT_ROOT}")

    sglang_pkg = types.ModuleType("sglang")
    sglang_pkg.__path__ = []  # synthetic package: only explicit submodules resolve
    setattr(sglang_pkg, _ALIAS_MARKER, str(SNAPSHOT_ROOT))

    # jit_kernel/utils.py imports sglang.utils.is_in_ci at module load; provide the
    # minimal shim (the harness never runs in SGLang CI).
    utils_shim = types.ModuleType("sglang.utils")
    utils_shim.is_in_ci = lambda: False
    sglang_pkg.utils = utils_shim

    sys.modules["sglang"] = sglang_pkg
    sys.modules["sglang.utils"] = utils_shim

    spec = importlib.util.spec_from_file_location(
        "sglang.jit_kernel",
        SNAPSHOT_ROOT / "__init__.py",
        submodule_search_locations=[str(SNAPSHOT_ROOT)],
    )
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load snapshot package from {SNAPSHOT_ROOT}")
    jit_kernel_pkg = importlib.util.module_from_spec(spec)
    sys.modules["sglang.jit_kernel"] = jit_kernel_pkg
    spec.loader.exec_module(jit_kernel_pkg)
    sglang_pkg.jit_kernel = jit_kernel_pkg


def assert_snapshot_only() -> None:
    """Fail if the 'sglang' module in this process is not the vendored snapshot."""
    mod = sys.modules.get("sglang")
    if mod is None or getattr(mod, _ALIAS_MARKER, None) != str(SNAPSHOT_ROOT):
        raise RuntimeError("sglang module is not the vendored snapshot alias")
    for name, sub in list(sys.modules.items()):
        if not name.startswith("sglang"):
            continue
        mod_file = getattr(sub, "__file__", None)
        if mod_file and not str(Path(mod_file).resolve()).startswith(str(_BASELINE_DIR)):
            raise RuntimeError(f"non-snapshot sglang module loaded: {name} from {mod_file}")


_install_snapshot_alias()

_srnss = importlib.import_module(
    "sglang.jit_kernel.diffusion.cutedsl.scale_residual_norm_scale_shift"
)
_snapshot_utils = importlib.import_module("sglang.jit_kernel.utils")

# Public baseline callables: the upstream torch.library custom ops themselves,
# i.e. the exact host stack production uses (validation, BSFD broadcast, compile
# cache, CuTe launch on the current torch stream, internal output allocation).
fused_norm_scale_shift = _srnss.fused_norm_scale_shift
fused_scale_residual_norm_scale_shift = _srnss.fused_scale_residual_norm_scale_shift

# The snapshot's tvm-ffi JIT loader; the candidate builds through this same
# loader so both sides share one build stack (flags: -std=c++20 -O3
# --expt-relaxed-constexpr + device-derived arch, no fast-math).
snapshot_load_jit = _snapshot_utils.load_jit
SNAPSHOT_KERNEL_PATH = _snapshot_utils.KERNEL_PATH
