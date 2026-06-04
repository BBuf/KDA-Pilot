"""Local low-overhead entry ABI for the vendored SGLang baseline.

Both functions resolve lazily to the snapshot's public custom ops (the same
``@torch.library.custom_op`` wrappers production uses), so baseline timings
include the identical host-side registration/dispatch cost as the shipping
SGLang path. No SGLang checkout is imported at any point (enforced by
``loader.assert_snapshot_only``).
"""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

_HERE = Path(__file__).resolve().parent

_loader_spec = importlib.util.spec_from_file_location(
    "kda_baseline_loader", _HERE / "loader.py"
)
assert _loader_spec is not None and _loader_spec.loader is not None
loader = importlib.util.module_from_spec(_loader_spec)
sys.modules["kda_baseline_loader"] = loader
_loader_spec.loader.exec_module(loader)

_MOD = None


def _module():
    global _MOD
    if _MOD is None:
        _MOD = loader.baseline_module()
        loader.assert_snapshot_only()
    return _MOD


def fused_norm_scale_shift(x, weight, bias, scale, shift, norm_type, eps=1e-5):
    return _module().fused_norm_scale_shift(
        x, weight, bias, scale, shift, norm_type, eps
    )


def fused_scale_residual_norm_scale_shift(
    residual, x, gate, weight, bias, scale, shift, norm_type, eps=1e-5
):
    return _module().fused_scale_residual_norm_scale_shift(
        residual, x, gate, weight, bias, scale, shift, norm_type, eps
    )
