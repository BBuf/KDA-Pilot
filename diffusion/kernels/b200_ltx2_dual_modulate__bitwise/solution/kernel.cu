// Candidate CUDA implementation of the LTX2 dual-modulation affine for B200,
// exposed through a destination-passing tvm-ffi ABI (inputs first, output tensors
// last; launches on torch's current CUDA stream).
//
// Split-fusion strategy (see docs/rms_norm_numerics.md):
//   normalization `normed = F.rms_norm(x, (D,), eps)` is computed in PyTorch
//   (identical to the baseline, hence bit-identical by construction; the
//   vectorized fused RMS reduction is not reproducible by a naive kernel sum), and
//   this kernel fuses the dual affine (and, for the temb path, the scale/shift
//   derivation) into a single pass writing both outputs.
//
// Bit-exact eager parity: every PyTorch operation boundary is reproduced with an
// explicit round-to-nearest-even bf16 store and fp32 opmath, with no FMA
// contraction and no fast-math:
//   t = bf16_rne(1 + scale); p = bf16_rne(normed * t); y = bf16_rne(p + shift).
//
// Entry points:
//   ltx2_dual_modulate_candidate(normed, scale0, shift0, scale1, shift1, y0, y1)
//   ltx2_ca_dual_modulate_from_temb_candidate(normed, temb_scale_shift,
//       scale_shift_table, y0, y1)

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
inline bool is_f32(DLDataType d) { return dtype_is(d, kDLFloat, 32); }

template <typename T>
inline const T* data_of(const TensorView& t) {
  return reinterpret_cast<const T*>(
      static_cast<const char*>(t.data_ptr()) + t.byte_offset());
}
template <typename T>
inline T* mutable_data_of(const TensorView& t) {
  return reinterpret_cast<T*>(
      static_cast<char*>(t.data_ptr()) + t.byte_offset());
}

inline bool last_dim_contiguous(const TensorView& t) {
  return t.ndim() > 0 && t.stride(t.ndim() - 1) == 1;
}

inline void check_bf16_cuda(const TensorView& t, const char* name) {
  CAND_CHECK(t.device().device_type == kDLCUDA, name, " must be a CUDA tensor");
  CAND_CHECK(is_bf16(t.dtype()), name, " must be bfloat16");
  CAND_CHECK(last_dim_contiguous(t), name, " last dimension must be contiguous");
}

inline void check_output(const TensorView& out, int64_t B, int64_t S, int64_t D,
                         const char* name) {
  CAND_CHECK(out.device().device_type == kDLCUDA, name, " must be a CUDA tensor");
  CAND_CHECK(is_bf16(out.dtype()), name, " must be bfloat16");
  CAND_CHECK(out.ndim() == 3 && out.size(0) == B && out.size(1) == S &&
                 out.size(2) == D,
             name, " shape must equal [B, S, D]");
  CAND_CHECK(last_dim_contiguous(out), name, " last dimension must be contiguous");
}

constexpr int kThreads = 256;

inline int64_t grid_for(int64_t total) {
  return (total + kThreads - 1) / kThreads;
}

// --------------------------------------------------------------------------
// Exact eager bf16 rounding boundaries.
// --------------------------------------------------------------------------

// y = bf16_rne( bf16_rne( normed * bf16_rne(1 + scale) ) + shift )
__device__ __forceinline__ __nv_bfloat16 affine_bf16(__nv_bfloat16 normed,
                                                     __nv_bfloat16 scale,
                                                     __nv_bfloat16 shift) {
  __nv_bfloat16 t = __float2bfloat16_rn(__fadd_rn(1.0f, __bfloat162float(scale)));
  __nv_bfloat16 p =
      __float2bfloat16_rn(__fmul_rn(__bfloat162float(normed), __bfloat162float(t)));
  return __float2bfloat16_rn(__fadd_rn(__bfloat162float(p), __bfloat162float(shift)));
}

// scale/shift = bf16_rne( fp32(table_as_bf16) + fp32(temb) ). table_as_bf16 is the
// table value already rounded to bf16 (matching `scale_shift_table.to(x.dtype)`).
__device__ __forceinline__ __nv_bfloat16 add_bf16(__nv_bfloat16 a, __nv_bfloat16 b) {
  return __float2bfloat16_rn(__fadd_rn(__bfloat162float(a), __bfloat162float(b)));
}

// --------------------------------------------------------------------------
// Explicit dual modulation.
// --------------------------------------------------------------------------

__global__ void dual_modulate_kernel(
    const __nv_bfloat16* __restrict__ normed,
    const __nv_bfloat16* __restrict__ scale0,
    const __nv_bfloat16* __restrict__ shift0,
    const __nv_bfloat16* __restrict__ scale1,
    const __nv_bfloat16* __restrict__ shift1,
    __nv_bfloat16* __restrict__ y0, __nv_bfloat16* __restrict__ y1, int64_t S,
    int64_t D, int64_t p_sb, int64_t p_ss, int64_t total) {
  for (int64_t idx = blockIdx.x * (int64_t)blockDim.x + threadIdx.x; idx < total;
       idx += (int64_t)gridDim.x * blockDim.x) {
    int64_t d = idx % D;
    int64_t row = idx / D;
    int64_t s = row % S;
    int64_t b = row / S;
    int64_t pidx = b * p_sb + s * p_ss + d;  // param last-dim stride is 1
    __nv_bfloat16 nm = normed[idx];
    y0[idx] = affine_bf16(nm, scale0[pidx], shift0[pidx]);
    y1[idx] = affine_bf16(nm, scale1[pidx], shift1[pidx]);
  }
}

// --------------------------------------------------------------------------
// Cross-attention dual modulation from temb.
// --------------------------------------------------------------------------

template <bool TABLE_F32>
__device__ __forceinline__ __nv_bfloat16 read_table_bf16(const void* table, int k,
                                                        int64_t D, int64_t d) {
  if (TABLE_F32) {
    return __float2bfloat16_rn(reinterpret_cast<const float*>(table)[k * D + d]);
  }
  return reinterpret_cast<const __nv_bfloat16*>(table)[k * D + d];
}

template <bool TABLE_F32>
__global__ void ca_dual_modulate_kernel(
    const __nv_bfloat16* __restrict__ normed,
    const __nv_bfloat16* __restrict__ temb,  // [B, temb_seq, 4*D] contiguous
    const void* __restrict__ table,          // [4, D], bf16 or fp32
    __nv_bfloat16* __restrict__ y0, __nv_bfloat16* __restrict__ y1, int64_t S,
    int64_t D, int64_t temb_seq, int64_t total) {
  for (int64_t idx = blockIdx.x * (int64_t)blockDim.x + threadIdx.x; idx < total;
       idx += (int64_t)gridDim.x * blockDim.x) {
    int64_t d = idx % D;
    int64_t row = idx / D;
    int64_t s = row % S;
    int64_t b = row / S;
    int64_t st = (temb_seq == 1) ? 0 : s;
    int64_t base = (b * temb_seq + st) * (4 * D);
    __nv_bfloat16 scale0 = add_bf16(read_table_bf16<TABLE_F32>(table, 0, D, d), temb[base + 0 * D + d]);
    __nv_bfloat16 shift0 = add_bf16(read_table_bf16<TABLE_F32>(table, 1, D, d), temb[base + 1 * D + d]);
    __nv_bfloat16 scale1 = add_bf16(read_table_bf16<TABLE_F32>(table, 2, D, d), temb[base + 2 * D + d]);
    __nv_bfloat16 shift1 = add_bf16(read_table_bf16<TABLE_F32>(table, 3, D, d), temb[base + 3 * D + d]);
    __nv_bfloat16 nm = normed[idx];
    y0[idx] = affine_bf16(nm, scale0, shift0);
    y1[idx] = affine_bf16(nm, scale1, shift1);
  }
}

// --------------------------------------------------------------------------
// Host entry points.
// --------------------------------------------------------------------------

void extract_param_strides(const TensorView& p, int64_t D, const char* name,
                           int64_t& sb, int64_t& ss) {
  check_bf16_cuda(p, name);
  if (p.ndim() == 2) {
    CAND_CHECK(p.size(1) == D, name, " hidden size must equal D");
    sb = p.stride(0);
    ss = 0;
  } else {
    CAND_CHECK(p.ndim() == 3 && p.size(2) == D, name, " must be [B, *, D]");
    sb = p.stride(0);
    ss = (p.size(1) == 1) ? 0 : p.stride(1);
  }
}

void ltx2_dual_modulate_candidate(TensorView normed, TensorView scale0,
                                  TensorView shift0, TensorView scale1,
                                  TensorView shift1, TensorView y0,
                                  TensorView y1) {
  check_bf16_cuda(normed, "normed");
  CAND_CHECK(normed.ndim() == 3, "normed must be rank-3 [B, S, D]");
  int64_t B = normed.size(0), S = normed.size(1), D = normed.size(2);
  CAND_CHECK(D % 256 == 0 && D <= 8192,
             "hidden size must be divisible by 256 and <= 8192");
  // All four params must share one layout (parallel scale/shift tensors).
  CAND_CHECK(shift0.ndim() == scale0.ndim() && scale1.ndim() == scale0.ndim() &&
                 shift1.ndim() == scale0.ndim(),
             "scale/shift params must share rank");
  for (int i = 0; i < scale0.ndim(); ++i) {
    CAND_CHECK(shift0.size(i) == scale0.size(i) &&
                   scale1.size(i) == scale0.size(i) &&
                   shift1.size(i) == scale0.size(i),
               "scale/shift params must share shape");
  }
  int64_t p_sb = 0, p_ss = 0;
  extract_param_strides(scale0, D, "scale0", p_sb, p_ss);
  int64_t tmp_sb, tmp_ss;
  extract_param_strides(shift0, D, "shift0", tmp_sb, tmp_ss);
  extract_param_strides(scale1, D, "scale1", tmp_sb, tmp_ss);
  extract_param_strides(shift1, D, "shift1", tmp_sb, tmp_ss);
  check_output(y0, B, S, D, "y0");
  check_output(y1, B, S, D, "y1");

  int64_t total = B * S * D;
  if (total == 0) return;
  cudaStream_t stream = at::cuda::getCurrentCUDAStream();
  int64_t blocks = grid_for(total);
  if (blocks > 65535) blocks = 65535;
  dual_modulate_kernel<<<blocks, kThreads, 0, stream>>>(
      data_of<__nv_bfloat16>(normed), data_of<__nv_bfloat16>(scale0),
      data_of<__nv_bfloat16>(shift0), data_of<__nv_bfloat16>(scale1),
      data_of<__nv_bfloat16>(shift1), mutable_data_of<__nv_bfloat16>(y0),
      mutable_data_of<__nv_bfloat16>(y1), S, D, p_sb, p_ss, total);
}

void ltx2_ca_dual_modulate_from_temb_candidate(TensorView normed,
                                               TensorView temb_scale_shift,
                                               TensorView scale_shift_table,
                                               TensorView y0, TensorView y1) {
  check_bf16_cuda(normed, "normed");
  CAND_CHECK(normed.ndim() == 3, "normed must be rank-3 [B, S, D]");
  int64_t B = normed.size(0), S = normed.size(1), D = normed.size(2);
  CAND_CHECK(D % 256 == 0 && D <= 8192,
             "hidden size must be divisible by 256 and <= 8192");

  check_bf16_cuda(temb_scale_shift, "temb_scale_shift");
  CAND_CHECK(temb_scale_shift.ndim() == 3, "temb_scale_shift must be [B, *, 4*D]");
  CAND_CHECK(temb_scale_shift.size(0) == B, "temb_scale_shift batch must equal B");
  int64_t temb_seq = temb_scale_shift.size(1);
  CAND_CHECK(temb_seq == 1 || temb_seq == S, "temb_seq must be 1 or S");
  CAND_CHECK(temb_scale_shift.size(2) == 4 * D,
             "temb_scale_shift last dimension must be 4*D");

  CAND_CHECK(scale_shift_table.device().device_type == kDLCUDA,
             "scale_shift_table must be a CUDA tensor");
  CAND_CHECK(last_dim_contiguous(scale_shift_table),
             "scale_shift_table last dimension must be contiguous");
  CAND_CHECK(scale_shift_table.ndim() == 2 && scale_shift_table.size(0) == 4 &&
                 scale_shift_table.size(1) == D,
             "scale_shift_table must be [4, D]");
  bool table_f32 = is_f32(scale_shift_table.dtype());
  CAND_CHECK(table_f32 || is_bf16(scale_shift_table.dtype()),
             "scale_shift_table must be bfloat16 or float32");

  check_output(y0, B, S, D, "y0");
  check_output(y1, B, S, D, "y1");

  int64_t total = B * S * D;
  if (total == 0) return;
  cudaStream_t stream = at::cuda::getCurrentCUDAStream();
  int64_t blocks = grid_for(total);
  if (blocks > 65535) blocks = 65535;
  const __nv_bfloat16* nm = data_of<__nv_bfloat16>(normed);
  const __nv_bfloat16* tb = data_of<__nv_bfloat16>(temb_scale_shift);
  const void* table = static_cast<const void*>(
      static_cast<const char*>(scale_shift_table.data_ptr()) +
      scale_shift_table.byte_offset());
  __nv_bfloat16* o0 = mutable_data_of<__nv_bfloat16>(y0);
  __nv_bfloat16* o1 = mutable_data_of<__nv_bfloat16>(y1);
  if (table_f32) {
    ca_dual_modulate_kernel<true><<<blocks, kThreads, 0, stream>>>(
        nm, tb, table, o0, o1, S, D, temb_seq, total);
  } else {
    ca_dual_modulate_kernel<false><<<blocks, kThreads, 0, stream>>>(
        nm, tb, table, o0, o1, S, D, temb_seq, total);
  }
}

}  // namespace

TVM_FFI_DLL_EXPORT_TYPED_FUNC(ltx2_dual_modulate_candidate,
                              ltx2_dual_modulate_candidate);
TVM_FFI_DLL_EXPORT_TYPED_FUNC(ltx2_ca_dual_modulate_from_temb_candidate,
                              ltx2_ca_dual_modulate_from_temb_candidate);
