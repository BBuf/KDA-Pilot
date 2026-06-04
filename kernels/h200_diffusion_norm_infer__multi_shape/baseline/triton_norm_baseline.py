"""Copied SGLang Triton norm baselines for the symmetric local A/B harness.

Pristine upstream sources live in baseline/upstream/{norm.py,rmsnorm_onepass.py}
(git archive of the container repo /home/sglang-omni/bbuf/repos/sglang at HEAD
84e1108312; both files are byte-identical to the locked baseline commit
c47f0e7cd for this kernel family). Provenance + local-edit log:
docs/baseline_source.md.

Local edits relative to upstream (semantics untouched):
- sglang-internal imports removed (register_custom_op, current_platform,
  debug_kernel_api, MPS/CPU fallbacks): this copy is CUDA-only and carries no
  registration layer, matching the candidate leg's topology in the local
  harness. The registration-preserving comparison happens at the in-tree
  arbiter step, not here.
- Only the two inference entry points and their Triton kernels are kept.
- Functions renamed with a `baseline_` prefix to avoid import collisions.
"""

from typing import Optional

import torch
import triton  # type: ignore
import triton.language as tl  # type: ignore
from torch import Tensor

# --------------------------------------------------------------------------- #
# One-pass LN/RMSN row kernel (upstream norm.py:_norm_infer_kernel, verbatim)
# --------------------------------------------------------------------------- #


@triton.jit
def _norm_infer_kernel(
    X,
    Y,
    W,
    B,
    stride_x_row,
    stride_y_row,
    M,
    N,
    eps,
    IS_RMS_NORM: tl.constexpr,
    HAS_WEIGHT: tl.constexpr,
    HAS_BIAS: tl.constexpr,
    BLOCK_N: tl.constexpr,
):
    row = tl.program_id(0)
    X += row * stride_x_row
    Y += row * stride_y_row
    if HAS_WEIGHT:
        W += 0
    if HAS_BIAS:
        B += 0
    cols = tl.arange(0, BLOCK_N)
    x = tl.load(X + cols, mask=cols < N, other=0.0).to(tl.float32)
    if not IS_RMS_NORM:
        mean = tl.sum(x, axis=0) / N
        xbar = tl.where(cols < N, x - mean, 0.0)
        var = tl.sum(xbar * xbar, axis=0) / N
    else:
        xbar = tl.where(cols < N, x, 0.0)
        var = tl.sum(xbar * xbar, axis=0) / N
    rstd = 1 / tl.sqrt(var + eps)
    x_hat = (x - mean) * rstd if not IS_RMS_NORM else x * rstd
    if HAS_WEIGHT:
        w = tl.load(W + cols, mask=cols < N, other=1.0).to(tl.float32)
        y = x_hat * w
    else:
        y = x_hat
    if HAS_BIAS:
        b = tl.load(B + cols, mask=cols < N, other=0.0).to(tl.float32)
        y += b
    tl.store(Y + cols, y, mask=cols < N)


def baseline_norm_infer(
    x: Tensor,
    weight: Optional[Tensor],
    bias: Optional[Tensor],
    eps: float,
    is_rms_norm: bool = False,
    out: Optional[Tensor] = None,
):
    """Verbatim copy of upstream norm.py:norm_infer (CUDA path)."""
    M, N = x.shape
    x = x.contiguous()
    if weight is not None:
        assert weight.shape == (N,)
        assert weight.stride(-1) == 1
    if bias is not None:
        assert bias.shape == (N,)
        assert bias.stride(-1) == 1
    if out is None:
        out = torch.empty_like(x)
    MAX_FUSED_SIZE = 65536 // x.element_size()
    BLOCK_N = min(MAX_FUSED_SIZE, triton.next_power_of_2(N))
    if N > BLOCK_N:
        raise RuntimeError("This layer norm doesn't support feature dim >= 64KB.")
    num_warps = min(max(BLOCK_N // 256, 1), 8)
    _norm_infer_kernel[(M,)](
        x,
        out,
        weight if weight is not None else x,  # dummy when HAS_WEIGHT=False
        bias if bias is not None else x,  # dummy when HAS_BIAS=False
        x.stride(0),
        out.stride(0),
        M,
        N,
        eps,
        IS_RMS_NORM=is_rms_norm,
        HAS_WEIGHT=weight is not None,
        HAS_BIAS=bias is not None,
        BLOCK_N=BLOCK_N,
        num_warps=num_warps,
    )
    return out


# --------------------------------------------------------------------------- #
# Tiled one-pass RMSNorm (upstream rmsnorm_onepass.py, verbatim kernel)
# --------------------------------------------------------------------------- #


@triton.jit
def _rms_norm_tiled_onepass(
    y_ptr,
    x_ptr,
    w_ptr,
    SEQ: tl.constexpr,
    DIM: tl.constexpr,
    EPS: tl.constexpr,
    BLOCK_SIZE_SEQ: tl.constexpr,
    BLOCK_SIZE_DIM: tl.constexpr,
):
    seq_blk_id = tl.program_id(0)
    seq_id = seq_blk_id * BLOCK_SIZE_SEQ

    seq_offset = seq_id + tl.arange(0, BLOCK_SIZE_SEQ)[:, None]
    s_mask = seq_offset < SEQ
    d_offset = tl.arange(0, BLOCK_SIZE_DIM)[None, :]
    d_mask = d_offset < DIM
    y_blk = y_ptr + seq_offset * DIM + d_offset
    x_blk = x_ptr + seq_offset * DIM + d_offset
    mask = s_mask & d_mask

    x = tl.load(x_blk, mask=mask, other=0.0).to(tl.float32)
    mean_square = tl.sum(x * x, axis=1, keep_dims=True) / DIM
    rstd = tl.math.rsqrt(mean_square + EPS)
    w = tl.load(w_ptr + d_offset, mask=d_mask)
    tl.store(y_blk, x * rstd * w, mask=mask)


def baseline_one_pass_rms_norm(
    x: torch.Tensor, w: torch.Tensor, eps: float = 1e-6
) -> torch.Tensor:
    """Verbatim copy of upstream rmsnorm_onepass.py:_triton_one_pass_rms_norm_cuda
    (the registered implementation's body; the upstream public wrapper is a thin
    pass-through to it)."""
    shape = x.shape
    x = x.contiguous()
    y = torch.empty_like(x)
    x_view = x.reshape(-1, shape[-1])
    y_view = y.reshape(-1, shape[-1])
    S, D = x_view.shape

    block_size_seq = min(16, triton.next_power_of_2(max(1, S // 512)))
    grid = (triton.cdiv(S, block_size_seq),)

    with torch.get_device_module().device(x.device):
        _rms_norm_tiled_onepass[grid](
            y_view,
            x_view,
            w,
            S,
            D,
            eps,
            BLOCK_SIZE_DIM=triton.next_power_of_2(D),
            BLOCK_SIZE_SEQ=block_size_seq,
        )
    return y
