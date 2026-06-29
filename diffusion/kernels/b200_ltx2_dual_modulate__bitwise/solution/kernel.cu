// Optimized candidate for LTX2 dual modulation, bit-for-bit equal to the PyTorch
// eager baseline. Strategy: reuse ATen `rms_norm` for the (bit-identical)
// normalization, then a single fused CUDA kernel applies BOTH affines in one pass
// over `normed`, preserving PyTorch's per-operation bf16 rounding boundaries.
//
// The hot path is memory-bound, so the dominant traffic (reading `normed`, writing
// y0 and y1 -- all compact) is moved in 16-byte vectors (8 bf16 per thread). The
// per-element affine arithmetic stays scalar fp32-opmath with explicit bf16 rounding,
// so the output bits are identical to the scalar path (vectorization only widens the
// loads/stores, never the math). A scalar path is kept as a fallback for the rare
// case of a non-16-byte-aligned output buffer.
//
// Exposed through the same destination-passing TVM-FFI ABI as the baseline (inputs
// first, scalar `double eps`, output tensors last). Input validation/rejection is
// shared with the baseline via ltx2_dual_modulate_common.cuh so both sides reject
// identical inputs. The kernel runs on PyTorch's current CUDA stream for x's device
// (a device guard makes the raw launch honor x.device()).

#include "../ltx2_dual_modulate_common.cuh"

#include <c10/cuda/CUDAGuard.h>

#include <cstdint>

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

constexpr int kVec = 8;  // bf16 elements per 16-byte (int4) vector access

// Reproduce eager `y = normed * (1 + scale) + shift` with the three bf16
// materialization points PyTorch makes visible: each binary op runs in fp32 opmath
// and stores a bf16 (round-to-nearest-even). No FMA contraction, no single-shot
// fp32 collapse -- collapsing to one rounding can differ by >=1 bf16 ulp.
__device__ __forceinline__ __nv_bfloat16 affine_bf16(__nv_bfloat16 normed,
                                                     __nv_bfloat16 scale,
                                                     __nv_bfloat16 shift) {
  __nv_bfloat16 t = __float2bfloat16_rn(__fadd_rn(1.0f, __bfloat162float(scale)));
  __nv_bfloat16 p =
      __float2bfloat16_rn(__fmul_rn(__bfloat162float(normed), __bfloat162float(t)));
  return __float2bfloat16_rn(__fadd_rn(__bfloat162float(p), __bfloat162float(shift)));
}

// Convert a table element to the fp32 value PyTorch sees after `table.to(x.dtype)`:
// an fp32 table is rounded to bf16 FIRST (then back to fp32 for the add); a bf16
// table passes through unchanged.
__device__ __forceinline__ float table_value_f32(float v) {
  return __bfloat162float(__float2bfloat16_rn(v));
}
__device__ __forceinline__ float table_value_f32(__nv_bfloat16 v) {
  return __bfloat162float(v);
}

// scale/shift = bf16(fp32(table_bf16) + fp32(temb)), matching
// `(scale_shift_table.to(x.dtype) + temb)` exactly (table rounded to bf16 first).
template <typename TableT>
__device__ __forceinline__ __nv_bfloat16 combine_scale_shift(
    const TableT* __restrict__ table, int64_t toff,
    const __nv_bfloat16* __restrict__ temb, int64_t eoff) {
  return __float2bfloat16_rn(
      __fadd_rn(table_value_f32(table[toff]), __bfloat162float(temb[eoff])));
}

// ---- Explicit dual modulation. Each of scale0/shift0/scale1/shift1 has its own
// batch stride `sb` and sequence stride `ss` (ss == 0 broadcasts over S, covering the
// [B,D] and [B,1,D] layouts; the production [B,1,D] params are non-compact with
// sb == 4*D). normed and the two outputs are compact [B,S,D] (idx == row*D + d). ----

__device__ __forceinline__ void explicit_one(
    const __nv_bfloat16* __restrict__ scale0, const __nv_bfloat16* __restrict__ shift0,
    const __nv_bfloat16* __restrict__ scale1, const __nv_bfloat16* __restrict__ shift1,
    __nv_bfloat16 n, int64_t o_s0, int64_t o_h0, int64_t o_s1, int64_t o_h1,
    __nv_bfloat16& r0, __nv_bfloat16& r1) {
  r0 = affine_bf16(n, scale0[o_s0], shift0[o_h0]);
  r1 = affine_bf16(n, scale1[o_s1], shift1[o_h1]);
}

__global__ void explicit_affine_kernel_scalar(
    const __nv_bfloat16* __restrict__ normed,
    const __nv_bfloat16* __restrict__ scale0,
    const __nv_bfloat16* __restrict__ shift0,
    const __nv_bfloat16* __restrict__ scale1,
    const __nv_bfloat16* __restrict__ shift1,
    __nv_bfloat16* __restrict__ y0, __nv_bfloat16* __restrict__ y1, int64_t total,
    int64_t S, int64_t D, int64_t s0_sb, int64_t s0_ss, int64_t h0_sb,
    int64_t h0_ss, int64_t s1_sb, int64_t s1_ss, int64_t h1_sb, int64_t h1_ss) {
  const int64_t stride = static_cast<int64_t>(gridDim.x) * blockDim.x;
  for (int64_t idx = static_cast<int64_t>(blockIdx.x) * blockDim.x + threadIdx.x;
       idx < total; idx += stride) {
    const int64_t d = idx % D;
    const int64_t row = idx / D;
    const int64_t b = row / S;
    const int64_t s = row - b * S;
    explicit_one(scale0, shift0, scale1, shift1, normed[idx], b * s0_sb + s * s0_ss + d,
                 b * h0_sb + s * h0_ss + d, b * s1_sb + s * s1_ss + d,
                 b * h1_sb + s * h1_ss + d, y0[idx], y1[idx]);
  }
}

// Vectorized: one thread handles kVec contiguous columns of one row. normed and the
// outputs move as 16-byte int4 (8 bf16); params are read per element (contiguous in
// the row, and broadcast/cached for the production [B,1,D] layout).
__global__ void explicit_affine_kernel_vec(
    const __nv_bfloat16* __restrict__ normed,
    const __nv_bfloat16* __restrict__ scale0,
    const __nv_bfloat16* __restrict__ shift0,
    const __nv_bfloat16* __restrict__ scale1,
    const __nv_bfloat16* __restrict__ shift1,
    __nv_bfloat16* __restrict__ y0, __nv_bfloat16* __restrict__ y1, int64_t total_vec,
    int64_t S, int64_t D, int64_t s0_sb, int64_t s0_ss, int64_t h0_sb,
    int64_t h0_ss, int64_t s1_sb, int64_t s1_ss, int64_t h1_sb, int64_t h1_ss) {
  const int64_t stride = static_cast<int64_t>(gridDim.x) * blockDim.x;
  for (int64_t c = static_cast<int64_t>(blockIdx.x) * blockDim.x + threadIdx.x;
       c < total_vec; c += stride) {
    const int64_t base = c * kVec;
    const int64_t d = base % D;
    const int64_t row = base / D;
    const int64_t b = row / S;
    const int64_t s = row - b * S;
    const int64_t o_s0 = b * s0_sb + s * s0_ss + d;
    const int64_t o_h0 = b * h0_sb + s * h0_ss + d;
    const int64_t o_s1 = b * s1_sb + s * s1_ss + d;
    const int64_t o_h1 = b * h1_sb + s * h1_ss + d;
    int4 nv = *reinterpret_cast<const int4*>(normed + base);
    const __nv_bfloat16* n8 = reinterpret_cast<const __nv_bfloat16*>(&nv);
    int4 r0v, r1v;
    __nv_bfloat16* r0 = reinterpret_cast<__nv_bfloat16*>(&r0v);
    __nv_bfloat16* r1 = reinterpret_cast<__nv_bfloat16*>(&r1v);
#pragma unroll
    for (int i = 0; i < kVec; ++i) {
      explicit_one(scale0, shift0, scale1, shift1, n8[i], o_s0 + i, o_h0 + i,
                   o_s1 + i, o_h1 + i, r0[i], r1[i]);
    }
    *reinterpret_cast<int4*>(y0 + base) = r0v;
    *reinterpret_cast<int4*>(y1 + base) = r1v;
  }
}

// ---- Cross-attention dual modulation from a timestep embedding. scale/shift rows
// are derived inline from `scale_shift_table` ([4,D], row stride table_s0) and
// `temb_scale_shift` (compact [B,temb_seq,4,D]); temb_seq is 1 (broadcast over S) or
// S. Row order matches unbind(2): 0->scale0, 1->shift0, 2->scale1, 3->shift1. ----

template <typename TableT>
__device__ __forceinline__ void ca_one(const TableT* __restrict__ table,
                                       const __nv_bfloat16* __restrict__ temb,
                                       __nv_bfloat16 n, int64_t td, int64_t tb,
                                       int64_t table_s0, int64_t D, __nv_bfloat16& r0,
                                       __nv_bfloat16& r1) {
  const __nv_bfloat16 sc0 = combine_scale_shift(table, 0 * table_s0 + td, temb, tb + 0 * D);
  const __nv_bfloat16 sh0 = combine_scale_shift(table, 1 * table_s0 + td, temb, tb + 1 * D);
  const __nv_bfloat16 sc1 = combine_scale_shift(table, 2 * table_s0 + td, temb, tb + 2 * D);
  const __nv_bfloat16 sh1 = combine_scale_shift(table, 3 * table_s0 + td, temb, tb + 3 * D);
  r0 = affine_bf16(n, sc0, sh0);
  r1 = affine_bf16(n, sc1, sh1);
}

template <typename TableT>
__global__ void ca_affine_kernel_scalar(const __nv_bfloat16* __restrict__ normed,
                                        const __nv_bfloat16* __restrict__ temb,
                                        const TableT* __restrict__ table,
                                        __nv_bfloat16* __restrict__ y0,
                                        __nv_bfloat16* __restrict__ y1, int64_t total,
                                        int64_t S, int64_t D, int64_t temb_seq,
                                        int64_t table_s0) {
  const int64_t row_elems = 4 * D;
  const int64_t stride = static_cast<int64_t>(gridDim.x) * blockDim.x;
  for (int64_t idx = static_cast<int64_t>(blockIdx.x) * blockDim.x + threadIdx.x;
       idx < total; idx += stride) {
    const int64_t d = idx % D;
    const int64_t row = idx / D;
    const int64_t b = row / S;
    const int64_t s = row - b * S;
    const int64_t ts = (temb_seq == 1) ? 0 : s;
    const int64_t tb = b * (temb_seq * row_elems) + ts * row_elems + d;
    ca_one(table, temb, normed[idx], d, tb, table_s0, D, y0[idx], y1[idx]);
  }
}

template <typename TableT>
__global__ void ca_affine_kernel_vec(const __nv_bfloat16* __restrict__ normed,
                                     const __nv_bfloat16* __restrict__ temb,
                                     const TableT* __restrict__ table,
                                     __nv_bfloat16* __restrict__ y0,
                                     __nv_bfloat16* __restrict__ y1, int64_t total_vec,
                                     int64_t S, int64_t D, int64_t temb_seq,
                                     int64_t table_s0) {
  const int64_t row_elems = 4 * D;
  const int64_t stride = static_cast<int64_t>(gridDim.x) * blockDim.x;
  for (int64_t c = static_cast<int64_t>(blockIdx.x) * blockDim.x + threadIdx.x;
       c < total_vec; c += stride) {
    const int64_t base = c * kVec;
    const int64_t d = base % D;
    const int64_t row = base / D;
    const int64_t b = row / S;
    const int64_t s = row - b * S;
    const int64_t ts = (temb_seq == 1) ? 0 : s;
    const int64_t tb = b * (temb_seq * row_elems) + ts * row_elems + d;
    int4 nv = *reinterpret_cast<const int4*>(normed + base);
    const __nv_bfloat16* n8 = reinterpret_cast<const __nv_bfloat16*>(&nv);
    int4 r0v, r1v;
    __nv_bfloat16* r0 = reinterpret_cast<__nv_bfloat16*>(&r0v);
    __nv_bfloat16* r1 = reinterpret_cast<__nv_bfloat16*>(&r1v);
#pragma unroll
    for (int i = 0; i < kVec; ++i) {
      ca_one(table, temb, n8[i], d + i, tb + i, table_s0, D, r0[i], r1[i]);
    }
    *reinterpret_cast<int4*>(y0 + base) = r0v;
    *reinterpret_cast<int4*>(y1 + base) = r1v;
  }
}

inline void launch_dims(int64_t n, int* grid, int* block) {
  *block = 256;
  int64_t want = (n + *block - 1) / *block;
  const int64_t cap = 131072;  // grid-stride loop covers any remainder
  *grid = static_cast<int>(want < 1 ? 1 : (want < cap ? want : cap));
}

const __nv_bfloat16* bf16_ptr(const at::Tensor& t) {
  return reinterpret_cast<const __nv_bfloat16*>(t.data_ptr<at::BFloat16>());
}

// True when the dominant compact buffers can be moved as 16-byte vectors. D is a
// multiple of 256 (so total is a multiple of kVec and row boundaries align), so only
// the base-pointer alignment of normed/y0/y1 needs checking.
inline bool vec_ok(const void* a, const void* b, const void* c) {
  auto al = [](const void* p) {
    return (reinterpret_cast<std::uintptr_t>(p) & (kVec * sizeof(__nv_bfloat16) - 1)) == 0;
  };
  return al(a) && al(b) && al(c);
}

void ltx2_dual_modulate_candidate(TensorView x, TensorView scale0, TensorView shift0,
                                  TensorView scale1, TensorView shift1, double eps,
                                  TensorView y0, TensorView y1) {
  Dims dm = check_x(x);
  ParamStrides ps0 = check_explicit_param(scale0, dm, "scale0");
  ParamStrides ph0 = check_explicit_param(shift0, dm, "shift0");
  ParamStrides ps1 = check_explicit_param(scale1, dm, "scale1");
  ParamStrides ph1 = check_explicit_param(shift1, dm, "shift1");
  check_output(y0, dm, "y0");
  check_output(y1, dm, "y1");

  const c10::cuda::CUDAGuard device_guard(static_cast<c10::DeviceIndex>(dm.dev));
  at::Tensor normed =
      at::rms_norm(as_tensor(x), {dm.D}, c10::optional<at::Tensor>{},
                   c10::optional<double>(eps))
          .contiguous();

  const int64_t total = dm.B * dm.S * dm.D;
  if (total == 0) return;
  const __nv_bfloat16* n = bf16_ptr(normed);
  const __nv_bfloat16* s0 = const_ptr<__nv_bfloat16>(scale0);
  const __nv_bfloat16* h0 = const_ptr<__nv_bfloat16>(shift0);
  const __nv_bfloat16* s1 = const_ptr<__nv_bfloat16>(scale1);
  const __nv_bfloat16* h1 = const_ptr<__nv_bfloat16>(shift1);
  __nv_bfloat16* o0 = mut_ptr<__nv_bfloat16>(y0);
  __nv_bfloat16* o1 = mut_ptr<__nv_bfloat16>(y1);
  cudaStream_t stream = at::cuda::getCurrentCUDAStream(dm.dev);
  int grid, block;
  if (vec_ok(n, o0, o1)) {
    launch_dims(total / kVec, &grid, &block);
    explicit_affine_kernel_vec<<<grid, block, 0, stream>>>(
        n, s0, h0, s1, h1, o0, o1, total / kVec, dm.S, dm.D, ps0.sb, ps0.ss, ph0.sb,
        ph0.ss, ps1.sb, ps1.ss, ph1.sb, ph1.ss);
  } else {
    launch_dims(total, &grid, &block);
    explicit_affine_kernel_scalar<<<grid, block, 0, stream>>>(
        n, s0, h0, s1, h1, o0, o1, total, dm.S, dm.D, ps0.sb, ps0.ss, ph0.sb, ph0.ss,
        ps1.sb, ps1.ss, ph1.sb, ph1.ss);
  }
  C10_CUDA_KERNEL_LAUNCH_CHECK();
}

void ltx2_ca_dual_modulate_from_temb_candidate(TensorView x,
                                               TensorView temb_scale_shift,
                                               TensorView scale_shift_table,
                                               double eps, TensorView y0,
                                               TensorView y1) {
  Dims dm = check_x(x);
  int64_t temb_seq = check_temb(temb_scale_shift, dm);
  TableInfo ti = check_table(scale_shift_table, dm);
  check_output(y0, dm, "y0");
  check_output(y1, dm, "y1");

  const c10::cuda::CUDAGuard device_guard(static_cast<c10::DeviceIndex>(dm.dev));
  at::Tensor normed =
      at::rms_norm(as_tensor(x), {dm.D}, c10::optional<at::Tensor>{},
                   c10::optional<double>(eps))
          .contiguous();

  const int64_t total = dm.B * dm.S * dm.D;
  if (total == 0) return;
  const __nv_bfloat16* n = bf16_ptr(normed);
  const __nv_bfloat16* temb = const_ptr<__nv_bfloat16>(temb_scale_shift);
  __nv_bfloat16* o0 = mut_ptr<__nv_bfloat16>(y0);
  __nv_bfloat16* o1 = mut_ptr<__nv_bfloat16>(y1);
  cudaStream_t stream = at::cuda::getCurrentCUDAStream(dm.dev);
  const bool vec = vec_ok(n, o0, o1);
  int grid, block;
  launch_dims(vec ? total / kVec : total, &grid, &block);
  if (ti.f32) {
    const float* tbl = const_ptr<float>(scale_shift_table);
    if (vec)
      ca_affine_kernel_vec<float><<<grid, block, 0, stream>>>(
          n, temb, tbl, o0, o1, total / kVec, dm.S, dm.D, temb_seq, ti.s0);
    else
      ca_affine_kernel_scalar<float><<<grid, block, 0, stream>>>(
          n, temb, tbl, o0, o1, total, dm.S, dm.D, temb_seq, ti.s0);
  } else {
    const __nv_bfloat16* tbl = const_ptr<__nv_bfloat16>(scale_shift_table);
    if (vec)
      ca_affine_kernel_vec<__nv_bfloat16><<<grid, block, 0, stream>>>(
          n, temb, tbl, o0, o1, total / kVec, dm.S, dm.D, temb_seq, ti.s0);
    else
      ca_affine_kernel_scalar<__nv_bfloat16><<<grid, block, 0, stream>>>(
          n, temb, tbl, o0, o1, total, dm.S, dm.D, temb_seq, ti.s0);
  }
  C10_CUDA_KERNEL_LAUNCH_CHECK();
}

}  // namespace

TVM_FFI_DLL_EXPORT_TYPED_FUNC(ltx2_dual_modulate_candidate,
                              ltx2_dual_modulate_candidate);
TVM_FFI_DLL_EXPORT_TYPED_FUNC(ltx2_ca_dual_modulate_from_temb_candidate,
                              ltx2_ca_dual_modulate_from_temb_candidate);
