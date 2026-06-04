"""Destination-passing launchers for the copied SGLang Triton baseline.

Each launcher is a faithful port of the upstream public wrapper in
``scale_shift_triton.py`` (SGLang main @ 133254086bf1f5b887c8c99d311719102d58a7eb)
with exactly one behavioral change, mirrored by the candidate ABI: output
tensors are provided by the caller (passed last) instead of being allocated
with ``torch.empty_like`` inside the call. Everything else — input validation,
broadcast normalization, expand/stride extraction, grid shapes, kernel
constants, the 4D ``.contiguous()`` reshapes, and the scalar-scalar zero fast
path (including its GPU->CPU sync) — matches the upstream wrapper so the
benchmark times the upstream implementation's real per-call cost.
"""

import torch
import triton  # type: ignore

from .scale_shift_triton import (
    _fused_layernorm_scale_shift_gate_select01_kernel,
    _fused_residual_layernorm_scale_shift_gate_select01_kernel,
    _fused_scale_shift_4d_kernel,
    fuse_scale_shift_kernel_blc_opt,
)


def fuse_scale_shift(
    x: torch.Tensor,
    scale: torch.Tensor,
    shift: torch.Tensor,
    scale_constant: float,
    output: torch.Tensor,
    block_l: int = 128,
    block_c: int = 128,
) -> None:
    assert (x.is_cuda and scale.is_cuda) or (x.is_xpu and scale.is_xpu)
    assert x.is_contiguous()
    assert output.shape == x.shape and output.dtype == x.dtype
    assert output.is_contiguous()

    B, L, C = x.shape
    if x.numel() == 0:
        return

    if scale.dim() == 4:
        # scale/shift: [B, F, 1, C]
        rows = B * L
        x_2d = x.view(rows, C)
        output_2d = output.view(rows, C)

        def grid(meta):
            return (rows, triton.cdiv(C, meta["BLOCK_N"]))

        num_frames = scale.shape[1]
        assert (
            L % num_frames == 0
        ), "seq_len must be divisible by num_frames for 4D scale/shift"
        frame_seqlen = L // num_frames

        # Compact scale [B, F, 1, C] -> [B*F, C] (per-frame)
        scale_reshaped = scale.squeeze(2).reshape(-1, C).contiguous()
        # shift is per-token [B, L, C] -> [B*L, C]
        shift_reshaped = shift.reshape(rows, C).contiguous()

        _fused_scale_shift_4d_kernel[grid](
            output_2d,
            x_2d,
            scale_reshaped,
            shift_reshaped,
            scale_constant,
            rows,
            C,
            L,
            num_frames,
            frame_seqlen,
        )
    else:
        # 2D: [B, C] or [1, C]  -> treat as [B, 1, C] and broadcast over L
        # 3D: [B, L, C] (or broadcastable variants like [B, 1, C], [1, L, C], [1, 1, C])
        # Also support scalar (0D or 1-element)
        if scale.dim() == 0 or (scale.dim() == 1 and scale.numel() == 1):
            scale_blc = scale.reshape(1)
        elif scale.dim() == 2:
            scale_blc = scale[:, None, :]
        elif scale.dim() == 3:
            scale_blc = scale
        else:
            raise ValueError("scale must be 0D/1D(1)/2D/3D or 4D")

        if shift.dim() == 0 or (shift.dim() == 1 and shift.numel() == 1):
            shift_blc = shift.reshape(1)
        elif shift.dim() == 2:
            shift_blc = shift[:, None, :]
        elif shift.dim() == 3:
            shift_blc = shift
        else:
            # broadcast later via expand if possible
            shift_blc = shift

        need_scale_scalar = scale_blc.dim() == 1 and scale_blc.numel() == 1
        need_shift_scalar = shift_blc.dim() == 1 and shift_blc.numel() == 1

        if not need_scale_scalar:
            scale_exp = scale_blc.expand(B, L, C)
            s_sb, s_sl, s_sc = scale_exp.stride()
        else:
            s_sb = s_sl = s_sc = 0

        if not need_shift_scalar:
            shift_exp = shift_blc.expand(B, L, C)
            sh_sb, sh_sl, sh_sc = shift_exp.stride()
        else:
            sh_sb = sh_sl = sh_sc = 0

        # If both scalars and both zero, copy fast-path
        if need_scale_scalar and need_shift_scalar:
            if not (
                scale_blc.any().to("cpu", non_blocking=True)
                or shift_blc.any().to("cpu", non_blocking=True)
            ):
                output.copy_(x)
                return

        grid = (triton.cdiv(L, block_l), triton.cdiv(C, block_c), B)
        fuse_scale_shift_kernel_blc_opt[grid](
            x,
            shift_blc if need_shift_scalar else shift_exp,
            scale_blc if need_scale_scalar else scale_exp,
            scale_constant,
            output,
            B,
            L,
            C,
            x.stride(0),
            x.stride(1),
            x.stride(2),
            sh_sb,
            sh_sl,
            sh_sc,
            s_sb,
            s_sl,
            s_sc,
            SCALE_IS_SCALAR=need_scale_scalar,
            SHIFT_IS_SCALAR=need_shift_scalar,
            BLOCK_L=block_l,
            BLOCK_C=block_c,
            num_warps=4,
            num_stages=2,
        )


def fuse_layernorm_scale_shift_gate_select01(
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
    output: torch.Tensor,
    gate_out: torch.Tensor,
) -> None:
    assert x.is_cuda
    assert x.is_contiguous()
    B, L, C = x.shape
    assert output.shape == x.shape and output.dtype == x.dtype
    assert gate_out.shape == x.shape and gate_out.dtype == x.dtype
    assert output.is_contiguous() and gate_out.is_contiguous()

    if (
        scale0.dim() != 2
        or shift0.dim() != 2
        or gate0.dim() != 2
        or scale1.dim() != 2
        or shift1.dim() != 2
        or gate1.dim() != 2
    ):
        raise ValueError("scale0/shift0/gate0/scale1/shift1/gate1 must be 2D [B, C]")
    if index.dim() != 2:
        raise ValueError("index must be 2D [B, L]")
    if weight is not None and (weight.dim() != 1 or weight.shape[0] != C):
        raise ValueError("weight must be 1D [C]")
    if bias is not None and (bias.dim() != 1 or bias.shape[0] != C):
        raise ValueError("bias must be 1D [C]")

    x_2d = x.view(B * L, C)
    output_2d = output.view(B * L, C)
    gate_out_2d = gate_out.view(B * L, C)
    weight = weight.contiguous() if weight is not None else x_2d
    bias = bias.contiguous() if bias is not None else x_2d

    MAX_FUSED_SIZE = 65536 // x_2d.element_size()
    BLOCK_N = min(MAX_FUSED_SIZE, triton.next_power_of_2(C))
    if C > BLOCK_N:
        raise RuntimeError("This layer norm doesn't support feature dim >= 64KB.")
    num_warps, num_stages = 4, 4

    grid = (B * L,)
    _fused_layernorm_scale_shift_gate_select01_kernel[grid](
        output_2d,
        gate_out_2d,
        x_2d,
        weight,
        bias,
        scale0.contiguous(),
        shift0.contiguous(),
        gate0.contiguous(),
        scale1.contiguous(),
        shift1.contiguous(),
        gate1.contiguous(),
        index.contiguous(),
        C,
        L,
        x_2d.stride(0),
        output_2d.stride(0),
        gate_out_2d.stride(0),
        weight.stride(0) if weight.dim() == 1 else 0,
        bias.stride(0) if bias.dim() == 1 else 0,
        scale0.stride(0),
        scale0.stride(1),
        shift0.stride(0),
        shift0.stride(1),
        gate0.stride(0),
        gate0.stride(1),
        scale1.stride(0),
        scale1.stride(1),
        shift1.stride(0),
        shift1.stride(1),
        gate1.stride(0),
        gate1.stride(1),
        index.stride(0),
        index.stride(1),
        eps,
        HAS_WEIGHT=weight is not x_2d,
        HAS_BIAS=bias is not x_2d,
        BLOCK_N=BLOCK_N,
        num_warps=num_warps,
        num_stages=num_stages,
    )


def fuse_residual_layernorm_scale_shift_gate_select01(
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
    output: torch.Tensor,
    residual_out: torch.Tensor,
    gate_out: torch.Tensor,
) -> None:
    assert x.is_cuda
    assert x.is_contiguous()
    assert residual.is_contiguous()
    assert residual_gate.is_contiguous()
    B, L, C = x.shape
    assert output.shape == x.shape and output.dtype == x.dtype
    assert residual_out.shape == x.shape and residual_out.dtype == x.dtype
    assert gate_out.shape == x.shape and gate_out.dtype == x.dtype
    assert (
        output.is_contiguous()
        and residual_out.is_contiguous()
        and gate_out.is_contiguous()
    )

    if residual.shape != x.shape:
        raise ValueError("residual must have the same shape as x")
    if residual_gate.shape != x.shape:
        raise ValueError("residual_gate must have the same shape as x")
    if (
        scale0.dim() != 2
        or shift0.dim() != 2
        or gate0.dim() != 2
        or scale1.dim() != 2
        or shift1.dim() != 2
        or gate1.dim() != 2
    ):
        raise ValueError("scale0/shift0/gate0/scale1/shift1/gate1 must be 2D [B, C]")
    if index.dim() != 2:
        raise ValueError("index must be 2D [B, L]")
    if weight is not None and (weight.dim() != 1 or weight.shape[0] != C):
        raise ValueError("weight must be 1D [C]")
    if bias is not None and (bias.dim() != 1 or bias.shape[0] != C):
        raise ValueError("bias must be 1D [C]")

    x_2d = x.view(B * L, C)
    residual_2d = residual.view(B * L, C)
    residual_gate_2d = residual_gate.view(B * L, C)
    output_2d = output.view(B * L, C)
    residual_out_2d = residual_out.view(B * L, C)
    gate_out_2d = gate_out.view(B * L, C)
    weight = weight.contiguous() if weight is not None else x_2d
    bias = bias.contiguous() if bias is not None else x_2d

    MAX_FUSED_SIZE = 65536 // x_2d.element_size()
    BLOCK_N = min(MAX_FUSED_SIZE, triton.next_power_of_2(C))
    if C > BLOCK_N:
        raise RuntimeError("This layer norm doesn't support feature dim >= 64KB.")
    num_warps, num_stages = 4, 4

    grid = (B * L,)
    _fused_residual_layernorm_scale_shift_gate_select01_kernel[grid](
        output_2d,
        residual_out_2d,
        gate_out_2d,
        x_2d,
        residual_2d,
        residual_gate_2d,
        weight,
        bias,
        scale0.contiguous(),
        shift0.contiguous(),
        gate0.contiguous(),
        scale1.contiguous(),
        shift1.contiguous(),
        gate1.contiguous(),
        index.contiguous(),
        C,
        L,
        x_2d.stride(0),
        residual_2d.stride(0),
        residual_gate_2d.stride(0),
        output_2d.stride(0),
        residual_out_2d.stride(0),
        gate_out_2d.stride(0),
        weight.stride(0) if weight.dim() == 1 else 0,
        bias.stride(0) if bias.dim() == 1 else 0,
        scale0.stride(0),
        scale0.stride(1),
        shift0.stride(0),
        shift0.stride(1),
        gate0.stride(0),
        gate0.stride(1),
        scale1.stride(0),
        scale1.stride(1),
        shift1.stride(0),
        shift1.stride(1),
        gate1.stride(0),
        gate1.stride(1),
        index.stride(0),
        index.stride(1),
        eps,
        HAS_WEIGHT=weight is not x_2d,
        HAS_BIAS=bias is not x_2d,
        BLOCK_N=BLOCK_N,
        num_warps=num_warps,
        num_stages=num_stages,
    )
