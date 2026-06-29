// Optimized staged candidate for b200_ltx2_rms_adaln__bitwise, exposed through
// the same destination-passing tvm-ffi ABI as the baseline (baseline/kernel.cu):
//
//   ltx2_rms_adaln_candidate(x, scale, shift, eps, output)
//
// Reference semantics (docs/baseline_source.md, docs/numerics_notes.md),
// recovered from SGLang main @ aaa31eb (re-confirmed byte-identical @ bb74ed4a)
// -> RMSNormNoWeight.forward_native + the inline DiT modulation callsite, both
// plain eager:
//
//   normed = torch.nn.functional.rms_norm(x, (D,), eps=eps)   // fp32 reduction, bf16 store
//   y = normed * (1 + scale) + shift                          // three bf16 stages
//
// STRATEGY (staged): stage 1 reuses the SAME at::rms_norm as the baseline, so
// `normed` is bit-identical by construction (no reduction-order reverse
// engineering). Stage 2 is one fused CUDA kernel that reproduces the three
// post-norm bf16 round-to-nearest-even boundaries exactly:
//
//   one_plus = bf16_rne(1.0f + f32(scale))
//   mul      = bf16_rne(f32(normed) * f32(one_plus))
//   y        = bf16_rne(f32(mul) + f32(shift))
//
// Explicit __float2bfloat16_rn / __fadd_rn / __fmul_rn; the intermediate
// roundings are barriers, so there is NO unbroken a*b+c expression to contract
// into an FMA. No --use_fast_math / FTZ (build flags symmetric with baseline).
// ATen ops + the kernel launch use torch's current CUDA stream. No sglang import.

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

inline bool is_bf16(const TensorView& t) { return dtype_is(t.dtype(), kDLBfloat, 16); }

inline at::ScalarType dl_to_scalar_type(DLDataType d) {
  if (dtype_is(d, kDLBfloat, 16)) return at::kBFloat16;
  if (dtype_is(d, kDLFloat, 16)) return at::kHalf;
  if (dtype_is(d, kDLFloat, 32)) return at::kFloat;
  cand_fail("unsupported dtype: code=", int(d.code), " bits=", int(d.bits));
}

// Effective element base pointer (storage pointer + byte offset). Mirrors what
// torch reports as Tensor.data_ptr(), which the Python gate aligns on.
inline uintptr_t eff_ptr(const TensorView& t) {
  return reinterpret_cast<uintptr_t>(static_cast<char*>(t.data_ptr()) + t.byte_offset());
}

// Row-major contiguity (compact), matching torch.Tensor.is_contiguous():
// size-1 dims do not constrain stride.
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

// Wrap a TensorView's existing device memory as an at::Tensor (no copy), for the
// shared at::rms_norm call. Mirrors baseline/kernel.cu::view_as_aten.
inline at::Tensor view_as_aten(const TensorView& t) {
  const int nd = t.ndim();
  std::vector<int64_t> sizes(nd), strides(nd);
  for (int i = 0; i < nd; ++i) {
    sizes[i] = t.size(i);
    strides[i] = t.stride(i);
  }
  CAND_CHECK(t.device().device_type == kDLCUDA, "all tensors must be CUDA");
  auto opts = at::TensorOptions()
                  .dtype(dl_to_scalar_type(t.dtype()))
                  .device(at::kCUDA, t.device().device_id);
  void* ptr = static_cast<char*>(t.data_ptr()) + t.byte_offset();
  return at::from_blob(ptr, sizes, strides, opts);
}

// Broadcast layout of a scale/shift tensor (exactly mirrors
// bench/adapter.py::layout_mode). The per-element offset for logical position
// (b, s, d) is b*sb + s*ss + d, with (sb, ss) derived from the mode:
//   PERCHAN [D]            : sb=0,    ss=0   -> offset = d
//   PERBATCH [B,D]/[B,1,D] : sb=D,    ss=0   -> offset = b*D + d
//   FULL [B,S,D]           : sb=S*D,  ss=D   -> offset = (b*S+s)*D + d = row*D + d
enum BcastMode : int { PERCHAN = 0, PERBATCH = 1, FULL = 2 };

inline BcastMode classify_mode(const TensorView& m, int64_t B, int64_t S, int64_t D,
                               const char* name) {
  CAND_CHECK(m.device().device_type == kDLCUDA, name, ": must be CUDA");
  CAND_CHECK(is_bf16(m), name, ": must be bfloat16");
  CAND_CHECK(is_compact(m), name, ": must be contiguous");
  const int nd = m.ndim();
  if (nd == 1 && m.size(0) == D) return PERCHAN;
  if (nd == 2 && m.size(0) == B && m.size(1) == D) return PERBATCH;
  if (nd == 3 && m.size(0) == B && m.size(1) == 1 && m.size(2) == D) return PERBATCH;
  if (nd == 3 && m.size(0) == B && m.size(1) == S && m.size(2) == D) return FULL;
  cand_fail(name, ": unsupported broadcast layout (rank ", nd, ")");
}

// One fused vec8 (16-byte) element group per loop iteration. normed and out are
// compact [N, D] (N = B*S). scale/shift base offset per row is selected by mode.
__global__ void modulate_kernel(const __nv_bfloat16* __restrict__ normed,
                                const __nv_bfloat16* __restrict__ scale,
                                const __nv_bfloat16* __restrict__ shift,
                                __nv_bfloat16* __restrict__ out,
                                int64_t N, int64_t S, int64_t D,
                                int scale_mode, int shift_mode) {
  const int64_t vec_per_row = D >> 3;            // D / 8 (D % 256 == 0 -> exact)
  const int64_t total_vec = N * vec_per_row;
  const int64_t stride = static_cast<int64_t>(gridDim.x) * blockDim.x;
  for (int64_t idx = static_cast<int64_t>(blockIdx.x) * blockDim.x + threadIdx.x;
       idx < total_vec; idx += stride) {
    const int64_t row = idx / vec_per_row;
    const int64_t d_base = (idx - row * vec_per_row) << 3;   // column * 8
    const int64_t nd_off = row * D + d_base;                 // normed/out element offset

    int64_t s_off, h_off;
    if (scale_mode == FULL)          s_off = nd_off;
    else if (scale_mode == PERBATCH) s_off = (row / S) * D + d_base;
    else /* PERCHAN */               s_off = d_base;
    if (shift_mode == FULL)          h_off = nd_off;
    else if (shift_mode == PERBATCH) h_off = (row / S) * D + d_base;
    else /* PERCHAN */               h_off = d_base;

    // 16-byte vectorized loads (8 bf16). All base pointers are 16-byte aligned
    // (support gate) and every offset is a multiple of 8, so each access is
    // 16-byte aligned.
    const uint4 nv = *reinterpret_cast<const uint4*>(normed + nd_off);
    const uint4 sv = *reinterpret_cast<const uint4*>(scale + s_off);
    const uint4 hv = *reinterpret_cast<const uint4*>(shift + h_off);
    const __nv_bfloat16* n8 = reinterpret_cast<const __nv_bfloat16*>(&nv);
    const __nv_bfloat16* s8 = reinterpret_cast<const __nv_bfloat16*>(&sv);
    const __nv_bfloat16* h8 = reinterpret_cast<const __nv_bfloat16*>(&hv);

    uint4 ov;
    __nv_bfloat16* o8 = reinterpret_cast<__nv_bfloat16*>(&ov);
#pragma unroll
    for (int j = 0; j < 8; ++j) {
      // Three discrete bf16 round-to-nearest-even boundaries (matches eager).
      // Operand order 1.0f + scale is kept; no FMA contraction.
      const float sc = __bfloat162float(s8[j]);
      const __nv_bfloat16 one_plus = __float2bfloat16_rn(__fadd_rn(1.0f, sc));
      const float prod =
          __fmul_rn(__bfloat162float(n8[j]), __bfloat162float(one_plus));
      const __nv_bfloat16 mul = __float2bfloat16_rn(prod);
      const float sum = __fadd_rn(__bfloat162float(mul), __bfloat162float(h8[j]));
      o8[j] = __float2bfloat16_rn(sum);
    }
    *reinterpret_cast<uint4*>(out + nd_off) = ov;
  }
}

// ltx2_rms_adaln_candidate(x, scale, shift, eps, output)
//   x:      [B, S, D] bf16, contiguous
//   scale:  bf16, layout in {[D], [B,D], [B,1,D], [B,S,D]}, contiguous
//   shift:  same as scale
//   eps:    double
//   output: [B, S, D] bf16, contiguous (destination, written in place)
void ltx2_rms_adaln_candidate(TensorView x, TensorView scale, TensorView shift,
                              double eps, TensorView output) {
  // ---- fail-closed support gate (mirrors bench/adapter.py::in_gate) ----
  CAND_CHECK(x.device().device_type == kDLCUDA, "x must be CUDA");
  CAND_CHECK(is_bf16(x), "x must be bfloat16");
  CAND_CHECK(x.ndim() == 3, "x must be rank-3 [B,S,D]");
  CAND_CHECK(is_compact(x), "x must be contiguous");
  const int64_t B = x.size(0), S = x.size(1), D = x.size(2);
  CAND_CHECK(D % 256 == 0 && D <= 8192,
             "D must be a multiple of 256 and <= 8192 (got ", D, ")");
  const int dev = x.device().device_id;

  // output: same device, bf16, same shape as x, contiguous
  CAND_CHECK(output.device().device_type == kDLCUDA && output.device().device_id == dev,
             "output must be on the same CUDA device as x");
  CAND_CHECK(is_bf16(output), "output must be bfloat16");
  CAND_CHECK(output.ndim() == 3 && output.size(0) == B && output.size(1) == S &&
                 output.size(2) == D,
             "output shape must equal x [B,S,D]");
  CAND_CHECK(is_compact(output), "output must be contiguous");

  // scale/shift: same device + classify layout (also checks bf16 + contiguity)
  CAND_CHECK(scale.device().device_type == kDLCUDA && scale.device().device_id == dev,
             "scale must be on the same CUDA device as x");
  CAND_CHECK(shift.device().device_type == kDLCUDA && shift.device().device_id == dev,
             "shift must be on the same CUDA device as x");
  const BcastMode scale_mode = classify_mode(scale, B, S, D, "scale");
  const BcastMode shift_mode = classify_mode(shift, B, S, D, "shift");

  // 16-byte alignment of every vectorized buffer (x included, per gate policy).
  CAND_CHECK(eff_ptr(x) % 16 == 0, "x base pointer must be 16-byte aligned");
  CAND_CHECK(eff_ptr(scale) % 16 == 0, "scale base pointer must be 16-byte aligned");
  CAND_CHECK(eff_ptr(shift) % 16 == 0, "shift base pointer must be 16-byte aligned");
  CAND_CHECK(eff_ptr(output) % 16 == 0, "output base pointer must be 16-byte aligned");

  // Aliasing: output overwriting scale/shift would corrupt vectorized reads.
  // (output aliasing x is safe: x is fully consumed by at::rms_norm into a fresh
  // `normed` buffer before the modulation kernel writes any output element.)
  const uintptr_t out_a = eff_ptr(output);
  const int64_t out_b = numel(output) * 2;
  auto overlaps = [](uintptr_t a, int64_t an, uintptr_t b, int64_t bn) {
    return a < b + static_cast<uintptr_t>(bn) && b < a + static_cast<uintptr_t>(an);
  };
  CAND_CHECK(!overlaps(out_a, out_b, eff_ptr(scale), numel(scale) * 2),
             "output must not alias scale");
  CAND_CHECK(!overlaps(out_a, out_b, eff_ptr(shift), numel(shift) * 2),
             "output must not alias shift");

  const c10::cuda::CUDAGuard guard(at::Device(at::kCUDA, dev));
  cudaStream_t stream = at::cuda::getCurrentCUDAStream();

  // ---- stage 1: shared at::rms_norm -> bit-identical bf16 `normed` ----
  at::Tensor xt = view_as_aten(x);
  at::Tensor normed = at::rms_norm(xt, {D}, /*weight=*/{}, /*eps=*/eps);

  // ---- stage 2: fused three-stage bf16 modulation ----
  const auto* normed_ptr = reinterpret_cast<const __nv_bfloat16*>(normed.data_ptr());
  const auto* scale_ptr = reinterpret_cast<const __nv_bfloat16*>(
      static_cast<char*>(scale.data_ptr()) + scale.byte_offset());
  const auto* shift_ptr = reinterpret_cast<const __nv_bfloat16*>(
      static_cast<char*>(shift.data_ptr()) + shift.byte_offset());
  auto* out_ptr = reinterpret_cast<__nv_bfloat16*>(
      static_cast<char*>(output.data_ptr()) + output.byte_offset());

  const int64_t N = B * S;
  const int64_t total_vec = N * (D >> 3);
  if (total_vec == 0) return;

  const int block = 256;
  int64_t grid64 = (total_vec + block - 1) / block;
  const int64_t kMaxGrid = 262140;  // grid-stride loop covers any remainder
  if (grid64 > kMaxGrid) grid64 = kMaxGrid;
  const dim3 grid(static_cast<unsigned>(grid64));

  modulate_kernel<<<grid, block, 0, stream>>>(
      normed_ptr, scale_ptr, shift_ptr, out_ptr, N, S, D,
      static_cast<int>(scale_mode), static_cast<int>(shift_mode));
}

}  // namespace

TVM_FFI_DLL_EXPORT_TYPED_FUNC(ltx2_rms_adaln_candidate, ltx2_rms_adaln_candidate);
