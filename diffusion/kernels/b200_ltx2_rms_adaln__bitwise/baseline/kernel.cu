// PyTorch-eager baseline for b200_ltx2_rms_adaln__bitwise, exposed through the
// same destination-passing tvm-ffi ABI as the candidate (solution/kernel.cu):
//
//   ltx2_rms_adaln_baseline(x, scale, shift, eps, output)
//
// Reference semantics (docs/baseline_source.md), recovered from SGLang main
// @ aaa31eb -> RMSNormNoWeight.forward_native + the inline DiT modulation
// callsite, both plain eager:
//
//   normed = torch.nn.functional.rms_norm(x, (D,), eps=eps)
//   y = normed * (1 + scale) + shift
//
// This file runs the *identical* ATen ops as Python eager (F.rms_norm dispatches
// to at::rms_norm; `1 + scale`, `*`, `+` dispatch to the same ATen elementwise
// kernels), so the result is bit-identical to the Python oracle. It is wrapped
// in the same direct-CUDA ABI as the candidate so the benchmark times both
// sides through equal adapter/wrapper overhead. ATen ops launch on torch's
// current CUDA stream. No sglang import anywhere.

#include <ATen/ATen.h>
#include <ATen/cuda/CUDAContext.h>
#include <c10/cuda/CUDAGuard.h>

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
[[noreturn]] void base_fail(Args&&... args) {
  std::ostringstream oss;
  (oss << ... << args);
  throw std::runtime_error(oss.str());
}

#define BASE_CHECK(cond, ...) \
  do {                        \
    if (!(cond)) {            \
      base_fail(__VA_ARGS__); \
    }                         \
  } while (0)

inline bool dtype_is(DLDataType d, uint8_t code, uint8_t bits) {
  return d.code == code && d.bits == bits && d.lanes == 1;
}

inline at::ScalarType dl_to_scalar_type(DLDataType d) {
  if (dtype_is(d, kDLBfloat, 16)) return at::kBFloat16;
  if (dtype_is(d, kDLFloat, 16)) return at::kHalf;
  if (dtype_is(d, kDLFloat, 32)) return at::kFloat;
  base_fail("unsupported dtype: code=", int(d.code), " bits=", int(d.bits));
}

// Wrap a TensorView's existing device memory as an at::Tensor (no copy). The
// returned tensor aliases the caller's buffer; lifetime is bounded by the call.
inline at::Tensor view_as_aten(const TensorView& t) {
  const int nd = t.ndim();
  std::vector<int64_t> sizes(nd), strides(nd);
  for (int i = 0; i < nd; ++i) {
    sizes[i] = t.size(i);
    strides[i] = t.stride(i);
  }
  BASE_CHECK(t.device().device_type == kDLCUDA, "all tensors must be CUDA");
  auto opts = at::TensorOptions()
                  .dtype(dl_to_scalar_type(t.dtype()))
                  .device(at::kCUDA, t.device().device_id);
  void* ptr = static_cast<char*>(t.data_ptr()) + t.byte_offset();
  return at::from_blob(ptr, sizes, strides, opts);
}

// ltx2_rms_adaln_baseline(x, scale, shift, eps, output)
//   x:      [B, S, D] bf16, contiguous
//   scale:  bf16, broadcastable to x ([D] / [B,D] / [B,1,D] / [B,S,D])
//   shift:  same as scale
//   eps:    double
//   output: [B, S, D] bf16, contiguous (destination, written in place)
void ltx2_rms_adaln_baseline(TensorView x, TensorView scale, TensorView shift,
                             double eps, TensorView output) {
  BASE_CHECK(x.ndim() >= 1, "x must have rank >= 1");
  at::Tensor xt = view_as_aten(x);
  at::Tensor st = view_as_aten(scale);
  at::Tensor sht = view_as_aten(shift);
  at::Tensor ot = view_as_aten(output);

  const c10::cuda::CUDAGuard guard(xt.device());
  const int64_t D = xt.size(xt.dim() - 1);

  // A 2D [B,D] scale/shift is per-(batch,channel) modulation broadcast over S
  // (semantically [B,1,D]); PyTorch will not broadcast a bare [B,D] against
  // [B,S,D], so unsqueeze it. [D]/[B,1,D]/[B,S,D] already broadcast directly.
  if (st.dim() == 2) st = st.unsqueeze(1);
  if (sht.dim() == 2) sht = sht.unsqueeze(1);

  // Exact eager op order; each op rounds to bf16 just as Python eager does.
  at::Tensor normed = at::rms_norm(xt, {D}, /*weight=*/{}, /*eps=*/eps);
  at::Tensor y = normed * (st + 1) + sht;  // (st + 1) == Python's (1 + scale)
  ot.copy_(y);
}

}  // namespace

TVM_FFI_DLL_EXPORT_TYPED_FUNC(ltx2_rms_adaln_baseline, ltx2_rms_adaln_baseline);
