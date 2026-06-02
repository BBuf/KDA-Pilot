# Implementation Draft — h200_diffusion_group_norm_silu__multi_shape

KDA optimization of SGLang's fused GroupNorm + SiLU diffusion-VAE kernel on NVIDIA H200
(Hopper, SM90). This draft records the recovered baseline contract (K/R/W), the design
directions, and the evidence/decision log. Code, benchmarks, and profiles stay in this
folder. Authored in RLCR Round 0 (baseline recovery; no GPU work yet).

## K — Kernel semantics and callsite contract

Two public entry points (recovered from the local SGLang checkout at
`/Users/bbuf/工作目录/Common/sglang`):

1. `sglang.jit_kernel.diffusion.group_norm_silu.apply_group_norm_silu(x, norm: nn.GroupNorm, activation: nn.SiLU) -> Tensor`
   - Fast path taken iff: `x.is_cuda` and `not torch.is_grad_enabled()` and `not x.requires_grad`
     and `isinstance(norm, nn.GroupNorm)` and `isinstance(activation, nn.SiLU)` and
     `not activation.inplace` and `norm.affine` and `norm.weight is not None` and `norm.bias is not None`.
   - On the fast path it calls `triton_group_norm_silu(x, norm.weight, norm.bias, num_groups=norm.num_groups, eps=norm.eps)`.
   - Otherwise returns `activation(norm(x))` (the eager fallback).

2. `sglang.jit_kernel.diffusion.triton.group_norm_silu.triton_group_norm_silu(x, weight, bias, num_groups, eps=1e-5) -> Tensor`
   - Support gate `_can_use_triton_group_norm_silu`: `x.is_cuda`, no grad, `x.dtype in {fp16,bf16,fp32}`,
     `x.ndim in (2,3,4,5)`, `x.shape[1] % num_groups == 0`, `weight`/`bias` are 1-D CUDA tensors with
     `dtype == x.dtype` and `shape == (channels,)`. If the gate fails it computes
     `F.silu(F.group_norm(x, num_groups, weight, bias, eps))` (native fallback).

Math (per the GroupNorm + SiLU definition):
`y = silu(normalize(x) * weight[ch] + bias[ch])`, `silu(z) = z * sigmoid(z)`,
`normalize` uses per-group mean/var over `group_size` elements.

Memory layout (critical): `x` is made `contiguous()` as `[B, C, *spatial]`. One group is a
CONTIGUOUS block of `group_size = channels_per_group * spatial` elements, where
`channels_per_group = C / num_groups` and `spatial = prod(shape[2:])` (or `1` for 2-D).
`group_base = b*C*spatial + g*group_size`. The affine `weight`/`bias` are indexed PER CHANNEL:
for an element at offset `i` within a group, `channel = g*channels_per_group + (i // spatial)`.

### Baseline algorithm (the thing we replace / benchmark against)
Gated by `_LARGE_GROUP_THRESHOLD = 1 << 18 = 262144` (in `group_size` elements):
- one-pass (`group_size < threshold`): grid `(num_groups, batch)`. For the production `B=1`,
  `num_groups=32` shapes this is **only 32 CTAs** on a 132-SM H200. Each CTA reduces its whole
  group (loop over `group_size` in `BLOCK_SIZE<=4096` steps), then RE-READS the group to apply
  normalize + affine + SiLU. `x` is read twice inside the kernel.
- chunked (`group_size >= threshold`): THREE Triton launches — stats (per-chunk partial
  sum + sumsq into fp32 scratch), finalize (mean/rstd), apply (re-read `x`, normalize, SiLU).
  A scalar-affine fast path is used when `spatial % CHUNK == 0 and chunks_per_row >= 64`
  (each chunk lies within one channel so `weight`/`bias` are scalar per chunk). `x` is read
  twice from HBM plus the partial buffers (~3N traffic).

## R — Reference / correctness contract

- Oracle (ground truth): `F.silu(F.group_norm(x, num_groups, weight=weight, bias=bias, eps=eps))`,
  evaluated at the SAME `eps` as the candidate call. This is exactly the SGLang reference test's
  `_reference`. Cross-check against an explicit FP32 reference where practical.
- Source test adapted: `python/sglang/jit_kernel/tests/diffusion/test_group_norm_silu.py`.
- Per-dtype tolerances (verbatim from the SGLang test): fp16 `(atol=3e-3, rtol=3e-3)`,
  bf16 `(7e-2, 2e-2)`, fp32 `(1e-5, 1e-5)`.
- Regression grid (must pass): `(2,64,32,32)` image_2d, `(1,64,4,16,16)` video_3d, `(4,128)` token_2d
  across `[fp16, bf16, fp32]` at `eps=1e-5`; the `apply_*` wrapper test runs only on the 2D/3D
  shapes and `[fp16, bf16]`; large-tile bf16 `(1,128,20,256,256)`. All `num_groups=32`.
- Candidate error must not exceed a small multiple of the reference BF16/FP16 quantization noise
  vs FP32. NaN/Inf are always rejected.

## W — Workload (FIXED — use verbatim, do not broaden)

Source: `docs/captured_shapes_h200.jsonl` (96 records = 48 `apply_group_norm_silu` + 48
`triton_group_norm_silu`; the same 48 unique x-shapes appear under both entry points).
All HunyuanVideo VAE, **B=1, fp16, num_groups=32, eps=1e-6**, 5-D `[1, C, T, H, W]`:
`C in {128,256,512}` (`channels_per_group in {4,8,16}`), `T in {2,3,5,9,17}`,
`H/W` from `12x10` up to `256x256`.

Size spread is enormous and dominates the geomean weighting (every shape weighted equally):
- smallest `[1,512,2,12,10]` = 122,880 elems (240 KB) — launch/latency bound.
- largest `[1,256,17,256,256]` = 285,212,672 elems (~570 MB fp16) and `[1,128,17,256,256]` (~285 MB)
  — pure HBM-bandwidth bound; baseline ~3N traffic, floor 2N.

Approximate baseline path split (by `group_size` vs `2^18`):
- one-pass (small/medium): e.g. `[1,512,2,12,10]` (gs=3,840), `[1,512,5,32,32]` (gs=81,920).
- chunked (large): e.g. `[1,512,9,128,128]` (gs=2,359,296), `[1,256,17,256,256]` (gs=8,912,896).

Benchmark methodology (AC-5): warmup + repeated timing; per shape report median/mean/std/min/p10/p90;
baseline vs candidate from the SAME verified-idle H200 + container; final headline = geometric mean
of per-shape median-latency speedups (outcome metric, not a pass/fail threshold). Record host/GPU
id/model and idleness before+after. Completion governed by roofline + NCU (AC-6).

## Candidate directions (ranked; to be validated by evidence in M3)

1. Deterministic two-pass native CUDA, occupancy-aware persistent grid (FIRST candidate).
   - Stats pass: per-(batch,group) `sum` + `sum_of_squares` into fp32 scratch, many CTAs per
     large group via grid-stride (`runtime::get_sm_count` * `get_blocks_per_sm`); then mean/rstd;
     then apply pass (re-read `x`, normalize, affine, SiLU). Removes the 32-CTA ceiling; simple numerics.
2. Vectorized `LDG.128`/`STG.128` (8 fp16/transaction) with float accumulation; correct tail +
   channel-boundary handling; scalar-affine fast path when a tile lies within one channel.
3. Reduction scheme: sum/sum-of-squares for fp16/bf16; Welford or deterministic tree reduction for
   fp32 if `(1e-5,1e-5)` tolerance requires it. Avoid nondeterministic atomics on the fp32 path.
4. Large-shape traffic reduction toward the 2N floor — group-stationary schedule to keep a group's
   data L2-resident between stats and apply. HYPOTHESIS ONLY (see Risks); confirm/refute with
   measured `dram__bytes` / L2-hit, not assumed.
5. Dispatcher with the minimum evidence-justified buckets (small/medium occupancy-bound, large
   bandwidth-bound, maybe tiny launch-bound). Only if evidence shows buckets need different tradeoffs.
6. Optional PDL (`enable_pdl` via `is_arch_support_pdl()`) and optional SM90 thread-block clusters —
   A/B test each; keep only on measured wins (PDL hurt isolated launch latency in the qknorm pilot;
   cluster launch depends on whether `host::LaunchKernel` exposes cluster attributes).

## Risks (Claude + Codex first-pass)

- L2-residency (direction 4) is a hypothesis: 32 concurrent groups exceed the ~50 MB L2 and
  "all-stats-then-all-apply" mostly re-reads from HBM; needs an explicit group-stationary schedule
  and measured `dram__bytes` proof.
- Nondeterministic reductions can break the tight fp32 `(1e-5,1e-5)` tolerance -> prefer deterministic.
- Single-kernel inter-block sync risks deadlock (CTAs spinning on un-coscheduled CTAs) -> two-launch default.
- Vector lanes can straddle channel boundaries when `spatial` is not vector-aligned -> per-element
  channel or channel-aligned tiles. (All production `spatial` happen to be multiples of 8, but the
  regression grid `(4,128)` has spatial=1 and `group_size=4`, so the scalar/tail path must be correct.)
- `eps` differs: production `1e-6` vs regression `1e-5` -> pass per-case eps to both candidate and oracle.
- jit_kernel/tvm-ffi export is a real delivery risk (TensorMatcher validation, current-stream launch,
  cache_once, scratch allocation, ndim 2..5 mapping, fallback).
- Non-contiguous inputs: the production shapes are all contiguous (`float16C`), but the fallback must
  still route non-contiguous/strided/grad/non-affine/missing-weight/inplace-SiLU to the SGLang baseline.
  (A strided-read kernel that skips the baseline `.contiguous()` copy is a known lever for the norm
  family, but it is OUT OF SCOPE here because every captured production input is contiguous.)

## DEC-1 (default applied)
fp16-first + correctness-preserving fallback: the native CUDA path optimizes the fp16 production
shapes; bf16/fp32 and any non-production signature satisfy correctness via fallback to the SGLang
baseline. User may override toward general multi-dtype native coverage at review.

## Prior-art notes (to be expanded in M3 task4 via KernelWiki / Codex)
- Canonical CUDA jit_kernel pattern to mirror: `python/sglang/jit_kernel/csrc/diffusion/qknorm_rope.cuh`
  (Params + `__grid_constant__`, templated `__global__`, `XxxKernel<...>::run(TensorView..., float eps)`,
  `host::TensorMatcher`/`SymbolicSize`/`SymbolicDevice`/`SymbolicDType` validation, occupancy-aware grid,
  `host::LaunchKernel(...).enable_pdl(...)`, `AlignedVector` vectorized loads, `warp::reduce_sum`).
- Sibling promoted kernels `h200_diffusion_qknorm_rope__multi_shape`, `h200_diffusion_norm_infer__multi_shape`
  — reference for `register.py -> load_jit` resolution and the validated install path.
- KernelWiki queries to run: `--tag group-norm`, `--symptom memory-bound --tag norm`,
  `"group norm silu fused vae blackwell"`. Record kept/rejected with page id / PR URL.

## jit_kernel build/export API (recovered from sglang/jit_kernel/utils.py + diffusion/qknorm_rope.py)

- Python wrapper pattern (mirror `diffusion/qknorm_rope.py`):
  `@cache_once def _module(dtype): args = make_cpp_args(dtype, is_arch_support_pdl()); return load_jit("group_norm_silu", *args, cuda_files=[<.cuh>], cuda_wrappers=[("group_norm_silu", f"GroupNormSiluKernel<{args}>::run")])`.
  Then `module.group_norm_silu(x, weight, bias, y, num_groups, eps)` invokes the launcher.
- `make_cpp_args` maps torch.dtype -> `fp16_t`/`bf16_t`/`fp32_t` and bool -> `true`/`false`; the
  CPPArgList str is `"fp16_t, true"` etc., used for the `XxxKernel<...>` template instantiation.
- `load_jit` flags are FIXED by sglang: `_get_default_target_flags()` = `[-DSGL_CUDA_ARCH=..., -std=c++20, -O3, --expt-relaxed-constexpr]` (+ `-DUSE_ROCM` on HIP). DEFAULT_INCLUDE = `jit_kernel/include` (the `sgl_kernel/*` headers). NO `--use_fast_math` (satisfies AC-3). header_only=True wraps via `TVM_FFI_DLL_EXPORT_TYPED_FUNC`.
- KEY DEV TRICK: `load_jit` does `(KERNEL_PATH/"csrc"/f).resolve()`; pathlib makes an ABSOLUTE `f`
  override the csrc prefix. So I pass `cuda_files=[<absolute path to src/group_norm_silu.cuh>]` and
  build my WORKSPACE .cuh with the official load_jit + exact flags, WITHOUT putting it in sglang csrc.
  At M5 (post-loop export) the .cuh moves to `csrc/diffusion/` with a normal relative path.
- Launcher contract (mirror qknorm_rope.cuh): `GroupNormSiluKernel<DType, kUsePDL>::run(tvm::ffi::TensorView x, TensorView weight, TensorView bias, TensorView y, int64_t num_groups, double eps)`; validate with `host::TensorMatcher{...}.with_dtype<DType>().with_device(...).verify(...)`; grid via `runtime::get_sm_count` + `runtime::get_blocks_per_sm`; `host::LaunchKernel(blocks, threads, device).enable_pdl(kUsePDL)(kernel, params)`. Output `y` is pre-allocated in Python (`torch.empty_like(x)`).
- Includes available: `sgl_kernel/{tensor.h,runtime.cuh,type.cuh,utils.cuh,vec.cuh,warp.cuh}` at
  `python/sglang/jit_kernel/include/`. Use `AlignedVector<packed_t<DType>, N>` + `load_as`/`store_as`
  for vectorized fp16x8, `warp::reduce_sum` for warp reductions, `cast<fp32x2_t>` for fp16->fp32.

## Validated first-candidate kernel design (task4 / Codex gpt-5.5:high; see .humanize/kernel-agent/codex_task4_output.md)

TWO buckets from the start (evidence-justified: tiny shapes are launch-bound, giants are
decomposition/occupancy-bound; baseline gives only ~215 GB/s):

A. LARGE bucket (`group_size >= LARGE_THRESH`, ~64K-128K elems): deterministic 3-stage.
   - Tiling: `BLOCK_THREADS=256`, `VEC=8` (half8 / 128-bit), `VECS_PER_THREAD=4` -> one CTA covers
     `256*4*8 = 8192` elems. `rows = B*num_groups`; `chunks_per_row = ceil(group_size/8192)`;
     `total_tasks = rows*chunks_per_row` (e.g. [1,256,17,256,256] -> 32*1088 = 34,816 tasks, saturates 132 SMs).
   - Stage 1 (stats): persistent grid `= min(total_tasks, blocks_per_sm*sm_count)` via
     `runtime::get_blocks_per_sm`; grid-stride `task=blockIdx.x; task<total_tasks; task+=gridDim.x`;
     `row=task/chunks_per_row, chunk=task%chunks_per_row`. Each CTA reduces its 8192-elem chunk to a
     block `{sum,sumsq}` (fp32, warp::reduce_sum + shared), writes `partial_sum[row,chunk]`,
     `partial_sumsq[row,chunk]` (fp32 scratch, NO atomics -> deterministic).
   - Stage 2 (finalize): launch `rows` CTAs (one per row); each reduces its `chunks_per_row` partials
     in INCREASING chunk id (fixed order); `mean=sum/n; var=max(sumsq/n - mean*mean, 0); rstd=rsqrt(var+eps)`;
     write `mean[row], rstd[row]`. Tiny stage; determinism > occupancy.
   - Stage 3 (apply): same task mapping; reload `mean/rstd[row]`; re-read x chunk (vectorized half8),
     `y = silu((x-mean)*rstd*w[ch] + b[ch])`; vectorized store. Use streaming/`evict_last` cache hints
     (x is one-use; mean/rstd/w/b reused). Scalar-affine fast path when the 8-elem vector lies within
     one channel (`vec_start/spatial == (vec_start+7)/spatial`), else per-lane channel = `g*cpg + (i//spatial)`.

B. SMALL bucket (`group_size < LARGE_THRESH`): single kernel, NO scratch, NO extra launches.
   - One CTA per (batch,group) [grid = rows]; CTA loops the group twice (reduce, then apply) keeping
     mean/rstd in shared/registers. For very tiny (`group_size <= 1024`, e.g. regression (4,128) gs=4):
     one warp per group, possibly multiple groups per CTA, to cut overhead (not to saturate SMs).
   - This avoids the 3-launch + scratch overhead that would dominate launch-bound tiny shapes.

Reduction numerics: fp32 `sum`+`sumsq`; biased (`/n`); `var=max(sumsq/n - mean^2, 0)`; `rsqrt(var+eps)`.
sum/sumsq is the fast first path for fp16/bf16 production. For fp32 regression `(1e-5,1e-5)` adversarial
cancellation, add a Welford/deterministic-combine fallback only IF a case fails (PyTorch uses Welford in
`RowwiseMomentsCUDAKernel`). DEC-1 default: fp32/bf16 may just fall back to the SGLang baseline.

Vectorization guards (correctness): half8 requires 16-byte alignment (base ptr + `group_base+i` divisible
by 8); if `group_size%8!=0` do `floor/8*8` vectorized then scalar tail; NEVER half8 when `spatial==1` or
`group_size<8` (regression (4,128)) -> scalar/half2. sigmoid: accuracy-compatible (no `__expf`/fast-sigmoid;
no `--use_fast_math`). 64-bit pointer offsets. Output `y` allocated in Python (`torch.empty_like(x)`), not in-place.

Dispatcher (Python register.py): pick bucket by `group_size` vs `LARGE_THRESH` (tune the threshold by
benchmark, start ~131072 = 1<<17 i.e. half the baseline's 1<<18). Fall back to SGLang baseline for any
unsupported dtype/layout/ndim/etc. Mirror baseline `_can_use_*` gate.

Prior art kept: qknorm_rope.cuh (structure/AlignedVector/warp::reduce_sum/occupancy/LaunchKernel);
SGLang PR #23938 (scalar-affine apply, ~74% H200 DRAM in its bench); PR #22814 (orig Triton);
PyTorch group_norm_kernel.cu RowwiseMomentsCUDAKernel (Welford fallback); Apex FastLayerNorm
(CTAS_PER_ROW / persistent multi-CTA / vector traits); KernelWiki technique-vectorized-loads (128-bit,
evict_last/streaming cache). NOTE: #23938 reportedly reached ~74% DRAM on apply, yet the MEASURED remote
baseline is ~215 GB/s on these shapes -> the remote baseline likely predates/doesn't hit that on the full
op; confirm the active bound with NCU in task8.

## Baseline measurements (ion8-h200, GPU 7, idle 0%util/100MB before+after; CUDA-event, warmup25/iters100)

Recorded in `benchmark.csv` (96 production cases). Median latency (triton entry; apply entry within ~1-4us):

| shape | numel (fp16) | baseline median | eff. BW @3N | path |
|---|---|---|---|---|
| [1,256,17,256,256] | 570 MB | 7955.6 us | ~215 GB/s | chunked |
| [1,128,17,256,256] | 285 MB | 4007.8 us | ~213 GB/s | chunked |
| [1,256,17,96,256]  | 214 MB | 3017.2 us | ~213 GB/s | chunked |
| [1,512,9,128,128]  | 151 MB | 2139.5 us | ~212 GB/s | chunked |
| [1,512,5,32,32]    | 5.2 MB |   53.5 us | ~294 GB/s | one-pass |
| [1,512,2,32,10]    | 0.6 MB |   37.8 us | launch-bound | one-pass |

CORRECTION (round 1): the numbers in THIS table were measured WITHOUT torch.no_grad(), so the
"baseline" was actually eager F.group_norm (the Triton fast path fell back). The REAL Triton baseline
(under no_grad) is near-peak (~4000 GB/s on giants); see BL-20260602, benchmark.csv, and docs/dispatch.md.
The table below is retained only as the record of that measurement bug.

KEY FINDING (SUPERSEDED — eager-fallback artifact): the SGLang baseline runs at only ~200-300 GB/s effective bandwidth on these shapes —
roughly 4-6% of the H200's ~4.8 TB/s HBM3e peak. The kernel is memory-bound but NOWHERE NEAR the
bandwidth bound. A BW-efficient native CUDA kernel (vectorized LDG.128/STG.128, high SM utilization,
deterministic two-pass) has large headroom: even ~2-3 TB/s would be ~10x on the large shapes, and the
2N floor would be more. Tiny shapes are launch/latency-bound (~38us) and need high grid utilization +
low launch overhead. This validates direction #1 (two-pass persistent CUDA) and #2 (vectorization) and
makes the L2-residency direction #4 a secondary refinement (the first-order win is just being BW-efficient).

## Evidence / decision log
- Round 0: baseline contract recovered (source read), correctness harness authored (110 cases),
  candidate directions ranked. solutions.jsonl seeded. Committed f5b143019.
- Round 1: remote H200 (ion8-h200, GPU 7) verified; sglang 0.5.12.dev472 + both baseline entries +
  ncu/nvcc present. Immutable baseline benchmark recorded (see table above) -> baseline is far below the
  BW bound, large headroom. Next: prior-art (task4) then first native CUDA candidate (task5/M2).
