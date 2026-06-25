// Candidate CUDA implementation of the SGLang diffusion residual-gate-add and
// 4D broadcast-add elementwise patterns for B200, exposed through a
// destination-passing tvm-ffi ABI that mirrors baseline/binding.py (inputs
// first, output tensor last; every launch on torch's current CUDA stream).
//
// Reference semantics (recovered upstream @ sgl-project/sglang main
// 8314247d9de0fa2c58e34756b3e1dbc6cf815dfd; see docs/baseline_source.md):
//   residual_gate_add(residual, update, gate, out):
//       out = residual + update * gate
//       gate is full-shape [B,L,D] (== residual) or row-broadcast [B,1,D].
//   broadcast_add_4d(a, b, out):
//       a [1,1,P,D] broadcasts over the sequence dim of b [1,S,P,D];
//       out[0,s,p,d] = a[0,0,p,d] + b[0,s,p,d].
//
// Math: elementwise arithmetic runs in fp32 and stores back in the input dtype
// (one rounding step). Tolerances follow the contract (bf16/fp16 5e-2,
// fp32 1e-5); the one-round fp32 form stays inside the bf16 tolerance versus
// the two-step eager reference (see docs/benchmark_method.md).
//
// Performance structure (B200, ~8 TB/s HBM3e, 148 SMs; bandwidth-bound):
//   - 16B-vectorized (8 bf16 / 4 fp32) grid-stride fast path gated at runtime
//     on contiguity, 16B base-pointer alignment, and a last dim divisible by
//     the vector width; a scalar grid-stride path covers the tail and every
//     layout the fast path rejects.
//   - The broadcast gate / broadcast `a` operand is reused across rows and is
//     read through the read-only cache (__ldg); streaming operands use the
//     default cache policy.
//   - Output is required distinct from the inputs (out-of-place) and contiguous:
//     aliasing and unsupported layouts are rejected on the host.

#include <ATen/cuda/CUDAContext.h>
#include <c10/cuda/CUDAGuard.h>

#include <cuda_bf16.h>
#include <cuda_fp16.h>

#include <dlpack/dlpack.h>
#include <tvm/ffi/container/tensor.h>
#if __has_include(<tvm/ffi/function.h>)
#include <tvm/ffi/function.h>
#endif

#include <cstdint>
#include <sstream>
#include <stdexcept>
#include <type_traits>

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

// --------------------------------------------------------------------------
// dtype helpers
// --------------------------------------------------------------------------

inline bool dtype_is(DLDataType d, uint8_t code, uint8_t bits) {
  return d.code == code && d.bits == bits && d.lanes == 1;
}
inline bool is_bf16(DLDataType d) { return dtype_is(d, kDLBfloat, 16); }
inline bool is_f16(DLDataType d) { return dtype_is(d, kDLFloat, 16); }
inline bool is_f32(DLDataType d) { return dtype_is(d, kDLFloat, 32); }
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

template <typename T>
union Vec16 {
  static constexpr int kElems = 16 / sizeof(T);
  uint4 raw;
  T elems[16 / sizeof(T)];
};

// --------------------------------------------------------------------------
// tensor view helpers
// --------------------------------------------------------------------------

template <typename T = char>
inline const T* data_of(const TensorView& t) {
  return reinterpret_cast<const T*>(static_cast<const char*>(t.data_ptr()) + t.byte_offset());
}
template <typename T = char>
inline T* mutable_data_of(const TensorView& t) {
  return reinterpret_cast<T*>(static_cast<char*>(t.data_ptr()) + t.byte_offset());
}

inline bool tensor_is_contiguous(const TensorView& t) {
  int64_t expect = 1;
  for (int i = t.ndim() - 1; i >= 0; --i) {
    if (t.size(i) == 1) continue;  // stride is free on size-1 dims
    if (t.stride(i) != expect) return false;
    expect *= t.size(i);
  }
  return true;
}

inline bool aligned16(const void* p) {
  return (reinterpret_cast<uintptr_t>(p) & 0xF) == 0;
}

inline void check_cuda(const TensorView& t, const char* name) {
  CAND_CHECK(t.device().device_type == kDLCUDA, name, " must be a CUDA tensor");
}

inline int64_t last_dim(const TensorView& t) { return t.size(t.ndim() - 1); }

// --------------------------------------------------------------------------
// residual_gate_add: out = residual + update * gate
// --------------------------------------------------------------------------

enum class GateMode { kFull, kBcastRow };

constexpr int kThreads = 256;

template <typename T, GateMode kGate, int kVec>
__global__ void rga_vec_kernel(const T* __restrict__ residual,
                               const T* __restrict__ update,
                               const T* __restrict__ gate,
                               T* __restrict__ out,
                               int64_t n_vec, int64_t row_vec) {
  // row_vec = D / kVec (vectors per row); only used for the broadcast gate.
  const int64_t stride = static_cast<int64_t>(blockDim.x) * gridDim.x;
  for (int64_t v = blockIdx.x * blockDim.x + threadIdx.x; v < n_vec; v += stride) {
    const Vec16<T> r{.raw = reinterpret_cast<const uint4*>(residual)[v]};
    const Vec16<T> u{.raw = reinterpret_cast<const uint4*>(update)[v]};
    Vec16<T> g;
    if (kGate == GateMode::kFull) {
      g.raw = reinterpret_cast<const uint4*>(gate)[v];
    } else {
      // Row-broadcast gate: D % kVec == 0, so each 16B vector stays inside one
      // row; the gate vector index is v modulo the per-row vector count.
      g.raw = __ldg(reinterpret_cast<const uint4*>(gate) + (v % row_vec));
    }
    Vec16<T> o;
#pragma unroll
    for (int k = 0; k < kVec; ++k) {
      o.elems[k] = from_f<T>(to_f(r.elems[k]) + to_f(u.elems[k]) * to_f(g.elems[k]));
    }
    reinterpret_cast<uint4*>(out)[v] = o.raw;
  }
}

template <typename T, GateMode kGate>
__global__ void rga_scalar_kernel(const T* __restrict__ residual,
                                  const T* __restrict__ update,
                                  const T* __restrict__ gate,
                                  T* __restrict__ out,
                                  int64_t begin, int64_t total, int64_t D) {
  const int64_t stride = static_cast<int64_t>(blockDim.x) * gridDim.x;
  for (int64_t i = begin + blockIdx.x * blockDim.x + threadIdx.x; i < total; i += stride) {
    const float gv = (kGate == GateMode::kFull) ? to_f(gate[i]) : to_f(__ldg(gate + (i % D)));
    out[i] = from_f<T>(to_f(residual[i]) + to_f(update[i]) * gv);
  }
}

inline int blocks_for(int64_t n) {
  int64_t b = (n + kThreads - 1) / kThreads;
  if (b < 1) b = 1;
  if (b > 65535) b = 65535;  // grid-stride covers the rest
  return static_cast<int>(b);
}

template <typename T>
void launch_rga(const TensorView& residual, const TensorView& update,
                const TensorView& gate, const TensorView& out,
                GateMode mode, cudaStream_t stream) {
  const int64_t total = residual.numel();
  const int64_t D = last_dim(residual);
  const T* rp = data_of<T>(residual);
  const T* up = data_of<T>(update);
  const T* gp = data_of<T>(gate);
  T* op = mutable_data_of<T>(out);
  constexpr int kVec = 16 / sizeof(T);

  const bool gate_contig = tensor_is_contiguous(gate);
  const bool vec_ok = tensor_is_contiguous(residual) && tensor_is_contiguous(update) &&
                      tensor_is_contiguous(out) && gate_contig &&
                      aligned16(rp) && aligned16(up) && aligned16(gp) && aligned16(op) &&
                      (D % kVec == 0) &&
                      (mode == GateMode::kFull ? (total % kVec == 0) : true);

  int64_t done = 0;
  if (vec_ok) {
    const int64_t n_vec = total / kVec;  // D % kVec == 0 => total % kVec == 0
    const int64_t row_vec = D / kVec;
    if (mode == GateMode::kFull) {
      rga_vec_kernel<T, GateMode::kFull, kVec>
          <<<blocks_for(n_vec), kThreads, 0, stream>>>(rp, up, gp, op, n_vec, row_vec);
    } else {
      rga_vec_kernel<T, GateMode::kBcastRow, kVec>
          <<<blocks_for(n_vec), kThreads, 0, stream>>>(rp, up, gp, op, n_vec, row_vec);
    }
    done = n_vec * kVec;
  }
  if (done < total) {
    if (mode == GateMode::kFull) {
      rga_scalar_kernel<T, GateMode::kFull>
          <<<blocks_for(total - done), kThreads, 0, stream>>>(rp, up, gp, op, done, total, D);
    } else {
      rga_scalar_kernel<T, GateMode::kBcastRow>
          <<<blocks_for(total - done), kThreads, 0, stream>>>(rp, up, gp, op, done, total, D);
    }
  }
}

void residual_gate_add(TensorView residual, TensorView update, TensorView gate, TensorView out) {
  check_cuda(residual, "residual");
  check_cuda(update, "update");
  check_cuda(gate, "gate");
  check_cuda(out, "out");

  CAND_CHECK(residual.ndim() >= 2, "residual must be at least 2D ([.., D])");
  CAND_CHECK(update.ndim() == residual.ndim(), "update rank must match residual");
  CAND_CHECK(out.ndim() == residual.ndim(), "out rank must match residual");
  for (int i = 0; i < residual.ndim(); ++i) {
    CAND_CHECK(update.size(i) == residual.size(i), "update shape must match residual");
    CAND_CHECK(out.size(i) == residual.size(i), "out shape must match residual");
  }
  const DLDataType dt = residual.dtype();
  CAND_CHECK(same_dtype(update.dtype(), dt) && same_dtype(gate.dtype(), dt) &&
                 same_dtype(out.dtype(), dt),
             "residual/update/gate/out must share dtype");
  CAND_CHECK(is_bf16(dt) || is_f16(dt) || is_f32(dt), "dtype must be bf16, fp16, or fp32");

  // Output must be distinct from every input (out-of-place only).
  CAND_CHECK(out.data_ptr() != residual.data_ptr() && out.data_ptr() != update.data_ptr() &&
                 out.data_ptr() != gate.data_ptr(),
             "out must not alias residual/update/gate");
  CAND_CHECK(tensor_is_contiguous(residual) && tensor_is_contiguous(update) &&
                 tensor_is_contiguous(out),
             "residual/update/out must be contiguous");

  // Gate mode: full == same shape as residual; broadcast == [.., 1, D] with a
  // size-1 second-to-last dim and a matching last dim.
  const int64_t D = last_dim(residual);
  CAND_CHECK(last_dim(gate) == D, "gate last dim must equal residual last dim");
  GateMode mode;
  bool full = (gate.ndim() == residual.ndim());
  for (int i = 0; full && i < residual.ndim(); ++i) full = (gate.size(i) == residual.size(i));
  if (full) {
    CAND_CHECK(tensor_is_contiguous(gate), "full-shape gate must be contiguous");
    mode = GateMode::kFull;
  } else {
    // Row-broadcast gate: same rank as residual, a size-1 row dim, and every
    // leading dim equal to 1 -- i.e. exactly D contiguous elements reused for
    // every row (the i%D indexing depends on this). Malformed [B,D] / [D] and
    // a true B>1 broadcast are rejected rather than silently mishandled.
    CAND_CHECK(gate.ndim() == residual.ndim(),
               "gate must be full-shape [.., D] or same-rank row-broadcast [.., 1, D]");
    CAND_CHECK(gate.size(gate.ndim() - 2) == 1, "row-broadcast gate must have a size-1 row dim");
    for (int i = 0; i < gate.ndim() - 1; ++i) {
      CAND_CHECK(gate.size(i) == 1,
                 "row-broadcast gate leading dims must be 1 (batch>1 broadcast unsupported)");
    }
    CAND_CHECK(tensor_is_contiguous(gate), "broadcast gate must be contiguous");
    mode = GateMode::kBcastRow;
  }

  // All operands must share one CUDA device; guard so the launch targets that
  // device regardless of the process's current device (multi-GPU safety).
  const int dev = residual.device().device_id;
  CAND_CHECK(update.device().device_id == dev && gate.device().device_id == dev &&
                 out.device().device_id == dev,
             "residual/update/gate/out must be on the same CUDA device");
  const c10::cuda::CUDAGuard device_guard(static_cast<c10::DeviceIndex>(dev));
  cudaStream_t stream = at::cuda::getCurrentCUDAStream(dev);
  if (residual.numel() == 0) return;
  if (is_bf16(dt)) {
    launch_rga<__nv_bfloat16>(residual, update, gate, out, mode, stream);
  } else if (is_f16(dt)) {
    launch_rga<__half>(residual, update, gate, out, mode, stream);
  } else {
    launch_rga<float>(residual, update, gate, out, mode, stream);
  }
}

// --------------------------------------------------------------------------
// broadcast_add_4d: out[0,s,p,d] = a[0,0,p,d] + b[0,s,p,d]
// --------------------------------------------------------------------------

template <typename T, int kVec>
__global__ void bcast_add_vec_kernel(const T* __restrict__ a, const T* __restrict__ b,
                                     T* __restrict__ out, int64_t n_vec, int64_t inner_vec) {
  const int64_t stride = static_cast<int64_t>(blockDim.x) * gridDim.x;
  for (int64_t v = blockIdx.x * blockDim.x + threadIdx.x; v < n_vec; v += stride) {
    const Vec16<T> bv{.raw = reinterpret_cast<const uint4*>(b)[v]};
    const Vec16<T> av{.raw = __ldg(reinterpret_cast<const uint4*>(a) + (v % inner_vec))};
    Vec16<T> o;
#pragma unroll
    for (int k = 0; k < kVec; ++k) o.elems[k] = from_f<T>(to_f(bv.elems[k]) + to_f(av.elems[k]));
    reinterpret_cast<uint4*>(out)[v] = o.raw;
  }
}

template <typename T>
__global__ void bcast_add_scalar_kernel(const T* __restrict__ a, const T* __restrict__ b,
                                        T* __restrict__ out, int64_t begin, int64_t total,
                                        int64_t inner) {
  const int64_t stride = static_cast<int64_t>(blockDim.x) * gridDim.x;
  for (int64_t i = begin + blockIdx.x * blockDim.x + threadIdx.x; i < total; i += stride) {
    out[i] = from_f<T>(to_f(b[i]) + to_f(__ldg(a + (i % inner))));
  }
}

template <typename T>
void launch_bcast_add(const TensorView& a, const TensorView& b, const TensorView& out,
                      int64_t inner, cudaStream_t stream) {
  const int64_t total = b.numel();
  const T* ap = data_of<T>(a);
  const T* bp = data_of<T>(b);
  T* op = mutable_data_of<T>(out);
  constexpr int kVec = 16 / sizeof(T);
  const bool vec_ok = tensor_is_contiguous(a) && tensor_is_contiguous(b) &&
                      tensor_is_contiguous(out) && aligned16(ap) && aligned16(bp) &&
                      aligned16(op) && (inner % kVec == 0);
  int64_t done = 0;
  if (vec_ok) {
    const int64_t n_vec = total / kVec;
    bcast_add_vec_kernel<T, kVec>
        <<<blocks_for(n_vec), kThreads, 0, stream>>>(ap, bp, op, n_vec, inner / kVec);
    done = n_vec * kVec;
  }
  if (done < total) {
    bcast_add_scalar_kernel<T>
        <<<blocks_for(total - done), kThreads, 0, stream>>>(ap, bp, op, done, total, inner);
  }
}

void broadcast_add_4d(TensorView a, TensorView b, TensorView out) {
  check_cuda(a, "a");
  check_cuda(b, "b");
  check_cuda(out, "out");
  CAND_CHECK(b.ndim() == 4 && a.ndim() == 4 && out.ndim() == 4,
             "broadcast_add_4d expects 4D a, b, and out");
  CAND_CHECK(b.size(0) == 1, "broadcast_add_4d supports batch size 1 only (a is reused per row)");
  CAND_CHECK(a.size(0) == b.size(0) && a.size(1) == 1, "a must be [1,1,P,D] broadcasting over dim1");
  CAND_CHECK(a.size(2) == b.size(2) && a.size(3) == b.size(3), "a/b inner dims (P,D) must match");
  for (int i = 0; i < 4; ++i) CAND_CHECK(out.size(i) == b.size(i), "out shape must match b");
  const DLDataType dt = b.dtype();
  CAND_CHECK(same_dtype(a.dtype(), dt) && same_dtype(out.dtype(), dt), "a/b/out must share dtype");
  CAND_CHECK(is_bf16(dt) || is_f16(dt) || is_f32(dt), "dtype must be bf16, fp16, or fp32");
  CAND_CHECK(out.data_ptr() != a.data_ptr() && out.data_ptr() != b.data_ptr(),
             "out must not alias a/b");
  CAND_CHECK(tensor_is_contiguous(a) && tensor_is_contiguous(b) && tensor_is_contiguous(out),
             "a/b/out must be contiguous");

  const int64_t inner = a.size(2) * a.size(3);  // P * D, the broadcast period
  // Same-device guard (multi-GPU safety): launch on the inputs' device, not the
  // process-current one.
  const int dev = b.device().device_id;
  CAND_CHECK(a.device().device_id == dev && out.device().device_id == dev,
             "a/b/out must be on the same CUDA device");
  const c10::cuda::CUDAGuard device_guard(static_cast<c10::DeviceIndex>(dev));
  cudaStream_t stream = at::cuda::getCurrentCUDAStream(dev);
  if (b.numel() == 0) return;
  if (is_bf16(dt)) {
    launch_bcast_add<__nv_bfloat16>(a, b, out, inner, stream);
  } else if (is_f16(dt)) {
    launch_bcast_add<__half>(a, b, out, inner, stream);
  } else {
    launch_bcast_add<float>(a, b, out, inner, stream);
  }
}

}  // namespace

TVM_FFI_DLL_EXPORT_TYPED_FUNC(residual_gate_add, residual_gate_add);
TVM_FFI_DLL_EXPORT_TYPED_FUNC(broadcast_add_4d, broadcast_add_4d);
