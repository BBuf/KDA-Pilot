// Native CUDA rotary-embedding kernels for NVIDIA B200 (SM100).
//
// Two production fast paths matching the SGLang diffusion baselines exactly:
//   * apply_rotary_embedding  : adjacent-pair rotation, head_dim 128, cos/sin
//     [num_tokens, 64] fp32 token-shared across heads, out-of-place.
//   * apply_ltx2_split_rotary_emb : split-half rotation, half in {32,64}, cos/sin
//     [B, H, S, half] bf16 addressed by (batch, head, token) strides (innermost
//     half contiguous), out-of-place. Replicates the baseline numeric order
//     (the x*cos product is rounded to bf16 before the fp32 sine add).
//
// Both are memory-bandwidth / launch bound, so the design favors coalesced
// 128-bit (int4 = 8 bf16) loads/stores and fp32 accumulation.

#include <torch/extension.h>
#include <ATen/cuda/CUDAContext.h>
#include <c10/cuda/CUDAStream.h>
#include <c10/cuda/CUDAGuard.h>
#include <cuda_bf16.h>

namespace {

constexpr int kStdHeadDim = 128;
constexpr int kStdHalf = 64;  // head_dim / 2
constexpr int kVec = 8;       // bf16 lanes per int4 (128-bit)

// ---------------------------------------------------------------------------
// Standard adjacent-pair RoPE: out[2i]=x1*c-x2*s, out[2i+1]=x1*s+x2*c.
// One CTA per (batch,token) row; cos/sin (token-shared) staged in shared memory
// and reused across all heads; x streamed as 128-bit words.
// ---------------------------------------------------------------------------
__global__ void rope_std_kernel(__nv_bfloat16* __restrict__ out,
                                const __nv_bfloat16* __restrict__ x,
                                const float* __restrict__ cos,
                                const float* __restrict__ sin,
                                int num_heads, int num_tokens) {
  const int bt = blockIdx.x;
  const int token = bt % num_tokens;
  __shared__ float scos[kStdHalf];
  __shared__ float ssin[kStdHalf];
  for (int i = threadIdx.x; i < kStdHalf; i += blockDim.x) {
    scos[i] = cos[(long)token * kStdHalf + i];
    ssin[i] = sin[(long)token * kStdHalf + i];
  }
  __syncthreads();

  const long row_base = (long)bt * num_heads * kStdHeadDim;
  const int words_per_row = num_heads * (kStdHeadDim / kVec);  // num_heads * 16
  const int4* xv = reinterpret_cast<const int4*>(x + row_base);
  int4* ov = reinterpret_cast<int4*>(out + row_base);

  for (int w = threadIdx.x; w < words_per_row; w += blockDim.x) {
    int4 packed = xv[w];
    const __nv_bfloat16* xh = reinterpret_cast<const __nv_bfloat16*>(&packed);
    const int i0 = ((w * kVec) % kStdHeadDim) / 2;  // first pair index in this word
    int4 outp;
    __nv_bfloat16* oh = reinterpret_cast<__nv_bfloat16*>(&outp);
#pragma unroll
    for (int j = 0; j < kVec / 2; ++j) {
      const float x1 = __bfloat162float(xh[2 * j]);
      const float x2 = __bfloat162float(xh[2 * j + 1]);
      const float c = scos[i0 + j];
      const float s = ssin[i0 + j];
      oh[2 * j] = __float2bfloat16(x1 * c - x2 * s);
      oh[2 * j + 1] = __float2bfloat16(x1 * s + x2 * c);
    }
    ov[w] = outp;
  }
}

// ---------------------------------------------------------------------------
// LTX-2 split-half rotary. Pairs (x[j], x[j+half]) within each head.
// One CTA per (batch,token); 128-bit vectorized over j in steps of 8.
// cos/sin addressed via (batch,head,token) strides; innermost half is stride-1.
// Numeric order matches the SGLang baseline: round (x*cos) to bf16, then add the
// sine product in fp32, then store bf16.
// ---------------------------------------------------------------------------
template <int HALF>
__global__ void ltx2_split_kernel(__nv_bfloat16* __restrict__ out,
                                  const __nv_bfloat16* __restrict__ x,
                                  const __nv_bfloat16* __restrict__ cos,
                                  const __nv_bfloat16* __restrict__ sin,
                                  int seq_len, int num_heads,
                                  long sc_b, long sc_h, long sc_t,
                                  long ss_b, long ss_h, long ss_t) {
  constexpr int HEAD_DIM = 2 * HALF;
  constexpr int WORDS_PER_HALF = HALF / kVec;
  const int bt = blockIdx.x;
  const int batch = bt / seq_len;
  const int token = bt - batch * seq_len;
  const long x_row = (long)bt * num_heads * HEAD_DIM;
  const int total_words = num_heads * WORDS_PER_HALF;

  for (int p = threadIdx.x; p < total_words; p += blockDim.x) {
    const int head = p / WORDS_PER_HALF;
    const int j0 = (p - head * WORDS_PER_HALF) * kVec;
    const long xb = x_row + (long)head * HEAD_DIM;
    const long cb = (long)batch * sc_b + (long)head * sc_h + (long)token * sc_t + j0;
    const long sb = (long)batch * ss_b + (long)head * ss_h + (long)token * ss_t + j0;

    int4 xf4 = *reinterpret_cast<const int4*>(x + xb + j0);
    int4 xs4 = *reinterpret_cast<const int4*>(x + xb + HALF + j0);
    int4 c4 = *reinterpret_cast<const int4*>(cos + cb);
    int4 s4 = *reinterpret_cast<const int4*>(sin + sb);
    const __nv_bfloat16* xfh = reinterpret_cast<const __nv_bfloat16*>(&xf4);
    const __nv_bfloat16* xsh = reinterpret_cast<const __nv_bfloat16*>(&xs4);
    const __nv_bfloat16* ch = reinterpret_cast<const __nv_bfloat16*>(&c4);
    const __nv_bfloat16* sh = reinterpret_cast<const __nv_bfloat16*>(&s4);

    int4 of4, os4;
    __nv_bfloat16* ofh = reinterpret_cast<__nv_bfloat16*>(&of4);
    __nv_bfloat16* osh = reinterpret_cast<__nv_bfloat16*>(&os4);
#pragma unroll
    for (int k = 0; k < kVec; ++k) {
      const float xf = __bfloat162float(xfh[k]);
      const float xs = __bfloat162float(xsh[k]);
      const float c = __bfloat162float(ch[k]);
      const float s = __bfloat162float(sh[k]);
      // bf16-round on the x*cos term, then fp32 sine add (matches baseline).
      const float of = __bfloat162float(__float2bfloat16(xf * c)) - xs * s;
      const float os = __bfloat162float(__float2bfloat16(xs * c)) + xf * s;
      ofh[k] = __float2bfloat16(of);
      osh[k] = __float2bfloat16(os);
    }
    *reinterpret_cast<int4*>(out + xb + j0) = of4;
    *reinterpret_cast<int4*>(out + xb + HALF + j0) = os4;
  }
}

inline __nv_bfloat16* bf16_ptr(torch::Tensor& t) {
  return reinterpret_cast<__nv_bfloat16*>(t.data_ptr<at::BFloat16>());
}
inline const __nv_bfloat16* bf16_ptr(const torch::Tensor& t) {
  return reinterpret_cast<const __nv_bfloat16*>(t.data_ptr<at::BFloat16>());
}

}  // namespace

// ---------------------------------------------------------------------------
// Host entry points (out-of-place; return a new tensor).
// ---------------------------------------------------------------------------
torch::Tensor apply_rotary_embedding_cuda(torch::Tensor x, torch::Tensor cos,
                                          torch::Tensor sin, bool interleaved) {
  TORCH_CHECK(!interleaved, "cuda fast path is interleaved=False only");
  TORCH_CHECK(x.is_cuda() && x.scalar_type() == at::kBFloat16 && x.is_contiguous());
  TORCH_CHECK(cos.scalar_type() == at::kFloat && cos.is_contiguous());
  TORCH_CHECK(sin.scalar_type() == at::kFloat && sin.is_contiguous());

  int num_tokens, num_heads, head_size;
  long bt_total;
  if (x.dim() > 3) {
    bt_total = (long)x.size(0) * x.size(1);
    num_tokens = x.size(1);
    num_heads = x.size(2);
    head_size = x.size(3);
  } else {
    bt_total = x.size(0);
    num_tokens = x.size(0);
    num_heads = x.size(1);
    head_size = x.size(2);
  }
  TORCH_CHECK(head_size == kStdHeadDim, "cuda fast path requires head_dim 128");
  TORCH_CHECK(cos.size(-1) == kStdHalf && sin.size(-1) == kStdHalf);

  torch::Tensor out = torch::empty_like(x);
  const dim3 grid((unsigned)bt_total);
  const dim3 block(256);
  const c10::cuda::CUDAGuard device_guard(x.device());  // launch on the inputs' device, not the current one
  auto stream = at::cuda::getCurrentCUDAStream();
  rope_std_kernel<<<grid, block, 0, stream>>>(bf16_ptr(out), bf16_ptr(x),
                                              cos.data_ptr<float>(),
                                              sin.data_ptr<float>(),
                                              num_heads, num_tokens);
  C10_CUDA_KERNEL_LAUNCH_CHECK();
  return out;
}

torch::Tensor apply_ltx2_split_rotary_emb_cuda(torch::Tensor x, torch::Tensor cos,
                                               torch::Tensor sin) {
  TORCH_CHECK(x.is_cuda() && x.scalar_type() == at::kBFloat16 && x.is_contiguous());
  TORCH_CHECK(cos.scalar_type() == at::kBFloat16 && sin.scalar_type() == at::kBFloat16);
  TORCH_CHECK(x.dim() == 3 && cos.dim() == 4 && sin.dim() == 4);

  const int batch = x.size(0);
  const int seq_len = x.size(1);
  const int num_heads = cos.size(1);
  const int half = cos.size(3);
  const int head_dim = 2 * half;
  TORCH_CHECK((long)x.size(2) == (long)num_heads * head_dim, "inner_dim mismatch");
  TORCH_CHECK(cos.stride(3) == 1 && sin.stride(3) == 1, "cos/sin innermost must be contiguous");

  torch::Tensor out = torch::empty_like(x);
  const dim3 grid((unsigned)((long)batch * seq_len));
  const dim3 block(256);
  const c10::cuda::CUDAGuard device_guard(x.device());  // launch on the inputs' device, not the current one
  auto stream = at::cuda::getCurrentCUDAStream();
  auto launch = [&](auto half_const) {
    constexpr int HALF = decltype(half_const)::value;
    ltx2_split_kernel<HALF><<<grid, block, 0, stream>>>(
        bf16_ptr(out), bf16_ptr(x), bf16_ptr(cos), bf16_ptr(sin), seq_len,
        num_heads, cos.stride(0), cos.stride(1), cos.stride(2), sin.stride(0),
        sin.stride(1), sin.stride(2));
  };
  if (half == 64) {
    launch(std::integral_constant<int, 64>{});
  } else if (half == 32) {
    launch(std::integral_constant<int, 32>{});
  } else {
    TORCH_CHECK(false, "cuda fast path requires half in {32,64}");
  }
  C10_CUDA_KERNEL_LAUNCH_CHECK();
  return out;
}

PYBIND11_MODULE(TORCH_EXTENSION_NAME, m) {
  m.def("apply_rotary_embedding", &apply_rotary_embedding_cuda,
        "adjacent-pair RoPE (B200, head_dim 128, interleaved=False)");
  m.def("apply_ltx2_split_rotary_emb", &apply_ltx2_split_rotary_emb_cuda,
        "LTX-2 split-half rotary (B200, half in {32,64})");
}
