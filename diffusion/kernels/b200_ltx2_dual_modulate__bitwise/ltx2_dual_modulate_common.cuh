// Shared host-side helpers for the LTX2 dual-modulation baseline and candidate.
// Included by both baseline/kernel.cu and solution/kernel.cu so the two sides
// perform BYTE-IDENTICAL input validation and reject the same unsupported rows
// (AC-1 ABI parity, AC-5 rejection). Also provides the TensorView -> at::Tensor
// view used to call ATen `rms_norm` inside the kernel call path.

#pragma once

#include <ATen/ATen.h>
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
#include <vector>

namespace ltx2 {

using tvm::ffi::TensorView;

template <typename... Args>
[[noreturn]] inline void fail(Args&&... args) {
  std::ostringstream oss;
  (oss << ... << args);
  throw std::runtime_error(oss.str());
}

#define LTX2_CHECK(cond, ...) \
  do {                        \
    if (!(cond)) {            \
      ::ltx2::fail(__VA_ARGS__); \
    }                         \
  } while (0)

inline bool dtype_is(DLDataType d, uint8_t code, uint8_t bits) {
  return d.code == code && d.bits == bits && d.lanes == 1;
}
inline bool is_bf16(DLDataType d) { return dtype_is(d, kDLBfloat, 16); }
inline bool is_f32(DLDataType d) { return dtype_is(d, kDLFloat, 32); }

inline at::ScalarType dl_scalar(DLDataType d) {
  if (is_bf16(d)) return at::kBFloat16;
  if (is_f32(d)) return at::kFloat;
  fail("unsupported dtype: code=", int(d.code), " bits=", int(d.bits));
}

// Non-owning at::Tensor view over a TensorView's storage (honours byte offset
// and strides). Used to call ATen ops; never frees the underlying buffer.
inline at::Tensor as_tensor(const TensorView& t) {
  std::vector<int64_t> sizes(t.ndim()), strides(t.ndim());
  for (int i = 0; i < t.ndim(); ++i) {
    sizes[i] = t.size(i);
    strides[i] = t.stride(i);
  }
  void* p = static_cast<char*>(t.data_ptr()) + t.byte_offset();
  auto opts = at::TensorOptions()
                  .dtype(dl_scalar(t.dtype()))
                  .device(at::kCUDA, t.device().device_id);
  return at::from_blob(p, sizes, strides, opts);
}

template <typename T>
inline const T* const_ptr(const TensorView& t) {
  return reinterpret_cast<const T*>(
      static_cast<const char*>(t.data_ptr()) + t.byte_offset());
}
template <typename T>
inline T* mut_ptr(const TensorView& t) {
  return reinterpret_cast<T*>(static_cast<char*>(t.data_ptr()) + t.byte_offset());
}

inline bool last_dim_contiguous(const TensorView& t) {
  return t.ndim() > 0 && t.stride(t.ndim() - 1) == 1;
}

struct Dims {
  int64_t B, S, D;
};

struct ParamStrides {
  int64_t sb;  // stride over batch
  int64_t ss;  // stride over sequence (0 when broadcast over S)
};

inline Dims check_x(const TensorView& x) {
  LTX2_CHECK(x.device().device_type == kDLCUDA, "x must be a CUDA tensor");
  LTX2_CHECK(is_bf16(x.dtype()), "x must be bfloat16");
  LTX2_CHECK(x.ndim() == 3, "x must be rank-3 [B, S, D]");
  LTX2_CHECK(last_dim_contiguous(x), "x last dimension must be contiguous");
  int64_t D = x.size(2);
  LTX2_CHECK(D % 256 == 0 && D <= 8192,
             "hidden size must be divisible by 256 and <= 8192 (got ", D, ")");
  return {x.size(0), x.size(1), D};
}

// Accepts exactly [B, D], [B, 1, D], or [B, S, D] (bf16, CUDA, last-dim
// contiguous); rejects rank-1, wrong batch, and wrong sequence length so the
// kernel can never index out of bounds.
inline ParamStrides check_explicit_param(const TensorView& p, const Dims& dm,
                                         const char* name) {
  LTX2_CHECK(p.device().device_type == kDLCUDA, name, " must be a CUDA tensor");
  LTX2_CHECK(is_bf16(p.dtype()), name, " must be bfloat16");
  LTX2_CHECK(last_dim_contiguous(p), name, " last dimension must be contiguous");
  if (p.ndim() == 2) {
    LTX2_CHECK(p.size(0) == dm.B, name, " batch must equal B");
    LTX2_CHECK(p.size(1) == dm.D, name, " hidden size must equal D");
    return {p.stride(0), 0};
  }
  LTX2_CHECK(p.ndim() == 3, name, " must be rank 2 or 3 ([B,D]/[B,1,D]/[B,S,D])");
  LTX2_CHECK(p.size(0) == dm.B, name, " batch must equal B");
  LTX2_CHECK(p.size(2) == dm.D, name, " hidden size must equal D");
  LTX2_CHECK(p.size(1) == 1 || p.size(1) == dm.S, name,
             " sequence dim must be 1 or S");
  return {p.stride(0), (p.size(1) == 1) ? 0 : p.stride(1)};
}

inline int64_t check_temb(const TensorView& t, const Dims& dm) {
  LTX2_CHECK(t.device().device_type == kDLCUDA,
             "temb_scale_shift must be a CUDA tensor");
  LTX2_CHECK(is_bf16(t.dtype()), "temb_scale_shift must be bfloat16");
  LTX2_CHECK(last_dim_contiguous(t),
             "temb_scale_shift last dimension must be contiguous");
  LTX2_CHECK(t.ndim() == 3, "temb_scale_shift must be [B, temb_seq, 4*D]");
  LTX2_CHECK(t.size(0) == dm.B, "temb_scale_shift batch must equal B");
  int64_t temb_seq = t.size(1);
  LTX2_CHECK(temb_seq == 1 || temb_seq == dm.S,
             "temb_scale_shift seq dim must be 1 or S");
  LTX2_CHECK(t.size(2) == 4 * dm.D,
             "temb_scale_shift last dimension must be 4*D");
  return temb_seq;
}

inline bool check_table(const TensorView& t, const Dims& dm) {
  LTX2_CHECK(t.device().device_type == kDLCUDA,
             "scale_shift_table must be a CUDA tensor");
  LTX2_CHECK(last_dim_contiguous(t),
             "scale_shift_table last dimension must be contiguous");
  LTX2_CHECK(t.ndim() == 2 && t.size(0) == 4 && t.size(1) == dm.D,
             "scale_shift_table must be [4, D]");
  bool f32 = is_f32(t.dtype());
  LTX2_CHECK(f32 || is_bf16(t.dtype()),
             "scale_shift_table must be bfloat16 or float32");
  return f32;
}

inline void check_output(const TensorView& y, const Dims& dm, const char* name) {
  LTX2_CHECK(y.device().device_type == kDLCUDA, name, " must be a CUDA tensor");
  LTX2_CHECK(is_bf16(y.dtype()), name, " must be bfloat16");
  LTX2_CHECK(y.ndim() == 3 && y.size(0) == dm.B && y.size(1) == dm.S &&
                 y.size(2) == dm.D,
             name, " shape must equal [B, S, D]");
  LTX2_CHECK(last_dim_contiguous(y), name, " last dimension must be contiguous");
}

}  // namespace ltx2
