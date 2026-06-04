#!/usr/bin/env python3
"""Apply the in-tree native-routing patch to a TASK-OWNED sglang worktree.

Inserts a try-native block at the top of each public function in
python/sglang/jit_kernel/diffusion/triton/scale_shift.py (original Triton
bodies stay as the fallback), copies the device header into
python/sglang/jit_kernel/csrc/diffusion/, and installs the wrapper module.
Refuses to run if the target file does not match the pinned upstream md5
(the version the candidate was validated against).

Usage: python apply_patch.py <sglang_worktree_root> <kernel_workspace_root>
"""

from __future__ import annotations

import hashlib
import py_compile
import shutil
import sys
from pathlib import Path

PINNED_MD5 = "b4c069aca94ccb7b2bbea2d2571634a1"

IMPORT_ANCHOR = "from sglang.multimodal_gen.runtime.platforms import current_platform\n"
IMPORT_ADD = (
    IMPORT_ANCHOR
    + "\nfrom sglang.jit_kernel.diffusion import scale_shift_kda as _scale_shift_kda\n"
)

DEF_INSERTS = {
    "def fuse_scale_shift_kernel(": (
        "    _kda_out = _scale_shift_kda.try_native_fuse_scale_shift(\n"
        "        x, scale, shift, scale_constant\n"
        "    )\n"
        "    if _kda_out is not None:\n"
        "        return _kda_out\n"
    ),
    "def fuse_layernorm_scale_shift_gate_select01_kernel(": (
        "    _kda_out = _scale_shift_kda.try_native_layernorm_select01(\n"
        "        x, weight, bias, scale0, shift0, gate0, scale1, shift1, gate1, index, eps\n"
        "    )\n"
        "    if _kda_out is not None:\n"
        "        return _kda_out\n"
    ),
    "def fuse_residual_layernorm_scale_shift_gate_select01_kernel(": (
        "    _kda_out = _scale_shift_kda.try_native_residual_layernorm_select01(\n"
        "        x, residual, residual_gate, weight, bias,\n"
        "        scale0, shift0, gate0, scale1, shift1, gate1, index, eps\n"
        "    )\n"
        "    if _kda_out is not None:\n"
        "        return _kda_out\n"
    ),
}


def main() -> int:
    worktree = Path(sys.argv[1]).resolve()
    workspace = Path(sys.argv[2]).resolve()
    pkg = worktree / "python" / "sglang" / "jit_kernel"
    target = pkg / "diffusion" / "triton" / "scale_shift.py"

    text = target.read_text()
    md5 = hashlib.md5(text.encode()).hexdigest()
    if md5 != PINNED_MD5:
        print(f"REFUSING: {target} md5 {md5} != pinned {PINNED_MD5}", file=sys.stderr)
        return 1

    assert text.count(IMPORT_ANCHOR) == 1
    text = text.replace(IMPORT_ANCHOR, IMPORT_ADD, 1)

    for def_line, insert in DEF_INSERTS.items():
        pos = text.index(def_line)
        sig_end = text.index("):\n", pos) + len("):\n")
        text = text[:sig_end] + insert + text[sig_end:]

    target.write_text(text)
    py_compile.compile(str(target), doraise=True)

    cuh_src = workspace / "solution" / "scale_shift_kda.cuh"
    cuh_dst = pkg / "csrc" / "diffusion" / "scale_shift_kda.cuh"
    shutil.copyfile(cuh_src, cuh_dst)

    wrapper_src = workspace / "intree" / "scale_shift_kda.py"
    wrapper_dst = pkg / "diffusion" / "scale_shift_kda.py"
    shutil.copyfile(wrapper_src, wrapper_dst)
    py_compile.compile(str(wrapper_dst), doraise=True)

    print("patched:", target)
    print("installed:", cuh_dst)
    print("installed:", wrapper_dst)
    return 0


if __name__ == "__main__":
    sys.exit(main())
