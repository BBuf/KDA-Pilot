"""Correctness harness for ``h200_diffusion_rotary_embedding__multi_shape``.

Gated by ``KDA_RUN_CORRECTNESS=1`` (needs CUDA + an importable SGLang). Run on the
remote H200 inside the ``sglang_bbuf`` container, e.g.::

    KDA_RUN_CORRECTNESS=1 pytest tests/test_correctness.py -v

Oracle design (the named ``test_rope.py`` exercises a *different* API --
``apply_rope_inplace`` / FlashInfer -- so it is not a literal oracle here):

* Semantic oracle: the SGLang diffusion triton baselines pinned at SGLang
  HEAD ``6965fe0ee``:
    - ``sglang.jit_kernel.diffusion.triton.rotary.apply_rotary_embedding``
    - ``sglang.jit_kernel.diffusion.triton.ltx2_rotary.apply_ltx2_split_rotary_emb``
* Independent cross-check: a PyTorch FP32 reference that reproduces each kernel's
  exact numerics -- standard is adjacent-pair with rounding only on the final
  store; LTX-2 is split-half with a deliberate intermediate ``(x*cos)->bf16``
  rounding before the FP32 ``sin`` term, indexed through the *non-contiguous*
  4D ``(B, num_heads, S, half_dim)`` cos/sin tables.

Workload = the 6 deduplicated production shapes (1 hunyuanvideo standard + 5
LTX-2). The standard hunyuanvideo row appears twice in the captured table; it is
counted once here.
"""

from __future__ import annotations

import importlib.util
import os
from pathlib import Path
from typing import Any

import pytest

try:
    import torch
except ImportError:  # pragma: no cover - CUDA env owns the real run
    torch = None


KERNEL_SLUG = "h200_diffusion_rotary_embedding__multi_shape"
OP_TYPE = "rotary_embedding"
KERNEL_DIR = Path(__file__).resolve().parents[1]
DEVICE = "cuda"

# Oracle provenance: the SGLang checkout the baseline numerics are pinned to.
SGLANG_ORACLE_COMMIT = "6965fe0ee"

pytestmark = pytest.mark.skipif(
    os.environ.get("KDA_RUN_CORRECTNESS") != "1",
    reason="Set KDA_RUN_CORRECTNESS=1 on the remote H200 (CUDA + SGLang) to run.",
)


# ---------------------------------------------------------------------------
# Module loading
# ---------------------------------------------------------------------------
def _load_register_module():
    register_py = KERNEL_DIR / "src" / "register.py"
    spec = importlib.util.spec_from_file_location(
        f"kda_kernel_{KERNEL_SLUG}_register", register_py
    )
    assert spec is not None and spec.loader is not None, register_py
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


# ---------------------------------------------------------------------------
# PyTorch FP32 references (mirror the exact SGLang triton numerics)
# ---------------------------------------------------------------------------
def std_rope_ref_fp32(x: "torch.Tensor", cos: "torch.Tensor", sin: "torch.Tensor") -> "torch.Tensor":
    """Adjacent-pair RoPE reference for ``apply_rotary_embedding`` (interleaved=False).

    ``x``: (B,T,H,D) or (T,H,D); ``cos``/``sin``: fp32 contiguous (T, D//2),
    shared across heads/batches via ``bt % T``. Rounding to the input dtype
    happens only on the (caller's) final store; this returns fp32.
    """
    orig_shape = x.shape
    if x.dim() == 4:
        B, T, H, D = x.shape
    else:
        T, H, D = x.shape
        B = 1
    assert D % 2 == 0, "head_size must be even"
    assert cos.shape == sin.shape == (T, D // 2), (cos.shape, sin.shape, (T, D // 2))

    xv = x.reshape(B * T, H, D).float()
    pos = torch.arange(B * T, device=x.device) % T
    c = cos.index_select(0, pos).float().view(B * T, 1, D // 2)
    s = sin.index_select(0, pos).float().view(B * T, 1, D // 2)

    x1 = xv[..., 0::2]
    x2 = xv[..., 1::2]

    out = torch.empty_like(xv)
    out[..., 0::2] = x1 * c - x2 * s
    out[..., 1::2] = x1 * s + x2 * c
    return out.reshape(orig_shape)


def ltx2_rope_ref_fp32(x: "torch.Tensor", cos: "torch.Tensor", sin: "torch.Tensor") -> "torch.Tensor":
    """Split-half RoPE reference for ``apply_ltx2_split_rotary_emb``.

    ``x``: (B,S,H*2*half) bf16; ``cos``/``sin``: (B,H,S,half) bf16, possibly
    non-contiguous. Reproduces the deliberate intermediate ``(x*cos)->bf16``
    rounding before adding the FP32 ``sin`` term. Returns fp32.
    """
    B, S, inner = x.shape
    CB, H, CS, half = cos.shape
    assert (CB, CS) == (B, S), (cos.shape, (B, S))
    assert sin.shape == cos.shape, (sin.shape, cos.shape)
    D = half * 2
    assert inner == H * D, (inner, H * D)

    xv = x.view(B, S, H, D)
    x_first = xv[..., :half].float()
    x_second = xv[..., half:].float()

    c = cos.permute(0, 2, 1, 3).float()  # (B,S,H,half)
    s = sin.permute(0, 2, 1, 3).float()

    first_cos = (x_first * c).to(torch.bfloat16).float()
    second_cos = (x_second * c).to(torch.bfloat16).float()

    out = torch.empty((B, S, H, D), device=x.device, dtype=torch.float32)
    out[..., :half] = first_cos - x_second * s
    out[..., half:] = second_cos + x_first * s
    return out.reshape_as(x)


# ---------------------------------------------------------------------------
# Input builders (deterministic; LTX-2 cos/sin are intentionally non-contiguous)
# ---------------------------------------------------------------------------
def _build_standard_inputs(B: int, T: int, H: int, D: int, dtype, *, seed: int):
    g = torch.Generator(device=DEVICE).manual_seed(seed)
    x = torch.randn(B, T, H, D, device=DEVICE, dtype=torch.float32, generator=g).to(dtype)
    angles = torch.randn(T, D // 2, device=DEVICE, dtype=torch.float32, generator=g)
    cos = torch.cos(angles).contiguous()  # fp32 (T, D//2)
    sin = torch.sin(angles).contiguous()
    return (x, cos, sin), {"interleaved": False}


def _build_ltx2_inputs(B: int, S: int, H: int, half: int, dtype, *, seed: int):
    g = torch.Generator(device=DEVICE).manual_seed(seed)
    D = half * 2
    x = (torch.randn(B, S, H * D, device=DEVICE, dtype=torch.float32, generator=g) * 1e-1).to(dtype)
    angles = torch.randn(B, S, H, half, device=DEVICE, dtype=torch.float32, generator=g)
    cos_base = torch.cos(angles).to(dtype).contiguous()  # (B,S,H,half)
    sin_base = torch.sin(angles).to(dtype).contiguous()
    cos = cos_base.permute(0, 2, 1, 3)  # (B,H,S,half) -> non-contiguous strided view
    sin = sin_base.permute(0, 2, 1, 3)
    assert not cos.is_contiguous() and not sin.is_contiguous(), "LTX-2 cos/sin must be non-contiguous"
    return (x, cos, sin), {}


# ---------------------------------------------------------------------------
# Cases: the 6 deduplicated production shapes
# ---------------------------------------------------------------------------
def make_cases() -> list[dict[str, Any]]:
    """Return all configured correctness/benchmark cases (6 unique shapes).

    Tensors are materialized once so ``benchmark.py`` times only the kernel call.
    """
    if torch is None:
        return []

    cases: list[dict[str, Any]] = []

    # Standard apply_rotary_embedding -- hunyuanvideo (appears twice in the
    # captured table; counted once).
    args, kwargs = _build_standard_inputs(1, 27030, 24, 128, torch.bfloat16, seed=0)
    cases.append(
        {
            "name": "hunyuanvideo__std__B1_T27030_H24_D128__bf16",
            "api": "standard",
            "args": args,
            "kwargs": kwargs,
            "atol": 1e-2,
            "rtol": 1e-2,
            "warmup": 25,
            "iters": 100,
        }
    )

    # LTX-2 apply_ltx2_split_rotary_emb -- (B=1, num_heads=32).
    ltx2_specs = [
        ("ltx2__B1_S1536_H32_half64__bf16", 1, 1536, 32, 64),
        ("ltx2__B1_S126_H32_half32__bf16", 1, 126, 32, 32),
        ("ltx2__B1_S1536_H32_half32__bf16", 1, 1536, 32, 32),
        ("ltx2__B1_S6144_H32_half64__bf16", 1, 6144, 32, 64),
        ("ltx2__B1_S6144_H32_half32__bf16", 1, 6144, 32, 32),
    ]
    for i, (name, B, S, H, half) in enumerate(ltx2_specs, start=1):
        args, kwargs = _build_ltx2_inputs(B, S, H, half, torch.bfloat16, seed=i)
        cases.append(
            {
                "name": name,
                "api": "ltx2",
                "args": args,
                "kwargs": kwargs,
                "atol": 1e-2,
                "rtol": 1e-2,
                "warmup": 25,
                "iters": 100,
            }
        )

    return cases


# ---------------------------------------------------------------------------
# Oracle / reference / candidate
# ---------------------------------------------------------------------------
def baseline(case: dict[str, Any]) -> Any:
    """SGLang diffusion triton baseline -- the semantic oracle."""
    args = case["args"]
    kwargs = case.get("kwargs", {})
    if case["api"] == "standard":
        from sglang.jit_kernel.diffusion.triton.rotary import apply_rotary_embedding

        return apply_rotary_embedding(*args, **kwargs)
    if case["api"] == "ltx2":
        from sglang.jit_kernel.diffusion.triton.ltx2_rotary import (
            apply_ltx2_split_rotary_emb,
        )

        return apply_ltx2_split_rotary_emb(*args, **kwargs)
    raise ValueError(f"unknown api {case['api']!r}")


def reference(case: dict[str, Any]) -> Any:
    """Independent PyTorch FP32 reference."""
    x, cos, sin = case["args"][0], case["args"][1], case["args"][2]
    if case["api"] == "standard":
        return std_rope_ref_fp32(x, cos, sin)
    if case["api"] == "ltx2":
        return ltx2_rope_ref_fp32(x, cos, sin)
    raise ValueError(f"unknown api {case['api']!r}")


def candidate(case: dict[str, Any]) -> Any:
    module = _load_register_module()
    wrapper = getattr(module, "optimized_wrapper")
    args = case.get("args", ())
    kwargs = case.get("kwargs", {})
    return wrapper(*args, **kwargs)


# ---------------------------------------------------------------------------
# Assertions
# ---------------------------------------------------------------------------
def _assert_no_nan_inf(value: Any, *, path: str) -> None:
    if torch is not None and isinstance(value, torch.Tensor):
        assert not torch.isnan(value).any(), f"{path} contains NaN"
        assert not torch.isinf(value).any(), f"{path} contains Inf"
    elif isinstance(value, (tuple, list)):
        for i, item in enumerate(value):
            _assert_no_nan_inf(item, path=f"{path}[{i}]")
    elif isinstance(value, dict):
        for key, item in value.items():
            _assert_no_nan_inf(item, path=f"{path}.{key}")


def _assert_close(actual: Any, expected: Any, *, case: dict[str, Any], path: str = "out") -> None:
    atol = case.get("atol", 1e-2)
    rtol = case.get("rtol", 1e-2)
    _assert_no_nan_inf(actual, path=path)
    assert isinstance(actual, torch.Tensor) and isinstance(expected, torch.Tensor), (
        f"{path}: expected tensors, got {type(actual)} vs {type(expected)}"
    )
    assert actual.shape == expected.shape, f"{path} shape {actual.shape} != {expected.shape}"
    torch.testing.assert_close(actual.float(), expected.float(), atol=atol, rtol=rtol)


def assert_bf16_noise_bounded(
    actual: "torch.Tensor", ref_fp32: "torch.Tensor", *, mult: float = 3.0, floor: float = 1e-6
) -> None:
    """Sharp check: candidate error vs the FP32 reference must stay within a small
    multiple of the reference's own bf16 quantization noise. Catches a candidate
    that, e.g., skips the LTX-2 intermediate bf16 rounding."""
    a = actual.float()
    ref_bf16 = ref_fp32.to(torch.bfloat16).float()
    err = (a - ref_fp32).abs()
    noise = (ref_bf16 - ref_fp32).abs()

    err_rms = torch.sqrt(torch.mean(err.square()))
    noise_rms = torch.sqrt(torch.mean(noise.square()))

    assert err.max().item() <= mult * noise.max().clamp_min(floor).item() + floor, (
        f"max abs error {err.max().item():.3e} exceeds {mult}x bf16 noise "
        f"{noise.max().item():.3e}"
    )
    assert err_rms.item() <= mult * noise_rms.clamp_min(floor).item() + floor, (
        f"rms error {err_rms.item():.3e} exceeds {mult}x bf16 rms noise {noise_rms.item():.3e}"
    )


# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------
def test_register_metadata() -> None:
    module = _load_register_module()
    assert hasattr(module, "register")
    spec = module.register()
    assert spec["name"] == KERNEL_SLUG
    assert spec["op_type"] == OP_TYPE
    assert callable(spec["callable"])


def test_baseline_matches_reference() -> None:
    """Validate the oracle itself: SGLang baseline must match the FP32 reference
    within bf16 noise. Independent of the candidate (passes before the kernel
    exists), so it locks the recovered numeric contract."""
    cases = make_cases()
    assert cases, "No cases. Fill make_cases()."
    for case in cases:
        base = baseline(case)
        ref = reference(case)
        _assert_no_nan_inf(base, path=case["name"] + ":baseline")
        assert_bf16_noise_bounded(base, ref, mult=3.0)


def test_correctness_cases() -> None:
    cases = make_cases()
    assert cases, "No correctness cases recovered. Fill make_cases() before optimizing."
    for case in cases:
        x = case["args"][0]
        x_before = x.clone()

        base = baseline(case)
        ref = reference(case)
        cand = candidate(case)

        # Functional contract: neither baseline nor candidate mutates the input.
        assert torch.equal(x, x_before), f"{case['name']}: input x was mutated (functional contract)"

        _assert_no_nan_inf(cand, path=case["name"] + ":candidate")
        # Primary oracle comparison: candidate vs SGLang baseline.
        _assert_close(cand, base, case=case, path=case["name"])
        # Sharp cross-check: candidate within bf16 noise of the FP32 reference.
        assert_bf16_noise_bounded(cand, ref, mult=3.0)


if __name__ == "__main__":
    import sys

    sys.exit(pytest.main([__file__, "-v", "-s"]))
