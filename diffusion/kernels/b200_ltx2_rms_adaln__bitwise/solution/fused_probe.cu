// task10 bounded-attempt probe (DIAGNOSTIC, not part of the production candidate).
//
// To decide whether a fully-fused single kernel (RMS reduction + modulation in
// one pass) can be bit-wise exact, we must first know whether a custom
// single-kernel fp32 RMS reduction reproduces ATen's `normed` bf16 bits. This
// exports `ltx2_rms_normed_probe(x, eps, output)` = the candidate's own
// RMSNorm-only path; bench/probe_fused.py compares its raw uint16 output against
// at::rms_norm. If they are NOT bit-identical, a fully-fused kernel cannot
// guarantee bit-exactness and the staged path (which reuses at::rms_norm) is the
// production choice. See docs/dispatch.md.

#include <ATen/cuda/CUDAContext.h>
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

// One block per row; fp32 thread-strided partial sums of x^2 + shared-memory
// tree reduction; rstd = rsqrt(mean(x^2) + eps); normed = round_bf16(x * rstd).
__global__ void rms_normed_probe_kernel(const __nv_bfloat16* __restrict__ x,
                                        __nv_bfloat16* __restrict__ out,
                                        int D, float eps) {
  extern __shared__ float sdata[];
  const int row = blockIdx.x;
  const long base = static_cast<long>(row) * D;
  float local = 0.0f;
  for (int c = threadIdx.x; c < D; c += blockDim.x) {
    const float v = __bfloat162float(x[base + c]);
    local += v * v;
  }
  sdata[threadIdx.x] = local;
  __syncthreads();
  for (int s = blockDim.x >> 1; s > 0; s >>= 1) {  // blockDim.x is a power of two
    if (threadIdx.x < s) sdata[threadIdx.x] += sdata[threadIdx.x + s];
    __syncthreads();
  }
  const float rstd = rsqrtf(sdata[0] / static_cast<float>(D) + eps);
  for (int c = threadIdx.x; c < D; c += blockDim.x) {
    out[base + c] = __float2bfloat16_rn(__bfloat162float(x[base + c]) * rstd);
  }
}

void ltx2_rms_normed_probe(TensorView x, double eps, TensorView output) {
  if (x.device().device_type != kDLCUDA) probe_fail("x must be CUDA");
  if (x.ndim() != 3) probe_fail("x must be rank-3 [B,S,D]");
  const int64_t B = x.size(0), S = x.size(1), D = x.size(2);
  const auto* xp = reinterpret_cast<const __nv_bfloat16*>(
      static_cast<const char*>(x.data_ptr()) + x.byte_offset());
  auto* op = reinterpret_cast<__nv_bfloat16*>(
      static_cast<char*>(output.data_ptr()) + output.byte_offset());
  const int rows = static_cast<int>(B * S);
  const int threads = 256;  // power of two for the tree reduction
  cudaStream_t stream = at::cuda::getCurrentCUDAStream();
  rms_normed_probe_kernel<<<dim3(rows), threads, threads * sizeof(float), stream>>>(
      xp, op, static_cast<int>(D), static_cast<float>(eps));
}

}  // namespace

TVM_FFI_DLL_EXPORT_TYPED_FUNC(ltx2_rms_normed_probe, ltx2_rms_normed_probe);
