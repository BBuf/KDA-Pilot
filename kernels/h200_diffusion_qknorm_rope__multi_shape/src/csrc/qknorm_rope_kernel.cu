// Fused in-place QK-Norm + RoPE for NVIDIA H200 (SM90 / Hopper).
//
// Source lineage: ported from the promoted sibling B200 implementation
// (kda_kernels/diffusion/qknorm_rope/_impls/b200/csrc/qknorm_rope_kernel.cu).
// The kernel is SM-agnostic (warp shuffles, vectorized 64/128-bit loads,
// cudaOccupancyMaxActiveBlocksPerMultiprocessor grid sizing; no SM100-only
// tcgen05/TMEM), so it rebuilds for sm_90 unchanged.
//
// Clean-room native CUDA implementation of the SGLang diffusion
// `fused_inplace_qknorm_rope` semantics, built from workspace-owned sources via
// torch's C++/CUDA extension toolchain (no dependency on SGLang-internal
// headers). One warp normalizes (RMSNorm over the full head_dim, fp32
// accumulation) and rotates (RoPE) one (token, head) vector, in place.
//
// Production fast path: bf16, contiguous, head_dim=128, rope_dim=128,
// is_neox=False, equal Q/K head counts, int32/int64 positions.

#include <torch/extension.h>
#include <ATen/cuda/CUDAContext.h>

#include <cuda.h>
#include <cuda_runtime.h>
#include <cuda_bf16.h>

#include <algorithm>

namespace {

constexpr int kWarpSize = 32;
constexpr int kThreadsPerBlock = 256;
constexpr int kWarpsPerBlock = kThreadsPerBlock / kWarpSize;  // 8

__device__ __forceinline__ float warp_reduce_sum(float v) {
#pragma unroll
  for (int offset = kWarpSize / 2; offset > 0; offset >>= 1) {
    v += __shfl_xor_sync(0xffffffffu, v, offset);
  }
  return v;
}

// One warp owns one (token, head) head-vector. Each lane owns ELEMS = D/32
// contiguous bf16 elements, loaded/stored as a single 8-byte (64-bit) access.
template <int HEAD_DIM, int ROPE_DIM, bool IS_NEOX, typename IdType>
__global__ void fused_qknorm_rope_kernel(
    __nv_bfloat16* __restrict__ q,
    __nv_bfloat16* __restrict__ k,
    const __nv_bfloat16* __restrict__ q_weight,
    const __nv_bfloat16* __restrict__ k_weight,
    const float* __restrict__ cos_sin_cache,
    const IdType* __restrict__ positions,
    float eps,
    int num_tokens,
    int num_qo_heads,
    int num_kv_heads,
    long q_row_stride,
    long k_row_stride,
    long head_stride) {
  constexpr int kElems = HEAD_DIM / kWarpSize;          // 4 for head_dim=128
  constexpr int kRotaryLanes = ROPE_DIM / kElems;       // 32 for rope_dim=128
  constexpr int kHalfRotaryLanes = kRotaryLanes / 2;
  static_assert(HEAD_DIM % kWarpSize == 0, "head_dim must be a multiple of 32");
  static_assert(kElems == 4, "this fast path is specialized for 4 elems/lane (head_dim=128)");
  static_assert(ROPE_DIM > 0 && ROPE_DIM <= HEAD_DIM, "invalid rope_dim");
  static_assert(ROPE_DIM % kElems == 0, "rope_dim must align with per-lane width");

  const int lane = threadIdx.x % kWarpSize;
  const int warp_in_block = threadIdx.x / kWarpSize;
  const int warps_per_block = blockDim.x / kWarpSize;
  const int num_qk_heads = num_qo_heads + num_kv_heads;
  const long num_works = static_cast<long>(num_qk_heads) * num_tokens;
  const long stride_workers = static_cast<long>(gridDim.x) * warps_per_block;

  for (long idx = static_cast<long>(blockIdx.x) * warps_per_block + warp_in_block;
       idx < num_works; idx += stride_workers) {
    const long token_id = idx / num_qk_heads;
    const int head_id = static_cast<int>(idx % num_qk_heads);
    const bool is_q = head_id < num_qo_heads;
    __nv_bfloat16* base = is_q
        ? (q + token_id * q_row_stride + static_cast<long>(head_id) * head_stride)
        : (k + token_id * k_row_stride + static_cast<long>(head_id - num_qo_heads) * head_stride);
    const __nv_bfloat16* weight = is_q ? q_weight : k_weight;

    // Vectorized 8-byte load of this lane's 4 bf16 elements.
    const float2 raw = *reinterpret_cast<const float2*>(base + lane * kElems);
    const float2 e0 = __bfloat1622float2(*reinterpret_cast<const __nv_bfloat162*>(&raw.x));
    const float2 e1 = __bfloat1622float2(*reinterpret_cast<const __nv_bfloat162*>(&raw.y));
    float elems[kElems] = {e0.x, e0.y, e1.x, e1.y};

    float sum_sq = 0.0f;
#pragma unroll
    for (int i = 0; i < kElems; ++i) sum_sq = fmaf(elems[i], elems[i], sum_sq);
    sum_sq = warp_reduce_sum(sum_sq);
    const float inv_rms = rsqrtf(sum_sq / static_cast<float>(HEAD_DIM) + eps);

    const float2 wraw = *reinterpret_cast<const float2*>(weight + lane * kElems);
    const float2 w0 = __bfloat1622float2(*reinterpret_cast<const __nv_bfloat162*>(&wraw.x));
    const float2 w1 = __bfloat1622float2(*reinterpret_cast<const __nv_bfloat162*>(&wraw.y));
    elems[0] *= inv_rms * w0.x;
    elems[1] *= inv_rms * w0.y;
    elems[2] *= inv_rms * w1.x;
    elems[3] *= inv_rms * w1.y;

    if (lane < kRotaryLanes) {
      const long pos = static_cast<long>(positions[token_id]);
      const float* cos_ptr = cos_sin_cache + pos * ROPE_DIM;
      const float* sin_ptr = cos_ptr + ROPE_DIM / 2;
      if constexpr (!IS_NEOX) {
        // Interleaved (GPT-J): rotate adjacent pairs (2m, 2m+1). For head_dim=128
        // each lane owns kElems/2 pairs whose angle indices are consecutive
        // (lane*(kElems/2) + p), so cos/sin load as one coalesced float2 per lane
        // instead of strided scalar __ldg (removes the over-fetch NCU flagged).
        const float2 cosv = __ldg(reinterpret_cast<const float2*>(cos_ptr) + lane);
        const float2 sinv = __ldg(reinterpret_cast<const float2*>(sin_ptr) + lane);
        const float cpair[2] = {cosv.x, cosv.y};
        const float spair[2] = {sinv.x, sinv.y};
#pragma unroll
        for (int p = 0; p < kElems / 2; ++p) {
          const float x = elems[2 * p];
          const float y = elems[2 * p + 1];
          elems[2 * p] = fmaf(x, cpair[p], -y * spair[p]);
          elems[2 * p + 1] = fmaf(y, cpair[p], x * spair[p]);
        }
      } else {
        // NeoX (rotate-half) via shuffle across the rotary half.
        constexpr unsigned mask =
            (kRotaryLanes == kWarpSize) ? 0xffffffffu : ((1u << kRotaryLanes) - 1u);
#pragma unroll
        for (int i = 0; i < kElems; ++i) {
          float swapped = __shfl_xor_sync(mask, elems[i], kHalfRotaryLanes);
          if (lane < kHalfRotaryLanes) swapped = -swapped;
          int dim_idx = (lane * kElems + i);
          dim_idx = (dim_idx * 2) % ROPE_DIM;
          const int half_idx = dim_idx / 2;
          const float c = __ldg(cos_ptr + half_idx);
          const float s = __ldg(sin_ptr + half_idx);
          elems[i] = elems[i] * c + swapped * s;
        }
      }
    }

    float2 out_raw;
    *reinterpret_cast<__nv_bfloat162*>(&out_raw.x) = __float22bfloat162_rn(make_float2(elems[0], elems[1]));
    *reinterpret_cast<__nv_bfloat162*>(&out_raw.y) = __float22bfloat162_rn(make_float2(elems[2], elems[3]));
    *reinterpret_cast<float2*>(base + lane * kElems) = out_raw;
  }
}

template <int HEAD_DIM, int ROPE_DIM, bool IS_NEOX, typename IdType>
int blocks_for(int num_works) {
  int blocks_per_sm = 0;
  cudaOccupancyMaxActiveBlocksPerMultiprocessor(
      &blocks_per_sm, fused_qknorm_rope_kernel<HEAD_DIM, ROPE_DIM, IS_NEOX, IdType>,
      kThreadsPerBlock, 0);
  int dev = 0;
  cudaGetDevice(&dev);
  int num_sm = 0;
  cudaDeviceGetAttribute(&num_sm, cudaDevAttrMultiProcessorCount, dev);
  const int max_blocks = std::max(1, blocks_per_sm * num_sm);
  const int needed = (num_works + kWarpsPerBlock - 1) / kWarpsPerBlock;
  return std::max(1, std::min(max_blocks, needed));
}

// 2-heads-per-warp, 128-bit vectorized variant for the production config
// (head_dim=128, rope_dim=128, is_neox=False): each lane owns 8 bf16 (one 16-byte
// load/store), 16 lanes cover a head, a warp covers 2 heads of the SAME token
// (num_qk_heads is even for equal Q/K heads), so cos/sin load once per lane and
// the RMS reduction is a 16-lane (half-warp) reduction. Goal: more bytes in
// flight per warp (memory-level parallelism) on the latency-bound large shapes.
template <typename IdType>
__global__ void fused_qknorm_rope_2head_kernel(
    __nv_bfloat16* __restrict__ q,
    __nv_bfloat16* __restrict__ k,
    const __nv_bfloat16* __restrict__ q_weight,
    const __nv_bfloat16* __restrict__ k_weight,
    const float* __restrict__ cos_sin_cache,
    const IdType* __restrict__ positions,
    float eps,
    int num_tokens,
    int num_qo_heads,
    int num_kv_heads,
    long q_row_stride,
    long k_row_stride,
    long head_stride) {
  constexpr int HEAD_DIM = 128, ROPE_DIM = 128, LANES_PER_HEAD = 16, ELEMS = 8;
  const int lane = threadIdx.x % kWarpSize;
  const int head_slot = lane / LANES_PER_HEAD;  // 0 or 1
  const int ll = lane % LANES_PER_HEAD;         // 0..15
  const int warp_in_block = threadIdx.x / kWarpSize;
  const int warps_per_block = blockDim.x / kWarpSize;
  const int num_qk_heads = num_qo_heads + num_kv_heads;
  const long num_works = static_cast<long>(num_qk_heads) * num_tokens;
  const long stride_warps = static_cast<long>(gridDim.x) * warps_per_block;

  for (long gw = static_cast<long>(blockIdx.x) * warps_per_block + warp_in_block;
       gw * 2 < num_works; gw += stride_warps) {
    const long work0 = gw * 2;
    const long work_idx = work0 + head_slot;
    const bool valid = work_idx < num_works;
    const long token_id = work0 / num_qk_heads;  // both slots share this token
    const int head_id = valid ? static_cast<int>(work_idx % num_qk_heads) : 0;
    const bool is_q = head_id < num_qo_heads;
    __nv_bfloat16* base = is_q
        ? (q + token_id * q_row_stride + static_cast<long>(head_id) * head_stride)
        : (k + token_id * k_row_stride + static_cast<long>(head_id - num_qo_heads) * head_stride);
    const __nv_bfloat16* weight = is_q ? q_weight : k_weight;

    float elems[ELEMS];
    if (valid) {
      const float4 raw = *reinterpret_cast<const float4*>(base + ll * ELEMS);
      const float2 e0 = __bfloat1622float2(*reinterpret_cast<const __nv_bfloat162*>(&raw.x));
      const float2 e1 = __bfloat1622float2(*reinterpret_cast<const __nv_bfloat162*>(&raw.y));
      const float2 e2 = __bfloat1622float2(*reinterpret_cast<const __nv_bfloat162*>(&raw.z));
      const float2 e3 = __bfloat1622float2(*reinterpret_cast<const __nv_bfloat162*>(&raw.w));
      elems[0] = e0.x; elems[1] = e0.y; elems[2] = e1.x; elems[3] = e1.y;
      elems[4] = e2.x; elems[5] = e2.y; elems[6] = e3.x; elems[7] = e3.y;
    } else {
#pragma unroll
      for (int i = 0; i < ELEMS; ++i) elems[i] = 0.0f;
    }

    float sum_sq = 0.0f;
#pragma unroll
    for (int i = 0; i < ELEMS; ++i) sum_sq = fmaf(elems[i], elems[i], sum_sq);
#pragma unroll
    for (int off = LANES_PER_HEAD / 2; off > 0; off >>= 1)  // 16-lane (half-warp) reduce
      sum_sq += __shfl_xor_sync(0xffffffffu, sum_sq, off);
    const float inv_rms = rsqrtf(sum_sq / static_cast<float>(HEAD_DIM) + eps);

    const float4 wraw = *reinterpret_cast<const float4*>(weight + ll * ELEMS);
    const float2 w0 = __bfloat1622float2(*reinterpret_cast<const __nv_bfloat162*>(&wraw.x));
    const float2 w1 = __bfloat1622float2(*reinterpret_cast<const __nv_bfloat162*>(&wraw.y));
    const float2 w2 = __bfloat1622float2(*reinterpret_cast<const __nv_bfloat162*>(&wraw.z));
    const float2 w3 = __bfloat1622float2(*reinterpret_cast<const __nv_bfloat162*>(&wraw.w));
    const float wv[ELEMS] = {w0.x, w0.y, w1.x, w1.y, w2.x, w2.y, w3.x, w3.y};
#pragma unroll
    for (int i = 0; i < ELEMS; ++i) elems[i] *= inv_rms * wv[i];

    const long pos = static_cast<long>(positions[token_id]);
    const float* cos_ptr = cos_sin_cache + pos * ROPE_DIM;
    const float* sin_ptr = cos_ptr + ROPE_DIM / 2;
    const float4 cosv = __ldg(reinterpret_cast<const float4*>(cos_ptr) + ll);
    const float4 sinv = __ldg(reinterpret_cast<const float4*>(sin_ptr) + ll);
    const float cc[4] = {cosv.x, cosv.y, cosv.z, cosv.w};
    const float ss[4] = {sinv.x, sinv.y, sinv.z, sinv.w};
#pragma unroll
    for (int p = 0; p < 4; ++p) {
      const float x = elems[2 * p];
      const float y = elems[2 * p + 1];
      elems[2 * p] = fmaf(x, cc[p], -y * ss[p]);
      elems[2 * p + 1] = fmaf(y, cc[p], x * ss[p]);
    }

    if (valid) {
      float4 out;
      *reinterpret_cast<__nv_bfloat162*>(&out.x) = __float22bfloat162_rn(make_float2(elems[0], elems[1]));
      *reinterpret_cast<__nv_bfloat162*>(&out.y) = __float22bfloat162_rn(make_float2(elems[2], elems[3]));
      *reinterpret_cast<__nv_bfloat162*>(&out.z) = __float22bfloat162_rn(make_float2(elems[4], elems[5]));
      *reinterpret_cast<__nv_bfloat162*>(&out.w) = __float22bfloat162_rn(make_float2(elems[6], elems[7]));
      *reinterpret_cast<float4*>(base + ll * ELEMS) = out;
    }
  }
}

template <typename IdType>
int blocks_for_2head(int num_works) {
  int blocks_per_sm = 0;
  cudaOccupancyMaxActiveBlocksPerMultiprocessor(
      &blocks_per_sm, fused_qknorm_rope_2head_kernel<IdType>, kThreadsPerBlock, 0);
  int dev = 0;
  cudaGetDevice(&dev);
  int num_sm = 0;
  cudaDeviceGetAttribute(&num_sm, cudaDevAttrMultiProcessorCount, dev);
  const int max_blocks = std::max(1, blocks_per_sm * num_sm);
  const int warps_needed = (num_works / 2 + kWarpsPerBlock - 1) / kWarpsPerBlock;
  return std::max(1, std::min(max_blocks, warps_needed));
}

}  // namespace

// In-place fused QK-Norm + RoPE. Mutates q and k. Production fast path only;
// the Python dispatcher guarantees the supported signature before calling.
void fused_qknorm_rope(
    torch::Tensor q,
    torch::Tensor k,
    torch::Tensor q_weight,
    torch::Tensor k_weight,
    torch::Tensor cos_sin_cache,
    torch::Tensor positions,
    double eps,
    bool is_neox) {
  TORCH_CHECK(q.is_cuda() && k.is_cuda(), "q,k must be CUDA tensors");
  TORCH_CHECK(q.scalar_type() == at::kBFloat16 && k.scalar_type() == at::kBFloat16,
              "this fast path is bf16-only");
  TORCH_CHECK(q.dim() == 3 && k.dim() == 3, "q,k must be [tokens, heads, head_dim]");
  TORCH_CHECK(q.stride(2) == 1 && k.stride(2) == 1, "head_dim must be contiguous");
  TORCH_CHECK(q_weight.is_cuda() && k_weight.is_cuda() && positions.is_cuda(),
              "weights and positions must be CUDA tensors");
  TORCH_CHECK(positions.dim() == 1 && positions.is_contiguous(),
              "positions must be 1-D contiguous");
  TORCH_CHECK(cos_sin_cache.scalar_type() == at::kFloat && cos_sin_cache.is_contiguous() &&
                  cos_sin_cache.dim() == 2,
              "cos_sin_cache must be a contiguous 2-D float32 tensor");

  const int num_tokens = static_cast<int>(q.size(0));
  const int num_qo_heads = static_cast<int>(q.size(1));
  const int num_kv_heads = static_cast<int>(k.size(1));
  const int head_dim = static_cast<int>(q.size(2));
  const int rope_dim = static_cast<int>(cos_sin_cache.size(1));
  TORCH_CHECK(head_dim == 128 && rope_dim == 128 && !is_neox,
              "fast path supports head_dim=128, rope_dim=128, is_neox=False");

  const long q_row_stride = q.stride(0);
  const long k_row_stride = k.stride(0);
  const long head_stride = q.stride(1);
  const int num_works = (num_qo_heads + num_kv_heads) * num_tokens;
  if (num_works == 0) return;

  auto* q_ptr = reinterpret_cast<__nv_bfloat16*>(q.data_ptr());
  auto* k_ptr = reinterpret_cast<__nv_bfloat16*>(k.data_ptr());
  const auto* qw = reinterpret_cast<const __nv_bfloat16*>(q_weight.data_ptr());
  const auto* kw = reinterpret_cast<const __nv_bfloat16*>(k_weight.data_ptr());
  const auto* cache = cos_sin_cache.data_ptr<float>();
  const auto stream = at::cuda::getCurrentCUDAStream();
  const float eps_f = static_cast<float>(eps);

  // num_qk_heads is even for equal Q/K heads (the dispatch gate guarantees it),
  // which the 2-heads-per-warp kernel relies on (both head slots share a token).
  TORCH_CHECK((num_qo_heads + num_kv_heads) % 2 == 0,
              "2-head fast path requires an even Q+K head count");
  if (positions.scalar_type() == at::kLong) {
    const auto* pos = positions.data_ptr<int64_t>();
    const int blocks = blocks_for_2head<int64_t>(num_works);
    fused_qknorm_rope_2head_kernel<int64_t><<<blocks, kThreadsPerBlock, 0, stream>>>(
        q_ptr, k_ptr, qw, kw, cache, pos, eps_f, num_tokens, num_qo_heads, num_kv_heads,
        q_row_stride, k_row_stride, head_stride);
  } else if (positions.scalar_type() == at::kInt) {
    const auto* pos = positions.data_ptr<int32_t>();
    const int blocks = blocks_for_2head<int32_t>(num_works);
    fused_qknorm_rope_2head_kernel<int32_t><<<blocks, kThreadsPerBlock, 0, stream>>>(
        q_ptr, k_ptr, qw, kw, cache, pos, eps_f, num_tokens, num_qo_heads, num_kv_heads,
        q_row_stride, k_row_stride, head_stride);
  } else {
    TORCH_CHECK(false, "positions must be int32 or int64");
  }
}

// 1-head-per-warp variant (the generic templated kernel), exposed only for
// dispatcher A/B benchmarking on H200. Same supported signature as the 2-head
// production path. The Python dispatcher always routes to the 2-head path; this
// entrypoint lets benchmark.py compare the two warp-to-work mappings on H200.
void fused_qknorm_rope_1head(
    torch::Tensor q,
    torch::Tensor k,
    torch::Tensor q_weight,
    torch::Tensor k_weight,
    torch::Tensor cos_sin_cache,
    torch::Tensor positions,
    double eps,
    bool is_neox) {
  TORCH_CHECK(q.is_cuda() && k.is_cuda(), "q,k must be CUDA tensors");
  TORCH_CHECK(q.scalar_type() == at::kBFloat16 && k.scalar_type() == at::kBFloat16,
              "this fast path is bf16-only");
  TORCH_CHECK(q.dim() == 3 && k.dim() == 3, "q,k must be [tokens, heads, head_dim]");
  TORCH_CHECK(q.stride(2) == 1 && k.stride(2) == 1, "head_dim must be contiguous");
  const int num_tokens = static_cast<int>(q.size(0));
  const int num_qo_heads = static_cast<int>(q.size(1));
  const int num_kv_heads = static_cast<int>(k.size(1));
  const int head_dim = static_cast<int>(q.size(2));
  const int rope_dim = static_cast<int>(cos_sin_cache.size(1));
  TORCH_CHECK(head_dim == 128 && rope_dim == 128 && !is_neox,
              "1-head fast path supports head_dim=128, rope_dim=128, is_neox=False");
  const long q_row_stride = q.stride(0);
  const long k_row_stride = k.stride(0);
  const long head_stride = q.stride(1);
  const int num_works = (num_qo_heads + num_kv_heads) * num_tokens;
  if (num_works == 0) return;
  auto* q_ptr = reinterpret_cast<__nv_bfloat16*>(q.data_ptr());
  auto* k_ptr = reinterpret_cast<__nv_bfloat16*>(k.data_ptr());
  const auto* qw = reinterpret_cast<const __nv_bfloat16*>(q_weight.data_ptr());
  const auto* kw = reinterpret_cast<const __nv_bfloat16*>(k_weight.data_ptr());
  const auto* cache = cos_sin_cache.data_ptr<float>();
  const auto stream = at::cuda::getCurrentCUDAStream();
  const float eps_f = static_cast<float>(eps);
  if (positions.scalar_type() == at::kLong) {
    const auto* pos = positions.data_ptr<int64_t>();
    const int blocks = blocks_for<128, 128, false, int64_t>(num_works);
    fused_qknorm_rope_kernel<128, 128, false, int64_t><<<blocks, kThreadsPerBlock, 0, stream>>>(
        q_ptr, k_ptr, qw, kw, cache, pos, eps_f, num_tokens, num_qo_heads, num_kv_heads,
        q_row_stride, k_row_stride, head_stride);
  } else if (positions.scalar_type() == at::kInt) {
    const auto* pos = positions.data_ptr<int32_t>();
    const int blocks = blocks_for<128, 128, false, int32_t>(num_works);
    fused_qknorm_rope_kernel<128, 128, false, int32_t><<<blocks, kThreadsPerBlock, 0, stream>>>(
        q_ptr, k_ptr, qw, kw, cache, pos, eps_f, num_tokens, num_qo_heads, num_kv_heads,
        q_row_stride, k_row_stride, head_stride);
  } else {
    TORCH_CHECK(false, "positions must be int32 or int64");
  }
}

PYBIND11_MODULE(TORCH_EXTENSION_NAME, m) {
  m.def("fused_qknorm_rope", &fused_qknorm_rope,
        "Fused in-place QK-Norm + RoPE (H200 production fast path, 2-heads-per-warp)");
  m.def("fused_qknorm_rope_1head", &fused_qknorm_rope_1head,
        "Fused in-place QK-Norm + RoPE (1-head-per-warp variant, for A/B benchmarking)");
}
