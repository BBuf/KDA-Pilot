"""Candidate entry point for `glm45__fp8_fused_moe`.

Two ops, both bit-parity-preserving reschedules of the shipped SGLang Triton MoE
(see kda_kernels.py for the parity contract and NOTES.md for the experiment
ledger):

* `triton_fused_moe_gemm`: per-token fp8 quant (bit-exact replica) + a
  schedule-retuned clone of `fused_moe_kernel` with a per-shape config table
  tuned for B300 (the shipped default config is untuned for E=161 there), a
  skip-all-padding-block early exit, and expert_ids ratio indexing so the
  64/128-aligned routing the rows carry can drive smaller M-tiles. Standalone
  up-M=32 uses a per-row release/acquire quant-to-GEMM handoff to overlap safe
  consumer launch/setup without exposing any pre-publication stores.
* `moe_fused_experts_fp8`: the whole dispatch rebuilt from those kernels:
  quant -> (align) -> up GEMM -> fused silu+quant -> down GEMM -> combine.
  Decode (M==1) runs slot-direct with no moe_align at all. The complete
  multi-kernel dispatch uses ordinary stream serialization after E37 exposed
  another rare official-gate-only PDL stale read; standalone GEMM retains its
  guarded PDL paths. The combine flavor follows the baseline's M-regime split
  (inductor-fused tree for M<=32, sequential sgl kernel above), because their
  rounding differs and is part of the reference bits.

Anything off the captured flag pattern is rejected explicitly.  This keeps the
candidate standalone, as required by the baseline policy, instead of importing
the installed SGLang implementation at runtime.
"""

import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
if _HERE not in sys.path:
    sys.path.insert(0, _HERE)

import torch
import triton.language as tl
from kda_kernels import (
    combine_small,
    moe_align,
    moe_gemm,
    per_token_quant_fp8,
    per_token_quant_fp8_handshake,
    silu_mul_quant,
    sum_reduce_big,
)


# ----------------------------------------------------------------------------- #
# tuned config tables (B300, E=161; tuned on the frozen rows' real payloads)
# ----------------------------------------------------------------------------- #
def _cfg(bm, bn, bk, g, w, s):
    return {
        "BLOCK_SIZE_M": bm,
        "BLOCK_SIZE_N": bn,
        "BLOCK_SIZE_K": bk,
        "GROUP_SIZE_M": g,
        "num_warps": w,
        "num_stages": s,
    }


# up GEMM (N=384, K=5120), keyed by token rows M (=A.shape[0]); value must keep
# BLOCK_SIZE_M dividing the align block of the routing arrays it is used with.
# NOTE on BLOCK_SIZE_M: only 64 and 128 are admissible. They keep tl.dot on
# the same tcgen05 path the baseline uses; BM=16/32 lower to a different MMA
# whose k32 accumulation rarely (~5e-6/element) rounds differently (caught by
# multi-draw stress, exp21 in NOTES.md).
_UP_CFG = [
    (1, _cfg(64, 32, 256, 1, 8, 4)),
    (15, _cfg(64, 128, 128, 1, 4, 4)),
    (16, _cfg(64, 128, 128, 1, 4, 6)),
    (256, _cfg(64, 128, 128, 1, 4, 4)),
    (10**9, _cfg(128, 256, 128, 32, 8, 4)),
]
# down GEMM (N=5120, K=192), keyed by A rows (M*topk). Two tables: the
# standalone GEMM rows and the dispatch-internal down GEMM see different
# routing densities at the same shapes, and their optima differ at large M.
_DOWN_CFG = [
    (16, _cfg(64, 128, 64, 1, 4, 3)),
    (512, _cfg(64, 256, 64, 1, 8, 4)),
    (10**9, _cfg(64, 128, 64, 32, 4, 3)),
]
_DOWN_CFG_GEMM_OP = [
    (16, _cfg(64, 128, 64, 1, 4, 3)),
    (512, _cfg(64, 256, 64, 1, 8, 4)),
    (10**9, _cfg(128, 256, 64, 32, 4, 2)),
]


def _pick(table, m):
    for bound, cfg in table:
        if m <= bound:
            return dict(cfg)
    return dict(table[-1][1])


def _infer_align_block(sorted_token_ids, expert_ids):
    b = max(1, round(sorted_token_ids.shape[0] / max(1, expert_ids.shape[0])))
    # snap to the power-of-two block moe_align was run with
    p = 1
    while p * 2 <= b:
        p *= 2
    return p if p == b else b


# ----------------------------------------------------------------------------- #
# op 1: the expert GEMM (fp8 arm)
# ----------------------------------------------------------------------------- #
def fp8_moe_gemm(
    A,
    B,
    bias,
    C,
    A_scale,
    B_scale,
    B_zp,
    topk_weights,
    topk_ids,
    sorted_token_ids,
    expert_ids,
    num_tokens_post_padded,
    mul_routed_weight,
    top_k,
    config,
    compute_type,
    use_fp8_w8a8,
    use_int8_w8a8,
    use_int8_w8a16,
    use_int4_w4a16,
    per_channel_quant,
    block_shape=None,
    **flags,
):
    unsupported = (
        not use_fp8_w8a8
        or use_int8_w8a8
        or use_int8_w8a16
        or use_int4_w4a16
        or not per_channel_quant
        or block_shape is not None
        or bias is not None
        or B_zp is not None
        or flags.get("a_use_tma")
        or flags.get("b_use_tma")
        or flags.get("c_sorted")
        or flags.get("filter_expert", True)
        or flags.get("fuse_sum_all_reduce")
        or flags.get("fuse_add_to_output")
        or flags.get("mask_output")
        or flags.get("lora_preserve_base")
        or flags.get("fuse_swiglu")
        or flags.get("no_combine")
        or A.dtype not in (torch.bfloat16, torch.float16)
        or A_scale is not None
    )
    if unsupported:
        raise NotImplementedError(
            "solution supports the frozen FP8 per-channel MoE GEMM contract only"
        )

    N, K = B.shape[1], B.shape[2]
    if N < K:
        cfg = _pick(_UP_CFG, A.shape[0])
    else:
        cfg = _pick(_DOWN_CFG_GEMM_OP, A.shape[0])
    align_block = _infer_align_block(sorted_token_ids, expert_ids)
    if align_block % cfg["BLOCK_SIZE_M"] != 0:
        cfg["BLOCK_SIZE_M"] = align_block
    if config and config.get("GROUP_SIZE_M"):
        cfg["GROUP_SIZE_M"] = max(cfg["GROUP_SIZE_M"], config["GROUP_SIZE_M"])
    handshake = N < K and A.shape[0] == 32
    if handshake:
        A_q, A_s, ready = per_token_quant_fp8_handshake(A)
    else:
        A_q, A_s = per_token_quant_fp8(A)
        ready = None
    moe_gemm(
        A_q,
        A_s,
        B,
        B_scale,
        C,
        topk_weights,
        sorted_token_ids,
        expert_ids,
        num_tokens_post_padded,
        mul_routed_weight,
        top_k,
        cfg,
        compute_type,
        align_block=align_block,
        routing_external=(N < K),
        early_trigger=False,  # op-terminal kernel: C goes back to the caller
        ready=ready,
        handshake=handshake,
    )


# ----------------------------------------------------------------------------- #
# op 2: the whole dispatch
# ----------------------------------------------------------------------------- #
_TORCH_COMPILE_COMBINE_MAX = 32  # baseline switches combine flavor here


def fused_experts_fp8(
    hidden_states,
    w1,
    w2,
    topk_weights,
    topk_ids,
    b1=None,
    b2=None,
    inplace=False,
    activation="silu",
    is_gated=True,
    apply_router_weight_on_input=False,
    use_fp8_w8a8=False,
    use_int8_w8a8=False,
    use_int8_w8a16=False,
    use_int4_w4a16=False,
    per_channel_quant=False,
    w1_scale=None,
    w2_scale=None,
    w1_zp=None,
    w2_zp=None,
    a1_scale=None,
    a2_scale=None,
    block_shape=None,
    no_combine=False,
    routed_scaling_factor=None,
    gemm1_alpha=None,
    gemm1_limit=None,
    filter_expert=True,
    swiglu_limit=None,
    gate_up_interleaved=True,
    a1_q=None,
    fuse_swiglu_interleaved=False,
):
    M = hidden_states.shape[0]
    topk = topk_ids.shape[1]
    unsupported = (
        not use_fp8_w8a8
        or use_int8_w8a8
        or use_int8_w8a16
        or use_int4_w4a16
        or not per_channel_quant
        or block_shape is not None
        or b1 is not None
        or b2 is not None
        or w1_zp is not None
        or w2_zp is not None
        or a1_scale is not None
        or a2_scale is not None
        or a1_q is not None
        or activation != "silu"
        or not is_gated
        or gemm1_alpha is not None
        or gemm1_limit is not None
        or swiglu_limit is not None
        or fuse_swiglu_interleaved
        or apply_router_weight_on_input
        or no_combine
        or filter_expert
        or hidden_states.dtype != torch.bfloat16
        or topk > 16
        or w1.shape[1] % 2 != 0
    )
    if unsupported:
        raise NotImplementedError(
            "solution supports the frozen FP8 per-channel fused-experts contract only"
        )

    assert hidden_states.is_contiguous() and w1.is_contiguous() and w2.is_contiguous()
    E, N1, _ = w1.shape
    rsf = 1.0 if routed_scaling_factor is None else float(routed_scaling_factor)
    out = hidden_states if inplace else torch.empty_like(hidden_states)

    # 1. activation quant (bit-exact replica of sgl per-token quant).  E37
    # disables PDL for the complete multi-kernel dispatch after another rare
    # official-gate-only stale read survived post-store trigger placement.
    # Standalone GEMM retains its independently guarded PDL paths.
    dispatch_pdl = False
    A_q, A_s = per_token_quant_fp8(
        hidden_states, early_trigger=False, launch_pdl=dispatch_pdl
    )

    up_cfg = _pick(_UP_CFG, M)
    c1 = torch.empty(
        M * topk, N1, device=hidden_states.device, dtype=hidden_states.dtype
    )

    sorted_ids = expert_ids = ntpp = None
    if M == 1:
        # slot-direct: no moe_align at all
        moe_gemm(
            A_q,
            A_s,
            w1,
            w1_scale,
            c1,
            topk_weights,
            None,
            topk_ids.view(-1),
            None,
            mul_routed_weight=False,
            top_k=topk,
            config=up_cfg,
            compute_type=tl.bfloat16,
            slot_mode=True,
            routing_external=True,
            launch_pdl=dispatch_pdl,
        )
    else:
        sorted_ids, expert_ids, ntpp = moe_align(
            topk_ids, up_cfg["BLOCK_SIZE_M"], E, launch_pdl=dispatch_pdl
        )
        moe_gemm(
            A_q,
            A_s,
            w1,
            w1_scale,
            c1,
            topk_weights,
            sorted_ids,
            expert_ids,
            ntpp,
            mul_routed_weight=False,
            top_k=topk,
            config=up_cfg,
            compute_type=tl.bfloat16,
            launch_pdl=dispatch_pdl,
        )

    # 2. silu*up + down-activation quant, fused
    c2q, c2s = silu_mul_quant(c1, launch_pdl=dispatch_pdl)

    # 3. down GEMM
    down_cfg = _pick(_DOWN_CFG, M * topk)
    c3 = torch.empty(
        M, topk, w2.shape[1], device=hidden_states.device, dtype=hidden_states.dtype
    )
    if M == 1:
        moe_gemm(
            c2q,
            c2s,
            w2,
            w2_scale,
            c3,
            topk_weights,
            None,
            topk_ids.view(-1),
            None,
            mul_routed_weight=True,
            top_k=1,
            config=down_cfg,
            compute_type=tl.bfloat16,
            slot_mode=True,
            routing_external=True,
            launch_pdl=dispatch_pdl,
        )
    else:
        moe_gemm(
            c2q,
            c2s,
            w2,
            w2_scale,
            c3,
            topk_weights,
            sorted_ids,
            expert_ids,
            ntpp,
            mul_routed_weight=True,
            top_k=1,
            config=down_cfg,
            compute_type=tl.bfloat16,
            align_block=up_cfg["BLOCK_SIZE_M"],
            launch_pdl=dispatch_pdl,
        )

    # 4. weighted combine - per-M-regime flavor, matching the baseline's bits
    if M <= _TORCH_COMPILE_COMBINE_MAX:
        combine_small(c3, out, rsf, launch_pdl=dispatch_pdl)
    else:
        sum_reduce_big(c3, out, rsf, launch_pdl=dispatch_pdl)
    return out


OPS = {
    "triton_fused_moe_gemm": lambda **kw: fp8_moe_gemm(**kw),
    "moe_fused_experts_fp8": lambda **kw: fused_experts_fp8(**kw),
}


# ----------------------------------------------------------------------------- #
# RECONSTRUCT: byte-identical to the baseline's hooks (tools/derive_inputs.derive
# plus the task fixes), so both arms are fed the same repaired inputs whether the
# caller applies the baseline's hook (bench harness) or this module's own
# (tests/test_solution.py).
# ----------------------------------------------------------------------------- #
_TOOLS = os.path.join(_HERE, "..", "..", "tools")
if _TOOLS not in sys.path:
    sys.path.insert(0, _TOOLS)
from derive_inputs import derive as _derive


def _gemm_fix(kw: dict) -> dict:
    a = kw.get("A")
    dt = a.dtype if torch.is_tensor(a) else torch.bfloat16
    kw["compute_type"] = {torch.bfloat16: tl.bfloat16, torch.float16: tl.float16}.get(
        dt, tl.bfloat16
    )
    kw.setdefault("bias", None)
    return kw


def _experts_fix(kw: dict) -> dict:
    kw.setdefault("inplace", False)
    kw.setdefault("activation", "silu")
    kw.setdefault("apply_router_weight_on_input", False)
    kw.setdefault("no_combine", False)
    return kw


def _repair(task_hook):
    def run(kw):
        kw = _derive(kw)
        return task_hook(kw)

    return run


RECONSTRUCT = {
    "triton_fused_moe_gemm": _repair(_gemm_fix),
    "moe_fused_experts_fp8": _repair(_experts_fix),
}
