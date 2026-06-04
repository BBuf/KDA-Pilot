// Fused residual-modulation kernels for Z-Image-style diffusion blocks:
//   y  = rms(x) * tanh(scale) + shift
//   y2 = rms(y) * (1 + scale2)            (dual variant)
//
// bf16 / rms-norm PRODUCTION-ONLY native path (weight=[D] present, bias absent,
// scale/scale2 row-invariant [D] views of [1,1,D], shift full [num_rows, D],
// unit stride on D, 16-byte-aligned pointers, D % 256 == 0 and D <= 8192).
// The Python wrapper keeps every other accepted signature on the CuTe-DSL path.
//
// One row per CTA, D/8 threads, one 128-bit bf16x8 vector per thread, fp32
// accumulation with a warp + cross-warp shared-memory reduction; the weighted
// norm output is quantized to bf16 before the modulation epilogue and the
// second norm consumes the quantized y (matches the CuTe-DSL kernel dataflow).
// Promoted from the KDA task h200_diffusion_cutedsl_norm_tanh_mul_add__multi_shape
// (H200: 1.33-1.36x interleaved geomean over the captured Z-Image shapes).

#include <sgl_kernel/tensor.h>

#include <sgl_kernel/runtime.cuh>
#include <sgl_kernel/type.cuh>
#include <sgl_kernel/utils.cuh>

#include <dlpack/dlpack.h>

#include <cuda_bf16.h>

#include <cstdint>

namespace {

struct NormTanhMulAddParams {
  const void* __restrict__ x_ptr;       // [num_rows, dim] bf16
  const void* __restrict__ weight_ptr;  // [dim] bf16
  const void* __restrict__ scale_ptr;   // [dim] bf16 (row-invariant)
  const void* __restrict__ shift_ptr;   // [num_rows, dim] bf16
  void* __restrict__ y_ptr;             // [num_rows, dim] bf16
  const void* __restrict__ weight2_ptr; // [dim] bf16 (dual only)
  const void* __restrict__ scale2_ptr;  // [dim] bf16 (dual only)
  void* __restrict__ y2_ptr;            // [num_rows, dim] bf16 (dual only)
  uint32_t num_rows;
  uint32_t dim;
  float eps;
};

constexpr uint32_t kElemsPerThread = 8;  // one 128-bit bf16x8 vector
constexpr uint32_t kVecPairs = kElemsPerThread / 2;
constexpr uint32_t kMaxWarps = 32;  // dim <= 8192 -> blockDim <= 1024

struct Bf16x8 {
  __nv_bfloat162 v[kVecPairs];
};
static_assert(sizeof(Bf16x8) == 16, "Bf16x8 must be one 128-bit vector");

__device__ __forceinline__ Bf16x8 load_bf16x8(const void* base, uint32_t vec_idx) {
  Bf16x8 out;
  *reinterpret_cast<uint4*>(&out) = reinterpret_cast<const uint4*>(base)[vec_idx];
  return out;
}

__device__ __forceinline__ void store_bf16x8(void* base, uint32_t vec_idx, const Bf16x8& val) {
  reinterpret_cast<uint4*>(base)[vec_idx] = *reinterpret_cast<const uint4*>(&val);
}

__device__ __forceinline__ float warp_reduce_sum_f32(float v) {
#pragma unroll
  for (int m = 16; m > 0; m >>= 1) {
    v += __shfl_xor_sync(0xffffffffu, v, m, 32);
  }
  return v;
}

// Two-stage block reduction (warp shuffle + cross-warp shared memory). The
// leading barrier makes back-to-back reductions safe to reuse the same
// shared-memory scratch.
__device__ __forceinline__ float
block_reduce_sum_f32(float v, float* smem_partials, uint32_t num_warps) {
  const uint32_t lane = threadIdx.x & 31u;
  const uint32_t warp = threadIdx.x >> 5u;
  v = warp_reduce_sum_f32(v);
  __syncthreads();
  if (lane == 0) {
    smem_partials[warp] = v;
  }
  __syncthreads();
  if (warp == 0) {
    float t = lane < num_warps ? smem_partials[lane] : 0.0f;
    t = warp_reduce_sum_f32(t);
    if (lane == 0) {
      smem_partials[kMaxWarps] = t;
    }
  }
  __syncthreads();
  return smem_partials[kMaxWarps];
}

template <bool kHasNorm2>
__global__ void norm_tanh_mul_add_kernel(const NormTanhMulAddParams __grid_constant__ params) {
  __shared__ float smem_partials[kMaxWarps + 1];

  const uint32_t row = blockIdx.x;
  const uint32_t tid = threadIdx.x;
  const uint32_t num_warps = blockDim.x >> 5u;
  const uint32_t dim = params.dim;
  const size_t row_bytes = static_cast<size_t>(dim) * sizeof(__nv_bfloat16);

  const char* x_row = static_cast<const char*>(params.x_ptr) + static_cast<size_t>(row) * row_bytes;
  const Bf16x8 xv = load_bf16x8(x_row, tid);

  float xf[kElemsPerThread];
  float sumsq = 0.0f;
#pragma unroll
  for (uint32_t j = 0; j < kVecPairs; ++j) {
    const float2 p = __bfloat1622float2(xv.v[j]);
    xf[2 * j] = p.x;
    xf[2 * j + 1] = p.y;
    sumsq += p.x * p.x + p.y * p.y;
  }
  const float total = block_reduce_sum_f32(sumsq, smem_partials, num_warps);
  const float factor = rsqrtf(total / static_cast<float>(dim) + params.eps);

  const Bf16x8 wv = load_bf16x8(params.weight_ptr, tid);
  const Bf16x8 sv = load_bf16x8(params.scale_ptr, tid);
  const char* shift_row =
      static_cast<const char*>(params.shift_ptr) + static_cast<size_t>(row) * row_bytes;
  const Bf16x8 shv = load_bf16x8(shift_row, tid);

  Bf16x8 yv;
  float yqf[kElemsPerThread];
  float sumsq2 = 0.0f;
#pragma unroll
  for (uint32_t j = 0; j < kVecPairs; ++j) {
    const float2 w = __bfloat1622float2(wv.v[j]);
    const float2 s = __bfloat1622float2(sv.v[j]);
    const float2 sh = __bfloat1622float2(shv.v[j]);
    // Quantize the weighted norm output to bf16 (baseline register dataflow).
    const __nv_bfloat162 nq = __float22bfloat162_rn(
        make_float2(xf[2 * j] * factor * w.x, xf[2 * j + 1] * factor * w.y));
    const float2 nqf = __bfloat1622float2(nq);
    const float2 val =
        make_float2(nqf.x * tanhf(s.x) + sh.x, nqf.y * tanhf(s.y) + sh.y);
    yv.v[j] = __float22bfloat162_rn(val);
    if constexpr (kHasNorm2) {
      const float2 yq = __bfloat1622float2(yv.v[j]);
      yqf[2 * j] = yq.x;
      yqf[2 * j + 1] = yq.y;
      sumsq2 += yq.x * yq.x + yq.y * yq.y;
    }
  }
  char* y_row = static_cast<char*>(params.y_ptr) + static_cast<size_t>(row) * row_bytes;
  store_bf16x8(y_row, tid, yv);

  if constexpr (kHasNorm2) {
    const float total2 = block_reduce_sum_f32(sumsq2, smem_partials, num_warps);
    const float factor2 = rsqrtf(total2 / static_cast<float>(dim) + params.eps);
    const Bf16x8 w2v = load_bf16x8(params.weight2_ptr, tid);
    const Bf16x8 s2v = load_bf16x8(params.scale2_ptr, tid);
    Bf16x8 y2v;
#pragma unroll
    for (uint32_t j = 0; j < kVecPairs; ++j) {
      const float2 w2 = __bfloat1622float2(w2v.v[j]);
      const float2 s2 = __bfloat1622float2(s2v.v[j]);
      const __nv_bfloat162 n2q = __float22bfloat162_rn(
          make_float2(yqf[2 * j] * factor2 * w2.x, yqf[2 * j + 1] * factor2 * w2.y));
      const float2 n2qf = __bfloat1622float2(n2q);
      const float2 val2 =
          make_float2(n2qf.x * (1.0f + s2.x), n2qf.y * (1.0f + s2.y));
      y2v.v[j] = __float22bfloat162_rn(val2);
    }
    char* y2_row = static_cast<char*>(params.y2_ptr) + static_cast<size_t>(row) * row_bytes;
    store_bf16x8(y2_row, tid, y2v);
  }
}

inline void check_dim_supported(int64_t dim) {
  host::RuntimeCheck(dim % 256 == 0 && dim <= 8192,
                     "dim must be a multiple of 256 and <= 8192, got ", dim);
}

template <typename DType>
struct NormTanhMulAddSingleKernel {
  static void
  run(const tvm::ffi::TensorView x,
      const tvm::ffi::TensorView weight,
      const tvm::ffi::TensorView scale,
      const tvm::ffi::TensorView shift,
      const tvm::ffi::TensorView y,
      double eps) {
    using namespace host;

    auto N = SymbolicSize{"num_rows"};
    auto D = SymbolicSize{"dim"};
    auto device = SymbolicDevice{};
    device.set_options<kDLCUDA>();

    TensorMatcher({N, D}).with_strides({D, 1}).with_dtype<DType>().with_device(device)
        .verify(x).verify(shift).verify(y);
    TensorMatcher({D}).with_dtype<DType>().with_device(device).verify(weight).verify(scale);

    const auto dim64 = D.unwrap();
    check_dim_supported(dim64);
    const auto num_rows = static_cast<uint32_t>(N.unwrap());
    const auto dim = static_cast<uint32_t>(dim64);

    const auto params = NormTanhMulAddParams{
        .x_ptr = x.data_ptr(),
        .weight_ptr = weight.data_ptr(),
        .scale_ptr = scale.data_ptr(),
        .shift_ptr = shift.data_ptr(),
        .y_ptr = y.data_ptr(),
        .weight2_ptr = nullptr,
        .scale2_ptr = nullptr,
        .y2_ptr = nullptr,
        .num_rows = num_rows,
        .dim = dim,
        .eps = static_cast<float>(eps),
    };
    LaunchKernel(num_rows, dim / kElemsPerThread, device.unwrap())(
        norm_tanh_mul_add_kernel<false>, params);
  }
};

template <typename DType>
struct NormTanhMulAddDualKernel {
  static void
  run(const tvm::ffi::TensorView x,
      const tvm::ffi::TensorView weight,
      const tvm::ffi::TensorView scale,
      const tvm::ffi::TensorView shift,
      const tvm::ffi::TensorView weight2,
      const tvm::ffi::TensorView scale2,
      const tvm::ffi::TensorView y,
      const tvm::ffi::TensorView y2,
      double eps) {
    using namespace host;

    auto N = SymbolicSize{"num_rows"};
    auto D = SymbolicSize{"dim"};
    auto device = SymbolicDevice{};
    device.set_options<kDLCUDA>();

    TensorMatcher({N, D}).with_strides({D, 1}).with_dtype<DType>().with_device(device)
        .verify(x).verify(shift).verify(y).verify(y2);
    TensorMatcher({D}).with_dtype<DType>().with_device(device)
        .verify(weight).verify(scale).verify(weight2).verify(scale2);

    const auto dim64 = D.unwrap();
    check_dim_supported(dim64);
    const auto num_rows = static_cast<uint32_t>(N.unwrap());
    const auto dim = static_cast<uint32_t>(dim64);

    const auto params = NormTanhMulAddParams{
        .x_ptr = x.data_ptr(),
        .weight_ptr = weight.data_ptr(),
        .scale_ptr = scale.data_ptr(),
        .shift_ptr = shift.data_ptr(),
        .y_ptr = y.data_ptr(),
        .weight2_ptr = weight2.data_ptr(),
        .scale2_ptr = scale2.data_ptr(),
        .y2_ptr = y2.data_ptr(),
        .num_rows = num_rows,
        .dim = dim,
        .eps = static_cast<float>(eps),
    };
    LaunchKernel(num_rows, dim / kElemsPerThread, device.unwrap())(
        norm_tanh_mul_add_kernel<true>, params);
  }
};

}  // namespace
