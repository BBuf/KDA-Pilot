// Candidate CUDA implementation of the LTX2 dual modulation for B200, exposed
// through the full-operation destination-passing TVM-FFI ABI (inputs first,
// scalar `double eps`, output tensors last; launches on torch's current CUDA
// stream).
//
// Split-fusion strategy (docs/rms_norm_numerics.md): `normed = F.rms_norm(x,(D,),eps)`
// is computed inside the call path via ATen `at::rms_norm` (bit-identical to the
// baseline; PyTorch's vectorized fused RMS reduction is not reproducible by a naive
// kernel), and this module fuses the dual affine (and, for the temb path, the
// scale/shift derivation) into a single pass writing both outputs.
//
// Bit-exact eager parity: every PyTorch operation boundary is reproduced with an
// explicit round-to-nearest-even bf16 store and fp32 opmath, no FMA contraction and
// no fast-math:  t=bf16(1+scale); p=bf16(normed*t); y=bf16(p+shift).
//
// Entry points (full op):
//   ltx2_dual_modulate_candidate(x, scale0, shift0, scale1, shift1, eps, y0, y1)
//   ltx2_ca_dual_modulate_from_temb_candidate(x, temb_scale_shift,
//       scale_shift_table, eps, y0, y1)

#include "../ltx2_dual_modulate_common.cuh"

#include <c10/cuda/CUDAGuard.h>

namespace {

using ltx2::as_tensor;
using ltx2::check_explicit_param;
using ltx2::check_output;
using ltx2::check_table;
using ltx2::check_temb;
using ltx2::check_x;
using ltx2::const_ptr;
using ltx2::Dims;
using ltx2::mut_ptr;
using ltx2::ParamStrides;
using ltx2::TableInfo;
using tvm::ffi::TensorView;

constexpr int kThreads = 256;

inline int64_t grid_for(int64_t total) {
  int64_t b = (total + kThreads - 1) / kThreads;
  return b > 65535 ? 65535 : b;
}

// y = bf16_rne( bf16_rne( normed * bf16_rne(1 + scale) ) + shift )
__device__ __forceinline__ __nv_bfloat16 affine_bf16(__nv_bfloat16 normed,
                                                     __nv_bfloat16 scale,
                                                     __nv_bfloat16 shift) {
  __nv_bfloat16 t = __float2bfloat16_rn(__fadd_rn(1.0f, __bfloat162float(scale)));
  __nv_bfloat16 p =
      __float2bfloat16_rn(__fmul_rn(__bfloat162float(normed), __bfloat162float(t)));
  return __float2bfloat16_rn(__fadd_rn(__bfloat162float(p), __bfloat162float(shift)));
}

// scale/shift = bf16_rne( fp32(table_as_bf16) + fp32(temb) ); table_as_bf16 mirrors
// `scale_shift_table.to(x.dtype)` (fp32 table is rounded to bf16 first).
__device__ __forceinline__ __nv_bfloat16 add_bf16(__nv_bfloat16 a, __nv_bfloat16 b) {
  return __float2bfloat16_rn(__fadd_rn(__bfloat162float(a), __bfloat162float(b)));
}

// Each of the four params broadcasts independently with its own (batch, seq)
// strides (seq stride 0 means broadcast over S; last-dim stride is always 1).
__global__ void dual_modulate_kernel(
    const __nv_bfloat16* __restrict__ normed,
    const __nv_bfloat16* __restrict__ scale0, int64_t s0_sb, int64_t s0_ss,
    const __nv_bfloat16* __restrict__ shift0, int64_t h0_sb, int64_t h0_ss,
    const __nv_bfloat16* __restrict__ scale1, int64_t s1_sb, int64_t s1_ss,
    const __nv_bfloat16* __restrict__ shift1, int64_t h1_sb, int64_t h1_ss,
    __nv_bfloat16* __restrict__ y0, __nv_bfloat16* __restrict__ y1, int64_t S,
    int64_t D, int64_t total) {
  for (int64_t idx = blockIdx.x * (int64_t)blockDim.x + threadIdx.x; idx < total;
       idx += (int64_t)gridDim.x * blockDim.x) {
    int64_t d = idx % D;
    int64_t row = idx / D;
    int64_t s = row % S;
    int64_t b = row / S;
    __nv_bfloat16 nm = normed[idx];
    y0[idx] = affine_bf16(nm, scale0[b * s0_sb + s * s0_ss + d],
                          shift0[b * h0_sb + s * h0_ss + d]);
    y1[idx] = affine_bf16(nm, scale1[b * s1_sb + s * s1_ss + d],
                          shift1[b * h1_sb + s * h1_ss + d]);
  }
}

template <bool TABLE_F32>
__device__ __forceinline__ __nv_bfloat16 read_table_bf16(const void* table, int k,
                                                        int64_t s0, int64_t d) {
  if (TABLE_F32) {
    return __float2bfloat16_rn(reinterpret_cast<const float*>(table)[k * s0 + d]);
  }
  return reinterpret_cast<const __nv_bfloat16*>(table)[k * s0 + d];
}

template <bool TABLE_F32>
__global__ void ca_dual_modulate_kernel(
    const __nv_bfloat16* __restrict__ normed,
    const __nv_bfloat16* __restrict__ temb,  // [B, temb_seq, 4*D] compact
    const void* __restrict__ table,          // [4, D], bf16 or fp32, row stride s0
    int64_t table_s0, __nv_bfloat16* __restrict__ y0,
    __nv_bfloat16* __restrict__ y1, int64_t S, int64_t D, int64_t temb_seq,
    int64_t total) {
  for (int64_t idx = blockIdx.x * (int64_t)blockDim.x + threadIdx.x; idx < total;
       idx += (int64_t)gridDim.x * blockDim.x) {
    int64_t d = idx % D;
    int64_t row = idx / D;
    int64_t s = row % S;
    int64_t b = row / S;
    int64_t st = (temb_seq == 1) ? 0 : s;
    int64_t base = (b * temb_seq + st) * (4 * D);
    __nv_bfloat16 scale0 = add_bf16(read_table_bf16<TABLE_F32>(table, 0, table_s0, d), temb[base + 0 * D + d]);
    __nv_bfloat16 shift0 = add_bf16(read_table_bf16<TABLE_F32>(table, 1, table_s0, d), temb[base + 1 * D + d]);
    __nv_bfloat16 scale1 = add_bf16(read_table_bf16<TABLE_F32>(table, 2, table_s0, d), temb[base + 2 * D + d]);
    __nv_bfloat16 shift1 = add_bf16(read_table_bf16<TABLE_F32>(table, 3, table_s0, d), temb[base + 3 * D + d]);
    __nv_bfloat16 nm = normed[idx];
    y0[idx] = affine_bf16(nm, scale0, shift0);
    y1[idx] = affine_bf16(nm, scale1, shift1);
  }
}

void ltx2_dual_modulate_candidate(TensorView x, TensorView scale0,
                                  TensorView shift0, TensorView scale1,
                                  TensorView shift1, double eps, TensorView y0,
                                  TensorView y1) {
  Dims dm = check_x(x);
  // Run on x's device (not necessarily the current device) for multi-GPU safety.
  const c10::cuda::CUDAGuard device_guard(static_cast<c10::DeviceIndex>(dm.dev));
  // Each param is validated and broadcast independently ([B,D]/[B,1,D]/[B,S,D]).
  ParamStrides s0 = check_explicit_param(scale0, dm, "scale0");
  ParamStrides h0 = check_explicit_param(shift0, dm, "shift0");
  ParamStrides s1 = check_explicit_param(scale1, dm, "scale1");
  ParamStrides h1 = check_explicit_param(shift1, dm, "shift1");
  check_output(y0, dm, "y0");
  check_output(y1, dm, "y1");

  int64_t total = dm.B * dm.S * dm.D;
  if (total == 0) return;
  at::Tensor normed = at::rms_norm(as_tensor(x), {dm.D}, c10::optional<at::Tensor>{},
                                   c10::optional<double>(eps));
  cudaStream_t stream = at::cuda::getCurrentCUDAStream();
  dual_modulate_kernel<<<grid_for(total), kThreads, 0, stream>>>(
      reinterpret_cast<const __nv_bfloat16*>(normed.data_ptr()),
      const_ptr<__nv_bfloat16>(scale0), s0.sb, s0.ss,
      const_ptr<__nv_bfloat16>(shift0), h0.sb, h0.ss,
      const_ptr<__nv_bfloat16>(scale1), s1.sb, s1.ss,
      const_ptr<__nv_bfloat16>(shift1), h1.sb, h1.ss,
      mut_ptr<__nv_bfloat16>(y0), mut_ptr<__nv_bfloat16>(y1), dm.S, dm.D, total);
}

void ltx2_ca_dual_modulate_from_temb_candidate(TensorView x,
                                               TensorView temb_scale_shift,
                                               TensorView scale_shift_table,
                                               double eps, TensorView y0,
                                               TensorView y1) {
  Dims dm = check_x(x);
  // Run on x's device (not necessarily the current device) for multi-GPU safety.
  const c10::cuda::CUDAGuard device_guard(static_cast<c10::DeviceIndex>(dm.dev));
  int64_t temb_seq = check_temb(temb_scale_shift, dm);
  TableInfo ti = check_table(scale_shift_table, dm);
  check_output(y0, dm, "y0");
  check_output(y1, dm, "y1");

  int64_t total = dm.B * dm.S * dm.D;
  if (total == 0) return;
  at::Tensor normed = at::rms_norm(as_tensor(x), {dm.D}, c10::optional<at::Tensor>{},
                                   c10::optional<double>(eps));
  cudaStream_t stream = at::cuda::getCurrentCUDAStream();
  const __nv_bfloat16* nm = reinterpret_cast<const __nv_bfloat16*>(normed.data_ptr());
  const __nv_bfloat16* tb = const_ptr<__nv_bfloat16>(temb_scale_shift);
  const void* table = static_cast<const void*>(const_ptr<char>(scale_shift_table));
  __nv_bfloat16* o0 = mut_ptr<__nv_bfloat16>(y0);
  __nv_bfloat16* o1 = mut_ptr<__nv_bfloat16>(y1);
  if (ti.f32) {
    ca_dual_modulate_kernel<true><<<grid_for(total), kThreads, 0, stream>>>(
        nm, tb, table, ti.s0, o0, o1, dm.S, dm.D, temb_seq, total);
  } else {
    ca_dual_modulate_kernel<false><<<grid_for(total), kThreads, 0, stream>>>(
        nm, tb, table, ti.s0, o0, o1, dm.S, dm.D, temb_seq, total);
  }
}

}  // namespace

TVM_FFI_DLL_EXPORT_TYPED_FUNC(ltx2_dual_modulate_candidate,
                              ltx2_dual_modulate_candidate);
TVM_FFI_DLL_EXPORT_TYPED_FUNC(ltx2_ca_dual_modulate_from_temb_candidate,
                              ltx2_ca_dual_modulate_from_temb_candidate);
