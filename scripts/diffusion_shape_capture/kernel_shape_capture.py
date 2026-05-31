"""Monkey-patch diffusion kernels in SGLang to record input shapes/dtypes.

Activated by `sitecustomize.py` shipped next to this file. Writes one JSON line
per observed call to the file at `DIFFUSION_SHAPE_LOG`, defaulting to
`/tmp/diffusion_shape_log.jsonl`. Each line includes the kernel slug, label,
positional/keyword arg shape/dtype info, and a coarse call counter.

The hook never raises on capture failures - it always falls through to the
original function call. The log file is opened in append mode and flushed
after every record, so partial runs still yield useful data.
"""

from __future__ import annotations

import json
import os
import sys
import threading
import time
from typing import Any

_LOG_PATH = os.environ.get("DIFFUSION_SHAPE_LOG", "/tmp/diffusion_shape_log.jsonl")
_MODEL_LABEL = os.environ.get("DIFFUSION_SHAPE_MODEL", "unknown")
_HOST_LABEL = os.environ.get("DIFFUSION_SHAPE_HOST", "unknown")
_ARCH_LABEL = os.environ.get("DIFFUSION_SHAPE_ARCH", "unknown")

_lock = threading.Lock()
_call_counters: dict[str, int] = {}
_seen_signatures: set[tuple[str, str]] = set()
_installed = False


def _shape(value: Any) -> Any:
    try:
        import torch
    except Exception:
        torch = None
    if torch is not None and hasattr(value, "shape") and hasattr(value, "dtype"):
        try:
            return {
                "shape": list(value.shape),
                "dtype": str(value.dtype),
                "device": str(getattr(value, "device", "?")),
                "strides": list(value.stride()) if hasattr(value, "stride") else None,
                "contiguous": bool(value.is_contiguous()) if hasattr(value, "is_contiguous") else None,
            }
        except Exception:
            return {"shape": list(value.shape), "dtype": str(value.dtype)}
    if isinstance(value, (list, tuple)):
        return [_shape(v) for v in value]
    if isinstance(value, dict):
        return {k: _shape(v) for k, v in value.items()}
    if isinstance(value, (int, float, bool, str)) or value is None:
        return value
    return f"<{type(value).__name__}>"


def _emit(record: dict[str, Any]) -> None:
    try:
        with _lock:
            with open(_LOG_PATH, "a", buffering=1) as f:
                f.write(json.dumps(record, default=str) + "\n")
    except Exception:
        pass


def _wrap(kernel_name: str, fn):
    def wrapped(*args, **kwargs):
        try:
            shaped_args = [_shape(a) for a in args]
            shaped_kwargs = {k: _shape(v) for k, v in kwargs.items()}
            signature = json.dumps(
                {"args": shaped_args, "kwargs": shaped_kwargs},
                sort_keys=True,
                default=str,
            )
            with _lock:
                _call_counters[kernel_name] = _call_counters.get(kernel_name, 0) + 1
                call_idx = _call_counters[kernel_name]
                signature_key = (kernel_name, signature)
                is_new_signature = signature_key not in _seen_signatures
                if is_new_signature:
                    _seen_signatures.add(signature_key)
            if is_new_signature or call_idx <= 4 or call_idx % 1024 == 0:
                _emit(
                    {
                        "kernel": kernel_name,
                        "model": _MODEL_LABEL,
                        "host": _HOST_LABEL,
                        "arch": _ARCH_LABEL,
                        "call_idx": call_idx,
                        "new_signature": is_new_signature,
                        "args": shaped_args,
                        "kwargs": shaped_kwargs,
                        "ts": time.time(),
                    }
                )
        except Exception:
            pass
        return fn(*args, **kwargs)

    wrapped.__wrapped__ = fn  # type: ignore[attr-defined]
    wrapped.__name__ = getattr(fn, "__name__", kernel_name)
    return wrapped


_TARGETS = [
    ("sglang.jit_kernel.diffusion.qknorm_rope", "fused_inplace_qknorm_rope"),
    ("sglang.jit_kernel.diffusion.triton.norm", "norm_infer"),
    ("sglang.jit_kernel.diffusion.triton.rmsnorm_onepass", "triton_one_pass_rms_norm"),
    ("sglang.jit_kernel.diffusion.triton.group_norm_silu", "triton_group_norm_silu"),
    ("sglang.jit_kernel.diffusion.group_norm_silu", "apply_group_norm_silu"),
    ("sglang.jit_kernel.diffusion.triton.rotary", "apply_rotary_embedding"),
    ("sglang.jit_kernel.diffusion.triton.ltx2_rotary", "apply_ltx2_split_rotary_emb"),
    ("sglang.jit_kernel.diffusion.triton.scale_shift", "fuse_scale_shift_kernel"),
    ("sglang.jit_kernel.diffusion.triton.scale_shift", "fuse_layernorm_scale_shift_gate_select01_kernel"),
    ("sglang.jit_kernel.diffusion.triton.scale_shift", "fuse_residual_layernorm_scale_shift_gate_select01_kernel"),
    ("sglang.jit_kernel.diffusion.cutedsl.norm_tanh_mul_add_norm_scale", "fused_norm_tanh_mul_add"),
    ("sglang.jit_kernel.diffusion.cutedsl.norm_tanh_mul_add_norm_scale", "fused_norm_tanh_mul_add_norm_scale"),
    ("sglang.jit_kernel.diffusion.cutedsl.scale_residual_norm_scale_shift", "fused_norm_scale_shift"),
    ("sglang.jit_kernel.diffusion.cutedsl.scale_residual_norm_scale_shift", "fused_scale_residual_norm_scale_shift"),
]


def _is_triton_jit(fn) -> bool:
    """Skip Triton kernels (must remain subscriptable)."""
    cls = type(fn).__name__
    return cls in {"JITFunction", "Autotuner", "Heuristics"} or hasattr(fn, "arg_names")


def install() -> None:
    global _installed
    if _installed:
        return
    _installed = True
    _emit(
        {
            "event": "install",
            "model": _MODEL_LABEL,
            "host": _HOST_LABEL,
            "arch": _ARCH_LABEL,
            "ts": time.time(),
            "log_path": _LOG_PATH,
            "pid": os.getpid(),
        }
    )
    for module_path, name in _TARGETS:
        try:
            __import__(module_path)
            module = sys.modules[module_path]
            target = getattr(module, name, None)
            if target is None:
                continue
            if getattr(target, "_diff_shape_wrapped", False):
                continue
            if _is_triton_jit(target):
                continue
            slug = f"{module_path.rsplit('.', 1)[-1]}.{name}"
            wrapped = _wrap(slug, target)
            wrapped._diff_shape_wrapped = True  # type: ignore[attr-defined]
            setattr(module, name, wrapped)
        except Exception as exc:
            _emit(
                {
                    "event": "install_skip",
                    "kernel": f"{module_path}.{name}",
                    "error": repr(exc),
                }
            )

    try:
        import torch.library
        original_impl_fn = getattr(torch.library, "_C", None)
    except Exception:
        pass


install()
