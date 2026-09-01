"""Candidate entry point for `lfm25__triton_fused_moe`.

Standalone Triton fused-MoE GEMM against the copied baseline ABI. The kernels keep the
baseline's exact numerical path - bf16 MMA with an fp32 accumulator advanced in
ascending-K order (`acc += tl.dot(a, b)`), fp32 routed-weight multiply, one rounding to
bf16 at the store - because the correctness gate is rtol=atol=1e-5 on bf16, which is
bit-exactness in practice. probe_numerics.py verified on this GPU that BLOCK_N /
BLOCK_K / GROUP_M / num_warps / num_stages / TMA-vs-cp.async all preserve bits, and
exp_bm128.py verified that tcgen05 m64 and m128 tiles round identically.

What changes vs the baseline:
  * per-workload-shape tuned schedules (CONFIGS below, from solution/tune_results/);
  * prefill rows (metadata BLOCK_M=64) run a super-block kernel: each CTA covers
    MERGE consecutive metadata blocks; when they belong to one expert (>97% of blocks
    at these shapes: expert segments span ~20-32 blocks) a single (MERGE*64)-row GEMM
    runs against that expert panel, halving per-row B traffic and using fatter tcgen05
    tiles; mixed blocks fall back to per-block GEMMs, reproducing baseline blocking.

BLOCK_SIZE_M itself is pinned by the moe_align_block_size metadata and is always taken
from the caller's config.
"""

from typing import Any

import torch
import triton
import triton.language as tl

try:
    from triton.tools.tensor_descriptor import TensorDescriptor

    _support_tensor_descriptor = True
except Exception:  # noqa: BLE001 - absence of TMA support is the signal itself
    _support_tensor_descriptor = False


@triton.jit
def _write_zeros_to_output(
    c_ptr,
    stride_cm,
    stride_cn,
    pid_n,
    N,
    offs_token,
    token_mask,
    BLOCK_SIZE_M,
    BLOCK_SIZE_N,
    compute_type,
):
    accumulator = tl.zeros((BLOCK_SIZE_M, BLOCK_SIZE_N), dtype=compute_type)
    offs_cn = pid_n * BLOCK_SIZE_N + tl.arange(0, BLOCK_SIZE_N)
    c_ptrs = c_ptr + stride_cm * offs_token[:, None] + stride_cn * offs_cn[None, :]
    c_mask = token_mask[:, None] & (offs_cn[None, :] < N)
    tl.store(c_ptrs, accumulator, mask=c_mask)


@triton.jit
def _fused_moe_kernel(
    a_ptr,
    b_ptr,
    b_desc,
    c_ptr,
    topk_weights_ptr,
    sorted_token_ids_ptr,
    expert_ids_ptr,
    num_tokens_post_padded_ptr,
    N,
    K,
    EM,
    num_valid_tokens,
    stride_am,
    stride_ak,
    stride_be,
    stride_bk,
    stride_bn,
    stride_cm,
    stride_cn,
    BLOCK_SIZE_M: tl.constexpr,
    BLOCK_SIZE_N: tl.constexpr,
    BLOCK_SIZE_K: tl.constexpr,
    GROUP_SIZE_M: tl.constexpr,
    MUL_ROUTED_WEIGHT: tl.constexpr,
    top_k: tl.constexpr,
    compute_type: tl.constexpr,
    even_Ks: tl.constexpr,
    even_Ns: tl.constexpr,
    filter_expert: tl.constexpr,
):
    """Baseline `fused_moe_kernel`, bf16 non-quant path, schedule-only changes."""
    pid = tl.program_id(axis=0)
    num_pid_m = tl.cdiv(EM, BLOCK_SIZE_M)
    num_pid_n = tl.cdiv(N, BLOCK_SIZE_N)
    num_pid_in_group = GROUP_SIZE_M * num_pid_n
    group_id = pid // num_pid_in_group
    first_pid_m = group_id * GROUP_SIZE_M
    group_size_m = min(num_pid_m - first_pid_m, GROUP_SIZE_M)
    pid_m = first_pid_m + ((pid % num_pid_in_group) % group_size_m)
    pid_n = (pid % num_pid_in_group) // group_size_m

    num_tokens_post_padded = tl.load(num_tokens_post_padded_ptr)
    if pid_m * BLOCK_SIZE_M >= num_tokens_post_padded:
        return
    offs_token_id = pid_m * BLOCK_SIZE_M + tl.arange(0, BLOCK_SIZE_M).to(tl.int64)
    offs_token = tl.load(sorted_token_ids_ptr + offs_token_id).to(tl.int64)
    token_mask = offs_token < num_valid_tokens

    off_experts_i32 = tl.load(expert_ids_ptr + pid_m)
    off_experts = off_experts_i32.to(tl.int64)

    if filter_expert and off_experts == -1:
        _write_zeros_to_output(
            c_ptr,
            stride_cm,
            stride_cn,
            pid_n,
            N,
            offs_token,
            token_mask,
            BLOCK_SIZE_M,
            BLOCK_SIZE_N,
            compute_type,
        )
        return

    if even_Ns:
        offs_bn = pid_n * BLOCK_SIZE_N + tl.arange(0, BLOCK_SIZE_N).to(tl.int64)
    else:
        offs_bn = (pid_n * BLOCK_SIZE_N + tl.arange(0, BLOCK_SIZE_N).to(tl.int64)) % N
    offs_k = tl.arange(0, BLOCK_SIZE_K)
    a_ptrs = a_ptr + (
        offs_token[:, None] // top_k * stride_am + offs_k[None, :] * stride_ak
    )
    if b_desc is None:
        b_ptrs = (
            b_ptr
            + off_experts * stride_be
            + (offs_k[:, None] * stride_bk + offs_bn[None, :] * stride_bn)
        )
    else:
        start_offs_n = pid_n * BLOCK_SIZE_N

    accumulator = tl.zeros((BLOCK_SIZE_M, BLOCK_SIZE_N), dtype=tl.float32)
    for k_start in range(0, K, BLOCK_SIZE_K):
        if even_Ks:
            a = tl.load(a_ptrs, mask=token_mask[:, None], other=0.0)
        else:
            a = tl.load(
                a_ptrs,
                mask=token_mask[:, None] & (offs_k[None, :] < K - k_start),
                other=0.0,
            )
        if b_desc is not None:
            b = (
                b_desc.load([off_experts_i32, start_offs_n, k_start])
                .reshape(BLOCK_SIZE_N, BLOCK_SIZE_K)
                .T
            )
        elif even_Ks:
            b = tl.load(b_ptrs)
        else:
            b = tl.load(b_ptrs, mask=offs_k[:, None] < K - k_start, other=0.0)
        accumulator += tl.dot(a, b)
        a_ptrs += BLOCK_SIZE_K * stride_ak
        if b_desc is None:
            b_ptrs += BLOCK_SIZE_K * stride_bk

    if MUL_ROUTED_WEIGHT:
        moe_weight = tl.load(topk_weights_ptr + offs_token, mask=token_mask, other=0)
        accumulator *= moe_weight[:, None]

    accumulator = accumulator.to(compute_type)
    offs_cn = pid_n * BLOCK_SIZE_N + tl.arange(0, BLOCK_SIZE_N)
    c_ptrs = c_ptr + stride_cm * offs_token[:, None] + stride_cn * offs_cn[None, :]
    if even_Ns:
        c_mask = token_mask[:, None]
    else:
        c_mask = token_mask[:, None] & (offs_cn[None, :] < N)
    tl.store(c_ptrs, accumulator, mask=c_mask)


@triton.jit
def _gemm_rows(
    a_ptr,
    b_ptr,
    b_desc,
    c_ptr,
    topk_weights_ptr,
    offs_token,
    token_mask,
    off_experts,
    pid_n,
    K,
    stride_am,
    stride_ak,
    stride_be,
    stride_bk,
    stride_bn,
    stride_cm,
    stride_cn,
    ROWS: tl.constexpr,
    BLOCK_SIZE_N: tl.constexpr,
    BLOCK_SIZE_K: tl.constexpr,
    MUL_ROUTED_WEIGHT: tl.constexpr,
    top_k: tl.constexpr,
    compute_type: tl.constexpr,
):
    """One [ROWS, BLOCK_N] output tile against a single expert panel (N, K even)."""
    offs_bn = pid_n * BLOCK_SIZE_N + tl.arange(0, BLOCK_SIZE_N).to(tl.int64)
    offs_k = tl.arange(0, BLOCK_SIZE_K)
    a_ptrs = a_ptr + (
        offs_token[:, None] // top_k * stride_am + offs_k[None, :] * stride_ak
    )
    if b_desc is None:
        b_ptrs = (
            b_ptr
            + off_experts * stride_be
            + (offs_k[:, None] * stride_bk + offs_bn[None, :] * stride_bn)
        )
    else:
        start_n = pid_n * BLOCK_SIZE_N
        eid32 = off_experts.to(tl.int32)
    accumulator = tl.zeros((ROWS, BLOCK_SIZE_N), dtype=tl.float32)
    for k_start in range(0, K, BLOCK_SIZE_K):
        a = tl.load(a_ptrs, mask=token_mask[:, None], other=0.0)
        if b_desc is None:
            b = tl.load(b_ptrs)
        else:
            b = (
                b_desc.load([eid32, start_n, k_start])
                .reshape(BLOCK_SIZE_N, BLOCK_SIZE_K)
                .T
            )
        accumulator += tl.dot(a, b)
        a_ptrs += BLOCK_SIZE_K * stride_ak
        if b_desc is None:
            b_ptrs += BLOCK_SIZE_K * stride_bk
    if MUL_ROUTED_WEIGHT:
        moe_weight = tl.load(topk_weights_ptr + offs_token, mask=token_mask, other=0)
        accumulator *= moe_weight[:, None]
    accumulator = accumulator.to(compute_type)
    offs_cn = pid_n * BLOCK_SIZE_N + tl.arange(0, BLOCK_SIZE_N)
    c_ptrs = c_ptr + stride_cm * offs_token[:, None] + stride_cn * offs_cn[None, :]
    tl.store(c_ptrs, accumulator, mask=token_mask[:, None])


@triton.jit
def _fused_moe_kernel_merge(
    a_ptr,
    b_ptr,
    b_desc,
    c_ptr,
    topk_weights_ptr,
    sorted_token_ids_ptr,
    expert_ids_ptr,
    num_tokens_post_padded_ptr,
    N,
    K,
    EM,
    num_valid_tokens,
    stride_am,
    stride_ak,
    stride_be,
    stride_bk,
    stride_bn,
    stride_cm,
    stride_cn,
    META_M: tl.constexpr,
    MERGE: tl.constexpr,
    BLOCK_SIZE_N: tl.constexpr,
    BLOCK_SIZE_K: tl.constexpr,
    GROUP_SIZE_M: tl.constexpr,
    MUL_ROUTED_WEIGHT: tl.constexpr,
    top_k: tl.constexpr,
    compute_type: tl.constexpr,
):
    """Super-block GEMM over MERGE consecutive metadata blocks (requires N % BLOCK_N ==
    0, K % BLOCK_K == 0, filter_expert=False). Bit-exact with the baseline blocking:
    each output row's K-chain is identical, only the tile that carries it changes."""
    BLOCK_SIZE_M: tl.constexpr = MERGE * META_M
    pid = tl.program_id(axis=0)
    num_pid_m = tl.cdiv(EM, BLOCK_SIZE_M)
    num_pid_n = tl.cdiv(N, BLOCK_SIZE_N)
    num_pid_in_group = GROUP_SIZE_M * num_pid_n
    group_id = pid // num_pid_in_group
    first_pid_m = group_id * GROUP_SIZE_M
    group_size_m = min(num_pid_m - first_pid_m, GROUP_SIZE_M)
    pid_m = first_pid_m + ((pid % num_pid_in_group) % group_size_m)
    pid_n = (pid % num_pid_in_group) // group_size_m

    num_tokens_post_padded = tl.load(num_tokens_post_padded_ptr)
    if pid_m * BLOCK_SIZE_M >= num_tokens_post_padded:
        return
    # Metadata blocks covered by this CTA. Blocks beyond the padded extent carry
    # unread garbage expert ids - fold them onto the first block; their rows are
    # masked off by token_mask, so only the pointer base must stay in bounds.
    nblk = tl.cdiv(num_tokens_post_padded, META_M)
    eid_a = tl.load(expert_ids_ptr + MERGE * pid_m).to(tl.int64)
    offs_blk = MERGE * pid_m + tl.arange(0, MERGE)
    blk_ok = offs_blk < nblk
    eids_raw = tl.load(expert_ids_ptr + offs_blk, mask=blk_ok, other=0).to(tl.int64)
    eids = tl.where(blk_ok, eids_raw, eid_a)
    uniform = tl.min(eids) == tl.max(eids)

    if uniform:
        # Unlike the per-block kernel, a super-block can span rows in
        # [num_tokens_post_padded, EM): mask the id load at the array bound and gate
        # the row mask at the padded extent, so neither the tail contents nor the
        # allocation size behind EM are relied upon.
        offs_token_id = pid_m * BLOCK_SIZE_M + tl.arange(0, BLOCK_SIZE_M).to(tl.int64)
        row_ok = offs_token_id < num_tokens_post_padded
        offs_token = tl.load(
            sorted_token_ids_ptr + offs_token_id,
            mask=offs_token_id < EM,
            other=num_valid_tokens,
        ).to(tl.int64)
        token_mask = row_ok & (offs_token < num_valid_tokens)
        _gemm_rows(
            a_ptr,
            b_ptr,
            b_desc,
            c_ptr,
            topk_weights_ptr,
            offs_token,
            token_mask,
            eid_a,
            pid_n,
            K,
            stride_am,
            stride_ak,
            stride_be,
            stride_bk,
            stride_bn,
            stride_cm,
            stride_cn,
            BLOCK_SIZE_M,
            BLOCK_SIZE_N,
            BLOCK_SIZE_K,
            MUL_ROUTED_WEIGHT,
            top_k,
            compute_type,
        )
    else:
        offs_lo = tl.arange(0, META_M).to(tl.int64)
        for j in tl.static_range(MERGE):
            blk_j = MERGE * pid_m + j
            eid_j = tl.load(expert_ids_ptr + blk_j, mask=blk_j < nblk, other=0).to(
                tl.int64
            )
            offs_j = pid_m * BLOCK_SIZE_M + j * META_M + offs_lo
            tok_j = tl.load(
                sorted_token_ids_ptr + offs_j,
                mask=offs_j < EM,
                other=num_valid_tokens,
            ).to(tl.int64)
            _gemm_rows(
                a_ptr,
                b_ptr,
                b_desc,
                c_ptr,
                topk_weights_ptr,
                tok_j,
                (blk_j < nblk)
                & (offs_j < num_tokens_post_padded)
                & (tok_j < num_valid_tokens),
                eid_j,
                pid_n,
                K,
                stride_am,
                stride_ak,
                stride_be,
                stride_bk,
                stride_bn,
                stride_cm,
                stride_cn,
                META_M,
                BLOCK_SIZE_N,
                BLOCK_SIZE_K,
                MUL_ROUTED_WEIGHT,
                top_k,
                compute_type,
            )


# --------------------------------------------------------------------------- #
# host side
# --------------------------------------------------------------------------- #
_TMA_ALLOCATOR_SET = False


def _set_triton_tma_allocator():
    global _TMA_ALLOCATOR_SET
    if _TMA_ALLOCATOR_SET:
        return

    def alloc_fn(size: int, alignment: int, stream: int | None):
        return torch.empty(size, device="cuda", dtype=torch.int8)

    triton.set_allocator(alloc_fn)
    _TMA_ALLOCATOR_SET = True


_B_DESC_CACHE: dict[tuple, "TensorDescriptor"] = {}


def _b_tma_desc(B: torch.Tensor, block_n: int, block_k: int):
    key = (
        int(B.data_ptr()),
        tuple(B.shape),
        tuple(B.stride()),
        str(B.dtype),
        int(block_n),
        int(block_k),
    )
    desc = _B_DESC_CACHE.get(key)
    if desc is None:
        desc = TensorDescriptor(B, B.shape, B.stride(), [1, block_n, block_k])
        if len(_B_DESC_CACHE) > 64:
            _B_DESC_CACHE.clear()
        _B_DESC_CACHE[key] = desc
    return desc


# Tuned schedules from solution/tune_results/ (official do_bench-around-graph timing,
# every entry verified bit-exact against the baseline on the captured payloads).
# key: (E, N, K, top_k, mul_routed_weight, em_bucket); em_bucket over
# sorted_token_ids.shape[0]: 0 decode (<=256), 1 small batch (<=8192), 2 prefill.
# "merge": run _fused_moe_kernel_merge with that super-block factor.
CONFIGS: dict[tuple, dict[str, Any]] = {
    # LFM2.5-8B-A1B (E=32): up N=3584 K=2048 top4, down N=2048 K=1792 top1
    (32, 3584, 2048, 4, False, 0): {
        "BLOCK_SIZE_N": 128,
        "BLOCK_SIZE_K": 128,
        "GROUP_SIZE_M": 1,
        "num_warps": 4,
        "num_stages": 4,
    },
    (32, 2048, 1792, 1, True, 0): {
        "BLOCK_SIZE_N": 64,
        "BLOCK_SIZE_K": 128,
        "GROUP_SIZE_M": 1,
        "num_warps": 4,
        "num_stages": 6,
    },
    (32, 3584, 2048, 4, False, 1): {
        "BLOCK_SIZE_N": 128,
        "BLOCK_SIZE_K": 128,
        "GROUP_SIZE_M": 1,
        "num_warps": 4,
        "num_stages": 4,
        "tma": True,
    },
    (32, 2048, 1792, 1, True, 1): {
        "BLOCK_SIZE_N": 128,
        "BLOCK_SIZE_K": 128,
        "GROUP_SIZE_M": 1,
        "num_warps": 4,
        "num_stages": 4,
        "tma": True,
    },
    (32, 3584, 2048, 4, False, 2): {
        "BLOCK_SIZE_N": 256,
        "BLOCK_SIZE_K": 64,
        "GROUP_SIZE_M": 8,
        "num_warps": 8,
        "num_stages": 4,
        "tma": True,
        "merge": 2,
    },
    # GLM-4.7-Flash (E=65): up N=3072 K=2048 top5, down N=2048 K=1536 top1
    (65, 3072, 2048, 5, False, 0): {
        "BLOCK_SIZE_N": 64,
        "BLOCK_SIZE_K": 128,
        "GROUP_SIZE_M": 1,
        "num_warps": 4,
        "num_stages": 6,
        "tma": True,
    },
    (65, 2048, 1536, 1, True, 0): {
        "BLOCK_SIZE_N": 64,
        "BLOCK_SIZE_K": 128,
        "GROUP_SIZE_M": 1,
        "num_warps": 4,
        "num_stages": 4,
        "tma": True,
    },
    (65, 3072, 2048, 5, False, 1): {
        "BLOCK_SIZE_N": 128,
        "BLOCK_SIZE_K": 128,
        "GROUP_SIZE_M": 8,
        "num_warps": 4,
        "num_stages": 4,
        "tma": True,
    },
    (65, 2048, 1536, 1, True, 1): {
        "BLOCK_SIZE_N": 128,
        "BLOCK_SIZE_K": 128,
        "GROUP_SIZE_M": 1,
        "num_warps": 4,
        "num_stages": 4,
        "tma": True,
    },
    (65, 3072, 2048, 5, False, 2): {
        "BLOCK_SIZE_N": 256,
        "BLOCK_SIZE_K": 64,
        "GROUP_SIZE_M": 8,
        "num_warps": 8,
        "num_stages": 4,
        "tma": True,
        "merge": 2,
    },
}

# Tuner hook: when set, overrides every dispatch (used only by the tuning scripts).
CONFIG_OVERRIDE: dict[str, Any] | None = None


def _em_bucket(em: int) -> int:
    if em <= 256:
        return 0
    if em <= 8192:
        return 1
    return 2


def _pick_config(E, N, K, top_k, mul_routed_weight, em, caller_cfg):
    if CONFIG_OVERRIDE is not None:
        cfg = dict(CONFIG_OVERRIDE)
    else:
        key = (E, N, K, top_k, bool(mul_routed_weight), _em_bucket(em))
        cfg = CONFIGS.get(key)
        cfg = dict(cfg) if cfg is not None else dict(caller_cfg)
    cfg["BLOCK_SIZE_M"] = caller_cfg["BLOCK_SIZE_M"]
    cfg.setdefault("BLOCK_SIZE_N", caller_cfg.get("BLOCK_SIZE_N", 64))
    cfg.setdefault("BLOCK_SIZE_K", caller_cfg.get("BLOCK_SIZE_K", 64))
    cfg.setdefault("GROUP_SIZE_M", caller_cfg.get("GROUP_SIZE_M", 1))
    return cfg


def invoke_fused_moe_gemm(
    A: torch.Tensor,
    B: torch.Tensor,
    bias: torch.Tensor | None,
    C: torch.Tensor,
    A_scale: torch.Tensor | None,
    B_scale: torch.Tensor | None,
    B_zp: torch.Tensor | None,
    topk_weights: torch.Tensor,
    topk_ids: torch.Tensor,
    sorted_token_ids: torch.Tensor,
    expert_ids: torch.Tensor,
    num_tokens_post_padded: torch.Tensor,
    mul_routed_weight: bool,
    top_k: int,
    config: dict[str, Any],
    compute_type: tl.dtype,
    use_fp8_w8a8: bool = False,
    use_int8_w8a8: bool = False,
    use_int8_w8a16: bool = False,
    use_int4_w4a16: bool = False,
    per_channel_quant: bool = False,
    block_shape: list[int] | None = None,
    no_combine: bool = False,
    a_use_tma: bool = False,
    b_use_tma: bool = False,
    c_sorted: bool = False,
    filter_expert: bool = True,
    fuse_sum_all_reduce: bool = False,
    router_topk: int = 1,
    fuse_add_to_output: bool = False,
    add_output_mask: torch.Tensor | None = None,
    mask_output: bool = False,
    lora_preserve_base: bool = False,
    fuse_swiglu: bool = False,
) -> None:
    assert not (use_fp8_w8a8 or use_int8_w8a8 or use_int8_w8a16 or use_int4_w4a16), (
        "quantized paths are outside this candidate's envelope"
    )
    assert bias is None and block_shape is None
    assert not (fuse_swiglu or fuse_add_to_output or mask_output or fuse_sum_all_reduce)
    assert not (c_sorted or a_use_tma or lora_preserve_base)
    assert topk_weights.stride(1) == 1
    assert sorted_token_ids.stride(0) == 1

    E, N, K = B.shape[0], B.shape[1], B.shape[2]
    EM = sorted_token_ids.shape[0]
    cfg = _pick_config(E, N, K, top_k, mul_routed_weight, EM, config)

    merge = int(cfg.pop("merge", 0))
    use_tma = bool(cfg.pop("tma", False)) and _support_tensor_descriptor
    bn, bk = cfg["BLOCK_SIZE_N"], cfg["BLOCK_SIZE_K"]
    if merge and (filter_expert or N % bn != 0 or K % bk != 0):
        merge = 0  # outside the merge kernel's envelope: fall back to the general one

    if use_tma:
        _set_triton_tma_allocator()
        b_desc = _b_tma_desc(B, bn, bk)
        b_arg = None
    else:
        b_desc = None
        b_arg = B

    if merge:
        meta_m = cfg.pop("BLOCK_SIZE_M")
        grid = (triton.cdiv(EM, merge * meta_m) * triton.cdiv(N, bn),)
        _fused_moe_kernel_merge[grid](
            A,
            b_arg,
            b_desc,
            C,
            topk_weights,
            sorted_token_ids,
            expert_ids,
            num_tokens_post_padded,
            N,
            K,
            EM,
            topk_ids.numel(),
            A.stride(0),
            A.stride(1),
            B.stride(0),
            B.stride(2),
            B.stride(1),
            C.stride(-2),
            C.stride(-1),
            META_M=meta_m,
            MERGE=merge,
            MUL_ROUTED_WEIGHT=mul_routed_weight,
            top_k=top_k,
            compute_type=compute_type,
            **cfg,
        )
        return

    grid = (triton.cdiv(EM, cfg["BLOCK_SIZE_M"]) * triton.cdiv(N, bn),)
    _fused_moe_kernel[grid](
        A,
        b_arg,
        b_desc,
        C,
        topk_weights,
        sorted_token_ids,
        expert_ids,
        num_tokens_post_padded,
        N,
        K,
        EM,
        topk_ids.numel(),
        A.stride(0),
        A.stride(1),
        B.stride(0),
        B.stride(2),
        B.stride(1),
        C.stride(-2),
        C.stride(-1),
        MUL_ROUTED_WEIGHT=mul_routed_weight,
        top_k=top_k,
        compute_type=compute_type,
        even_Ks=(K % bk == 0),
        even_Ns=(N % bn == 0),
        filter_expert=filter_expert,
        **cfg,
    )


OPS = {
    "triton_fused_moe_gemm": lambda **kw: invoke_fused_moe_gemm(**kw),
}


def _moe_fix(kw: dict) -> dict:
    """Same reconstruction as baseline/entry.py: compute_type is recorded as a name."""
    a = kw.get("A")
    dt = a.dtype if torch.is_tensor(a) else torch.bfloat16
    kw["compute_type"] = {
        torch.bfloat16: tl.bfloat16,
        torch.float16: tl.float16,
    }.get(dt, tl.bfloat16)
    kw.setdefault("bias", None)
    return kw


import os as _os
import sys as _sys

_sys.path.insert(
    0, _os.path.join(_os.path.dirname(_os.path.abspath(__file__)), "..", "..", "tools")
)
from derive_inputs import derive as _derive


def _repair(kw):
    return _moe_fix(_derive(kw))


RECONSTRUCT = {"triton_fused_moe_gemm": _repair}
