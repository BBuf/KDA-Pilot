"""Registration entrypoint for the b200_diffusion_rotary_embedding__multi_shape KDA task.

Exposes the two preserved SGLang public callables (native-CUDA fast path with
baseline fallback) and the KDA registration metadata. ``wrapper.py`` is loaded by
absolute path so this module works whether imported as a package member or via
``importlib.util.spec_from_file_location`` (as the correctness/benchmark harness
does, which sets ``__file__``).

It also stays importable under a bare ``exec`` that does NOT define ``__file__``
(as the KDA export tool does when it only needs the ``EXPORTS`` function-name
keys): in that case the wrapper load is deferred and ``EXPORTS`` maps to lazy
proxies, so the export tool can still read the keys.
"""

from __future__ import annotations

import importlib.util
import os
from typing import Any

KERNEL_SLUG = "b200_diffusion_rotary_embedding__multi_shape"
OP_TYPE = "rotary_embedding"


def _load_wrapper():
    wrapper_py = os.path.join(os.path.dirname(os.path.abspath(__file__)), "wrapper.py")
    spec = importlib.util.spec_from_file_location("kda_diffrope_wrapper", wrapper_py)
    assert spec is not None and spec.loader is not None, wrapper_py
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


try:
    _wrapper = _load_wrapper()  # eager when __file__ is available (harness / runtime)
except Exception:
    _wrapper = None  # bare exec without __file__ (e.g. KDA export reading EXPORTS keys)


def _resolve(name: str):
    global _wrapper
    if _wrapper is None:
        _wrapper = _load_wrapper()
    return getattr(_wrapper, name)


if _wrapper is not None:
    apply_rotary_embedding = _wrapper.apply_rotary_embedding
    apply_ltx2_split_rotary_emb = _wrapper.apply_ltx2_split_rotary_emb
else:

    def apply_rotary_embedding(*args: Any, **kwargs: Any) -> Any:
        return _resolve("apply_rotary_embedding")(*args, **kwargs)

    def apply_ltx2_split_rotary_emb(*args: Any, **kwargs: Any) -> Any:
        return _resolve("apply_ltx2_split_rotary_emb")(*args, **kwargs)


# Map preserved SGLang public callable names -> optimized implementations.
EXPORTS = {
    "apply_rotary_embedding": apply_rotary_embedding,
    "apply_ltx2_split_rotary_emb": apply_ltx2_split_rotary_emb,
}


def optimized_wrapper(*args: Any, **kwargs: Any) -> Any:
    """Back-compatible single-entry wrapper (routes to the standard RoPE op)."""
    return apply_rotary_embedding(*args, **kwargs)


def register() -> dict[str, Any]:
    return {
        "name": KERNEL_SLUG,
        "op_type": OP_TYPE,
        "callable": optimized_wrapper,
        "version": "dev",
        "source": __file__,
        "exports": EXPORTS,
    }
