// Fused GroupNorm + SiLU candidate kernel for NVIDIA B200 (sm_100).
//
// Semantics (matches the copied upstream Triton baseline):
//   y = silu(group_norm(x, num_groups, weight, bias, eps))
//   mean/var per (batch, group) over (C/G) * prod(spatial) elements, computed
//   in fp32 with var = E[x^2] - E[x]^2 (clamped >= 0); per-channel affine;
//   silu(t) = t * sigmoid(t). Output is written CONTIGUOUS (NC...) regardless
//   of input layout — identical to the baseline, which materializes
//   x.contiguous() and returns a contiguous tensor.
//
// Inputs may be contiguous or arbitrarily strided (the production set contains
// channels-last-3d rows); strided inputs are read natively — the candidate
// never materializes a contiguous copy of x.
//
// ABI (standalone contract): tvm::ffi::TensorView args, scalars, output last,
// launched on PyTorch's current CUDA stream.

#include <ATen/cuda/CUDAContext.h>
#include <c10/cuda/CUDAException.h>
#include <cuda_bf16.h>
#include <cuda_fp16.h>
#include <tvm/ffi/container/tensor.h>
#include <tvm/ffi/error.h>
#include <tvm/ffi/function.h>

#include <cstdint>

namespace {

constexpr int kBlockThreads = 256;
constexpr int kMaxDims = 5;

struct StridedLayout {
  // Sizes/strides (in elements) of x for the dims after slicing one batch and
  // one group: the group spans channels [g*cpg, (g+1)*cpg) and all spatial
  // positions. We fold that as a virtual shape [cpg, s0, s1, ...] with the
  // matching input strides; linear index i in [0, group_size) decomposes as
  // i = ((c * s0_size + p0) * s1_size + p1) ...
  int64_t sizes[kMaxDims];    // [cpg, spatial dims...]
  int64_t strides[kMaxDims];  // input strides for those dims
  int ndim;                   // number of valid entries (>= 1)
  int64_t batch_stride;       // input stride of the batch dim
  int64_t channel_stride;     // input stride of the channel dim
};

template <typename T>
__device__ __forceinline__ float to_float(T v);
template <>
__device__ __forceinline__ float to_float<__half>(__half v) {
  return __half2float(v);
}
template <>
__device__ __forceinline__ float to_float<__nv_bfloat16>(__nv_bfloat16 v) {
  return __bfloat162float(v);
}
template <>
__device__ __forceinline__ float to_float<float>(float v) {
  return v;
}

template <typename T>
__device__ __forceinline__ T from_float(float v);
template <>
__device__ __forceinline__ __half from_float<__half>(float v) {
  return __float2half(v);
}
template <>
__device__ __forceinline__ __nv_bfloat16 from_float<__nv_bfloat16>(float v) {
  return __float2bfloat16(v);
}
template <>
__device__ __forceinline__ float from_float<float>(float v) {
  return v;
}

// Map a group-linear index to the strided input offset (relative to the start
// of this (batch, group) slice) using the folded sizes/strides.
__device__ __forceinline__ int64_t strided_offset(
    int64_t idx, const StridedLayout& lay) {
  int64_t off = 0;
  int64_t rem = idx;
#pragma unroll
  for (int d = kMaxDims - 1; d >= 1; --d) {
    if (d < lay.ndim) {
      int64_t sz = lay.sizes[d];
      int64_t q = rem / sz;
      int64_t r = rem - q * sz;
      off += r * lay.strides[d];
      rem = q;
    }
  }
  off += rem * lay.strides[0];  // channel-within-group dim
  return off;
}

__device__ __forceinline__ float block_reduce_sum(float v, float* smem_slot) {
  // Warp tree-reduce, then cross-warp via shared memory. blockDim.x is a
  // multiple of 32 (kBlockThreads = 256), so full masks are safe.
  for (int offset = 16; offset > 0; offset >>= 1) {
    v += __shfl_down_sync(0xffffffffu, v, offset);
  }
  const int lane = threadIdx.x & 31;
  const int warp = threadIdx.x >> 5;
  if (lane == 0) smem_slot[warp] = v;
  __syncthreads();
  const int num_warps = blockDim.x >> 5;
  v = (threadIdx.x < num_warps) ? smem_slot[threadIdx.x] : 0.0f;
  if (warp == 0) {
    for (int offset = 16; offset > 0; offset >>= 1) {
      v += __shfl_down_sync(0xffffffffu, v, offset);
    }
  }
  return v;  // valid in thread 0
}

// silu in fp32: t * sigmoid(t). Use the numerically plain form; no fast-math
// flags are passed at compile time (contract).
__device__ __forceinline__ float silu(float t) {
  return t / (1.0f + expf(-t));
}

// Generic two-pass kernel: one CTA per (batch, group). Reads x through the
// strided layout, accumulates fp32 sum/sumsq, then normalizes + affine + silu
// and writes the contiguous output. Correct for every supported shape/layout;
// the optimized regime kernels (added by the tuning rounds) take over where
// they win.

template <typename T>
__global__ void gns_generic_two_pass_kernel(
    const T* __restrict__ x,
    const T* __restrict__ weight,
    const T* __restrict__ bias,
    T* __restrict__ out,
    StridedLayout lay,
    int64_t num_groups,
    int64_t channels_per_group,
    int64_t spatial,
    int64_t group_size,
    float eps) {
  const int64_t group = blockIdx.x % num_groups;
  const int64_t batch = blockIdx.x / num_groups;
  const T* xg =
      x + batch * lay.batch_stride + group * channels_per_group * lay.channel_stride;
  T* og = out + (batch * num_groups + group) * group_size;

  __shared__ float smem[2 * (kBlockThreads / 32) + 2];
  float* warp_sums = smem;
  float* warp_sqs = smem + (kBlockThreads / 32);
  float* stats = smem + 2 * (kBlockThreads / 32);

  float sum = 0.0f, sumsq = 0.0f;
  for (int64_t i = threadIdx.x; i < group_size; i += blockDim.x) {
    const float v = to_float<T>(xg[strided_offset(i, lay)]);
    sum += v;
    sumsq += v * v;
  }
  const float total = block_reduce_sum(sum, warp_sums);
  __syncthreads();
  const float total_sq = block_reduce_sum(sumsq, warp_sqs);
  if (threadIdx.x == 0) {
    const float inv = 1.0f / static_cast<float>(group_size);
    const float mean = total * inv;
    float var = total_sq * inv - mean * mean;
    var = var < 0.0f ? 0.0f : var;
    stats[0] = mean;
    stats[1] = rsqrtf(var + eps);
  }
  __syncthreads();
  const float mean = stats[0];
  const float rstd = stats[1];

  const int64_t weight_base = group * channels_per_group;
  for (int64_t i = threadIdx.x; i < group_size; i += blockDim.x) {
    const float v = to_float<T>(xg[strided_offset(i, lay)]);
    const int64_t ch = i / spatial;
    const float w = to_float<T>(weight[weight_base + ch]);
    const float b = to_float<T>(bias[weight_base + ch]);
    og[i] = from_float<T>(silu((v - mean) * rstd * w + b));
  }
}

void check(bool cond, const char* msg) {
  if (!cond) {
    TVM_FFI_THROW(RuntimeError) << msg;
  }
}

template <typename T>
void launch_generic(
    const tvm::ffi::TensorView& x,
    const tvm::ffi::TensorView& weight,
    const tvm::ffi::TensorView& bias,
    const tvm::ffi::TensorView& out,
    int64_t num_groups,
    double eps,
    cudaStream_t stream) {
  const int ndim = static_cast<int>(x.ndim());
  const int64_t batch = x.size(0);
  const int64_t channels = x.size(1);
  const int64_t channels_per_group = channels / num_groups;

  int64_t spatial = 1;
  for (int d = 2; d < ndim; ++d) spatial *= x.size(d);
  const int64_t group_size = channels_per_group * spatial;

  StridedLayout lay;
  lay.batch_stride = x.stride(0);
  lay.channel_stride = x.stride(1);
  lay.sizes[0] = channels_per_group;
  lay.strides[0] = x.stride(1);
  lay.ndim = 1;
  for (int d = 2; d < ndim; ++d) {
    lay.sizes[lay.ndim] = x.size(d);
    lay.strides[lay.ndim] = x.stride(d);
    lay.ndim += 1;
  }
  // Unused trailing dims get size 1 / stride 0 so the unrolled decomposition
  // is a no-op for them.
  for (int d = lay.ndim; d < kMaxDims; ++d) {
    lay.sizes[d] = 1;
    lay.strides[d] = 0;
  }

  const dim3 grid(static_cast<unsigned>(batch * num_groups));
  const dim3 block(kBlockThreads);
  gns_generic_two_pass_kernel<T><<<grid, block, 0, stream>>>(
      static_cast<const T*>(x.data_ptr()),
      static_cast<const T*>(weight.data_ptr()),
      static_cast<const T*>(bias.data_ptr()),
      static_cast<T*>(out.data_ptr()),
      lay,
      num_groups,
      channels_per_group,
      spatial,
      group_size,
      static_cast<float>(eps));
  C10_CUDA_KERNEL_LAUNCH_CHECK();
}

void group_norm_silu(
    tvm::ffi::TensorView x,
    tvm::ffi::TensorView weight,
    tvm::ffi::TensorView bias,
    int64_t num_groups,
    double eps,
    tvm::ffi::TensorView out) {
  const int ndim = static_cast<int>(x.ndim());
  check(ndim >= 2 && ndim <= kMaxDims, "x must have 2..5 dims");
  check(num_groups > 0 && x.size(1) % num_groups == 0,
        "channels must divide num_groups");
  check(weight.ndim() == 1 && bias.ndim() == 1, "weight/bias must be 1-D");
  check(weight.size(0) == x.size(1) && bias.size(0) == x.size(1),
        "weight/bias must have C elements");
  check(out.ndim() == ndim, "out must match x rank");
  int64_t numel = 1;
  for (int d = 0; d < ndim; ++d) {
    check(out.size(d) == x.size(d), "out must match x shape");
    numel *= x.size(d);
  }
  // The output is contiguous by contract (mirrors the upstream baseline's
  // contiguous return); verify the strides.
  int64_t expect = 1;
  for (int d = ndim - 1; d >= 0; --d) {
    check(out.stride(d) == expect || out.size(d) == 1, "out must be contiguous");
    expect *= out.size(d);
  }
  check(x.dtype() == weight.dtype() && x.dtype() == bias.dtype() &&
            x.dtype() == out.dtype(),
        "dtype mismatch");
  if (numel == 0) {
    return;  // nothing to do for empty tensors
  }

  cudaStream_t stream = at::cuda::getCurrentCUDAStream();

  const DLDataType dt = x.dtype();
  if (dt.code == kDLFloat && dt.bits == 16) {
    launch_generic<__half>(x, weight, bias, out, num_groups, eps, stream);
  } else if (dt.code == kDLBfloat && dt.bits == 16) {
    launch_generic<__nv_bfloat16>(x, weight, bias, out, num_groups, eps, stream);
  } else if (dt.code == kDLFloat && dt.bits == 32) {
    launch_generic<float>(x, weight, bias, out, num_groups, eps, stream);
  } else {
    TVM_FFI_THROW(RuntimeError) << "unsupported dtype (fp16/bf16/fp32 only)";
  }
}

}  // namespace

TVM_FFI_DLL_EXPORT_TYPED_FUNC(group_norm_silu, group_norm_silu);
