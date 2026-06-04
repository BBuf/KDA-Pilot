// Candidate CUDA implementation of the SGLang diffusion scale/shift entry
// points for B200, exposed through a destination-passing tvm-ffi ABI that
// mirrors baseline/binding.py (inputs, scalars, output tensors last; launches
// on torch's current CUDA stream).
//
// Reference semantics: baseline/scale_shift_triton.py (SGLang main
// @ 1332540). Three exports:
//   fuse_scale_shift(x, scale, shift, scale_constant, output)
//   fuse_layernorm_scale_shift_gate_select01(x, weight?, bias?, scale0,
//       shift0, gate0, scale1, shift1, gate1, index, eps, output, gate_out)
//   fuse_residual_layernorm_scale_shift_gate_select01(x, residual,
//       residual_gate, weight?, bias?, ..., index, eps, output, residual_out,
//       gate_out)
//
// Math notes kept aligned with the reference:
//  - scale/shift arithmetic runs in fp32 and stores back in x's dtype.
//  - LayerNorm statistics are fp32 two-pass (mean, then centered variance),
//    matching the reference's compute order class.
//  - The residual variant normalizes the fp32 pre-downcast residual values;
//    residual_out stores their downcast copies.
//  - gate_out is a raw-dtype pass-through of the selected gate row (no fp32
//    round trip).

#include <ATen/cuda/CUDAContext.h>

#include <cuda_bf16.h>
#include <cuda_fp16.h>

#include <dlpack/dlpack.h>
#include <tvm/ffi/container/tensor.h>
#if __has_include(<tvm/ffi/function.h>)
#include <tvm/ffi/function.h>
#endif

#include <algorithm>
#include <cstdint>
#include <cstring>
#include <sstream>
#include <stdexcept>

namespace {

using tvm::ffi::Optional;
using tvm::ffi::TensorView;

// Host-side failures throw a C++ exception; the tvm-ffi boundary converts it
// into a Python error (same pattern as the production jit kernels).
template <typename... Args>
[[noreturn]] void cand_fail(Args&&... args) {
  std::ostringstream oss;
  (oss << ... << args);
  throw std::runtime_error(oss.str());
}

#define CAND_CHECK(cond, ...)  \
  do {                         \
    if (!(cond)) {             \
      cand_fail(__VA_ARGS__);  \
    }                          \
  } while (0)

// ---------------------------------------------------------------------------
// dtype helpers
// ---------------------------------------------------------------------------

inline bool dtype_is(DLDataType d, uint8_t code, uint8_t bits) {
  return d.code == code && d.bits == bits && d.lanes == 1;
}
inline bool is_bf16(DLDataType d) { return dtype_is(d, kDLBfloat, 16); }
inline bool is_f16(DLDataType d) { return dtype_is(d, kDLFloat, 16); }
inline bool is_f32(DLDataType d) { return dtype_is(d, kDLFloat, 32); }
inline bool is_i32(DLDataType d) { return dtype_is(d, kDLInt, 32); }
inline bool is_i64(DLDataType d) { return dtype_is(d, kDLInt, 64); }
inline bool same_dtype(DLDataType a, DLDataType b) {
  return a.code == b.code && a.bits == b.bits && a.lanes == b.lanes;
}

__device__ __forceinline__ float to_f(__nv_bfloat16 v) { return __bfloat162float(v); }
__device__ __forceinline__ float to_f(__half v) { return __half2float(v); }
__device__ __forceinline__ float to_f(float v) { return v; }

template <typename T>
__device__ __forceinline__ T from_f(float v);
template <>
__device__ __forceinline__ __nv_bfloat16 from_f<__nv_bfloat16>(float v) { return __float2bfloat16(v); }
template <>
__device__ __forceinline__ __half from_f<__half>(float v) { return __float2half(v); }
template <>
__device__ __forceinline__ float from_f<float>(float v) { return v; }

// ---------------------------------------------------------------------------
// tensor view helpers
// ---------------------------------------------------------------------------

inline int64_t numel_of(const TensorView& t) {
  int64_t n = 1;
  for (int i = 0; i < t.ndim(); ++i) n *= t.shape(i);
  return n;
}

inline bool tensor_is_contiguous(const TensorView& t) {
  int64_t expect = 1;
  for (int i = t.ndim() - 1; i >= 0; --i) {
    if (t.shape(i) == 1) continue;  // stride is free on size-1 dims
    if (t.stride(i) != expect) return false;
    expect *= t.shape(i);
  }
  return true;
}

inline void check_cuda_tensor(const TensorView& t, const char* name) {
  CAND_CHECK(t.device().device_type == kDLCUDA, name, " must be a CUDA tensor");
}

inline void check_output_like(const TensorView& out, const TensorView& x, const char* name) {
  CAND_CHECK(out.ndim() == x.ndim(), name, " rank must match x");
  for (int i = 0; i < x.ndim(); ++i) {
    CAND_CHECK(out.shape(i) == x.shape(i), name, " shape must match x");
  }
  CAND_CHECK(same_dtype(out.dtype(), x.dtype()), name, " dtype must match x");
  CAND_CHECK(tensor_is_contiguous(out), name, " must be contiguous");
}

// Broadcast strides over [B, L, C] (0-stride on broadcast dims), mirroring the
// upstream wrapper's reshape/expand normalization for 0D/1D(1)/2D/3D operands.
struct Blc {
  const void* ptr = nullptr;
  int64_t sb = 0, sl = 0, sc = 0;
  bool scalar = false;
};

inline Blc normalize_blc(const TensorView& t, int64_t B, int64_t L, int64_t C, const char* name) {
  Blc r;
  r.ptr = t.data_ptr();
  const int nd = t.ndim();
  if (nd == 0 || (nd == 1 && numel_of(t) == 1)) {
    r.scalar = true;
    return r;
  }
  if (nd == 2) {
    CAND_CHECK(t.shape(0) == B || t.shape(0) == 1, name, " dim0 must be 1 or B");
    CAND_CHECK(t.shape(1) == C, name, " dim1 must equal C");
    r.sb = (t.shape(0) == 1) ? 0 : t.stride(0);
    r.sl = 0;
    r.sc = t.stride(1);
    return r;
  }
  if (nd == 3) {
    const int64_t want[3] = {B, L, C};
    int64_t st[3];
    for (int i = 0; i < 3; ++i) {
      CAND_CHECK(t.shape(i) == want[i] || t.shape(i) == 1,
                 name, " dim", i, " must be 1 or match x");
      st[i] = (t.shape(i) == 1) ? 0 : t.stride(i);
    }
    r.sb = st[0];
    r.sl = st[1];
    r.sc = st[2];
    return r;
  }
  cand_fail(name, " must be 0D/1D(1)/2D/3D or 4D");
  return r;  // unreachable
}

inline float read_scalar_as_float(const void* ptr, DLDataType dtype, cudaStream_t stream) {
  unsigned char bytes[8] = {0};
  const size_t nbytes = dtype.bits / 8;
  cudaMemcpyAsync(bytes, ptr, nbytes, cudaMemcpyDeviceToHost, stream);
  cudaStreamSynchronize(stream);
  if (is_f32(dtype)) {
    float v;
    memcpy(&v, bytes, 4);
    return v;
  }
  if (is_bf16(dtype)) {
    uint32_t hi;
    uint16_t raw;
    memcpy(&raw, bytes, 2);
    hi = uint32_t(raw) << 16;
    float v;
    memcpy(&v, &hi, 4);
    return v;
  }
  if (is_f16(dtype)) {
    __half h;
    memcpy(&h, bytes, 2);
    return __half2float(h);
  }
  cand_fail("unsupported scalar dtype");
  return 0.0f;
}

constexpr int kEwThreads = 256;
constexpr int64_t kEwMaxBlocks = 16384;

inline int ew_blocks(int64_t total) {
  const int64_t b = (total + kEwThreads - 1) / kEwThreads;
  return static_cast<int>(std::min<int64_t>(b, kEwMaxBlocks));
}

// ---------------------------------------------------------------------------
// entry point 1: fuse_scale_shift
// ---------------------------------------------------------------------------

template <typename XT, typename ST>
__global__ void scale_shift_strided_kernel(
    const XT* __restrict__ x, const ST* __restrict__ scale, const ST* __restrict__ shift,
    XT* __restrict__ out, float scale_constant,
    int64_t total, int64_t seq_len, int64_t channels,
    int64_t s_sb, int64_t s_sl, int64_t s_sc,
    int64_t h_sb, int64_t h_sl, int64_t h_sc) {
  const int64_t step = static_cast<int64_t>(gridDim.x) * blockDim.x;
  for (int64_t i = static_cast<int64_t>(blockIdx.x) * blockDim.x + threadIdx.x; i < total;
       i += step) {
    const int64_t c = i % channels;
    const int64_t t = i / channels;
    const int64_t l = t % seq_len;
    const int64_t b = t / seq_len;
    const float xv = to_f(x[i]);
    const float sv = to_f(scale[b * s_sb + l * s_sl + c * s_sc]);
    const float hv = to_f(shift[b * h_sb + l * h_sl + c * h_sc]);
    out[i] = from_f<XT>(fmaf(xv, scale_constant + sv, hv));
  }
}

// 4D per-frame layout: scale [B, F, 1, C] (read strided, no compaction copy);
// shift per-token [B, L, C].
template <typename XT, typename ST>
__global__ void scale_shift_frame_kernel(
    const XT* __restrict__ x, const ST* __restrict__ scale, const ST* __restrict__ shift,
    XT* __restrict__ out, float scale_constant,
    int64_t total, int64_t seq_len, int64_t channels, int64_t frame_seqlen,
    int64_t s_sb, int64_t s_sf, int64_t s_sc,
    int64_t h_sb, int64_t h_sl, int64_t h_sc) {
  const int64_t step = static_cast<int64_t>(gridDim.x) * blockDim.x;
  for (int64_t i = static_cast<int64_t>(blockIdx.x) * blockDim.x + threadIdx.x; i < total;
       i += step) {
    const int64_t c = i % channels;
    const int64_t t = i / channels;
    const int64_t l = t % seq_len;
    const int64_t b = t / seq_len;
    const int64_t f = l / frame_seqlen;
    const float xv = to_f(x[i]);
    const float sv = to_f(scale[b * s_sb + f * s_sf + c * s_sc]);
    const float hv = to_f(shift[b * h_sb + l * h_sl + c * h_sc]);
    out[i] = from_f<XT>(fmaf(xv, scale_constant + sv, hv));
  }
}

template <typename XT, typename ST>
void launch_fuse_scale_shift(const TensorView& x, const TensorView& scale,
                             const TensorView& shift, double scale_constant,
                             const TensorView& output, cudaStream_t stream) {
  const int64_t B = x.shape(0), L = x.shape(1), C = x.shape(2);
  const int64_t total = B * L * C;
  if (total == 0) return;

  const XT* xp = static_cast<const XT*>(x.data_ptr());
  XT* op = static_cast<XT*>(output.data_ptr());
  const float sc = static_cast<float>(scale_constant);

  if (scale.ndim() == 4) {
    // scale [B, F, 1, C]; shift must be a full per-token [B, L, C] tensor.
    CAND_CHECK(scale.shape(0) == B && scale.shape(2) == 1 && scale.shape(3) == C,
               "4D scale must be [B, F, 1, C]");
    const int64_t F = scale.shape(1);
    CAND_CHECK(F > 0 && L % F == 0, "seq_len must be divisible by num_frames for 4D scale/shift");
    CAND_CHECK(shift.ndim() == 3 && shift.shape(0) == B && shift.shape(1) == L && shift.shape(2) == C,
               "shift must be [B, L, C] for the 4D scale path");
    scale_shift_frame_kernel<XT, ST><<<ew_blocks(total), kEwThreads, 0, stream>>>(
        xp, static_cast<const ST*>(scale.data_ptr()), static_cast<const ST*>(shift.data_ptr()),
        op, sc, total, L, C, L / F,
        scale.stride(0), scale.stride(1), scale.stride(3),
        shift.stride(0), shift.stride(1), shift.stride(2));
    return;
  }

  const Blc s = normalize_blc(scale, B, L, C, "scale");
  const Blc h = normalize_blc(shift, B, L, C, "shift");

  if (s.scalar && h.scalar) {
    // Reference fast path: when both scalars are zero the reference copies x
    // through unchanged (regardless of scale_constant); match it exactly.
    const float sv = read_scalar_as_float(s.ptr, scale.dtype(), stream);
    const float hv = read_scalar_as_float(h.ptr, shift.dtype(), stream);
    if (sv == 0.0f && hv == 0.0f) {
      cudaMemcpyAsync(op, xp, total * sizeof(XT), cudaMemcpyDeviceToDevice, stream);
      return;
    }
  }

  scale_shift_strided_kernel<XT, ST><<<ew_blocks(total), kEwThreads, 0, stream>>>(
      xp, static_cast<const ST*>(s.ptr), static_cast<const ST*>(h.ptr), op, sc,
      total, L, C, s.sb, s.sl, s.sc, h.sb, h.sl, h.sc);
}

void fuse_scale_shift(TensorView x, TensorView scale, TensorView shift, double scale_constant,
                      TensorView output) {
  check_cuda_tensor(x, "x");
  check_cuda_tensor(scale, "scale");
  check_cuda_tensor(shift, "shift");
  check_cuda_tensor(output, "output");
  CAND_CHECK(x.ndim() == 3, "x must be [B, L, C]");
  CAND_CHECK(tensor_is_contiguous(x), "x must be contiguous");
  check_output_like(output, x, "output");
  CAND_CHECK(same_dtype(scale.dtype(), shift.dtype()), "scale and shift dtypes must match");

  cudaStream_t stream = at::cuda::getCurrentCUDAStream();
  const DLDataType xt = x.dtype(), st = scale.dtype();

  if (is_bf16(xt) && is_bf16(st)) {
    launch_fuse_scale_shift<__nv_bfloat16, __nv_bfloat16>(x, scale, shift, scale_constant, output, stream);
  } else if (is_bf16(xt) && is_f32(st)) {
    launch_fuse_scale_shift<__nv_bfloat16, float>(x, scale, shift, scale_constant, output, stream);
  } else if (is_f16(xt) && is_f16(st)) {
    launch_fuse_scale_shift<__half, __half>(x, scale, shift, scale_constant, output, stream);
  } else if (is_f16(xt) && is_f32(st)) {
    launch_fuse_scale_shift<__half, float>(x, scale, shift, scale_constant, output, stream);
  } else if (is_f32(xt) && is_f32(st)) {
    launch_fuse_scale_shift<float, float>(x, scale, shift, scale_constant, output, stream);
  } else {
    cand_fail("unsupported dtype combination for fuse_scale_shift");
  }
}

// ---------------------------------------------------------------------------
// entry points 2/3: LayerNorm + select01 modulation (+ residual)
// ---------------------------------------------------------------------------

constexpr int kLnThreads = 256;

__device__ __forceinline__ float block_reduce_sum(float v, float* shared) {
  const unsigned full = 0xffffffffu;  // blockDim.x is a multiple of 32
#pragma unroll
  for (int off = 16; off > 0; off >>= 1) v += __shfl_down_sync(full, v, off);
  const int lane = threadIdx.x & 31;
  const int warp = threadIdx.x >> 5;
  if (lane == 0) shared[warp] = v;
  __syncthreads();
  const int nwarp = blockDim.x >> 5;
  v = (threadIdx.x < nwarp) ? shared[threadIdx.x] : 0.0f;
  if (warp == 0) {
#pragma unroll
    for (int off = 16; off > 0; off >>= 1) v += __shfl_down_sync(full, v, off);
    if (lane == 0) shared[0] = v;
  }
  __syncthreads();
  const float out = shared[0];
  __syncthreads();  // shared[] is reused by the next reduction
  return out;
}

struct ModStrides {
  int64_t s_sb, s_sc, h_sb, h_sc, g_sb, g_sc;
};

template <typename XT, typename IT>
__global__ void ln_select01_kernel(
    const XT* __restrict__ x,
    const XT* __restrict__ weight, const XT* __restrict__ bias,  // nullable
    const XT* __restrict__ scale0, const XT* __restrict__ shift0, const XT* __restrict__ gate0,
    const XT* __restrict__ scale1, const XT* __restrict__ shift1, const XT* __restrict__ gate1,
    const IT* __restrict__ index,
    XT* __restrict__ out, XT* __restrict__ gate_out,
    float eps, int64_t seq_len, int64_t channels,
    ModStrides m0, ModStrides m1, int64_t idx_sb, int64_t idx_sl) {
  __shared__ float red[32];
  const int64_t row = blockIdx.x;
  const int64_t b = row / seq_len;
  const int64_t l = row % seq_len;
  const XT* xr = x + row * channels;

  float sum = 0.0f;
  for (int64_t c = threadIdx.x; c < channels; c += blockDim.x) sum += to_f(xr[c]);
  const float mean = block_reduce_sum(sum, red) / channels;

  float vsum = 0.0f;
  for (int64_t c = threadIdx.x; c < channels; c += blockDim.x) {
    const float d = to_f(xr[c]) - mean;
    vsum += d * d;
  }
  const float var = block_reduce_sum(vsum, red) / channels;
  const float rstd = rsqrtf(var + eps);

  const bool sel = index[b * idx_sb + l * idx_sl] != IT(0);
  const XT* s = sel ? scale1 : scale0;
  const XT* h = sel ? shift1 : shift0;
  const XT* g = sel ? gate1 : gate0;
  const ModStrides m = sel ? m1 : m0;

  XT* outr = out + row * channels;
  XT* gr = gate_out + row * channels;
  for (int64_t c = threadIdx.x; c < channels; c += blockDim.x) {
    float xh = (to_f(xr[c]) - mean) * rstd;
    if (weight != nullptr) xh *= to_f(weight[c]);
    if (bias != nullptr) xh += to_f(bias[c]);
    const float sv = to_f(s[b * m.s_sb + c * m.s_sc]);
    const float hv = to_f(h[b * m.h_sb + c * m.h_sc]);
    outr[c] = from_f<XT>(fmaf(xh, 1.0f + sv, hv));
    gr[c] = g[b * m.g_sb + c * m.g_sc];
  }
}

template <typename XT, typename IT>
__global__ void residual_ln_select01_kernel(
    const XT* __restrict__ x, const XT* __restrict__ residual, const XT* __restrict__ residual_gate,
    const XT* __restrict__ weight, const XT* __restrict__ bias,  // nullable
    const XT* __restrict__ scale0, const XT* __restrict__ shift0, const XT* __restrict__ gate0,
    const XT* __restrict__ scale1, const XT* __restrict__ shift1, const XT* __restrict__ gate1,
    const IT* __restrict__ index,
    XT* __restrict__ out, XT* __restrict__ residual_out, XT* __restrict__ gate_out,
    float eps, int64_t seq_len, int64_t channels,
    ModStrides m0, ModStrides m1, int64_t idx_sb, int64_t idx_sl) {
  __shared__ float red[32];
  const int64_t row = blockIdx.x;
  const int64_t b = row / seq_len;
  const int64_t l = row % seq_len;
  const XT* xr = x + row * channels;
  const XT* rr = residual + row * channels;
  const XT* rgr = residual_gate + row * channels;
  XT* ror = residual_out + row * channels;

  // The fp32 residual expression r = residual + residual_gate * x is the
  // LayerNorm input; residual_out only stores its downcast copy. Recomputing
  // r per pass is deterministic (identical fp32 instruction sequence).
  float sum = 0.0f;
  for (int64_t c = threadIdx.x; c < channels; c += blockDim.x) {
    const float r = fmaf(to_f(rgr[c]), to_f(xr[c]), to_f(rr[c]));
    ror[c] = from_f<XT>(r);
    sum += r;
  }
  const float mean = block_reduce_sum(sum, red) / channels;

  float vsum = 0.0f;
  for (int64_t c = threadIdx.x; c < channels; c += blockDim.x) {
    const float r = fmaf(to_f(rgr[c]), to_f(xr[c]), to_f(rr[c]));
    const float d = r - mean;
    vsum += d * d;
  }
  const float var = block_reduce_sum(vsum, red) / channels;
  const float rstd = rsqrtf(var + eps);

  const bool sel = index[b * idx_sb + l * idx_sl] != IT(0);
  const XT* s = sel ? scale1 : scale0;
  const XT* h = sel ? shift1 : shift0;
  const XT* g = sel ? gate1 : gate0;
  const ModStrides m = sel ? m1 : m0;

  XT* outr = out + row * channels;
  XT* gr = gate_out + row * channels;
  for (int64_t c = threadIdx.x; c < channels; c += blockDim.x) {
    const float r = fmaf(to_f(rgr[c]), to_f(xr[c]), to_f(rr[c]));
    float xh = (r - mean) * rstd;
    if (weight != nullptr) xh *= to_f(weight[c]);
    if (bias != nullptr) xh += to_f(bias[c]);
    const float sv = to_f(s[b * m.s_sb + c * m.s_sc]);
    const float hv = to_f(h[b * m.h_sb + c * m.h_sc]);
    outr[c] = from_f<XT>(fmaf(xh, 1.0f + sv, hv));
    gr[c] = g[b * m.g_sb + c * m.g_sc];
  }
}

struct GatedArgs {
  int64_t B, L, C;
  const void* weight = nullptr;
  const void* bias = nullptr;
  ModStrides m0, m1;
  int64_t idx_sb, idx_sl;
};

inline void check_mod_tensor(const TensorView& t, int64_t B, int64_t C, DLDataType want,
                             const char* name) {
  CAND_CHECK(t.ndim() == 2, "scale0/shift0/gate0/scale1/shift1/gate1 must be 2D [B, C]");
  CAND_CHECK(t.shape(0) == B && t.shape(1) == C, name, " must be [B, C]");
  CAND_CHECK(same_dtype(t.dtype(), want), name, " dtype must match x");
}

inline GatedArgs validate_gated_common(
    const TensorView& x, const Optional<TensorView>& weight, const Optional<TensorView>& bias,
    const TensorView& scale0, const TensorView& shift0, const TensorView& gate0,
    const TensorView& scale1, const TensorView& shift1, const TensorView& gate1,
    const TensorView& index) {
  check_cuda_tensor(x, "x");
  CAND_CHECK(x.ndim() == 3, "x must be [B, L, C]");
  CAND_CHECK(tensor_is_contiguous(x), "x must be contiguous");
  GatedArgs a;
  a.B = x.shape(0);
  a.L = x.shape(1);
  a.C = x.shape(2);
  const DLDataType xt = x.dtype();
  check_mod_tensor(scale0, a.B, a.C, xt, "scale0");
  check_mod_tensor(shift0, a.B, a.C, xt, "shift0");
  check_mod_tensor(gate0, a.B, a.C, xt, "gate0");
  check_mod_tensor(scale1, a.B, a.C, xt, "scale1");
  check_mod_tensor(shift1, a.B, a.C, xt, "shift1");
  check_mod_tensor(gate1, a.B, a.C, xt, "gate1");
  CAND_CHECK(index.ndim() == 2, "index must be 2D [B, L]");
  CAND_CHECK(index.shape(0) == a.B && index.shape(1) == a.L, "index must be [B, L]");
  CAND_CHECK(is_i32(index.dtype()) || is_i64(index.dtype()), "index must be int32 or int64");
  if (weight.has_value()) {
    const TensorView& w = weight.value();
    CAND_CHECK(w.ndim() == 1 && w.shape(0) == a.C, "weight must be 1D [C]");
    CAND_CHECK(same_dtype(w.dtype(), xt), "weight dtype must match x");
    CAND_CHECK(tensor_is_contiguous(w), "weight must be contiguous");
    a.weight = w.data_ptr();
  }
  if (bias.has_value()) {
    const TensorView& bv = bias.value();
    CAND_CHECK(bv.ndim() == 1 && bv.shape(0) == a.C, "bias must be 1D [C]");
    CAND_CHECK(same_dtype(bv.dtype(), xt), "bias dtype must match x");
    CAND_CHECK(tensor_is_contiguous(bv), "bias must be contiguous");
    a.bias = bv.data_ptr();
  }
  a.m0 = ModStrides{scale0.stride(0), scale0.stride(1), shift0.stride(0), shift0.stride(1),
                    gate0.stride(0), gate0.stride(1)};
  a.m1 = ModStrides{scale1.stride(0), scale1.stride(1), shift1.stride(0), shift1.stride(1),
                    gate1.stride(0), gate1.stride(1)};
  a.idx_sb = index.stride(0);
  a.idx_sl = index.stride(1);
  return a;
}

void fuse_layernorm_scale_shift_gate_select01(
    TensorView x, Optional<TensorView> weight, Optional<TensorView> bias,
    TensorView scale0, TensorView shift0, TensorView gate0,
    TensorView scale1, TensorView shift1, TensorView gate1,
    TensorView index, double eps, TensorView output, TensorView gate_out) {
  const GatedArgs a = validate_gated_common(x, weight, bias, scale0, shift0, gate0,
                                            scale1, shift1, gate1, index);
  check_output_like(output, x, "output");
  check_output_like(gate_out, x, "gate_out");
  const int64_t rows = a.B * a.L;
  if (rows == 0 || a.C == 0) return;

  cudaStream_t stream = at::cuda::getCurrentCUDAStream();
  const DLDataType xt = x.dtype();
  const bool idx64 = is_i64(index.dtype());

#define LN_LAUNCH(XT, IT)                                                                  \
  ln_select01_kernel<XT, IT><<<static_cast<unsigned>(rows), kLnThreads, 0, stream>>>(      \
      static_cast<const XT*>(x.data_ptr()), static_cast<const XT*>(a.weight),              \
      static_cast<const XT*>(a.bias), static_cast<const XT*>(scale0.data_ptr()),           \
      static_cast<const XT*>(shift0.data_ptr()), static_cast<const XT*>(gate0.data_ptr()), \
      static_cast<const XT*>(scale1.data_ptr()), static_cast<const XT*>(shift1.data_ptr()),\
      static_cast<const XT*>(gate1.data_ptr()), static_cast<const IT*>(index.data_ptr()),  \
      static_cast<XT*>(output.data_ptr()), static_cast<XT*>(gate_out.data_ptr()),          \
      static_cast<float>(eps), a.L, a.C, a.m0, a.m1, a.idx_sb, a.idx_sl)

  if (is_bf16(xt)) {
    idx64 ? LN_LAUNCH(__nv_bfloat16, int64_t) : LN_LAUNCH(__nv_bfloat16, int32_t);
  } else if (is_f16(xt)) {
    idx64 ? LN_LAUNCH(__half, int64_t) : LN_LAUNCH(__half, int32_t);
  } else if (is_f32(xt)) {
    idx64 ? LN_LAUNCH(float, int64_t) : LN_LAUNCH(float, int32_t);
  } else {
    cand_fail("unsupported x dtype");
  }
#undef LN_LAUNCH
}

void fuse_residual_layernorm_scale_shift_gate_select01(
    TensorView x, TensorView residual, TensorView residual_gate,
    Optional<TensorView> weight, Optional<TensorView> bias,
    TensorView scale0, TensorView shift0, TensorView gate0,
    TensorView scale1, TensorView shift1, TensorView gate1,
    TensorView index, double eps, TensorView output, TensorView residual_out,
    TensorView gate_out) {
  const GatedArgs a = validate_gated_common(x, weight, bias, scale0, shift0, gate0,
                                            scale1, shift1, gate1, index);
  check_cuda_tensor(residual, "residual");
  check_cuda_tensor(residual_gate, "residual_gate");
  CAND_CHECK(residual.ndim() == 3 && residual.shape(0) == a.B && residual.shape(1) == a.L &&
                 residual.shape(2) == a.C,
             "residual must have the same shape as x");
  CAND_CHECK(residual_gate.ndim() == 3 && residual_gate.shape(0) == a.B &&
                 residual_gate.shape(1) == a.L && residual_gate.shape(2) == a.C,
             "residual_gate must have the same shape as x");
  CAND_CHECK(same_dtype(residual.dtype(), x.dtype()), "residual dtype must match x");
  CAND_CHECK(same_dtype(residual_gate.dtype(), x.dtype()), "residual_gate dtype must match x");
  CAND_CHECK(tensor_is_contiguous(residual), "residual must be contiguous");
  CAND_CHECK(tensor_is_contiguous(residual_gate), "residual_gate must be contiguous");
  check_output_like(output, x, "output");
  check_output_like(residual_out, x, "residual_out");
  check_output_like(gate_out, x, "gate_out");
  const int64_t rows = a.B * a.L;
  if (rows == 0 || a.C == 0) return;

  cudaStream_t stream = at::cuda::getCurrentCUDAStream();
  const DLDataType xt = x.dtype();
  const bool idx64 = is_i64(index.dtype());

#define RLN_LAUNCH(XT, IT)                                                                  \
  residual_ln_select01_kernel<XT, IT><<<static_cast<unsigned>(rows), kLnThreads, 0,         \
                                        stream>>>(                                          \
      static_cast<const XT*>(x.data_ptr()), static_cast<const XT*>(residual.data_ptr()),    \
      static_cast<const XT*>(residual_gate.data_ptr()), static_cast<const XT*>(a.weight),   \
      static_cast<const XT*>(a.bias), static_cast<const XT*>(scale0.data_ptr()),            \
      static_cast<const XT*>(shift0.data_ptr()), static_cast<const XT*>(gate0.data_ptr()),  \
      static_cast<const XT*>(scale1.data_ptr()), static_cast<const XT*>(shift1.data_ptr()), \
      static_cast<const XT*>(gate1.data_ptr()), static_cast<const IT*>(index.data_ptr()),   \
      static_cast<XT*>(output.data_ptr()), static_cast<XT*>(residual_out.data_ptr()),       \
      static_cast<XT*>(gate_out.data_ptr()), static_cast<float>(eps), a.L, a.C, a.m0, a.m1, \
      a.idx_sb, a.idx_sl)

  if (is_bf16(xt)) {
    idx64 ? RLN_LAUNCH(__nv_bfloat16, int64_t) : RLN_LAUNCH(__nv_bfloat16, int32_t);
  } else if (is_f16(xt)) {
    idx64 ? RLN_LAUNCH(__half, int64_t) : RLN_LAUNCH(__half, int32_t);
  } else if (is_f32(xt)) {
    idx64 ? RLN_LAUNCH(float, int64_t) : RLN_LAUNCH(float, int32_t);
  } else {
    cand_fail("unsupported x dtype");
  }
#undef RLN_LAUNCH
}

}  // namespace

TVM_FFI_DLL_EXPORT_TYPED_FUNC(fuse_scale_shift, fuse_scale_shift);
TVM_FFI_DLL_EXPORT_TYPED_FUNC(fuse_layernorm_scale_shift_gate_select01,
                              fuse_layernorm_scale_shift_gate_select01);
TVM_FFI_DLL_EXPORT_TYPED_FUNC(fuse_residual_layernorm_scale_shift_gate_select01,
                              fuse_residual_layernorm_scale_shift_gate_select01);
