# Interface: h200_diffusion_group_norm_silu__multi_shape

- Kernel slug: `h200_diffusion_group_norm_silu__multi_shape`
- Op type: `group_norm_silu`
- Target GPU: NVIDIA H200 (Hopper / SM90)
- Wrapped SGLang entry points (both preserved):
  - `sglang.jit_kernel.diffusion.triton.group_norm_silu:triton_group_norm_silu`
  - `sglang.jit_kernel.diffusion.group_norm_silu:apply_group_norm_silu`

## Final wrapper signature(s)

`src/register.py:optimized_wrapper(*args, **kwargs)` preserves BOTH callsites:
- triton form: `optimized_wrapper(x, weight, bias, num_groups=int, eps=float)` -> Tensor
- apply form:  `optimized_wrapper(x, norm: nn.GroupNorm, activation: nn.SiLU)` -> Tensor

Native CUDA kernel: `src/group_norm_silu.cuh` exposes
`GroupNormSiluKernel<DType, kUsePDL>::run(...)` (SMALL, single-CTA) and `::run_large(...)`
(LARGE, 3-stage), built + exported via SGLang `jit_kernel` / tvm-ffi (`load_jit` +
`make_cpp_args`); NOT `torch.utils.cpp_extension`; compile flags = SGLang defaults
(`-std=c++20 -O3 --expt-relaxed-constexpr -DSGL_CUDA_ARCH`), NO `--use_fast_math`. The
workspace `.cuh` is built via an absolute `cuda_files` path (M5 export moves it to
`csrc/diffusion/`). PDL templated, OFF in this candidate.

## Per-shape dispatch table (which path handles which bucket)

`group_size = (channels / num_groups) * spatial`. Decision (measured, ion8-h200 GPU7):

| Bucket | Condition | Path | Why |
|---|---|---|---|
| tiny / small / medium | `group_size < 1<<16` (65536) | candidate SMALL (one CTA per (batch,group), 2-pass) | low launch overhead; baseline is overhead-bound here -> 1.2-2.7x |
| medium-large | `1<<16 <= group_size < 900,000` | candidate LARGE (3-stage multi-CTA, persistent, half8, channel-hoisted affine) | high SM utilization; still beats baseline (1.0-2.1x) |
| giant (BW-bound) | `group_size >= 900,000` | SGLang Triton baseline (fallback) | baseline is near-peak (~4000 GB/s ~= 84% of 4.8 TB/s); candidate large path is compute-bound (~2550 GB/s) and loses there |

Clean measured crossover: all candidate wins had `group_size <= 884,736`; all losses had
`group_size >= 983,040`. Threshold `_GIANT_THRESH = 900_000`. See `docs/dispatch.md`.

## Fallback cases (route to SGLang baseline)

Non-fp16/bf16 dtype (e.g. fp32), grad-enabled / `requires_grad`, non-contiguous input,
`ndim` not in 2..5, `channels % num_groups != 0`, weight/bias not 1-D `(channels,)` /
dtype mismatch / not CUDA, apply-form with non-affine GroupNorm / missing weight or bias /
inplace SiLU, group_size >= `_GIANT_THRESH`, or any kernel exception -> SGLang baseline
(`triton_group_norm_silu` / `apply_group_norm_silu`). The candidate never returns an
incorrect result for an unsupported signature.

## Tolerance methodology

Oracle `F.silu(F.group_norm(x, num_groups, weight, bias, eps))` at the per-case `eps`
(prod 1e-6, regression 1e-5). Per-dtype tolerances from the SGLang reference test:
fp16 `(3e-3, 3e-3)`, bf16 `(7e-2, 2e-2)`, fp32 `(1e-5, 1e-5)`. `tests/test_correctness.py`
asserts candidate-vs-oracle (primary) + baseline-vs-oracle (sanity) + candidate-vs-baseline
(parity, 2x) + NaN/Inf, over 110 cases (96 prod + 14 regression). Status: 110/110 pass
(KDA_RUN_CORRECTNESS=1, no_grad, ion8-h200 GPU7).

## Benchmark command + latency formula

`python benchmark.py --mode both --shapes prod --entry triton --out <csv> --host ion8-h200 --gpu 7`
(runs under `torch.no_grad()` = the inference callsite; CUDA-event timing, warmup25/iters100).
Headline = geometric mean of per-shape (baseline_median_us / candidate_median_us).

## Result (ion8-h200 GPU 7, idle, no_grad; canonical `benchmark.csv`)

- geomean speedup vs SGLang Triton baseline = **1.4487x** over the 48 production shapes
  (triton entry); canonical `benchmark.csv` records median/mean/std/min/p10/p90 for BOTH
  baseline and candidate + a per-row `path` column (12 small / 24 large / 12 baseline_giant).
- Correctness: 110/110 (strict `KDA_STRICT_CANDIDATE=1`, proving the native path ran) + a
  fallback matrix (storage-offset/misaligned/non-contiguous/grad/requires_grad/non-affine/
  inplace-SiLU/fp32 all fall back + correct).
- Hardening (round-1 review): `_can_use` rejects `storage_offset!=0` and 16-byte-misaligned
  data pointers (`_aligned()`); strict mode surfaces candidate failures instead of silent fallback.
- Physical SGLang export VALIDATED in a HEAD-isolated worktree (relative `load_jit`, public
  `apply_group_norm_silu` wired to the candidate, non-recursive fallback): in-SGLang correctness
  matrix passes + smoke `[1,512,3,128,40]` = 3.55x. See `docs/sglang_jit_export.md`.

## Roofline / completion (active bound per bucket)

- small/medium: launch/latency-overhead-bound (small ops ~38-130µs dominated by overhead);
  the candidate reduces overhead + vectorizes -> near the latency floor (1.2-2.7x).
- giant: HBM-bandwidth-bound. The SGLang baseline reaches ~4000 GB/s ~= 84% of the H200's
  ~4.8 TB/s peak on ~3N traffic -> near the attainable bound for a two-read groupnorm; the
  candidate is routed there. NCU refuted the L2-residency / 2N-traffic lever (the candidate
  large path is compute-bound, dram 31%, not BW-bound). A simple `x*2` copy hits ~4200 GB/s,
  confirming the baseline is near-peak on the giants.
- Conclusion: each important bucket is near its active bound (small via the candidate, giant
  via the near-peak baseline). geomean 1.45x is a real win, not a no-go.

## Source lineage

- Pattern mirror: `python/sglang/jit_kernel/csrc/diffusion/qknorm_rope.cuh` (Params + grid_constant,
  TensorMatcher, LaunchKernel, AlignedVector, warp::reduce_sum).
- Ideas consulted (Codex/KernelWiki): SGLang PR #23938 (scalar-affine apply), #22814 (orig Triton),
  PyTorch `RowwiseMomentsCUDAKernel`, Apex FastLayerNorm (persistent multi-CTA). Recorded in
  `docs/draft.md` + `solutions.jsonl`.

## Evidence Requirements (satisfied)
- final wrapper signature(s): above.
- per-shape dispatch table: above + `docs/dispatch.md`.
- fallback cases: above.
- tolerance methodology: above.
- benchmark command + latency formula: above.
- source lineage: above.
