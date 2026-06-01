// Native-CUDA candidates for the two SGLang diffusion inference norm kernels,
// built + exported through the SGLang jit_kernel / tvm-ffi stack (mirrors
// csrc/diffusion/qknorm_rope.cuh). First correctness-faithful port:
//   - LayerNormInferKernel<DType>: fp32 LayerNorm, one CTA per row, loads the
//     row once and reduces twice (mean, then sum((x-mean)^2)/N) to match the
//     Triton baseline's numerics.
//   - RmsNormOnepassKernel<kD, DType>: bf16 RMSNorm, one warp per row, fp32
//     square accumulation + warp-shuffle reduction (kD=128).
// No --use_fast_math, no PDL in this first port (PDL is a later A/B knob).

#include <sgl_kernel/tensor.h>

#include <sgl_kernel/math.cuh>
#include <sgl_kernel/runtime.cuh>
#include <sgl_kernel/type.cuh>
#include <sgl_kernel/utils.cuh>
#include <sgl_kernel/vec.cuh>
#include <sgl_kernel/warp.cuh>

#include <dlpack/dlpack.h>

#include <cstdint>
#include <type_traits>

namespace {

// =====================================================================
// Family A: fp32 LayerNorm (inference), one CTA per row.
// =====================================================================
struct LayerNormInferParams {
  const void* __restrict__ x_ptr;
  void* __restrict__ y_ptr;
  const void* __restrict__ w_ptr;
  const void* __restrict__ b_ptr;
  int64_t row_stride;  // elements between rows (= N for contiguous)
  uint32_t M;
  uint32_t N;
  float eps;
};

constexpr uint32_t kLNThreads = 256;
constexpr uint32_t kLNWarps = kLNThreads / 32;
// float4 vectors handled per thread. Covers N <= kLNThreads*4*kLNMaxVec = 5120
// (every configured LN shape; the host allowlist rejects anything larger).
constexpr uint32_t kLNMaxVec = 5;

// Block sum-reduction: warp-shuffle within each warp, one shared-mem round, then
// warp 0 reduces the per-warp partials via shuffle (no serial thread-0 loop).
// Reuses `s_warp` (size kNWarps) as both scratch and broadcast slot.
template <uint32_t kNWarps>
SGL_DEVICE float ln_block_reduce_sum(float v, float* s_warp) {
  using namespace device;
  const uint32_t lane = threadIdx.x % 32, wid = threadIdx.x / 32;
  v = warp::reduce_sum(v);
  if (lane == 0) s_warp[wid] = v;
  __syncthreads();
  if (wid == 0) {
    float t = (lane < kNWarps) ? s_warp[lane] : 0.0f;
    t = warp::reduce_sum(t);  // lanes >= kNWarps contribute 0
    if (lane == 0) s_warp[0] = t;
  }
  __syncthreads();
  const float total = s_warp[0];
  __syncthreads();  // all threads must read before s_warp is reused
  return total;
}

template <typename DType>
__global__ void layernorm_infer_kernel(const LayerNormInferParams __grid_constant__ params) {
  using namespace device;
  static_assert(std::is_same_v<DType, fp32_t>, "LN CUDA path is fp32-only");

  const uint32_t row = blockIdx.x;
  if (row >= params.M) return;
  const uint32_t tid = threadIdx.x;
  const uint32_t N = params.N;
  const uint32_t nvec = N >> 2;  // float4 count (N is a multiple of 4)
  const float fN = static_cast<float>(N);

  const float4* x4 = reinterpret_cast<const float4*>(
      static_cast<const float*>(params.x_ptr) + static_cast<int64_t>(row) * params.row_stride);
  float4* y4 = reinterpret_cast<float4*>(
      static_cast<float*>(params.y_ptr) + static_cast<int64_t>(row) * params.row_stride);
  const float4* w4 = reinterpret_cast<const float4*>(params.w_ptr);
  const float4* b4 = reinterpret_cast<const float4*>(params.b_ptr);

  // Pass 1: read the row once (vectorized) into registers; partial sum.
  float4 vals[kLNMaxVec];
  float partial_sum = 0.0f;
#pragma unroll
  for (uint32_t i = 0; i < kLNMaxVec; ++i) {
    const uint32_t vi = tid + i * kLNThreads;
    if (vi < nvec) {
      const float4 v = x4[vi];
      vals[i] = v;
      partial_sum += v.x + v.y + v.z + v.w;
    }
  }

  __shared__ float s_warp[kLNWarps];
  const float mean = ln_block_reduce_sum<kLNWarps>(partial_sum, s_warp) / fN;

  // Pass 2: variance = sum((x - mean)^2) / N (matches the Triton baseline).
  float partial_var = 0.0f;
#pragma unroll
  for (uint32_t i = 0; i < kLNMaxVec; ++i) {
    const uint32_t vi = tid + i * kLNThreads;
    if (vi < nvec) {
      const float4 v = vals[i];
      const float dx = v.x - mean, dy = v.y - mean, dz = v.z - mean, dw = v.w - mean;
      partial_var += dx * dx + dy * dy + dz * dz + dw * dw;
    }
  }
  const float rstd = math::rsqrt(ln_block_reduce_sum<kLNWarps>(partial_var, s_warp) / fN + params.eps);

  // Normalize + affine + store (vectorized).
#pragma unroll
  for (uint32_t i = 0; i < kLNMaxVec; ++i) {
    const uint32_t vi = tid + i * kLNThreads;
    if (vi < nvec) {
      const float4 v = vals[i];
      const float4 wv = w4[vi];
      const float4 bv = b4[vi];
      float4 o;
      o.x = (v.x - mean) * rstd * wv.x + bv.x;
      o.y = (v.y - mean) * rstd * wv.y + bv.y;
      o.z = (v.z - mean) * rstd * wv.z + bv.z;
      o.w = (v.w - mean) * rstd * wv.w + bv.w;
      y4[vi] = o;
    }
  }
}

template <typename DType>
struct LayerNormInferKernel {
  static void
  run(const tvm::ffi::TensorView x,
      const tvm::ffi::TensorView weight,
      const tvm::ffi::TensorView bias,
      const tvm::ffi::TensorView out,
      float eps) {
    using namespace host;
    static_assert(std::is_same_v<DType, fp32_t>, "LN CUDA path is fp32-only");

    auto M = SymbolicSize{"M"};
    auto N = SymbolicSize{"N"};
    auto device = SymbolicDevice{};
    device.set_options<kDLCUDA>();

    TensorMatcher({M, N}).with_strides({N, 1}).with_dtype<DType>().with_device(device).verify(x);
    TensorMatcher({N}).with_dtype<DType>().with_device(device).verify(weight).verify(bias);
    TensorMatcher({M, N}).with_strides({N, 1}).with_dtype<DType>().with_device(device).verify(out);

    const auto m = static_cast<uint32_t>(M.unwrap());
    const auto n = static_cast<uint32_t>(N.unwrap());
    const auto params = LayerNormInferParams{
        .x_ptr = x.data_ptr(),
        .y_ptr = out.data_ptr(),
        .w_ptr = weight.data_ptr(),
        .b_ptr = bias.data_ptr(),
        .row_stride = static_cast<int64_t>(n),
        .M = m,
        .N = n,
        .eps = eps,
    };
    LaunchKernel(m, kLNThreads, device.unwrap()).enable_pdl(false)(layernorm_infer_kernel<DType>, params);
  }
};

// =====================================================================
// Family B: bf16 RMSNorm (one pass), one warp per row, kD == 128.
// =====================================================================
struct RmsNormParams {
  const void* __restrict__ x_ptr;
  void* __restrict__ y_ptr;
  const void* __restrict__ w_ptr;
  int64_t row_stride;  // elements between rows (= kD for contiguous)
  uint32_t S;
  float eps;
};

constexpr uint32_t kRmsThreads = 256;

template <int kD, typename DType>
__global__ void rmsnorm_onepass_kernel(const RmsNormParams __grid_constant__ params) {
  using namespace device;
  static_assert(kD % 32 == 0, "kD must be a multiple of the warp size");
  constexpr uint32_t kElemsPerThread = kD / 32;
  using Vec = AlignedVector<DType, kElemsPerThread>;

  const uint32_t lane = threadIdx.x % 32;
  const uint32_t warp = threadIdx.x / 32;
  const uint32_t warps_per_block = blockDim.x / 32;
  const uint32_t row = blockIdx.x * warps_per_block + warp;
  if (row >= params.S) return;

  const DType* x = static_cast<const DType*>(params.x_ptr) + static_cast<int64_t>(row) * params.row_stride;
  DType* y = static_cast<DType*>(params.y_ptr) + static_cast<int64_t>(row) * params.row_stride;
  const DType* w = static_cast<const DType*>(params.w_ptr);

  Vec xv, wv;
  xv.load(x, lane);  // lane owns elements [lane*kElemsPerThread, +kElemsPerThread)
  wv.load(w, lane);

  float elems[kElemsPerThread];
  float ss = 0.0f;
#pragma unroll
  for (uint32_t i = 0; i < kElemsPerThread; ++i) {
    const float v = cast<fp32_t>(xv[i]);
    elems[i] = v;
    ss += v * v;
  }
  ss = warp::reduce_sum(ss);
  const float rstd = math::rsqrt(ss / static_cast<float>(kD) + params.eps);

  Vec yv;
#pragma unroll
  for (uint32_t i = 0; i < kElemsPerThread; ++i) {
    const float ww = cast<fp32_t>(wv[i]);
    yv[i] = cast<DType>(elems[i] * rstd * ww);
  }
  yv.store(y, lane);
}

template <int kD, typename DType>
struct RmsNormOnepassKernel {
  static void
  run(const tvm::ffi::TensorView x,
      const tvm::ffi::TensorView w,
      const tvm::ffi::TensorView out,
      float eps) {
    using namespace host;

    auto S = SymbolicSize{"S"};
    auto D = SymbolicSize{"D"};
    auto device = SymbolicDevice{};
    D.set_value(kD);
    device.set_options<kDLCUDA>();

    TensorMatcher({S, D}).with_strides({D, 1}).with_dtype<DType>().with_device(device).verify(x);
    TensorMatcher({D}).with_dtype<DType>().with_device(device).verify(w);
    TensorMatcher({S, D}).with_strides({D, 1}).with_dtype<DType>().with_device(device).verify(out);

    const auto s = static_cast<uint32_t>(S.unwrap());
    constexpr uint32_t kWarpsPB = kRmsThreads / 32;
    const auto params = RmsNormParams{
        .x_ptr = x.data_ptr(),
        .y_ptr = out.data_ptr(),
        .w_ptr = w.data_ptr(),
        .row_stride = static_cast<int64_t>(kD),
        .S = s,
        .eps = eps,
    };
    const auto blocks = div_ceil(s, kWarpsPB);
    LaunchKernel(blocks, kRmsThreads, device.unwrap()).enable_pdl(false)(rmsnorm_onepass_kernel<kD, DType>, params);
  }
};

}  // namespace
