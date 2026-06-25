// Candidate CUDA implementation of the fused 5D causal-Conv3D cat/pad copy.
//
// Memory-bandwidth-bound pure copy (no arithmetic). Optimized flat-chunk design:
//   * Flat-chunk mapping: each thread owns VEC consecutive output elements
//     (VEC = 16/sizeof(elem) => 8 bf16 / 4 fp32 = a 16-byte vector). The output
//     tensor base is 16-byte aligned and chunks are 16-byte aligned off it, so
//     each thread issues ONE 128-bit coalesced store — saturating B200 HBM far
//     better than per-element stores.
//   * The expensive flat-index decomposition is done ONCE per chunk; within the
//     chunk `ow` is incremented with O(1) row-boundary handling (recomputing the
//     source-row base only when crossing a row), amortizing the index math.
//   * Each of the VEC lanes is copy-or-zero: interior reads come from the cat of
//     cache+x (cache fills the innermost left-depth planes); spatial/temporal
//     borders are constant zero. Source reads use __ldg (scalar, read-only) so the
//     W_l shift cannot trigger a misaligned wide load.
//   * A stride-aware generic fallback handles non-contiguous x/cache (reads via
//     TensorView strides) and any shape the vector path cannot cleanly cover; the
//     contiguous output is always required.
//
// ABI: destination-passing, output last, current CUDA stream. Exported via
// tvm-ffi as `causal_conv3d_cat_pad_candidate`.

#include <ATen/cuda/CUDAContext.h>
#include <c10/cuda/CUDAGuard.h>

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

constexpr int kFlatBlock = 256;

// Flat-chunk vectorized copy. ET = element uint type; VEC = elements per 16-byte
// vector. Each thread writes one 128-bit store covering VEC consecutive output
// positions, computing copy-or-zero per lane with amortized index math.
template <typename ET, int VEC>
__global__ void __launch_bounds__(kFlatBlock) cat_pad_flat_kernel(
    const ET* __restrict__ x, const ET* __restrict__ cache, ET* __restrict__ out,
    long total_vecs, long channels, long t_size, long h_size, long w_size, long cache_t,
    long out_t, long out_h, long out_w, long pad_d_left, long pad_h_top, long pad_w_left) {
  union Pack {
    ET e[VEC];
    uint4 raw;
  };
  const long nthreads = (long)gridDim.x * blockDim.x;
  for (long vid = (long)blockIdx.x * blockDim.x + threadIdx.x; vid < total_vecs;
       vid += nthreads) {
    long base = vid * VEC;
    long ow = base % out_w;
    long tmp = base / out_w;
    long oh = tmp % out_h;
    tmp /= out_h;
    long od = tmp % out_t;
    tmp /= out_t;
    long oc = tmp % channels;
    long ob = tmp / channels;

    long ih = oh - pad_h_top;
    long src_t = od - pad_d_left;
    int interior = (ih >= 0 && ih < h_size && src_t >= 0 && src_t < cache_t + t_size);
    const ET* src = nullptr;
    if (interior) {
      if (src_t < cache_t) {
        src = cache + (((ob * channels + oc) * cache_t + src_t) * h_size + ih) * w_size;
      } else {
        src = x + (((ob * channels + oc) * t_size + (src_t - cache_t)) * h_size + ih) * w_size;
      }
    }

    Pack pk;
#pragma unroll
    for (int k = 0; k < VEC; ++k) {
      ET v = ET(0);
      if (interior) {
        long iw = ow - pad_w_left;
        if (iw >= 0 && iw < w_size) v = __ldg(src + iw);
      }
      pk.e[k] = v;
      // advance to the next output column, handling row/plane wrap O(1)
      if (++ow == out_w) {
        ow = 0;
        if (++oh == out_h) {
          oh = 0;
          if (++od == out_t) {
            od = 0;
            if (++oc == channels) {
              oc = 0;
              ++ob;
            }
          }
        }
        ih = oh - pad_h_top;
        src_t = od - pad_d_left;
        interior = (ih >= 0 && ih < h_size && src_t >= 0 && src_t < cache_t + t_size);
        if (interior) {
          if (src_t < cache_t) {
            src = cache + (((ob * channels + oc) * cache_t + src_t) * h_size + ih) * w_size;
          } else {
            src = x + (((ob * channels + oc) * t_size + (src_t - cache_t)) * h_size + ih) * w_size;
          }
        } else {
          src = nullptr;
        }
      }
    }
    reinterpret_cast<uint4*>(out)[vid] = pk.raw;
  }
}

// Stride-aware generic fallback for non-contiguous x/cache (or shapes the vector
// path cannot cleanly cover). One thread per output element; reads via element
// strides. Output must be contiguous.
template <typename ET>
__global__ void cat_pad_strided_kernel(
    const ET* __restrict__ x, long xs0, long xs1, long xs2, long xs3, long xs4,
    const ET* __restrict__ cache, long cs0, long cs1, long cs2, long cs3, long cs4,
    ET* __restrict__ out, long total, long channels, long t_size, long h_size, long w_size,
    long cache_t, long out_t, long out_h, long out_w, long pad_d_left, long pad_h_top,
    long pad_w_left) {
  long idx = (long)blockIdx.x * blockDim.x + threadIdx.x;
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
      val = cache[ob * cs0 + oc * cs1 + src_t * cs2 + ih * cs3 + iw * cs4];
    } else {
      long xt = src_t - cache_t;
      val = x[ob * xs0 + oc * xs1 + xt * xs2 + ih * xs3 + iw * xs4];
    }
  }
  out[idx] = val;
}

template <typename ET, int VEC>
void launch_flat(const char* x_p, const char* c_p, char* out_p, long total, long channels,
                 long t_size, long h_size, long w_size, long cache_t, long out_t, long out_h,
                 long out_w, long depth_left, long pad_h_top, long pad_w_left,
                 cudaStream_t stream) {
  const long total_vecs = total / VEC;
  long grid = (total_vecs + kFlatBlock - 1) / kFlatBlock;
  if (grid < 1) grid = 1;
  cat_pad_flat_kernel<ET, VEC><<<(unsigned)grid, kFlatBlock, 0, stream>>>(
      reinterpret_cast<const ET*>(x_p), reinterpret_cast<const ET*>(c_p),
      reinterpret_cast<ET*>(out_p), total_vecs, channels, t_size, h_size, w_size, cache_t, out_t,
      out_h, out_w, depth_left, pad_h_top, pad_w_left);
}

template <typename ET>
void launch_strided(const TensorView& x, const TensorView& cache, const char* x_p, const char* c_p,
                    char* out_p, long total, long channels, long t_size, long h_size, long w_size,
                    long cache_t, long out_t, long out_h, long out_w, long depth_left,
                    long pad_h_top, long pad_w_left, cudaStream_t stream) {
  const int block = 256;
  const long grid = (total + block - 1) / block;
  cat_pad_strided_kernel<ET><<<(unsigned)grid, block, 0, stream>>>(
      reinterpret_cast<const ET*>(x_p), x.stride(0), x.stride(1), x.stride(2), x.stride(3),
      x.stride(4), reinterpret_cast<const ET*>(c_p), cache.stride(0), cache.stride(1),
      cache.stride(2), cache.stride(3), cache.stride(4), reinterpret_cast<ET*>(out_p), total,
      channels, t_size, h_size, w_size, cache_t, out_t, out_h, out_w, depth_left, pad_h_top,
      pad_w_left);
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
  CAND_CHECK(cache.size(0) == bsz && cache.size(1) == channels && cache.size(3) == h_size &&
                 cache.size(4) == w_size,
             "cache must share N,C,H,W with x");

  const long depth_left = pad_d_left - cache_t;  // already-decremented left zero planes
  CAND_CHECK(depth_left >= 0, "depth_left must be >= cache_t (pad_d_left=", pad_d_left,
             ", cache_t=", cache_t, ")");
  CAND_CHECK(pad_d_right == 0, "depth_right must be 0");
  CAND_CHECK(pad_w_left == pad_w_right, "width padding must be symmetric");
  CAND_CHECK(pad_h_top == pad_h_bottom, "height padding must be symmetric");

  const long out_t = t_size + cache_t + depth_left + pad_d_right;
  const long out_h = h_size + pad_h_top + pad_h_bottom;
  const long out_w = w_size + pad_w_left + pad_w_right;
  CAND_CHECK(output.size(0) == bsz && output.size(1) == channels && output.size(2) == out_t &&
                 output.size(3) == out_h && output.size(4) == out_w,
             "output shape mismatch");
  CAND_CHECK(tensor_is_contiguous(output), "output must be C-contiguous");

  const long total = bsz * channels * out_t * out_h * out_w;
  if (total == 0) return;

  const int ebits = x.dtype().bits;
  CAND_CHECK(ebits == 16 || ebits == 32, "unsupported element bit width: ", ebits);

  char* out_p = static_cast<char*>(output.data_ptr()) + output.byte_offset();
  const char* x_p = static_cast<const char*>(x.data_ptr()) + x.byte_offset();
  const char* c_p = static_cast<const char*>(cache.data_ptr()) + cache.byte_offset();

  // Match the baseline wrapper's device context: require cache/output on the same
  // CUDA device as x, and guard the current device to x's device so a multi-GPU
  // caller launches on the right device/stream (no-op for the single-device path).
  const int x_dev = x.device().device_id;
  CAND_CHECK(cache.device().device_id == x_dev, "cache must be on the same CUDA device as x");
  CAND_CHECK(output.device().device_id == x_dev, "output must be on the same CUDA device as x");
  const c10::cuda::CUDAGuard device_guard{static_cast<c10::DeviceIndex>(x_dev)};
  cudaStream_t stream = at::cuda::getCurrentCUDAStream();

  const bool x_contig = tensor_is_contiguous(x);
  const bool cache_contig = (cache_t == 0) || tensor_is_contiguous(cache);
  const int vec = 16 / (ebits / 8);  // 8 for bf16/fp16, 4 for fp32
  const bool out16 = (reinterpret_cast<uintptr_t>(out_p) % 16) == 0;
  const bool vec_ok = x_contig && cache_contig && out16 && (total % vec == 0);

  if (vec_ok) {
    // Fast path: flat 16-byte vectorized copy.
    if (ebits == 16) {
      launch_flat<uint16_t, 8>(x_p, c_p, out_p, total, channels, t_size, h_size, w_size, cache_t,
                               out_t, out_h, out_w, depth_left, pad_h_top, pad_w_left, stream);
    } else {
      launch_flat<uint32_t, 4>(x_p, c_p, out_p, total, channels, t_size, h_size, w_size, cache_t,
                               out_t, out_h, out_w, depth_left, pad_h_top, pad_w_left, stream);
    }
  } else {
    // Generic stride-aware fallback (non-contiguous, or shape the vector path
    // cannot cleanly cover). Correct for contiguous inputs too.
    if (ebits == 16) {
      launch_strided<uint16_t>(x, cache, x_p, c_p, out_p, total, channels, t_size, h_size, w_size,
                               cache_t, out_t, out_h, out_w, depth_left, pad_h_top, pad_w_left,
                               stream);
    } else {
      launch_strided<uint32_t>(x, cache, x_p, c_p, out_p, total, channels, t_size, h_size, w_size,
                               cache_t, out_t, out_h, out_w, depth_left, pad_h_top, pad_w_left,
                               stream);
    }
  }
}

}  // namespace

TVM_FFI_DLL_EXPORT_TYPED_FUNC(causal_conv3d_cat_pad_candidate, causal_conv3d_cat_pad_candidate);
