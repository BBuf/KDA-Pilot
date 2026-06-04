"""Apply the minimal in-tree routing patch to scale_residual_norm_scale_shift.py.

Inserts a try-native-first block at the top of both public custom-op BODIES
(the `@torch.library.custom_op` registrations themselves are untouched).
Refuses to patch if the target file does not match the pinned baseline hash
(guards against version drift) or is already patched.

Usage: python apply_patch.py <path/to/scale_residual_norm_scale_shift.py>
"""

from __future__ import annotations

import hashlib
import sys
from pathlib import Path

PINNED_SHA256 = "d6818e5da8d3c5ace3950313e996a22b4c051edc29ab7026eb8cb9d79e414df9"

NSS_ANCHOR = (
    "    stream = cuda.CUstream(torch.cuda.current_stream().cuda_stream)\n"
    "    # Tensor Validation\n"
)
NSS_INSERT = (
    "    from sglang.jit_kernel.diffusion.norm_scale_shift_native import (\n"
    "        try_fused_norm_scale_shift as _try_native_nss,\n"
    "    )\n"
    "\n"
    "    _native_y = _try_native_nss(x, weight, bias, scale, shift, norm_type, eps)\n"
    "    if _native_y is not None:\n"
    "        return _native_y\n"
)

SRNSS_ANCHOR = (
    "    # Tensor Validation\n"
    "    BSD = x.shape\n"
    "    validate_x(x, *BSD)\n"
    "    validate_x(residual, *BSD)\n"
)
SRNSS_INSERT = (
    "    from sglang.jit_kernel.diffusion.norm_scale_shift_native import (\n"
    "        try_fused_scale_residual_norm_scale_shift as _try_native_srnss,\n"
    "    )\n"
    "\n"
    "    _native_out = _try_native_srnss(\n"
    "        residual, x, gate, weight, bias, scale, shift, norm_type, eps\n"
    "    )\n"
    "    if _native_out is not None:\n"
    "        return _native_out\n"
)


def main() -> int:
    target = Path(sys.argv[1])
    text = target.read_text()
    if "norm_scale_shift_native" in text:
        print("already patched; nothing to do")
        return 0
    digest = hashlib.sha256(text.encode()).hexdigest()
    if digest != PINNED_SHA256:
        print(f"refusing to patch: sha256 {digest} != pinned {PINNED_SHA256}")
        return 1
    if text.count(NSS_ANCHOR) != 1 or text.count(SRNSS_ANCHOR) != 1:
        print("refusing to patch: anchors not unique")
        return 1
    text = text.replace(NSS_ANCHOR, NSS_INSERT + NSS_ANCHOR, 1)
    text = text.replace(SRNSS_ANCHOR, SRNSS_INSERT + SRNSS_ANCHOR, 1)
    target.write_text(text)
    print(f"patched {target}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
