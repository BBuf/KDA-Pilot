# Interface: b200_diffusion_cutedsl_norm_tanh_mul_add__multi_shape

- Kernel slug: `b200_diffusion_cutedsl_norm_tanh_mul_add__multi_shape`
- Op type: `cutedsl_norm_tanh_mul_add`
- Target GPU: NVIDIA B200
- Wrapped SGLang entry points:
- `sglang.jit_kernel.diffusion.cutedsl.norm_tanh_mul_add_norm_scale:fused_norm_tanh_mul_add`
- `sglang.jit_kernel.diffusion.cutedsl.norm_tanh_mul_add_norm_scale:fused_norm_tanh_mul_add_norm_scale`

## Export

`src/register.py` provides:

```python
KERNEL_SLUG = "b200_diffusion_cutedsl_norm_tanh_mul_add__multi_shape"
OP_TYPE = "cutedsl_norm_tanh_mul_add"

def optimized_wrapper(*args, **kwargs): ...

def register() -> dict: ...
```

## Recovered public signatures (final)

Both upstream entry points are `torch.library.custom_op`s (`sglang::fused_norm_tanh_mul_add`,
`sglang::fused_norm_tanh_mul_add_norm_scale`) with fake-tensor registrations; the shipped
integration preserves those registrations (only the kernel inside changes).

```python
fused_norm_tanh_mul_add(x, weight, bias, scale, shift, norm_type, eps=1e-5) -> Tensor
fused_norm_tanh_mul_add_norm_scale(
    x, weight, bias, scale, shift, weight2, bias2, scale2, norm_type, eps=1e-5
) -> tuple[Tensor, Tensor]
```

Semantics: `y = round_to_dtype(norm(x)) * tanh(scale) + shift`;
second entry point adds `y2 = round_to_dtype(norm2(round_to_dtype(y))) * (1 + scale2)`.
Norm reductions accumulate in fp32. Affine semantics: rms applies `weight` only
(`bias` ignored); layer applies affine only when BOTH `weight` and `bias` are tensors.
`tanh` is exact fp32 `tanhf` (no approximations; build has no `--use_fast_math`).

Public contract (identical in baseline copy and candidate dispatcher):
- `x`: `[B, S, D]`, dtype ∈ {fp16, bf16, fp32}, last-dim stride 1
- `scale`/`shift`/`scale2`: 3-D `[1|B, 1|S, D]`, last-dim stride 1 (1-D/2-D/4-D layouts raise `ValueError`)
- `weight`/`bias`/`weight2`/`bias2`: `None` or contiguous `[D]`
- `D % 256 == 0` and `D <= 8192` (unchanged from upstream); `norm_type` ∈ {`"layer"`, `"rms"`}

## Dispatch table (current)

| Route | Condition |
|---|---|
| native CUDA fast path (`src/norm_tanh_cuda/norm_tanh_mul_add.cuh` via SGLang `load_jit`/tvm-ffi) | CUDA tensors on one device; uniform dtype ∈ {bf16, fp16, fp32}; `x` contiguous `[B,S,D]`; modulation tensors `[1|B,1|S,D]` with last-dim stride 1, non-broadcast strides multiples of 8 elements; weight-likes `None`/`[D]` contiguous; `D % 256 == 0 && D <= 8192`; base pointers aligned to 8 elements; for the second entry point, effective affine pattern of (`weight2`,`bias2`) equals (`weight`,`bias`) |
| baseline fallback (`baseline/` CuTe-DSL copy, raw callables) | every other public-valid signature (mixed per-tensor dtypes, misaligned bases, unaligned outer strides, differing second-norm affine pattern, non-contiguous `x`, non-CUDA tensors) |
| `RuntimeError` | any would-be fallback when `KDA_REQUIRE_CANDIDATE=1` (anti-silent-fallback guard for benchmarks/tests) |

Native kernel structure: one CTA processes `KDA_ROWS_PER_CTA` rows (default 8), `D/8`
threads, vectorized 8-element loads/stores (128-bit fp16/bf16, 256-bit fp32), fp32
warp+CTA reductions, row-invariant `tanh(scale)` / `(1+scale2)` hoisted per CTA when the
effective seq stride is 0 (production layout `[1,1,D]`). PDL off by default
(`KDA_ENABLE_PDL=1` opt-in); `-lineinfo` only via `KDA_NVCC_LINEINFO=1` for profiling
builds (separate JIT cache key).

## Fallback cases

See dispatch table; fallbacks are exercised by `tests/test_correctness.py`
(`test_fallback_valid_signatures`, `test_second_norm_affine_pattern_routing`) and must
match the baseline in behavior class (same outputs within tolerance or same exception
type).

## Tolerance methodology used in tests

- Candidate vs baseline and candidate vs fp32 reference: `atol=rtol=5e-2` (fp16/bf16),
  `1e-5` (fp32).
- Dynamic quantization-noise bound: candidate max-abs-error vs the fp32 reference must
  not exceed `max(2 x baseline_error, 4 x dtype_eps x max|ref|)`.
- The fp32 reference reproduces baseline rounding points (normalized result rounded to
  the I/O dtype before modulation; second norm consumes rounded `y`) and baseline affine
  semantics; NaN/Inf checks on every output; NaN-injection and wrong-eps self-tests keep
  the validator honest.

## Source lineage

- Baseline copy: `baseline/` from SGLang `main@edb1b3f8f` (container `/sgl-workspace/sglang`,
  byte-identical to local recovery checkout @ `0689ba84b8` for all copied files; sha256
  table in `docs/baseline_source.md`).
- Candidate: workspace-owned `src/norm_tanh_cuda/norm_tanh_mul_add.cuh` +
  `src/norm_tanh_cuda/wrapper.py`, built with SGLang jit_kernel default flags
  (`-DSGL_CUDA_ARCH=1000 -std=c++20 -O3 --expt-relaxed-constexpr`, no fast-math),
  mirroring `python/sglang/jit_kernel/csrc/diffusion/qknorm_rope.cuh` idioms.

## Evidence (final)

- **Promotion arbiter (DISPATCH-SYMMETRIC in-SGLang drop-in — both routes in one patched
  checkout, env-toggled; contract-clean idle GPU 1): geomean 1.493×** — v1 1.596×/1.621×
  (geo 1.609×), v2 1.378×/1.393× (geo 1.385×) on the 4 captured zimage shapes; in-SGLang
  correctness PASS with the gate-verified fallback (`native_supported(...) is False`
  asserted + output-vs-reference within tolerance) (`docs/sglang_jit_export.md`,
  `export/sglang_drop_in.patch`, `export/arbiter_runs/*_r4.json`).
- Per-shape dispatch decision: BOTH entry points ship the native fast path (v2 meets
  the pre-registered integrated parity-or-better rule); PDL off; `KDA_ROWS_PER_CTA=8`.
- Honest decomposition: raw-callable wall geomean 1.400×; device-only v1 +4% / v2 −16%
  (NCU `profile/final_lb_k8_full/REPORT.md`); residual device gap latency-structural
  (see `docs/results.md` bound attribution).
- Frozen baseline (B200 GPU0, commit `3957e12df`): wall-synced 82.0 / 83.4 / 111.6 /
  112.2 µs; NCU baseline kernels 43.0 (v1) / 66.0 µs (v2), compute-bound on per-row tanh.
- Benchmark command: `python benchmark.py` (A/B; `--baseline-only` for the frozen rows)
  with `CUDA_VISIBLE_DEVICES=<idle GPU>`; per-shape median/mean/std/min/p10/p90 +
  geomean (dev + wall channels); full ledger in `benchmark.csv` / `solutions.jsonl`.
