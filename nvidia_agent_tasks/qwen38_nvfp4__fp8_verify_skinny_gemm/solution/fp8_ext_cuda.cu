#include <cuda_bf16.h>
#include <cuda_fp8.h>
#include <cuda_runtime.h>

#include <cstdint>

namespace qwen38_fp8 {

constexpr int kWarps = 8;
constexpr int kThreads = 32 * kWarps;
constexpr int kVectorBytes = 16;

__device__ __forceinline__ float dot16_fp8(
    const float4 weight,
    const float4 activation) {
  const auto* w2 = reinterpret_cast<const __nv_fp8x2_e4m3*>(&weight);
  const auto* x2 = reinterpret_cast<const __nv_fp8x2_e4m3*>(&activation);
  float result = 0.0f;
#pragma unroll
  for (int pair = 0; pair < 8; ++pair) {
    const float2 w = static_cast<float2>(w2[pair]);
    const float2 x = static_cast<float2>(x2[pair]);
    result = fmaf(w.x, x.x, result);
    result = fmaf(w.y, x.y, result);
  }
  return result;
}

template <
    int N,
    int K,
    int Rows,
    int Warps = kWarps,
    int Unroll = 1,
    int PrefetchDistance = 0>
__global__ __launch_bounds__(32 * Warps) void gemv_m1_kernel(
    __nv_bfloat16* __restrict__ output,
    const uint8_t* __restrict__ input,
    const uint8_t* __restrict__ weight,
    const float* __restrict__ alpha) {
  __shared__ __align__(16) uint8_t shared_input[K];

  const int tid = threadIdx.x;
  for (int offset = tid * kVectorBytes; offset < K;
       offset += 32 * Warps * kVectorBytes) {
    *reinterpret_cast<float4*>(shared_input + offset) =
        *reinterpret_cast<const float4*>(input + offset);
  }
  __syncthreads();

  const int warp = tid >> 5;
  const int lane = tid & 31;
  const int row_start = (blockIdx.x * Warps + warp) * Rows;
  if (row_start >= N) {
    return;
  }

  float accumulators[Rows] = {};
#pragma unroll 2
  for (int column = lane * kVectorBytes * Unroll; column < K;
       column += 32 * kVectorBytes * Unroll) {
    if constexpr (PrefetchDistance > 0) {
      constexpr int kIterationBytes = 32 * kVectorBytes * Unroll;
      const int prefetch_column = column + PrefetchDistance * kIterationBytes;
      if (prefetch_column < K && (lane & 7) == 0) {
#pragma unroll
        for (int row = 0; row < Rows; ++row) {
          const auto* prefetch_address =
              weight + static_cast<size_t>(row_start + row) * K +
              prefetch_column;
          asm volatile(
              "prefetch.global.L2 [%0];"
              :
              : "l"(prefetch_address)
              : "memory");
        }
      }
    }
    float4 x[Unroll];
#pragma unroll
    for (int item = 0; item < Unroll; ++item) {
      x[item] = *reinterpret_cast<const float4*>(
          shared_input + column + item * kVectorBytes);
    }
#pragma unroll
    for (int row = 0; row < Rows; ++row) {
      const auto* address =
          weight + static_cast<size_t>(row_start + row) * K + column;
#pragma unroll
      for (int item = 0; item < Unroll; ++item) {
        const float4 w = __ldcs(reinterpret_cast<const float4*>(
            address + item * kVectorBytes));
        accumulators[row] += dot16_fp8(w, x[item]);
      }
    }
  }

#pragma unroll
  for (int row = 0; row < Rows; ++row) {
#pragma unroll
    for (int offset = 16; offset > 0; offset >>= 1) {
      accumulators[row] +=
          __shfl_down_sync(0xffffffff, accumulators[row], offset);
    }
  }
  if (lane == 0) {
    const float scale = alpha[0];
    if constexpr (Rows == 2) {
      // The N=8192 path assigns two adjacent output rows to every warp. Pack
      // their BF16 conversion into one naturally aligned 32-bit store; this
      // halves sparse global-store instructions and sectors without changing
      // the reduction or its rounding mode.
      *reinterpret_cast<__nv_bfloat162*>(output + row_start) =
          __floats2bfloat162_rn(
              accumulators[0] * scale, accumulators[1] * scale);
    } else {
#pragma unroll
      for (int row = 0; row < Rows; ++row) {
        output[row_start + row] =
            __float2bfloat16_rn(accumulators[row] * scale);
      }
    }
  }
}

__device__ __forceinline__ uint16_t fp32_pair_to_e4m3(
    float low,
    float high) {
  uint16_t packed;
  asm("cvt.rn.satfinite.e4m3x2.f32 %0, %1, %2;"
      : "=h"(packed)
      : "f"(high), "f"(low));
  return packed;
}

template <int Lines>
__device__ __forceinline__ void prefetch_weight_lines_evict_last(
    const uint8_t* address) {
  static_assert(Lines >= 0 && Lines <= 48);
#pragma unroll
  for (int line = 0; line < Lines; ++line) {
    const auto* line_address = address + line * 128;
    asm volatile(
        "prefetch.global.L2::evict_last [%0];"
        :
        : "l"(line_address)
        : "memory");
  }
}

template <
    int K,
    int PrefetchWeightRows = 0,
    bool RetainPrefetchedWeight = (K == 5120),
    int PrefetchWeightLines = 2,
    int PrefetchLaterWaveLines = 0,
    int PrefetchTailRows = 0,
    bool UsePdl = (K == 5120)>
__global__ __launch_bounds__(64) void quantize_m9_kernel(
    uint8_t* __restrict__ output,
    const __nv_bfloat16* __restrict__ input,
    const float* __restrict__ scale,
    const uint8_t* __restrict__ weight = nullptr) {
  constexpr int kRows = 9;
  constexpr int kElementsPerVector = 8;
  constexpr int kVectors = kRows * K / kElementsPerVector;
  const int vector = blockIdx.x * blockDim.x + threadIdx.x;
  if (vector >= kVectors) {
    return;
  }
  // Let the programmatically dependent CUTLASS launch enter dispatch while
  // this short quantizer grid is still executing.  Its GDC wait keeps all TMA
  // reads behind completion of this grid, so the FP8 stores remain ordered.
  if constexpr (UsePdl) {
    cudaTriggerProgrammaticLaunchCompletion();
  }
  if constexpr (PrefetchWeightRows > 0) {
    // Use the otherwise underfilled quantizer grid to request weight lines in
    // L2 while BF16-to-FP8 conversion is in flight.
    // Keep the K=5120 requests at the back of L2's eviction queue until the
    // dependent GEMM consumes them.  K=6144 retains ordinary prefetches: its
    // serial launch has no dependent-dispatch interval to protect.
    // Both forms stay nonblocking; bulk prefetches extended the quantizer
    // interval enough to erase the overlap.
    if (vector < PrefetchWeightRows) {
      const auto* address = weight + static_cast<size_t>(vector) * K;
      if constexpr (RetainPrefetchedWeight) {
        prefetch_weight_lines_evict_last<PrefetchWeightLines>(address);
        if constexpr (PrefetchTailRows > 0) {
          if (vector < PrefetchTailRows) {
            const auto* tail_address =
                weight + static_cast<size_t>(PrefetchWeightRows + vector) * K;
            prefetch_weight_lines_evict_last<PrefetchWeightLines>(tail_address);
          }
        }
        if constexpr (PrefetchLaterWaveLines > 0) {

          // The wide GEMM launches 32-row tiles, so its first 188-SM wave
          // spans 6,016 weight rows.  Activation conversion supplies only
          // 5,760 threads; let its first 256 threads cover the remaining
          // rows and warm the complete first wave rather than stopping one
          // quarter-tile short.
          if (vector < 256) {
            const auto* tail_address =
                weight + static_cast<size_t>(PrefetchWeightRows + vector) * K;
            prefetch_weight_lines_evict_last<PrefetchWeightLines>(
                tail_address);
          }

          // The first 188-CTA wave consumes rows 0..6015. Queue the same
          // retained K prefix for both later waves after the first-wave
          // requests, turning this underfilled predecessor into a second
          // memory-request stream while the dependent GEMM is dispatching.
          const auto* second_wave_address =
              weight + static_cast<size_t>(6016 + vector) * K;
          prefetch_weight_lines_evict_last<PrefetchLaterWaveLines>(
              second_wave_address);
          if (vector < 4608) {
            const auto* third_wave_address =
                weight + static_cast<size_t>(11776 + vector) * K;
            prefetch_weight_lines_evict_last<PrefetchLaterWaveLines>(
                third_wave_address);
          }
        }
      } else {
        asm volatile(
            "prefetch.global.L2 [%0];"
            :
            : "l"(address)
            : "memory");
        asm volatile(
            "prefetch.global.L2 [%0];"
            :
            : "l"(address + 128)
            : "memory");
        if constexpr (PrefetchWeightLines == 4) {
          asm volatile(
              "prefetch.global.L2 [%0];"
              :
              : "l"(address + 256)
              : "memory");
          asm volatile(
              "prefetch.global.L2 [%0];"
              :
              : "l"(address + 384)
              : "memory");
        }
      }
    }
  }

  const int column = vector * kElementsPerVector;
  const float inverse_scale = 1.0f / scale[0];
  const uint4 raw = *reinterpret_cast<const uint4*>(input + column);
  const auto* pairs = reinterpret_cast<const __nv_bfloat162*>(&raw);
  uint64_t packed = 0;
#pragma unroll
  for (int pair = 0; pair < 4; ++pair) {
    float2 values = __bfloat1622float2(pairs[pair]);
    values.x *= inverse_scale;
    values.y *= inverse_scale;
    packed |= static_cast<uint64_t>(fp32_pair_to_e4m3(values.x, values.y))
        << (pair * 16);
  }
  *reinterpret_cast<uint64_t*>(output + column) = packed;
}

template <int N, int K, int Rows>
__global__ __launch_bounds__(kThreads, 2) void gemv_m9_kernel(
    __nv_bfloat16* __restrict__ output,
    const uint8_t* __restrict__ input,
    const uint8_t* __restrict__ weight,
    const float* __restrict__ weight_scale,
    const float* __restrict__ input_scale) {
  constexpr int M = 9;
  const int tid = threadIdx.x;
  const int warp = tid >> 5;
  const int lane = tid & 31;
  const int row_start = (blockIdx.x * kWarps + warp) * Rows;
  if (row_start >= N) {
    return;
  }

  float accumulators[Rows][M] = {};
  for (int column = lane * kVectorBytes; column < K;
       column += 32 * kVectorBytes) {
    float4 x_vectors[M];
#pragma unroll
    for (int m = 0; m < M; ++m) {
      x_vectors[m] = *reinterpret_cast<const float4*>(input + m * K + column);
    }

    float4 w_vectors[Rows];
#pragma unroll
    for (int row = 0; row < Rows; ++row) {
      const auto* address =
          weight + static_cast<size_t>(row_start + row) * K + column;
      w_vectors[row] = __ldcs(reinterpret_cast<const float4*>(address));
    }

#pragma unroll
    for (int pair = 0; pair < 8; ++pair) {
      float2 x_pairs[M];
#pragma unroll
      for (int m = 0; m < M; ++m) {
        const auto* x2 =
            reinterpret_cast<const __nv_fp8x2_e4m3*>(&x_vectors[m]);
        x_pairs[m] = static_cast<float2>(x2[pair]);
      }
#pragma unroll
      for (int row = 0; row < Rows; ++row) {
        const auto* w2 =
            reinterpret_cast<const __nv_fp8x2_e4m3*>(&w_vectors[row]);
        const float2 w = static_cast<float2>(w2[pair]);
#pragma unroll
        for (int m = 0; m < M; ++m) {
          accumulators[row][m] =
              fmaf(w.x, x_pairs[m].x, accumulators[row][m]);
          accumulators[row][m] =
              fmaf(w.y, x_pairs[m].y, accumulators[row][m]);
        }
      }
    }
  }

#pragma unroll
  for (int row = 0; row < Rows; ++row) {
#pragma unroll
    for (int m = 0; m < M; ++m) {
#pragma unroll
      for (int offset = 16; offset > 0; offset >>= 1) {
        accumulators[row][m] +=
            __shfl_down_sync(0xffffffff, accumulators[row][m], offset);
      }
    }
  }

  if (lane == 0) {
    const float scale = weight_scale[0] * input_scale[0];
#pragma unroll
    for (int row = 0; row < Rows; ++row) {
#pragma unroll
      for (int m = 0; m < M; ++m) {
        output[m * N + row_start + row] =
            __float2bfloat16_rn(accumulators[row][m] * scale);
      }
    }
  }
}

template <
    int N,
    int K,
    int Rows,
    int Warps = kWarps,
    int Unroll = 1,
    int PrefetchDistance = 0>
void run_m1(
    void* output,
    const void* input,
    const void* weight,
    const void* alpha,
    cudaStream_t stream) {
  constexpr int blocks = N / (Warps * Rows);
  gemv_m1_kernel<N, K, Rows, Warps, Unroll, PrefetchDistance>
      <<<blocks, 32 * Warps, 0, stream>>>(
      static_cast<__nv_bfloat16*>(output),
      static_cast<const uint8_t*>(input),
      static_cast<const uint8_t*>(weight),
      static_cast<const float*>(alpha));
}

template <int N, int K, int Rows>
void run_m9(
    void* output,
    void* quantized_input,
    const void* input,
    const void* weight,
    const void* weight_scale,
    const void* input_scale,
    cudaStream_t stream) {
  constexpr int quantization_blocks = (9 * K / 8 + 63) / 64;
  quantize_m9_kernel<K><<<quantization_blocks, 64, 0, stream>>>(
      static_cast<uint8_t*>(quantized_input),
      static_cast<const __nv_bfloat16*>(input),
      static_cast<const float*>(input_scale));
  constexpr int blocks = N / (kWarps * Rows);
  gemv_m9_kernel<N, K, Rows><<<blocks, kThreads, 0, stream>>>(
      static_cast<__nv_bfloat16*>(output),
      static_cast<const uint8_t*>(quantized_input),
      static_cast<const uint8_t*>(weight),
      static_cast<const float*>(weight_scale),
      static_cast<const float*>(input_scale));
}

}  // namespace qwen38_fp8

void launch_fp8_gemv(
    void* output,
    const void* input,
    const void* weight,
    const void* alpha,
    int n,
    int k,
    cudaStream_t stream) {
  using namespace qwen38_fp8;
  if (n == 16384 && k == 5120) {
    run_m1<16384, 5120, 2>(output, input, weight, alpha, stream);
  } else if (n == 8192 && k == 5120) {
    // Twice as many warps amortize the shared activation load over twice the
    // output rows while keeping the total launched thread count unchanged.
    run_m1<8192, 5120, 2, 16, 1, 1>(
        output, input, weight, alpha, stream);
  } else if (n == 5120 && k == 6144) {
    // Keep one output row per warp, but amortize the 6 KiB activation staging
    // over sixteen warps.  The 320-CTA grid still fills all 188 SMs while
    // halving the duplicated activation loads and shared-memory stores.
    run_m1<5120, 6144, 1, 16>(output, input, weight, alpha, stream);
  }
}

void launch_fp8_linear(
    void* output,
    void* quantized_input,
    const void* input,
    const void* weight,
    const void* weight_scale,
    const void* input_scale,
    int n,
    int k,
    cudaStream_t stream) {
  using namespace qwen38_fp8;
  if (n == 16384 && k == 5120) {
    run_m9<16384, 5120, 4>(
        output, quantized_input, input, weight, weight_scale, input_scale, stream);
  } else if (n == 8192 && k == 5120) {
    run_m9<8192, 5120, 2>(
        output, quantized_input, input, weight, weight_scale, input_scale, stream);
  } else if (n == 5120 && k == 6144) {
    run_m9<5120, 6144, 2>(
        output, quantized_input, input, weight, weight_scale, input_scale, stream);
  }
}

void launch_fp8_quantize(
    void* quantized_input,
    const void* input,
    const void* input_scale,
    const void* weight,
    int n,
    int k,
    cudaStream_t stream) {
  using namespace qwen38_fp8;
  if (k == 5120) {
    if (n == 16384) {
      // Prefetch the first four 512-byte K stages for every output row. The
      // dependent GEMM overlaps this nonblocking request stream with live
      // activation conversion and consumes the retained lines from L2.
      quantize_m9_kernel<5120, 5760, true, 16, 16><<<90, 64, 0, stream>>>(
          static_cast<uint8_t*>(quantized_input),
          static_cast<const __nv_bfloat16*>(input),
          static_cast<const float*>(input_scale),
          static_cast<const uint8_t*>(weight));
    } else {
      // This GEMM is a single 128-CTA wave.  Use the dependent quantizer's
      // otherwise idle issue slots to retain the first 4 KiB of every weight
      // row in L2 before that wave consumes it.  Thirty-two lines is the
      // measured saturation point; prefetching the final eight lines is a wash.
      quantize_m9_kernel<5120, 5760, true, 32, 0, 2432>
          <<<90, 64, 0, stream>>>(
          static_cast<uint8_t*>(quantized_input),
          static_cast<const __nv_bfloat16*>(input),
          static_cast<const float*>(input_scale),
          static_cast<const uint8_t*>(weight));
    }
  } else if (k == 6144) {
    // The 160-CTA GEMM is a single underfilled device wave. Release it while
    // conversion is live, and use the predecessor's otherwise idle issue
    // slots to retain every 128-byte line of every weight row for that wave.
    quantize_m9_kernel<6144, 5120, true, 48, 0, 0, true>
        <<<108, 64, 0, stream>>>(
        static_cast<uint8_t*>(quantized_input),
        static_cast<const __nv_bfloat16*>(input),
        static_cast<const float*>(input_scale),
        static_cast<const uint8_t*>(weight));
  }
}
