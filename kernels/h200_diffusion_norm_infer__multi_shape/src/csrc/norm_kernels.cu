// Native CUDA normalization kernels for h200_diffusion_norm_infer__multi_shape.
//
// Two specialized, memory-bound forward kernels matching the recovered SGLang
// baseline semantics (pinned commit c47f0e7cd):
//
//   rms_norm_bf16_n128  : RMSNorm, bf16, N=128 fixed. y = x * rsqrt(mean(x^2)+eps) * w.
//                         FP32 accumulation; rsqrtf (approx, matches Triton tl.math.rsqrt
//                         + bf16 output). 16 lanes/row, 2 rows/warp, vectorized 128-bit
//                         (uint4 = 8 bf16) loads/stores, half-warp shuffle reduction.
//
//   layer_norm_fp32     : LayerNorm, fp32, N=5120 fixed. y = (x-mean)*rstd*w + b,
//                         biased variance (/N), rstd = 1/sqrtf(var+eps) (precise, matches
//                         Triton 1/tl.sqrt). One CTA/row, 256 threads, 5 float4/thread,
//                         x retained in registers, mean then sum((x-mean)^2) (no E[x^2]-mean^2).
//
// Compiled WITHOUT --use_fast_math so the fp32 1/sqrtf stays IEEE-precise for the
// strict 1e-5 tolerance. The wrapper routes ONLY the captured production shapes here.

#include <torch/extension.h>
#include <cuda.h>
#include <cuda_runtime.h>
#include <cuda_bf16.h>
#include <c10/cuda/CUDAStream.h>
#include <c10/cuda/CUDAGuard.h>

namespace {

// ---------------------------------------------------------------------------
// RMSNorm bf16, N = 128
// ---------------------------------------------------------------------------
constexpr int RMS_N = 128;
constexpr int RMS_THREADS = 256;             // 8 warps
constexpr int RMS_ROWS_PER_CTA = (RMS_THREADS / 32) * 2;  // 2 rows per warp -> 16

__global__ void rms_norm_bf16_n128_kernel(
    const __nv_bfloat16* __restrict__ X,
    __nv_bfloat16* __restrict__ Y,
    const __nv_bfloat16* __restrict__ W,
    long M,
    float eps) {
  const int warps_per_cta = blockDim.x >> 5;
  const int warp_in_cta = threadIdx.x >> 5;
  const int lane = threadIdx.x & 31;
  const int sub = lane >> 4;        // 0 or 1 -> which of the 2 rows this warp owns
  const int lane16 = lane & 15;     // 0..15 -> which 8-element chunk of the row
  const long total_warps = (long)gridDim.x * warps_per_cta;
  const long global_warp = (long)blockIdx.x * warps_per_cta + warp_in_cta;

  // Preload the 8 weight values for this lane's chunk (reused across all rows).
  const uint4 wv = *reinterpret_cast<const uint4*>(W + lane16 * 8);
  const __nv_bfloat16* wb = reinterpret_cast<const __nv_bfloat16*>(&wv);
  float wf[8];
#pragma unroll
  for (int i = 0; i < 8; ++i) wf[i] = __bfloat162float(wb[i]);

  for (long pair = global_warp; pair * 2 < M; pair += total_warps) {
    const long row = pair * 2 + sub;
    if (row >= M) continue;  // only triggers for odd M (captured M are all even)

    const uint4 xv = *reinterpret_cast<const uint4*>(X + row * RMS_N + lane16 * 8);
    const __nv_bfloat16* xb = reinterpret_cast<const __nv_bfloat16*>(&xv);
    float v[8];
    float ss = 0.f;
#pragma unroll
    for (int i = 0; i < 8; ++i) {
      v[i] = __bfloat162float(xb[i]);
      ss += v[i] * v[i];
    }
    // Reduce within the 16-lane half-warp that owns this row (xor by 8,4,2,1
    // stays inside each contiguous 16-lane group; full warp is active).
#pragma unroll
    for (int off = 8; off > 0; off >>= 1) ss += __shfl_xor_sync(0xffffffffu, ss, off);

    const float rstd = rsqrtf(ss / (float)RMS_N + eps);

    uint4 yv;
    __nv_bfloat16* yb = reinterpret_cast<__nv_bfloat16*>(&yv);
#pragma unroll
    for (int i = 0; i < 8; ++i) yb[i] = __float2bfloat16(v[i] * rstd * wf[i]);
    *reinterpret_cast<uint4*>(Y + row * RMS_N + lane16 * 8) = yv;
  }
}

// ---------------------------------------------------------------------------
// LayerNorm fp32, N = 5120
// ---------------------------------------------------------------------------
constexpr int LN_N = 5120;
constexpr int LN_THREADS = 256;
constexpr int LN_VPT = LN_N / (LN_THREADS * 4);  // float4 chunks per thread = 5

__device__ __forceinline__ double warpReduceSumD(double v) {
#pragma unroll
  for (int o = 16; o > 0; o >>= 1) v += __shfl_down_sync(0xffffffffu, v, o);
  return v;
}

__device__ __forceinline__ double blockReduceSumD(double v, double* smem) {
  const int lane = threadIdx.x & 31;
  const int wid = threadIdx.x >> 5;
  v = warpReduceSumD(v);
  if (lane == 0) smem[wid] = v;
  __syncthreads();
  if (wid == 0) {
    double t = (lane < (blockDim.x >> 5)) ? smem[lane] : 0.0;
    t = warpReduceSumD(t);
    if (lane == 0) smem[0] = t;
  }
  __syncthreads();
  const double total = smem[0];
  __syncthreads();  // allow smem reuse for the next reduction
  return total;
}

// FP64-internal math: mean/variance reductions and the normalize are done in
// double, casting to fp32 only at the final store. This is strictly more
// accurate than the fp32-accumulating Triton baseline, so it meets the strict
// 1e-5 ceiling even on ill-conditioned rows (var->0 => rstd~1/sqrt(eps)).
// Memory traffic is unchanged (load fp32 x/w/b, store fp32 y), so the kernel
// stays memory-bandwidth-bound.
__global__ void layer_norm_fp32_kernel(
    const float* __restrict__ X,
    float* __restrict__ Y,
    const float* __restrict__ W,
    const float* __restrict__ B,
    float eps) {
  __shared__ double smem[32];
  const long row = blockIdx.x;
  const float* xrow = X + row * LN_N;
  float* yrow = Y + row * LN_N;

  // Pass 1: load this thread's float4 chunks into registers; sum in double.
  float4 xr[LN_VPT];
  double local_sum = 0.0;
#pragma unroll
  for (int k = 0; k < LN_VPT; ++k) {
    const int idx4 = k * LN_THREADS + threadIdx.x;  // coalesced float4 index
    xr[k] = reinterpret_cast<const float4*>(xrow)[idx4];
    local_sum += (double)xr[k].x + (double)xr[k].y + (double)xr[k].z + (double)xr[k].w;
  }
  const double mean = blockReduceSumD(local_sum, smem) / (double)LN_N;

  // Pass 2: biased variance in double from retained registers (sum((x-mean)^2)/N).
  double local_ss = 0.0;
#pragma unroll
  for (int k = 0; k < LN_VPT; ++k) {
    const double dx = (double)xr[k].x - mean, dy = (double)xr[k].y - mean,
                 dz = (double)xr[k].z - mean, dw = (double)xr[k].w - mean;
    local_ss += dx * dx + dy * dy + dz * dz + dw * dw;
  }
  const double var = blockReduceSumD(local_ss, smem) / (double)LN_N;
  const double rstd = 1.0 / sqrt(var + (double)eps);  // precise double rsqrt

  // Pass 3: normalize + affine in double; reload w,b (L2-resident) and store fp32.
#pragma unroll
  for (int k = 0; k < LN_VPT; ++k) {
    const int idx4 = k * LN_THREADS + threadIdx.x;
    const float4 wv = reinterpret_cast<const float4*>(W)[idx4];
    const float4 bv = reinterpret_cast<const float4*>(B)[idx4];
    float4 yv;
    yv.x = (float)(((double)xr[k].x - mean) * rstd * (double)wv.x + (double)bv.x);
    yv.y = (float)(((double)xr[k].y - mean) * rstd * (double)wv.y + (double)bv.y);
    yv.z = (float)(((double)xr[k].z - mean) * rstd * (double)wv.z + (double)bv.z);
    yv.w = (float)(((double)xr[k].w - mean) * rstd * (double)wv.w + (double)bv.w);
    reinterpret_cast<float4*>(yrow)[idx4] = yv;
  }
}

}  // namespace

// ---------------------------------------------------------------------------
// Launchers (assume the captured shape; the Python wrapper enforces the gate)
// ---------------------------------------------------------------------------
torch::Tensor rms_norm_bf16_n128(torch::Tensor x, torch::Tensor w, double eps) {
  TORCH_CHECK(x.is_cuda() && w.is_cuda(), "rms_norm_bf16_n128: tensors must be CUDA");
  TORCH_CHECK(x.scalar_type() == at::kBFloat16, "rms_norm_bf16_n128: x must be bf16");
  TORCH_CHECK(x.dim() == 2 && x.size(1) == RMS_N, "rms_norm_bf16_n128: x must be [M,128]");
  TORCH_CHECK(x.is_contiguous() && w.is_contiguous(), "rms_norm_bf16_n128: contiguous required");
  TORCH_CHECK(w.numel() == RMS_N, "rms_norm_bf16_n128: w must be [128]");
  // Make x's device current so the output allocation, stream, and kernel launch all
  // target x's GPU even when called with a different current device (multi-GPU process).
  const c10::cuda::CUDAGuard device_guard(x.device());
  const long M = x.size(0);
  auto y = torch::empty_like(x);
  if (M == 0) return y;

  const int rows_per_cta = RMS_ROWS_PER_CTA;
  long blocks = (M + rows_per_cta - 1) / rows_per_cta;
  const long cap = 132L * 32L;  // grid-stride cap to limit launch/tail on huge-M
  if (blocks > cap) blocks = cap;

  auto stream = at::cuda::getCurrentCUDAStream();
  rms_norm_bf16_n128_kernel<<<(int)blocks, RMS_THREADS, 0, stream>>>(
      reinterpret_cast<const __nv_bfloat16*>(x.data_ptr()),
      reinterpret_cast<__nv_bfloat16*>(y.data_ptr()),
      reinterpret_cast<const __nv_bfloat16*>(w.data_ptr()),
      M, (float)eps);
  return y;
}

torch::Tensor layer_norm_fp32(torch::Tensor x, torch::Tensor weight,
                              torch::Tensor bias, double eps) {
  TORCH_CHECK(x.is_cuda() && weight.is_cuda() && bias.is_cuda(),
              "layer_norm_fp32: tensors must be CUDA");
  TORCH_CHECK(x.scalar_type() == at::kFloat, "layer_norm_fp32: x must be fp32");
  TORCH_CHECK(x.dim() == 2 && x.size(1) == LN_N, "layer_norm_fp32: x must be [M,5120]");
  TORCH_CHECK(x.is_contiguous() && weight.is_contiguous() && bias.is_contiguous(),
              "layer_norm_fp32: contiguous required");
  TORCH_CHECK(weight.numel() == LN_N && bias.numel() == LN_N,
              "layer_norm_fp32: weight/bias must be [5120]");
  // Make x's device current (multi-GPU safety; see rms_norm_bf16_n128).
  const c10::cuda::CUDAGuard device_guard(x.device());
  const long M = x.size(0);
  auto y = torch::empty_like(x);
  if (M == 0) return y;

  auto stream = at::cuda::getCurrentCUDAStream();
  layer_norm_fp32_kernel<<<(int)M, LN_THREADS, 0, stream>>>(
      x.data_ptr<float>(), y.data_ptr<float>(),
      weight.data_ptr<float>(), bias.data_ptr<float>(), (float)eps);
  return y;
}

PYBIND11_MODULE(TORCH_EXTENSION_NAME, m) {
  m.def("rms_norm_bf16_n128", &rms_norm_bf16_n128, "RMSNorm bf16 N=128 (H200)");
  m.def("layer_norm_fp32", &layer_norm_fp32, "LayerNorm fp32 N=5120 (H200)");
}
