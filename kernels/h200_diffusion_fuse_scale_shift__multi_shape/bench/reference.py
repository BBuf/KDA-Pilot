"""Pure-PyTorch FP32 references and output comparators.

The references mirror the SGLang baseline semantics (see docs/baseline_source.md)
but compute everything in float32. They serve as the independent oracle for the
dynamic-tolerance cross-check: the candidate's error against the FP32 reference
must not exceed a small multiple of the baseline's own quantization noise.
"""

from __future__ import annotations

import torch
import torch.nn.functional as F

# Fixed tolerances copied from the SGLang oracle test
# (python/sglang/jit_kernel/tests/diffusion/test_qwen_image_modulation.py).
def fixed_tol(dtype: torch.dtype) -> tuple[float, float]:
    if dtype == torch.float32:
        return 1e-5, 1e-5
    return 5e-2, 5e-2


# Dynamic cross-check: max|cand - ref32| <= DYN_MULT * max|base - ref32| + floor.
DYN_MULT = 2.0
DYN_FLOOR = {
    torch.float32: 5e-5,
    torch.float16: 1e-3,
    torch.bfloat16: 1e-3,
}


def _f32(t: torch.Tensor) -> torch.Tensor:
    return t.to(torch.float32)


def _resolve_scale_shift_fp32(
    x: torch.Tensor, scale: torch.Tensor, shift: torch.Tensor
) -> tuple[torch.Tensor, torch.Tensor]:
    """Replicate the baseline wrapper's broadcast resolution, in fp32."""
    B, L, C = x.shape

    if scale.dim() == 4:
        # scale: (B, F, 1, C) per-frame; shift must be per-token (B, L, C)-reshapeable.
        num_frames = scale.shape[1]
        if L % num_frames != 0:
            raise AssertionError("seq_len must be divisible by num_frames")
        frame_seqlen = L // num_frames
        scale32 = (
            _f32(scale).squeeze(2).repeat_interleave(frame_seqlen, dim=1)
        )  # (B, L, C)
        shift32 = _f32(shift).reshape(B * L, C).view(B, L, C)
        return scale32.expand(B, L, C), shift32

    def _to_blc(t: torch.Tensor) -> torch.Tensor:
        if t.dim() == 0 or (t.dim() == 1 and t.numel() == 1):
            return _f32(t).reshape(1, 1, 1).expand(B, L, C)
        if t.dim() == 2:
            return _f32(t)[:, None, :].expand(B, L, C)
        if t.dim() == 3:
            return _f32(t).expand(B, L, C)
        raise ValueError("scale/shift must be 0D/1D(1)/2D/3D or 4D")

    return _to_blc(scale), _to_blc(shift)


def ref_fuse_scale_shift(
    x: torch.Tensor,
    scale: torch.Tensor,
    shift: torch.Tensor,
    scale_constant: float = 1.0,
) -> torch.Tensor:
    """FP32 reference for fuse_scale_shift_kernel: y = x * (c + scale) + shift."""
    scale32, shift32 = _resolve_scale_shift_fp32(x, scale, shift)
    return _f32(x) * (float(scale_constant) + scale32) + shift32


def _ref_select01_epilogue(
    normalized32: torch.Tensor,
    scale0: torch.Tensor,
    shift0: torch.Tensor,
    gate0: torch.Tensor,
    scale1: torch.Tensor,
    shift1: torch.Tensor,
    gate1: torch.Tensor,
    index: torch.Tensor,
) -> tuple[torch.Tensor, torch.Tensor]:
    idx = index.bool().unsqueeze(-1)  # (B, L, 1); nonzero selects set 1
    scale = torch.where(idx, _f32(scale1).unsqueeze(1), _f32(scale0).unsqueeze(1))
    shift = torch.where(idx, _f32(shift1).unsqueeze(1), _f32(shift0).unsqueeze(1))
    gate = torch.where(idx, _f32(gate1).unsqueeze(1), _f32(gate0).unsqueeze(1))
    return normalized32 * (1.0 + scale) + shift, gate


def _layer_norm32(
    x32: torch.Tensor,
    weight: torch.Tensor | None,
    bias: torch.Tensor | None,
    eps: float,
) -> torch.Tensor:
    C = x32.shape[-1]
    return F.layer_norm(
        x32,
        (C,),
        weight=_f32(weight) if weight is not None else None,
        bias=_f32(bias) if bias is not None else None,
        eps=eps,
    )


def ref_layernorm_select01(
    x: torch.Tensor,
    weight: torch.Tensor | None,
    bias: torch.Tensor | None,
    scale0: torch.Tensor,
    shift0: torch.Tensor,
    gate0: torch.Tensor,
    scale1: torch.Tensor,
    shift1: torch.Tensor,
    gate1: torch.Tensor,
    index: torch.Tensor,
    eps: float,
) -> tuple[torch.Tensor, torch.Tensor]:
    normalized32 = _layer_norm32(_f32(x), weight, bias, eps)
    return _ref_select01_epilogue(
        normalized32, scale0, shift0, gate0, scale1, shift1, gate1, index
    )


def ref_residual_layernorm_select01(
    x: torch.Tensor,
    residual: torch.Tensor,
    residual_gate: torch.Tensor,
    weight: torch.Tensor | None,
    bias: torch.Tensor | None,
    scale0: torch.Tensor,
    shift0: torch.Tensor,
    gate0: torch.Tensor,
    scale1: torch.Tensor,
    shift1: torch.Tensor,
    gate1: torch.Tensor,
    index: torch.Tensor,
    eps: float,
) -> tuple[torch.Tensor, torch.Tensor, torch.Tensor]:
    residual_out32 = _f32(residual) + _f32(residual_gate) * _f32(x)
    normalized32 = _layer_norm32(residual_out32, weight, bias, eps)
    out32, gate32 = _ref_select01_epilogue(
        normalized32, scale0, shift0, gate0, scale1, shift1, gate1, index
    )
    return out32, residual_out32, gate32


class ToleranceError(AssertionError):
    pass


def check_outputs(
    name: str,
    candidate: torch.Tensor,
    baseline: torch.Tensor,
    ref32: torch.Tensor,
    dtype: torch.dtype,
    tol_override: tuple | None = None,
) -> dict:
    """All-in-one validator for one output tensor.

    1. NaN/Inf guards on candidate (and sanity on baseline/ref32).
    2. Fixed tolerance: candidate vs baseline at the oracle's atol/rtol.
    3. Dynamic cross-check: candidate error vs FP32 reference bounded by a small
       multiple of the baseline's own error vs the same reference.
    Returns a metrics dict for the report; raises ToleranceError on failure.
    """
    if not torch.isfinite(candidate).all():
        raise ToleranceError(f"{name}: candidate contains NaN/Inf")
    if not torch.isfinite(baseline).all():
        raise ToleranceError(f"{name}: baseline contains NaN/Inf (invalid case)")
    if not torch.isfinite(ref32).all():
        raise ToleranceError(f"{name}: fp32 reference contains NaN/Inf (invalid case)")
    if candidate.shape != baseline.shape or candidate.dtype != baseline.dtype:
        raise ToleranceError(
            f"{name}: shape/dtype mismatch candidate={tuple(candidate.shape)}/{candidate.dtype} "
            f"baseline={tuple(baseline.shape)}/{baseline.dtype}"
        )

    atol, rtol = tol_override if tol_override is not None else fixed_tol(dtype)
    try:
        torch.testing.assert_close(candidate, baseline, atol=atol, rtol=rtol)
    except AssertionError as exc:
        raise ToleranceError(f"{name}: fixed-tolerance check failed: {exc}") from exc

    err_cand = (candidate.to(torch.float32) - ref32).abs().max().item()
    err_base = (baseline.to(torch.float32) - ref32).abs().max().item()
    budget = DYN_MULT * err_base + DYN_FLOOR[dtype]
    if err_cand > budget:
        raise ToleranceError(
            f"{name}: dynamic-tolerance check failed: candidate max|err|={err_cand:.3e} "
            f"exceeds {DYN_MULT}*baseline({err_base:.3e}) + floor({DYN_FLOOR[dtype]:.0e}) = {budget:.3e}"
        )
    return {"output": name, "err_cand": err_cand, "err_base": err_base, "budget": budget}
