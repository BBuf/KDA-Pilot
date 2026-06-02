"""Registration entrypoint for the h200_diffusion_rotary_embedding__multi_shape KDA task.

Exposes the two public SGLang diffusion RoPE callables (preserving their names) plus
a single ``optimized_wrapper`` compatibility entry that dispatches by the cos rank.
The real dispatch / kernel logic lives in ``wrapper.py``.
"""

from __future__ import annotations

import sys
from pathlib import Path
from typing import Any

_THIS_DIR = Path(__file__).resolve().parent
if str(_THIS_DIR) not in sys.path:
    sys.path.insert(0, str(_THIS_DIR))

import wrapper  # noqa: E402


KERNEL_SLUG = "h200_diffusion_rotary_embedding__multi_shape"
OP_TYPE = "rotary_embedding"

# Public callables (preserve the exact SGLang names for the in-SGLang export).
apply_rotary_embedding = wrapper.apply_rotary_embedding
apply_ltx2_split_rotary_emb = wrapper.apply_ltx2_split_rotary_emb
optimized_wrapper = wrapper.optimized_wrapper


def register() -> dict[str, Any]:
    return {
        "name": KERNEL_SLUG,
        "op_type": OP_TYPE,
        "callable": optimized_wrapper,
        "version": "dev",
        "source": __file__,
    }


EXPORTS = {
    "apply_rotary_embedding": apply_rotary_embedding,
    "apply_ltx2_split_rotary_emb": apply_ltx2_split_rotary_emb,
}
