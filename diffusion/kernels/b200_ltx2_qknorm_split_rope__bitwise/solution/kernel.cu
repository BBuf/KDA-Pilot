// Candidate CUDA implementation of the LTX2 split rotary embedding. The full
// candidate composes torch.nn.RMSNorm (reused unchanged, bit-exact by
// construction) with this fused split-RoPE kernel; see solution/candidate.py.
//
// Bit-exactness target (the eager fallback of upstream apply_split_rotary_emb):
//   out_first  = (first * cos)  - sin * second
//   out_second = (second * cos) + sin * first
// where `first*cos` / `second*cos` are rounded to bf16 FIRST (matching the
// standalone `out = split_x * cos_u` bf16 multiply), then the sine term is added
// (matching `addcmul_`). The first product is therefore visibly rounded before
// the sine term is added; we must not contract the whole expression into a
// single FMA. The addcmul step here uses an fp32 fused-multiply-add then a single
// bf16 round (hypothesis: PyTorch addcmul uses fp32 opmath); confirmed/adjusted
// empirically on the B200 against the torch oracle.
//
// cos/sin are indexed via their real strides (production layout is physically
// [B,S,num_heads,head_dim/2] viewed [B,num_heads,S,head_dim/2]); q/k and the
// output are contiguous [B,S,H]. Unsupported configs are rejected before launch
// by solution/candidate.py:validate_candidate_inputs (the authoritative entry gate).
//
// ABI: destination-passing, output last, current CUDA stream. Exported via
// tvm-ffi as `ltx2_split_rope_candidate`.

#include <ATen/cuda/CUDAContext.h>
#include <c10/cuda/CUDAGuard.h>

#include <cuda_bf16.h>

#include <dlpack/dlpack.h>
#include <tvm/ffi/container/tensor.h>
#include <tvm/ffi/function.h>

namespace {

using tvm::ffi::TensorView;

__global__ void ltx2_split_rope_kernel(
    const __nv_bfloat16* __restrict__ x,
    const __nv_bfloat16* __restrict__ cos,
    const __nv_bfloat16* __restrict__ sin,
    __nv_bfloat16* __restrict__ out,
    long n_pairs, long S, long H, int num_heads, int r,
    long cs0, long cs1, long cs2, long cs3,
    long ss0, long ss1, long ss2, long ss3) {
  const long per_row = static_cast<long>(num_heads) * r;
  const long head_dim = 2L * r;
  const long step = static_cast<long>(gridDim.x) * blockDim.x;
  for (long tid = static_cast<long>(blockIdx.x) * blockDim.x + threadIdx.x;
       tid < n_pairs; tid += step) {
    const long row = tid / per_row;            // [0, B*S)
    const long rem = tid - row * per_row;
    const long b = row / S;
    const long s = row - b * S;
    const int head = static_cast<int>(rem / r);
    const int j = static_cast<int>(rem - static_cast<long>(head) * r);

    const long base = row * H + static_cast<long>(head) * head_dim;
    const long i_first = base + j;
    const long i_second = base + r + j;
    const long coff = b * cs0 + static_cast<long>(head) * cs1 + s * cs2 + static_cast<long>(j) * cs3;
    const long soff = b * ss0 + static_cast<long>(head) * ss1 + s * ss2 + static_cast<long>(j) * ss3;

    const float first = __bfloat162float(x[i_first]);
    const float second = __bfloat162float(x[i_second]);
    const float cv = __bfloat162float(cos[coff]);
    const float sv = __bfloat162float(sin[soff]);

    // First, round (first*cos) and (second*cos) to bf16 (matches split_x*cos_u).
    const float fc = __bfloat162float(__float2bfloat16_rn(first * cv));
    const float sc = __bfloat162float(__float2bfloat16_rn(second * cv));
    // Then add the sine term in fp32, single bf16 round (not contracted with the above).
    out[i_first] = __float2bfloat16_rn(__fmaf_rn(-sv, second, fc));
    out[i_second] = __float2bfloat16_rn(__fmaf_rn(sv, first, sc));
  }
}

void ltx2_split_rope_candidate(
    TensorView x,    // [B, S, H] bf16, contiguous (RMSNorm output)
    TensorView cos,  // [B, num_heads, S, head_dim/2] bf16 (strided ok)
    TensorView sin,  // [B, num_heads, S, head_dim/2] bf16 (strided ok)
    TensorView out) {  // [B, S, H] bf16, contiguous (destination, passed last)
  const long B = x.size(0);
  const long S = x.size(1);
  const long H = x.size(2);
  const int num_heads = static_cast<int>(cos.size(1));
  const int r = static_cast<int>(cos.size(3));
  const long n_pairs = B * S * static_cast<long>(num_heads) * r;
  if (n_pairs == 0) return;

  const int x_dev = x.device().device_id;
  const c10::cuda::CUDAGuard device_guard{static_cast<c10::DeviceIndex>(x_dev)};
  cudaStream_t stream = at::cuda::getCurrentCUDAStream();

  const auto* x_p = reinterpret_cast<const __nv_bfloat16*>(
      static_cast<const char*>(x.data_ptr()) + x.byte_offset());
  const auto* cos_p = reinterpret_cast<const __nv_bfloat16*>(
      static_cast<const char*>(cos.data_ptr()) + cos.byte_offset());
  const auto* sin_p = reinterpret_cast<const __nv_bfloat16*>(
      static_cast<const char*>(sin.data_ptr()) + sin.byte_offset());
  auto* out_p = reinterpret_cast<__nv_bfloat16*>(
      static_cast<char*>(out.data_ptr()) + out.byte_offset());

  const int block = 256;
  long grid = (n_pairs + block - 1) / block;
  const long grid_cap = 65535L * 8;
  if (grid > grid_cap) grid = grid_cap;

  ltx2_split_rope_kernel<<<static_cast<unsigned>(grid), block, 0, stream>>>(
      x_p, cos_p, sin_p, out_p, n_pairs, S, H, num_heads, r,
      cos.stride(0), cos.stride(1), cos.stride(2), cos.stride(3),
      sin.stride(0), sin.stride(1), sin.stride(2), sin.stride(3));
}

}  // namespace

TVM_FFI_DLL_EXPORT_TYPED_FUNC(ltx2_split_rope_candidate, ltx2_split_rope_candidate);
