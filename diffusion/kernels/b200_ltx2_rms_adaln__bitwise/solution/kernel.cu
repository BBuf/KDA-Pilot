// Optimized candidate for b200_ltx2_rms_adaln__bitwise, exposed through a
// destination-passing tvm-ffi ABI that mirrors baseline/kernel.cu:
//
//   ltx2_rms_adaln_candidate(x, scale, shift, eps, output)
//
// Target (bit-wise equal to PyTorch eager; docs/baseline_source.md):
//   normed = F.rms_norm(x, (D,), eps=eps)
//   y = normed * (1 + scale) + shift     # each step rounds to bf16 (RNE)
//
// STAGED design (the bit-exactness-safe path):
//   Stage 1: normed = at::rms_norm(x, {D}, {}, eps)   -- the SAME ATen op the
//            baseline uses, so the fp32 reduction and bf16 store of `normed` are
//            bit-identical to the baseline by construction (no need to reverse-
//            engineer ATen's reduction order).
//   Stage 2: one custom fused CUDA kernel does the modulation in a single pass,
//            reproducing eager's three rounding points exactly:
//              one_plus = __float2bfloat16_rn(1 + scale)
//              mul      = __float2bfloat16_rn(normed * one_plus)
//              y        = __float2bfloat16_rn(mul + shift)
//            ATen's bf16 elementwise mul/add compute in fp32 opmath and store
//            with round-to-nearest-even; __float2bfloat16_rn matches that.
//
// This fuses eager's 3 elementwise launches + their temporaries into 1 kernel
// while preserving every PyTorch operation boundary. Launches on torch's
// current CUDA stream. Fail-closed support gate: CUDA, bf16, contiguous,
// rank-3 [B,S,D], D % 256 == 0, D <= 8192, scale/shift broadcast layout in
// {[D], [B,D], [B,1,D], [B,S,D]}; anything else throws (the public adapter
// routes out-of-gate inputs to the eager fallback). No sglang import.

#include <ATen/ATen.h>
#include <ATen/cuda/CUDAContext.h>
#include <c10/cuda/CUDAGuard.h>

#include <cuda_bf16.h>

#include <dlpack/dlpack.h>
#include <tvm/ffi/container/tensor.h>
#if __has_include(<tvm/ffi/function.h>)
#include <tvm/ffi/function.h>
#endif

#include <algorithm>
#include <cstdint>
#include <sstream>
#include <stdexcept>
#include <vector>

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

inline bool dtype_is(DLDataType d, uint8_t code, uint8_t bits) {
  return d.code == code && d.bits == bits && d.lanes == 1;
}
inline bool is_bf16(DLDataType d) { return dtype_is(d, kDLBfloat, 16); }

inline at::ScalarType dl_to_scalar_type(DLDataType d) {
  if (dtype_is(d, kDLBfloat, 16)) return at::kBFloat16;
  if (dtype_is(d, kDLFloat, 16)) return at::kHalf;
  if (dtype_is(d, kDLFloat, 32)) return at::kFloat;
  cand_fail("unsupported dtype: code=", int(d.code), " bits=", int(d.bits));
}

inline at::Tensor view_as_aten(const TensorView& t) {
  const int nd = t.ndim();
  std::vector<int64_t> sizes(nd), strides(nd);
  for (int i = 0; i < nd; ++i) {
    sizes[i] = t.size(i);
    strides[i] = t.stride(i);
  }
  auto opts = at::TensorOptions()
                  .dtype(dl_to_scalar_type(t.dtype()))
                  .device(at::kCUDA, t.device().device_id);
  void* ptr = static_cast<char*>(t.data_ptr()) + t.byte_offset();
  return at::from_blob(ptr, sizes, strides, opts);
}

inline bool tensor_is_contiguous(const TensorView& t) {
  int64_t expect = 1;
  for (int i = t.ndim() - 1; i >= 0; --i) {
    if (t.size(i) == 1) continue;
    if (t.stride(i) != expect) return false;
    expect *= t.size(i);
  }
  return true;
}

inline int64_t numel_of(const TensorView& t) {
  int64_t n = 1;
  for (int i = 0; i < t.ndim(); ++i) n *= t.size(i);
  return n;
}

// Broadcast modes for scale/shift over x=[B,S,D] (row r in [0,R), col c in [0,D)):
//   PERCHAN  ([D])            -> idx = c
//   PERBATCH ([B,D]/[B,1,D])  -> idx = (r / S) * D + c
//   FULL     ([B,S,D])        -> idx = r * D + c
enum BcastMode { PERCHAN = 0, PERBATCH = 1, FULL = 2 };

template <typename T>
union Vec16 {
  static constexpr int kElems = 16 / sizeof(T);
  uint4 raw;
  T elems[16 / sizeof(T)];
};

// One block per row; 8-wide (16B) vectorized columns; grid-stride within the row.
template <int MODE>
__global__ void rms_adaln_modulation_kernel(const __nv_bfloat16* __restrict__ normed,
                                            const __nv_bfloat16* __restrict__ scale,
                                            const __nv_bfloat16* __restrict__ shift,
                                            __nv_bfloat16* __restrict__ out,
                                            int S, int D) {
  constexpr int kPerVec = 8;  // 16 bytes / sizeof(bf16)
  const int row = blockIdx.x;
  const long row_base = static_cast<long>(row) * D;
  long mod_base;
  if (MODE == FULL) {
    mod_base = row_base;
  } else if (MODE == PERBATCH) {
    mod_base = static_cast<long>(row / S) * D;
  } else {  // PERCHAN
    mod_base = 0L;
  }
  const int vecD = D / kPerVec;
  for (int v = threadIdx.x; v < vecD; v += blockDim.x) {
    const int c = v * kPerVec;
    Vec16<__nv_bfloat16> n, s, h, o;
    n.raw = *reinterpret_cast<const uint4*>(normed + row_base + c);
    s.raw = *reinterpret_cast<const uint4*>(scale + mod_base + c);
    h.raw = *reinterpret_cast<const uint4*>(shift + mod_base + c);
#pragma unroll
    for (int k = 0; k < kPerVec; ++k) {
      const float nf = __bfloat162float(n.elems[k]);
      const float sf = __bfloat162float(s.elems[k]);
      const float hf = __bfloat162float(h.elems[k]);
      const __nv_bfloat16 one_plus = __float2bfloat16_rn(1.0f + sf);            // 1 + scale
      const __nv_bfloat16 mul =
          __float2bfloat16_rn(nf * __bfloat162float(one_plus));                 // normed * (1+scale)
      o.elems[k] = __float2bfloat16_rn(__bfloat162float(mul) + hf);            // + shift
    }
    *reinterpret_cast<uint4*>(out + row_base + c) = o.raw;
  }
}

int classify_mode(const TensorView& m, int64_t B, int64_t S, int64_t D,
                  const char* name) {
  const int64_t n = numel_of(m);
  if (n == D) return PERCHAN;
  if (n == B * D) return PERBATCH;     // [B,D] or [B,1,D]
  if (n == B * S * D) return FULL;     // [B,S,D]
  cand_fail(name, " has unsupported broadcast layout (numel=", n,
            ", expected ", D, ", ", B * D, ", or ", B * S * D, ")");
}

// ltx2_rms_adaln_candidate(x, scale, shift, eps, output)
void ltx2_rms_adaln_candidate(TensorView x, TensorView scale, TensorView shift,
                              double eps, TensorView output) {
  // ---- fail-closed support gate ----
  CAND_CHECK(x.device().device_type == kDLCUDA, "x must be a CUDA tensor");
  CAND_CHECK(is_bf16(x.dtype()), "x must be bfloat16 for the optimized path");
  CAND_CHECK(is_bf16(scale.dtype()) && is_bf16(shift.dtype()),
             "scale/shift must be bfloat16 for the optimized path");
  CAND_CHECK(is_bf16(output.dtype()), "output must be bfloat16");
  CAND_CHECK(x.ndim() == 3, "x must be rank-3 [B, S, D] for the optimized path");
  CAND_CHECK(tensor_is_contiguous(x), "x must be contiguous");
  CAND_CHECK(tensor_is_contiguous(output), "output must be contiguous");
  CAND_CHECK(tensor_is_contiguous(scale) && tensor_is_contiguous(shift),
             "scale/shift must be (last-dim) contiguous");

  const int64_t B = x.size(0), S = x.size(1), D = x.size(2);
  CAND_CHECK(output.ndim() == 3 && output.size(0) == B && output.size(1) == S &&
                 output.size(2) == D,
             "output shape must match x");
  CAND_CHECK(D % 256 == 0 && D <= 8192,
             "hidden size D must be divisible by 256 and <= 8192 (got ", D, ")");
  CAND_CHECK(scale.size(scale.ndim() - 1) == D && shift.size(shift.ndim() - 1) == D,
             "scale/shift last dim must equal D");

  const int mode_s = classify_mode(scale, B, S, D, "scale");
  const int mode_h = classify_mode(shift, B, S, D, "shift");
  CAND_CHECK(mode_s == mode_h,
             "scale and shift must share the same broadcast layout");

  // ---- Stage 1: exact ATen RMSNorm (bit-identical to the baseline's normed) ----
  at::Tensor xt = view_as_aten(x);
  const c10::cuda::CUDAGuard guard(xt.device());
  at::Tensor normed = at::rms_norm(xt, {D}, /*weight=*/{}, /*eps=*/eps);

  // ---- Stage 2: fused modulation kernel ----
  const auto* normed_ptr = reinterpret_cast<const __nv_bfloat16*>(normed.data_ptr());
  const auto* scale_ptr = reinterpret_cast<const __nv_bfloat16*>(
      static_cast<const char*>(scale.data_ptr()) + scale.byte_offset());
  const auto* shift_ptr = reinterpret_cast<const __nv_bfloat16*>(
      static_cast<const char*>(shift.data_ptr()) + shift.byte_offset());
  auto* out_ptr = reinterpret_cast<__nv_bfloat16*>(
      static_cast<char*>(output.data_ptr()) + output.byte_offset());

  const int rows = static_cast<int>(B * S);
  const int vecD = static_cast<int>(D / 8);
  int threads = std::min(1024, std::max(32, ((vecD + 31) / 32) * 32));
  cudaStream_t stream = at::cuda::getCurrentCUDAStream();
  dim3 grid(rows);

  switch (mode_s) {
    case PERCHAN:
      rms_adaln_modulation_kernel<PERCHAN><<<grid, threads, 0, stream>>>(
          normed_ptr, scale_ptr, shift_ptr, out_ptr, static_cast<int>(S),
          static_cast<int>(D));
      break;
    case PERBATCH:
      rms_adaln_modulation_kernel<PERBATCH><<<grid, threads, 0, stream>>>(
          normed_ptr, scale_ptr, shift_ptr, out_ptr, static_cast<int>(S),
          static_cast<int>(D));
      break;
    default:
      rms_adaln_modulation_kernel<FULL><<<grid, threads, 0, stream>>>(
          normed_ptr, scale_ptr, shift_ptr, out_ptr, static_cast<int>(S),
          static_cast<int>(D));
      break;
  }
}

}  // namespace

TVM_FFI_DLL_EXPORT_TYPED_FUNC(ltx2_rms_adaln_candidate, ltx2_rms_adaln_candidate);
