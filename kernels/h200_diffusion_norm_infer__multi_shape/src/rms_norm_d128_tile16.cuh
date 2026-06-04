// Multi-row tiled RMSNorm forward for the diffusion one-pass RMSNorm family
// (D=128, bf16/fp16), targeting the huge-M streaming shapes.
//
// y = x * rsqrt(mean(x^2) + eps) * w   (row-wise, no bias), fp32 accumulation.
//
// Mirrors the structure that makes the SGLang Triton baseline fast at
// M ~ 650k: one CTA owns a kRowsPerCta x 128 tile and the grid is exactly
// ceil(M / kRowsPerCta) blocks (no persistent grid-stride), exposing tens of
// thousands of independent CTAs for deep memory-level parallelism. Within a
// CTA, each row is reduced by kThreads/kRowsPerCta lanes using 128-bit packed
// loads; the [D] weight is loaded once per thread and reused across rows.
// Optional streaming cache hints (__ldcs/__stcs) mark x/y as evict-first,
// keeping the tiny reused weight resident in L1/L2.
//
// Built through the SGLang jit_kernel / tvm-ffi stack; conventions mirror
// src/rms_norm_d128.cuh (which remains the small/mid-M variant).

#include <sgl_kernel/tensor.h>

#include <sgl_kernel/runtime.cuh>
#include <sgl_kernel/type.cuh>
#include <sgl_kernel/utils.cuh>
#include <sgl_kernel/vec.cuh>
#include <sgl_kernel/warp.cuh>

#include <dlpack/dlpack.h>

#include <cstdint>
#include <type_traits>

namespace {

struct RmsNormTileParams {
  const void* __restrict__ x_ptr;
  void* __restrict__ y_ptr;
  const void* __restrict__ w_ptr;
  int64_t x_stride_bytes;
  int64_t y_stride_bytes;
  uint32_t num_rows;
  float eps;
};

template <typename Storage>
__device__ __forceinline__ Storage load_vec_streaming(const void* base, uint32_t slot) {
  static_assert(sizeof(Storage) == sizeof(float4));
  const float4 raw = __ldcs(reinterpret_cast<const float4*>(base) + slot);
  Storage out;
  static_assert(sizeof(out) == sizeof(raw));
  memcpy(&out, &raw, sizeof(raw));
  return out;
}

template <typename Storage>
__device__ __forceinline__ void store_vec_streaming(void* base, const Storage& v, uint32_t slot) {
  static_assert(sizeof(Storage) == sizeof(float4));
  float4 raw;
  memcpy(&raw, &v, sizeof(raw));
  __stcs(reinterpret_cast<float4*>(base) + slot, raw);
}

template <int64_t kDim, uint32_t kRowsPerCta, uint32_t kThreads, bool kStreamCache, bool kUsePDL,
          typename DType>
__global__ void __launch_bounds__(kThreads)
    rms_norm_tile(const RmsNormTileParams __grid_constant__ params) {
  using namespace device;

  static_assert(std::is_same_v<DType, fp16_t> || std::is_same_v<DType, bf16_t>);
  static_assert(kThreads % kWarpThreads == 0);
  static_assert(kThreads % kRowsPerCta == 0);

  constexpr uint32_t kLanesPerRow = kThreads / kRowsPerCta;
  static_assert(kLanesPerRow >= 1 && kLanesPerRow <= kWarpThreads,
                "a row must be owned by lanes within one warp");
  static_assert(kWarpThreads % kLanesPerRow == 0);
  constexpr uint32_t kElemsPerLane = kDim / kLanesPerRow;
  static_assert(kDim % kLanesPerRow == 0 && kElemsPerLane % 8 == 0,
                "each lane handles whole 128-bit chunks (8 elems)");
  constexpr uint32_t kChunks = kElemsPerLane / 8;  // 128-bit chunks per lane
  using Packed = packed_t<DType>;
  using Storage = AlignedVector<Packed, 4>;  // 4 packed pairs = 8 elems = 16B
  constexpr uint32_t kRowsPerWarp = kWarpThreads / kLanesPerRow;

  const uint32_t lane_id = threadIdx.x % kWarpThreads;
  const uint32_t warp_id = threadIdx.x / kWarpThreads;
  const uint32_t lane_in_row = lane_id % kLanesPerRow;
  const uint32_t row_in_warp = lane_id / kLanesPerRow;
  const uint32_t row_in_cta = warp_id * kRowsPerWarp + row_in_warp;
  const uint32_t row = blockIdx.x * kRowsPerCta + row_in_cta;

  PDLWaitPrimary<kUsePDL>();

  // Weight is identical for every row; load once and keep in registers.
  float w_elems[kElemsPerLane];
#pragma unroll
  for (uint32_t c = 0; c < kChunks; ++c) {
    const auto w_vec = load_as<Storage>(params.w_ptr, lane_in_row + c * kLanesPerRow);
#pragma unroll
    for (uint32_t j = 0; j < 4; ++j) {
      const auto [w0, w1] = cast<fp32x2_t>(w_vec[j]);
      w_elems[c * 8 + 2 * j] = w0;
      w_elems[c * 8 + 2 * j + 1] = w1;
    }
  }

  const bool valid = row < params.num_rows;
  // Invalid tail lanes read row 0 so the lane group stays converged through
  // the shuffle reduction; their result is simply not stored.
  const uint32_t safe_row = valid ? row : 0u;
  const void* x_row = pointer::offset(params.x_ptr, static_cast<int64_t>(safe_row) * params.x_stride_bytes);

  Storage x_vec[kChunks];
  float elems[kElemsPerLane];
  float sum_of_squares = 0.0f;
#pragma unroll
  for (uint32_t c = 0; c < kChunks; ++c) {
    x_vec[c] = kStreamCache ? load_vec_streaming<Storage>(x_row, lane_in_row + c * kLanesPerRow)
                            : load_as<Storage>(x_row, lane_in_row + c * kLanesPerRow);
#pragma unroll
    for (uint32_t j = 0; j < 4; ++j) {
      const auto [x0, x1] = cast<fp32x2_t>(x_vec[c][j]);
      elems[c * 8 + 2 * j] = x0;
      elems[c * 8 + 2 * j + 1] = x1;
      sum_of_squares += x0 * x0 + x1 * x1;
    }
  }

  sum_of_squares = warp::reduce_sum<kLanesPerRow>(sum_of_squares);
  const float rstd = math::rsqrt(sum_of_squares / static_cast<float>(kDim) + params.eps);

#pragma unroll
  for (uint32_t c = 0; c < kChunks; ++c) {
#pragma unroll
    for (uint32_t j = 0; j < 4; ++j) {
      const float y0 = elems[c * 8 + 2 * j] * rstd * w_elems[c * 8 + 2 * j];
      const float y1 = elems[c * 8 + 2 * j + 1] * rstd * w_elems[c * 8 + 2 * j + 1];
      x_vec[c][j] = cast<Packed, fp32x2_t>({y0, y1});
    }
  }
  if (valid) {
    void* y_row = pointer::offset(params.y_ptr, static_cast<int64_t>(row) * params.y_stride_bytes);
#pragma unroll
    for (uint32_t c = 0; c < kChunks; ++c) {
      if constexpr (kStreamCache) {
        store_vec_streaming<Storage>(y_row, x_vec[c], lane_in_row + c * kLanesPerRow);
      } else {
        store_as<Storage>(y_row, x_vec[c], lane_in_row + c * kLanesPerRow);
      }
    }
  }

  PDLTriggerSecondary<kUsePDL>();
}

template <int64_t kDim, uint32_t kRowsPerCta, uint32_t kThreads, bool kStreamCache, bool kUsePDL,
          typename DType>
struct RmsNormTileKernel {
  static_assert(kDim == 128, "this family is specialized for D=128");
  static constexpr auto kernel = rms_norm_tile<kDim, kRowsPerCta, kThreads, kStreamCache, kUsePDL, DType>;

  static void
  run(const tvm::ffi::TensorView x,
      const tvm::ffi::TensorView w,
      const tvm::ffi::TensorView y,
      float eps) {
    using namespace host;

    auto M = SymbolicSize{"num_rows"};
    auto D = SymbolicSize{"dim"};
    auto Sx = SymbolicSize{"x_row_stride"};
    auto Sy = SymbolicSize{"y_row_stride"};
    auto device = SymbolicDevice{};
    D.set_value(kDim);
    device.set_options<kDLCUDA>();

    TensorMatcher({M, D}).with_strides({Sx, 1}).with_dtype<DType>().with_device(device).verify(x);
    TensorMatcher({M, D}).with_strides({Sy, 1}).with_dtype<DType>().with_device(device).verify(y);
    TensorMatcher({D}).with_dtype<DType>().with_device(device).verify(w);

    const auto num_rows = static_cast<uint32_t>(M.unwrap());
    if (num_rows == 0) {
      return;  // empty input: output is already the (valid) empty tensor; a
               // zero-block launch would be an invalid CUDA configuration
    }
    const auto params = RmsNormTileParams{
        .x_ptr = x.data_ptr(),
        .y_ptr = y.data_ptr(),
        .w_ptr = w.data_ptr(),
        .x_stride_bytes = static_cast<int64_t>(Sx.unwrap() * sizeof(DType)),
        .y_stride_bytes = static_cast<int64_t>(Sy.unwrap() * sizeof(DType)),
        .num_rows = num_rows,
        .eps = eps,
    };

    // One tile per CTA, exactly like the Triton baseline's program grid: tens
    // of thousands of small independent CTAs give the memory system its
    // parallelism at huge M (the persistent capped grid starved it).
    const uint32_t num_blocks = div_ceil(num_rows, kRowsPerCta);
    LaunchKernel(num_blocks, kThreads, device.unwrap()).enable_pdl(kUsePDL)(kernel, params);
  }
};

}  // namespace
