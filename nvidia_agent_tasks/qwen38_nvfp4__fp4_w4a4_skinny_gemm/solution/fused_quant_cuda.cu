#include <cuda_bf16.h>
#include <cuda_runtime.h>

#include "tensorrt_llm/kernels/quantization.cuh"

namespace qwen38 {

constexpr int kSmallQuantColumns = 5120;
constexpr int kSmallQuantBlockColumns = kSmallQuantColumns / 16;
constexpr int kSmallQuantKtiles = kSmallQuantBlockColumns / 4;
constexpr int kSiluColumns = 17408;
constexpr int kSiluBlocksPerRow = kSiluColumns / 16;

// The large SiLU kernels make one streaming pass over gate/up activations.
// Avoid allocating those 32-byte vectors in L1, where NCU measures effectively
// no reuse. Keep the stock cached load for the launch-sized specializations.
template <class Vec>
__device__ __forceinline__ void load_streaming_vec(
    Vec& value, const Vec* pointer) {
  static_assert(sizeof(Vec) == 32);
  struct U32x8 {
    uint32_t data[8];
  };
  auto& words = reinterpret_cast<U32x8&>(value);
  asm volatile(
      "ld.global.L1::no_allocate.L2::evict_first.v8.u32 "
      "{%0, %1, %2, %3, %4, %5, %6, %7}, [%8];"
      : "=r"(words.data[0]), "=r"(words.data[1]), "=r"(words.data[2]),
        "=r"(words.data[3]), "=r"(words.data[4]), "=r"(words.data[5]),
        "=r"(words.data[6]), "=r"(words.data[7])
      : "l"(pointer)
      : "memory");
}

template <class Vec>
__device__ __forceinline__ void load_streaming_vec_16(
    Vec& value, const Vec* pointer) {
  static_assert(sizeof(Vec) == 16);
  struct U32x4 {
    uint32_t data[4];
  };
  auto& words = reinterpret_cast<U32x4&>(value);
  asm volatile(
      "ld.global.L1::no_allocate.v4.u32 "
      "{%0, %1, %2, %3}, [%4];"
      : "=r"(words.data[0]), "=r"(words.data[1]), "=r"(words.data[2]),
        "=r"(words.data[3])
      : "l"(pointer)
      : "memory");
}

template <int Rows, int Splits>
__global__ __launch_bounds__(128) void reduce_down_split_kernel(
    const float* partials, __nv_bfloat16* output) {
  constexpr int kElements = Rows * 5120;
  constexpr int kPairs = kElements / 2;
  auto* result = reinterpret_cast<__nv_bfloat162*>(output);
  for (int index = blockIdx.x * blockDim.x + threadIdx.x; index < kPairs;
       index += blockDim.x * gridDim.x) {
    float2 sum = reinterpret_cast<const float2*>(partials)[index];
#pragma unroll
    for (int split = 1; split < Splits; ++split) {
      const float2 value = reinterpret_cast<const float2*>(
          partials + split * kElements)[index];
      sum.x += value.x;
      sum.y += value.y;
    }
    result[index] = __floats2bfloat162_rn(sum.x, sum.y);
  }
}

template <int StaticRows>
__global__ __launch_bounds__(256, 4) void quantize_small_kernel(
    int rows,
    const __nv_bfloat16* input,
    const float* global_scale,
    uint64_t* output,
    uint32_t* output_scales) {
  using namespace tensorrt_llm::kernels;
  using Vec = PackedVec<__nv_bfloat16, 16>;

  const int active_rows = StaticRows == 0 ? rows : StaticRows;
  const int real_work = active_rows * kSmallQuantBlockColumns;
  const int zero_work = 32 * kSmallQuantKtiles;
  const int total_work = real_work + zero_work;
  for (int index = blockIdx.x * blockDim.x + threadIdx.x; index < total_work;
       index += blockDim.x * gridDim.x) {
    if (index < real_work) {
      Vec values;
      loadPackedVec(values, reinterpret_cast<const Vec*>(input) + index);
      const int row = index / kSmallQuantBlockColumns;
      const int column = index % kSmallQuantBlockColumns;
      auto* scale = cvt_quant_to_fp4_get_sf_out_offset<uint32_t, 16, 1>(
          row, column, kSmallQuantColumns, output_scales);
      output[index] = cvt_warp_fp16_to_fp4<
          __nv_bfloat16,
          16,
          16,
          false,
          false,
          std::false_type>(values, global_scale[0], scale);
    } else {
      const int zero_index = index - real_work;
      const int k_tile = zero_index / 32;
      const int outer_row = zero_index % 32;
      auto* words = output_scales + k_tile * 128 + outer_row * 4;
      if (outer_row >= active_rows) {
        // Scale words are 16-byte aligned by construction.  Most rows are
        // wholly padding for M in {1, 8, 9}, so clear all four inner-M groups
        // with one coalesced vector store.
        *reinterpret_cast<uint4*>(words) = make_uint4(0, 0, 0, 0);
      } else {
#pragma unroll
        for (int group = 1; group < 4; ++group) {
          if (outer_row + group * 32 >= active_rows) {
            words[group] = 0;
          }
        }
      }
    }
  }
}

template <int StaticRows>
__global__ __launch_bounds__(256, 4) void silu_small_kernel(
    int rows,
    const __nv_bfloat16* input,
    const float* global_scale,
    uint64_t* output,
    uint32_t* output_scales) {
  using namespace tensorrt_llm::kernels;
  using Vec = PackedVec<__nv_bfloat16, 16>;

  const int active_rows = StaticRows == 0 ? rows : StaticRows;
  const int work = active_rows * kSiluBlocksPerRow;
  for (int index = blockIdx.x * blockDim.x + threadIdx.x; index < work;
       index += blockDim.x * gridDim.x) {
    const int row = index / kSiluBlocksPerRow;
    const int column = index % kSiluBlocksPerRow;
    const int input_index = row * (2 * kSiluBlocksPerRow) + column;
    Vec gate;
    Vec up;
    loadPackedVec(gate, reinterpret_cast<const Vec*>(input) + input_index);
    loadPackedVec(
        up,
        reinterpret_cast<const Vec*>(input) + input_index + kSiluBlocksPerRow);
    silu_and_mul<__nv_bfloat16, 16>(gate, up);
    auto* scale = cvt_quant_to_fp4_get_sf_out_offset<uint32_t, 16, 1>(
        row, column, kSiluColumns, output_scales);
    output[index] = cvt_warp_fp16_to_fp4<
        __nv_bfloat16,
        16,
        16,
        false,
        false,
        std::false_type>(gate, global_scale[0], scale);
  }
}

// T=4096 is exactly 32 complete 128-row scale tiles. Stage one 128x32
// quantization tile's byte scales in shared memory, then write the native
// [K-tile, outer-M, inner-M, inner-K] layout with aligned 128-bit stores.
// The packed FP4 path remains row-major and uses the same bit-exact helper.
__global__ __launch_bounds__(256, 4) void silu_swizzled_4096_kernel(
    const __nv_bfloat16* input,
    const float* global_scale,
    uint64_t* output,
    uint32_t* output_scales) {
  using namespace tensorrt_llm::kernels;
  using Vec = PackedVec<__nv_bfloat16, 16>;
  constexpr int kRowsPerTile = 128;
  constexpr int kColumnsPerTile = 32;
  constexpr int kThreads = 256;
  constexpr int kTasksPerTile = kRowsPerTile * kColumnsPerTile;
  constexpr int kWordsPerTile = kTasksPerTile / 4;
  constexpr int kVectorsPerTile = kWordsPerTile / 4;
  constexpr int kKtilesPerRow = kSiluBlocksPerRow / 4;
  __shared__ uint8_t scale_bytes[kTasksPerTile];

  const int row_start = blockIdx.y * kRowsPerTile;
  const int column_start = blockIdx.x * kColumnsPerTile;
  const float sf_scale = global_scale[0];
  for (int local = threadIdx.x; local < kTasksPerTile;
       local += kThreads) {
    const int local_row = local / kColumnsPerTile;
    const int local_column = local % kColumnsPerTile;
    const int row = row_start + local_row;
    const int column = column_start + local_column;
    const int index = row * kSiluBlocksPerRow + column;
    const int input_index = row * (2 * kSiluBlocksPerRow) + column;
    Vec gate;
    Vec up;
    load_streaming_vec(gate, reinterpret_cast<const Vec*>(input) + input_index);
    load_streaming_vec(
        up,
        reinterpret_cast<const Vec*>(input) + input_index + kSiluBlocksPerRow);
    silu_and_mul<__nv_bfloat16, 16>(gate, up);
    output[index] = cvt_warp_fp16_to_fp4<
        __nv_bfloat16,
        16,
        16,
        false,
        false,
        std::false_type>(gate, sf_scale, scale_bytes + local);
  }
  __syncthreads();

  static_assert(kVectorsPerTile == kThreads);
  // A warp spans four rows and all eight K groups.  Its shared loads therefore
  // address every (row % 4, K-group) bank pair exactly once, instead of having
  // all lanes gather a fixed K group with an eight-way strided conflict.
  const int lane = threadIdx.x & 31;
  const int warp = threadIdx.x >> 5;
  const int k_tile_local = lane >> 2;
  const int outer_row = warp * 4 + (lane & 3);
  const int local_column = k_tile_local * 4;
  const auto* source = scale_bytes + outer_row * kColumnsPerTile + local_column;
  const uint4 packed = make_uint4(
      *reinterpret_cast<const uint32_t*>(source),
      *reinterpret_cast<const uint32_t*>(source + 32 * kColumnsPerTile),
      *reinterpret_cast<const uint32_t*>(source + 64 * kColumnsPerTile),
      *reinterpret_cast<const uint32_t*>(source + 96 * kColumnsPerTile));
  const int k_tile = blockIdx.x * (kColumnsPerTile / 4) + k_tile_local;
  const int64_t scale_offset =
      blockIdx.y * (kKtilesPerRow * 512) + k_tile * 512 + outer_row * 16;
  *reinterpret_cast<uint4*>(
      reinterpret_cast<uint8_t*>(output_scales) + scale_offset) = packed;
}

// Retained register-pressure variant: two adjacent lanes jointly quantize
// one 16-value scale block, keeping only eight BF16 values per lane.  It stages
// the same byte-scale tile and uses the same final scale-layout transpose as
// the production 16-value/thread kernel above.
__global__ __launch_bounds__(256, 4) void silu_swizzled_half8_4096_kernel(
    const __nv_bfloat16* input,
    const float* global_scale,
    uint32_t* output,
    uint32_t* output_scales) {
  using namespace tensorrt_llm::kernels;
  using Vec = PackedVec<__nv_bfloat16, 8>;
  constexpr int kRowsPerTile = 128;
  constexpr int kBlocksPerTile = 32;
  constexpr int kHalvesPerTileRow = 2 * kBlocksPerTile;
  constexpr int kThreads = 256;
  constexpr int kScaleTasksPerTile = kRowsPerTile * kBlocksPerTile;
  constexpr int kHalfTasksPerTile = 2 * kScaleTasksPerTile;
  constexpr int kVectorsPerTile = kScaleTasksPerTile / 16;
  constexpr int kHalfBlocksPerRow = 2 * kSiluBlocksPerRow;
  constexpr int kKtilesPerRow = kSiluBlocksPerRow / 4;
  __shared__ uint8_t scale_bytes[kScaleTasksPerTile];

  const int row_start = blockIdx.y * kRowsPerTile;
  const int half_column_start = blockIdx.x * kHalvesPerTileRow;
  const float sf_scale = global_scale[0];
  for (int local = threadIdx.x; local < kHalfTasksPerTile;
       local += kThreads) {
    const int local_row = local / kHalvesPerTileRow;
    const int local_half_column = local % kHalvesPerTileRow;
    const int row = row_start + local_row;
    const int half_column = half_column_start + local_half_column;
    const int index = row * kHalfBlocksPerRow + half_column;
    const int input_index = row * (2 * kHalfBlocksPerRow) + half_column;
    Vec gate;
    Vec up;
    load_streaming_vec_16(
        gate, reinterpret_cast<const Vec*>(input) + input_index);
    load_streaming_vec_16(
        up,
        reinterpret_cast<const Vec*>(input) + input_index +
            kHalfBlocksPerRow);
    silu_and_mul<__nv_bfloat16, 8>(gate, up);
    uint8_t* scale =
        (local_half_column & 1) == 0 ? scale_bytes + local / 2 : nullptr;
    output[index] = cvt_warp_fp16_to_fp4<
        __nv_bfloat16,
        16,
        8,
        false,
        false,
        std::false_type>(gate, sf_scale, scale);
  }
  __syncthreads();

  static_assert(kVectorsPerTile == kThreads);
  const int lane = threadIdx.x & 31;
  const int warp = threadIdx.x >> 5;
  const int k_tile_local = lane >> 2;
  const int outer_row = warp * 4 + (lane & 3);
  const int local_column = k_tile_local * 4;
  const auto* source = scale_bytes + outer_row * kBlocksPerTile + local_column;
  const uint4 packed = make_uint4(
      *reinterpret_cast<const uint32_t*>(source),
      *reinterpret_cast<const uint32_t*>(source + 32 * kBlocksPerTile),
      *reinterpret_cast<const uint32_t*>(source + 64 * kBlocksPerTile),
      *reinterpret_cast<const uint32_t*>(source + 96 * kBlocksPerTile));
  const int k_tile = blockIdx.x * (kBlocksPerTile / 4) + k_tile_local;
  const int64_t scale_offset =
      blockIdx.y * (kKtilesPerRow * 512) + k_tile * 512 + outer_row * 16;
  *reinterpret_cast<uint4*>(
      reinterpret_cast<uint8_t*>(output_scales) + scale_offset) = packed;
}

// T=4369 leaves a 17-row tail after 34 complete 128-row tiles. A narrower
// column tile, 128-thread CTA, and uniform tail specialization reduce wasted
// work while preserving the compiler register budget selected by launch bounds.
__global__ __launch_bounds__(256, 4) void silu_swizzled_4369_kernel(
    const __nv_bfloat16* input,
    const float* global_scale,
    uint64_t* output,
    uint32_t* output_scales) {
  using namespace tensorrt_llm::kernels;
  using Vec = PackedVec<__nv_bfloat16, 16>;
  constexpr int kRows = 4369;
  constexpr int kRowsPerTile = 128;
  constexpr int kColumnsPerTile = 16;
  constexpr int kThreads = 128;
  constexpr int kTasksPerTile = kRowsPerTile * kColumnsPerTile;
  constexpr int kWordsPerTile = kTasksPerTile / 4;
  constexpr int kVectorsPerTile = kWordsPerTile / 4;
  constexpr int kKtilesPerRow = kSiluBlocksPerRow / 4;
  __shared__ uint8_t scale_bytes[kTasksPerTile];

  const int row_start = blockIdx.y * kRowsPerTile;
  const int column_start = blockIdx.x * kColumnsPerTile;
  const float sf_scale = global_scale[0];

  // The final M tile contains exactly 17 live rows. Handle it as a uniform CTA
  // branch so the common path is branch-free and the tail neither initializes
  // nor writes the 111 padding rows that the public contract leaves unwritten.
  if (blockIdx.y == kRows / kRowsPerTile) {
    constexpr int kTailRows = kRows % kRowsPerTile;
    constexpr int kKtilesPerColumnTile = kColumnsPerTile / 4;
    constexpr int kTailTasks = kTailRows * kColumnsPerTile;
    for (int local = threadIdx.x; local < kTailTasks;
         local += kThreads) {
      const int local_row = local / kColumnsPerTile;
      const int local_column = local % kColumnsPerTile;
      const int row = row_start + local_row;
      const int column = column_start + local_column;
      const int index = row * kSiluBlocksPerRow + column;
      const int input_index = row * (2 * kSiluBlocksPerRow) + column;
      Vec gate;
      Vec up;
      load_streaming_vec(gate, reinterpret_cast<const Vec*>(input) + input_index);
      load_streaming_vec(
          up,
          reinterpret_cast<const Vec*>(input) + input_index + kSiluBlocksPerRow);
      silu_and_mul<__nv_bfloat16, 16>(gate, up);
      output[index] = cvt_warp_fp16_to_fp4<
          __nv_bfloat16,
          16,
          16,
          false,
          false,
          std::false_type>(gate, sf_scale, scale_bytes + local);
    }
    __syncthreads();

    // Tail rows occupy inner-M group zero. Store one aligned 16-byte scale
    // quartet per live outer-M row; the remaining three words are padding.
    constexpr int kTailWords = kTailRows * kKtilesPerColumnTile;
    for (int word = threadIdx.x; word < kTailWords;
         word += kThreads) {
      const int k_tile_local = word / kTailRows;
      const int local_row = word % kTailRows;
      const auto* source =
          scale_bytes + local_row * kColumnsPerTile + k_tile_local * 4;
      const uint32_t packed = *reinterpret_cast<const uint32_t*>(source);
      const int k_tile =
          blockIdx.x * kKtilesPerColumnTile + k_tile_local;
      const int64_t scale_offset =
          blockIdx.y * (kKtilesPerRow * 512) + k_tile * 512 +
          local_row * 16;
      *reinterpret_cast<uint4*>(
          reinterpret_cast<uint8_t*>(output_scales) + scale_offset) =
          make_uint4(packed, 0, 0, 0);
    }
    return;
  }

  for (int local = threadIdx.x; local < kTasksPerTile;
       local += kThreads) {
    const int local_row = local / kColumnsPerTile;
    const int local_column = local % kColumnsPerTile;
    const int row = row_start + local_row;
    const int column = column_start + local_column;
    const int index = row * kSiluBlocksPerRow + column;
    const int input_index = row * (2 * kSiluBlocksPerRow) + column;
    Vec gate;
    Vec up;
    load_streaming_vec(gate, reinterpret_cast<const Vec*>(input) + input_index);
    load_streaming_vec(
        up,
        reinterpret_cast<const Vec*>(input) + input_index + kSiluBlocksPerRow);
    silu_and_mul<__nv_bfloat16, 16>(gate, up);
    output[index] = cvt_warp_fp16_to_fp4<
        __nv_bfloat16,
        16,
        16,
        false,
        false,
        std::false_type>(gate, sf_scale, scale_bytes + local);
  }
  __syncthreads();

  static_assert(kVectorsPerTile == kThreads);
  const int vector = threadIdx.x;
  const int k_tile_local = vector / 32;
  const int outer_row = vector % 32;
  const int local_column = k_tile_local * 4;
  const auto* source = scale_bytes + outer_row * kColumnsPerTile + local_column;
  const uint4 packed = make_uint4(
      *reinterpret_cast<const uint32_t*>(source),
      *reinterpret_cast<const uint32_t*>(source + 32 * kColumnsPerTile),
      *reinterpret_cast<const uint32_t*>(source + 64 * kColumnsPerTile),
      *reinterpret_cast<const uint32_t*>(source + 96 * kColumnsPerTile));
  const int k_tile = blockIdx.x * (kColumnsPerTile / 4) + k_tile_local;
  const int64_t scale_offset =
      blockIdx.y * (kKtilesPerRow * 512) + k_tile * 512 + outer_row * 16;
  *reinterpret_cast<uint4*>(
      reinterpret_cast<uint8_t*>(output_scales) + scale_offset) = packed;
}

}  // namespace qwen38

void launch_reduce_down_split(
    void* output,
    const void* partials,
    int rows,
    int splits,
    cudaStream_t stream) {
  constexpr int kThreads = 128;
  if (rows == 1) {
    constexpr int kPairs = 5120 / 2;
    constexpr int kBlocks = (kPairs + kThreads - 1) / kThreads;
    if (splits == 2) {
      qwen38::reduce_down_split_kernel<1, 2><<<kBlocks, kThreads, 0, stream>>>(
          static_cast<const float*>(partials),
          static_cast<__nv_bfloat16*>(output));
    } else if (splits == 4) {
      qwen38::reduce_down_split_kernel<1, 4><<<kBlocks, kThreads, 0, stream>>>(
          static_cast<const float*>(partials),
          static_cast<__nv_bfloat16*>(output));
    } else if (splits == 8) {
      qwen38::reduce_down_split_kernel<1, 8><<<kBlocks, kThreads, 0, stream>>>(
          static_cast<const float*>(partials),
          static_cast<__nv_bfloat16*>(output));
    } else if (splits == 17) {
      qwen38::reduce_down_split_kernel<1, 17><<<kBlocks, kThreads, 0, stream>>>(
          static_cast<const float*>(partials),
          static_cast<__nv_bfloat16*>(output));
    }
  } else if (rows == 9) {
    constexpr int kPairs = 9 * 5120 / 2;
    constexpr int kBlocks = (kPairs + kThreads - 1) / kThreads;
    if (splits == 2) {
      qwen38::reduce_down_split_kernel<9, 2><<<kBlocks, kThreads, 0, stream>>>(
          static_cast<const float*>(partials),
          static_cast<__nv_bfloat16*>(output));
    } else if (splits == 4) {
      qwen38::reduce_down_split_kernel<9, 4><<<kBlocks, kThreads, 0, stream>>>(
          static_cast<const float*>(partials),
          static_cast<__nv_bfloat16*>(output));
    } else if (splits == 8) {
      qwen38::reduce_down_split_kernel<9, 8><<<kBlocks, kThreads, 0, stream>>>(
          static_cast<const float*>(partials),
          static_cast<__nv_bfloat16*>(output));
    } else if (splits == 17) {
      qwen38::reduce_down_split_kernel<9, 17><<<kBlocks, kThreads, 0, stream>>>(
          static_cast<const float*>(partials),
          static_cast<__nv_bfloat16*>(output));
    }
  }
}

void launch_small_quant(
    void* output,
    void* output_scales,
    const void* input,
    const void* global_scale,
    int rows,
    int grid_size,
    int block_size,
    cudaStream_t stream) {
  const auto* input_ptr = static_cast<const __nv_bfloat16*>(input);
  const auto* scale_ptr = static_cast<const float*>(global_scale);
  auto* output_ptr = static_cast<uint64_t*>(output);
  auto* output_scale_ptr = static_cast<uint32_t*>(output_scales);
  if (rows == 1) {
    qwen38::quantize_small_kernel<1><<<grid_size, block_size, 0, stream>>>(
        rows, input_ptr, scale_ptr, output_ptr, output_scale_ptr);
  } else if (rows == 8) {
    qwen38::quantize_small_kernel<8><<<grid_size, block_size, 0, stream>>>(
        rows, input_ptr, scale_ptr, output_ptr, output_scale_ptr);
  } else if (rows == 9) {
    qwen38::quantize_small_kernel<9><<<grid_size, block_size, 0, stream>>>(
        rows, input_ptr, scale_ptr, output_ptr, output_scale_ptr);
  } else {
    qwen38::quantize_small_kernel<0><<<grid_size, block_size, 0, stream>>>(
        rows, input_ptr, scale_ptr, output_ptr, output_scale_ptr);
  }
}

void launch_silu_small(
    void* output,
    void* output_scales,
    const void* input,
    const void* global_scale,
    int rows,
    int grid_size,
    int block_size,
    cudaStream_t stream) {
  const auto* input_ptr = static_cast<const __nv_bfloat16*>(input);
  const auto* scale_ptr = static_cast<const float*>(global_scale);
  auto* output_ptr = static_cast<uint64_t*>(output);
  auto* output_scale_ptr = static_cast<uint32_t*>(output_scales);
  if (rows == 1) {
    qwen38::silu_small_kernel<1><<<grid_size, block_size, 0, stream>>>(
        rows, input_ptr, scale_ptr, output_ptr, output_scale_ptr);
  } else if (rows == 9) {
    qwen38::silu_small_kernel<9><<<grid_size, block_size, 0, stream>>>(
        rows, input_ptr, scale_ptr, output_ptr, output_scale_ptr);
  } else if (rows == 4096) {
    qwen38::silu_small_kernel<4096><<<grid_size, block_size, 0, stream>>>(
        rows, input_ptr, scale_ptr, output_ptr, output_scale_ptr);
  } else if (rows == 4369) {
    qwen38::silu_small_kernel<4369><<<grid_size, block_size, 0, stream>>>(
        rows, input_ptr, scale_ptr, output_ptr, output_scale_ptr);
  } else {
    qwen38::silu_small_kernel<0><<<grid_size, block_size, 0, stream>>>(
        rows, input_ptr, scale_ptr, output_ptr, output_scale_ptr);
  }
}

void launch_silu_swizzled_4096(
    void* output,
    void* output_scales,
    const void* input,
    const void* global_scale,
    cudaStream_t stream) {
  constexpr int kRows = 4096;
  constexpr int kRowsPerTile = 128;
  constexpr int kColumnsPerTile = 32;
  const dim3 grid(
      qwen38::kSiluBlocksPerRow / kColumnsPerTile, kRows / kRowsPerTile);
  qwen38::silu_swizzled_4096_kernel<<<grid, 256, 0, stream>>>(
      static_cast<const __nv_bfloat16*>(input),
      static_cast<const float*>(global_scale),
      static_cast<uint64_t*>(output),
      static_cast<uint32_t*>(output_scales));
}

void launch_silu_swizzled_half8_4096(
    void* output,
    void* output_scales,
    const void* input,
    const void* global_scale,
    cudaStream_t stream) {
  constexpr int kRows = 4096;
  constexpr int kRowsPerTile = 128;
  constexpr int kColumnsPerTile = 32;
  const dim3 grid(
      qwen38::kSiluBlocksPerRow / kColumnsPerTile, kRows / kRowsPerTile);
  qwen38::silu_swizzled_half8_4096_kernel<<<grid, 256, 0, stream>>>(
      static_cast<const __nv_bfloat16*>(input),
      static_cast<const float*>(global_scale),
      static_cast<uint32_t*>(output),
      static_cast<uint32_t*>(output_scales));
}

void launch_silu_swizzled_4369(
    void* output,
    void* output_scales,
    const void* input,
    const void* global_scale,
    cudaStream_t stream) {
  const auto* input_ptr = static_cast<const __nv_bfloat16*>(input);
  const auto* scale_ptr = static_cast<const float*>(global_scale);
  auto* output_ptr = static_cast<uint64_t*>(output);
  auto* output_scale_ptr = static_cast<uint32_t*>(output_scales);
  constexpr int kRows = 4369;
  constexpr int kColumnsPerTile = 16;
  constexpr int kRowsPerTile = 128;
  const dim3 grid(
      qwen38::kSiluBlocksPerRow / kColumnsPerTile,
      (kRows + kRowsPerTile - 1) / kRowsPerTile);
  qwen38::silu_swizzled_4369_kernel<<<grid, 128, 0, stream>>>(
      input_ptr, scale_ptr, output_ptr, output_scale_ptr);
}

void launch_fused_quant(
    void* output,
    void* output_scales,
    const void* input,
    const void* global_scale,
    const void* mask,
    int rows,
    int columns,
    int grid_size,
    int block_size,
    cudaStream_t stream) {
  tensorrt_llm::kernels::cvt_fp16_to_fp4_expert<
      __nv_bfloat16,
      false,
      false,
      std::false_type><<<grid_size, block_size, 0, stream>>>(
      rows,
      columns,
      static_cast<const __nv_bfloat16*>(input),
      static_cast<const float*>(global_scale),
      static_cast<uint32_t*>(output),
      static_cast<uint32_t*>(output_scales),
      const_cast<int32_t*>(static_cast<const int32_t*>(mask)),
      true,
      1);
}
