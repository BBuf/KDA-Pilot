# SGLang jit_kernel export + drop-in replacement (kda_kernels overlay)

Final packaging step (task12), run after the RLCR optimization landed. The repo's
integration mechanism is the **`kda_kernels` overlay + runtime `install()`**, which
monkey-patches the two public SGLang symbols with the native-CUDA candidate. The
CUDA `.cuh` are compiled through SGLang's own `jit_kernel` / tvm-ffi `load_jit`
(no `torch.utils.cpp_extension`, no `--use_fast_math`).

## Export command (from repo root)

```
python3 scripts/export_kda_kernels/export.py h200_diffusion_norm_infer__multi_shape
```

Prerequisite: `src/register.py` defines
`EXPORTS = {"norm_infer": norm_infer, "triton_one_pass_rms_norm": triton_one_pass_rms_norm}`
(read by the export tool) and `src/wrapper.py` re-exports those names (the generated
dispatcher imports `kda_kernels.diffusion.norm_infer._impls.h200.wrapper`).

## Generated files

- `kda_kernels/diffusion/norm_infer/__init__.py` — rewritten to import `norm_infer` and
  `triton_one_pass_rms_norm` from `._dispatcher`; `KDA_OPTIMIZED_norm_infer = True`,
  `KDA_OPTIMIZED_triton_one_pass_rms_norm = True`; stamped commit `149392da…`, date
  2026-06-02, speedup `1.4223x`, arches `('h200',)`.
- `kda_kernels/diffusion/norm_infer/_dispatcher.py` — auto-generated arch dispatcher with a
  per-(fn, device) target cache (steady-state calls skip capability probe + import +
  attribute lookup) and non-recursive SGLang baseline fallback.
- `kda_kernels/diffusion/norm_infer/_impls/h200/` — `wrapper.py`, `norm_dispatch.py`,
  `register.py`, `rms_norm_d128.cuh`, `layer_norm_n5120.cuh`, `KDA_EXPORTS.json`, `KDA_STATUS.md`.

## Template args / wrapper names passed to load_jit

- `_rms_module`: `load_jit("kda_rms_norm", *make_cpp_args(128, False, bf16_t),
  cuda_files=[<abs>/rms_norm_d128.cuh], cuda_wrappers=[("rms_norm","RmsNormKernel<128, false, bf16_t>::run")])`.
- `_ln_module`: `load_jit("kda_layer_norm", *make_cpp_args(5120, True, False, fp32_t),
  cuda_files=[<abs>/layer_norm_n5120.cuh], cuda_wrappers=[("layer_norm","LayerNormKernel<5120, true, false, fp32_t>::run")])`.
- No `--use_fast_math`; default SGLang jit target flags.

## Arch / shape / dtype gates + fallback

- `triton_one_pass_rms_norm` → CUDA bf16, `x.is_contiguous()`, D==128, w [128] bf16 → `rms_norm_warp`; else SGLang baseline.
- `norm_infer` → CUDA fp32, `is_rms_norm=False`, `out is None`, `x.is_contiguous()`, N==5120, weight & bias [N] fp32 → `layer_norm_block`; else SGLang baseline.
- Dispatcher arch gate: capability (9,0) → `h200`; other arches/None → baseline.

## Install + drop-in validation (remote ion8-h200 GPU7, NVIDIA H200, idle)

Command:
```
cd <repo> && CUDA_VISIBLE_DEVICES=7 PYTHONPATH=. python validate_install.py
```

- `kda_kernels.install(strict=True)` → both entries **swapped**:
  - `sglang.jit_kernel.diffusion.triton.norm:norm_infer` → `kda_kernels.diffusion.norm_infer._dispatcher`
  - `sglang.jit_kernel.diffusion.triton.rmsnorm_onepass:triton_one_pass_rms_norm` → same dispatcher
- Correctness through the installed (swapped) symbols vs the captured original baseline + a PyTorch FP32 reference:
  - helios LN [8640,5120] f32: vs_base 2.86e-6 (within 1e-5).
  - RMS bf16 {648720,1320,650040,16384,4096}×128: vs_base ≤ 1.56e-2, vs_ref ≤ 3.12e-2 (within 5e-2); no NaN/Inf.
- Fallback (unsupported → baseline, exact match): fp16 RMS D=128 → baseline; `is_rms_norm=True` via `norm_infer` → baseline.
- select01 modulation oracle through the installed `norm_infer`: matches baseline (the [*,3072] oracle shape falls back; output identical).
- Smoke benchmark through the installed path: rms 4096×128 base 30.33us → installed 15.58us (**1.95x**); rms 648720×128 base 106.94us → installed 103.36us (**1.03x**). Matches the workspace `benchmark.csv` (geomean 1.4223x).
- Result: `VALIDATE_OK`.

## Notes
- `kda_kernels.install()` patches the module attributes; the dispatcher preloads the
  promoted impl and captures the original baselines first, so its fallback is non-recursive.
- This is the repo's drop-in mechanism; it does not edit the SGLang source tree
  (`python/sglang/jit_kernel/csrc/...`). The candidate `.cuh` is compiled in-place from
  `kda_kernels/.../_impls/h200/` via `load_jit`. Re-run / revert:
  `python3 scripts/export_kda_kernels/export.py --revert h200_diffusion_norm_infer__multi_shape`.
