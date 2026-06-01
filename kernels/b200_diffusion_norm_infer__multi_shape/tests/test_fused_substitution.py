"""Fused-modulation oracle (AC-C / task7) — full coverage.

Substitute the optimized candidate for ``norm_infer`` in the reference paths of
``test_qwen_image_modulation.py`` (the Z-Image/Qwen-Image select01 dual-modulation
baseline) and confirm the SGLang fused kernels still match. Covers BOTH the
``select01`` and the ``residual`` select01 paths, over the SGLang CI grid (batch,
seq, hidden) plus fp32 (which the CI dtype set omits but which exercises the CUDA
LayerNorm). fp16/bf16 fall back to the baseline, so the substitution is a no-op and
the original oracle relation holds; fp32 routes (M=B*S, hidden) through the CUDA
kernel via the configured-shape allowlist.

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

_REG = None


def _register():
    global _REG
    if _REG is None:
        spec = importlib.util.spec_from_file_location("kda_reg_fused", KERNEL_DIR / "src" / "register.py")
        _REG = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(_REG)
    return _REG


def _tol(dt):
    return (1e-5, 1e-5) if dt == torch.float32 else (5e-2, 5e-2)


# Grid mirrors SGLang's test_qwen_image_modulation CI ranges (batch/seq/hidden),
# plus fp32 to exercise the CUDA LayerNorm. M=B*S in {6,12,128,256}, hidden in
# {512,3072} are all in register._SUPPORTED_LN, so fp32 routes to CUDA.
@pytest.mark.parametrize("path", ["select01", "residual"])
@pytest.mark.parametrize("dtype", ["fp32", "bf16", "fp16"])
@pytest.mark.parametrize("batch", [1, 2])
@pytest.mark.parametrize("seq", [6, 128])
@pytest.mark.parametrize("hidden", [512, 3072])
def test_fused_substitution(path, dtype, batch, seq, hidden):
    import triton
    import sglang.jit_kernel.tests.diffusion.test_qwen_image_modulation as T
    from sglang.jit_kernel.diffusion.triton.scale_shift import (
        fuse_layernorm_scale_shift_gate_select01_kernel,
        fuse_residual_layernorm_scale_shift_gate_select01_kernel,
    )

    reg = _register()
    dt = {"fp32": torch.float32, "bf16": torch.bfloat16, "fp16": torch.float16}[dtype]
    atol, rtol = _tol(dt)
    torch.cuda.manual_seed(0)
    x = torch.randn(batch, seq, hidden, device="cuda", dtype=dt)
    weight = torch.randn(hidden, device="cuda", dtype=dt)
    bias = torch.randn(hidden, device="cuda", dtype=dt)
    index = torch.randint(0, 2, (batch, seq), device="cuda", dtype=torch.int32)
    mod = T._make_modulation_tensors(batch, hidden, dt)

    def with_substituted(fn):
        saved = T.norm_infer
        T.norm_infer = lambda *a, **k: reg.optimized_norm_infer(*a, **k)
        try:
            return fn()
        finally:
            T.norm_infer = saved

    if path == "select01":
        out_orig, gate_orig = T._baseline_select01_modulation(x, weight, bias, *mod, index, T.EPS)
        out_cand, gate_cand = with_substituted(
            lambda: T._baseline_select01_modulation(x, weight, bias, *mod, index, T.EPS)
        )
        out_fused, gate_fused = fuse_layernorm_scale_shift_gate_select01_kernel(
            x.contiguous(), weight=weight, bias=bias,
            scale0=mod[0], shift0=mod[1], gate0=mod[2],
            scale1=mod[3], shift1=mod[4], gate1=mod[5], index=index, eps=T.EPS,
        )
        triton.testing.assert_close(out_cand, out_fused, atol=atol, rtol=rtol)
        triton.testing.assert_close(gate_cand, gate_fused, atol=atol, rtol=rtol)
        triton.testing.assert_close(out_cand, out_orig, atol=atol, rtol=rtol)  # drop-in equivalence
    else:
        residual = torch.randn_like(x)
        residual_gate = torch.randn_like(x)
        out_orig, res_orig, gate_orig = T._baseline_residual_select01_modulation(
            x, residual, residual_gate, weight, bias, *mod, index, T.EPS
        )
        out_cand, res_cand, gate_cand = with_substituted(
            lambda: T._baseline_residual_select01_modulation(
                x, residual, residual_gate, weight, bias, *mod, index, T.EPS
            )
        )
        out_fused, res_fused, gate_fused = fuse_residual_layernorm_scale_shift_gate_select01_kernel(
            x.contiguous(), residual=residual.contiguous(), residual_gate=residual_gate.contiguous(),
            weight=weight, bias=bias,
            scale0=mod[0], shift0=mod[1], gate0=mod[2],
            scale1=mod[3], shift1=mod[4], gate1=mod[5], index=index, eps=T.EPS,
        )
        triton.testing.assert_close(out_cand, out_fused, atol=atol, rtol=rtol)
        triton.testing.assert_close(res_cand, res_fused, atol=atol, rtol=rtol)
        triton.testing.assert_close(gate_cand, gate_fused, atol=atol, rtol=rtol)
        triton.testing.assert_close(out_cand, out_orig, atol=atol, rtol=rtol)  # drop-in equivalence
