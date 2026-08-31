#include <torch/types.h>
#include <cuda.h>
#include <cuda_runtime.h>

#include <ATen/cuda/CUDAContext.h>
#include <c10/cuda/CUDAGuard.h>
#include <c10/cuda/CUDAException.h>
#include <cublas_v2.h>
#include <cuda_bf16.h>
#include <cuda_runtime.h>
#include <torch/extension.h>

namespace {

using BF16 = __nv_bfloat16;
using Vec8 = uint4;

constexpr int kWarpSize = 32;
constexpr int kTinyN = 144;
constexpr int kWideN = 896;
constexpr int kTinyK = 7168;
constexpr int kTinyNThreads = kTinyK / 8;
constexpr int kTinyNWarps = kTinyNThreads / kWarpSize;
constexpr int kSmallKN = 1536;
constexpr int kSmallKK = 128;
constexpr int kSmallKSplit = 12;
constexpr int kSmallKLanes = kSmallKK / 8;
constexpr int kSmallKThreads = kSmallKSplit * kSmallKLanes;
constexpr int kFallbackParts = 7;

__device__ __forceinline__ void pdl_wait() {
#if defined(__CUDA_ARCH__) && __CUDA_ARCH__ >= 900
  asm volatile("griddepcontrol.wait;" ::: "memory");
#endif
}

__device__ __forceinline__ void pdl_trigger() {
#if defined(__CUDA_ARCH__) && __CUDA_ARCH__ >= 900
  asm volatile("griddepcontrol.launch_dependents;" :::);
#endif
}

template <int Width>
__device__ __forceinline__ float warp_sum(float value) {
#pragma unroll
  for (int mask = Width / 2; mask >= 1; mask >>= 1) {
    value += __shfl_xor_sync(0xffffffffu, value, mask, 32);
  }
  return value;
}

template <int Width>
__device__ __forceinline__ double warp_sum_double(double value) {
#pragma unroll
  for (int mask = Width / 2; mask >= 1; mask >>= 1) {
    value += __shfl_xor_sync(0xffffffffu, value, mask, 32);
  }
  return value;
}

__device__ __forceinline__ float bf16_boundary_distance(
    float value, BF16 rounded) {
  const uint32_t bits = __float_as_uint(fabsf(value));
  const int exponent = (bits >> 23) & 0xff;
  if (exponent <= 8 || exponent >= 255) {
    return 0.0f;
  }
  const float half_ulp = __uint_as_float(
      static_cast<uint32_t>(exponent - 8) << 23);
  return half_ulp - fabsf(value - __bfloat162float(rounded));
}

__device__ __forceinline__ float fallback_repair_threshold(float value) {
  const int exponent = (__float_as_uint(fabsf(value)) >> 23) & 0xff;
  if (exponent <= 126) {
    return 7.5e-6f;
  }
  if (exponent <= 128) {
    return 1.05e-5f;
  }
  if (exponent == 129) {
    return 1.35e-5f;
  }
  return 1.5e-5f;
}

__device__ __forceinline__ bool bf16_needs_tiny_k_correction(float value) {
  const uint32_t bits = __float_as_uint(value);
  const uint32_t boundary_offset =
      (bits & 0xffffu) - static_cast<uint32_t>(0x8000 - 3);
  if (boundary_offset > 6u) {
    return false;
  }
  return (bits & 0x7fffffffu) >= 0x3e800000u;
}

__device__ __forceinline__ bool bf16_needs_mma_correction(
    float value, unsigned radius) {
  const uint32_t bits = __float_as_uint(value);
  const uint32_t boundary_offset =
      (bits & 0xffffu) - static_cast<uint32_t>(0x8000u - radius);
  return boundary_offset <= 2u * radius &&
      (bits & 0x7fffffffu) >= 0x3e800000u;
}

__device__ __forceinline__ void accumulate_pair(
    float& acc, const BF16* x, const BF16* w) {
  const float2 xf = __bfloat1622float2(
      *reinterpret_cast<const __nv_bfloat162*>(x));
  const float2 wf = __bfloat1622float2(
      *reinterpret_cast<const __nv_bfloat162*>(w));
  acc = fmaf(xf.x, wf.x, acc);
  acc = fmaf(xf.y, wf.y, acc);
}

__device__ __forceinline__ float balanced_dot8(
    const Vec8& xv, const Vec8& wv) {
  const BF16* xb = reinterpret_cast<const BF16*>(&xv);
  const BF16* wb = reinterpret_cast<const BF16*>(&wv);
  const float2 x0 = __bfloat1622float2(
      *reinterpret_cast<const __nv_bfloat162*>(xb + 0));
  const float2 x1 = __bfloat1622float2(
      *reinterpret_cast<const __nv_bfloat162*>(xb + 2));
  const float2 x2 = __bfloat1622float2(
      *reinterpret_cast<const __nv_bfloat162*>(xb + 4));
  const float2 x3 = __bfloat1622float2(
      *reinterpret_cast<const __nv_bfloat162*>(xb + 6));
  const float2 w0 = __bfloat1622float2(
      *reinterpret_cast<const __nv_bfloat162*>(wb + 0));
  const float2 w1 = __bfloat1622float2(
      *reinterpret_cast<const __nv_bfloat162*>(wb + 2));
  const float2 w2 = __bfloat1622float2(
      *reinterpret_cast<const __nv_bfloat162*>(wb + 4));
  const float2 w3 = __bfloat1622float2(
      *reinterpret_cast<const __nv_bfloat162*>(wb + 6));
  const float p0 = fmaf(x0.x, w0.x, x0.y * w0.y);
  const float p1 = fmaf(x1.x, w1.x, x1.y * w1.y);
  const float p2 = fmaf(x2.x, w2.x, x2.y * w2.y);
  const float p3 = fmaf(x3.x, w3.x, x3.y * w3.y);
  return (p0 + p1) + (p2 + p3);
}

__device__ __forceinline__ Vec8 load_vec8_global(const Vec8* ptr) {
  Vec8 value;
  asm volatile(
      "ld.global.v4.u32 {%0, %1, %2, %3}, [%4];"
      : "=r"(value.x), "=r"(value.y), "=r"(value.z), "=r"(value.w)
      : "l"(ptr)
      : "memory");
  return value;
}

__device__ __forceinline__ double exact_dot8(
    const Vec8& xv, const Vec8& wv, double value) {
  const BF16* xb = reinterpret_cast<const BF16*>(&xv);
  const BF16* wb = reinterpret_cast<const BF16*>(&wv);
  const float2 x0 = __bfloat1622float2(
      *reinterpret_cast<const __nv_bfloat162*>(xb + 0));
  const float2 x1 = __bfloat1622float2(
      *reinterpret_cast<const __nv_bfloat162*>(xb + 2));
  const float2 x2 = __bfloat1622float2(
      *reinterpret_cast<const __nv_bfloat162*>(xb + 4));
  const float2 x3 = __bfloat1622float2(
      *reinterpret_cast<const __nv_bfloat162*>(xb + 6));
  const float2 w0 = __bfloat1622float2(
      *reinterpret_cast<const __nv_bfloat162*>(wb + 0));
  const float2 w1 = __bfloat1622float2(
      *reinterpret_cast<const __nv_bfloat162*>(wb + 2));
  const float2 w2 = __bfloat1622float2(
      *reinterpret_cast<const __nv_bfloat162*>(wb + 4));
  const float2 w3 = __bfloat1622float2(
      *reinterpret_cast<const __nv_bfloat162*>(wb + 6));
  value += static_cast<double>(x0.x * w0.x);
  value += static_cast<double>(x0.y * w0.y);
  value += static_cast<double>(x1.x * w1.x);
  value += static_cast<double>(x1.y * w1.y);
  value += static_cast<double>(x2.x * w2.x);
  value += static_cast<double>(x2.y * w2.y);
  value += static_cast<double>(x3.x * w3.x);
  value += static_cast<double>(x3.y * w3.y);
  return value;
}

struct FloatExpansion {
  float hi;
  float lo;
};

__device__ __forceinline__ FloatExpansion two_sum(float a, float b) {
  const float sum = a + b;
  const float b_virtual = sum - a;
  const float error = (a - (sum - b_virtual)) + (b - b_virtual);
  return FloatExpansion{sum, error};
}

__device__ __forceinline__ FloatExpansion compensated_dot8(
    const Vec8& xv, const Vec8& wv) {
  const BF16* xb = reinterpret_cast<const BF16*>(&xv);
  const BF16* wb = reinterpret_cast<const BF16*>(&wv);
  FloatExpansion result{
      __bfloat162float(xb[0]) * __bfloat162float(wb[0]), 0.0f};
#pragma unroll
  for (int i = 1; i < 8; ++i) {
    const float product = __bfloat162float(xb[i]) * __bfloat162float(wb[i]);
    const FloatExpansion next = two_sum(result.hi, product);
    result.hi = next.hi;
    result.lo += next.lo;
  }
  return two_sum(result.hi, result.lo);
}

template <int Width>
__device__ __forceinline__ FloatExpansion warp_sum_compensated(
    FloatExpansion value) {
  const unsigned active = __activemask();
#pragma unroll
  for (int mask = Width / 2; mask >= 1; mask >>= 1) {
    const float other_hi = __shfl_xor_sync(active, value.hi, mask, 32);
    const float other_lo = __shfl_xor_sync(active, value.lo, mask, 32);
    const FloatExpansion high_sum = two_sum(value.hi, other_hi);
    const float low_sum = (value.lo + other_lo) + high_sum.lo;
    value = two_sum(high_sum.hi, low_sum);
  }
  return value;
}

__device__ __noinline__ BF16 corrected_dot8_subwarp(Vec8 xv, Vec8 wv) {
  const FloatExpansion precise =
      warp_sum_compensated<16>(compensated_dot8(xv, wv));
  return __float2bfloat16_rn(precise.hi + precise.lo);
}

template <int M>
__device__ __forceinline__ uint32_t load_u32_l2_prefetch(
    const uint32_t* ptr) {
  uint32_t value;
#if defined(__CUDA_ARCH__) && __CUDA_ARCH__ >= 800
  if constexpr (M == 7) {
    asm volatile("ld.global.ca.u32 %0, [%1];" : "=r"(value) : "l"(ptr));
  } else {
    asm volatile(
        "ld.global.L2::256B.u32 %0, [%1];" : "=r"(value) : "l"(ptr));
  }
#else
  value = *ptr;
#endif
  return value;
}

__device__ __forceinline__ uint32_t load_u32_weight(
    const uint32_t* ptr) {
  uint32_t value;
#if defined(__CUDA_ARCH__) && __CUDA_ARCH__ >= 800
  asm volatile("ld.global.ca.u32 %0, [%1];" : "=r"(value) : "l"(ptr));
#else
  value = *ptr;
#endif
  return value;
}

struct MmaBf16Fragment {
  uint32_t a0;
  uint32_t a1;
  uint32_t a2;
  uint32_t a3;
};

template <int M>
__device__ __forceinline__ MmaBf16Fragment load_tiny_k_mma_x_fragment(
    const BF16* __restrict__ x,
    int64_t x_stride,
    int row0,
    int row1,
    int thread_in_group,
    int kk) {
  MmaBf16Fragment fragment{};
  if (row0 < M) {
    const BF16* x_row = x + row0 * x_stride + kk;
    fragment.a0 = load_u32_l2_prefetch<M>(
        reinterpret_cast<const uint32_t*>(x_row + thread_in_group * 2));
    fragment.a1 = load_u32_l2_prefetch<M>(
        reinterpret_cast<const uint32_t*>(x_row + 8 + thread_in_group * 2));
  }
  if (row1 < M) {
    const BF16* x_row = x + row1 * x_stride + kk;
    fragment.a2 = load_u32_l2_prefetch<M>(
        reinterpret_cast<const uint32_t*>(x_row + thread_in_group * 2));
    fragment.a3 = load_u32_l2_prefetch<M>(
        reinterpret_cast<const uint32_t*>(x_row + 8 + thread_in_group * 2));
  }
  return fragment;
}

__device__ __forceinline__ void mma_m16n8k16_bf16(
    float& d0,
    float& d1,
    float& d2,
    float& d3,
    uint32_t a0,
    uint32_t a1,
    uint32_t a2,
    uint32_t a3,
    uint32_t b0,
    uint32_t b1) {
  asm volatile(
      "mma.sync.aligned.m16n8k16.row.col.f32.bf16.bf16.f32 "
      "{%0, %1, %2, %3}, "
      "{%4, %6, %5, %7}, "
      "{%8, %9}, "
      "{%0, %1, %2, %3};\n"
      : "+f"(d0), "+f"(d1), "+f"(d2), "+f"(d3)
      : "r"(a0), "r"(a1), "r"(a2), "r"(a3), "r"(b0), "r"(b1));
}

template <int Parts>
__device__ __forceinline__ float reduce_mma_parts(float values[Parts]) {
  if constexpr (Parts == 2) {
    return __fadd_rn(values[0], values[1]);
  } else if constexpr (Parts == 4) {
    return __fadd_rn(
        __fadd_rn(values[0], values[1]),
        __fadd_rn(values[2], values[3]));
  } else {
    return __fadd_rn(
        __fadd_rn(
            __fadd_rn(values[0], values[1]),
            __fadd_rn(values[2], values[3])),
        __fadd_rn(
            __fadd_rn(values[4], values[5]),
            __fadd_rn(values[6], values[7])));
  }
}

__device__ __forceinline__ bool bf16_needs_tiny_n_correction(
    float value, BF16 rounded, float threshold) {
  return fabsf(value) >= 0.25f &&
      bf16_boundary_distance(value, rounded) < threshold;
}

template <int Threads>
__device__ __forceinline__ void repair_tiny_n_output(
    BF16* out,
    const BF16* x,
    const BF16* w,
    double* warp_partials) {
  constexpr int kWarps = Threads / kWarpSize;
  const int tx = threadIdx.x;
  const int lane = tx & (kWarpSize - 1);
  const int warp = tx / kWarpSize;
  double value = 0.0;
  for (int k = tx; k < kTinyK; k += Threads) {
    value = fma(
        static_cast<double>(__bfloat162float(x[k])),
        static_cast<double>(__bfloat162float(w[k])),
        value);
  }
  value = warp_sum_double<32>(value);
  if (lane == 0) {
    warp_partials[warp] = value;
  }
  __syncthreads();
  if (warp == 0) {
    value = lane < kWarps ? warp_partials[lane] : 0.0;
    value = warp_sum_double<32>(value);
    if (lane == 0) {
      *out = __float2bfloat16_rn(static_cast<float>(value));
    }
  }
  __syncthreads();
}

__device__ __noinline__ BF16 exact_tiny_n_dot_warp(
    const BF16* __restrict__ x,
    const BF16* __restrict__ w,
    int lane) {
  double value = 0.0;
  for (int k = lane; k < kTinyK; k += kWarpSize) {
    value = fma(
        static_cast<double>(__bfloat162float(x[k])),
        static_cast<double>(__bfloat162float(w[k])),
        value);
  }
  value = warp_sum_double<kWarpSize>(value);
  return __float2bfloat16_rn(static_cast<float>(value));
}

template <int M, int N, int NSplit>
__global__ __launch_bounds__(kTinyNThreads, 1) void tiny_n_baseline_kernel(
    BF16* __restrict__ out,
    const BF16* __restrict__ x,
    const BF16* __restrict__ w) {
  const int bx = blockIdx.x;
  const int tx = threadIdx.x;
  const BF16* w_tile = w + bx * (NSplit * kTinyK);

  Vec8 wv[NSplit];
#pragma unroll
  for (int n = 0; n < NSplit; ++n) {
    wv[n] = reinterpret_cast<const Vec8*>(w_tile + n * kTinyK)[tx];
  }

  Vec8 xv[M];
#pragma unroll
  for (int m = 0; m < M; ++m) {
    xv[m] = reinterpret_cast<const Vec8*>(x + m * kTinyK)[tx];
  }

  __shared__ float partial[kTinyNWarps][M * NSplit];
  const int warp_id = tx / kWarpSize;
  const int lane = tx & (kWarpSize - 1);

#pragma unroll
  for (int m = 0; m < M; ++m) {
#pragma unroll
    for (int n = 0; n < NSplit; ++n) {
      float acc = 0.0f;
      const BF16* xb = reinterpret_cast<const BF16*>(&xv[m]);
      const BF16* wb = reinterpret_cast<const BF16*>(&wv[n]);
#pragma unroll
      for (int i = 0; i < 4; ++i) {
        accumulate_pair(acc, xb + 2 * i, wb + 2 * i);
      }
      partial[warp_id][m * NSplit + n] = warp_sum<32>(acc);
    }
  }

  __syncthreads();
  bool repair = false;
  if (tx < M * NSplit) {
    float value = partial[0][tx];
#pragma unroll
    for (int warp = 1; warp < kTinyNWarps; ++warp) {
      value += partial[warp][tx];
    }
    const int m = tx / NSplit;
    const int n = tx % NSplit;
    const BF16 rounded = __float2bfloat16_rn(value);
    out[m * N + bx * NSplit + n] = rounded;
    repair = bf16_needs_tiny_n_correction(value, rounded, 3.0e-6f);
  }

  if (warp_id * kWarpSize < M * NSplit) {
    unsigned pending = __ballot_sync(0xffffffffu, repair);
    while (pending != 0) {
      const int owner = __ffs(static_cast<int>(pending)) - 1;
      const int output_index = warp_id * kWarpSize + owner;
      const int m = output_index / NSplit;
      const int n = output_index % NSplit;
      const BF16 precise = exact_tiny_n_dot_warp(
          x + m * kTinyK, w_tile + n * kTinyK, lane);
      if (lane == 0) {
        out[m * N + bx * NSplit + n] = precise;
      }
      pending &= pending - 1;
    }
  }
}

template <int MT, int NS, int Threads, bool Improved>
__global__ __launch_bounds__(Threads) void tiny_n_tiled_kernel(
    BF16* __restrict__ out,
    const BF16* __restrict__ x,
    const BF16* __restrict__ w,
    int m_rows) {
  constexpr int kChunks = kTinyK / 8;
  constexpr int kIterations = (kChunks + Threads - 1) / Threads;
  constexpr int kWarps = Threads / kWarpSize;
  constexpr int kOutputs = MT * NS;
  constexpr int kNBlocks = kTinyN / NS;

  const int tx = threadIdx.x;
  const int n_base = (blockIdx.x % kNBlocks) * NS;
  const int m_base = (blockIdx.x / kNBlocks) * MT;

  Vec8 wv[NS][kIterations];
#pragma unroll
  for (int n = 0; n < NS; ++n) {
#pragma unroll
    for (int s = 0; s < kIterations; ++s) {
      const int chunk = tx + s * Threads;
      if (chunk < kChunks) {
        wv[n][s] = reinterpret_cast<const Vec8*>(
            w + (n_base + n) * kTinyK)[chunk];
      } else {
        wv[n][s] = Vec8{0, 0, 0, 0};
      }
    }
  }

  float acc[kOutputs];
#pragma unroll
  for (int output = 0; output < kOutputs; ++output) {
    acc[output] = 0.0f;
  }

#pragma unroll
  for (int s = 0; s < kIterations; ++s) {
    const int chunk = tx + s * Threads;
#pragma unroll
    for (int m = 0; m < MT; ++m) {
      Vec8 xv = Vec8{0, 0, 0, 0};
      if (m_base + m < m_rows && chunk < kChunks) {
        xv = reinterpret_cast<const Vec8*>(
            x + (m_base + m) * kTinyK)[chunk];
      }
#pragma unroll
      for (int n = 0; n < NS; ++n) {
        if constexpr (Improved) {
          acc[m * NS + n] += balanced_dot8(xv, wv[n][s]);
        } else {
          const BF16* xb = reinterpret_cast<const BF16*>(&xv);
          const BF16* wb = reinterpret_cast<const BF16*>(&wv[n][s]);
#pragma unroll
          for (int i = 0; i < 4; ++i) {
            accumulate_pair(acc[m * NS + n], xb + 2 * i, wb + 2 * i);
          }
        }
      }
    }
  }

  __shared__ float partial[kOutputs][kWarpSize];
  const int lane = tx & (kWarpSize - 1);
  const int warp = tx / kWarpSize;

#pragma unroll
  for (int output = 0; output < kOutputs; ++output) {
    const float value = warp_sum<32>(acc[output]);
    if (lane == 0) {
      partial[output][warp] = value;
    }
  }

  __syncthreads();
  for (int output = warp; output < kOutputs; output += kWarps) {
    float value;
    if constexpr (Improved) {
      double precise = lane < kWarps
          ? static_cast<double>(partial[output][lane])
          : 0.0;
      precise = warp_sum_double<32>(precise);
      value = static_cast<float>(precise);
    } else {
      value = lane < kWarps ? partial[output][lane] : 0.0f;
      value = warp_sum<32>(value);
    }
    const int m = output / NS;
    const int n = output % NS;
    bool repair = false;
    if (lane == 0 && m_base + m < m_rows) {
        const BF16 rounded = __float2bfloat16_rn(value);
        out[(m_base + m) * kTinyN + n_base + n] = rounded;
        constexpr float threshold = Improved ? 7.5e-7f : 1.5e-5f;
        repair = bf16_needs_tiny_n_correction(value, rounded, threshold);
    }
    repair = __shfl_sync(0xffffffffu, static_cast<int>(repair), 0);
    if (repair) {
      const BF16 precise = exact_tiny_n_dot_warp(
          x + (m_base + m) * kTinyK,
          w + (n_base + n) * kTinyK,
          lane);
      if (lane == 0) {
        out[(m_base + m) * kTinyN + n_base + n] = precise;
      }
    }
  }
}

template <int M, int NSplit>
__global__ __launch_bounds__(NSplit * kSmallKLanes, 1) void tiny_k_kernel(
    BF16* __restrict__ out,
    const BF16* __restrict__ x,
    const BF16* __restrict__ w,
    int64_t x_stride) {
  const int tx = threadIdx.x;
  const int n_idx = blockIdx.x * NSplit + tx / kSmallKLanes;
  const int work_id = tx % kSmallKLanes;
  const Vec8 wv = reinterpret_cast<const Vec8*>(
      w + n_idx * kSmallKK)[work_id];

  pdl_wait();

  Vec8 xv[M];
#pragma unroll
  for (int m = 0; m < M; ++m) {
    xv[m] = reinterpret_cast<const Vec8*>(x + m * x_stride)[work_id];
  }

  unsigned correction_mask = 0;
#pragma unroll
  for (int m = 0; m < M; ++m) {
    const float acc = balanced_dot8(xv[m], wv);
    const float value = warp_sum<16>(acc);
    const BF16 rounded = __float2bfloat16_rn(value);
    if (work_id == 0) {
      out[m * kSmallKN + n_idx] = rounded;
    }
    if (bf16_needs_tiny_k_correction(value)) {
      correction_mask |= 1u << m;
    }
  }

  while (correction_mask != 0) {
    const int m = __ffs(correction_mask) - 1;
    correction_mask &= correction_mask - 1;
    const Vec8 repair_x = reinterpret_cast<const Vec8*>(
        x + m * x_stride)[work_id];
    const BF16 precise = corrected_dot8_subwarp(repair_x, wv);
    if (work_id == 0) {
      out[m * kSmallKN + n_idx] = precise;
    }
  }
  pdl_trigger();
}

__device__ __noinline__ BF16 exact_dot16_subwarp(
    Vec8 xv0, Vec8 xv1, Vec8 wv0, Vec8 wv1) {
  double value = exact_dot8(xv0, wv0, 0.0);
  value = exact_dot8(xv1, wv1, value);
  value = warp_sum_double<8>(value);
  return __float2bfloat16_rn(static_cast<float>(value));
}

template <int M, int NSplit>
__global__ __launch_bounds__(NSplit * 8, 1) void tiny_k8_kernel(
    BF16* __restrict__ out,
    const BF16* __restrict__ x,
    const BF16* __restrict__ w,
    int64_t x_stride) {
  const int tx = threadIdx.x;
  const int n_idx = blockIdx.x * NSplit + tx / 8;
  const int work_id = tx & 7;
  const Vec8* w_row = reinterpret_cast<const Vec8*>(w + n_idx * kSmallKK);
  const Vec8 wv0 = w_row[work_id];
  const Vec8 wv1 = w_row[work_id + 8];

  pdl_wait();

  Vec8 xv0[M];
  Vec8 xv1[M];
#pragma unroll
  for (int m = 0; m < M; ++m) {
    const Vec8* x_row = reinterpret_cast<const Vec8*>(x + m * x_stride);
    xv0[m] = x_row[work_id];
    xv1[m] = x_row[work_id + 8];
  }

  unsigned correction_mask = 0;
#pragma unroll
  for (int m = 0; m < M; ++m) {
    const float acc = balanced_dot8(xv0[m], wv0) +
        balanced_dot8(xv1[m], wv1);
    const float value = warp_sum<8>(acc);
    const BF16 rounded = __float2bfloat16_rn(value);
    if (work_id == 0) {
      out[m * kSmallKN + n_idx] = rounded;
    }
    if (bf16_needs_tiny_k_correction(value)) {
      correction_mask |= 1u << m;
    }
  }

  while (correction_mask != 0) {
    const int m = __ffs(correction_mask) - 1;
    correction_mask &= correction_mask - 1;
    const BF16 precise = exact_dot16_subwarp(
        xv0[m], xv1[m], wv0, wv1);
    if (work_id == 0) {
      out[m * kSmallKN + n_idx] = precise;
    }
  }
  pdl_trigger();
}

template <int M, int Parts, unsigned RepairRadius, int BlockWarps = 2>
__global__ __launch_bounds__(BlockWarps * kWarpSize, 1) void tiny_k_mma_kernel(
    BF16* __restrict__ out,
    const BF16* __restrict__ x,
    const BF16* __restrict__ w,
    int64_t x_stride) {
  static_assert(Parts == 2 || Parts == 4 || Parts == 8);
  const int lane = threadIdx.x & (kWarpSize - 1);
  const int warp = threadIdx.x / kWarpSize;
  const int group = lane >> 2;
  const int thread_in_group = lane & 3;
  const int n_base = (blockIdx.x * BlockWarps + warp) * 8;
  const int row0 = group;
  const int row1 = group + 8;
  const int column0 = n_base + thread_in_group * 2;

  uint32_t weight0[kSmallKK / 16];
  uint32_t weight1[kSmallKK / 16];
#pragma unroll
  for (int kk = 0; kk < kSmallKK; kk += 16) {
    const BF16* w_column = w + (n_base + group) * kSmallKK + kk;
    weight0[kk / 16] = load_u32_weight(
        reinterpret_cast<const uint32_t*>(
            w_column + thread_in_group * 2));
    weight1[kk / 16] = load_u32_weight(
        reinterpret_cast<const uint32_t*>(
            w_column + 8 + thread_in_group * 2));
  }

  pdl_wait();

  float accum[Parts][4] = {};
#pragma unroll
  for (int kk = 0; kk < kSmallKK; kk += 16) {
    const MmaBf16Fragment fragment = load_tiny_k_mma_x_fragment<M>(
        x, x_stride, row0, row1, thread_in_group, kk);
    const int part = (kk / 16) & (Parts - 1);
    mma_m16n8k16_bf16(
        accum[part][0],
        accum[part][1],
        accum[part][2],
        accum[part][3],
        fragment.a0,
        fragment.a1,
        fragment.a2,
        fragment.a3,
        weight0[kk / 16],
        weight1[kk / 16]);
  }

  float values[Parts];
#pragma unroll
  for (int part = 0; part < Parts; ++part) {
    values[part] = accum[part][0];
  }
  const float d0 = reduce_mma_parts<Parts>(values);
#pragma unroll
  for (int part = 0; part < Parts; ++part) {
    values[part] = accum[part][1];
  }
  const float d1 = reduce_mma_parts<Parts>(values);
#pragma unroll
  for (int part = 0; part < Parts; ++part) {
    values[part] = accum[part][2];
  }
  const float d2 = reduce_mma_parts<Parts>(values);
#pragma unroll
  for (int part = 0; part < Parts; ++part) {
    values[part] = accum[part][3];
  }
  const float d3 = reduce_mma_parts<Parts>(values);

  if (row0 < M) {
    *reinterpret_cast<__nv_bfloat162*>(
        out + row0 * kSmallKN + column0) =
        __floats2bfloat162_rn(d0, d1);
  }
  if (row1 < M) {
    *reinterpret_cast<__nv_bfloat162*>(
        out + row1 * kSmallKN + column0) =
        __floats2bfloat162_rn(d2, d3);
  }

  const float outputs[4] = {d0, d1, d2, d3};
  unsigned repair_bits = 0;
#pragma unroll
  for (int slot = 0; slot < 4; ++slot) {
    const int output_row = group + ((slot >> 1) * 8);
    repair_bits |= static_cast<unsigned>(
        output_row < M &&
        bf16_needs_mma_correction(outputs[slot], RepairRadius))
        << slot;
  }
  unsigned pending = __ballot_sync(0xffffffffu, repair_bits != 0);
  while (pending != 0) {
    const int owner = __ffs(static_cast<int>(pending)) - 1;
    unsigned owner_bits = __shfl_sync(
        0xffffffffu, repair_bits, owner, kWarpSize);
    while (owner_bits != 0) {
      const int slot = __ffs(static_cast<int>(owner_bits)) - 1;
      const int repair_row = (owner >> 2) + ((slot >> 1) * 8);
      const int repair_column =
          n_base + (owner & 3) * 2 + (slot & 1);
      double exact = 0.0;
#pragma unroll
      for (int offset = lane; offset < kSmallKK; offset += kWarpSize) {
        exact = fma(
            static_cast<double>(__bfloat162float(
                x[repair_row * x_stride + offset])),
            static_cast<double>(__bfloat162float(
                w[repair_column * kSmallKK + offset])),
            exact);
      }
      exact = warp_sum_double<kWarpSize>(exact);
      if (lane == 0) {
        out[repair_row * kSmallKN + repair_column] =
            __float2bfloat16_rn(static_cast<float>(exact));
      }
      owner_bits &= owner_bits - 1;
    }
    pending &= pending - 1;
  }
  pdl_trigger();
}

__global__ __launch_bounds__(256) void reduce_convert_repair_kernel(
    BF16* __restrict__ out,
    const float* __restrict__ partials,
    const BF16* __restrict__ x,
    const BF16* __restrict__ w,
    int total,
    int64_t x_stride) {
  constexpr int kThreads = 256;
  constexpr int kWarps = kThreads / kWarpSize;
  __shared__ double exact_partials[kWarps][kThreads];
  __shared__ int candidate_indices[kThreads];
  __shared__ int candidate_count;
  const int tx = threadIdx.x;
  const int lane = tx & (kWarpSize - 1);
  const int warp = tx / kWarpSize;
  const int index = blockIdx.x * blockDim.x + threadIdx.x;
  if (tx == 0) {
    candidate_count = 0;
  }
  __syncthreads();
  pdl_wait();

  if (index < total) {
    double precise = 0.0;
#pragma unroll
    for (int part = 0; part < kFallbackParts; ++part) {
      precise += static_cast<double>(partials[part * total + index]);
    }
    const float value = static_cast<float>(precise);
    const BF16 rounded = __float2bfloat16_rn(value);
    out[index] = rounded;
    if (fabsf(value) >= 0.25f &&
        bf16_boundary_distance(value, rounded) <
            fallback_repair_threshold(value)) {
      const int position = atomicAdd(&candidate_count, 1);
      candidate_indices[position] = index;
    }
  }
  __syncthreads();

  if (candidate_count == 0) {
    pdl_trigger();
    return;
  }

  for (int position = 0; position < candidate_count; ++position) {
    const int output_index = candidate_indices[position];
    const int m = output_index / kTinyN;
    const int n = output_index - m * kTinyN;
    const Vec8* x_row = reinterpret_cast<const Vec8*>(x + m * x_stride);
    const Vec8* w_row = reinterpret_cast<const Vec8*>(w + n * kTinyK);
    double value = 0.0;
#pragma unroll
    for (int part = 0; part < 4; ++part) {
      const int vector = tx + part * kThreads;
      if (vector < kTinyK / 8) {
        const Vec8 xv = load_vec8_global(x_row + vector);
        const Vec8 wv = load_vec8_global(w_row + vector);
        value = exact_dot8(xv, wv, value);
      }
    }
    value = warp_sum_double<32>(value);
    if (lane == 0) {
      exact_partials[warp][position] = value;
    }
  }
  __syncthreads();

  if (tx < candidate_count) {
    double value = 0.0;
#pragma unroll
    for (int source_warp = 0; source_warp < kWarps; ++source_warp) {
      value += exact_partials[source_warp][tx];
    }
    out[candidate_indices[tx]] =
        __float2bfloat16_rn(static_cast<float>(value));
  }
  pdl_trigger();
}

template <typename Kernel, typename... Args>
void launch_pdl(
    dim3 grid,
    dim3 block,
    cudaStream_t stream,
    Kernel kernel,
    Args... args) {
  cudaLaunchAttribute attribute{};
  attribute.id = cudaLaunchAttributeProgrammaticStreamSerialization;
  attribute.val.programmaticStreamSerializationAllowed = true;
  cudaLaunchConfig_t config{};
  config.gridDim = grid;
  config.blockDim = block;
  config.dynamicSmemBytes = 0;
  config.stream = stream;
  config.attrs = &attribute;
  config.numAttrs = 1;
  C10_CUDA_CHECK(cudaLaunchKernelEx(&config, kernel, args...));
}

void check_common(const torch::Tensor& x, const torch::Tensor& w) {
  TORCH_CHECK(x.is_cuda() && w.is_cuda(), "x and w must be CUDA tensors");
  TORCH_CHECK(x.scalar_type() == at::kBFloat16, "x must be bfloat16");
  TORCH_CHECK(w.scalar_type() == at::kBFloat16, "w must be bfloat16");
  TORCH_CHECK(x.dim() == 2 && w.dim() == 2, "x and w must be rank-2");
  TORCH_CHECK(x.get_device() == w.get_device(), "x and w must share a device");
  TORCH_CHECK(x.stride(1) == 1, "x inner stride must be 1");
  TORCH_CHECK(w.is_contiguous(), "w must be contiguous");
}

template <int M, int N, int NS>
void launch_tiny_n_baseline(
    cudaStream_t stream,
    BF16* out,
    const BF16* x,
    const BF16* w) {
  tiny_n_baseline_kernel<M, N, NS><<<
      dim3(N / NS), dim3(kTinyNThreads), 0, stream>>>(out, x, w);
}

template <int MT, int NS, int Threads, bool Improved>
void launch_tiny_n_tiled(
    int m,
    cudaStream_t stream,
    BF16* out,
    const BF16* x,
    const BF16* w) {
  const int blocks = (kTinyN / NS) * ((m + MT - 1) / MT);
  tiny_n_tiled_kernel<MT, NS, Threads, Improved><<<
      dim3(blocks), dim3(Threads), 0, stream>>>(out, x, w, m);
}

template <int M>
void dispatch_tiny_n_m(
    int64_t n,
    cudaStream_t stream,
    BF16* out,
    const BF16* x,
    const BF16* w) {
  if (n == kWideN) {
    launch_tiny_n_baseline<M, kWideN, 7>(stream, out, x, w);
  } else if constexpr (M == 11) {
    launch_tiny_n_tiled<3, 3, 448, true>(M, stream, out, x, w);
  } else if constexpr (M == 13) {
    launch_tiny_n_tiled<3, 3, 448, true>(M, stream, out, x, w);
  } else if constexpr (M == 16) {
    launch_tiny_n_tiled<3, 4, 448, true>(M, stream, out, x, w);
  } else {
    launch_tiny_n_baseline<M, kTinyN, 2>(stream, out, x, w);
  }
}

void dispatch_tiny_n(
    int64_t m,
    int64_t n,
    cudaStream_t stream,
    BF16* out,
    const BF16* x,
    const BF16* w) {
#define KDA_CASE(MValue) \
  case MValue: \
    dispatch_tiny_n_m<MValue>(n, stream, out, x, w); \
    break
  switch (m) {
    KDA_CASE(1); KDA_CASE(2); KDA_CASE(3); KDA_CASE(4);
    KDA_CASE(5); KDA_CASE(6); KDA_CASE(7); KDA_CASE(8);
    KDA_CASE(9); KDA_CASE(10); KDA_CASE(11); KDA_CASE(12);
    KDA_CASE(13); KDA_CASE(14); KDA_CASE(15); KDA_CASE(16);
    default: TORCH_CHECK(false, "tiny-N M must be in [1, 16]");
  }
#undef KDA_CASE
}

template <int M, int NSplit>
void launch_tiny_k(
    cudaStream_t stream,
    BF16* out,
    const BF16* x,
    const BF16* w,
    int64_t stride) {
  launch_pdl(
      dim3(kSmallKN / NSplit), dim3(NSplit * kSmallKLanes), stream,
      tiny_k_kernel<M, NSplit>, out, x, w, stride);
}

template <int M>
void launch_tiny_k_mma(
    cudaStream_t stream,
    BF16* out,
    const BF16* x,
    const BF16* w,
    int64_t stride) {
  constexpr int kBlockWarps =
      (M == 7 || M == 9 || M == 10 || M == 11 || M == 12 || M == 16 ? 3 : 2);
  launch_pdl(
      dim3(kSmallKN / (8 * kBlockWarps)),
      dim3(kBlockWarps * kWarpSize),
      stream,
      tiny_k_mma_kernel<
          M, (M == 10 || M == 12 ? 2 : 4), (M == 12 ? 6 : 3), kBlockWarps>,
      out,
      x,
      w,
      stride);
}

void dispatch_tiny_k_mma(
    int64_t m,
    cudaStream_t stream,
    BF16* out,
    const BF16* x,
    const BF16* w,
    int64_t stride) {
#define KDA_CASE(MValue) \
  case MValue: \
    launch_tiny_k_mma<MValue>(stream, out, x, w, stride); \
    break
  switch (m) {
    KDA_CASE(1); KDA_CASE(2); KDA_CASE(3); KDA_CASE(4);
    KDA_CASE(5); KDA_CASE(6); KDA_CASE(7); KDA_CASE(8);
    KDA_CASE(9); KDA_CASE(10); KDA_CASE(11); KDA_CASE(12);
    KDA_CASE(13); KDA_CASE(14); KDA_CASE(15); KDA_CASE(16);
    default: TORCH_CHECK(false, "tiny-K MMA M must be in [1, 16]");
  }
#undef KDA_CASE
}

void dispatch_tiny_k(
    int64_t m,
    cudaStream_t stream,
    BF16* out,
    const BF16* x,
    const BF16* w,
    int64_t stride) {
#define KDA_CASE(MValue, NSplit) \
  case MValue: \
    launch_tiny_k<MValue, NSplit>(stream, out, x, w, stride); \
    break
  switch (m) {
    KDA_CASE(1, 32); KDA_CASE(2, 24); KDA_CASE(3, 16); KDA_CASE(4, 16);
    KDA_CASE(5, 16); KDA_CASE(6, 16); KDA_CASE(7, 16); KDA_CASE(8, 12);
    KDA_CASE(9, 12); KDA_CASE(10, 12); KDA_CASE(11, 12); KDA_CASE(12, 12);
    KDA_CASE(13, 12); KDA_CASE(14, 12); KDA_CASE(15, 12); KDA_CASE(16, 12);
    default: TORCH_CHECK(false, "tiny-K M must be in [1, 16]");
  }
#undef KDA_CASE
}

template <int M, int NSplit>
void launch_tiny_k8(
    cudaStream_t stream,
    BF16* out,
    const BF16* x,
    const BF16* w,
    int64_t stride) {
  launch_pdl(
      dim3(kSmallKN / NSplit), dim3(NSplit * 8), stream,
      tiny_k8_kernel<M, NSplit>, out, x, w, stride);
}

}  // namespace

torch::Tensor tiny_n_cuda(torch::Tensor x, torch::Tensor w) {
  check_common(x, w);
  TORCH_CHECK(x.size(1) == kTinyK && w.size(1) == kTinyK, "tiny-N K mismatch");
  TORCH_CHECK(w.size(0) == kTinyN || w.size(0) == kWideN, "tiny-N N mismatch");
  TORCH_CHECK(x.is_contiguous(), "tiny-N x must be contiguous");
  const int64_t m = x.size(0);
  const int64_t n = w.size(0);
  TORCH_CHECK(m >= 1 && m <= (n == kWideN ? 8 : 16), "tiny-N M out of range");
  c10::cuda::CUDAGuard guard(x.device());
  auto out = torch::empty({m, n}, x.options());
  auto* out_ptr = reinterpret_cast<BF16*>(out.data_ptr<at::BFloat16>());
  const auto* x_ptr = reinterpret_cast<const BF16*>(x.data_ptr<at::BFloat16>());
  const auto* w_ptr = reinterpret_cast<const BF16*>(w.data_ptr<at::BFloat16>());
  cudaStream_t stream = at::cuda::getCurrentCUDAStream(x.get_device());
  dispatch_tiny_n(m, n, stream, out_ptr, x_ptr, w_ptr);
  C10_CUDA_KERNEL_LAUNCH_CHECK();
  return out;
}

torch::Tensor tiny_k_cuda(torch::Tensor x, torch::Tensor w) {
  check_common(x, w);
  TORCH_CHECK(x.size(1) == kSmallKK, "tiny-K K mismatch");
  TORCH_CHECK(
      w.size(0) == kSmallKN && w.size(1) == kSmallKK,
      "tiny-K weight shape mismatch");
  TORCH_CHECK(
      x.stride(0) * sizeof(BF16) % sizeof(Vec8) == 0,
      "x rows must be aligned");
  const int64_t m = x.size(0);
  TORCH_CHECK(m >= 1 && m <= 16, "tiny-K M out of range");
  c10::cuda::CUDAGuard guard(x.device());
  auto out = torch::empty({m, kSmallKN}, x.options());
  auto* out_ptr = reinterpret_cast<BF16*>(out.data_ptr<at::BFloat16>());
  const auto* x_ptr = reinterpret_cast<const BF16*>(x.data_ptr<at::BFloat16>());
  const auto* w_ptr = reinterpret_cast<const BF16*>(w.data_ptr<at::BFloat16>());
  cudaStream_t stream = at::cuda::getCurrentCUDAStream(x.get_device());
  if (m == 1) {
    launch_tiny_k8<1, 32>(
        stream, out_ptr, x_ptr, w_ptr, x.stride(0));
  } else if (m >= 7) {
    dispatch_tiny_k_mma(m, stream, out_ptr, x_ptr, w_ptr, x.stride(0));
  } else {
    dispatch_tiny_k(m, stream, out_ptr, x_ptr, w_ptr, x.stride(0));
  }
  C10_CUDA_KERNEL_LAUNCH_CHECK();
  return out;
}

torch::Tensor fallback_small_k_cuda(torch::Tensor x, torch::Tensor w) {
  // The dispatcher still classifies M > 12 as fallback.  Reuse the accurate
  // vector GEMM arithmetic because the stock BF16 linear kernel can cross the
  // strict double-reference rounding boundary on this shape.
  return tiny_k_cuda(x, w);
}

torch::Tensor accurate_linear_cuda(torch::Tensor x, torch::Tensor w) {
  check_common(x, w);
  TORCH_CHECK(
      x.size(1) == kTinyK && w.size(0) == kTinyN && w.size(1) == kTinyK,
      "accurate fallback shape mismatch");
  TORCH_CHECK(x.stride(0) <= INT_MAX, "x stride is too large");
  TORCH_CHECK(x.size(0) <= INT_MAX, "M is too large");

  c10::cuda::CUDAGuard guard(x.device());
  const int m = static_cast<int>(x.size(0));
  const int total = m * kTinyN;
  auto out = torch::empty({m, kTinyN}, x.options());
  auto partials = torch::empty(
      {kFallbackParts, m, kTinyN}, x.options().dtype(at::kFloat));
  auto* out_ptr = reinterpret_cast<BF16*>(out.data_ptr<at::BFloat16>());
  auto* partials_ptr = partials.data_ptr<float>();
  const auto* x_ptr = reinterpret_cast<const BF16*>(x.data_ptr<at::BFloat16>());
  const auto* w_ptr = reinterpret_cast<const BF16*>(w.data_ptr<at::BFloat16>());
  cudaStream_t stream = at::cuda::getCurrentCUDAStream(x.get_device());
  const float alpha = 1.0f;
  const float beta = 0.0f;
  cublasHandle_t handle = at::cuda::getCurrentCUDABlasHandle();
  constexpr int split_k = kTinyK / kFallbackParts;

  const cublasStatus_t status = cublasGemmStridedBatchedEx(
      handle,
      CUBLAS_OP_T,
      CUBLAS_OP_N,
      kTinyN,
      m,
      split_k,
      &alpha,
      w_ptr,
      CUDA_R_16BF,
      kTinyK,
      split_k,
      x_ptr,
      CUDA_R_16BF,
      static_cast<int>(x.stride(0)),
      split_k,
      &beta,
      partials_ptr,
      CUDA_R_32F,
      kTinyN,
      total,
      kFallbackParts,
      CUBLAS_COMPUTE_32F,
      CUBLAS_GEMM_DEFAULT_TENSOR_OP);
  TORCH_CHECK(
      status == CUBLAS_STATUS_SUCCESS,
      "split cublasGemmStridedBatchedEx failed: ",
      status);

  constexpr int kThreads = 256;
  const int blocks = (total + kThreads - 1) / kThreads;
  launch_pdl(
      dim3(blocks),
      dim3(kThreads),
      stream,
      reduce_convert_repair_kernel,
      out_ptr,
      partials_ptr,
      x_ptr,
      w_ptr,
      total,
      x.stride(0));
  C10_CUDA_KERNEL_LAUNCH_CHECK();
  return out;
}
