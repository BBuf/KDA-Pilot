// Native CUDA candidate for the two SGLang diffusion rotary-embedding kernels,
// built through SGLang's jit_kernel / tvm-ffi stack (NOT torch.utils.cpp_extension).
// Mirrors the launcher/validation style of csrc/diffusion/qknorm_rope.cuh.
//
// Two distinct device kernels behind shared host glue:
//   * StandardRopeKernel  -- apply_rotary_embedding: adjacent-pair (2i,2i+1)
//     rotation, bf16/fp16 x, fp32 (T, head_size/2) cos/sin shared across heads,
//     fp32 math, rounding only on the final store. Functional: writes a caller-
//     allocated `out`, never mutates inputs.
//   * Ltx2SplitRopeKernel -- apply_ltx2_split_rotary_emb: split-half rotation,
//     bf16 x, per-head NON-contiguous (B, num_heads, S, half) bf16 cos/sin indexed
//     by real strides, with the deliberate intermediate (x*cos)->bf16->fp32
//     rounding before the fp32 sin term.
//
// Compile flags follow the SGLang jit_kernel build (no --use_fast_math).

#include <sgl_kernel/tensor.h>

#include <sgl_kernel/runtime.cuh>
#include <sgl_kernel/type.cuh>
#include <sgl_kernel/utils.cuh>

#include <dlpack/dlpack.h>

#include <algorithm>
#include <cstdint>
#include <type_traits>

namespace {

constexpr uint32_t kThreadsPerBlock = 256;

// Cap the grid; the kernels use a grid-stride loop so any total is covered.
constexpr int64_t kMaxBlocks = 262144;

template <typename T>
inline uint32_t grid_for(int64_t total) {
  const int64_t needed = device::div_ceil(total, static_cast<int64_t>(kThreadsPerBlock));
  return static_cast<uint32_t>(std::min<int64_t>(needed, kMaxBlocks));
}

// ---------------------------------------------------------------------------
// Standard adjacent-pair RoPE
// ---------------------------------------------------------------------------
struct StdRopeParams {
  void* __restrict__ out;
  const void* __restrict__ x;
  const float* __restrict__ cos;
  const float* __restrict__ sin;
  int64_t total_pairs;   // N * H * half
  int64_t x_row_stride;  // H * D (elements)
  uint32_t H;
  uint32_t D;
  uint32_t half;         // D / 2
  uint32_t num_tokens;   // T (cos rows)
};

template <typename DType>
__global__ void standard_rope_kernel(const StdRopeParams __grid_constant__ params) {
  using namespace device;
  const auto out = params.out;
  const auto xp = params.x;
  const auto cosp = params.cos;
  const auto sinp = params.sin;
  const int64_t total_pairs = params.total_pairs;
  const int64_t x_row_stride = params.x_row_stride;
  const uint32_t H = params.H;
  const uint32_t D = params.D;
  const uint32_t half = params.half;
  const uint32_t num_tokens = params.num_tokens;

  const int64_t stride = static_cast<int64_t>(gridDim.x) * blockDim.x;
  for (int64_t gid = static_cast<int64_t>(blockIdx.x) * blockDim.x + threadIdx.x; gid < total_pairs;
       gid += stride) {
    const uint32_t i = static_cast<uint32_t>(gid % half);
    const int64_t tmp = gid / half;
    const uint32_t h = static_cast<uint32_t>(tmp % H);
    const int64_t row = tmp / H;
    const int64_t token = row % num_tokens;

    const int64_t x_base = row * x_row_stride + static_cast<int64_t>(h) * D;
    const int64_t e0 = x_base + 2 * static_cast<int64_t>(i);
    const int64_t e1 = e0 + 1;

    const float x1 = cast<fp32_t>(load_as<DType>(xp, e0));
    const float x2 = cast<fp32_t>(load_as<DType>(xp, e1));
    const float c = cosp[token * half + i];
    const float s = sinp[token * half + i];

    // Match the baseline's tl.fma ordering: x1*c then fused -x2*s, etc.
    const float o1 = fmaf(-x2, s, x1 * c);
    const float o2 = fmaf(x1, s, x2 * c);

    store_as<DType>(out, cast<DType>(o1), e0);
    store_as<DType>(out, cast<DType>(o2), e1);
  }
}

template <typename DType>
struct StandardRopeKernel {
  static void run(
      tvm::ffi::TensorView out,
      tvm::ffi::TensorView x,
      tvm::ffi::TensorView cos,
      tvm::ffi::TensorView sin) {
    using namespace host;

    auto N = SymbolicSize{"N"};
    auto H = SymbolicSize{"H"};
    auto D = SymbolicSize{"D"};
    auto T = SymbolicSize{"T"};
    auto Half = SymbolicSize{"half"};
    auto device = SymbolicDevice{};
    device.set_options<kDLCUDA>();

    TensorMatcher({N, H, D}).with_dtype<DType>().with_device(device).verify(x).verify(out);
    TensorMatcher({T, Half}).with_dtype<float>().with_device(device).verify(cos).verify(sin);

    const int64_t n = N.unwrap();
    const auto h = static_cast<uint32_t>(H.unwrap());
    const auto d = static_cast<uint32_t>(D.unwrap());
    const auto t = static_cast<uint32_t>(T.unwrap());
    const auto half = static_cast<uint32_t>(Half.unwrap());
    RuntimeCheck(d % 2 == 0, "head_size must be even");
    RuntimeCheck(d == 2 * half, "head_size must equal 2 * cos width");
    RuntimeCheck(t != 0 && n % t == 0, "N must be a positive multiple of num_tokens");

    const int64_t total_pairs = n * static_cast<int64_t>(h) * half;
    const auto params = StdRopeParams{
        .out = out.data_ptr(),
        .x = x.data_ptr(),
        .cos = static_cast<const float*>(cos.data_ptr()),
        .sin = static_cast<const float*>(sin.data_ptr()),
        .total_pairs = total_pairs,
        .x_row_stride = static_cast<int64_t>(h) * d,
        .H = h,
        .D = d,
        .half = half,
        .num_tokens = t,
    };
    LaunchKernel(grid_for<DType>(total_pairs), kThreadsPerBlock, device.unwrap())(
        standard_rope_kernel<DType>, params);
  }
};

// ---------------------------------------------------------------------------
// LTX-2 split-half RoPE
// ---------------------------------------------------------------------------
struct Ltx2RopeParams {
  void* __restrict__ out;
  const void* __restrict__ x;
  const void* __restrict__ cos;
  const void* __restrict__ sin;
  int64_t total;        // B * S * H * half
  int64_t x_outer;      // inner = H * D (elements between (b,s) rows of x)
  int64_t cos_stride_b;
  int64_t cos_stride_h;
  int64_t cos_stride_s;  // cos/sin last-dim stride is 1
  uint32_t S;
  uint32_t H;
  uint32_t half;
  uint32_t D;            // 2 * half
};

template <typename DType>
__global__ void ltx2_split_rope_kernel(const Ltx2RopeParams __grid_constant__ params) {
  using namespace device;
  const auto out = params.out;
  const auto xp = params.x;
  const auto cosp = params.cos;
  const auto sinp = params.sin;
  const int64_t total = params.total;
  const int64_t x_outer = params.x_outer;
  const int64_t cs_b = params.cos_stride_b;
  const int64_t cs_h = params.cos_stride_h;
  const int64_t cs_s = params.cos_stride_s;
  const uint32_t S = params.S;
  const uint32_t H = params.H;
  const uint32_t half = params.half;
  const uint32_t D = params.D;

  const int64_t stride = static_cast<int64_t>(gridDim.x) * blockDim.x;
  for (int64_t gid = static_cast<int64_t>(blockIdx.x) * blockDim.x + threadIdx.x; gid < total;
       gid += stride) {
    const uint32_t j = static_cast<uint32_t>(gid % half);
    const int64_t tmp = gid / half;
    const uint32_t h = static_cast<uint32_t>(tmp % H);
    const int64_t tmp2 = tmp / H;
    const uint32_t s = static_cast<uint32_t>(tmp2 % S);
    const int64_t b = tmp2 / S;

    const int64_t x_base = (b * S + s) * x_outer + static_cast<int64_t>(h) * D;
    const int64_t cidx =
        b * cs_b + static_cast<int64_t>(h) * cs_h + static_cast<int64_t>(s) * cs_s + j;

    const float xf = cast<fp32_t>(load_as<DType>(xp, x_base + j));
    const float xs = cast<fp32_t>(load_as<DType>(xp, x_base + half + j));
    const float c = cast<fp32_t>(load_as<DType>(cosp, cidx));
    const float sn = cast<fp32_t>(load_as<DType>(sinp, cidx));

    // Deliberate intermediate bf16 rounding of (x * cos) before the fp32 sin term.
    const float of = cast<fp32_t>(cast<DType>(xf * c)) - xs * sn;
    const float og = cast<fp32_t>(cast<DType>(xs * c)) + xf * sn;

    store_as<DType>(out, cast<DType>(of), x_base + j);
    store_as<DType>(out, cast<DType>(og), x_base + half + j);
  }
}

template <typename DType>
struct Ltx2SplitRopeKernel {
  static void run(
      tvm::ffi::TensorView out,
      tvm::ffi::TensorView x,
      tvm::ffi::TensorView cos,
      tvm::ffi::TensorView sin) {
    using namespace host;

    auto B = SymbolicSize{"B"};
    auto S = SymbolicSize{"S"};
    auto Inner = SymbolicSize{"inner"};
    auto Hh = SymbolicSize{"num_heads"};
    auto Half = SymbolicSize{"half"};
    auto Sb = SymbolicSize{"cos_stride_b"};
    auto Sh = SymbolicSize{"cos_stride_h"};
    auto Ss = SymbolicSize{"cos_stride_s"};
    auto device = SymbolicDevice{};
    device.set_options<kDLCUDA>();

    TensorMatcher({B, S, Inner}).with_dtype<DType>().with_device(device).verify(x).verify(out);
    // cos/sin: (B, num_heads, S, half), last-dim stride 1 (may be non-contiguous overall).
    TensorMatcher({B, Hh, S, Half})
        .with_strides({Sb, Sh, Ss, 1})
        .with_dtype<DType>()
        .with_device(device)
        .verify(cos)
        .verify(sin);

    const int64_t b = B.unwrap();
    const auto s = static_cast<uint32_t>(S.unwrap());
    const int64_t inner = Inner.unwrap();
    const auto hh = static_cast<uint32_t>(Hh.unwrap());
    const auto half = static_cast<uint32_t>(Half.unwrap());
    const auto d = 2u * half;
    RuntimeCheck(inner == static_cast<int64_t>(hh) * d, "inner_dim must equal num_heads * 2 * half");

    // Size-1 leading dim has its stride check skipped, so guard cos_stride_b.
    const int64_t cs_b = Sb.has_value() ? Sb.unwrap() : 0;

    const int64_t total = b * s * static_cast<int64_t>(hh) * half;
    const auto params = Ltx2RopeParams{
        .out = out.data_ptr(),
        .x = x.data_ptr(),
        .cos = cos.data_ptr(),
        .sin = sin.data_ptr(),
        .total = total,
        .x_outer = inner,
        .cos_stride_b = cs_b,
        .cos_stride_h = Sh.unwrap(),
        .cos_stride_s = Ss.unwrap(),
        .S = s,
        .H = hh,
        .half = half,
        .D = d,
    };
    LaunchKernel(grid_for<DType>(total), kThreadsPerBlock, device.unwrap())(
        ltx2_split_rope_kernel<DType>, params);
  }
};

}  // namespace
