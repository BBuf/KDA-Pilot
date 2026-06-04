"""Dispatcher for the b200_diffusion_cutedsl_norm_tanh_mul_add__multi_shape task.

``optimized_wrapper`` preserves the public SGLang contract of both entry
points:

    fused_norm_tanh_mul_add(x, weight, bias, scale, shift, norm_type, eps=1e-5)
    fused_norm_tanh_mul_add_norm_scale(x, weight, bias, scale, shift,
                                       weight2, bias2, scale2, norm_type, eps=1e-5)

Routing:
- eligible signatures go to the native CUDA fast path (``src/norm_tanh_cuda``,
  built through SGLang's jit_kernel / tvm-ffi stack);
- everything else falls back to the frozen CuTe-DSL baseline copy under
  ``baseline/`` (which enforces the upstream validation contract, raising
  ValueError exactly like the public op);
- with ``KDA_REQUIRE_CANDIDATE=1`` a would-be fallback raises RuntimeError
  instead, so benchmarks can never silently measure the baseline as the
  candidate.
"""

from __future__ import annotations

import importlib.util
import os
import sys
from pathlib import Path
from typing import Any, Optional

KERNEL_SLUG = "b200_diffusion_cutedsl_norm_tanh_mul_add__multi_shape"
OP_TYPE = "cutedsl_norm_tanh_mul_add"

_KERNEL_DIR = Path(__file__).resolve().parents[1]
if str(_KERNEL_DIR) not in sys.path:
    sys.path.insert(0, str(_KERNEL_DIR))

_SUPPORTED_DTYPES = ("torch.float16", "torch.bfloat16", "torch.float32")
_NORM_TYPES = ("layer", "rms")
_VECTOR_ELEMS = 8  # one thread owns 8 elements; row starts must stay vector-aligned

_fast_path_hit_count = 0
_fallback_hit_count = 0
_last_fallback_reason: str = ""

_baseline_mod = None
_native_mod: Any = None
_native_load_attempted = False
_native_load_error: str = ""


def _baseline():
    global _baseline_mod
    if _baseline_mod is None:
        import baseline  # self-contained copy, see docs/baseline_source.md

        _baseline_mod = baseline
    return _baseline_mod


def _load_native():
    """Load the native CUDA module (jit_kernel / tvm-ffi build) if present."""

    global _native_mod, _native_load_attempted, _native_load_error
    if _native_load_attempted:
        return _native_mod
    _native_load_attempted = True
    wrapper_py = _KERNEL_DIR / "src" / "norm_tanh_cuda" / "wrapper.py"
    if not wrapper_py.exists():
        _native_load_error = f"native wrapper not present: {wrapper_py}"
        return None
    try:
        spec = importlib.util.spec_from_file_location(
            f"kda_{KERNEL_SLUG}_native", wrapper_py
        )
        assert spec is not None and spec.loader is not None
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        _native_mod = module
    except Exception as exc:  # noqa: BLE001 - record and fall back
        _native_load_error = f"native wrapper failed to load: {exc!r}"
        _native_mod = None
    return _native_mod


def native_available() -> bool:
    return _load_native() is not None


def native_load_error() -> str:
    _load_native()
    return _native_load_error


def fast_path_hits() -> int:
    return _fast_path_hit_count


def fallback_hits() -> int:
    return _fallback_hit_count


def last_fallback_reason() -> str:
    return _last_fallback_reason


def _parse_call(args: tuple, kwargs: dict) -> dict:
    """Normalize positional/keyword calls of either entry point."""

    second_norm_kwargs = {"weight2", "bias2", "scale2"}
    if len(args) >= 8 or second_norm_kwargs & kwargs.keys():
        names = [
            "x", "weight", "bias", "scale", "shift",
            "weight2", "bias2", "scale2", "norm_type", "eps",
        ]
        variant = "v2"
    else:
        names = ["x", "weight", "bias", "scale", "shift", "norm_type", "eps"]
        variant = "v1"
    params: dict[str, Any] = {"eps": 1e-5}
    for name, value in zip(names, args):
        params[name] = value
    for key, value in kwargs.items():
        if key not in names:
            raise TypeError(f"unexpected keyword argument: {key}")
        params[key] = value
    missing = [n for n in names if n not in params and n != "eps"]
    if missing:
        raise TypeError(f"missing arguments: {missing}")
    params["variant"] = variant
    return params


def _is_3d_broadcastable(t, B: int, S: int, D: int) -> bool:
    return (
        t.ndim == 3
        and t.shape[0] in (1, B)
        and t.shape[1] in (1, S)
        and t.shape[2] == D
        and t.stride(-1) == 1
    )


def _is_weight_like(t, D: int) -> bool:
    return t is None or (t.ndim == 1 and t.shape == (D,) and t.stride(-1) == 1)


def _effective_affine(weight, bias, norm_type: str) -> bool:
    """Baseline affine semantics: rms uses weight only (bias ignored); layer
    applies affine only when BOTH weight and bias are tensors."""

    if norm_type == "rms":
        return weight is not None
    return weight is not None and bias is not None


def _fast_path_reject_reason(p: dict) -> Optional[str]:
    """Return None when the native fast path can handle this call."""

    import torch

    x = p["x"]
    if not isinstance(x, torch.Tensor):
        return "x is not a tensor"
    if not x.is_cuda:
        return "x is not a CUDA tensor"
    if x.ndim != 3:
        return f"x ndim {x.ndim} != 3"
    if str(x.dtype) not in _SUPPORTED_DTYPES:
        return f"unsupported dtype {x.dtype}"
    if p["norm_type"] not in _NORM_TYPES:
        return f"unsupported norm_type {p['norm_type']!r}"
    B, S, D = x.shape
    if D % 256 != 0 or D > 8192:
        return f"D={D} outside contract (D % 256 == 0 and D <= 8192)"
    if not x.is_contiguous():
        return "x is not contiguous"
    vec_bytes = _VECTOR_ELEMS * x.element_size()
    tensor_keys = ["scale", "shift"] + (["scale2"] if p["variant"] == "v2" else [])
    weight_keys = ["weight", "bias"] + (
        ["weight2", "bias2"] if p["variant"] == "v2" else []
    )
    for key in tensor_keys:
        t = p[key]
        if not isinstance(t, torch.Tensor):
            return f"{key} is not a tensor"
        if not _is_3d_broadcastable(t, B, S, D):
            return f"{key} layout {tuple(t.shape)} not [1|B, 1|S, D] contiguous-D"
        if t.dtype != x.dtype:
            return f"{key} dtype {t.dtype} != x dtype {x.dtype}"
        if not t.is_cuda or t.device != x.device:
            return f"{key} not on {x.device}"
        # Rows accessed via effective strides must stay vector-aligned.
        for dim in (0, 1):
            if t.shape[dim] != 1 and t.stride(dim) % _VECTOR_ELEMS != 0:
                return f"{key} stride({dim})={t.stride(dim)} not a multiple of {_VECTOR_ELEMS}"
    for key in weight_keys:
        t = p[key]
        if t is None:
            continue
        if not isinstance(t, torch.Tensor) or not _is_weight_like(t, D):
            return f"{key} is not None or a contiguous [D] tensor"
        if t.dtype != x.dtype:
            return f"{key} dtype {t.dtype} != x dtype {x.dtype}"
        if not t.is_cuda or t.device != x.device:
            return f"{key} not on {x.device}"
    if p["variant"] == "v2" and _effective_affine(
        p["weight2"], p["bias2"], p["norm_type"]
    ) != _effective_affine(p["weight"], p["bias"], p["norm_type"]):
        return "second-norm effective affine pattern differs from the first norm"
    for key in ["x"] + tensor_keys + weight_keys:
        t = p[key]
        if t is not None and t.data_ptr() % vec_bytes != 0:
            return f"{key} base pointer not {vec_bytes}-byte aligned"
    if not native_available():
        return native_load_error() or "native module unavailable"
    return None


def _run_baseline(p: dict):
    mod = _baseline()
    if p["variant"] == "v1":
        return mod.fused_norm_tanh_mul_add(
            p["x"], p["weight"], p["bias"], p["scale"], p["shift"],
            p["norm_type"], p["eps"],
        )
    return mod.fused_norm_tanh_mul_add_norm_scale(
        p["x"], p["weight"], p["bias"], p["scale"], p["shift"],
        p["weight2"], p["bias2"], p["scale2"], p["norm_type"], p["eps"],
    )


def _run_native(p: dict):
    native = _load_native()
    if p["variant"] == "v1":
        return native.fused_norm_tanh_mul_add(
            p["x"], p["weight"], p["bias"], p["scale"], p["shift"],
            p["norm_type"], p["eps"],
        )
    return native.fused_norm_tanh_mul_add_norm_scale(
        p["x"], p["weight"], p["bias"], p["scale"], p["shift"],
        p["weight2"], p["bias2"], p["scale2"], p["norm_type"], p["eps"],
    )


def optimized_wrapper(*args: Any, **kwargs: Any) -> Any:
    global _fast_path_hit_count, _fallback_hit_count, _last_fallback_reason

    params = _parse_call(args, kwargs)
    reason = _fast_path_reject_reason(params)
    if reason is None:
        _fast_path_hit_count += 1
        return _run_native(params)
    _last_fallback_reason = reason
    if os.environ.get("KDA_REQUIRE_CANDIDATE") == "1":
        raise RuntimeError(
            f"KDA_REQUIRE_CANDIDATE=1 but the native fast path declined: {reason}"
        )
    _fallback_hit_count += 1
    return _run_baseline(params)


def register() -> dict[str, Any]:
    return {
        "name": KERNEL_SLUG,
        "op_type": OP_TYPE,
        "callable": optimized_wrapper,
        "version": "dev",
        "source": __file__,
    }
