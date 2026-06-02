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
  `KDA_OPTIMIZED_triton_one_pass_rms_norm = True`; speedup `1.4223x`, arches `('h200',)`.
  - Source lineage (matches the generated metadata): `KDA_COMMIT_*` is the **export-source
    commit** — the kernel-pilot git HEAD when the export tool ran (the source tree the export was
    generated against). The exported `src/` in this package is committed in the kernel-pilot commit
    that introduces this package update (typically the immediate SUCCESSOR of the stamp), so the
    stamp marks the generation point, not a commit whose tree byte-matches the package — do not
    expect `git show <KDA_COMMIT_*>` to reproduce this exact package tree.
    `KDA_BENCHMARKED_COMMIT_* = b9dcb121ea4c9a1eaf153442548972f5da4704f1` is the **perf
    reproducibility anchor**: the candidate kernels (`rms_norm_d128.cuh`, `layer_norm_n5120.cuh`)
    are byte-identical from `149392da2` onward, so the `1.4223x` geomean reproduces from any commit
    since — only wrapper/validation/metadata changed across rounds, not the kernels. See
    `_impls/h200/KDA_EXPORTS.json` (`commit_role`, `benchmarked_commit`, `benchmarked_note`) and
    `_impls/h200/KDA_STATUS.md` for the machine-readable form.
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
- Correctness through the installed (swapped) symbols, **strictly gated** (Round 2): each
  output is checked for shape, dtype, no-NaN, no-Inf, and `torch.testing.assert_close` against
  BOTH the captured original baseline AND a PyTorch FP32 reference, at `atol=rtol=1e-5` for the
  fp32 LayerNorm shape and `5e-2` for bf16 RMS / the select01 oracle. The script
  `raise SystemExit(1)` on any failure (a `5e-5` fp32 LayerNorm regression would now fail, not
  print OK). Re-run result: all six perf shapes `OK`, select01 oracle `OK`, `VALIDATE_OK`, exit 0.
- Fallback (unsupported → baseline, exact `torch.equal`): fp16 RMS D=128 → baseline;
  `is_rms_norm=True` via `norm_infer` → baseline.
- Smoke benchmark through the installed path: rms 4096×128 base ~30us → installed ~15.6us (**1.92x**);
  rms 648720×128 base ~106.6us → installed ~103.4us (**1.03x**). Matches the workspace
  `benchmark.csv` (geomean 1.4223x).
- Result: `VALIDATE_OK` (exit 0).

## Notes
- `kda_kernels.install()` patches the module attributes; the dispatcher preloads the
  promoted impl and captures the original baselines first, so its fallback is non-recursive.
- This is the repo's drop-in mechanism; it does not edit the SGLang source tree
  (`python/sglang/jit_kernel/csrc/...`). The candidate `.cuh` is compiled in-place from
  `kda_kernels/.../_impls/h200/` via `load_jit`. Re-run / revert:
  `python3 scripts/export_kda_kernels/export.py --revert h200_diffusion_norm_infer__multi_shape`.
