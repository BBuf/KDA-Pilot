// Candidate CUDA implementation of the fused 5D causal-Conv3D cat/pad copy.
//
// This is the initial correctness-first candidate: a faithful transliteration of
// the upstream Triton kernel `_fused_cat_pad_5d_kernel` (one thread per output
// element, masked reads, constant-zero borders). It assumes C-contiguous x and
// cache (the upstream kernel does the same via hardcoded stride formulas) and is
// dtype-agnostic by element size (2-byte bf16/fp16, 4-byte fp32) since the op is
// a pure copy + zero-fill. Vectorized/specialized fast paths come in a later
// optimization stage; this version exists to lock down exact correctness.
//
// ABI: destination-passing, output tensor passed last, launched on PyTorch's
// current CUDA stream. Exported via tvm-ffi as `causal_conv3d_cat_pad_candidate`.

#include <ATen/cuda/CUDAContext.h>

#include <cuda_bf16.h>
#include <cuda_fp16.h>

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
[[noreturn]] void cand_fail(Args&&... args) {
  std::ostringstream oss;
  (oss << ... << args);
  throw std::runtime_error(oss.str());
}

#define CAND_CHECK(cond, ...) \
  do {                        \
    if (!(cond)) {            \
      cand_fail(__VA_ARGS__); \
    }                         \
  } while (0)

inline bool same_dtype(DLDataType a, DLDataType b) {
  return a.code == b.code && a.bits == b.bits && a.lanes == b.lanes;
}

inline void check_cuda_tensor(const TensorView& t, const char* name) {
  CAND_CHECK(t.device().device_type == kDLCUDA, name, " must be a CUDA tensor");
}

inline bool tensor_is_contiguous(const TensorView& t) {
  int64_t expect = 1;
  for (int i = t.ndim() - 1; i >= 0; --i) {
    if (t.size(i) == 1) continue;  // stride is free on size-1 dims
    if (t.stride(i) != expect) return false;
    expect *= t.size(i);
  }
  return true;
}

// One output element per thread. ET is an unsigned integer of the element's byte
// width; the value is copied bit-for-bit (no numeric conversion) and borders are
// written as all-zero bits (== 0.0 for bf16/fp16/fp32). Reads happen only for
// in-range source positions, so no clamped/invalid addresses are dereferenced.
template <typename ET>
__global__ void cat_pad_copy_kernel(
    const ET* __restrict__ x_ptr, const ET* __restrict__ cache_ptr,
    ET* __restrict__ out_ptr, long total, long channels, long t_size, long h_size,
    long w_size, long cache_t, long out_t, long out_h, long out_w, long pad_d_left,
    long pad_h_top, long pad_w_left) {
  long idx = static_cast<long>(blockIdx.x) * blockDim.x + threadIdx.x;
  if (idx >= total) return;

  long ow = idx % out_w;
  long tmp = idx / out_w;
  long oh = tmp % out_h;
  tmp /= out_h;
  long od = tmp % out_t;
  tmp /= out_t;
  long oc = tmp % channels;
  long ob = tmp / channels;

  long iw = ow - pad_w_left;
  long ih = oh - pad_h_top;
  long src_t = od - pad_d_left;

  ET val = ET(0);
  if (iw >= 0 && iw < w_size && ih >= 0 && ih < h_size && src_t >= 0 &&
      src_t < cache_t + t_size) {
    if (src_t < cache_t) {
      long off = (((ob * channels + oc) * cache_t + src_t) * h_size + ih) * w_size + iw;
      val = cache_ptr[off];
    } else {
      long xt = src_t - cache_t;
      long off = (((ob * channels + oc) * t_size + xt) * h_size + ih) * w_size + iw;
      val = x_ptr[off];
    }
  }
  out_ptr[idx] = val;
}

void causal_conv3d_cat_pad_candidate(
    TensorView x, TensorView cache, int64_t pad_w_left, int64_t pad_w_right,
    int64_t pad_h_top, int64_t pad_h_bottom, int64_t pad_d_left, int64_t pad_d_right,
    TensorView output) {
  check_cuda_tensor(x, "x");
  check_cuda_tensor(cache, "cache");
  check_cuda_tensor(output, "output");
  CAND_CHECK(x.ndim() == 5, "x must be 5D [N,C,T,H,W]");
  CAND_CHECK(cache.ndim() == 5, "cache must be 5D [N,C,cache_t,H,W]");
  CAND_CHECK(output.ndim() == 5, "output must be 5D");
  CAND_CHECK(same_dtype(x.dtype(), cache.dtype()), "x and cache dtype must match");
  CAND_CHECK(same_dtype(x.dtype(), output.dtype()), "x and output dtype must match");

  const long bsz = x.size(0);
  const long channels = x.size(1);
  const long t_size = x.size(2);
  const long h_size = x.size(3);
  const long w_size = x.size(4);
  const long cache_t = cache.size(2);

  CAND_CHECK(cache.size(0) == bsz && cache.size(1) == channels &&
                 cache.size(3) == h_size && cache.size(4) == w_size,
             "cache must share N,C,H,W with x");

  // Mirror the upstream wrapper's validation exactly.
  const long depth_left = pad_d_left - cache_t;  // already-decremented left zero planes
  CAND_CHECK(depth_left >= 0, "depth_left must be >= cache_t (pad_d_left=", pad_d_left,
             ", cache_t=", cache_t, ")");
  CAND_CHECK(pad_d_right == 0, "depth_right must be 0");
  CAND_CHECK(pad_w_left == pad_w_right, "width padding must be symmetric");
  CAND_CHECK(pad_h_top == pad_h_bottom, "height padding must be symmetric");

  const long out_t = t_size + cache_t + depth_left + pad_d_right;
  const long out_h = h_size + pad_h_top + pad_h_bottom;
  const long out_w = w_size + pad_w_left + pad_w_right;
  CAND_CHECK(output.size(0) == bsz && output.size(1) == channels &&
                 output.size(2) == out_t && output.size(3) == out_h &&
                 output.size(4) == out_w,
             "output shape mismatch");

  // The upstream kernel uses hardcoded C-contiguous stride formulas; require the
  // same layout so the A/B comparison is exact and no strided input is mis-read.
  CAND_CHECK(tensor_is_contiguous(x), "x must be C-contiguous");
  CAND_CHECK(tensor_is_contiguous(cache) || cache_t == 0, "cache must be C-contiguous");
  CAND_CHECK(tensor_is_contiguous(output), "output must be C-contiguous");

  const long total = bsz * channels * out_t * out_h * out_w;
  if (total == 0) return;

  const int block = 256;
  const long grid = (total + block - 1) / block;
  cudaStream_t stream = at::cuda::getCurrentCUDAStream();

  const int ebits = x.dtype().bits;
  void* out_p = static_cast<char*>(output.data_ptr()) + output.byte_offset();
  const void* x_p = static_cast<const char*>(x.data_ptr()) + x.byte_offset();
  const void* c_p = static_cast<const char*>(cache.data_ptr()) + cache.byte_offset();

  if (ebits == 16) {
    cat_pad_copy_kernel<uint16_t><<<grid, block, 0, stream>>>(
        reinterpret_cast<const uint16_t*>(x_p), reinterpret_cast<const uint16_t*>(c_p),
        reinterpret_cast<uint16_t*>(out_p), total, channels, t_size, h_size, w_size,
        cache_t, out_t, out_h, out_w, depth_left, pad_h_top, pad_w_left);
  } else if (ebits == 32) {
    cat_pad_copy_kernel<uint32_t><<<grid, block, 0, stream>>>(
        reinterpret_cast<const uint32_t*>(x_p), reinterpret_cast<const uint32_t*>(c_p),
        reinterpret_cast<uint32_t*>(out_p), total, channels, t_size, h_size, w_size,
        cache_t, out_t, out_h, out_w, depth_left, pad_h_top, pad_w_left);
  } else {
    cand_fail("unsupported element bit width: ", ebits);
  }
}

}  // namespace

TVM_FFI_DLL_EXPORT_TYPED_FUNC(causal_conv3d_cat_pad_candidate, causal_conv3d_cat_pad_candidate);
