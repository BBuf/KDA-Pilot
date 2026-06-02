#!/usr/bin/env python3
"""Persisted call-path decomposition (Round 4 finding, BL-20260602-candidate-bypasses-custom-op-asymmetry).

For each given shape, times three paths with CUDA events to attribute overhead:
  1. baseline custom-op  : sglang fused_inplace_qknorm_rope (register_custom_op wrapper)
  2. baseline direct module : _jit_qknorm_rope_module(...).qknorm_rope(...)   (no custom op)
  3. candidate direct module : src/register optimized_wrapper path (KDA_CAND_VARIANT)

(1)-(2) = register_custom_op overhead; (2) vs (3) = device-fair candidate-vs-baseline.
Run from the kernel folder on the B200 box:
  CUDA_VISIBLE_DEVICES=<idle> KDA_CAND_VARIANT=staged PYTHONPATH=. python profile/decompose.py
"""

import importlib.util
import os
import statistics
import sys
from pathlib import Path

import torch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from tests.test_correctness import _make_inputs, make_cases  # noqa: E402

from sglang.jit_kernel.diffusion.qknorm_rope import (  # noqa: E402
    _jit_qknorm_rope_module,
    fused_inplace_qknorm_rope,
)

_spec = importlib.util.spec_from_file_location("kda_reg", ROOT / "src" / "register.py")
_reg = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_reg)

VARIANT = os.environ.get("KDA_CAND_VARIANT", "staged")
SHAPES = sys.argv[1:] or ["qwen__small__B19_H24_D128_R128", "qwen-edit__large__B8424_H24_D128_R128"]


def t(fn, warmup=20, iters=100):
    for _ in range(warmup):
        fn()
    torch.cuda.synchronize()
    s = []
    for _ in range(iters):
        a = torch.cuda.Event(enable_timing=True)
        b = torch.cuda.Event(enable_timing=True)
        a.record()
        fn()
        b.record()
        torch.cuda.synchronize()
        s.append(a.elapsed_time(b) * 1e3)
    return statistics.median(s)


def main():
    cases = {c["name"]: c for c in make_cases()}
    print(f"variant={VARIANT} gpu={torch.cuda.get_device_name(0)} CVD={os.environ.get('CUDA_VISIBLE_DEVICES')}")
    for name in SHAPES:
        case = cases[name]
        inp = _make_inputs(case)

        def cust():
            fused_inplace_qknorm_rope(inp["q"], inp["k"], inp["q_weight"], inp["k_weight"],
                                      inp["cos_sin_cache"], inp["positions"],
                                      is_neox=case["is_neox"], eps=case["eps"], rope_dim=case["rope_dim"])

        mod = _jit_qknorm_rope_module(case["head_dim"], case["rope_dim"], case["is_neox"], torch.bfloat16)

        def base_direct():
            mod.qknorm_rope(inp["q"], inp["k"], inp["q_weight"], inp["k_weight"],
                            inp["cos_sin_cache"], inp["positions"], case["eps"])

        def cand():
            _reg.optimized_wrapper(inp["q"], inp["k"], inp["q_weight"], inp["k_weight"],
                                   inp["cos_sin_cache"], inp["positions"],
                                   is_neox=case["is_neox"], eps=case["eps"],
                                   head_dim=case["head_dim"], rope_dim=case["rope_dim"])

        c1, c2, c3 = t(cust), t(base_direct), t(cand)
        print(f"\n{name}")
        print(f"  baseline custom-op      : {c1:7.2f} us")
        print(f"  baseline DIRECT module  : {c2:7.2f} us")
        print(f"  candidate ({VARIANT}) DIRECT : {c3:7.2f} us")
        print(f"  custom-op overhead      : {c1 - c2:7.2f} us   |  device-fair cand-vs-baseline: {c2 / c3:.4f}x")


if __name__ == "__main__":
    main()
