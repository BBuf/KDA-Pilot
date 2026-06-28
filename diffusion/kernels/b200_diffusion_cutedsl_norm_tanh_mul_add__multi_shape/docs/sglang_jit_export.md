# SGLang jit_kernel Export & Drop-In Replacement Evidence

Date: 2026-06-04 — host `ion-b200` (ion-b200), container
`sglang_bbuf`, GPU 0 (`GPU-a4d97fda-2684-94c9-4291-c6b291c0eb33`), SGLang checkout
`/sgl-workspace/sglang @ edb1b3f8f` (patched for measurement, then restored clean —
the applied diff is preserved verbatim in `export/sglang_drop_in.patch`).

## SGLang files patched (the shipping integration)

1. **NEW** `python/sglang/jit_kernel/csrc/diffusion/norm_tanh_modulation.cuh`
   — byte-identical copy of `src/norm_tanh_cuda/norm_tanh_mul_add.cuh` (final
   launch-bounds K=8 build).
2. **NEW** `python/sglang/jit_kernel/diffusion/norm_tanh_modulation.py`
   — copy of `export/sglang_integration/norm_tanh_modulation.py`: `load_jit` +
   `make_cpp_args` + `cache_once` driver, eligibility gate `native_supported(...)`,
   per-entry-point routing switches.
3. **MODIFIED** `python/sglang/jit_kernel/diffusion/cutedsl/norm_tanh_mul_add_norm_scale.py`
   — four routing lines inserted at the top of each `torch.library.custom_op` body
   (before the original CuTe-DSL implementation, which remains the fallback).
   The `@torch.library.custom_op("sglang::fused_norm_tanh_mul_add[..._norm_scale]")`
   decorators and `register_fake` registrations are **untouched**.

## Public entry points preserved

- `sglang.jit_kernel.diffusion.cutedsl.norm_tanh_mul_add_norm_scale:fused_norm_tanh_mul_add`
- `sglang.jit_kernel.diffusion.cutedsl.norm_tanh_mul_add_norm_scale:fused_norm_tanh_mul_add_norm_scale`

Same names, same signatures, same custom-op registrations (torch.compile / CUDA-graph
compatibility preserved); only the internal implementation routes eligible calls to the
native kernel.

## load_jit template arguments / wrapper names

```python
args = make_cpp_args(D, rows_per_cta, is_rms, has_affine, second_norm, use_pdl, dtype)
load_jit("norm_tanh_modulation", *args,
         cuda_files=["diffusion/norm_tanh_modulation.cuh"],
         cuda_wrappers=[("run", f"FusedNormTanhModulationKernel<{args}>::run")])
# production instantiations: <3840, 8, true, true, {false|true}, false, bf16_t>
```

Compile flags: jit_kernel defaults only (`-DSGL_CUDA_ARCH=1000 -std=c++20 -O3
--expt-relaxed-constexpr`); no `--use_fast_math`. PDL compiled false (A/B-validated off).

## Gates and fallback behavior

`native_supported(...)`: CUDA tensors on one device; uniform dtype ∈ {bf16, fp16, fp32};
contiguous 3-D `x`; modulation tensors `[1|B,1|S,D]` with unit D-stride and 8-element-
aligned non-broadcast strides; weight-likes None or contiguous `[D]`; `D % 256 == 0 &&
D <= 8192`; 8-element-aligned base pointers; second entry point additionally requires
matching effective affine patterns. Everything else falls through to the original
CuTe-DSL body (verified by the mixed-dtype fallback probe). Env switches
`SGLANG_NATIVE_NORM_TANH_V{1,2}` allow disabling either route.

## In-SGLang validation (the promotion arbiter — dispatch-symmetric)

Driver: `export/sglang_integration/inSGLang_ab_driver.py` (public custom-op callables;
50 warmup + 200 wall-synced iters; JIT build excluded by warmup).

**Promoted arbiter (r4, round 1, contract-clean idle GPU 1)** — BOTH routes measured in
the SAME patched checkout, so the wrapper, custom-op registration, AND the inserted
`native_supported(...)` dispatch branch are byte-identical on both sides; only the
selected route differs (`SGLANG_NATIVE_NORM_TANH_V1=0 SGLANG_NATIVE_NORM_TANH_V2=0`
for the CuTe route vs defaults for the native route):

| Entry / shape | CuTe route | native route | speedup (r4) |
|---|---:|---:|---:|
| v1 S=4096 | 105.01 µs | 65.80 µs | 1.596× |
| v1 S=4128 | 106.14 µs | 65.46 µs | 1.621× |
| v2 S=4096 | 134.72 µs | 97.80 µs | 1.378× |
| v2 S=4128 | 135.14 µs | 97.04 µs | 1.393× |
| **geomean** | | | **1.493×** (v1 1.609×, v2 1.385×) |

Full stats (median/mean/std/min/p10/p90) in `export/arbiter_runs/*_r4.json` and
`benchmark.csv` mode `in-sglang-arbiter-dispatch-symmetric`. An identical r3 session on
GPU 0 (which carried a foreign 0%-util memory-resident app — superseded for that reason)
agrees within ~1% (geomean 1.507×); the CuTe-route medians also match the historical
clean-checkout runs (r1/r2) within noise, showing the added dispatch branch costs ≈ nil.

- Correctness (patched, strengthened): `IN_SGLANG_CORRECTNESS_PASS` — 4 captured zimage
  signatures vs the fp32 semantic reference through the public ops, AND the mixed-dtype
  fallback probe now (a) asserts `native_supported(...) is False` and (b) compares the
  public-op fallback output against the reference within production tolerances.

Decision per the pre-registered rule (Codex-reviewed): **ship the native path for both
entry points** — in the dispatch-symmetric arbiter v1 (1.609×) and v2 (1.385×) each
clear parity-or-better, so both routes default ON in
`export/sglang_integration/norm_tanh_modulation.py`. Honest decomposition stands:
device-only deltas are v1 +4% / v2 −16% (NCU, `profile/final_lb_k8_full/REPORT.md`); the
integrated win is dominated by the cheaper native host path, which is legitimate
shipped-path cost on both sides.

### Confirmation rerun (r2) — full stats + reproducibility proof

The drop-in was re-applied from scratch via `export/apply_drop_in.sh` (sha256 manifest:
`.cuh 56482c46…56ba0`, wrapper `cc947358…d48fc`); the produced checkout diff is
byte-identical to the recorded `export/sglang_drop_in.patch` (`PATCH_IDENTICAL_TO_RECORDED`),
correctness re-passed, and the benchmark was re-collected with full statistics (median /
mean / std / min / p10 / p90; raw summaries in `export/arbiter_runs/*.json`; rows appended
to `benchmark.csv` under mode `in-sglang-arbiter`):

| Entry / shape | clean median | patched median | speedup (r2) |
|---|---:|---:|---:|
| v1 S=4096 | 106.00 µs | 66.02 µs | 1.606× |
| v1 S=4128 | 108.94 µs | 65.95 µs | 1.652× |
| v2 S=4096 | 137.16 µs | 98.29 µs | 1.395× |
| v2 S=4128 | 136.95 µs | 97.79 µs | 1.400× |
| **geomean (r2)** | | | **1.509×** |

(r1 measured 1.487× — run-to-run agreement within ~1.5%. The clean v2 S=4096 mean/std in
r2 carry a single first-iteration outlier; medians/percentiles are robust.) The checkout
was restored clean after each run.

## Reproduction commands

```bash
# inside sglang_bbuf on ion-b200, CUDA_VISIBLE_DEVICES=0
python export/sglang_integration/inSGLang_ab_driver.py bench clean_baseline   # clean checkout
# apply export/sglang_drop_in.patch + the two new files
python export/sglang_integration/inSGLang_ab_driver.py correctness patched
python export/sglang_integration/inSGLang_ab_driver.py bench patched_native
```
