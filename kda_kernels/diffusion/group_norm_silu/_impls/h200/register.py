"""Registration for the h200_diffusion_group_norm_silu__multi_shape KDA task.

Exposes the two public SGLang callable names (``triton_group_norm_silu`` and
``apply_group_norm_silu``) backed by the zero-overhead native-CUDA dispatcher in
``group_norm_dispatch.py`` (re-exported by ``wrapper.py``). The native kernel is
built through SGLang's jit_kernel / tvm-ffi stack (``load_jit``), NOT
``torch.utils.cpp_extension``.

``EXPORTS`` is the contract consumed by ``scripts/export_kda_kernels/export.py``:
it maps each public SGLang callable name to the wrapper that replaces it after
promotion into ``kda_kernels``. The export tool reads ``EXPORTS`` by ``exec``-ing
this file in a bare namespace (no ``__file__``, possibly no sglang/torch), so the
bindings below are guarded to keep the dict's keys readable in that environment;
the callables resolve at runtime where the GPU stack is available.
"""

from __future__ import annotations

import pathlib
import sys
from typing import Any

KERNEL_SLUG = "h200_diffusion_group_norm_silu__multi_shape"
OP_TYPE = "group_norm_silu"

# Make the task src dir importable when loaded as a standalone file. Guarded because
# the export tool exec()s this file without __file__ defined.
try:
    _SRC = str(pathlib.Path(__file__).resolve().parent)
    if _SRC not in sys.path:
        sys.path.insert(0, _SRC)
except NameError:
    pass

try:
    from group_norm_dispatch import (
        apply_group_norm_silu,
        selected_path,
        triton_group_norm_silu,
    )
except Exception:  # pragma: no cover - export-time read without the GPU stack
    triton_group_norm_silu = None  # type: ignore[assignment]
    apply_group_norm_silu = None  # type: ignore[assignment]
    selected_path = None  # type: ignore[assignment]

# Public SGLang callable name -> replacement wrapper. Read by the export tool.
EXPORTS = {
    "triton_group_norm_silu": triton_group_norm_silu,
    "apply_group_norm_silu": apply_group_norm_silu,
}


def optimized_wrapper(*args: Any, **kwargs: Any) -> Any:
    """Generic harness entry (benchmark.py / test_correctness.py). Routes by signature:
    the apply form is (x, nn.GroupNorm, nn.SiLU); everything else is the triton form
    (x, weight, bias, num_groups, eps)."""
    from torch import nn

    if len(args) >= 3 and isinstance(args[1], nn.GroupNorm) and isinstance(args[2], nn.SiLU):
        return apply_group_norm_silu(args[0], args[1], args[2])
    x = args[0]
    weight = args[1] if len(args) > 1 else kwargs.get("weight")
    bias = args[2] if len(args) > 2 else kwargs.get("bias")
    num_groups = args[3] if len(args) > 3 else kwargs.get("num_groups")
    eps = args[4] if len(args) > 4 else kwargs.get("eps", 1e-5)
    return triton_group_norm_silu(x, weight, bias, num_groups, eps)


def register() -> dict[str, Any]:
    return {
        "name": KERNEL_SLUG,
        "op_type": OP_TYPE,
        "callable": optimized_wrapper,
        "exports": dict(EXPORTS),
        "version": "dev",
        "source": __file__,
    }
