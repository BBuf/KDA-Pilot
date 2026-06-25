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
// Lossless memory movement (raw-bit copy; NaN/Inf preserved). The output is
// decomposed into 1-2 sequence "regions"; each region is copied directly into
// the final output (the fused slice+concat never materializes a contiguous
// prefix). Contiguous regions (plain concat, the shard half of slice+concat)
// are flat coalesced copies; the head-sliced prefix is a pitched block copy.
// A general per-output-vector kernel handles the B>1 / non-16B-aligned cases.

#include <ATen/cuda/CUDAContext.h>
#include <c10/cuda/CUDAGuard.h>
#include <cuda_runtime.h>
#include <dlpack/dlpack.h>
#include <tvm/ffi/container/tensor.h>
#include <tvm/ffi/function.h>

#include <cstdint>
#include <string>

namespace {

using tvm::ffi::Optional;
using tvm::ffi::TensorView;

constexpr int OP_COPY = 0;
constexpr int OP_CONCAT = 1;
constexpr int OP_SLICE_CONCAT = 2;
constexpr int ORDER_AB = 0;
constexpr int ORDER_BA = 1;
constexpr int BLOCK = 256;
constexpr int64_t MAX_GRID = 1 << 20;

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

// Standard dense/contiguous check (size-1 dims have free stride).
inline bool is_contiguous(const TensorView& t) {
  int64_t expect = 1;
  for (int i = t.ndim() - 1; i >= 0; --i) {
    if (t.size(i) == 1) continue;
    if (t.stride(i) != expect) return false;
    expect *= t.size(i);
  }
  return true;
}
inline int64_t grid_for(int64_t total) {
  int64_t g = (total + BLOCK - 1) / BLOCK;
  if (g < 1) g = 1;
  if (g > MAX_GRID) g = MAX_GRID;
  return g;
}

// ---------------------------------------------------------------------------
// Optimized path (B==1, 16B-aligned): per-region pitched/flat 16B copies.
// A region copies `nblocks` contiguous blocks of `blk_vecs` 16B vectors each.
// Source block i starts at element (src_base + i*src_pitch); destination block i
// at element (dst_base + i*blk_elems) (output is contiguous). nblocks==1 is a
// flat coalesced copy with no per-vector index math.
// ---------------------------------------------------------------------------
__global__ void pitched_copy_kernel(const char* __restrict__ src, int64_t src_base_elem,
                                    int64_t src_pitch_elem, char* __restrict__ dst,
                                    int64_t dst_base_elem, int nblocks, int blk_elems,
                                    int blk_vecs, int es) {
  const int64_t gstride = (int64_t)gridDim.x * blockDim.x;
  const int64_t total = (int64_t)nblocks * blk_vecs;
  if (nblocks == 1) {
    const uint4* s = reinterpret_cast<const uint4*>(src + src_base_elem * es);
    uint4* d = reinterpret_cast<uint4*>(dst + dst_base_elem * es);
    for (int64_t i = blockIdx.x * (int64_t)blockDim.x + threadIdx.x; i < total; i += gstride)
      __stcs(d + i, __ldcs(s + i));
  } else {
    for (int64_t i = blockIdx.x * (int64_t)blockDim.x + threadIdx.x; i < total; i += gstride) {
      const int blk = (int)(i / blk_vecs);
      const int vib = (int)(i - (int64_t)blk * blk_vecs);
      const char* sp = src + (src_base_elem + (int64_t)blk * src_pitch_elem) * es;
      char* dp = dst + (dst_base_elem + (int64_t)blk * blk_elems) * es;
      __stcs(reinterpret_cast<uint4*>(dp) + vib, __ldcs(reinterpret_cast<const uint4*>(sp) + vib));
    }
  }
}

void launch_region(const char* src, int64_t src_base_elem, int64_t src_pitch_elem, char* dst,
                   int64_t dst_base_elem, int nblocks, int blk_elems, int es, cudaStream_t stream) {
  if (nblocks <= 0 || blk_elems <= 0) return;
  const int blk_vecs = (int)(((int64_t)blk_elems * es) / 16);
  const int64_t total = (int64_t)nblocks * blk_vecs;
  pitched_copy_kernel<<<(unsigned)grid_for(total), BLOCK, 0, stream>>>(
      src, src_base_elem, src_pitch_elem, dst, dst_base_elem, nblocks, blk_elems, blk_vecs, es);
}

// Single-launch concat of two contiguous sources into a contiguous output:
// out[0:first_vecs) <- first, out[first_vecs:total) <- second (one coalesced pass,
// just a segment branch, no per-vector index math). Matches ATen's single-kernel cat.
__global__ void concat_kernel(const char* __restrict__ first, const char* __restrict__ second,
                              char* __restrict__ out, int64_t first_vecs, int64_t total_vecs) {
  const uint4* f = reinterpret_cast<const uint4*>(first);
  const uint4* s = reinterpret_cast<const uint4*>(second);
  uint4* o = reinterpret_cast<uint4*>(out);
  const int64_t gstride = (int64_t)gridDim.x * blockDim.x;
  for (int64_t i = blockIdx.x * (int64_t)blockDim.x + threadIdx.x; i < total_vecs; i += gstride) {
    if (i < first_vecs) __stcs(o + i, __ldcs(f + i));
    else __stcs(o + i, __ldcs(s + (i - first_vecs)));
  }
}

void launch_concat(const char* first, const char* second, char* out, int64_t first_elems,
                   int64_t total_elems, int es, cudaStream_t stream) {
  const int64_t first_vecs = (first_elems * es) / 16;
  const int64_t total_vecs = (total_elems * es) / 16;
  concat_kernel<<<(unsigned)grid_for(total_vecs), BLOCK, 0, stream>>>(first, second, out, first_vecs, total_vecs);
}

// ---------------------------------------------------------------------------
// General fallback (any B / strides): one thread per output element-or-vector,
// mapping each output row (b, os, oh) to its source row by segment.
// ---------------------------------------------------------------------------
struct CopyPlan {
  const char* a;
  const char* b;
  char* out;
  int64_t aB, aS, aH, bB, bS, bH;
  int B, OutSeq, H, D, elem_size, Pa, first_is_a, h_start;
};

__device__ __forceinline__ void resolve_src(const CopyPlan& p, int b, int os, int oh,
                                             const char*& base, int64_t& selem) {
  const bool first_seg = (os < p.Pa);
  const bool use_a = (first_seg == (p.first_is_a != 0));
  int64_t sB, sS, sH;
  int shead, sidx = first_seg ? os : (os - p.Pa);
  if (use_a) { base = p.a; sB = p.aB; sS = p.aS; sH = p.aH; shead = p.h_start + oh; }
  else       { base = p.b; sB = p.bB; sS = p.bS; sH = p.bH; shead = oh; }
  selem = (int64_t)b * sB + (int64_t)sidx * sS + (int64_t)shead * sH;
}

__global__ void general_vec_kernel(CopyPlan p, int64_t total_vecs, int vecs_per_row) {
  const int64_t gstride = (int64_t)gridDim.x * blockDim.x;
  for (int64_t i = blockIdx.x * (int64_t)blockDim.x + threadIdx.x; i < total_vecs; i += gstride) {
    const int64_t row = i / vecs_per_row;
    const int vir = (int)(i - row * vecs_per_row);
    const int oh = (int)(row % p.H);
    const int64_t t = row / p.H;
    const int os = (int)(t % p.OutSeq);
    const int b = (int)(t / p.OutSeq);
    const char* base; int64_t selem;
    resolve_src(p, b, os, oh, base, selem);
    const int64_t delem = (((int64_t)b * p.OutSeq + os) * p.H + oh) * p.D;
    __stcs(reinterpret_cast<uint4*>(p.out + delem * p.elem_size) + vir,
           __ldcs(reinterpret_cast<const uint4*>(base + selem * p.elem_size) + vir));
  }
}

__global__ void general_scalar_kernel(CopyPlan p, int64_t total_elems) {
  const int64_t gstride = (int64_t)gridDim.x * blockDim.x;
  const int es = p.elem_size;
  for (int64_t i = blockIdx.x * (int64_t)blockDim.x + threadIdx.x; i < total_elems; i += gstride) {
    const int d = (int)(i % p.D);
    const int64_t r = i / p.D;
    const int oh = (int)(r % p.H);
    const int64_t t = r / p.H;
    const int os = (int)(t % p.OutSeq);
    const int b = (int)(t / p.OutSeq);
    const char* base; int64_t selem;
    resolve_src(p, b, os, oh, base, selem);
    selem += d;
    const int64_t delem = ((((int64_t)b * p.OutSeq + os) * p.H + oh) * p.D) + d;
    if (es == 2)
      *reinterpret_cast<uint16_t*>(p.out + delem * es) = *reinterpret_cast<const uint16_t*>(base + selem * es);
    else
      *reinterpret_cast<uint32_t*>(p.out + delem * es) = *reinterpret_cast<const uint32_t*>(base + selem * es);
  }
}

void launch_general(const CopyPlan& p, cudaStream_t stream) {
  const int64_t row_bytes = (int64_t)p.D * p.elem_size;
  const int64_t total_rows = (int64_t)p.B * p.OutSeq * p.H;
  const bool can_vec = (row_bytes % 16 == 0) && aligned16(p.a) &&
                       (p.b == nullptr || aligned16(p.b)) && aligned16(p.out);
  if (can_vec) {
    const int vecs_per_row = (int)(row_bytes / 16);
    const int64_t total = total_rows * vecs_per_row;
    general_vec_kernel<<<(unsigned)grid_for(total), BLOCK, 0, stream>>>(p, total, vecs_per_row);
  } else {
    const int64_t total = total_rows * p.D;
    general_scalar_kernel<<<(unsigned)grid_for(total), BLOCK, 0, stream>>>(p, total);
  }
}

inline void check_4d_contig_output(const TensorView& out) {
  CAND_CHECK(out.ndim() == 4, "output must be 4D [B, OutSeq, H, D]");
  CAND_CHECK(out.stride(3) == 1, "output last dim must be contiguous");
  CAND_CHECK(out.stride(2) == out.size(3), "output heads must be contiguous");
  CAND_CHECK(out.stride(1) == out.size(2) * out.size(3), "output seq must be contiguous");
  CAND_CHECK(out.size(0) == 1 || out.stride(0) == out.size(1) * out.size(2) * out.size(3),
             "output batch stride must be dense (no padded B>1 view)");
}

}  // namespace

void attention_concat_copy_candidate(int64_t op_type, int64_t order, int64_t h_start,
                                     int64_t h_local, TensorView source_a,
                                     Optional<TensorView> source_b,
                                     Optional<TensorView> scratch, TensorView output) {
  (void)scratch;  // candidate writes the output once; scratch (baseline-only) is ignored.

  CAND_CHECK(output.device().device_type == kDLCUDA, "output must be a CUDA tensor");
  CAND_CHECK(source_a.device().device_type == kDLCUDA, "source_a must be a CUDA tensor");
  CAND_CHECK(source_a.device().device_id == output.device().device_id,
             "source_a must be on the same CUDA device as output");
  check_4d_contig_output(output);
  const DLDataType dt = output.dtype();
  CAND_CHECK(same_dtype(source_a.dtype(), dt), "source_a dtype must match output");
  const int es = dtype_elem_size(dt);
  CAND_CHECK(source_a.stride(source_a.ndim() - 1) == 1, "source_a last dim must be contiguous");

  const int B = (int)output.size(0);
  const int OutSeq = (int)output.size(1);
  const int H = (int)output.size(2);
  const int D = (int)output.size(3);
  const int64_t HD = (int64_t)H * D;
  if ((int64_t)B * OutSeq * HD == 0) return;

  char* out = mutable_data_of<char>(output);
  const char* a = data_of<char>(source_a);
  const int64_t aS = source_a.stride(1);  // source_a seq stride (elements)

  // Resolve source_b (shard / second tensor) once if present.
  const char* b = nullptr;
  int64_t bS = 0;
  DLDataType bt = dt;
  if (source_b.has_value()) {
    const TensorView sb = source_b.value();
    CAND_CHECK(sb.device().device_type == kDLCUDA, "source_b must be a CUDA tensor");
    CAND_CHECK(sb.device().device_id == output.device().device_id,
               "source_b must be on the same CUDA device as output");
    CAND_CHECK(sb.stride(sb.ndim() - 1) == 1, "source_b last dim must be contiguous");
    b = data_of<char>(sb);
    bS = sb.stride(1);
    bt = sb.dtype();
    CAND_CHECK(same_dtype(bt, dt), "source_b dtype must match output");
  }

  const bool aligned = aligned16(a) && (b == nullptr || aligned16(b)) && aligned16(out) &&
                       ((HD * es) % 16 == 0);

  // ---- ABI contract validation (fail loudly before any copy; both paths) ----
  if (op_type == OP_CONCAT || op_type == OP_SLICE_CONCAT) {
    CAND_CHECK(order == ORDER_AB || order == ORDER_BA, "order must be 0 (AB) or 1 (BA)");
    CAND_CHECK(b != nullptr, "concat / slice_concat require source_b");
  } else if (op_type != OP_COPY) {
    cand_fail("unknown op_type");
  }

  // exact supported-layout enforcement (reject unsupported strides / contiguous copy loudly)
  if (op_type == OP_COPY) {
    CAND_CHECK(source_a.ndim() == 4, "copy: source_a must be 4D");
    CAND_CHECK(source_a.stride(2) == D, "copy: source_a head-dim stride must equal D");
    CAND_CHECK(source_a.stride(1) % D == 0 && source_a.stride(1) > (int64_t)H * D,
               "copy: source_a must be a non-contiguous head-sliced view (stride(1) > H*D)");
  } else {  // OP_CONCAT or OP_SLICE_CONCAT
    const TensorView sb = source_b.value();
    CAND_CHECK(sb.stride(sb.ndim() - 1) == 1, "source_b last dim must be contiguous");
    if (op_type == OP_CONCAT) {
      CAND_CHECK(is_contiguous(source_a) && is_contiguous(sb),
                 "concat: source_a and source_b must be dense/contiguous");
    } else {
      CAND_CHECK(is_contiguous(source_a), "slice_concat: prefix (source_a) must be a dense full-head tensor");
      CAND_CHECK(is_contiguous(sb), "slice_concat: shard (source_b) must be dense/contiguous");
    }
  }

  // full shape validation: every source dim (batch, seq, head, head_dim) vs output
  CAND_CHECK(source_a.ndim() == 4, "source_a must be 4D");
  CAND_CHECK(source_a.size(0) == B && source_a.size(3) == D, "source_a batch/head_dim must match output");
  if (op_type == OP_COPY) {
    CAND_CHECK(source_a.size(1) == OutSeq && source_a.size(2) == H, "copy: source_a shape must match output");
  } else {
    const TensorView sb_shape = source_b.value();
    CAND_CHECK(sb_shape.ndim() == 4 && sb_shape.size(0) == B && sb_shape.size(3) == D,
               "source_b batch/head_dim must match output");
    CAND_CHECK(source_a.size(1) + sb_shape.size(1) == OutSeq,
               "first+second segment seq length must equal output seq");
    CAND_CHECK(sb_shape.size(2) == H, "source_b head count must equal output H");
    if (op_type == OP_CONCAT)
      CAND_CHECK(source_a.size(2) == H, "concat: source_a head count must equal output H");
  }

  if (op_type == OP_SLICE_CONCAT) {
    CAND_CHECK(source_a.ndim() == 4, "slice_concat: source_a (prefix) must be 4D");
    const int full_heads = (int)source_a.size(2);
    CAND_CHECK(h_local > 0, "slice_concat: h_local must be > 0");
    CAND_CHECK((int)h_local == H, "slice_concat: h_local must equal output head count");
    CAND_CHECK(full_heads > (int)h_local,
               "slice_concat: full-head prefix required (h_full > h_local); pre-sliced prefix rejected");
    CAND_CHECK(h_start >= 0 && (int)(h_start + h_local) <= full_heads,
               "slice_concat: head slice out of range");
    CAND_CHECK(h_start % h_local == 0, "slice_concat: h_start must be a multiple of h_local (sp_rank * h_local)");
  }

  const int dev = output.device().device_id;
  c10::cuda::CUDAGuard guard(static_cast<c10::DeviceIndex>(dev));
  cudaStream_t stream = at::cuda::getCurrentCUDAStream(dev);

  // ---- Fast region path: B==1 and 16B-aligned (covers every production/regression row) ----
  if (B == 1 && aligned) {
    if (op_type == OP_COPY) {
      CAND_CHECK(source_a.ndim() == 4, "copy: source_a must be 4D");
      CAND_CHECK((int)source_a.size(1) == OutSeq && (int)source_a.size(2) == H &&
                 (int)source_a.size(3) == D, "copy: source_a shape must match output");
      // OutSeq blocks of HD contiguous elements, source seq-pitch aS (head-sliced view).
      launch_region(a, 0, aS, out, 0, OutSeq, (int)HD, es, stream);
      return;
    }
    if (op_type == OP_CONCAT) {
      CAND_CHECK(b != nullptr, "concat: source_b required");
      const int Sa = (int)source_a.size(1), Sb = (int)source_b.value().size(1);
      CAND_CHECK((int)source_a.size(2) == H && (int)source_b.value().size(2) == H, "concat: head count mismatch");
      CAND_CHECK((int)source_a.size(3) == D && (int)source_b.value().size(3) == D, "concat: head_dim mismatch");
      CAND_CHECK(Sa + Sb == OutSeq, "concat: Sa + Sb must equal OutSeq");
      // Single coalesced pass: [first, second] per order (first=a,second=b for AB; swapped for BA).
      const char* first = (order == ORDER_AB) ? a : b;
      const char* second = (order == ORDER_AB) ? b : a;
      const int64_t first_elems = (int64_t)((order == ORDER_AB) ? Sa : Sb) * HD;
      launch_concat(first, second, out, first_elems, (int64_t)OutSeq * HD, es, stream);
      return;
    }
    if (op_type == OP_SLICE_CONCAT) {
      CAND_CHECK(b != nullptr, "slice_concat: source_b (shard) required");
      const TensorView shard = source_b.value();
      const int full_heads = (int)source_a.size(2);
      const int P = (int)source_a.size(1);
      const int Ssh = (int)shard.size(1);
      CAND_CHECK((int)h_local == H, "slice_concat: h_local must equal output head count");
      CAND_CHECK((int)shard.size(2) == H, "slice_concat: shard head count must equal output");
      CAND_CHECK(h_start >= 0 && (int)(h_start + h_local) <= full_heads, "slice_concat: head slice out of range");
      CAND_CHECK((int)source_a.size(3) == D && (int)shard.size(3) == D, "slice_concat: head_dim mismatch");
      CAND_CHECK(P + Ssh == OutSeq, "slice_concat: P + Sshard must equal OutSeq");
      const int64_t prefix_dst = (order == ORDER_AB) ? 0 : (int64_t)Ssh * HD;
      const int64_t shard_dst = (order == ORDER_AB) ? (int64_t)P * HD : 0;
      // prefix: P blocks of (h_local*D) contiguous, head-sliced source (base h_start*D, pitch aS).
      launch_region(a, (int64_t)h_start * D, aS, out, prefix_dst, P, (int)HD, es, stream);
      // shard: one flat contiguous copy.
      launch_region(b, 0, 0, out, shard_dst, 1, (int)((int64_t)Ssh * HD), es, stream);
      return;
    }
    cand_fail("unknown op_type");
  }

  // ---- General fallback (B>1 or non-16B-aligned): per-output-vector mapping ----
  CopyPlan p{};
  p.out = out; p.a = a; p.b = b;
  p.B = B; p.OutSeq = OutSeq; p.H = H; p.D = D; p.elem_size = es; p.h_start = 0;
  p.aB = source_a.stride(0); p.aS = aS; p.aH = source_a.stride(2);
  if (op_type == OP_COPY) {
    CAND_CHECK(source_a.ndim() == 4 && (int)source_a.size(1) == OutSeq && (int)source_a.size(2) == H,
               "copy: source_a shape must match output");
    p.Pa = OutSeq; p.first_is_a = 1;
  } else if (op_type == OP_CONCAT) {
    CAND_CHECK(b != nullptr, "concat: source_b required");
    const TensorView sb = source_b.value();
    CAND_CHECK((int)source_a.size(2) == H && (int)sb.size(2) == H, "concat: head count mismatch");
    CAND_CHECK((int)source_a.size(1) + (int)sb.size(1) == OutSeq, "concat: Sa + Sb must equal OutSeq");
    p.bB = sb.stride(0); p.bS = sb.stride(1); p.bH = sb.stride(2);
    if (order == ORDER_AB) { p.Pa = (int)source_a.size(1); p.first_is_a = 1; }
    else                   { p.Pa = (int)sb.size(1);        p.first_is_a = 0; }
  } else if (op_type == OP_SLICE_CONCAT) {
    CAND_CHECK(b != nullptr, "slice_concat: source_b (shard) required");
    const TensorView shard = source_b.value();
    const int full_heads = (int)source_a.size(2);
    CAND_CHECK((int)h_local == H && (int)shard.size(2) == H, "slice_concat: head count mismatch");
    CAND_CHECK(h_start >= 0 && (int)(h_start + h_local) <= full_heads, "slice_concat: head slice out of range");
    CAND_CHECK((int)source_a.size(1) + (int)shard.size(1) == OutSeq, "slice_concat: P + Sshard must equal OutSeq");
    p.bB = shard.stride(0); p.bS = shard.stride(1); p.bH = shard.stride(2);
    p.h_start = (int)h_start;
    if (order == ORDER_AB) { p.Pa = (int)source_a.size(1); p.first_is_a = 1; }
    else                   { p.Pa = (int)shard.size(1);     p.first_is_a = 0; }
  } else {
    cand_fail("unknown op_type");
  }
  launch_general(p, stream);
}

TVM_FFI_DLL_EXPORT_TYPED_FUNC(attention_concat_copy_candidate, attention_concat_copy_candidate);
