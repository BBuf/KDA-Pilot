"""Fused-modulation oracle (AC-C / task7).

Substitute the optimized candidate for ``norm_infer`` in the reference path of
``test_qwen_image_modulation.py`` (the Z-Image/Qwen-Image select01 dual-modulation
baseline) and confirm the SGLang fused kernel still matches. fp32 exercises the
CUDA LayerNorm (set ``KDA_REQUIRE_CUDA=1``); bf16 falls back to the baseline, so
the substitution is a no-op there and the original oracle relation holds.

Run on the remote B200 inside ``sglang_bbuf``:
  CUDA_VISIBLE_DEVICES=<id> KDA_RUN_CORRECTNESS=1 KDA_REQUIRE_CUDA=1 \
    python -m pytest -q tests/test_fused_substitution.py
"""

from __future__ import annotations

import importlib.util
import os
from pathlib import Path

import pytest

try:
    import torch
except ImportError:  # pragma: no cover
    torch = None

KERNEL_DIR = Path(__file__).resolve().parents[1]

pytestmark = pytest.mark.skipif(
    os.environ.get("KDA_RUN_CORRECTNESS") != "1",
    reason="Set KDA_RUN_CORRECTNESS=1 (remote B200) to run the fused oracle.",
)


def _load_register():
    spec = importlib.util.spec_from_file_location("kda_reg_fused", KERNEL_DIR / "src" / "register.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def _tol(dt):
    return (1e-5, 1e-5) if dt == torch.float32 else (5e-2, 5e-2)


@pytest.mark.parametrize("dtype", ["fp32", "bf16"])
@pytest.mark.parametrize("hidden", [512, 3072])
def test_fused_select01_substitution(dtype, hidden):
    import triton
    import sglang.jit_kernel.tests.diffusion.test_qwen_image_modulation as T
    from sglang.jit_kernel.diffusion.triton.scale_shift import (
        fuse_layernorm_scale_shift_gate_select01_kernel,
    )

    reg = _load_register()
    dt = {"fp32": torch.float32, "bf16": torch.bfloat16}[dtype]
    B, S = 2, 128
    torch.cuda.manual_seed(0)
    x = torch.randn(B, S, hidden, device="cuda", dtype=dt)
    weight = torch.randn(hidden, device="cuda", dtype=dt)
    bias = torch.randn(hidden, device="cuda", dtype=dt)
    index = torch.randint(0, 2, (B, S), device="cuda", dtype=torch.int32)
    mod = T._make_modulation_tensors(B, hidden, dt)

    # Reference with the original norm_infer.
    out_orig, gate_orig = T._baseline_select01_modulation(x, weight, bias, *mod, index, T.EPS)

    # Reference with the candidate substituted for norm_infer (module-global).
    saved = T.norm_infer
    T.norm_infer = lambda *a, **k: reg.optimized_norm_infer(*a, **k)
    try:
        out_cand, gate_cand = T._baseline_select01_modulation(x, weight, bias, *mod, index, T.EPS)
    finally:
        T.norm_infer = saved

    out_fused, gate_fused = fuse_layernorm_scale_shift_gate_select01_kernel(
        x.contiguous(), weight=weight, bias=bias,
        scale0=mod[0], shift0=mod[1], gate0=mod[2],
        scale1=mod[3], shift1=mod[4], gate1=mod[5],
        index=index, eps=T.EPS,
    )

    atol, rtol = _tol(dt)
    # Oracle: candidate-substituted reference matches the fused kernel.
    triton.testing.assert_close(out_cand, out_fused, atol=atol, rtol=rtol)
    triton.testing.assert_close(gate_cand, gate_fused, atol=atol, rtol=rtol)
    # Drop-in equivalence: substituting the candidate does not change the
    # reference vs the original norm_infer.
    triton.testing.assert_close(out_cand, out_orig, atol=atol, rtol=rtol)
