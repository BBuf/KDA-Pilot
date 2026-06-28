#!/usr/bin/env python3
"""NCU profiling driver for the candidate's fused modulation kernel (task12).

Runs `ltx2_rms_adaln_candidate` on a given `[B,S,D]` shape so Nsight Compute can
capture `rms_adaln_modulation_kernel`. Usage:
    CUDA_VISIBLE_DEVICES=<id> ncu -k regex:rms_adaln_modulation ... \
        python3 bench/profile_one.py B S D
No sglang import.
"""

from __future__ import annotations

import pathlib
import sys

import torch

_TASK = pathlib.Path(__file__).resolve().parents[1]
if str(_TASK) not in sys.path:
    sys.path.insert(0, str(_TASK))

import bench.adapter as adapter  # builds + loads the candidate module


def main() -> int:
    B, S, D = (int(a) for a in sys.argv[1:4])
    dev = torch.device("cuda:0")
    torch.cuda.set_device(dev)
    torch.set_grad_enabled(False)
    torch.manual_seed(1234)
    x = torch.randn(B, S, D, device=dev, dtype=torch.bfloat16)
    scale = torch.randn(B, S, D, device=dev, dtype=torch.bfloat16)
    shift = torch.randn(B, S, D, device=dev, dtype=torch.bfloat16)
    out = [torch.empty_like(x)]
    wl = {"function": "rms_adaln"}
    inp = {"x": x, "scale": scale, "shift": shift, "eps": 1e-6}
    for _ in range(5):  # warmup
        adapter.call_candidate(wl, inp, out)
    torch.cuda.synchronize()
    for _ in range(3):  # profiled launches
        adapter.call_candidate(wl, inp, out)
    torch.cuda.synchronize()
    return 0


if __name__ == "__main__":
    sys.exit(main())
