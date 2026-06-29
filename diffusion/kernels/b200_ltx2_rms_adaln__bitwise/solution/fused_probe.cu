// Fully-fused feasibility probe for b200_ltx2_rms_adaln__bitwise.
//
// Question: can a custom single-kernel fp32 RMS reduction reproduce
// at::rms_norm's bf16 `normed` BIT-FOR-BIT? If it cannot on any required row,
// then a fully-fused single kernel (reduction + modulation in one pass) cannot be
// bit-exact, so the staged candidate (which reuses at::rms_norm) is the
// production path. bench/probe_fused.py builds this and compares the raw uint16
// output against torch.nn.functional.rms_norm.
//
//   ltx2_rms_normed_probe(x, eps, output): output = custom_rms_norm(x)  (bf16)
//
// This implements a standard one-block-per-row fp32 sum-of-squares reduction
// (shared-memory tree). The point of the probe is exactly to measure whether
// this reduction's order/rounding matches ATen's; it is NOT expected to be a
// drop-in replacement unless the probe proves bit-equality everywhere. No
// --use_fast_math. No sglang import.

#include <ATen/ATen.h>
#include <ATen/cuda/CUDAContext.h>
#include <c10/cuda/CUDAGuard.h>

#include <cuda_bf16.h>
#include <dlpack/dlpack.h>
#include <tvm/ffi/container/tensor.h>
#if __has_include(<tvm/ffi/function.h>)
#include <tvm/ffi/function.h>
#endif

#include <cstdint>
#include <sstream>
#include <stdexcept>

namespace {

using tvm::ffi::TensorView;

template <typename... Args>
[[noreturn]] void probe_fail(Args&&... args) {
  std::ostringstream oss;
  (oss << ... << args);
  throw std::runtime_error(oss.str());
}

#define PROBE_CHECK(cond, ...) \
  do {                         \
    if (!(cond)) {             \
      probe_fail(__VA_ARGS__); \
    }                          \
  } while (0)

inline bool dtype_is(DLDataType d, uint8_t code, uint8_t bits) {
  return d.code == code && d.bits == bits && d.lanes == 1;
}

inline bool is_bf16(const TensorView& t) { return dtype_is(t.dtype(), kDLBfloat, 16); }

inline bool is_compact(const TensorView& t) {
  int64_t expect = 1;
  for (int i = t.ndim() - 1; i >= 0; --i) {
    if (t.size(i) == 1) continue;
    if (t.stride(i) != expect) return false;
    expect *= t.size(i);
  }
  return true;
}

inline int64_t numel(const TensorView& t) {
  int64_t n = 1;
  for (int i = 0; i < t.ndim(); ++i) n *= t.size(i);
  return n;
}

// One block per row. Block-reduce the fp32 sum of squares over D, then write the
// normalized bf16 row (RNE store). BLOCK must be a power of two.
template <int BLOCK>
__global__ void rms_normed_kernel(const __nv_bfloat16* __restrict__ x,
                                  __nv_bfloat16* __restrict__ out,
                                  int64_t D, float eps) {
  const int64_t base = static_cast<int64_t>(blockIdx.x) * D;
  __shared__ float sdata[BLOCK];

  float acc = 0.0f;
  for (int64_t d = threadIdx.x; d < D; d += BLOCK) {
    const float v = __bfloat162float(x[base + d]);
    acc += v * v;
  }
  sdata[threadIdx.x] = acc;
  __syncthreads();

  for (int s = BLOCK >> 1; s > 0; s >>= 1) {
    if (static_cast<int>(threadIdx.x) < s) {
      sdata[threadIdx.x] += sdata[threadIdx.x + s];
    }
    __syncthreads();
  }

  const float mean = sdata[0] / static_cast<float>(D);
  const float inv = rsqrtf(mean + eps);
  for (int64_t d = threadIdx.x; d < D; d += BLOCK) {
    const float v = __bfloat162float(x[base + d]);
    out[base + d] = __float2bfloat16_rn(v * inv);
  }
}

// ltx2_rms_normed_probe(x, eps, output)
//   x:      [..., D] bf16, contiguous
//   eps:    double
//   output: same shape as x, bf16, contiguous (destination)
void ltx2_rms_normed_probe(TensorView x, double eps, TensorView output) {
  PROBE_CHECK(x.device().device_type == kDLCUDA, "x must be CUDA");
  PROBE_CHECK(is_bf16(x), "x must be bfloat16");
  PROBE_CHECK(x.ndim() >= 1, "x must have rank >= 1");
  PROBE_CHECK(is_compact(x), "x must be contiguous");
  const int dev = x.device().device_id;
  PROBE_CHECK(output.device().device_type == kDLCUDA && output.device().device_id == dev,
              "output must be on the same CUDA device as x");
  PROBE_CHECK(is_bf16(output), "output must be bfloat16");
  PROBE_CHECK(is_compact(output), "output must be contiguous");
  PROBE_CHECK(numel(output) == numel(x), "output must have the same number of elements as x");

  const int64_t D = x.size(x.ndim() - 1);
  PROBE_CHECK(D > 0, "last dim must be positive");
  const int64_t N = numel(x) / D;
  if (N == 0) return;

  const c10::cuda::CUDAGuard guard(at::Device(at::kCUDA, dev));
  cudaStream_t stream = at::cuda::getCurrentCUDAStream();

  const auto* x_ptr = reinterpret_cast<const __nv_bfloat16*>(
      static_cast<char*>(x.data_ptr()) + x.byte_offset());
  auto* out_ptr = reinterpret_cast<__nv_bfloat16*>(
      static_cast<char*>(output.data_ptr()) + output.byte_offset());

  constexpr int BLOCK = 256;
  rms_normed_kernel<BLOCK>
      <<<static_cast<unsigned>(N), BLOCK, 0, stream>>>(x_ptr, out_ptr, D,
                                                       static_cast<float>(eps));
}

}  // namespace

TVM_FFI_DLL_EXPORT_TYPED_FUNC(ltx2_rms_normed_probe, ltx2_rms_normed_probe);
