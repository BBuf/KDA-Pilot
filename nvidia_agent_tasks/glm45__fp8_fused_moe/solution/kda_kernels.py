"""Triton kernels for the glm45__fp8_fused_moe candidate.

Every kernel here is bit-parity-constrained against the shipped SGLang baseline:
the task gate is `torch.testing.assert_close(rtol=1e-5, atol=1e-5)` on bf16
outputs, which one bf16 ulp (~0.4% relative) already exceeds - so each stage
must reproduce the baseline's arithmetic exactly, and only the *schedule* may
change. The freedoms and constraints were established empirically on this box
(see NOTES.md experiment ledger):

* tl.dot fp8e4m3 x fp8e4m3 -> fp32 accumulation is bit-invariant to
  BLOCK_N/BLOCK_K/num_warps/num_stages/GROUP_M retiling when the same Blackwell
  MMA lowering is retained. BM in {64,128} preserves the shipped accumulation
  bits under multi-draw stress; BM in {16,32} can select a different MMA unit
  and produced rare one-ULP flips, so dispatch tables never use those tiles.
* Triton's fp32 `/` lowers to div.full (approximate); the CUDA kernels this
  replaces use IEEE div.rn. Divisions on value paths therefore use inline-asm
  `div.rn.f32`.
* silu in the JIT activation kernel is `x / (1.0f + expf(-x))` with CUDA's
  accurate expf == libdevice exp, and the divide is IEEE - replicated with
  libdevice.exp + div.rn (verified bit-exact on 6.3M samples).
* the per-token fp8 quant kernel computes scale = amax/448 (div.rn),
  scale_inv = 1/scale *unguarded* (an all-zero row quantizes through
  0*inf=NaN -> fminf(NaN,448)=448 -> 0x7E), val = x*scale_inv clamped with
  CUDA fminf/fmaxf NaN semantics, then cvt.rn.satfinite - replicated below.
* the M<=32 combine is inductor's fused kernel: bf16(sum_tree16(f32 vals) * 2.5)
  with a single final rounding; the tree is Triton's tl.sum over a 16-wide
  masked axis - replicated by building the same [*, 16] tensor.
"""

import torch
import triton
import triton.language as tl
from triton.language.extra import libdevice
from triton.language.extra.cuda import gdc_launch_dependents, gdc_wait

# Kernels accept a launch_pdl switch.  The standalone GEMM path uses PDL (and
# its M=32 release/acquire handoff), but the complete dispatch deliberately uses
# ordinary stream serialization.  E37 in NOTES.md records an official-gate-only
# stale-read failure that survived the earlier post-store-trigger hardening;
# disabling early launch for the multi-kernel dispatch removes that entire race
# class while retaining ample row-wise performance margin.  gdc_wait() and
# gdc_launch_dependents() are safe when the launch attribute is disabled.


@triton.jit
def _div_rn(a, b):
    return tl.inline_asm_elementwise(
        "div.rn.f32 $0, $1, $2;",
        "=f,f,f",
        [a, b],
        dtype=tl.float32,
        is_pure=True,
        pack=1,
    )


@triton.jit
def _handshake_init(ready_ptr, pid):
    """Reset this row's flag before releasing the dependent grid."""
    tl.atomic_xchg(ready_ptr + pid, 0, sem="release", scope="gpu")
    gdc_launch_dependents()


@triton.jit
def _handshake_publish(ready_ptr, pid):
    """Release one row after every thread has issued its FP8 output stores."""
    tl.debug_barrier()
    tl.atomic_xchg(ready_ptr + pid, 1, sem="release", scope="gpu")


# --------------------------------------------------------------------------- #
# per-token fp8 quant (bit-parity replica of sglang's JIT per_token_quant_fp8)
# --------------------------------------------------------------------------- #
@triton.jit
def _per_token_quant_fp8_kernel(
    x_ptr,
    q_ptr,
    s_ptr,
    ready_ptr,
    K,
    stride_xm,
    R,
    BLOCK: tl.constexpr,
    NUM_CHUNKS: tl.constexpr,
    ROWS: tl.constexpr,
    EARLY_TRIGGER: tl.constexpr,
    HANDSHAKE: tl.constexpr,
):
    gdc_wait()
    pid = tl.program_id(0).to(tl.int64)
    if HANDSHAKE:
        _handshake_init(ready_ptr, pid)
    if NUM_CHUNKS == 1 and ROWS > 1:
        rows = pid * ROWS + tl.arange(0, ROWS).to(tl.int64)
        rmask = rows < R
        offs = tl.arange(0, BLOCK)
        mask = rmask[:, None] & (offs < K)[None, :]
        x = tl.load(
            x_ptr + rows[:, None] * stride_xm + offs[None, :], mask=mask, other=0.0
        ).to(tl.float32)
        amax = tl.max(tl.where(mask, tl.abs(x), 0.0), 1)
        scale = _div_rn(amax, tl.full((), 448.0, tl.float32))
        scale_inv = _div_rn(tl.full((), 1.0, tl.float32), scale)
        v = x * scale_inv[:, None]
        v = tl.where(v < 448.0, v, 448.0)
        v = tl.where(v > -448.0, v, -448.0)
        tl.store(
            q_ptr + rows[:, None] * K + offs[None, :], v.to(tl.float8e4nv), mask=mask
        )
        tl.store(s_ptr + rows, scale, mask=rmask)
        if HANDSHAKE:
            _handshake_publish(ready_ptr, pid)
        elif EARLY_TRIGGER:
            gdc_launch_dependents()
        return
    base = x_ptr + pid * stride_xm
    offs = tl.arange(0, BLOCK)
    if NUM_CHUNKS == 1:
        x = tl.load(base + offs, mask=offs < K, other=0.0).to(tl.float32)
        amax = tl.max(tl.abs(x), 0)
        scale = _div_rn(amax, tl.full((), 448.0, tl.float32))
        scale_inv = _div_rn(tl.full((), 1.0, tl.float32), scale)
        v = x * scale_inv
        # CUDA fminf/fmaxf semantics: fminf(NaN, 448) = 448
        v = tl.where(v < 448.0, v, 448.0)
        v = tl.where(v > -448.0, v, -448.0)
        tl.store(q_ptr + pid * K + offs, v.to(tl.float8e4nv), mask=offs < K)
        tl.store(s_ptr + pid, scale)
        if HANDSHAKE:
            _handshake_publish(ready_ptr, pid)
        elif EARLY_TRIGGER:
            gdc_launch_dependents()
    else:
        amax = tl.zeros((BLOCK,), dtype=tl.float32)
        for c in tl.static_range(NUM_CHUNKS):
            x = tl.load(base + c * BLOCK + offs, mask=c * BLOCK + offs < K, other=0.0)
            amax = tl.maximum(amax, tl.abs(x.to(tl.float32)))
        amax = tl.max(amax, 0)
        scale = _div_rn(amax, tl.full((), 448.0, tl.float32))
        scale_inv = _div_rn(tl.full((), 1.0, tl.float32), scale)
        for c in tl.static_range(NUM_CHUNKS):
            x = tl.load(base + c * BLOCK + offs, mask=c * BLOCK + offs < K, other=0.0)
            v = x.to(tl.float32) * scale_inv
            v = tl.where(v < 448.0, v, 448.0)
            v = tl.where(v > -448.0, v, -448.0)
            tl.store(
                q_ptr + pid * K + c * BLOCK + offs,
                v.to(tl.float8e4nv),
                mask=c * BLOCK + offs < K,
            )
        tl.store(s_ptr + pid, scale)
        if HANDSHAKE:
            _handshake_publish(ready_ptr, pid)


def per_token_quant_fp8(
    x: torch.Tensor, early_trigger: bool = True, launch_pdl: bool = True
):
    """x [M, K] bf16/fp16 -> contiguous fp8 rows plus fp32 row scales.

    ``early_trigger=False`` preserves ordinary stream completion ordering when
    the immediate dependent launch does not participate in the PDL chain.
    """
    M, K = x.shape
    q = torch.empty(M, K, device=x.device, dtype=torch.float8_e4m3fn)
    s = torch.empty(M, 1, device=x.device, dtype=torch.float32)
    if K <= 2048 or K <= 8192 and M <= 1024:
        block, chunks = triton.next_power_of_2(K), 1
    else:
        block = 1024
        chunks = triton.cdiv(K, block)
    rows = 8 if (chunks == 1 and K <= 2048 and M > 1024) else 1
    _per_token_quant_fp8_kernel[(triton.cdiv(M, rows),)](
        x,
        q,
        s,
        q,
        K,
        x.stride(0),
        M,
        BLOCK=block,
        NUM_CHUNKS=chunks,
        ROWS=rows,
        EARLY_TRIGGER=early_trigger,
        HANDSHAKE=False,
        num_warps=max(4, min(8, block // 256)),
        launch_pdl=launch_pdl,
    )
    return q, s


def per_token_quant_fp8_handshake(x: torch.Tensor):
    """M=32/K=5120 quant with a per-row release/acquire GEMM handoff."""
    M, K = x.shape
    assert M == 32 and K == 5120
    q = torch.empty(M, K, device=x.device, dtype=torch.float8_e4m3fn)
    s = torch.empty(M, 1, device=x.device, dtype=torch.float32)
    ready = torch.empty(M, device=x.device, dtype=torch.int32)
    block = triton.next_power_of_2(K)
    _per_token_quant_fp8_kernel[(M,)](
        x,
        q,
        s,
        ready,
        K,
        x.stride(0),
        M,
        BLOCK=block,
        NUM_CHUNKS=1,
        ROWS=1,
        EARLY_TRIGGER=False,
        HANDSHAKE=True,
        num_warps=8,
        launch_pdl=True,
    )
    return q, s, ready


# --------------------------------------------------------------------------- #
# fused silu_and_mul + per-token fp8 quant of the result
# (baseline: JIT act_and_mul_kernel writes c2 bf16; JIT quant reads c2 -> q.
#  Here: silu*up computed in fp32 exactly as the activation kernel, rounded to
#  bf16 in-register (the value the quant kernel would have read), then the
#  quant replica runs on those bf16 values.)
# --------------------------------------------------------------------------- #
@triton.jit
def _silu_mul_quant_kernel(
    x_ptr,  # [R, 2*HALF] bf16 (gate | up halves)
    q_ptr,  # [R, HALF] fp8
    s_ptr,  # [R] f32
    R,
    HALF: tl.constexpr,
    BLOCK: tl.constexpr,
    ROWS: tl.constexpr,
):
    gdc_wait()
    pid = tl.program_id(0).to(tl.int64)
    rows = pid * ROWS + tl.arange(0, ROWS).to(tl.int64)
    rmask = rows < R
    offs = tl.arange(0, BLOCK)
    mask = rmask[:, None] & (offs < HALF)[None, :]
    gate = tl.load(
        x_ptr + rows[:, None] * 2 * HALF + offs[None, :], mask=mask, other=0.0
    ).to(tl.float32)
    up = tl.load(
        x_ptr + rows[:, None] * 2 * HALF + HALF + offs[None, :], mask=mask, other=0.0
    ).to(tl.float32)
    silu = _div_rn(gate, 1.0 + libdevice.exp(-gate))
    c2 = (silu * up).to(tl.bfloat16)  # the bf16 value the baseline stores
    v32 = c2.to(tl.float32)
    amax = tl.max(tl.where(mask, tl.abs(v32), 0.0), 1)
    scale = _div_rn(amax, tl.full((), 448.0, tl.float32))
    scale_inv = _div_rn(tl.full((), 1.0, tl.float32), scale)
    v = v32 * scale_inv[:, None]
    v = tl.where(v < 448.0, v, 448.0)
    v = tl.where(v > -448.0, v, -448.0)
    tl.store(
        q_ptr + rows[:, None] * HALF + offs[None, :], v.to(tl.float8e4nv), mask=mask
    )
    tl.store(s_ptr + rows, scale, mask=rmask)
    gdc_launch_dependents()


def silu_mul_quant(c1: torch.Tensor, launch_pdl: bool = True):
    """c1 [R, N] bf16 -> (q [R, N//2] fp8, s [R, 1] f32); silu(c1[:, :N/2])*c1[:, N/2:]."""
    R, N = c1.shape
    half = N // 2
    q = torch.empty(R, half, device=c1.device, dtype=torch.float8_e4m3fn)
    s = torch.empty(R, 1, device=c1.device, dtype=torch.float32)
    rows = 1 if R <= 1024 else 8
    _silu_mul_quant_kernel[(triton.cdiv(R, rows),)](
        c1,
        q,
        s,
        R,
        HALF=half,
        BLOCK=triton.next_power_of_2(half),
        ROWS=rows,
        num_warps=4,
        launch_pdl=launch_pdl,
    )
    return q, s


# --------------------------------------------------------------------------- #
# moe_align_block_size replacement (scheduling metadata only - any valid
# expert-grouped layout is numerically equivalent; the kernels only require
# that real slots of one expert form a contiguous prefix of that expert's
# block-aligned segment, which the atomic scatter below guarantees).
# --------------------------------------------------------------------------- #
@triton.jit
def _align_small_prepare_kernel(
    ids_ptr,
    counts_ptr,
    starts_ptr,
    cursor_ptr,
    ntpp_ptr,
    numel,
    BLOCK: tl.constexpr,
    E: tl.constexpr,
    EPOW: tl.constexpr,
    BLOCK_SIZE: tl.constexpr,
):
    """Single-CTA count + prefix scan for the frozen small routing sets."""
    gdc_wait()
    offs = tl.arange(0, BLOCK)
    mask = offs < numel
    e = tl.load(ids_ptr + offs, mask=mask, other=E)
    valid = mask & (e >= 0) & (e < E)
    # Bin E is a dump bucket for masked/invalid lanes and is not published.
    e = tl.where(valid, e, E)
    hist = tl.histogram(e, EPOW)
    bins = tl.arange(0, EPOW)
    emask = bins < E
    cnt = tl.where(emask, hist, 0)
    aligned = tl.cdiv(cnt, BLOCK_SIZE) * BLOCK_SIZE
    cum = tl.cumsum(aligned, 0)
    tl.store(counts_ptr + bins, cnt, mask=emask)
    tl.store(starts_ptr + bins, cum - aligned, mask=emask)
    tl.store(cursor_ptr + bins, 0, mask=emask)
    tl.store(ntpp_ptr, tl.max(cum, 0))


@triton.jit
def _align_small_finish_kernel(
    ids_ptr,
    counts_ptr,
    starts_ptr,
    cursor_ptr,
    expert_ids_ptr,
    sorted_ptr,
    numel,
    E: tl.constexpr,
    EPOW: tl.constexpr,
    SLOT_BLOCK: tl.constexpr,
    BLOCK_SIZE: tl.constexpr,
    MAX_BLOCKS: tl.constexpr,
):
    """Fill block metadata/padding and scatter all real slots in one CTA."""
    gdc_wait()

    experts = tl.arange(0, EPOW)
    emask = experts < E
    cnt = tl.load(counts_ptr + experts, mask=emask, other=0)
    start = tl.load(starts_ptr + experts, mask=emask, other=0)
    nb = tl.cdiv(cnt, BLOCK_SIZE)

    # One expert may own several M blocks.  The frozen small rows need at most
    # MAX_BLOCKS per expert; the output addresses are disjoint across experts.
    blocks = tl.arange(0, MAX_BLOCKS)
    block_mask = emask[:, None] & (blocks[None, :] < nb[:, None])
    block_pos = start[:, None] // BLOCK_SIZE + blocks[None, :]
    tl.store(
        expert_ids_ptr + block_pos,
        experts[:, None].to(tl.int32),
        mask=block_mask,
    )

    # Counts occupy a prefix of each expert segment, so padding is the short
    # tail of at most BLOCK_SIZE-1 slots.  These writes never overlap the real
    # scatter below and therefore need no CTA barrier.
    pads = tl.arange(0, BLOCK_SIZE)
    tail = nb * BLOCK_SIZE - cnt
    pad_mask = emask[:, None] & (pads[None, :] < tail[:, None])
    pad_pos = start[:, None] + cnt[:, None] + pads[None, :]
    tl.store(sorted_ptr + pad_pos, numel, mask=pad_mask)

    slots = tl.arange(0, SLOT_BLOCK)
    slot_mask = slots < numel
    e = tl.load(ids_ptr + slots, mask=slot_mask, other=0)
    valid = slot_mask & (e >= 0) & (e < E)
    within = tl.atomic_add(cursor_ptr + e, 1, mask=valid)
    dst = tl.load(starts_ptr + e, mask=valid, other=0) + within
    tl.store(sorted_ptr + dst, slots.to(tl.int32), mask=valid)
    gdc_launch_dependents()


@triton.jit
def _align_count_kernel(
    ids_ptr, counts_ptr, numel, BLOCK: tl.constexpr, E: tl.constexpr, EPOW: tl.constexpr
):
    gdc_wait()
    pid = tl.program_id(0)
    offs = pid * BLOCK + tl.arange(0, BLOCK)
    mask = offs < numel
    # masked lanes land in the dump bin E, which is never flushed
    e = tl.load(ids_ptr + offs, mask=mask, other=E)
    hist = tl.histogram(e, EPOW)
    bins = tl.arange(0, EPOW)
    tl.atomic_add(counts_ptr + bins, hist, mask=(bins < E) & (hist > 0))


@triton.jit
def _align_scan_kernel(
    counts_ptr,
    starts_ptr,
    ntpp_ptr,
    E: tl.constexpr,
    EPOW: tl.constexpr,
    BLOCK_SIZE: tl.constexpr,
):
    gdc_wait()
    offs = tl.arange(0, EPOW)
    emask = offs < E
    cnt = tl.load(counts_ptr + offs, mask=emask, other=0)
    aligned = tl.cdiv(cnt, BLOCK_SIZE) * BLOCK_SIZE
    cum = tl.cumsum(aligned, 0)
    tl.store(starts_ptr + offs, cum - aligned, mask=emask)
    tl.store(ntpp_ptr, tl.max(cum, 0))


@triton.jit
def _align_fill_kernel(
    counts_ptr,
    starts_ptr,
    expert_ids_ptr,
    sorted_ptr,
    pad_val,
    BLOCK_SIZE: tl.constexpr,
):
    gdc_wait()
    e = tl.program_id(0)
    cnt = tl.load(counts_ptr + e)
    start = tl.load(starts_ptr + e)
    nb = tl.cdiv(cnt, BLOCK_SIZE)
    b0 = start // BLOCK_SIZE
    boffs = tl.arange(0, 64)
    for base in range(0, nb, 64):
        b = base + boffs
        tl.store(expert_ids_ptr + b0 + b, e, mask=b < nb)
    # pad the segment tail [start+cnt, start+nb*BLOCK_SIZE)
    tail = nb * BLOCK_SIZE - cnt
    poffs = tl.arange(0, 128)
    for base in range(0, tail, 128):
        p = base + poffs
        tl.store(sorted_ptr + start + cnt + p, pad_val, mask=p < tail)


@triton.jit
def _align_scatter_kernel(
    ids_ptr, starts_ptr, cursor_ptr, sorted_ptr, numel, BLOCK: tl.constexpr
):
    gdc_wait()
    pid = tl.program_id(0)
    offs = pid * BLOCK + tl.arange(0, BLOCK)
    mask = offs < numel
    e = tl.load(ids_ptr + offs, mask=mask, other=0)
    within = tl.atomic_add(cursor_ptr + e, 1, mask=mask)
    start = tl.load(starts_ptr + e, mask=mask, other=0)
    tl.store(sorted_ptr + start + within, offs.to(tl.int32), mask=mask)
    gdc_launch_dependents()


def moe_align(
    topk_ids: torch.Tensor,
    block_size: int,
    num_experts: int,
    launch_pdl: bool = True,
):
    """Drop-in for sglang's moe_align_block_size (same output contract; slot
    order within an expert is atomic-race order, which is numerically
    irrelevant - every slot's row is computed independently)."""
    numel = topk_ids.numel()
    if numel < num_experts + 1:
        cap = numel * block_size
    else:
        cap = numel + (num_experts + 1) * (block_size - 1)
    dev = topk_ids.device
    sorted_ids = torch.empty(cap, dtype=torch.int32, device=dev)
    max_blocks = triton.cdiv(cap, block_size)
    expert_ids = torch.empty(max_blocks, dtype=torch.int32, device=dev)
    ntpp = torch.empty(1, dtype=torch.int32, device=dev)
    small = numel <= 512
    buf = (
        torch.empty(3 * num_experts, dtype=torch.int32, device=dev)
        if small
        else torch.zeros(3 * num_experts, dtype=torch.int32, device=dev)
    )
    counts, starts, cursor = (
        buf[:num_experts],
        buf[num_experts : 2 * num_experts],
        buf[2 * num_experts :],
    )
    flat = topk_ids.view(-1)
    epow = triton.next_power_of_2(num_experts + 1)
    if small:
        slot_block = triton.next_power_of_2(max(numel, 2))
        max_blocks = triton.next_power_of_2(max(triton.cdiv(numel, block_size), 1))
        _align_small_prepare_kernel[(1,)](
            flat,
            counts,
            starts,
            cursor,
            ntpp,
            numel,
            BLOCK=slot_block,
            E=num_experts,
            EPOW=epow,
            BLOCK_SIZE=block_size,
            num_warps=8,
            launch_pdl=launch_pdl,
        )
        _align_small_finish_kernel[(1,)](
            flat,
            counts,
            starts,
            cursor,
            expert_ids,
            sorted_ids,
            numel,
            E=num_experts,
            EPOW=epow,
            SLOT_BLOCK=slot_block,
            BLOCK_SIZE=block_size,
            MAX_BLOCKS=max_blocks,
            num_warps=8,
            launch_pdl=launch_pdl,
        )
        return sorted_ids, expert_ids, ntpp

    _align_count_kernel[(triton.cdiv(numel, 2048),)](
        flat,
        counts,
        numel,
        BLOCK=2048,
        E=num_experts,
        EPOW=epow,
        num_warps=8,
        launch_pdl=launch_pdl,
    )
    _align_scan_kernel[(1,)](
        counts,
        starts,
        ntpp,
        E=num_experts,
        EPOW=triton.next_power_of_2(num_experts),
        BLOCK_SIZE=block_size,
        launch_pdl=launch_pdl,
    )
    _align_fill_kernel[(num_experts,)](
        counts,
        starts,
        expert_ids,
        sorted_ids,
        numel,
        BLOCK_SIZE=block_size,
        launch_pdl=launch_pdl,
    )
    _align_scatter_kernel[(triton.cdiv(numel, 1024),)](
        flat,
        starts,
        cursor,
        sorted_ids,
        numel,
        BLOCK=1024,
        launch_pdl=launch_pdl,
    )
    return sorted_ids, expert_ids, ntpp


# --------------------------------------------------------------------------- #
# grouped MoE GEMM - schedule-retuned clone of sglang's fused_moe_kernel
# (fp8 w8a8, per-output-channel weight scales, per-token activation scales).
# Extensions over the baseline, none of which touch the value path:
#  * EXPERT_RATIO: expert_ids was built for blocks of BLOCK_SIZE_M*EXPERT_RATIO
#    (reusing the 64/128-aligned routing the GEMM-level rows carry while
#    retiling BLOCK_M down);
#  * skip-pad early-exit: within one align block the real tokens are a
#    contiguous prefix (moe_align scatters real ids at the segment start and
#    leaves the numel-fill after them), so a sub-block whose first sorted id is
#    the pad value writes nothing in the baseline - it can return before
#    loading anything.
#  * SLOT_MODE: decode fast path with no moe_align at all - program m handles
#    exactly slot m (token m // top_k, expert topk_ids[m]); the tile has one
#    valid row. Identical math to a sorted block that contains that slot.
# --------------------------------------------------------------------------- #
@triton.jit
def _moe_gemm_kernel(
    a_ptr,
    b_ptr,
    c_ptr,
    a_scale_ptr,
    b_scale_ptr,
    topk_weights_ptr,
    sorted_token_ids_ptr,
    expert_ids_ptr,
    num_tokens_post_padded_ptr,
    ready_ptr,
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
    stride_bse,
    stride_bsn,
    BLOCK_SIZE_M: tl.constexpr,
    BLOCK_SIZE_N: tl.constexpr,
    BLOCK_SIZE_K: tl.constexpr,
    GROUP_SIZE_M: tl.constexpr,
    MUL_ROUTED_WEIGHT: tl.constexpr,
    top_k: tl.constexpr,
    compute_type: tl.constexpr,
    even_Ks: tl.constexpr,
    EXPERT_RATIO: tl.constexpr,
    SKIP_PAD_BLOCKS: tl.constexpr,
    SLOT_MODE: tl.constexpr,
    B_EVICT: tl.constexpr,
    ROUTING_EXTERNAL: tl.constexpr,
    EARLY_TRIGGER: tl.constexpr,
    HANDSHAKE: tl.constexpr,
):
    if not ROUTING_EXTERNAL:
        gdc_wait()
    pid = tl.program_id(axis=0)
    if SLOT_MODE:
        num_pid_n = tl.cdiv(N, BLOCK_SIZE_N)
        pid_m = pid // num_pid_n
        pid_n = pid % num_pid_n
        offs_m = tl.arange(0, BLOCK_SIZE_M).to(tl.int64)
        slot = pid_m.to(tl.int64)
        offs_token = slot + offs_m  # only row 0 is real
        token_mask = offs_m == 0
        off_experts = tl.load(expert_ids_ptr + slot).to(tl.int64)  # topk_ids flat
    else:
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
        if SKIP_PAD_BLOCKS:
            first_id = tl.load(sorted_token_ids_ptr + pid_m * BLOCK_SIZE_M)
            if first_id >= num_valid_tokens:
                return
        offs_token_id = pid_m * BLOCK_SIZE_M + tl.arange(0, BLOCK_SIZE_M).to(tl.int64)
        offs_token = tl.load(sorted_token_ids_ptr + offs_token_id)
        offs_token = offs_token.to(tl.int64)
        token_mask = offs_token < num_valid_tokens
        off_experts = tl.load(expert_ids_ptr + pid_m // EXPERT_RATIO).to(tl.int64)

    offs_bn = (pid_n * BLOCK_SIZE_N + tl.arange(0, BLOCK_SIZE_N).to(tl.int64)) % N
    offs_k = tl.arange(0, BLOCK_SIZE_K)
    a_ptrs = a_ptr + (
        offs_token[:, None] // top_k * stride_am + offs_k[None, :] * stride_ak
    )
    b_ptrs = (
        b_ptr
        + off_experts * stride_be
        + (offs_k[:, None] * stride_bk + offs_bn[None, :] * stride_bn)
    )

    # per-output-channel weight scale, per-token activation scale
    b_scale_ptrs = (
        b_scale_ptr + off_experts * stride_bse + offs_bn[None, :] * stride_bsn
    )
    b_scale = tl.load(b_scale_ptrs)
    if ROUTING_EXTERNAL:
        # routing arrays and weight scales are workload inputs, not products of
        # the preceding kernel: load them while it is still draining. Under
        # HANDSHAKE the producer triggered at CTA entry, so this wait returns
        # almost immediately - but it is NOT redundant: it is the only
        # guarantee that the producer's pre-trigger flag resets are visible
        # (the trigger itself gives no memory-visibility guarantee), without
        # which the poll below could read a stale/garbage nonzero flag and
        # consume unwritten A/A-scale bytes (the E19/E24/E31 class).
        gdc_wait()
    if HANDSHAKE:
        ready_rows = offs_token // top_k
        row_ready = tl.atomic_add(
            ready_ptr + ready_rows,
            tl.zeros((BLOCK_SIZE_M,), tl.int32),
            mask=token_mask,
            sem="acquire",
            scope="gpu",
        )
        waiting = tl.max(tl.where(token_mask, row_ready == 0, 0), axis=0)
        while waiting != 0:
            row_ready = tl.atomic_add(
                ready_ptr + ready_rows,
                tl.zeros((BLOCK_SIZE_M,), tl.int32),
                mask=token_mask,
                sem="acquire",
                scope="gpu",
            )
            waiting = tl.max(tl.where(token_mask, row_ready == 0, 0), axis=0)
    a_scale_ptrs = a_scale_ptr + (offs_token // top_k)
    a_scale = tl.load(a_scale_ptrs, mask=token_mask, other=0.0)[:, None]

    accumulator = tl.zeros((BLOCK_SIZE_M, BLOCK_SIZE_N), dtype=tl.float32)
    for k_start in range(0, K, BLOCK_SIZE_K):
        if even_Ks:
            a = tl.load(a_ptrs, mask=token_mask[:, None], other=0.0)
            if B_EVICT:
                b = tl.load(b_ptrs, eviction_policy="evict_first")
            else:
                b = tl.load(b_ptrs)
        else:
            a = tl.load(
                a_ptrs,
                mask=token_mask[:, None] & (offs_k[None, :] < K - k_start),
                other=0.0,
            )
            if B_EVICT:
                b = tl.load(
                    b_ptrs,
                    mask=offs_k[:, None] < K - k_start,
                    other=0.0,
                    eviction_policy="evict_first",
                )
            else:
                b = tl.load(b_ptrs, mask=offs_k[:, None] < K - k_start, other=0.0)
        accumulator = tl.dot(a, b, acc=accumulator)
        a_ptrs += BLOCK_SIZE_K * stride_ak
        b_ptrs += BLOCK_SIZE_K * stride_bk

    accumulator *= a_scale * b_scale
    if MUL_ROUTED_WEIGHT:
        moe_weight = tl.load(topk_weights_ptr + offs_token, mask=token_mask, other=0)
        accumulator *= moe_weight[:, None]

    accumulator = accumulator.to(compute_type)
    offs_cn = pid_n * BLOCK_SIZE_N + tl.arange(0, BLOCK_SIZE_N)
    c_ptrs = c_ptr + stride_cm * offs_token[:, None] + stride_cn * offs_cn[None, :]
    c_mask = token_mask[:, None] & (offs_cn[None, :] < N)
    tl.store(c_ptrs, accumulator, mask=c_mask)
    if EARLY_TRIGGER:
        gdc_launch_dependents()


def moe_gemm(
    A_q,
    A_scale,
    B,
    B_scale,
    C,
    topk_weights,
    sorted_token_ids,
    expert_ids,
    num_tokens_post_padded,
    mul_routed_weight,
    top_k,
    config,
    compute_type,
    align_block=None,
    slot_mode=False,
    skip_pad_blocks=True,
    b_evict=False,
    routing_external=False,
    early_trigger=True,
    ready=None,
    handshake=False,
    launch_pdl=True,
):
    """Launch the grouped GEMM. A_q fp8 [M, K]; C bf16 (written through offs_token).

    slot_mode: expert_ids is topk_ids.view(-1); sorted/num_post ignored; grid is
    one configured BLOCK_SIZE_M tile per (slot, n-block), with only row 0 valid.
    handshake: acquire-poll ``ready`` for every live activation row instead of
    relying on the preceding PDL trigger for those row stores.
    """
    if handshake:
        assert routing_external and ready is not None
    N = B.shape[1]
    K = B.shape[2]
    bm = config["BLOCK_SIZE_M"]
    if slot_mode:
        num_slots = expert_ids.numel()
        grid = (num_slots * triton.cdiv(N, config["BLOCK_SIZE_N"]),)
        EM = num_slots
        ratio = 1
        sorted_arg = expert_ids  # unused in kernel, any tensor
        ntpp_arg = expert_ids
    else:
        EM = sorted_token_ids.shape[0]
        if align_block is None:
            align_block = bm
        assert align_block % bm == 0
        ratio = align_block // bm
        grid = (triton.cdiv(EM, bm) * triton.cdiv(N, config["BLOCK_SIZE_N"]),)
        sorted_arg = sorted_token_ids
        ntpp_arg = num_tokens_post_padded
    even_Ks = (K % config["BLOCK_SIZE_K"]) == 0
    _moe_gemm_kernel[grid](
        A_q,
        B,
        C,
        A_scale,
        B_scale,
        topk_weights,
        sorted_arg,
        expert_ids,
        ntpp_arg,
        C if ready is None else ready,
        N,
        K,
        EM,
        topk_weights.numel() if not slot_mode else expert_ids.numel(),
        A_q.stride(0),
        A_q.stride(1),
        B.stride(0),
        B.stride(2),
        B.stride(1),
        C.stride(-2),
        C.stride(-1),
        B_scale.stride(0),
        B_scale.stride(1),
        BLOCK_SIZE_M=bm,
        BLOCK_SIZE_N=config["BLOCK_SIZE_N"],
        BLOCK_SIZE_K=config["BLOCK_SIZE_K"],
        GROUP_SIZE_M=config.get("GROUP_SIZE_M", 1),
        MUL_ROUTED_WEIGHT=mul_routed_weight,
        top_k=top_k,
        compute_type=compute_type,
        even_Ks=even_Ks,
        EXPERT_RATIO=ratio,
        SKIP_PAD_BLOCKS=skip_pad_blocks,
        SLOT_MODE=slot_mode,
        B_EVICT=b_evict,
        ROUTING_EXTERNAL=routing_external,
        EARLY_TRIGGER=early_trigger,
        HANDSHAKE=handshake,
        num_warps=config.get("num_warps", 4),
        num_stages=config.get("num_stages", 4),
        launch_pdl=launch_pdl,
    )


# --------------------------------------------------------------------------- #
# standalone combine replica of inductor's fused sum*rsf kernel (M <= 32 path)
# --------------------------------------------------------------------------- #
@triton.jit
def _combine_kernel(
    x_ptr,  # [M, TOPK, N] bf16
    out_ptr,  # [M, N] bf16
    xnumel,
    N,
    rsf,
    TOPK: tl.constexpr,
    XBLOCK: tl.constexpr,
):
    gdc_wait()
    xoffset = tl.program_id(0) * XBLOCK
    xindex = xoffset + tl.arange(0, XBLOCK)[:, None]
    xmask = xindex < xnumel
    r0_index = tl.arange(0, 16)[None, :]
    r0_mask = r0_index < TOPK
    x0 = xindex % N
    x1 = xindex // N
    tmp0 = tl.load(
        x_ptr + (x0 + N * r0_index + TOPK * N * x1), r0_mask & xmask, other=0.0
    ).to(tl.float32)
    tmp3 = tl.where(r0_mask, tmp0, 0)
    tmp4 = tl.sum(tmp3, 1)[:, None].to(tl.float32)
    tmp6 = tmp4 * rsf
    # op-terminal kernel: no early trigger (see the module comment on tails)
    tl.store(out_ptr + xindex, tmp6, xmask)


def combine_small(x, out, routed_scaling_factor, launch_pdl=True):
    """x [M, TOPK, N] bf16 -> out [M, N] bf16 = bf16(sum(x, 1) * rsf), inductor parity."""
    M, topk, N = x.shape
    xnumel = M * N
    XBLOCK = 128
    _combine_kernel[(triton.cdiv(xnumel, XBLOCK),)](
        x,
        out,
        xnumel,
        N,
        routed_scaling_factor,
        TOPK=topk,
        XBLOCK=XBLOCK,
        num_warps=8,
        launch_pdl=launch_pdl,
    )


# --------------------------------------------------------------------------- #
# combine replica of sgl_kernel's moe_sum_reduce (M > 32 path): per element
# acc = sum_k(f32(x[t,k,d])) in ascending k, acc *= rsf, one bf16 rounding.
# --------------------------------------------------------------------------- #
@triton.jit
def _sum_reduce_kernel(
    x_ptr,
    out_ptr,
    xnumel,
    N,
    rsf,
    TOPK: tl.constexpr,
    XBLOCK: tl.constexpr,
):
    gdc_wait()
    xindex = tl.program_id(0).to(tl.int64) * XBLOCK + tl.arange(0, XBLOCK).to(tl.int64)
    xmask = xindex < xnumel
    d = xindex % N
    t = xindex // N
    base = x_ptr + t * (TOPK * N) + d
    acc = tl.zeros((XBLOCK,), dtype=tl.float32)
    for k in tl.static_range(TOPK):
        acc += tl.load(base + k * N, mask=xmask, other=0.0).to(tl.float32)
    acc = acc * rsf
    # op-terminal kernel: no early trigger (see the module comment on tails)
    tl.store(out_ptr + xindex, acc.to(tl.bfloat16), mask=xmask)


def sum_reduce_big(x, out, routed_scaling_factor, launch_pdl=True):
    """x [M, TOPK, N] bf16 -> out [M, N] bf16, sgl moe_sum_reduce parity."""
    M, topk, N = x.shape
    xnumel = M * N
    XBLOCK = 512
    _sum_reduce_kernel[(triton.cdiv(xnumel, XBLOCK),)](
        x,
        out,
        xnumel,
        N,
        routed_scaling_factor,
        TOPK=topk,
        XBLOCK=XBLOCK,
        num_warps=4,
        launch_pdl=launch_pdl,
    )
