"""Registration entrypoint for the h200_diffusion_qknorm_rope__multi_shape task.

``optimized_wrapper`` preserves the recovered SGLang callsite contract and
routes the production signature to the workspace-owned native CUDA kernel,
falling back to the SGLang baseline otherwise (see ``wrapper.py``).

``EXPORTS`` is read by ``scripts/export_kda_kernels/export.py`` (keys only) to
decide which functions to promote. The wrapper is imported lazily so this file
``exec``s cleanly even where torch/sglang are absent (e.g. a local export run).
"""

from __future__ import annotations

import sys
from pathlib import Path
from typing import Any

# Make ``wrapper`` importable when this file is loaded as a standalone module
# (the KDA correctness/benchmark harness loads it by path). Guard against exec
# contexts without ``__file__`` (export.py's read_exports execs this file in a
# bare namespace and only needs the EXPORTS keys).
try:
    _SRC_DIR = str(Path(__file__).resolve().parent)
    if _SRC_DIR not in sys.path:
        sys.path.insert(0, _SRC_DIR)
except NameError:
    pass

KERNEL_SLUG = "h200_diffusion_qknorm_rope__multi_shape"
OP_TYPE = "qknorm_rope_inplace"


def optimized_wrapper(*args: Any, **kwargs: Any) -> Any:
    from wrapper import fused_inplace_qknorm_rope

    return fused_inplace_qknorm_rope(*args, **kwargs)


def register() -> dict[str, Any]:
    return {
        "name": KERNEL_SLUG,
        "op_type": OP_TYPE,
        "callable": optimized_wrapper,
        "version": "dev",
        "source": __file__,
    }


# Only the keys matter to the export tool; the value is the promoted callable.
EXPORTS = {
    "fused_inplace_qknorm_rope": optimized_wrapper,
}
