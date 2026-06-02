"""Registration entrypoint for the h200_diffusion_qknorm_rope__multi_shape KDA task.

``optimized_wrapper`` preserves the SGLang ``fused_inplace_qknorm_rope`` callsite contract:
in-place on q and k, returns None. Supported signatures use the native-CUDA candidate built via
SGLang's jit_kernel/tvm-ffi stack; unsupported signatures take a safe PyTorch semantic fallback.

``EXPORTS`` is read by ``scripts/export_kda_kernels/export.py`` (keys only) to decide which
functions to promote into ``kda_kernels``. The wrapper is imported lazily so this file ``exec``s
cleanly even where ``__file__``/torch/sglang are absent (the export tool ``exec``s this module in a
bare namespace and only needs the ``EXPORTS`` keys).
"""

from __future__ import annotations

import sys
from pathlib import Path
from typing import Any

# Make ``wrapper`` importable when this file is loaded as a standalone module (the KDA
# correctness/benchmark harness loads it by path). Guard against exec contexts without
# ``__file__`` (export.py's read_exports execs this file in a bare namespace).
try:
    _SRC_DIR = str(Path(__file__).resolve().parent)
    if _SRC_DIR not in sys.path:
        sys.path.insert(0, _SRC_DIR)
except NameError:
    pass

KERNEL_SLUG = "h200_diffusion_qknorm_rope__multi_shape"
OP_TYPE = "qknorm_rope_inplace"


def optimized_wrapper(*args: Any, **kwargs: Any) -> Any:
    """Lazy forwarder to the wrapper's optimized op (re-exported as the registered callable)."""
    from wrapper import optimized_wrapper as _impl

    return _impl(*args, **kwargs)


def register() -> dict[str, Any]:
    return {
        "name": KERNEL_SLUG,
        "op_type": OP_TYPE,
        "callable": optimized_wrapper,
        "version": "dev",
        "source": __file__,
    }


# Only the keys matter to the export tool; the value is the promoted callable. The wrapper module
# also exposes ``fused_inplace_qknorm_rope`` directly, which is what the generated kda_kernels
# dispatcher imports.
EXPORTS = {
    "fused_inplace_qknorm_rope": optimized_wrapper,
}
