#include <torch/extension.h>

#include <ATen/cuda/CUDAContext.h>
#include <c10/cuda/CUDAGuard.h>
#include <c10/cuda/CUDAException.h>
#include <cuda_bf16.h>

#include <cstdint>

namespace {

using nv_bfloat16 = __nv_bfloat16;
using nv_bfloat162 = __nv_bfloat162;

constexpr int kChannels = 16384;
constexpr int kPairs = kChannels / 2;
constexpr int kTokens = 9;
constexpr int kWidth = 4;

constexpr int kQkvzWidth = 16384;
constexpr int kQkvWidth = 10240;
constexpr int kZWidth = 6144;
constexpr int kValueHeads = 48;

union PackedRows2 {
  uint4 bits;
  nv_bfloat16 values[8];
};

__device__ __forceinline__ nv_bfloat162 pair_values(
    nv_bfloat16 lo, nv_bfloat16 hi) {
  return __halves2bfloat162(lo, hi);
}

__device__ __forceinline__ nv_bfloat162 dot4_exact(
    nv_bfloat162 a0,
    nv_bfloat162 a1,
    nv_bfloat162 a2,
    nv_bfloat162 a3,
    nv_bfloat162 b0,
    nv_bfloat162 b1,
    nv_bfloat162 b2,
    nv_bfloat162 b3) {
  const float2 p0 = __bfloat1622float2(__hmul2(a0, b0));
  const float2 p1 = __bfloat1622float2(__hmul2(a1, b1));
  const float2 p2 = __bfloat1622float2(__hmul2(a2, b2));
  const float2 p3 = __bfloat1622float2(__hmul2(a3, b3));
  float2 result;
  result.x = __fadd_rn(__fadd_rn(__fadd_rn(p0.x, p1.x), p2.x), p3.x);
  result.y = __fadd_rn(__fadd_rn(__fadd_rn(p0.y, p1.y), p2.y), p3.y);
  return __floats2bfloat162_rn(result.x, result.y);
}

__device__ __forceinline__ nv_bfloat162 dot4_packed(
    nv_bfloat162 a0,
    nv_bfloat162 a1,
    nv_bfloat162 a2,
    nv_bfloat162 a3,
    nv_bfloat162 b0,
    nv_bfloat162 b1,
    nv_bfloat162 b2,
    nv_bfloat162 b3) {
  nv_bfloat162 result = __hmul2(a0, b0);
  result = __hfma2(a1, b1, result);
  result = __hfma2(a2, b2, result);
  return __hfma2(a3, b3, result);
}

__global__ __launch_bounds__(32, 8) void conv1d_t9_w4_pair_kernel(
    const nv_bfloat162* __restrict__ x,
    nv_bfloat16* __restrict__ state,
    const nv_bfloat16* __restrict__ weight,
    nv_bfloat162* __restrict__ out) {
  const int pair = static_cast<int>(blockIdx.x) * blockDim.x + threadIdx.x;
  const int channel = 2 * pair;

  PackedRows2 state_rows;
  state_rows.bits = reinterpret_cast<const uint4*>(state)[pair];
  PackedRows2 weight_rows;
  weight_rows.bits = reinterpret_cast<const uint4*>(weight)[pair];

  const nv_bfloat162 x0 = x[0 * kPairs + pair];
  const nv_bfloat162 x1 = x[1 * kPairs + pair];
  const nv_bfloat162 x2 = x[2 * kPairs + pair];
  const nv_bfloat162 x3 = x[3 * kPairs + pair];
  const nv_bfloat162 x4 = x[4 * kPairs + pair];
  const nv_bfloat162 x5 = x[5 * kPairs + pair];
  const nv_bfloat162 x6 = x[6 * kPairs + pair];
  const nv_bfloat162 x7 = x[7 * kPairs + pair];
  const nv_bfloat162 x8 = x[8 * kPairs + pair];

  const nv_bfloat162 s0 = pair_values(state_rows.values[0], state_rows.values[4]);
  const nv_bfloat162 s1 = pair_values(state_rows.values[1], state_rows.values[5]);
  const nv_bfloat162 s2 = pair_values(state_rows.values[2], state_rows.values[6]);
  const nv_bfloat162 w0 = pair_values(weight_rows.values[0], weight_rows.values[4]);
  const nv_bfloat162 w1 = pair_values(weight_rows.values[1], weight_rows.values[5]);
  const nv_bfloat162 w2 = pair_values(weight_rows.values[2], weight_rows.values[6]);
  const nv_bfloat162 w3 = pair_values(weight_rows.values[3], weight_rows.values[7]);

  out[0 * kPairs + pair] = dot4_exact(s0, s1, s2, x0, w0, w1, w2, w3);
  out[1 * kPairs + pair] = dot4_exact(s1, s2, x0, x1, w0, w1, w2, w3);
  out[2 * kPairs + pair] = dot4_exact(s2, x0, x1, x2, w0, w1, w2, w3);
  out[3 * kPairs + pair] = dot4_exact(x0, x1, x2, x3, w0, w1, w2, w3);
  out[4 * kPairs + pair] = dot4_exact(x1, x2, x3, x4, w0, w1, w2, w3);
  out[5 * kPairs + pair] = dot4_exact(x2, x3, x4, x5, w0, w1, w2, w3);
  out[6 * kPairs + pair] = dot4_exact(x3, x4, x5, x6, w0, w1, w2, w3);
  out[7 * kPairs + pair] = dot4_exact(x4, x5, x6, x7, w0, w1, w2, w3);
  out[8 * kPairs + pair] = dot4_exact(x5, x6, x7, x8, w0, w1, w2, w3);

  state_rows.values[0] = __low2bfloat16(x6);
  state_rows.values[1] = __low2bfloat16(x7);
  state_rows.values[2] = __low2bfloat16(x8);
  state_rows.values[4] = __high2bfloat16(x6);
  state_rows.values[5] = __high2bfloat16(x7);
  state_rows.values[6] = __high2bfloat16(x8);
  reinterpret_cast<uint4*>(state)[pair] = state_rows.bits;
}

__global__ __launch_bounds__(32, 8) void conv1d_t9_w4_pair_fast_kernel(
    const nv_bfloat162* __restrict__ x,
    nv_bfloat16* __restrict__ state,
    const nv_bfloat16* __restrict__ weight,
    nv_bfloat162* __restrict__ out) {
  const int pair = static_cast<int>(blockIdx.x) * blockDim.x + threadIdx.x;

  PackedRows2 state_rows;
  state_rows.bits = reinterpret_cast<const uint4*>(state)[pair];
  PackedRows2 weight_rows;
  weight_rows.bits = reinterpret_cast<const uint4*>(weight)[pair];

  const nv_bfloat162 x0 = x[0 * kPairs + pair];
  const nv_bfloat162 x1 = x[1 * kPairs + pair];
  const nv_bfloat162 x2 = x[2 * kPairs + pair];
  const nv_bfloat162 x3 = x[3 * kPairs + pair];
  const nv_bfloat162 x4 = x[4 * kPairs + pair];
  const nv_bfloat162 x5 = x[5 * kPairs + pair];
  const nv_bfloat162 x6 = x[6 * kPairs + pair];
  const nv_bfloat162 x7 = x[7 * kPairs + pair];
  const nv_bfloat162 x8 = x[8 * kPairs + pair];

  const nv_bfloat162 s0 = pair_values(state_rows.values[0], state_rows.values[4]);
  const nv_bfloat162 s1 = pair_values(state_rows.values[1], state_rows.values[5]);
  const nv_bfloat162 s2 = pair_values(state_rows.values[2], state_rows.values[6]);
  const nv_bfloat162 w0 = pair_values(weight_rows.values[0], weight_rows.values[4]);
  const nv_bfloat162 w1 = pair_values(weight_rows.values[1], weight_rows.values[5]);
  const nv_bfloat162 w2 = pair_values(weight_rows.values[2], weight_rows.values[6]);
  const nv_bfloat162 w3 = pair_values(weight_rows.values[3], weight_rows.values[7]);

  out[0 * kPairs + pair] = dot4_packed(s0, s1, s2, x0, w0, w1, w2, w3);
  out[1 * kPairs + pair] = dot4_packed(s1, s2, x0, x1, w0, w1, w2, w3);
  out[2 * kPairs + pair] = dot4_packed(s2, x0, x1, x2, w0, w1, w2, w3);
  out[3 * kPairs + pair] = dot4_packed(x0, x1, x2, x3, w0, w1, w2, w3);
  out[4 * kPairs + pair] = dot4_packed(x1, x2, x3, x4, w0, w1, w2, w3);
  out[5 * kPairs + pair] = dot4_packed(x2, x3, x4, x5, w0, w1, w2, w3);
  out[6 * kPairs + pair] = dot4_packed(x3, x4, x5, x6, w0, w1, w2, w3);
  out[7 * kPairs + pair] = dot4_packed(x4, x5, x6, x7, w0, w1, w2, w3);
  out[8 * kPairs + pair] = dot4_packed(x5, x6, x7, x8, w0, w1, w2, w3);

  state_rows.values[0] = __low2bfloat16(x6);
  state_rows.values[1] = __low2bfloat16(x7);
  state_rows.values[2] = __low2bfloat16(x8);
  state_rows.values[4] = __high2bfloat16(x6);
  state_rows.values[5] = __high2bfloat16(x7);
  state_rows.values[6] = __high2bfloat16(x8);
  reinterpret_cast<uint4*>(state)[pair] = state_rows.bits;
}

torch::Tensor launch_conv(
    const torch::Tensor& x,
    const torch::Tensor& state,
    const torch::Tensor& weight) {
  TORCH_CHECK(x.is_cuda() && state.is_cuda() && weight.is_cuda(),
              "x/state/weight must be CUDA tensors");
  TORCH_CHECK(x.scalar_type() == at::kBFloat16 &&
                  state.scalar_type() == at::kBFloat16 &&
                  weight.scalar_type() == at::kBFloat16,
              "x/state/weight must be BF16");
  TORCH_CHECK(x.sizes() == at::IntArrayRef({1, kChannels, kTokens}),
              "x must have shape [1, 16384, 9]");
  TORCH_CHECK(state.sizes() == at::IntArrayRef({1, kChannels, kWidth}),
              "state must have shape [1, 16384, 4]");
  TORCH_CHECK(weight.sizes() == at::IntArrayRef({kChannels, kWidth}),
              "weight must have shape [16384, 4]");
  TORCH_CHECK(x.stride(1) == 1 && x.stride(2) == kChannels,
              "x must be channel-contiguous");
  TORCH_CHECK(state.is_contiguous() && weight.is_contiguous(),
              "state and weight must be contiguous");

  c10::cuda::CUDAGuard guard(x.device());
  auto out = torch::empty_like(x);
  constexpr int threads = 32;
  constexpr int blocks = kPairs / threads;
  auto stream = at::cuda::getCurrentCUDAStream(x.get_device());
  conv1d_t9_w4_pair_kernel<<<blocks, threads, 0, stream>>>(
      reinterpret_cast<const nv_bfloat162*>(x.data_ptr()),
      reinterpret_cast<nv_bfloat16*>(state.data_ptr()),
      reinterpret_cast<const nv_bfloat16*>(weight.data_ptr()),
      reinterpret_cast<nv_bfloat162*>(out.data_ptr()));
  C10_CUDA_KERNEL_LAUNCH_CHECK();
  return out;
}

template <int Threads>
torch::Tensor launch_conv_fast(
    const torch::Tensor& x,
    const torch::Tensor& state,
    const torch::Tensor& weight) {
  TORCH_CHECK(x.is_cuda() && state.is_cuda() && weight.is_cuda(),
              "x/state/weight must be CUDA tensors");
  TORCH_CHECK(x.scalar_type() == at::kBFloat16 &&
                  state.scalar_type() == at::kBFloat16 &&
                  weight.scalar_type() == at::kBFloat16,
              "x/state/weight must be BF16");
  TORCH_CHECK(x.sizes() == at::IntArrayRef({1, kChannels, kTokens}),
              "x must have shape [1, 16384, 9]");
  TORCH_CHECK(state.sizes() == at::IntArrayRef({1, kChannels, kWidth}),
              "state must have shape [1, 16384, 4]");
  TORCH_CHECK(weight.sizes() == at::IntArrayRef({kChannels, kWidth}),
              "weight must have shape [16384, 4]");
  TORCH_CHECK(x.stride(1) == 1 && x.stride(2) == kChannels,
              "x must be channel-contiguous");
  TORCH_CHECK(state.is_contiguous() && weight.is_contiguous(),
              "state and weight must be contiguous");

  c10::cuda::CUDAGuard guard(x.device());
  auto out = torch::empty_like(x);
  constexpr int blocks = kPairs / Threads;
  auto stream = at::cuda::getCurrentCUDAStream(x.get_device());
  conv1d_t9_w4_pair_fast_kernel<<<blocks, Threads, 0, stream>>>(
      reinterpret_cast<const nv_bfloat162*>(x.data_ptr()),
      reinterpret_cast<nv_bfloat16*>(state.data_ptr()),
      reinterpret_cast<const nv_bfloat16*>(weight.data_ptr()),
      reinterpret_cast<nv_bfloat162*>(out.data_ptr()));
  C10_CUDA_KERNEL_LAUNCH_CHECK();
  return out;
}

template <int Threads>
__global__ __launch_bounds__(Threads) void qkvzba_copy_kernel(
    const uint4* __restrict__ mixed_qkvz,
    const uint4* __restrict__ mixed_ba,
    uint4* __restrict__ output) {
  constexpr int kElemsPerVector = sizeof(uint4) / sizeof(nv_bfloat16);
  constexpr int kInputVectors = kQkvzWidth / kElemsPerVector;
  constexpr int kQkvVectors = kQkvWidth / kElemsPerVector;
  constexpr int kZVectors = kZWidth / kElemsPerVector;
  constexpr int kQkvBlocks = kQkvVectors / Threads;
  constexpr int kBaVectors = (2 * kValueHeads) / kElemsPerVector;

  const int token = static_cast<int>(blockIdx.y);
  const int block = static_cast<int>(blockIdx.x);
  const int lane = static_cast<int>(threadIdx.x);
  const int local_vector = block * Threads + lane;

  if (block < kQkvBlocks) {
    output[token * kQkvVectors + local_vector] =
        mixed_qkvz[token * kInputVectors + local_vector];
  } else {
    const int z_vector = local_vector - kQkvVectors;
    output[kTokens * kQkvVectors + token * kZVectors + z_vector] =
        mixed_qkvz[token * kInputVectors + kQkvVectors + z_vector];
  }

  if (block == 0 && lane < kBaVectors) {
    constexpr int kHeadVectors = kValueHeads / kElemsPerVector;
    const int region = lane / kHeadVectors;
    const int vector_in_region = lane - region * kHeadVectors;
    const int output_base = kTokens * (kQkvVectors + kZVectors);
    output[output_base + region * (kTokens * kHeadVectors) +
           token * kHeadVectors + vector_in_region] =
        mixed_ba[token * kBaVectors + lane];
  }
}

template <int Threads>
__global__ __launch_bounds__(Threads) void qkvzba_copy_flat_kernel(
    const uint4* __restrict__ mixed_qkvz,
    const uint4* __restrict__ mixed_ba,
    uint4* __restrict__ output) {
  constexpr int kElemsPerVector = sizeof(uint4) / sizeof(nv_bfloat16);
  constexpr int kInputVectors = kQkvzWidth / kElemsPerVector;
  constexpr int kQkvVectors = kQkvWidth / kElemsPerVector;
  constexpr int kZVectors = kZWidth / kElemsPerVector;
  constexpr int kBaVectors = (2 * kValueHeads) / kElemsPerVector;
  constexpr int kHeadVectors = kValueHeads / kElemsPerVector;

  const int index = static_cast<int>(blockIdx.x) * Threads + threadIdx.x;
  const bool has_ba = index < kTokens * kBaVectors;
  uint4 ba_value;
  if (has_ba) {
    // Issue the independent side-vector read before the main QKVZ value is
    // consumed, overlapping both arrivals in the two CTAs that carry B/A.
    ba_value = mixed_ba[index];
  }

  const int token = index / kInputVectors;
  const int local_vector = index - token * kInputVectors;
  const uint4 value = mixed_qkvz[index];
  if (local_vector < kQkvVectors) {
    output[token * kQkvVectors + local_vector] = value;
  } else {
    output[kTokens * kQkvVectors + token * kZVectors +
           local_vector - kQkvVectors] = value;
  }

  if (has_ba) {
    const int ba_token = index / kBaVectors;
    const int ba_local = index - ba_token * kBaVectors;
    const int region = ba_local / kHeadVectors;
    const int vector_in_region = ba_local - region * kHeadVectors;
    const int output_base = kTokens * (kQkvVectors + kZVectors);
    output[output_base + region * (kTokens * kHeadVectors) +
           ba_token * kHeadVectors + vector_in_region] = ba_value;
  }
}

template <int Threads>
void launch_qkvzba_copy(
    const torch::Tensor& mixed_qkvz,
    const torch::Tensor& mixed_ba,
    const torch::Tensor& output) {
  TORCH_CHECK(mixed_qkvz.is_cuda() && mixed_ba.is_cuda() && output.is_cuda(),
              "split tensors must be CUDA tensors");
  TORCH_CHECK(mixed_qkvz.scalar_type() == at::kBFloat16 &&
                  mixed_ba.scalar_type() == at::kBFloat16 &&
                  output.scalar_type() == at::kBFloat16,
              "split tensors must be BF16");
  TORCH_CHECK(mixed_qkvz.is_contiguous() && mixed_ba.is_contiguous() &&
                  output.is_contiguous(),
              "split tensors must be contiguous");

  constexpr int kElemsPerVector = sizeof(uint4) / sizeof(nv_bfloat16);
  constexpr int kBlocksPerToken =
      (kQkvWidth + kZWidth) / kElemsPerVector / Threads;
  c10::cuda::CUDAGuard guard(mixed_qkvz.device());
  auto stream = at::cuda::getCurrentCUDAStream(mixed_qkvz.get_device());
  qkvzba_copy_kernel<Threads><<<dim3(kBlocksPerToken, kTokens), Threads, 0, stream>>>(
      reinterpret_cast<const uint4*>(mixed_qkvz.data_ptr()),
      reinterpret_cast<const uint4*>(mixed_ba.data_ptr()),
      reinterpret_cast<uint4*>(output.data_ptr()));
  C10_CUDA_KERNEL_LAUNCH_CHECK();
}

template <int Threads>
void launch_qkvzba_copy_flat(
    const torch::Tensor& mixed_qkvz,
    const torch::Tensor& mixed_ba,
    const torch::Tensor& output) {
  TORCH_CHECK(mixed_qkvz.is_cuda() && mixed_ba.is_cuda() && output.is_cuda(),
              "split tensors must be CUDA tensors");
  TORCH_CHECK(mixed_qkvz.scalar_type() == at::kBFloat16 &&
                  mixed_ba.scalar_type() == at::kBFloat16 &&
                  output.scalar_type() == at::kBFloat16,
              "split tensors must be BF16");
  TORCH_CHECK(mixed_qkvz.is_contiguous() && mixed_ba.is_contiguous() &&
                  output.is_contiguous(),
              "split tensors must be contiguous");

  constexpr int kElemsPerVector = sizeof(uint4) / sizeof(nv_bfloat16);
  constexpr int kTotalVectors = kTokens * kQkvzWidth / kElemsPerVector;
  static_assert(kTotalVectors % Threads == 0);
  c10::cuda::CUDAGuard guard(mixed_qkvz.device());
  auto stream = at::cuda::getCurrentCUDAStream(mixed_qkvz.get_device());
  qkvzba_copy_flat_kernel<Threads><<<kTotalVectors / Threads, Threads, 0, stream>>>(
      reinterpret_cast<const uint4*>(mixed_qkvz.data_ptr()),
      reinterpret_cast<const uint4*>(mixed_ba.data_ptr()),
      reinterpret_cast<uint4*>(output.data_ptr()));
  C10_CUDA_KERNEL_LAUNCH_CHECK();
}

}  // namespace

PYBIND11_MODULE(TORCH_EXTENSION_NAME, m) {
  m.def("conv1d_t9_w4_pair_exact", &launch_conv);
  m.def("conv1d_t9_w4_pair_fast", &launch_conv_fast<32>);
  m.def("conv1d_t9_w4_pair_fast_16", &launch_conv_fast<16>);
  m.def("qkvzba_copy_128", &launch_qkvzba_copy<128>);
  m.def("qkvzba_copy_flat_32", &launch_qkvzba_copy_flat<32>);
  m.def("qkvzba_copy_flat_64", &launch_qkvzba_copy_flat<64>);
  m.def("qkvzba_copy_flat_96", &launch_qkvzba_copy_flat<96>);
}
