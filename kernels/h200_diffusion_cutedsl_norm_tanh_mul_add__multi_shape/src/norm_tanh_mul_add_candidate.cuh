// Native CUDA candidate for the SGLang diffusion residual-modulation kernels
//   y  = rms(x)  * tanh(scale) + shift
//   y2 = rms(y)  * (1 + scale2)            (dual variant)
//
// Production fast path only (dispatched from Python): bf16, rms norm,
// weight=[D] present, bias absent, scale/scale2 row-invariant [D] views of
// [1,1,D], shift full [num_rows, D], unit stride on D, D % 256 == 0 and
// D <= 8192 (so blockDim = D/8 <= 1024 with one 128-bit bf16x8 vector per
// thread and an integral warp count).
//
// Structure is a faithful port of the CuTe-DSL baseline for clean device-delta
// attribution: one row per CTA, D/8 threads, fp32 accumulation with warp +
// cross-warp shared-memory reduction, and the same register dataflow — the
// weighted norm output is quantized to bf16 before the modulation epilogue,
// and the second norm consumes the quantized y.

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

// Two-stage block reduction (warp shuffle + cross-warp shared memory).
// Anchor flavor (kTwoSync=false): a barrier between the warp reduction and
// the partial write makes back-to-back reductions safe on ONE scratch slot
// (3 barriers per reduction). Two-sync flavor (kTwoSync=true): the dual's
// two reductions ping-pong between scratch slots selected by `slot`, so the
// leading barrier is unnecessary (2 barriers per reduction) — every thread
// passes the previous reduction's final barrier before any thread can write
// the OTHER slot's partials.
template <bool kTwoSync>
__device__ __forceinline__ float block_reduce_sum_f32(
    float v, float (&smem_partials)[2][kMaxWarps + 1], uint32_t num_warps, uint32_t slot) {
  const uint32_t lane = threadIdx.x & 31u;
  const uint32_t warp = threadIdx.x >> 5u;
  float* s = smem_partials[kTwoSync ? (slot & 1u) : 0u];
  v = warp_reduce_sum_f32(v);
  if constexpr (!kTwoSync) {
    __syncthreads();
  }
  if (lane == 0) {
    s[warp] = v;
  }
  __syncthreads();
  if (warp == 0) {
    float t = lane < num_warps ? s[lane] : 0.0f;
    t = warp_reduce_sum_f32(t);
    if (lane == 0) {
      s[kMaxWarps] = t;
    }
  }
  __syncthreads();
  return s[kMaxWarps];
}

// Precompute tanh(scale) once per call into an fp32 [dim] buffer (the main
// kernel otherwise recomputes ~num_rows * dim tanhf — 38.6% XU pipe pressure
// in the anchor profile).
__global__ void tanh_scale_f32_kernel(
    const __nv_bfloat16* __restrict__ scale, float* __restrict__ out, uint32_t dim) {
  const uint32_t i = blockIdx.x * blockDim.x + threadIdx.x;
  if (i < dim) {
    out[i] = tanhf(__bfloat162float(scale[i]));
  }
}

template <bool kHasNorm2, bool kTanhPre, bool kTwoSync>
__device__ __forceinline__ void
norm_tanh_mul_add_body(const NormTanhMulAddParams& params) {
  __shared__ float smem_partials[2][kMaxWarps + 1];

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
  const float total = block_reduce_sum_f32<kTwoSync>(sumsq, smem_partials, num_warps, 0);
  const float factor = rsqrtf(total / static_cast<float>(dim) + params.eps);

  // Operand loads stay AFTER the reduction (they overlap its barriers; see
  // BL-20260604-load-after-reduce). kTanhPre swaps the bf16 scale + per-row
  // tanhf for fp32 loads of the precomputed tanh(scale) buffer.
  const Bf16x8 wv = load_bf16x8(params.weight_ptr, tid);
  Bf16x8 sv;
  float4 ts0, ts1;
  if constexpr (kTanhPre) {
    const float4* ts = reinterpret_cast<const float4*>(params.scale_ptr);
    ts0 = ts[tid * 2];
    ts1 = ts[tid * 2 + 1];
  } else {
    sv = load_bf16x8(params.scale_ptr, tid);
  }
  const char* shift_row =
      static_cast<const char*>(params.shift_ptr) + static_cast<size_t>(row) * row_bytes;
  const Bf16x8 shv = load_bf16x8(shift_row, tid);

  Bf16x8 yv;
  float yqf[kElemsPerThread];
  float sumsq2 = 0.0f;
#pragma unroll
  for (uint32_t j = 0; j < kVecPairs; ++j) {
    const float2 w = __bfloat1622float2(wv.v[j]);
    float2 t;
    if constexpr (kTanhPre) {
      const float* tsf = j < 2 ? &ts0.x : &ts1.x;
      const uint32_t off = (2 * j) & 3u;
      t = make_float2(tsf[off], tsf[off + 1]);
    } else {
      const float2 s = __bfloat1622float2(sv.v[j]);
      t = make_float2(tanhf(s.x), tanhf(s.y));
    }
    const float2 sh = __bfloat1622float2(shv.v[j]);
    // Quantize the weighted norm output to bf16 (baseline register dataflow).
    const __nv_bfloat162 nq = __float22bfloat162_rn(
        make_float2(xf[2 * j] * factor * w.x, xf[2 * j + 1] * factor * w.y));
    const float2 nqf = __bfloat1622float2(nq);
    const float2 val = make_float2(nqf.x * t.x + sh.x, nqf.y * t.y + sh.y);
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
    const float total2 = block_reduce_sum_f32<kTwoSync>(sumsq2, smem_partials, num_warps, 1);
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

// __launch_bounds__ must sit on the __global__ declaration, so the shared
// body is stamped into two kernels: the default one and a register-capped
// one (max 512 threads, min 4 blocks/SM -> <=32 regs/thread target) that
// lifts the dual entry's 40-reg occupancy cap (3 -> 4 CTAs/SM).
template <bool kHasNorm2, bool kTanhPre, bool kTwoSync>
__global__ void norm_tanh_mul_add_kernel(const NormTanhMulAddParams __grid_constant__ params) {
  norm_tanh_mul_add_body<kHasNorm2, kTanhPre, kTwoSync>(params);
}

template <bool kHasNorm2, bool kTanhPre, bool kTwoSync>
__global__ void __launch_bounds__(512, 4)
norm_tanh_mul_add_kernel_lb(const NormTanhMulAddParams __grid_constant__ params) {
  norm_tanh_mul_add_body<kHasNorm2, kTanhPre, kTwoSync>(params);
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
        norm_tanh_mul_add_kernel<false, false, false>, params);
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
        norm_tanh_mul_add_kernel<true, false, false>, params);
  }
};

// ---- Wave-2 variant launchers -------------------------------------------
// Uniform signatures: a fp32 [dim] tanh buffer is always passed; kTanhPre
// launches the precompute kernel into it first, otherwise it is unused
// (shape-verified only). kLb selects the register-capped kernel stamp.

inline void launch_tanh_precompute(
    const tvm::ffi::TensorView& scale, const tvm::ffi::TensorView& tanh_buf,
    uint32_t dim, DLDevice device) {
  host::LaunchKernel((dim + 255) / 256, 256, device)(
      tanh_scale_f32_kernel,
      static_cast<const __nv_bfloat16*>(scale.data_ptr()),
      static_cast<float*>(tanh_buf.data_ptr()), dim);
}

template <typename DType, bool kTanhPre, bool kTwoSync, bool kLb>
struct NormTanhMulAddSingleV2 {
  static void
  run(const tvm::ffi::TensorView x,
      const tvm::ffi::TensorView weight,
      const tvm::ffi::TensorView scale,
      const tvm::ffi::TensorView shift,
      const tvm::ffi::TensorView tanh_buf,
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
    TensorMatcher({D}).with_dtype<float>().with_device(device).verify(tanh_buf);

    const auto dim64 = D.unwrap();
    check_dim_supported(dim64);
    const auto num_rows = static_cast<uint32_t>(N.unwrap());
    const auto dim = static_cast<uint32_t>(dim64);

    if constexpr (kTanhPre) {
      launch_tanh_precompute(scale, tanh_buf, dim, device.unwrap());
    }
    const auto params = NormTanhMulAddParams{
        .x_ptr = x.data_ptr(),
        .weight_ptr = weight.data_ptr(),
        .scale_ptr = kTanhPre ? tanh_buf.data_ptr() : scale.data_ptr(),
        .shift_ptr = shift.data_ptr(),
        .y_ptr = y.data_ptr(),
        .weight2_ptr = nullptr,
        .scale2_ptr = nullptr,
        .y2_ptr = nullptr,
        .num_rows = num_rows,
        .dim = dim,
        .eps = static_cast<float>(eps),
    };
    constexpr auto kernel = kLb ? norm_tanh_mul_add_kernel_lb<false, kTanhPre, kTwoSync>
                                : norm_tanh_mul_add_kernel<false, kTanhPre, kTwoSync>;
    LaunchKernel(num_rows, dim / kElemsPerThread, device.unwrap())(kernel, params);
  }
};

template <typename DType, bool kTanhPre, bool kTwoSync, bool kLb>
struct NormTanhMulAddDualV2 {
  static void
  run(const tvm::ffi::TensorView x,
      const tvm::ffi::TensorView weight,
      const tvm::ffi::TensorView scale,
      const tvm::ffi::TensorView shift,
      const tvm::ffi::TensorView weight2,
      const tvm::ffi::TensorView scale2,
      const tvm::ffi::TensorView tanh_buf,
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
    TensorMatcher({D}).with_dtype<float>().with_device(device).verify(tanh_buf);

    const auto dim64 = D.unwrap();
    check_dim_supported(dim64);
    const auto num_rows = static_cast<uint32_t>(N.unwrap());
    const auto dim = static_cast<uint32_t>(dim64);

    if constexpr (kTanhPre) {
      launch_tanh_precompute(scale, tanh_buf, dim, device.unwrap());
    }
    const auto params = NormTanhMulAddParams{
        .x_ptr = x.data_ptr(),
        .weight_ptr = weight.data_ptr(),
        .scale_ptr = kTanhPre ? tanh_buf.data_ptr() : scale.data_ptr(),
        .shift_ptr = shift.data_ptr(),
        .y_ptr = y.data_ptr(),
        .weight2_ptr = weight2.data_ptr(),
        .scale2_ptr = scale2.data_ptr(),
        .y2_ptr = y2.data_ptr(),
        .num_rows = num_rows,
        .dim = dim,
        .eps = static_cast<float>(eps),
    };
    constexpr auto kernel = kLb ? norm_tanh_mul_add_kernel_lb<true, kTanhPre, kTwoSync>
                                : norm_tanh_mul_add_kernel<true, kTanhPre, kTwoSync>;
    LaunchKernel(num_rows, dim / kElemsPerThread, device.unwrap())(kernel, params);
  }
};

}  // namespace
