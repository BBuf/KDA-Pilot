"""Shape-capture shim for the GroupNorm+SiLU entry points (audit evidence).

Activated by prepending this directory to PYTHONPATH before launching a native
SGLang diffusion preset run (the interpreter auto-imports ``sitecustomize``;
the variable propagates to spawned worker processes). It wraps the two public
entry points the moment their modules finish importing and appends one JSONL
row per call to ``GNS_CAPTURE_OUT``.

This shim exists for *workload-audit capture runs only* — it patches nothing
on disk and is never active during correctness or benchmark runs (those forbid
touching sglang entirely). Row format matches the retained pre-reset capture
JSONL consumed by bench/gen_workloads.py.

Environment:
    GNS_CAPTURE_OUT    output JSONL path (required to activate)
    GNS_CAPTURE_MODEL  model/preset label recorded per row
    GNS_CAPTURE_ARCH   arch label (default: h200)
"""

from __future__ import annotations

import builtins
import json
import os
import socket
import sys
import threading
import time

_OUT = os.environ.get("GNS_CAPTURE_OUT")

if _OUT:
    _LOCK = threading.Lock()
    _COUNTS: dict[str, int] = {}
    _SEEN: set = set()

    _TARGETS = {
        "sglang.jit_kernel.diffusion.group_norm_silu": (
            "apply_group_norm_silu",
            "group_norm_silu.apply_group_norm_silu",
        ),
        "sglang.jit_kernel.diffusion.triton.group_norm_silu": (
            "triton_group_norm_silu",
            "group_norm_silu.triton_group_norm_silu",
        ),
    }

    def _describe(arg):
        try:
            import torch

            if isinstance(arg, torch.Tensor):
                return {
                    "contiguous": bool(arg.is_contiguous()),
                    "device": str(arg.device),
                    "dtype": str(arg.dtype),
                    "shape": list(arg.shape),
                    "strides": list(arg.stride()),
                }
        except Exception:
            pass
        return f"<{type(arg).__name__}>"

    def _log_call(kernel: str, args, kwargs) -> None:
        try:
            described_args = [_describe(a) for a in args]
            described_kwargs = {
                k: (v if isinstance(v, (int, float, str, bool)) else _describe(v))
                for k, v in kwargs.items()
            }
            sig = json.dumps(
                [kernel, described_args, described_kwargs], sort_keys=True, default=str
            )
            with _LOCK:
                _COUNTS[kernel] = _COUNTS.get(kernel, 0) + 1
                row = {
                    "arch": os.environ.get("GNS_CAPTURE_ARCH", "h200"),
                    "args": described_args,
                    "call_idx": _COUNTS[kernel],
                    "host": socket.gethostname(),
                    "kernel": kernel,
                    "kwargs": described_kwargs,
                    "model": os.environ.get("GNS_CAPTURE_MODEL", "unknown"),
                    "new_signature": sig not in _SEEN,
                    "ts": time.time(),
                }
                _SEEN.add(sig)
                with open(_OUT, "a", encoding="utf-8") as fh:
                    fh.write(json.dumps(row) + "\n")
        except Exception:
            pass  # capture must never break the model run

    def _wrap(module, attr: str, kernel_name: str) -> None:
        original = getattr(module, attr, None)
        if original is None or getattr(original, "_gns_capture_wrapped", False):
            return

        def wrapper(*args, **kwargs):
            _log_call(kernel_name, args, kwargs)
            return original(*args, **kwargs)

        wrapper._gns_capture_wrapped = True
        wrapper.__name__ = getattr(original, "__name__", attr)
        setattr(module, attr, wrapper)

    def _patch_loaded_targets() -> None:
        for mod_name, (attr, kernel_name) in _TARGETS.items():
            module = sys.modules.get(mod_name)
            if module is not None:
                _wrap(module, attr, kernel_name)

    _orig_import = builtins.__import__

    def _capture_import(name, globals=None, locals=None, fromlist=(), level=0):
        module = _orig_import(name, globals, locals, fromlist, level)
        # Cheap post-import sweep whenever anything sglang-related loads.
        if name.startswith("sglang"):
            _patch_loaded_targets()
        return module

    builtins.__import__ = _capture_import
    _patch_loaded_targets()
