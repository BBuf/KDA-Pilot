#!/usr/bin/env python3
"""NCU harness: select01 production shape (B=1, L=8424, C=3072, bf16, int32 index).

Runs the vendored Triton baseline kernel and the native CUDA kernel a few
times each so one ncu session captures both for side-by-side analysis.
Shape matches docs/captured_shapes_h200.jsonl row prod07 exactly.

Usage (inside the container, idle GPU):
  KDA_LINEINFO=1 ncu --set full --target-processes all -o reports/full \
      python profile/select01_v2/harness/profile_select01.py
"""

from __future__ import annotations

import sys
from pathlib import Path

KERNEL_DIR = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(KERNEL_DIR))

import torch  # noqa: E402

from baseline import scale_shift as base  # noqa: E402
from solution import dispatch  # noqa: E402

REPS = 5


def main() -> None:
    torch.manual_seed(0)
    device = torch.device("cuda")
    B, L, C = 1, 8424, 3072
    dt = torch.bfloat16
    x = torch.randn(B, L, C, device=device, dtype=dt)
    mods = [torch.randn(B, C, device=device, dtype=dt) for _ in range(6)]
    index = torch.randint(0, 2, (B, L), device=device, dtype=torch.int32)
    eps = 1e-6

    # Warmup both paths (compiles excluded from profiling via --launch-skip
    # or simply by ncu profiling every launch; reps stay small).
    for _ in range(3):
        base.fuse_layernorm_scale_shift_gate_select01_kernel(x, None, None, *mods, index, eps)
        dispatch.fuse_layernorm_scale_shift_gate_select01_kernel(x, None, None, *mods, index, eps)
    torch.cuda.synchronize()

    for _ in range(REPS):
        base.fuse_layernorm_scale_shift_gate_select01_kernel(x, None, None, *mods, index, eps)
    torch.cuda.synchronize()
    for _ in range(REPS):
        out = dispatch.fuse_layernorm_scale_shift_gate_select01_kernel(
            x, None, None, *mods, index, eps
        )
    torch.cuda.synchronize()
    route = dispatch.consume_last_route()
    assert route and route[0] == "native", route
    print("done; native route:", route, "out:", tuple(out[0].shape))


if __name__ == "__main__":
    main()
