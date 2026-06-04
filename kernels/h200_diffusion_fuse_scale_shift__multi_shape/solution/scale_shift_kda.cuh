// Fused scale-shift / dual-modulation CUDA kernels for SGLang diffusion (H200).
//
// Family A — elementwise modulation:
//   y[b,l,c] = x[b,l,c] * (scale_constant + scale[...]) + shift[...]
//   x is (B, L, C) contiguous; scale/shift arrive as (B, L, C) views with
//   row strides (expand()-style zero-stride broadcast covers (B,C)/(1,C)/
//   (1,1,C) and non-contiguous per-token tensors), as a 1-element scalar
//   (splat), or as a per-frame (B*F, C) matrix (frame mode). Compute in fp32,
//   store in the x dtype. 16-byte vectorized loads/stores along C.
//
// Family B — LayerNorm + select01 dual modulation (+ optional residual):
//   x_hat = LayerNorm_fp32(x or residual_out, eps) [* weight] [+ bias]
//   sel   = index[b,l] != 0
//   out   = x_hat * (1 + scale_sel) + shift_sel ;  gate_out = gate_sel
//   residual mode first computes residual_out = residual + residual_gate * x
//   in fp32, stores the rounded copy, and runs LayerNorm on the UNROUNDED
//   fp32 values (matches the Triton baseline numerics).
//   One CTA per row, fp32 two-pass (centered) variance like the baseline.

#include <sgl_kernel/tensor.h>

#include <sgl_kernel/runtime.cuh>
#include <sgl_kernel/type.cuh>
#include <sgl_kernel/utils.cuh>
#include <sgl_kernel/vec.cuh>
#include <sgl_kernel/warp.cuh>

#include <dlpack/dlpack.h>

#include <algorithm>
#include <cstdint>
#include <type_traits>

namespace {

constexpr uint32_t kThreads = 256;
constexpr uint32_t kWarpsPerBlock = kThreads / device::kWarpThreads;
constexpr int64_t kMaxGridY = 65535;

template <typename T>
constexpr uint32_t vec_elems() {
  return 16 / sizeof(T);  // 16B packets: 8x bf16/fp16, 4x fp32
}

// Convert one 16-byte packet of DType into kN fp32 lanes (kN = vec_elems<DType>).
template <typename DType, uint32_t kN>
SGL_DEVICE void packet_to_fp32(const device::AlignedVector<DType, kN>& v, float* out) {
  using Packed = packed_t<DType>;
  const Packed* pairs = reinterpret_cast<const Packed*>(v.data());
#pragma unroll
  for (uint32_t j = 0; j < kN / 2; ++j) {
    const auto [x0, x1] = device::cast<fp32x2_t>(pairs[j]);
    out[2 * j] = x0;
    out[2 * j + 1] = x1;
  }
}

template <>
SGL_DEVICE void packet_to_fp32<float, 4>(const device::AlignedVector<float, 4>& v, float* out) {
#pragma unroll
  for (uint32_t j = 0; j < 4; ++j) {
    out[j] = v[j];
  }
}

// Convert kN fp32 lanes back into a 16-byte packet of DType.
template <typename DType, uint32_t kN>
SGL_DEVICE void fp32_to_packet(const float* in, device::AlignedVector<DType, kN>& v) {
  using Packed = packed_t<DType>;
  Packed* pairs = reinterpret_cast<Packed*>(v.data());
#pragma unroll
  for (uint32_t j = 0; j < kN / 2; ++j) {
    pairs[j] = device::cast<Packed, fp32x2_t>({in[2 * j], in[2 * j + 1]});
  }
}

template <>
SGL_DEVICE void fp32_to_packet<float, 4>(const float* in, device::AlignedVector<float, 4>& v) {
#pragma unroll
  for (uint32_t j = 0; j < 4; ++j) {
    v[j] = in[j];
  }
}

// Load kXVec fp32 lanes from a row of SType at vector slot `vslot`
// (element index vslot * kXVec). SType may be narrower or wider than the
// x dtype; the packet count adjusts so the element count matches.
template <typename SType, uint32_t kXVec>
SGL_DEVICE void load_row_fp32(const void* row_ptr, uint32_t vslot, float* out) {
  constexpr uint32_t kSVec = vec_elems<SType>();
  using SVec = device::AlignedVector<SType, kSVec>;
  constexpr uint32_t kPackets = kXVec / kSVec;  // 1 (same width) or 2 (fp32 vs 16-bit x)
  static_assert(kPackets >= 1, "scale dtype wider than two packets per x packet");
#pragma unroll
  for (uint32_t p = 0; p < kPackets; ++p) {
    SVec v;
    v.load(row_ptr, static_cast<int64_t>(vslot) * kPackets + p);
    packet_to_fp32<SType, kSVec>(v, out + p * kSVec);
  }
}

// ---------------------------------------------------------------------------
// Family A
// ---------------------------------------------------------------------------

struct FuseScaleShiftParams {
  const void* __restrict__ x_ptr;
  const void* __restrict__ scale_ptr;
  const void* __restrict__ shift_ptr;
  void* __restrict__ y_ptr;
  int64_t rows;       // B * L
  int64_t seq_len;    // L
  int64_t inner_dim;  // C
  int64_t scale_stride_b;  // element strides of the (B, L, C) view (0 = broadcast)
  int64_t scale_stride_l;
  int64_t shift_stride_b;
  int64_t shift_stride_l;
  int64_t frame_seqlen;  // frame mode: L / num_frames
  int64_t num_frames;
  float scale_constant;
};

template <typename DTypeX, typename DTypeScale, typename DTypeShift, bool kScaleSplat,
          bool kShiftSplat, bool kFrameMode, bool kUsePDL>
__global__ void fused_scale_shift_elementwise(const FuseScaleShiftParams __grid_constant__ params) {
  using namespace device;
  constexpr uint32_t kXVec = vec_elems<DTypeX>();
  using XVec = AlignedVector<DTypeX, kXVec>;

  PDLWaitPrimary<kUsePDL>();

  const int64_t row = blockIdx.y;
  const int64_t num_vecs = params.inner_dim / kXVec;
  const int64_t vslot = static_cast<int64_t>(blockIdx.x) * blockDim.x + threadIdx.x;
  if (row >= params.rows || vslot >= num_vecs) {
    PDLTriggerSecondary<kUsePDL>();
    return;
  }

  const int64_t b = row / params.seq_len;
  const int64_t l = row - b * params.seq_len;

  const void* x_row = pointer::offset(params.x_ptr, row * params.inner_dim * sizeof(DTypeX));
  void* y_row = pointer::offset(params.y_ptr, row * params.inner_dim * sizeof(DTypeX));

  XVec xv;
  xv.load(x_row, vslot);
  float xf[kXVec];
  packet_to_fp32<DTypeX, kXVec>(xv, xf);

  float sf[kXVec];
  if constexpr (kScaleSplat) {
    const float s = cast<fp32_t>(*static_cast<const DTypeScale*>(params.scale_ptr));
#pragma unroll
    for (uint32_t i = 0; i < kXVec; ++i) {
      sf[i] = s;
    }
  } else {
    int64_t scale_row_elems;
    if constexpr (kFrameMode) {
      scale_row_elems = (b * params.num_frames + l / params.frame_seqlen) * params.inner_dim;
    } else {
      scale_row_elems = b * params.scale_stride_b + l * params.scale_stride_l;
    }
    const void* scale_row =
        pointer::offset(params.scale_ptr, scale_row_elems * sizeof(DTypeScale));
    load_row_fp32<DTypeScale, kXVec>(scale_row, static_cast<uint32_t>(vslot), sf);
  }

  float shf[kXVec];
  if constexpr (kShiftSplat) {
    const float s = cast<fp32_t>(*static_cast<const DTypeShift*>(params.shift_ptr));
#pragma unroll
    for (uint32_t i = 0; i < kXVec; ++i) {
      shf[i] = s;
    }
  } else {
    const int64_t shift_row_elems = b * params.shift_stride_b + l * params.shift_stride_l;
    const void* shift_row =
        pointer::offset(params.shift_ptr, shift_row_elems * sizeof(DTypeShift));
    load_row_fp32<DTypeShift, kXVec>(shift_row, static_cast<uint32_t>(vslot), shf);
  }

#pragma unroll
  for (uint32_t i = 0; i < kXVec; ++i) {
    xf[i] = fmaf(xf[i], params.scale_constant + sf[i], shf[i]);
  }

  XVec yv;
  fp32_to_packet<DTypeX, kXVec>(xf, yv);
  yv.store(y_row, vslot);

  PDLTriggerSecondary<kUsePDL>();
}

template <typename DTypeX, typename DTypeScale, typename DTypeShift, bool kScaleSplat,
          bool kShiftSplat, bool kFrameMode, bool kUsePDL>
struct FuseScaleShiftKernel {
  static constexpr auto kernel = fused_scale_shift_elementwise<DTypeX, DTypeScale, DTypeShift,
                                                               kScaleSplat, kShiftSplat,
                                                               kFrameMode, kUsePDL>;

  // scale/shift contracts (verified):
  //   splat: 1-element tensor of DTypeScale/DTypeShift
  //   strided: (B, L, C) view with strides (sb, sl, 1)
  //   frame mode (scale only): contiguous (B*F, C) matrix
  static void
  run(const tvm::ffi::TensorView x,
      const tvm::ffi::TensorView scale,
      const tvm::ffi::TensorView shift,
      const tvm::ffi::TensorView y,
      float scale_constant,
      int64_t num_frames) {
    using namespace host;

    auto B = SymbolicSize{"batch"};
    auto L = SymbolicSize{"seq_len"};
    auto C = SymbolicSize{"inner_dim"};
    auto device = SymbolicDevice{};
    device.set_options<kDLCUDA>();

    TensorMatcher({B, L, C}).with_dtype<DTypeX>().with_device(device).verify(x).verify(y);
    int64_t scale_sb = 0, scale_sl = 0, shift_sb = 0, shift_sl = 0;
    if constexpr (kScaleSplat) {
      TensorMatcher({1}).with_dtype<DTypeScale>().with_device(device).verify(scale);
    } else if constexpr (kFrameMode) {
      TensorMatcher({-1, C}).with_dtype<DTypeScale>().with_device(device).verify(scale);
    } else {
      auto SB = SymbolicSize{"scale_stride_b"};
      auto SL = SymbolicSize{"scale_stride_l"};
      TensorMatcher({B, L, C})
          .with_strides({SB, SL, 1})
          .with_dtype<DTypeScale>()
          .with_device(device)
          .verify(scale);
      scale_sb = SB.unwrap();
      scale_sl = SL.unwrap();
    }
    if constexpr (kShiftSplat) {
      TensorMatcher({1}).with_dtype<DTypeShift>().with_device(device).verify(shift);
    } else {
      auto HB = SymbolicSize{"shift_stride_b"};
      auto HL = SymbolicSize{"shift_stride_l"};
      TensorMatcher({B, L, C})
          .with_strides({HB, HL, 1})
          .with_dtype<DTypeShift>()
          .with_device(device)
          .verify(shift);
      shift_sb = HB.unwrap();
      shift_sl = HL.unwrap();
    }

    const int64_t batch = B.unwrap();
    const int64_t seq_len = L.unwrap();
    const int64_t inner = C.unwrap();
    const int64_t rows = batch * seq_len;
    constexpr uint32_t kXVec = vec_elems<DTypeX>();

    const auto params = FuseScaleShiftParams{
        .x_ptr = x.data_ptr(),
        .scale_ptr = scale.data_ptr(),
        .shift_ptr = shift.data_ptr(),
        .y_ptr = y.data_ptr(),
        .rows = rows,
        .seq_len = seq_len,
        .inner_dim = inner,
        .scale_stride_b = scale_sb,
        .scale_stride_l = scale_sl,
        .shift_stride_b = shift_sb,
        .shift_stride_l = shift_sl,
        .frame_seqlen = kFrameMode && num_frames > 0 ? seq_len / num_frames : 1,
        .num_frames = num_frames,
        .scale_constant = scale_constant,
    };

    const int64_t num_vecs = inner / kXVec;
    // Prefer the block size that tiles the row exactly (no half-empty blocks);
    // short rows take one 128-thread block instead of a mostly-idle 256.
    uint32_t threads = kThreads;
    if (num_vecs % kThreads != 0 && (num_vecs <= 128 || num_vecs % 128 == 0)) {
      threads = 128;
    }
    const uint32_t col_blocks = static_cast<uint32_t>(div_ceil(num_vecs, int64_t{threads}));
    const dim3 grid(col_blocks, static_cast<uint32_t>(rows));
    LaunchKernel(grid, threads, device.unwrap()).enable_pdl(kUsePDL)(kernel, params);
  }
};

// ---------------------------------------------------------------------------
// Family B
// ---------------------------------------------------------------------------

// Block-wide fp32 sum, deterministic fixed-order tree reduce, result
// broadcast to all threads. Sized for up to kWarpsPerBlock warps; works for
// any runtime block size <= kThreads (inactive warp slots are zero-filled).
// `smem` must hold >= kWarpsPerBlock + 1 floats. The trailing barrier makes
// back-to-back reductions over the same buffer safe.
SGL_DEVICE float block_reduce_sum(float v, float* smem) {
  using namespace device;
  v = warp::reduce_sum(v);
  const uint32_t lane = threadIdx.x & (kWarpThreads - 1);
  const uint32_t warp_id = threadIdx.x >> 5;
  const uint32_t num_warps = (blockDim.x + kWarpThreads - 1) / kWarpThreads;
  if (lane == 0) {
    smem[warp_id] = v;
  }
  __syncthreads();
  if (warp_id == 0) {
    float t = (lane < num_warps) ? smem[lane] : 0.0f;
    t = warp::reduce_sum<kWarpsPerBlock>(t);
    if (lane == 0) {
      smem[kWarpsPerBlock] = t;
    }
  }
  __syncthreads();
  const float out = smem[kWarpsPerBlock];
  __syncthreads();
  return out;
}

struct LNSelect01Params {
  const void* __restrict__ x_ptr;
  const void* __restrict__ residual_ptr;
  const void* __restrict__ residual_gate_ptr;
  const void* __restrict__ weight_ptr;
  const void* __restrict__ bias_ptr;
  const void* __restrict__ scale0_ptr;
  const void* __restrict__ shift0_ptr;
  const void* __restrict__ gate0_ptr;
  const void* __restrict__ scale1_ptr;
  const void* __restrict__ shift1_ptr;
  const void* __restrict__ gate1_ptr;
  const void* __restrict__ index_ptr;
  void* __restrict__ out_ptr;
  void* __restrict__ residual_out_ptr;
  void* __restrict__ gate_out_ptr;
  int64_t seq_len;
  int64_t inner_dim;
  int64_t mod_stride_b;  // shared row stride (elements) of the six (B, C) tensors
  int64_t index_stride_b;
  int64_t index_stride_l;
  float eps;
};

// One CTA per row. kMaxIter bounds the per-thread register tile:
// C <= kThreads * vec * kMaxIter (e.g. bf16: 256*8*4 = 8192).
template <typename DTypeX, typename IdType, bool kHasWeight, bool kHasBias, bool kHasResidual,
          bool kUsePDL>
__global__ void fused_ln_select01(const LNSelect01Params __grid_constant__ params) {
  using namespace device;
  constexpr uint32_t kXVec = vec_elems<DTypeX>();
  constexpr uint32_t kMaxIter = 4;
  using XVec = AlignedVector<DTypeX, kXVec>;

  __shared__ float smem[kWarpsPerBlock + 1];

  PDLWaitPrimary<kUsePDL>();

  const int64_t row = blockIdx.x;
  const int64_t b = row / params.seq_len;
  const int64_t l = row - b * params.seq_len;
  const int64_t num_vecs = params.inner_dim / kXVec;
  const float inv_n = 1.0f / static_cast<float>(params.inner_dim);

  const void* x_row = pointer::offset(params.x_ptr, row * params.inner_dim * sizeof(DTypeX));
  void* out_row = pointer::offset(params.out_ptr, row * params.inner_dim * sizeof(DTypeX));
  void* gate_out_row =
      pointer::offset(params.gate_out_ptr, row * params.inner_dim * sizeof(DTypeX));

  // The modulation selection depends only on index[b, l] — NOT on the
  // reduction — so the gate copy-through is hoisted ABOVE the block-reduction
  // barrier to overlap its load+store traffic with the LN statistics
  // (profiling showed the barrier-then-serial-epilogue ordering left DRAM
  // idle ~7% of the kernel). The scale/shift tiles stay post-barrier: holding
  // them in registers across the barrier costs ~64 regs/thread and the
  // measured occupancy loss outweighed the overlap gain.
  const int64_t idx_off = b * params.index_stride_b + l * params.index_stride_l;
  const bool sel = static_cast<const IdType*>(params.index_ptr)[idx_off] != IdType(0);
  const int64_t mod_off = b * params.mod_stride_b;
  const void* scale_row = pointer::offset(sel ? params.scale1_ptr : params.scale0_ptr,
                                          mod_off * sizeof(DTypeX));
  const void* shift_row = pointer::offset(sel ? params.shift1_ptr : params.shift0_ptr,
                                          mod_off * sizeof(DTypeX));
  const void* gate_row = pointer::offset(sel ? params.gate1_ptr : params.gate0_ptr,
                                         mod_off * sizeof(DTypeX));

  // Load the row into fp32 registers (residual mode fuses the gated add) and
  // accumulate the sum. The variance is computed in a second, register-only
  // pass as the CENTERED sum of (x - mean)^2, matching the baseline formula:
  // the single-pass E[x^2] - mean^2 form catastrophically cancels in fp32
  // when a row's offset is large relative to its spread (e.g. mean ~1e3,
  // std ~0.1 collapses to var ~ 0).
  // Tile loops are statically unrolled with slot guards so the register
  // arrays stay in registers (dynamic indexing would spill to local memory).
  float vals[kMaxIter][kXVec];
  float lsum = 0.0f;
#pragma unroll
  for (uint32_t it = 0; it < kMaxIter; ++it) {
    const int64_t vslot = threadIdx.x + static_cast<int64_t>(it) * blockDim.x;
    if (vslot >= num_vecs) {
      continue;
    }
    XVec xv;
    xv.load(x_row, vslot);
    float* vf = vals[it];
    packet_to_fp32<DTypeX, kXVec>(xv, vf);
    if constexpr (kHasResidual) {
      const void* res_row =
          pointer::offset(params.residual_ptr, row * params.inner_dim * sizeof(DTypeX));
      const void* rg_row =
          pointer::offset(params.residual_gate_ptr, row * params.inner_dim * sizeof(DTypeX));
      XVec rv, gv;
      rv.load(res_row, vslot);
      gv.load(rg_row, vslot);
      float rf[kXVec], gf[kXVec];
      packet_to_fp32<DTypeX, kXVec>(rv, rf);
      packet_to_fp32<DTypeX, kXVec>(gv, gf);
#pragma unroll
      for (uint32_t i = 0; i < kXVec; ++i) {
        vf[i] = fmaf(gf[i], vf[i], rf[i]);  // residual + residual_gate * x
      }
      void* res_out_row =
          pointer::offset(params.residual_out_ptr, row * params.inner_dim * sizeof(DTypeX));
      XVec rov;
      fp32_to_packet<DTypeX, kXVec>(vf, rov);
      rov.store(res_out_row, vslot);
    }
#pragma unroll
    for (uint32_t i = 0; i < kXVec; ++i) {
      lsum += vf[i];
    }

    // Independent of the reduction: gate copy-through (native dtype, transient
    // registers) stays in flight while the barrier resolves.
    XVec gv;
    gv.load(gate_row, vslot);
    gv.store(gate_out_row, vslot);
  }

  const float mean = block_reduce_sum(lsum, smem) * inv_n;

  float lsumsq = 0.0f;
#pragma unroll
  for (uint32_t it = 0; it < kMaxIter; ++it) {
    const int64_t vslot = threadIdx.x + static_cast<int64_t>(it) * blockDim.x;
    if (vslot >= num_vecs) {
      continue;
    }
#pragma unroll
    for (uint32_t i = 0; i < kXVec; ++i) {
      const float d = vals[it][i] - mean;
      lsumsq = fmaf(d, d, lsumsq);
    }
  }
  const float var = block_reduce_sum(lsumsq, smem) * inv_n;
  const float rstd = math::rsqrt(var + params.eps);

#pragma unroll
  for (uint32_t it = 0; it < kMaxIter; ++it) {
    const int64_t vslot64 = threadIdx.x + static_cast<int64_t>(it) * blockDim.x;
    if (vslot64 >= num_vecs) {
      continue;
    }
    const uint32_t vslot = static_cast<uint32_t>(vslot64);
    float* vf = vals[it];
#pragma unroll
    for (uint32_t i = 0; i < kXVec; ++i) {
      vf[i] = (vf[i] - mean) * rstd;
    }
    if constexpr (kHasWeight) {
      float wf[kXVec];
      load_row_fp32<DTypeX, kXVec>(params.weight_ptr, vslot, wf);
#pragma unroll
      for (uint32_t i = 0; i < kXVec; ++i) {
        vf[i] *= wf[i];
      }
    }
    if constexpr (kHasBias) {
      float bf[kXVec];
      load_row_fp32<DTypeX, kXVec>(params.bias_ptr, vslot, bf);
#pragma unroll
      for (uint32_t i = 0; i < kXVec; ++i) {
        vf[i] += bf[i];
      }
    }
    float sf[kXVec], shf[kXVec];
    load_row_fp32<DTypeX, kXVec>(scale_row, vslot, sf);
    load_row_fp32<DTypeX, kXVec>(shift_row, vslot, shf);
#pragma unroll
    for (uint32_t i = 0; i < kXVec; ++i) {
      vf[i] = fmaf(vf[i], 1.0f + sf[i], shf[i]);
    }
    XVec ov;
    fp32_to_packet<DTypeX, kXVec>(vf, ov);
    ov.store(out_row, vslot);
  }

  PDLTriggerSecondary<kUsePDL>();
}

template <typename DTypeX, bool kHasWeight, bool kHasBias, bool kHasResidual, bool kUsePDL>
struct FuseLNSelect01Kernel {
  template <typename IdType>
  static constexpr auto kernel =
      fused_ln_select01<DTypeX, IdType, kHasWeight, kHasBias, kHasResidual, kUsePDL>;

  // weight/bias use x as a sentinel when absent (mirrors the baseline wrapper);
  // residual tensors use x as sentinel when kHasResidual is false.
  static void
  run(const tvm::ffi::TensorView x,
      const tvm::ffi::TensorView residual,
      const tvm::ffi::TensorView residual_gate,
      const tvm::ffi::TensorView weight,
      const tvm::ffi::TensorView bias,
      const tvm::ffi::TensorView scale0,
      const tvm::ffi::TensorView shift0,
      const tvm::ffi::TensorView gate0,
      const tvm::ffi::TensorView scale1,
      const tvm::ffi::TensorView shift1,
      const tvm::ffi::TensorView gate1,
      const tvm::ffi::TensorView index,
      const tvm::ffi::TensorView out,
      const tvm::ffi::TensorView residual_out,
      const tvm::ffi::TensorView gate_out,
      float eps) {
    using namespace host;

    auto B = SymbolicSize{"batch"};
    auto L = SymbolicSize{"seq_len"};
    auto C = SymbolicSize{"inner_dim"};
    auto MB = SymbolicSize{"mod_stride_b"};
    auto IB = SymbolicSize{"index_stride_b"};
    auto IL = SymbolicSize{"index_stride_l"};
    auto device = SymbolicDevice{};
    auto id_type = SymbolicDType{};
    device.set_options<kDLCUDA>();

    TensorMatcher({B, L, C}).with_dtype<DTypeX>().with_device(device).verify(x).verify(out).verify(
        gate_out);
    if constexpr (kHasResidual) {
      TensorMatcher({B, L, C})
          .with_dtype<DTypeX>()
          .with_device(device)
          .verify(residual)
          .verify(residual_gate)
          .verify(residual_out);
    }
    if constexpr (kHasWeight) {
      TensorMatcher({C}).with_dtype<DTypeX>().with_device(device).verify(weight);
    }
    if constexpr (kHasBias) {
      TensorMatcher({C}).with_dtype<DTypeX>().with_device(device).verify(bias);
    }
    // The six modulation tensors share one (B, C) shape and one row stride.
    TensorMatcher({B, C})
        .with_strides({MB, 1})
        .with_dtype<DTypeX>()
        .with_device(device)
        .verify(scale0)
        .verify(shift0)
        .verify(gate0)
        .verify(scale1)
        .verify(shift1)
        .verify(gate1);
    TensorMatcher({B, L})
        .with_strides({IB, IL})
        .with_dtype<int32_t, int64_t>(id_type)
        .with_device(device)
        .verify(index);

    const int64_t batch = B.unwrap();
    const int64_t seq_len = L.unwrap();
    const int64_t rows = batch * seq_len;

    const auto params = LNSelect01Params{
        .x_ptr = x.data_ptr(),
        .residual_ptr = residual.data_ptr(),
        .residual_gate_ptr = residual_gate.data_ptr(),
        .weight_ptr = weight.data_ptr(),
        .bias_ptr = bias.data_ptr(),
        .scale0_ptr = scale0.data_ptr(),
        .shift0_ptr = shift0.data_ptr(),
        .gate0_ptr = gate0.data_ptr(),
        .scale1_ptr = scale1.data_ptr(),
        .shift1_ptr = shift1.data_ptr(),
        .gate1_ptr = gate1.data_ptr(),
        .index_ptr = index.data_ptr(),
        .out_ptr = out.data_ptr(),
        .residual_out_ptr = residual_out.data_ptr(),
        .gate_out_ptr = gate_out.data_ptr(),
        .seq_len = seq_len,
        .inner_dim = C.unwrap(),
        .mod_stride_b = MB.unwrap(),
        .index_stride_b = IB.unwrap(),
        .index_stride_l = IL.unwrap(),
        .eps = eps,
    };

    const auto selected_kernel =
        id_type.is_type<int32_t>() ? kernel<int32_t> : kernel<int64_t>;
    // Pick the smallest block (>=4 warps) whose 4-iteration register tile
    // covers the row: fewer warps -> cheaper block reduction for C=3072.
    constexpr uint32_t kXVec = vec_elems<DTypeX>();
    const int64_t num_vecs = C.unwrap() / kXVec;
    const uint32_t threads = num_vecs <= int64_t{128} * 4 ? 128 : kThreads;
    LaunchKernel(static_cast<uint32_t>(rows), threads, device.unwrap())
        .enable_pdl(kUsePDL)(selected_kernel, params);
  }
};

}  // namespace
