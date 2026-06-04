// Native CUDA replacement for the SGLang CuTe-DSL fused norm-tanh-modulation
// kernels (diffusion Z-Image residual modulation):
//
//   y  = round_to_dtype(norm(x)) * tanh(scale) + shift
//   y2 = round_to_dtype(norm2(round_to_dtype(y))) * (1 + scale2)        [optional]
//
// Semantics mirror baseline/norm_tanh_mul_add_norm_scale.py exactly:
//   - norm reductions accumulate in fp32; the normalized result is rounded to
//     the I/O dtype BEFORE modulation; the second norm consumes the rounded y.
//   - rms norm uses weight only (bias ignored); layer norm applies affine only
//     when BOTH weight and bias are present (encoded as one kHasAffine flag,
//     resolved by the Python wrapper).
//   - tanh is exact fp32 libdevice tanhf (no approximations, no fast-math).
//
// Performance structure (vs the CTA-per-row baseline):
//   - kRowsPerCta rows are processed by one CTA; weight/bias vectors and the
//     tanh(scale) / (1 + scale2) modulation vectors are loaded/computed once
//     per CTA and reused across rows whenever the tensor is row-invariant
//     (effective seq-stride 0, single-batch CTA or batch-stride 0) — the
//     production layout scale/scale2 = [1, 1, D].
//   - 128-bit (fp16/bf16) / 256-bit (fp32) vectorized loads and stores;
//     one thread owns 8 consecutive elements; block = D/8 threads.
//
// Modulation tensors scale/shift/scale2 accept any [1|B, 1|S, D] layout with
// unit stride on D; broadcast dims use effective stride 0 (derived host-side
// from the TensorView). x/y/y2 must be contiguous [B, S, D].

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

struct NormTanhModulationParams {
  void* __restrict__ y_ptr;
  void* __restrict__ y2_ptr;
  const void* __restrict__ x_ptr;
  const void* __restrict__ weight_ptr;
  const void* __restrict__ bias_ptr;
  const void* __restrict__ scale_ptr;
  const void* __restrict__ shift_ptr;
  const void* __restrict__ weight2_ptr;
  const void* __restrict__ bias2_ptr;
  const void* __restrict__ scale2_ptr;
  int64_t scale_b_stride;   // element strides; 0 encodes a broadcast dim
  int64_t scale_s_stride;
  int64_t shift_b_stride;
  int64_t shift_s_stride;
  int64_t scale2_b_stride;
  int64_t scale2_s_stride;
  uint32_t seq;
  uint32_t total_rows;  // batch * seq
  float eps;
};

constexpr uint32_t kVecElems = 8;

// Two-level fp32 sum reduction across the CTA. smem must hold kNumWarps + 1
// floats. Result is broadcast to all threads. Safe to call repeatedly with the
// same buffer (internal barriers order reuse).
template <uint32_t kNumWarps>
SGL_DEVICE float cta_reduce_sum_f32(float value, float* smem) {
  using namespace device;
  static_assert(kNumWarps >= 1 && kNumWarps <= kWarpThreads);
  value = warp::reduce_sum(value);
  const uint32_t warp_id = threadIdx.x / kWarpThreads;
  const uint32_t lane_id = threadIdx.x % kWarpThreads;
  if (lane_id == 0) {
    smem[warp_id] = value;
  }
  __syncthreads();
  if (warp_id == 0) {
    float partial = lane_id < kNumWarps ? smem[lane_id] : 0.0f;
    partial = warp::reduce_sum(partial);
    if (lane_id == 0) {
      smem[kNumWarps] = partial;
    }
  }
  __syncthreads();
  return smem[kNumWarps];
}

// Cap registers so several CTAs fit per SM: at 48 regs/thread the 480-thread
// production block dropped to 2 CTAs/SM (40% occupancy) and went latency-bound
// (NCU evidence, round 0). 4 CTAs x 512 threads = 2048 = SM thread limit.
template <uint32_t kThreads>
inline constexpr uint32_t kMinBlocksPerSmHint = kThreads <= 512 ? 4 : (kThreads <= 1024 ? 2 : 1);

template <int64_t kD, int32_t kRowsPerCta, bool kIsRms, bool kHasAffine, bool kSecondNorm, bool kUsePDL,
          typename DType>
__global__ void __launch_bounds__(kD / kVecElems, kMinBlocksPerSmHint<kD / kVecElems>)
    norm_tanh_modulation_kernel(const NormTanhModulationParams __grid_constant__ params) {
  using namespace device;

  constexpr uint32_t kThreads = kD / kVecElems;
  constexpr uint32_t kNumWarps = kThreads / kWarpThreads;
  using Vec = AlignedVector<DType, kVecElems>;

  __shared__ float reduce_smem[kNumWarps + 1];

  const uint32_t tid = threadIdx.x;
  const int64_t vec_idx = tid;  // index of this thread's 8-element chunk within a row

  PDLWaitPrimary<kUsePDL>();

  const auto to_f32 = [](DType v) -> float { return cast<float>(v); };
  const auto to_dtype = [](float v) -> DType { return cast<DType>(v); };

  // CTA-invariant affine vectors (norm weight/bias along D).
  float w1[kVecElems], b1[kVecElems];
  float w2[kVecElems], b2[kVecElems];
  if constexpr (kHasAffine) {
    Vec wv;
    wv.load(params.weight_ptr, vec_idx);
#pragma unroll
    for (uint32_t j = 0; j < kVecElems; ++j) w1[j] = to_f32(wv[j]);
    if constexpr (!kIsRms) {
      Vec bv;
      bv.load(params.bias_ptr, vec_idx);
#pragma unroll
      for (uint32_t j = 0; j < kVecElems; ++j) b1[j] = to_f32(bv[j]);
    }
    if constexpr (kSecondNorm) {
      Vec wv2;
      wv2.load(params.weight2_ptr, vec_idx);
#pragma unroll
      for (uint32_t j = 0; j < kVecElems; ++j) w2[j] = to_f32(wv2[j]);
      if constexpr (!kIsRms) {
        Vec bv2;
        bv2.load(params.bias2_ptr, vec_idx);
#pragma unroll
        for (uint32_t j = 0; j < kVecElems; ++j) b2[j] = to_f32(bv2[j]);
      }
    }
  }

  const uint32_t row_begin = blockIdx.x * kRowsPerCta;
  const uint32_t row_end =
      row_begin + kRowsPerCta < params.total_rows ? row_begin + kRowsPerCta : params.total_rows;
  if (row_begin >= params.total_rows) {
    PDLTriggerSecondary<kUsePDL>();
    return;
  }
  const uint32_t batch_first = row_begin / params.seq;
  const uint32_t batch_last = (row_end - 1) / params.seq;
  const bool cta_single_batch = batch_first == batch_last;

  const auto modulation_row = [&](const void* base, int64_t b_stride, int64_t s_stride, uint32_t b,
                                  uint32_t s) -> const DType* {
    return static_cast<const DType*>(base) + static_cast<int64_t>(b) * b_stride +
           static_cast<int64_t>(s) * s_stride;
  };

  // Hoist row-invariant modulation vectors: tanh(scale) and (1 + scale2).
  // Valid when the seq dim broadcasts AND either the batch dim broadcasts or
  // every row of this CTA lives in one batch (production: scale = [1, 1, D]).
  const bool scale_hoisted =
      params.scale_s_stride == 0 && (params.scale_b_stride == 0 || cta_single_batch);
  float tanh_scale[kVecElems];
  if (scale_hoisted) {
    Vec sv;
    sv.load(modulation_row(params.scale_ptr, params.scale_b_stride, 0, batch_first, 0), vec_idx);
#pragma unroll
    for (uint32_t j = 0; j < kVecElems; ++j) tanh_scale[j] = ::tanhf(to_f32(sv[j]));
  }
  bool scale2_hoisted = false;
  float one_plus_scale2[kVecElems];
  if constexpr (kSecondNorm) {
    scale2_hoisted =
        params.scale2_s_stride == 0 && (params.scale2_b_stride == 0 || cta_single_batch);
    if (scale2_hoisted) {
      Vec sv2;
      sv2.load(modulation_row(params.scale2_ptr, params.scale2_b_stride, 0, batch_first, 0), vec_idx);
#pragma unroll
      for (uint32_t j = 0; j < kVecElems; ++j) one_plus_scale2[j] = 1.0f + to_f32(sv2[j]);
    }
  }

  for (uint32_t r = row_begin; r < row_end; ++r) {
    const uint32_t b = r / params.seq;
    const uint32_t s = r - b * params.seq;
    const int64_t row_vec_base = static_cast<int64_t>(r) * (kD / kVecElems);

    // ---- first norm: fp32 reduction over x ----
    Vec xv;
    xv.load(params.x_ptr, row_vec_base + vec_idx);
    float xf[kVecElems];
#pragma unroll
    for (uint32_t j = 0; j < kVecElems; ++j) xf[j] = to_f32(xv[j]);

    float normalized[kVecElems];
    if constexpr (kIsRms) {
      float sum_sq = 0.0f;
#pragma unroll
      for (uint32_t j = 0; j < kVecElems; ++j) sum_sq += xf[j] * xf[j];
      sum_sq = cta_reduce_sum_f32<kNumWarps>(sum_sq, reduce_smem);
      const float factor = math::rsqrt(sum_sq / static_cast<float>(kD) + params.eps);
#pragma unroll
      for (uint32_t j = 0; j < kVecElems; ++j) {
        normalized[j] = xf[j] * factor;
        if constexpr (kHasAffine) normalized[j] *= w1[j];
      }
    } else {
      float sum = 0.0f;
#pragma unroll
      for (uint32_t j = 0; j < kVecElems; ++j) sum += xf[j];
      const float mean = cta_reduce_sum_f32<kNumWarps>(sum, reduce_smem) / static_cast<float>(kD);
      float sum_var = 0.0f;
#pragma unroll
      for (uint32_t j = 0; j < kVecElems; ++j) {
        const float centered = xf[j] - mean;
        sum_var += centered * centered;
      }
      const float var = cta_reduce_sum_f32<kNumWarps>(sum_var, reduce_smem) / static_cast<float>(kD);
      const float factor = math::rsqrt(var + params.eps);
#pragma unroll
      for (uint32_t j = 0; j < kVecElems; ++j) {
        normalized[j] = (xf[j] - mean) * factor;
        if constexpr (kHasAffine) normalized[j] = normalized[j] * w1[j] + b1[j];
      }
    }

    // Baseline rounds the normalized result to the I/O dtype before modulation.
    DType normalized_rounded[kVecElems];
#pragma unroll
    for (uint32_t j = 0; j < kVecElems; ++j) normalized_rounded[j] = to_dtype(normalized[j]);

    // ---- modulation: y = rounded_norm * tanh(scale) + shift ----
    if (!scale_hoisted) {
      Vec sv;
      sv.load(modulation_row(params.scale_ptr, params.scale_b_stride, params.scale_s_stride, b, s), vec_idx);
#pragma unroll
      for (uint32_t j = 0; j < kVecElems; ++j) tanh_scale[j] = ::tanhf(to_f32(sv[j]));
    }
    Vec shv;
    shv.load(modulation_row(params.shift_ptr, params.shift_b_stride, params.shift_s_stride, b, s), vec_idx);

    Vec yv;
#pragma unroll
    for (uint32_t j = 0; j < kVecElems; ++j) {
      yv[j] = to_dtype(to_f32(normalized_rounded[j]) * tanh_scale[j] + to_f32(shv[j]));
    }
    yv.store(params.y_ptr, row_vec_base + vec_idx);

    // ---- optional second norm on the dtype-rounded y ----
    if constexpr (kSecondNorm) {
      float yf[kVecElems];
#pragma unroll
      for (uint32_t j = 0; j < kVecElems; ++j) yf[j] = to_f32(yv[j]);

      float normalized2[kVecElems];
      if constexpr (kIsRms) {
        float sum_sq2 = 0.0f;
#pragma unroll
        for (uint32_t j = 0; j < kVecElems; ++j) sum_sq2 += yf[j] * yf[j];
        sum_sq2 = cta_reduce_sum_f32<kNumWarps>(sum_sq2, reduce_smem);
        const float factor2 = math::rsqrt(sum_sq2 / static_cast<float>(kD) + params.eps);
#pragma unroll
        for (uint32_t j = 0; j < kVecElems; ++j) {
          normalized2[j] = yf[j] * factor2;
          if constexpr (kHasAffine) normalized2[j] *= w2[j];
        }
      } else {
        float sum2 = 0.0f;
#pragma unroll
        for (uint32_t j = 0; j < kVecElems; ++j) sum2 += yf[j];
        const float mean2 = cta_reduce_sum_f32<kNumWarps>(sum2, reduce_smem) / static_cast<float>(kD);
        float sum_var2 = 0.0f;
#pragma unroll
        for (uint32_t j = 0; j < kVecElems; ++j) {
          const float centered2 = yf[j] - mean2;
          sum_var2 += centered2 * centered2;
        }
        const float var2 = cta_reduce_sum_f32<kNumWarps>(sum_var2, reduce_smem) / static_cast<float>(kD);
        const float factor2 = math::rsqrt(var2 + params.eps);
#pragma unroll
        for (uint32_t j = 0; j < kVecElems; ++j) {
          normalized2[j] = (yf[j] - mean2) * factor2;
          if constexpr (kHasAffine) normalized2[j] = normalized2[j] * w2[j] + b2[j];
        }
      }

      if (!scale2_hoisted) {
        Vec sv2;
        sv2.load(modulation_row(params.scale2_ptr, params.scale2_b_stride, params.scale2_s_stride, b, s),
                 vec_idx);
#pragma unroll
        for (uint32_t j = 0; j < kVecElems; ++j) one_plus_scale2[j] = 1.0f + to_f32(sv2[j]);
      }

      Vec y2v;
#pragma unroll
      for (uint32_t j = 0; j < kVecElems; ++j) {
        y2v[j] = to_dtype(to_f32(to_dtype(normalized2[j])) * one_plus_scale2[j]);
      }
      y2v.store(params.y2_ptr, row_vec_base + vec_idx);
    }
  }

  PDLTriggerSecondary<kUsePDL>();
}

template <int64_t kD, int32_t kRowsPerCta, bool kIsRms, bool kHasAffine, bool kSecondNorm, bool kUsePDL,
          typename DType>
struct FusedNormTanhModulationKernel {
  static_assert(kD % 256 == 0 && kD <= 8192, "D must be a multiple of 256 and <= 8192");
  static_assert(kRowsPerCta >= 1 && kRowsPerCta <= 64, "rows-per-CTA out of range");
  static_assert(
      std::is_same_v<DType, fp16_t> || std::is_same_v<DType, bf16_t> || std::is_same_v<DType, fp32_t>,
      "unsupported dtype");

  static constexpr auto kernel =
      norm_tanh_modulation_kernel<kD, kRowsPerCta, kIsRms, kHasAffine, kSecondNorm, kUsePDL, DType>;

  // Unused slots (per kHasAffine / kIsRms / kSecondNorm) receive an inert
  // placeholder TensorView from the Python wrapper; they are neither verified
  // nor dereferenced.
  static void
  run(tvm::ffi::TensorView y,
      tvm::ffi::TensorView y2,
      tvm::ffi::TensorView x,
      tvm::ffi::TensorView weight,
      tvm::ffi::TensorView bias,
      tvm::ffi::TensorView scale,
      tvm::ffi::TensorView shift,
      tvm::ffi::TensorView weight2,
      tvm::ffi::TensorView bias2,
      tvm::ffi::TensorView scale2,
      float eps) {
    using namespace host;

    auto B = SymbolicSize{"batch"};
    auto S = SymbolicSize{"seq"};
    auto device = SymbolicDevice{};
    device.set_options<kDLCUDA>();

    // x / y / y2: contiguous [B, S, D] (no with_strides => contiguity enforced).
    TensorMatcher({B, S, kD}).with_dtype<DType>().with_device(device).verify(x).verify(y);
    if constexpr (kSecondNorm) {
      TensorMatcher({B, S, kD}).with_dtype<DType>().with_device(device).verify(y2);
    }
    if constexpr (kHasAffine) {
      TensorMatcher({kD}).with_dtype<DType>().with_device(device).verify(weight);
      if constexpr (!kIsRms) {
        TensorMatcher({kD}).with_dtype<DType>().with_device(device).verify(bias);
      }
      if constexpr (kSecondNorm) {
        TensorMatcher({kD}).with_dtype<DType>().with_device(device).verify(weight2);
        if constexpr (!kIsRms) {
          TensorMatcher({kD}).with_dtype<DType>().with_device(device).verify(bias2);
        }
      }
    }

    const int64_t batch = B.unwrap();
    const int64_t seq = S.unwrap();

    constexpr int64_t kVecBytes = static_cast<int64_t>(kVecElems) * sizeof(DType);
    const auto check_alignment = [&](const tvm::ffi::TensorView& t, const char* name) {
      RuntimeCheck(
          reinterpret_cast<uintptr_t>(t.data_ptr()) % kVecBytes == 0,
          name,
          " base pointer must be aligned for vectorized access");
    };
    check_alignment(x, "x");
    check_alignment(y, "y");
    if constexpr (kSecondNorm) check_alignment(y2, "y2");

    // Modulation tensors: [1|B, 1|S, D], unit stride on D; broadcast dims get
    // effective stride 0; non-broadcast strides must keep rows vector-aligned.
    const auto modulation_strides = [&](const tvm::ffi::TensorView& t,
                                        const char* name) -> std::pair<int64_t, int64_t> {
      TensorMatcher({-1, -1, kD}).with_strides({-1, -1, 1}).with_dtype<DType>().with_device(device).verify(t);
      RuntimeCheck(t.size(0) == 1 || t.size(0) == batch, name, " dim 0 must be 1 or batch");
      RuntimeCheck(t.size(1) == 1 || t.size(1) == seq, name, " dim 1 must be 1 or seq");
      const int64_t b_stride = t.size(0) == 1 ? 0 : t.stride(0);
      const int64_t s_stride = t.size(1) == 1 ? 0 : t.stride(1);
      RuntimeCheck(
          b_stride % kVecElems == 0 && s_stride % kVecElems == 0,
          name,
          " strides must be multiples of the vector width");
      check_alignment(t, name);
      return {b_stride, s_stride};
    };

    const auto [scale_bs, scale_ss] = modulation_strides(scale, "scale");
    const auto [shift_bs, shift_ss] = modulation_strides(shift, "shift");
    int64_t scale2_bs = 0, scale2_ss = 0;
    if constexpr (kSecondNorm) {
      const auto strides2 = modulation_strides(scale2, "scale2");
      scale2_bs = strides2.first;
      scale2_ss = strides2.second;
    }
    if constexpr (kHasAffine) {
      check_alignment(weight, "weight");
      if constexpr (!kIsRms) check_alignment(bias, "bias");
      if constexpr (kSecondNorm) {
        check_alignment(weight2, "weight2");
        if constexpr (!kIsRms) check_alignment(bias2, "bias2");
      }
    }

    const int64_t total_rows = batch * seq;
    RuntimeCheck(total_rows > 0, "empty input");
    RuntimeCheck(total_rows <= INT64_C(0xffffffff), "row count exceeds kernel limit");

    const auto params = NormTanhModulationParams{
        .y_ptr = y.data_ptr(),
        .y2_ptr = kSecondNorm ? y2.data_ptr() : y.data_ptr(),
        .x_ptr = x.data_ptr(),
        .weight_ptr = kHasAffine ? weight.data_ptr() : x.data_ptr(),
        .bias_ptr = (kHasAffine && !kIsRms) ? bias.data_ptr() : x.data_ptr(),
        .scale_ptr = scale.data_ptr(),
        .shift_ptr = shift.data_ptr(),
        .weight2_ptr = (kHasAffine && kSecondNorm) ? weight2.data_ptr() : x.data_ptr(),
        .bias2_ptr = (kHasAffine && kSecondNorm && !kIsRms) ? bias2.data_ptr() : x.data_ptr(),
        .scale2_ptr = kSecondNorm ? scale2.data_ptr() : x.data_ptr(),
        .scale_b_stride = scale_bs,
        .scale_s_stride = scale_ss,
        .shift_b_stride = shift_bs,
        .shift_s_stride = shift_ss,
        .scale2_b_stride = scale2_bs,
        .scale2_s_stride = scale2_ss,
        .seq = static_cast<uint32_t>(seq),
        .total_rows = static_cast<uint32_t>(total_rows),
        .eps = eps,
    };

    constexpr uint32_t kThreads = kD / kVecElems;
    const uint32_t num_blocks = static_cast<uint32_t>(div_ceil(total_rows, static_cast<int64_t>(kRowsPerCta)));
    LaunchKernel(num_blocks, kThreads, device.unwrap()).enable_pdl(kUsePDL)(kernel, params);
  }
};

}  // namespace
