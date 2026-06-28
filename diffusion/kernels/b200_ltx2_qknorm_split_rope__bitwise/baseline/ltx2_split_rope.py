"""Task-local copy of the SGLang LTX2 split rotary-embedding reference.

Source provenance (see docs/baseline_source.md for the full record):
- Repo:   https://github.com/sgl-project/sglang
- Branch: main
- Commit: aaa31eb0a11e09f9511bade5e815907ec0b91fa0
- File:   python/sglang/multimodal_gen/runtime/models/dits/ltx_2.py
  (sha256 ff3fd96e8df346a82840a18a00f2702b8b7d02bc1950fbfcebfe3d760bde0141)
- Copied: apply_interleaved_rotary_emb (upstream lines 177-183, verbatim),
          apply_split_rotary_emb     (upstream lines 186-239).

LOCAL EDIT (documented in docs/baseline_source.md):
  Upstream apply_split_rotary_emb dispatches to a bf16 Triton fast path
  (sglang.jit_kernel.diffusion.triton.ltx2_rotary.apply_ltx2_split_rotary_emb)
  whenever the inputs are the production shape (x 3-D, cos/sin 4-D, all bf16,
  cuda, x contiguous). That fast path is exactly the optimized kernel this task
  is REPLACING, and it is not the bit-exact reference. The oracle therefore uses
  apply_split_rotary_emb_eager() below, which is the upstream EAGER FALLBACK
  expression (upstream lines 208-239) with the fast-path dispatch removed so it
  always runs the eager math. This module imports nothing from sglang.
"""

from typing import Tuple

import torch


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
    """Bit-exact eager reference for split RoPE (the oracle target).

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


# Backwards-compatible name used by the oracle; always the forced-eager path.
apply_split_rotary_emb = apply_split_rotary_emb_eager


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
