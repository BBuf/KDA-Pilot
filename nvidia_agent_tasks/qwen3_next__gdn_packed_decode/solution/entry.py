"""Candidate for `qwen3_next__gdn_packed_decode`.

CUDA row-streaming port of `fused_recurrent_gated_delta_rule_packed_decode_kernel`
(the GDN analogue of sglang's KDA packed-decode CUDA kernel). The Triton baseline
holds a [BV=32, K=128] fp32 state tile in the registers of a single-warp program
and launches a grid of only 4*B such programs: 16 warps for the whole GPU at
B=1, and a per-warp serial tile walk that leaves it ~flat at 5-6 us of kernel
time across the whole captured batch range (B=1..32, CUPTI-timed).

This kernel streams the state instead, two V-rows per warp through 256-bit
accesses: lanes 0..15 own row r and lanes 16..31 own row r+1 (8 consecutive
K-elements per lane), so one 4-round half-warp butterfly reduces both rows in
the same shuffle instructions and each warp issues a single 1KB-contiguous
load+store pair per row pair - which streams measurably better on B300 HBM
than the 512B float4 variant we also tried (6.0 vs 7.4 us at B=32). Each
(sequence, v-head) is split across SPLIT CTAs so small batches fill the
machine; setup (l2-normed q/k, gate, beta) is computed redundantly per warp
and there is no __syncthreads anywhere.

The recurrence is unchanged: full K window, fp32 state, every touched slot
written back in place, the same gate math in the same order
(g = -exp(A_log) * softplus(a + dt_bias), beta = sigmoid(b) rounded through
bf16 exactly like the Triton kernel), and rows with a negative cache index
only zero their output. Only the reduction order differs from tl.sum (warp
shuffles), so outputs match the baseline to ULPs, not bits: the shipped
16-step chain gate passes at final-state rel err ~3e-7 against rtol 2e-2.

Two kernel bodies share that math. The generic one (cfg 0-3) is the fallback
for unseen layouts. The lean one (cfg 4+) bakes the frozen decode layout in as
constants (HV=4, H=2, 65536-float slot pitch; asserted host-side), issues the
index load first, puts every state row in flight through a clamped slot address
before the padding branch, and uses hardware approximation intrinsics
(__expf/__logf/rsqrtf/__fdividef) for the per-warp scalar setup. Frozen B <= 6
uses its maximum-split cfg4 latency shape; B >= 13 uses cfg5, the same proven
two-warp/four-row geometry as generic cfg3 with less setup code and two fewer
registers. The formulas and order are unchanged, the fp32 state recurrence
stays exact, and both active shapes pass the full 16-step chain gate.
"""

import os
import sys

import torch
from torch.utils.cpp_extension import load_inline

sys.path.insert(
    0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "tools")
)
from derive_inputs import derive

_CUDA_SRC = r"""
#include <cuda_bf16.h>
#include <cstdint>

namespace {

struct Params {
  const __nv_bfloat16* __restrict__ mixed_qkv;  // [B, 2*H*K + HV*V]
  const __nv_bfloat16* __restrict__ a;          // [B, HV]
  const __nv_bfloat16* __restrict__ b;          // [B, HV]
  const float* __restrict__ A_log;              // [HV]
  const __nv_bfloat16* __restrict__ dt_bias;    // [HV]
  __nv_bfloat16* __restrict__ o;                // [B, HV, V] contiguous
  float* __restrict__ state;                    // pool, slot pitch = stride_state
  const int32_t* __restrict__ indices;          // [B]
  int64_t stride_mixed;
  int64_t stride_a;
  int64_t stride_b;
  int64_t stride_state;
  int32_t H;
  int32_t HV;
  float scale;
};

// 8 consecutive bf16 as one 16-byte load.
__device__ __forceinline__ void load_bf16x8(const __nv_bfloat16* p, float out[8]) {
  const uint4 raw = *reinterpret_cast<const uint4*>(p);
  const uint32_t words[4] = {raw.x, raw.y, raw.z, raw.w};
#pragma unroll
  for (int i = 0; i < 4; ++i) {
    const __nv_bfloat162 pair = *reinterpret_cast<const __nv_bfloat162*>(&words[i]);
    out[2 * i] = __bfloat162float(pair.x);
    out[2 * i + 1] = __bfloat162float(pair.y);
  }
}

// 256-bit state accesses (sm_100+).
struct alignas(32) f32x8 {
  float v[8];
};

__device__ __forceinline__ f32x8 ld256(const float* p) {
  f32x8 r;
  asm volatile("ld.global.v8.f32 {%0,%1,%2,%3,%4,%5,%6,%7}, [%8];"
               : "=f"(r.v[0]), "=f"(r.v[1]), "=f"(r.v[2]), "=f"(r.v[3]),
                 "=f"(r.v[4]), "=f"(r.v[5]), "=f"(r.v[6]), "=f"(r.v[7])
               : "l"(p));
  return r;
}

__device__ __forceinline__ void st256(float* p, const f32x8& r) {
  asm volatile("st.global.v8.f32 [%0], {%1,%2,%3,%4,%5,%6,%7,%8};"
               :: "l"(p), "f"(r.v[0]), "f"(r.v[1]), "f"(r.v[2]), "f"(r.v[3]),
                  "f"(r.v[4]), "f"(r.v[5]), "f"(r.v[6]), "f"(r.v[7]) : "memory");
}

// Butterfly over one 16-lane half (offsets 8..1 never cross bit 4): both
// halves reduce their own row in the same instructions, two sums interleaved.
__device__ __forceinline__ void half_sum2(float& x, float& y) {
#pragma unroll
  for (int off = 8; off > 0; off >>= 1) {
    x += __shfl_xor_sync(0xffffffffu, x, off);
    y += __shfl_xor_sync(0xffffffffu, y, off);
  }
}

// K = V = 128 specialization. Each CTA covers V/SPLIT rows of one
// (sequence, v-head); its WARPS warps take ROWS = V/(SPLIT*WARPS) consecutive
// rows each, two per iteration (lanes 0..15 row r, lanes 16..31 row r+1).
template <int WARPS, int SPLIT>
__global__ __launch_bounds__(WARPS * 32) void gdn_packed_decode_kernel_v8(const Params p) {
  constexpr int K = 128;
  constexpr int V = 128;
  constexpr int ROWS = V / (SPLIT * WARPS);
  static_assert(ROWS % 2 == 0, "v8 path needs an even row count per warp");
  const uint32_t i_nh = blockIdx.x / SPLIT;
  const uint32_t chunk = blockIdx.x % SPLIT;
  const uint32_t n = i_nh / p.HV;
  const uint32_t hv = i_nh % p.HV;
  const uint32_t i_h = hv / (p.HV / p.H);
  const uint32_t warp = threadIdx.x >> 5;
  const uint32_t lane = threadIdx.x & 31;
  const uint32_t half = lane >> 4;
  const uint32_t hl = lane & 15;

  // Issue every load that does not depend on the slot index before the
  // padding branch: under the harness's cold-L2 regime each of these is a
  // full-latency fetch, and the slot index -> state row chain is the one
  // dependency that cannot be broken, so everything else overlaps it.
  const int64_t sidx = p.indices[n];
  const __nv_bfloat16* mixed = p.mixed_qkv + n * p.stride_mixed;
  const uint32_t e0 = hl * 8;
  float q[8], k[8];
  load_bf16x8(mixed + i_h * K + e0, q);
  load_bf16x8(mixed + p.H * K + i_h * K + e0, k);
  const float a_raw = __bfloat162float(p.a[n * p.stride_a + hv]);
  const float b_raw = __bfloat162float(p.b[n * p.stride_b + hv]);
  const float dtb = __bfloat162float(p.dt_bias[hv]);
  const float A_val = p.A_log[hv];
  const __nv_bfloat16* v_ptr = mixed + 2 * p.H * K + hv * V;
  const int r0 = chunk * (V / SPLIT) + warp * ROWS;
  float vv;
  float vv_next;
  if constexpr (ROWS > 2) {
    vv = __bfloat162float(v_ptr[r0 + half]);
    vv_next = __bfloat162float(v_ptr[r0 + half + 2]);
  }

  __nv_bfloat16* o_ptr = p.o + (static_cast<int64_t>(n) * p.HV + hv) * V;
  if (sidx < 0) {
    // Padded cuda-graph slot: zero this CTA's slice of the output, leave the
    // pool alone.
    for (int i = threadIdx.x; i < V / SPLIT; i += WARPS * 32)
      o_ptr[chunk * (V / SPLIT) + i] = __float2bfloat16(0.0f);
    return;
  }

  // The first state address is now known, so put its dependent global load in
  // flight before the norm/gate setup.  That setup is independent work long
  // enough to cover a useful fraction of the cold state-fetch latency.
  float* h_base = p.state + sidx * p.stride_state + static_cast<int64_t>(hv) * (V * K);
  f32x8 h8;
  f32x8 h8_next;
  if constexpr (ROWS > 2) {
    h8 = ld256(h_base + (r0 + half) * K + e0);
    h8_next = ld256(h_base + (r0 + half + 2) * K + e0);
  }

  // --- per-warp redundant setup ---
  // tl: q / sqrt(sum(q*q) + 1e-6), then * scale. <k, q> of the normalized
  // vectors is the raw dot rescaled, so one 3-way butterfly covers setup.
  float q_sq = 0.0f, k_sq = 0.0f, qk = 0.0f;
#pragma unroll
  for (int e = 0; e < 8; ++e) {
    q_sq += q[e] * q[e];
    k_sq += k[e] * k[e];
    qk += q[e] * k[e];
  }
#pragma unroll
  for (int off = 8; off > 0; off >>= 1) {
    q_sq += __shfl_xor_sync(0xffffffffu, q_sq, off);
    k_sq += __shfl_xor_sync(0xffffffffu, k_sq, off);
    qk += __shfl_xor_sync(0xffffffffu, qk, off);
  }
  const float q_inv = 1.0f / sqrtf(q_sq + 1e-6f);
  const float k_inv = 1.0f / sqrtf(k_sq + 1e-6f);
  const float kq = qk * q_inv * p.scale * k_inv;
#pragma unroll
  for (int e = 0; e < 8; ++e) {
    q[e] = q[e] * q_inv * p.scale;
    k[e] = k[e] * k_inv;
  }

  // Gate math in the Triton kernel's order: x = a + dt_bias (both loaded to
  // fp32), softplus with the 20.0 threshold, g = -exp(A_log) * softplus(x),
  // decay = exp(g). beta keeps the kernel's bf16 round-trip of sigmoid(b).
  const float x = a_raw + dtb;
  const float sp = (x <= 20.0f) ? logf(1.0f + expf(x)) : x;
  const float g = -expf(A_val) * sp;
  const float decay = expf(g);
  const float beta = __bfloat162float(__float2bfloat16(1.0f / (1.0f + expf(-b_raw))));

  // --- stream this warp's V-rows, two per iteration ---
  // The state math is the Triton kernel's, element for element: hd = h*decay,
  // then h_new = fma(v_new, k, hd). Only the output is reassociated
  // (o = <hd, q> + v_new * <k, q>) so its reduction shares the <hd, k>
  // butterfly instead of waiting on the state update.
#pragma unroll(ROWS < 8 ? ROWS / 2 : 4)
  for (int r = r0; r < r0 + ROWS; r += 2) {
    const int my_r = r + half;
    if constexpr (ROWS == 2)
      vv = __bfloat162float(v_ptr[my_r]);
    if constexpr (ROWS == 2)
      h8 = ld256(h_base + my_r * K + e0);
    float hd[8];
    float t = 0.0f, u = 0.0f;
#pragma unroll
    for (int e = 0; e < 8; ++e) {
      hd[e] = h8.v[e] * decay;
      t += hd[e] * k[e];
      u += hd[e] * q[e];
    }
    // `h8` is dead once `hd` is formed. Advance to the row pair that was put
    // in flight beside the first load, before the independent setup work.
    if constexpr (ROWS > 2) {
      if (r + 2 < r0 + ROWS)
        h8 = h8_next;
    }
    half_sum2(t, u);
    const float v_new = (vv - t) * beta;
    f32x8 h;
#pragma unroll
    for (int e = 0; e < 8; ++e) h.v[e] = fmaf(v_new, k[e], hd[e]);
    st256(h_base + my_r * K + e0, h);
    if (hl == 0) o_ptr[my_r] = __float2bfloat16(u + v_new * kq);
    if constexpr (ROWS > 2) {
      if (r + 2 < r0 + ROWS)
        vv = vv_next;
    }
  }
}

// Lean fixed-layout variant. At B <= 6 the kernel is not bandwidth-bound: its
// span is two serial cold-DRAM hops (cache_indices -> state rows) plus launch,
// cold instruction fetch, and the tail, so the wins here are issue-order and
// code size, not FLOPs. HV=4, H=2, K=V=128 and the 65536-float slot pitch are
// frozen workload facts (asserted host-side), so the whole preamble reduces to
// shifts and the index load issues within the first instructions. Every state
// row-pair is put in flight through a clamped slot address before the padding
// branch resolves and before any setup math, and the setup uses the hardware
// approximation intrinsics (__expf/__logf/rsqrtf/__fdividef): same formulas in
// the same order as the Triton kernel, ~2-8 ulp on the scalar gate/norm
// values, validated against the full 16-step captured state chain. The
// recurrence itself stays exact: fp32 hd = h*decay, v_new = (vv - <hd,k>)*beta
// rounded once, h_new = fma(v_new, k, hd), every touched slot written back.
template <int WARPS, int SPLIT>
__global__ __launch_bounds__(WARPS * 32) void gdn_packed_decode_kernel_lean(const Params p) {
  constexpr int K = 128;
  constexpr int V = 128;
  constexpr int ROWS = V / (SPLIT * WARPS);
  constexpr int PAIRS = ROWS / 2;
  constexpr uint32_t LOG_SPLIT =
      (SPLIT == 64) ? 6u : (SPLIT == 32) ? 5u : (SPLIT == 16) ? 4u : 3u;
  static_assert(SPLIT == 64 || SPLIT == 32 || SPLIT == 16 || SPLIT == 8,
                "lean split table");
  static_assert(ROWS == 2 || ROWS == 4 || ROWS == 8, "lean rows per warp");
  const uint32_t i_nh = blockIdx.x >> LOG_SPLIT;
  const uint32_t chunk = blockIdx.x & (SPLIT - 1);
  const uint32_t n = i_nh >> 2;
  const uint32_t hv = i_nh & 3u;
  const uint32_t warp = threadIdx.x >> 5;
  const uint32_t lane = threadIdx.x & 31;
  const uint32_t half = lane >> 4;
  const uint32_t hl = lane & 15;

  const int64_t sidx = p.indices[n];  // hop 1: the one unbreakable dependency
  const __nv_bfloat16* mixed = p.mixed_qkv + n * p.stride_mixed;
  const uint32_t e0 = hl * 8;
  const uint32_t qoff = (hv >> 1) * K + e0;
  float q[8], k[8];
  load_bf16x8(mixed + qoff, q);
  load_bf16x8(mixed + 2 * K + qoff, k);
  const float a_raw = __bfloat162float(p.a[n * p.stride_a + hv]);
  const float b_raw = __bfloat162float(p.b[n * p.stride_b + hv]);
  const float dtb = __bfloat162float(p.dt_bias[hv]);
  const float A_val = p.A_log[hv];
  const __nv_bfloat16* v_ptr = mixed + 4 * K + hv * V;
  const int r0 = chunk * (V / SPLIT) + warp * ROWS;
  float vv[PAIRS];
#pragma unroll
  for (int j = 0; j < PAIRS; ++j)
    vv[j] = __bfloat162float(v_ptr[r0 + 2 * j + half]);

  // hop 2, issued the moment sidx lands: clamp padded slots to row 0 so the
  // loads never wait on the branch; padded CTAs discard and return below.
  float* h_base = p.state + ((sidx < 0 ? int64_t{0} : sidx) << 16) +
                  (static_cast<int64_t>(hv) << 14);
  f32x8 hb[PAIRS];
#pragma unroll
  for (int j = 0; j < PAIRS; ++j)
    hb[j] = ld256(h_base + (r0 + 2 * j + half) * K + e0);

  __nv_bfloat16* o_ptr = p.o + (static_cast<int64_t>(n) * 4 + hv) * V;
  if (sidx < 0) {
    for (int i = threadIdx.x; i < V / SPLIT; i += WARPS * 32)
      o_ptr[chunk * (V / SPLIT) + i] = __float2bfloat16(0.0f);
    return;
  }

  // Redundant per-warp setup, fully shadowed by the state-row flight.
  float q_sq = 0.0f, k_sq = 0.0f, qk = 0.0f;
#pragma unroll
  for (int e = 0; e < 8; ++e) {
    q_sq += q[e] * q[e];
    k_sq += k[e] * k[e];
    qk += q[e] * k[e];
  }
#pragma unroll
  for (int off = 8; off > 0; off >>= 1) {
    q_sq += __shfl_xor_sync(0xffffffffu, q_sq, off);
    k_sq += __shfl_xor_sync(0xffffffffu, k_sq, off);
    qk += __shfl_xor_sync(0xffffffffu, qk, off);
  }
  const float q_inv = rsqrtf(q_sq + 1e-6f);
  const float k_inv = rsqrtf(k_sq + 1e-6f);
  const float kq = qk * q_inv * p.scale * k_inv;
#pragma unroll
  for (int e = 0; e < 8; ++e) {
    q[e] = q[e] * q_inv * p.scale;
    k[e] = k[e] * k_inv;
  }
  const float x = a_raw + dtb;
  const float sp = (x <= 20.0f) ? __logf(1.0f + __expf(x)) : x;
  const float g = -__expf(A_val) * sp;
  const float decay = __expf(g);
  const float beta =
      __bfloat162float(__float2bfloat16(__fdividef(1.0f, 1.0f + __expf(-b_raw))));

#pragma unroll
  for (int j = 0; j < PAIRS; ++j) {
    const int my_r = r0 + 2 * j + half;
    float hd[8];
    float t = 0.0f, u = 0.0f;
#pragma unroll
    for (int e = 0; e < 8; ++e) {
      hd[e] = hb[j].v[e] * decay;
      t += hd[e] * k[e];
      u += hd[e] * q[e];
    }
    half_sum2(t, u);
    const float v_new = (vv[j] - t) * beta;
    f32x8 h;
#pragma unroll
    for (int e = 0; e < 8; ++e) h.v[e] = fmaf(v_new, k[e], hd[e]);
    st256(h_base + my_r * K + e0, h);
    if (hl == 0) o_ptr[my_r] = __float2bfloat16(u + v_new * kq);
  }
}

}  // namespace

// cfg -> (WARPS, SPLIT); grid is B*HV*SPLIT CTAs of WARPS*32 threads.
#define GDN_CASE(ID, W, S)                                                          \
  case ID:                                                                          \
    gdn_packed_decode_kernel_v8<W, S><<<nh * S, W * 32, 0, stream>>>(p);            \
    break;
#define GDN_LEAN_CASE(ID, W, S)                                                     \
  case ID:                                                                          \
    gdn_packed_decode_kernel_lean<W, S><<<nh * S, W * 32, 0, stream>>>(p);          \
    break;

extern "C" void gdn_launch(Params p, int B, int cfg, cudaStream_t stream) {
  const int nh = B * p.HV;
  switch (cfg) {
    GDN_CASE(0, 1, 64)
    GDN_CASE(1, 2, 32)
    GDN_CASE(2, 4, 16)
    GDN_LEAN_CASE(4, 1, 64)
    GDN_LEAN_CASE(5, 2, 16)
    default:
    GDN_CASE(3, 2, 16)
  }
}
"""

_CPP_SRC = r"""
#include <torch/extension.h>
#include <c10/cuda/CUDAStream.h>
#include <cuda_runtime_api.h>
#include <cstdint>

struct Params {
  const void* mixed_qkv;
  const void* a;
  const void* b;
  const float* A_log;
  const void* dt_bias;
  void* o;
  float* state;
  const int32_t* indices;
  int64_t stride_mixed;
  int64_t stride_a;
  int64_t stride_b;
  int64_t stride_state;
  int32_t H;
  int32_t HV;
  float scale;
};

extern "C" void gdn_launch(Params p, int B, int cfg, cudaStream_t stream);

void gdn_packed_decode(at::Tensor mixed_qkv, at::Tensor a, at::Tensor b, at::Tensor A_log,
                       at::Tensor dt_bias, double scale, at::Tensor ssm_states, at::Tensor out,
                       at::Tensor cache_indices, int64_t H, int64_t cfg) {
  const auto B = static_cast<int>(mixed_qkv.size(0));
  const auto HV = static_cast<int>(ssm_states.size(-3));
  Params p{mixed_qkv.const_data_ptr(),
           a.const_data_ptr(),
           b.const_data_ptr(),
           A_log.const_data_ptr<float>(),
           dt_bias.const_data_ptr(),
           out.data_ptr(),
           ssm_states.data_ptr<float>(),
           cache_indices.const_data_ptr<int32_t>(),
           mixed_qkv.stride(0),
           a.stride(0),
           b.stride(0),
           ssm_states.stride(-4),
           static_cast<int32_t>(H),
           static_cast<int32_t>(HV),
           static_cast<float>(scale)};
  gdn_launch(p, B, static_cast<int>(cfg), at::cuda::getCurrentCUDAStream());
}
"""

_mod = load_inline(
    name="gdn_packed_decode_candidate",
    cpp_sources=[_CPP_SRC],
    cuda_sources=[_CUDA_SRC],
    functions=["gdn_packed_decode"],
    # Keep line mappings in the shipped cubin so profiler collections can
    # attribute scheduler stalls to the exact state-streaming operations.
    # `-lineinfo` does not enable device debug code or change optimization.
    extra_cuda_cflags=["-O3", "-lineinfo"],
    verbose=False,
)

# Per-batch launch config, tuned on this box (see
# docs/gdn_packed_decode_optimization.md for the sweep): cfg -> (WARPS, SPLIT)
# per the switch in _CUDA_SRC. Grid is B*HV*SPLIT CTAs, ROWS=V/(SPLIT*WARPS)
# rows per warp. Small batches take the lean kernel (cfg4): their span is
# latency + launch + code fetch, and trimming those moved B<=3 into the next
# 2.048us timer bucket. B>=13 takes the lean body at the same W2/S16/R4
# double-prefetch geometry as cfg3; CUPTI resolves the largest win at B=32.
_CFG = {1: 4, 2: 4, 3: 4, 5: 4, 6: 4, 13: 5, 16: 5, 32: 5}


def _cfg_for(batch: int) -> int:
    if batch in _CFG:
        return _CFG[batch]
    return 3  # (2,16) R4: two state-row pairs prefetched across setup


def _run(
    mixed_qkv,
    a,
    b,
    A_log,
    dt_bias,
    scale,
    ssm_states,
    cache_indices,
    num_v_heads,
    head_v_dim,
    **kwargs,
):
    B = mixed_qkv.shape[0]
    HV, V, K = ssm_states.shape[-3:]
    assert (
        K == 128
        and V == 128
        and mixed_qkv.dtype == torch.bfloat16
        and ssm_states.dtype == torch.float32
        and ssm_states.stride(-1) == 1
        and ssm_states.stride(-2) == K
        and ssm_states.stride(-3) == V * K
        and cache_indices.dtype == torch.int32
        and mixed_qkv.stride(-1) == 1
        and a.stride(-1) == 1
        and b.stride(-1) == 1
    )
    H = (mixed_qkv.shape[1] - HV * V) // (2 * K)
    cfg = _cfg_for(B)
    if cfg >= 4:
        # The lean small-batch kernels bake in the frozen decode layout.
        assert HV == 4 and H == 2 and ssm_states.stride(-4) == 65536
    out = mixed_qkv.new_empty(B, 1, num_v_heads, head_v_dim)
    _mod.gdn_packed_decode(
        mixed_qkv,
        a,
        b,
        A_log,
        dt_bias,
        float(scale),
        ssm_states,
        out,
        cache_indices,
        H,
        cfg,
    )
    # [B, 1, HV, V] -> [1, B, HV, V], a view, matching the baseline's return layout.
    return out.transpose(0, 1)


OPS = {"gdn_decode_packed_triton": _run}

# The kernel returns `out` *and* advances this batch's slots in `ssm_states` in
# place; declaring the state as an output keeps the gate looking at it.
OUTPUT_ARGS = {"gdn_decode_packed_triton": ("ssm_states",)}


def _repair(kw):
    """Same address-argument repair as the baseline (`derive`), with one
    distinction the chain replay needs: a chain step ships a compact state pool
    holding exactly the touched rows plus already-remapped indices - every
    tensor in it is real capture data, so there is nothing to repair (running
    `derive` there would clamp the real, negative `dt_bias`)."""
    ssm = kw.get("ssm_states")
    idx = kw.get("cache_indices")
    if torch.is_tensor(ssm) and torch.is_tensor(idx) and ssm.shape[0] <= idx.numel():
        return kw
    return derive(kw)


RECONSTRUCT = {"gdn_decode_packed_triton": _repair}
