// Candidate CUDA kernels for the SGLang USPAttention prefix head-slice /
// contiguous-copy / sequence-concat memory movement, for NVIDIA B200 (sm_100).
//
// Single exported selector function (destination passing, output last), shared
// with the PyTorch baseline ABI (baseline/binding.py). Three op types on
// [B, S, H, D] tensors (bf16 / fp16 / fp32), head_dim D contiguous (stride 1):
//
//   op_type 0  copy_contiguous          : copy a (possibly non-contiguous) source -> contiguous output
//   op_type 1  concat_sequence          : cat([a, b], dim=1) per `order`
//   op_type 2  slice_heads_then_concat  : cat(prefix[:, :, h_start:h_start+h_local, :], shard, dim=1) per `order`
//
// The whole task is lossless memory movement, so the kernel copies raw bits
// (NaN/Inf preserved). Each output "row" is the D contiguous elements at a
// fixed (b, out_seq, out_head); one thread copies one 16-byte vector of a row,
// mapping it to the correct source row. The fused slice+concat path writes the
// output exactly once and never materializes an intermediate contiguous prefix.

#include <ATen/cuda/CUDAContext.h>
#include <c10/cuda/CUDAGuard.h>
#include <cuda_runtime.h>
#include <dlpack/dlpack.h>
#include <tvm/ffi/container/tensor.h>
#include <tvm/ffi/function.h>

#include <cstdint>
#include <sstream>
#include <stdexcept>
#include <string>

namespace {

using tvm::ffi::Optional;
using tvm::ffi::TensorView;

constexpr int OP_COPY = 0;
constexpr int OP_CONCAT = 1;
constexpr int OP_SLICE_CONCAT = 2;
constexpr int ORDER_AB = 0;
constexpr int ORDER_BA = 1;

[[noreturn]] inline void cand_fail(const std::string& msg) {
  throw std::runtime_error("attention_concat_copy_candidate: " + msg);
}
#define CAND_CHECK(cond, msg) \
  do { if (!(cond)) cand_fail(msg); } while (0)

template <typename T = void>
inline const T* data_of(const TensorView& t) {
  return reinterpret_cast<const T*>(static_cast<const char*>(t.data_ptr()) + t.byte_offset());
}
template <typename T = void>
inline T* mutable_data_of(const TensorView& t) {
  return reinterpret_cast<T*>(static_cast<char*>(t.data_ptr()) + t.byte_offset());
}

inline int dtype_elem_size(DLDataType d) {
  const bool ok = (d.code == kDLBfloat && d.bits == 16) ||
                  (d.code == kDLFloat && d.bits == 16) ||
                  (d.code == kDLFloat && d.bits == 32);
  if (!ok) cand_fail("unsupported dtype (expect bf16/fp16/fp32)");
  return d.bits / 8;
}
inline bool same_dtype(DLDataType a, DLDataType b) {
  return a.code == b.code && a.bits == b.bits && a.lanes == b.lanes;
}
inline bool aligned16(const void* p) {
  return (reinterpret_cast<uintptr_t>(p) & 0xF) == 0;
}

// Resolved copy plan: output is contiguous [B, OutSeq, H, D]. Each output row
// (b, os, oh) of D contiguous elements maps to a source row chosen by segment.
struct CopyPlan {
  const char* a;   // source_a base (byte ptr at element 0)
  const char* b;   // source_b base (byte ptr) or nullptr
  char* out;       // output base
  int64_t aB, aS, aH;  // source_a strides in ELEMENTS (batch, seq, head); head-dim stride is 1
  int64_t bB, bS, bH;  // source_b strides in ELEMENTS
  int B, OutSeq, H, D;
  int elem_size;
  int Pa;          // first-segment sequence length (output rows [0,Pa) come from the first source)
  int first_is_a;  // 1 if the first segment reads source_a, else source_b
  int h_start;     // head offset added when reading source_a (slice op); 0 otherwise
};

// Compute the source row base element offset for output row (b, os, oh).
__device__ __forceinline__ int64_t src_row_elem(const CopyPlan& p, int b, int os, int oh) {
  const bool first_seg = (os < p.Pa);
  const bool use_a = (first_seg == (p.first_is_a != 0));
  int64_t sB, sS, sH;
  int sidx, shead;
  if (use_a) {
    sB = p.aB; sS = p.aS; sH = p.aH; shead = p.h_start + oh;
  } else {
    sB = p.bB; sS = p.bS; sH = p.bH; shead = oh;
  }
  sidx = first_seg ? os : (os - p.Pa);
  return (int64_t)b * sB + (int64_t)sidx * sS + (int64_t)shead * sH;
}

__device__ __forceinline__ const char* src_base(const CopyPlan& p, int b, int os, int oh) {
  const bool first_seg = (os < p.Pa);
  const bool use_a = (first_seg == (p.first_is_a != 0));
  return use_a ? p.a : p.b;
}

// Vectorized path: one thread copies one 16-byte chunk of an output row.
__global__ void copy_vec_kernel(CopyPlan p, int64_t total_vecs, int vecs_per_row) {
  const int64_t stride = (int64_t)gridDim.x * blockDim.x;
  for (int64_t i = blockIdx.x * (int64_t)blockDim.x + threadIdx.x; i < total_vecs; i += stride) {
    const int64_t row = i / vecs_per_row;
    const int vir = (int)(i - row * vecs_per_row);
    const int oh = (int)(row % p.H);
    const int64_t t = row / p.H;
    const int os = (int)(t % p.OutSeq);
    const int b = (int)(t / p.OutSeq);

    const char* sbase = src_base(p, b, os, oh);
    const int64_t selem = src_row_elem(p, b, os, oh);
    const int64_t delem = (((int64_t)b * p.OutSeq + os) * p.H + oh) * p.D;

    const uint4* sp = reinterpret_cast<const uint4*>(sbase + selem * p.elem_size) + vir;
    uint4* dp = reinterpret_cast<uint4*>(p.out + delem * p.elem_size) + vir;
    __stcs(dp, __ldcs(sp));
  }
}

// Scalar fallback: one thread copies one element (handles any dtype size /
// non-16B-aligned rows). Element bytes are copied raw (lossless).
__global__ void copy_scalar_kernel(CopyPlan p, int64_t total_elems) {
  const int64_t stride = (int64_t)gridDim.x * blockDim.x;
  const int es = p.elem_size;
  for (int64_t i = blockIdx.x * (int64_t)blockDim.x + threadIdx.x; i < total_elems; i += stride) {
    const int d = (int)(i % p.D);
    const int64_t r = i / p.D;
    const int oh = (int)(r % p.H);
    const int64_t t = r / p.H;
    const int os = (int)(t % p.OutSeq);
    const int b = (int)(t / p.OutSeq);

    const char* sbase = src_base(p, b, os, oh);
    const int64_t selem = src_row_elem(p, b, os, oh) + d;
    const int64_t delem = ((((int64_t)b * p.OutSeq + os) * p.H + oh) * p.D) + d;
    const char* s = sbase + selem * es;
    char* o = p.out + delem * es;
    if (es == 2) {
      *reinterpret_cast<uint16_t*>(o) = *reinterpret_cast<const uint16_t*>(s);
    } else {
      *reinterpret_cast<uint32_t*>(o) = *reinterpret_cast<const uint32_t*>(s);
    }
  }
}

inline void check_4d_contig_output(const TensorView& out) {
  CAND_CHECK(out.ndim() == 4, "output must be 4D [B, OutSeq, H, D]");
  CAND_CHECK(out.stride(3) == 1, "output last dim must be contiguous");
  CAND_CHECK(out.stride(2) == out.size(3), "output heads must be contiguous");
  CAND_CHECK(out.stride(1) == out.size(2) * out.size(3), "output seq must be contiguous");
}

void launch(const CopyPlan& p, cudaStream_t stream) {
  const int block = 256;
  const int64_t row_bytes = (int64_t)p.D * p.elem_size;
  const bool can_vec = (row_bytes % 16 == 0) &&
                       aligned16(p.a) && (p.b == nullptr || aligned16(p.b)) && aligned16(p.out);
  const int64_t total_rows = (int64_t)p.B * p.OutSeq * p.H;
  if (can_vec) {
    const int vecs_per_row = (int)(row_bytes / 16);
    const int64_t total_vecs = total_rows * vecs_per_row;
    int64_t grid = (total_vecs + block - 1) / block;
    if (grid < 1) grid = 1;
    if (grid > (1 << 20)) grid = (1 << 20);  // grid-stride covers the remainder
    copy_vec_kernel<<<(unsigned)grid, block, 0, stream>>>(p, total_vecs, vecs_per_row);
  } else {
    const int64_t total_elems = total_rows * p.D;
    int64_t grid = (total_elems + block - 1) / block;
    if (grid < 1) grid = 1;
    if (grid > (1 << 20)) grid = (1 << 20);
    copy_scalar_kernel<<<(unsigned)grid, block, 0, stream>>>(p, total_elems);
  }
}

}  // namespace

void attention_concat_copy_candidate(int64_t op_type, int64_t order, int64_t h_start,
                                     int64_t h_local, TensorView source_a,
                                     Optional<TensorView> source_b,
                                     Optional<TensorView> scratch, TensorView output) {
  (void)scratch;  // candidate writes the output once; scratch (baseline-only) is ignored.

  CAND_CHECK(output.device().device_type == kDLCUDA, "output must be a CUDA tensor");
  CAND_CHECK(source_a.device().device_type == kDLCUDA, "source_a must be a CUDA tensor");
  check_4d_contig_output(output);
  const DLDataType dt = output.dtype();
  CAND_CHECK(same_dtype(source_a.dtype(), dt), "source_a dtype must match output");
  const int es = dtype_elem_size(dt);

  CopyPlan p{};
  p.out = mutable_data_of<char>(output);
  p.a = data_of<char>(source_a);
  p.b = nullptr;
  p.B = (int)output.size(0);
  p.OutSeq = (int)output.size(1);
  p.H = (int)output.size(2);
  p.D = (int)output.size(3);
  p.elem_size = es;
  p.h_start = 0;
  CAND_CHECK(source_a.stride(source_a.ndim() - 1) == 1, "source_a last dim must be contiguous");

  if (op_type == OP_COPY) {
    // source_a is the (possibly non-contiguous) source view of shape [B, OutSeq, H, D].
    CAND_CHECK(source_a.ndim() == 4, "copy: source_a must be 4D");
    for (int i = 0; i < 4; ++i)
      CAND_CHECK((int)source_a.size(i) == (i == 0 ? p.B : i == 1 ? p.OutSeq : i == 2 ? p.H : p.D),
                 "copy: source_a shape must match output");
    p.aB = source_a.stride(0); p.aS = source_a.stride(1); p.aH = source_a.stride(2);
    p.Pa = p.OutSeq; p.first_is_a = 1;  // single segment from source_a
  } else if (op_type == OP_CONCAT) {
    CAND_CHECK(source_b.has_value(), "concat: source_b required");
    const TensorView b = source_b.value();
    CAND_CHECK(b.device().device_type == kDLCUDA, "source_b must be a CUDA tensor");
    CAND_CHECK(same_dtype(b.dtype(), dt), "source_b dtype must match output");
    CAND_CHECK(source_a.ndim() == 4 && b.ndim() == 4, "concat: sources must be 4D");
    CAND_CHECK((int)source_a.size(2) == p.H && (int)b.size(2) == p.H, "concat: head count must match output");
    CAND_CHECK((int)source_a.size(3) == p.D && (int)b.size(3) == p.D, "concat: head_dim must match output");
    CAND_CHECK((int)source_a.size(1) + (int)b.size(1) == p.OutSeq, "concat: Sa + Sb must equal OutSeq");
    CAND_CHECK(b.stride(b.ndim() - 1) == 1, "concat: source_b last dim must be contiguous");
    p.b = data_of<char>(b);
    p.aB = source_a.stride(0); p.aS = source_a.stride(1); p.aH = source_a.stride(2);
    p.bB = b.stride(0); p.bS = b.stride(1); p.bH = b.stride(2);
    if (order == ORDER_AB) { p.Pa = (int)source_a.size(1); p.first_is_a = 1; }
    else                   { p.Pa = (int)b.size(1);        p.first_is_a = 0; }
  } else if (op_type == OP_SLICE_CONCAT) {
    CAND_CHECK(source_b.has_value(), "slice_concat: source_b (shard) required");
    const TensorView shard = source_b.value();
    CAND_CHECK(shard.device().device_type == kDLCUDA, "shard must be a CUDA tensor");
    CAND_CHECK(same_dtype(shard.dtype(), dt), "shard dtype must match output");
    CAND_CHECK(source_a.ndim() == 4 && shard.ndim() == 4, "slice_concat: tensors must be 4D");
    const int full_heads = (int)source_a.size(2);
    const int P = (int)source_a.size(1);
    const int Ssh = (int)shard.size(1);
    CAND_CHECK((int)h_local == p.H, "slice_concat: h_local must equal output head count");
    CAND_CHECK((int)shard.size(2) == p.H, "slice_concat: shard head count must equal output");
    CAND_CHECK(h_start >= 0 && (int)(h_start + h_local) <= full_heads, "slice_concat: head slice out of range");
    CAND_CHECK((int)source_a.size(3) == p.D && (int)shard.size(3) == p.D, "slice_concat: head_dim mismatch");
    CAND_CHECK(P + Ssh == p.OutSeq, "slice_concat: P + Sshard must equal OutSeq");
    CAND_CHECK(shard.stride(shard.ndim() - 1) == 1, "slice_concat: shard last dim must be contiguous");
    p.b = data_of<char>(shard);
    p.aB = source_a.stride(0); p.aS = source_a.stride(1); p.aH = source_a.stride(2);
    p.bB = shard.stride(0); p.bS = shard.stride(1); p.bH = shard.stride(2);
    p.h_start = (int)h_start;  // applied to source_a (the full-head prefix) reads
    if (order == ORDER_AB) { p.Pa = P;   p.first_is_a = 1; }   // [prefix, shard]
    else                   { p.Pa = Ssh; p.first_is_a = 0; }   // [shard, prefix]
  } else {
    cand_fail("unknown op_type");
  }

  if ((int64_t)p.B * p.OutSeq * p.H * p.D == 0) return;  // nothing to copy

  const int dev = output.device().device_id;
  c10::cuda::CUDAGuard guard(static_cast<c10::DeviceIndex>(dev));
  cudaStream_t stream = at::cuda::getCurrentCUDAStream(dev);
  launch(p, stream);
}

TVM_FFI_DLL_EXPORT_TYPED_FUNC(attention_concat_copy_candidate, attention_concat_copy_candidate);
