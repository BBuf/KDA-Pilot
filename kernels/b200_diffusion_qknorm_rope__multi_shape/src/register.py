"""Registration entrypoint for the b200_diffusion_qknorm_rope__multi_shape KDA task.

``optimized_wrapper`` preserves the SGLang ``fused_inplace_qknorm_rope`` callsite contract
exactly (positional ``q, k, q_weight, k_weight, cos_sin_cache, positions``; keyword-only
``is_neox``, ``eps``, ``head_dim``, ``rope_dim``; returns ``None`` and mutates ``q`` and
``k`` in place). Supported (exact captured-large) signatures use the native-CUDA staged
candidate built via SGLang's jit_kernel/tvm-ffi stack; every other signature falls back to
the SGLang baseline. All implementation lives in the sibling ``wrapper.py`` module.

The sibling is loaded under a SLUG-SPECIFIC module name (``_kda_impl_<slug>_wrapper``) via
``importlib`` — NOT ``from wrapper import ...`` — so that when several kernels' ``register.py``
files are loaded in one process, this task never resolves another task's top-level ``wrapper``
out of ``sys.modules``.

``EXPORTS`` is read by ``scripts/export_kda_kernels/export.py`` (keys only) to decide which
functions to promote into ``kda_kernels``. The wrapper is imported lazily (only when called) so
this file ``exec``s cleanly even where ``__file__``/torch/sglang are absent — the export tool
``exec``s this module in a bare namespace and only needs the ``EXPORTS`` keys.
"""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path
from typing import Any

KERNEL_SLUG = "b200_diffusion_qknorm_rope__multi_shape"
OP_TYPE = "qknorm_rope_inplace"

# Resolve the source dir when ``__file__`` is available (the KDA correctness/benchmark harness
# loads this file by path). Guard against exec contexts without ``__file__`` — export.py's
# ``read_exports`` execs this module in a bare namespace and only reads ``EXPORTS``.
try:
    _SRC_DIR = str(Path(__file__).resolve().parent)
except NameError:
    _SRC_DIR = None

# Slug-specific module name so loading this task's wrapper can never collide with another
# task's top-level ``wrapper`` already present in sys.modules.
_IMPL_MODNAME = f"_kda_impl_{KERNEL_SLUG}_wrapper"
_impl_module = None


def _load_impl():
    """Import this task's sibling ``wrapper.py`` under ``_IMPL_MODNAME`` (memoized).

    Uses an explicit file-location spec so resolution is by absolute path, never via a
    generic name in ``sys.modules`` / ``sys.path`` that another kernel could shadow.
    """
    global _impl_module
    if _impl_module is not None:
        return _impl_module
    module = sys.modules.get(_IMPL_MODNAME)
    if module is None:
        if _SRC_DIR is None:
            raise RuntimeError(
                "register.py was loaded without __file__; cannot locate wrapper.py "
                "(this path is only reachable when the op is actually called)."
            )
        wrapper_path = str(Path(_SRC_DIR) / "wrapper.py")
        spec = importlib.util.spec_from_file_location(_IMPL_MODNAME, wrapper_path)
        if spec is None or spec.loader is None:
            raise ImportError(f"cannot load wrapper.py for {KERNEL_SLUG} at {wrapper_path}")
        module = importlib.util.module_from_spec(spec)
        sys.modules[_IMPL_MODNAME] = module
        spec.loader.exec_module(module)
    _impl_module = module
    return _impl_module


def optimized_wrapper(*args: Any, **kwargs: Any) -> Any:
    """Lazy forwarder to this task's wrapper op (re-exported as the registered callable)."""
    return _load_impl().optimized_wrapper(*args, **kwargs)


def register() -> dict[str, Any]:
    return {
        "name": KERNEL_SLUG,
        "op_type": OP_TYPE,
        "callable": optimized_wrapper,
        "version": "dev",
        "source": __file__,
    }


# Only the keys matter to the export tool; the value is the promoted callable. The wrapper
# module also exposes ``fused_inplace_qknorm_rope`` directly, which is what the generated
# kda_kernels dispatcher imports.
EXPORTS = {
    "fused_inplace_qknorm_rope": optimized_wrapper,
}
