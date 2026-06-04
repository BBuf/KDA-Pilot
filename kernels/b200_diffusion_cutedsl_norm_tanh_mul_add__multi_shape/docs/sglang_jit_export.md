# SGLang jit_kernel Export & Drop-In Replacement Evidence

Date: 2026-06-04 — host `innomatrix-us-adc-smb200-0003` (ion-b200), container
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

## In-SGLang validation (the promotion arbiter)

Driver: `export/sglang_integration/inSGLang_ab_driver.py` (public custom-op callables;
50 warmup + 200 wall-synced iters; idle GPU 0; JIT build excluded by warmup).

- Correctness (patched): `IN_SGLANG_CORRECTNESS_PASS` — 4 captured zimage signatures vs
  the fp32 semantic reference through the public ops + fallback probe (NaN-free).
- Benchmark, public-op wall medians (clean checkout vs patched checkout — identical
  wrapper/dispatch/registration layers, only the kernel inside differs):

| Entry / shape | clean (CuTe) | patched (native) | speedup |
|---|---:|---:|---:|
| v1 S=4096 | 104.84 µs | 65.72 µs | 1.595× |
| v1 S=4128 | 106.22 µs | 66.24 µs | 1.604× |
| v2 S=4096 | 134.42 µs | 98.01 µs | 1.372× |
| v2 S=4128 | 136.51 µs | 97.89 µs | 1.394× |
| **geomean** | | | **1.487×** |

Decision per the pre-registered rule (Codex-reviewed): **ship the native path for both
entry points** — v2 is parity-or-better integrated (1.37-1.39×), so the conditional ship
criterion is satisfied. Honest decomposition stands: device-only deltas are v1 +4% /
v2 −16% (NCU, `profile/final_lb_k8_full/REPORT.md`); the integrated win is dominated by
the cheaper native host path, which is legitimate shipped-path cost on both sides.

## Reproduction commands

```bash
# inside sglang_bbuf on ion-b200, CUDA_VISIBLE_DEVICES=0
python export/sglang_integration/inSGLang_ab_driver.py bench clean_baseline   # clean checkout
# apply export/sglang_drop_in.patch + the two new files
python export/sglang_integration/inSGLang_ab_driver.py correctness patched
python export/sglang_integration/inSGLang_ab_driver.py bench patched_native
```
