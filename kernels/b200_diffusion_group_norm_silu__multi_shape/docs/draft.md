# K/R/W Recovery and Working Notes — b200_diffusion_group_norm_silu__multi_shape

Recovered from `prompt.md`, `../../docs/standalone_diffusion_benchmark.md`,
`../../docs/diffusion_kernel_rules.md`, `../../docs/diffusion_correctness_contract.md`,
`../../docs/diffusion_benchmark_shape_coverage.md`, and upstream SGLang sources,
before any kernel implementation.

## K — Kernel Semantics and Callsite Contract

Math: `y = silu(group_norm(x, num_groups, weight, bias, eps))`, where
`silu(t) = t * sigmoid(t)` and GroupNorm normalizes each (batch, group) slice of
`(C/G) * prod(spatial)` elements with fp32 mean/variance
(`var = E[x^2] - E[x]^2` in the upstream Triton implementation), then applies a
per-channel affine `y = (x - mean) * rsqrt(var + eps) * w[c] + b[c]`.

Upstream entry points (SGLang, source provider only):

1. `sglang.jit_kernel.diffusion.triton.group_norm_silu:triton_group_norm_silu(x, weight, bias, num_groups, eps=1e-5)`
   - Gate `_can_use_triton_group_norm_silu`: CUDA tensor, no grad, dtype in
     {fp16, bf16, fp32}, `x.ndim in (2,3,4,5)`, `C % num_groups == 0`,
     `weight`/`bias` 1-D CUDA tensors of dtype == x.dtype, shape `(C,)`.
   - On gate pass: `x_contiguous = x.contiguous()` (FULL materialization copy
     for channels-last inputs), then
     - `group_size < 2^18`: one-pass Triton kernel, grid `(num_groups, batch)`,
       `BLOCK_SIZE = min(4096, next_pow2(group_size))`, two in-kernel sweeps
       (stats, then normalize+affine+silu).
     - `group_size >= 2^18`: chunked pipeline: `_group_norm_stats_kernel`
       (grid `(B*G, chunks)`, 8192-elem chunks = BLOCK 4096 x 2) →
       `_group_norm_finalize_stats_kernel` (mean/rstd per row) →
       `_group_norm_apply_kernel` (or `_group_norm_apply_scalar_affine_kernel`
       when `spatial % 8192 == 0 and chunks_per_row >= 64`).
   - On gate fail: `F.silu(F.group_norm(x, num_groups, weight, bias, eps))`.
   - Upstream wraps the impl in `@register_custom_op(op_name="triton_group_norm_silu_cuda", out_shape="x")`
     (from `sglang.srt.utils.custom_op`) — must be shimmed locally to a no-op
     decorator for standalone runtime isolation.

2. `sglang.jit_kernel.diffusion.group_norm_silu:apply_group_norm_silu(x, norm, activation)`
   - Python gate: `x.is_cuda`, no grad mode, `x.requires_grad == False`,
     `isinstance(norm, nn.GroupNorm)`, `isinstance(activation, nn.SiLU)`,
     `not activation.inplace`, `norm.affine`, weight+bias present.
   - On pass: calls (1) with `norm.weight, norm.bias, norm.num_groups, norm.eps`.
   - On fail: eager `activation(norm(x))`.
   - Callsite reality (HunyuanVideo VAE): always passes the gate; `eps=1e-6`,
     `num_groups=32`, fp16, both contiguous NCDHW and channels-last-3d inputs.

Local benchmark ABI (DEC-2, single exported symbol, identical both sides):
`group_norm_silu(x, weight, bias, num_groups: int64, eps: double, out)` —
tvm-ffi `TensorView` args, output passed last (destination passing), launch on
`at::cuda::getCurrentCUDAStream()`. Workload rows carry `function` metadata for
which upstream entry they represent; both route to the same exported call.

## R — Correctness Oracle and Baseline Path

- Oracle: fp32 reference `silu(F.group_norm(x_f32, G, w_f32, b_f32, eps))`,
  computed from fp32 upcasts, compared in fp32, with per-dtype tolerances:
  fp16 `atol=3e-3, rtol=3e-3`; bf16 `atol=7e-2, rtol=2e-2`; fp32 `atol=rtol=1e-5`.
- Baseline path: copied upstream Triton implementation (exact upstream `main`
  SHA at recovery time; see `docs/baseline_source.md`), local edits limited to
  (a) `register_custom_op` no-op shim, (b) destination-passing of the final
  output (template forbids timed-path output allocation). The internal
  `.contiguous()` and scratch allocations stay (DEC-1: allocator-inclusive).
- Canonical regression grid (contract): `(2,64,32,32)` 2-D image,
  `(1,64,4,16,16)` 3-D video, `(4,128)` token (spatial=1, group_size=4!),
  `(1,128,20,256,256)` large-tile; all `num_groups=32`; fp16/bf16/fp32.
  Wrapper path covers 2-D + 3-D rows for fp16/bf16 with real nn modules
  (untimed), including the eager-fallback branch when the gate rejects.
- Hardening: poisoned output buffers before each run, NaN/Inf checks, stress
  rows (nonzero mean/large offset, near-zero variance, unaligned storage
  offset, channels-last per dtype, mixed `eps` 1e-5/1e-6).
- `required_matched_ratio = 1.0` — one failing row invalidates the run.

## W — Workload Shape Set and Benchmark Methodology

- Source of truth: 160 retained live capture rows
  (`git show 35bc2c6b4~1:kernels/b200_diffusion_group_norm_silu__multi_shape/docs/captured_shapes_b200.jsonl`),
  host ion-b200, preset hunyuanvideo (VAE), all fp16, `num_groups=32`, `eps=1e-6`:
  80 rows per entry point = 40 tensor configs x {contiguous NCDHW,
  channels-last-3d}. 5-D `[1, C, D, H, W]`, `C in {512,256,128}`,
  `D in {2,3,5,9,17}`, `H x W` from `12x10` to `256x256`. Group sizes
  `(C/32) * D * H * W` span a few thousand elements to ~4.5M — both baseline
  branches (one-pass and chunked) are exercised.
- All 160 rows are production rows with equal weight (DEC-4); regression-grid
  rows ride along as `production: false`.
- Benchmark: `bench/benchmark.py` = unmodified-policy copy of
  `docs/standalone_diffusion_benchmark_template.py`; config.toml settings
  (warmup 10, iterations 200, trials 7, inner 1..4096 targeting >=1000us
  samples, isolated subprocess, timeout 600s). Interleaved per-trial A/B with
  deterministic seeded order randomization; CUDA events; fresh inputs per
  trial; preallocated outputs; median/mean/std/min/p10/p90 per row; headline =
  equal-weight geomean over production rows; arithmetic mean secondary.
- Validity gates before tuning: A/A run (candidate aliased to baseline) must
  land in 0.98–1.02; GPU idle before/after each run; provenance recorded.
- Promotion gate: geomean > 1.0 AND no production row < 0.97x (DEC-3 +
  standing ruling; losing buckets dispatch to a baseline-equivalent path).

## Candidate Direction Ranking (initial, to re-rank on evidence)

1. Channels-last native path — read full contiguous `C`-rows per spatial
   position (NDHWC), accumulate all 32 group partial sums per CTA, second sweep
   normalizes+activates and writes NDHWC directly; skips the baseline's
   copy (~5 passes → 3 passes; ~1.6x roofline ceiling on large NC rows).
2. Contiguous medium-group underfill fix — split groups across CTAs
   (stats+apply two-kernel, fp32 atomics or partials) instead of the baseline's
   32 resident CTAs at B=1; re-derive the B200 crossover empirically.
3. Large-group chunked slimming — fuse finalize into apply, 16B vector ld/st,
   fewer intermediates.
4. Numerics: fp32 sum/sumsq hierarchical reduction (matches baseline class);
   Welford only if stress rows fail. Tail-safe shuffle masks.
5. Deferred pending NCU evidence: cluster/DSMEM cooperative single-kernel, PDL.
   Tensor-core/TMEM features irrelevant (reduction + elementwise kernel).

## Iteration 0 Context Refresh (KernelWiki / ncu-report-skill)

- `external/KernelWiki/SKILL.md` (cutoff 2026-04-27) read: query paths
  `scripts/query.py` (natural language / tags), `queries/by-problem.md` for
  symptom → technique. Relevant starting tags for this kernel family:
  memory-bound, low SM utilization, vectorization; tensor-core topics N/A.
  Will query for groupnorm/layernorm reduction patterns and NDHWC coalescing
  before candidate v2 implementation.
- `external/ncu-report-skill/SKILL.md` read: B200 = sm_100, CC 10.0, 148 SMs,
  192 GB HBM3e. One run = one `profile/<run>/` dir (harness/, reports/,
  analysis/, REPORT.md); compile harnesses with `-lineinfo`; use sm_100 metric
  names (`reference/08-b200-metric-names.md`); `--set full` + `--set source`;
  PM sampling for tail effects; read NCU rule engine (`--page details`) first.
- No NCU evidence exists yet; first profiling decision point arrives after the
  first real A/B table (only if results are non-obvious).

## Pre-Remote Review Outcomes (Codex, 2026-06-04)

- Blocker fixed: correctness suite now disables grad and pins the CUDA device
  (the baseline gate requires no-grad to take the fused Triton path; a
  production-path probe asserts the gate accepts workload rows).
- Blocker fixed: candidate `select_path` gained the `is_grad_enabled` /
  `requires_grad` guards for exact gate parity with the baseline.
- Hardening added: `gen_workloads.py` validates captured kwargs and the
  weight/bias/module argument metadata instead of assuming them (frozen
  workloads.json unchanged, sha256 verified).
- Noted semantic difference (deliberate): the candidate clamps negative
  variance to zero before `rsqrt`; the upstream Triton baseline does not.
  Strictly safer numerics for catastrophic-cancellation corner cases; watched
  by the fp32 / low-variance / zero-variance stress rows.
- Risk accepted: generic v0 is expected to be slow on the largest rows (one
  CTA per (batch, group)); the optimized regimes (split-CTA, channels-last
  native) are the next milestones and v0 remains the correctness safety net.

## Kept / Rejected Ideas Log

- Kept (pending evidence): directions 1–4 above.
- Rejected at planning time: porting the Triton baseline to CUDA as "the
  baseline" (would not be the upstream baseline; rules keep Triton baselines
  as Triton behind a matched adapter); two divergent exported symbols (DEC-2);
  `--use_fast_math` (upstream does not use it); tensor-core/TMEM approaches
  (wrong kernel class).
