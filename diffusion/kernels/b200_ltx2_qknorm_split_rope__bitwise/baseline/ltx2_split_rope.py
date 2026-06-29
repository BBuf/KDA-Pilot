"""Task-local copy of the SGLang LTX2 split rotary-embedding production path.

Source provenance (see docs/baseline_source.md for the full record):
- Repo:   https://github.com/sgl-project/sglang
- Branch: main
- Commit: aaa31eb0a11e09f9511bade5e815907ec0b91fa0
- File:   python/sglang/multimodal_gen/runtime/models/dits/ltx_2.py
  (sha256 ff3fd96e8df346a82840a18a00f2702b8b7d02bc1950fbfcebfe3d760bde0141)
- Copied: apply_interleaved_rotary_emb (upstream lines 177-183, verbatim),
          apply_split_rotary_emb     (upstream lines 186-239).

LOCAL EDIT (documented in docs/baseline_source.md):
  The original task forced the eager fallback by removing the bf16 Triton
  dispatch. That was too weak for SGLang integration: current LTX2.3 production
  uses the Triton fast path for all live bf16 split-RoPE rows. This file now
  vendors that Triton kernel locally and keeps the same dispatcher condition as
  upstream `apply_split_rotary_emb`, while still importing nothing from sglang.
"""

from typing import Tuple

import torch
import triton
import triton.language as tl


@triton.jit
def _ltx2_split_rotary_kernel(
    out_ptr,
    x_ptr,
    cos_ptr,
    sin_ptr,
    seq_len: tl.constexpr,
    num_heads: tl.constexpr,
    head_dim: tl.constexpr,
    half_dim: tl.constexpr,
    stride_cos_b: tl.constexpr,
    stride_cos_h: tl.constexpr,
    stride_cos_t: tl.constexpr,
    stride_sin_b: tl.constexpr,
    stride_sin_h: tl.constexpr,
    stride_sin_t: tl.constexpr,
    BLOCK_HEADS: tl.constexpr,
    BLOCK_HALF: tl.constexpr,
):
    pid_bt = tl.program_id(0)
    head_block = tl.program_id(1)
    batch = pid_bt // seq_len
    token = pid_bt - batch * seq_len
    heads = head_block * BLOCK_HEADS + tl.arange(0, BLOCK_HEADS)
    offsets = tl.arange(0, BLOCK_HALF)
    mask = (heads[:, None] < num_heads) & (offsets[None, :] < half_dim)

    x_base = ((batch * seq_len + token) * num_heads + heads[:, None]) * head_dim
    cos_base = (
        batch * stride_cos_b + heads[:, None] * stride_cos_h + token * stride_cos_t
    )
    sin_base = (
        batch * stride_sin_b + heads[:, None] * stride_sin_h + token * stride_sin_t
    )

    x_first = tl.load(x_ptr + x_base + offsets[None, :], mask=mask, other=0.0)
    x_second = tl.load(
        x_ptr + x_base + half_dim + offsets[None, :], mask=mask, other=0.0
    )
    cos = tl.load(cos_ptr + cos_base + offsets[None, :], mask=mask, other=0.0)
    sin = tl.load(sin_ptr + sin_base + offsets[None, :], mask=mask, other=0.0)

    out_first = (x_first * cos).to(tl.bfloat16).to(tl.float32) + (
        -x_second.to(tl.float32) * sin.to(tl.float32)
    )
    out_second = (x_second * cos).to(tl.bfloat16).to(tl.float32) + (
        x_first.to(tl.float32) * sin.to(tl.float32)
    )

    tl.store(out_ptr + x_base + offsets[None, :], out_first, mask=mask)
    tl.store(out_ptr + x_base + half_dim + offsets[None, :], out_second, mask=mask)


def apply_ltx2_split_rotary_emb(
    x: torch.Tensor, cos: torch.Tensor, sin: torch.Tensor
) -> torch.Tensor:
    """Task-local copy of SGLang's bf16 Triton split-RoPE fast path."""
    batch, seq_len, inner_dim = x.shape
    cos_batch, num_heads, cos_seq_len, half_dim = cos.shape
    head_dim = half_dim * 2
    if (
        cos_batch != batch
        or cos_seq_len != seq_len
        or inner_dim != num_heads * head_dim
        or sin.shape != cos.shape
    ):
        raise ValueError(
            "LTX2 split RoPE shape mismatch: "
            f"x={tuple(x.shape)}, cos={tuple(cos.shape)}, sin={tuple(sin.shape)}"
        )

    out = torch.empty_like(x)
    block_half = triton.next_power_of_2(half_dim)
    block_heads = min(16, triton.next_power_of_2(num_heads))
    num_warps = min(8, max(1, block_heads))
    grid = (batch * seq_len, triton.cdiv(num_heads, block_heads))
    _ltx2_split_rotary_kernel[grid](
        out,
        x,
        cos,
        sin,
        seq_len,
        num_heads,
        head_dim,
        half_dim,
        cos.stride(0),
        cos.stride(1),
        cos.stride(2),
        sin.stride(0),
        sin.stride(1),
        sin.stride(2),
        BLOCK_HEADS=block_heads,
        BLOCK_HALF=block_half,
        num_warps=num_warps,
    )
    return out


def apply_interleaved_rotary_emb(
    x: torch.Tensor, freqs: Tuple[torch.Tensor, torch.Tensor]
) -> torch.Tensor:
    """Verbatim upstream copy (lines 177-183). Interleaved RoPE variant.

    Unused by this task (the production callsite uses the split variant when
    cos is 4-D); kept only as faithful copied source. Interleaved/non-split
    RoPE tensors are an explicit reject case for the candidate.
    """
    cos, sin = freqs
    x_real, x_imag = x.unflatten(2, (-1, 2)).unbind(-1)
    x_rotated = torch.stack([-x_imag, x_real], dim=-1).flatten(2)
    return x * cos + x_rotated * sin


def apply_split_rotary_emb_eager(
    x: torch.Tensor, freqs: Tuple[torch.Tensor, torch.Tensor]
) -> torch.Tensor:
    """Eager fallback for split RoPE.

    This is upstream apply_split_rotary_emb lines 208-239 VERBATIM, with the
    bf16 Triton fast-path dispatch (upstream lines 190-206) removed so the eager
    expression always runs. The candidate must reproduce these exact rounding
    points:
      out = split_x * cos_u          # bf16 multiply -> rounded to bf16 here
      first_out.addcmul_(-sin_u, second_x)   # (first*cos) - sin*second
      second_out.addcmul_(sin_u, first_x)    # (second*cos) + sin*first
    i.e. the first product is rounded to bf16 BEFORE the sine term is added.
    Contracting `x*cos +/- y*sin` into one FMA can change the bf16 output bits.
    """
    cos, sin = freqs
    x_dtype = x.dtype
    needs_reshape = False
    if x.ndim != 4 and cos.ndim == 4:
        b = x.shape[0]
        _, h, t, _ = cos.shape
        x = x.reshape(b, t, h, -1).swapaxes(1, 2)
        needs_reshape = True

    last = x.shape[-1]
    if last % 2 != 0:
        raise ValueError(
            f"Expected x.shape[-1] to be even for split rotary, got {last}."
        )
    r = last // 2

    split_x = x.reshape(*x.shape[:-1], 2, r)
    first_x = split_x[..., :1, :]
    second_x = split_x[..., 1:, :]

    cos_u = cos.unsqueeze(-2)
    sin_u = sin.unsqueeze(-2)

    out = split_x * cos_u
    first_out = out[..., :1, :]
    second_out = out[..., 1:, :]
    first_out.addcmul_(-sin_u, second_x)
    second_out.addcmul_(sin_u, first_x)

    out = out.reshape(*out.shape[:-2], last)
    if needs_reshape:
        out = out.swapaxes(1, 2).reshape(b, t, -1)
    return out.to(dtype=x_dtype)


def apply_split_rotary_emb(
    x: torch.Tensor, freqs: Tuple[torch.Tensor, torch.Tensor]
) -> torch.Tensor:
    """Production dispatcher copied from SGLang `apply_split_rotary_emb`.

    Live LTX2.3 rows are bf16 CUDA tensors with 3-D q/k and 4-D split-RoPE
    tables, so they must use the local Triton fast path. This is the bitwise
    target for candidate kernels. Eager fallback remains available only for
    unsupported/debug rows.
    """
    cos, sin = freqs
    if (
        x.ndim == 3
        and cos.ndim == 4
        and sin.ndim == 4
        and x.dtype == torch.bfloat16
        and cos.dtype == torch.bfloat16
        and sin.dtype == torch.bfloat16
        and x.is_cuda
        and x.is_contiguous()
        and cos.is_cuda
        and sin.is_cuda
    ):
        return apply_ltx2_split_rotary_emb(x, cos, sin)
    return apply_split_rotary_emb_eager(x, freqs)


def split_rope_support_status(
    x: torch.Tensor,
    cos: torch.Tensor,
    sin: torch.Tensor,
    *,
    tp_world_size: int = 1,
) -> Tuple[bool, str]:
    """Return (supported, reason). Encodes the source-prompt reject list so the
    candidate path can cleanly reject/fall back instead of approximating.

    Reject: TP world size != 1; non-bf16 x/cos/sin; non-contiguous x;
    cos/sin last-dim stride != 1 (interleaved/non-split or non-contiguous last
    dim); shape/rank mismatch. (RMSNorm-instance, eps, and fp32-weight checks
    live with the norm inputs and are validated by the adapter/oracle caller.)
    """
    if tp_world_size != 1:
        return False, f"tensor-parallel world size {tp_world_size} != 1"
    for name, t in (("x", x), ("cos", cos), ("sin", sin)):
        if t.dtype != torch.bfloat16:
            return False, f"{name} dtype {t.dtype} != torch.bfloat16"
    if not x.is_contiguous():
        return False, "x is not contiguous"
    if cos.stride(-1) != 1 or sin.stride(-1) != 1:
        return False, "cos/sin last-dim stride != 1 (interleaved/non-split or non-contiguous)"
    if cos.ndim != 4 or sin.ndim != 4:
        return False, f"cos/sin must be 4-D (split layout), got {cos.ndim}-D"
    if x.shape[-1] % 2 != 0:
        return False, f"x last dim {x.shape[-1]} is not even"
    expected_h = cos.shape[1] * 2 * cos.shape[3]
    if x.shape[-1] != expected_h:
        return False, (
            f"x hidden {x.shape[-1]} != num_heads*head_dim "
            f"({cos.shape[1]}*{2 * cos.shape[3]} = {expected_h})"
        )
    if cos.shape != sin.shape:
        return False, f"cos shape {tuple(cos.shape)} != sin shape {tuple(sin.shape)}"
    if cos.shape[0] != x.shape[0]:
        return False, f"cos batch {cos.shape[0]} != x batch {x.shape[0]}"
    if cos.shape[2] != x.shape[1]:
        return False, f"cos seq length {cos.shape[2]} != x seq length {x.shape[1]}"
    return True, "supported"
