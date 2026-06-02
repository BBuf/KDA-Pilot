# SGLang jit_kernel export + drop-in replacement (kda_kernels overlay)

Final packaging step, run after the RLCR optimization landed. The repo's integration
mechanism is the **`kda_kernels` overlay + runtime `install()`**, which monkey-patches the
two public SGLang symbols with the native-CUDA candidate. The CUDA `.cuh` is compiled
through SGLang's own `jit_kernel` / tvm-ffi `load_jit` (no `torch.utils.cpp_extension`,
no `--use_fast_math`).

## Export command (from repo root)

```
python3 scripts/export_kda_kernels/export.py h200_diffusion_group_norm_silu__multi_shape
```

Prerequisite: `src/register.py` defines
`EXPORTS = {"triton_group_norm_silu": ..., "apply_group_norm_silu": ...}` (read by the export
tool) and `src/wrapper.py` re-exports those names (the generated dispatcher imports
`kda_kernels.diffusion.group_norm_silu._impls.h200.wrapper`). The implementation lives in
`src/group_norm_dispatch.py`, which captures the SGLang baselines at import so the
post-`install()` fallback is non-recursive.

## Generated files

- `kda_kernels/diffusion/group_norm_silu/__init__.py` — rewritten to import `triton_group_norm_silu`
  and `apply_group_norm_silu` from `._dispatcher`; `KDA_OPTIMIZED_* = True`; speedup `1.4487x`,
  arches `('h200',)`.
  - Source lineage: `KDA_COMMIT_*` is the **export-source commit** (kernel-pilot HEAD when the export
    tool ran); the exported `src/` is committed in the SUCCESSOR commit, so the stamp marks the
    generation point, not a commit whose tree byte-matches the package.
    `KDA_BENCHMARKED_COMMIT_* = 4b2a6c258e9115e019daaf33add3024ef5479867` is the **perf
    reproducibility anchor**: `group_norm_silu.cuh` is byte-identical from `53a6fd2de` onward, and the
    canonical `benchmark.csv` (geomean 1.4487x, `version=v5-dispatch-final`, ion8-h200 GPU7) was
    produced at that commit; only the wrapper/validation/metadata changed afterward. See
    `_impls/h200/KDA_EXPORTS.json` (`commit_role`, `benchmarked_commit`, `benchmarked_note`) and
    `_impls/h200/KDA_STATUS.md` for the machine-readable form.
- `kda_kernels/diffusion/group_norm_silu/_dispatcher.py` — auto-generated arch dispatcher with a
  per-(fn, device) target cache (steady-state calls skip capability probe + import + attribute
  lookup) and non-recursive SGLang baseline fallback.
- `kda_kernels/diffusion/group_norm_silu/_impls/h200/` — `wrapper.py`, `group_norm_dispatch.py`,
  `register.py`, `group_norm_silu.cuh`, `KDA_EXPORTS.json`, `KDA_STATUS.md`.

## Template args / wrapper names passed to load_jit

- `_module`: `load_jit("group_norm_silu_kda", *make_cpp_args(dtype, False),
  cuda_files=[<abs>/group_norm_silu.cuh],
  cuda_wrappers=[("group_norm_silu", "GroupNormSiluKernel<...>::run"),
  ("group_norm_silu_large", "GroupNormSiluKernel<...>::run_large")])`.
- No `--use_fast_math`; default SGLang jit target flags.

## Shape / dtype gates + dispatch + fallback

- `triton_group_norm_silu(x, weight, bias, num_groups, eps)` → native candidate when CUDA, no grad,
  fp16/bf16, contiguous, 16B-aligned, `num_groups == 32`, weight/bias `[C]`; else SGLang baseline.
- `apply_group_norm_silu(x, norm, activation)` → same gate via `norm`/`activation`; else SGLang baseline.
- Bucket dispatch on `group_size = (C/num_groups) * spatial`: `< 65536` single-CTA "small",
  `[65536, 900000)` 3-stage "large", `>= 900000` bandwidth-bound → SGLang Triton baseline ("giant").
- Dispatcher arch gate: capability `(9,0)` → `h200`; other arches / None → baseline.

## Install + drop-in validation (remote ion8-h200, container `sglang_omni_bbuf_kda`, GPU 7 = NVIDIA H200, idle)

```
PYTHONPATH=<repo>:/home/sglang-omni/bbuf/repos/sglang/python CUDA_VISIBLE_DEVICES=7 \
  python kernels/h200_diffusion_group_norm_silu__multi_shape/validate_install.py
```

- `kda_kernels.install(strict=True)` → 5 swaps; both group_norm_silu entries **swapped**:
  - `sglang.jit_kernel.diffusion.triton.group_norm_silu:triton_group_norm_silu` → kda dispatcher
  - `sglang.jit_kernel.diffusion.group_norm_silu:apply_group_norm_silu` → kda dispatcher
- Correctness through the installed (swapped) symbols, run under `no_grad`: the native candidate runs
  for the supported production buckets (dispatch `path in {small, large}`), matches the eager
  `F.silu(F.group_norm(...))` oracle (fp16 atol/rtol 3e-3, bf16 7e-2/2e-2), no NaN/Inf.
- Fallback (unsupported → baseline, exact `torch.equal`): giant `num_groups=32` → `baseline_giant`;
  `num_groups=16` → `baseline_unsupported`. Both bit-identical to the original SGLang baseline.
- Apply form (the Hunyuan VAE callsite) on `[1,512,5,32,32]` fp16 → candidate, matches eager.
- Smoke benchmark through the installed path: `[1,512,5,32,32]` **1.57x**, `[1,512,3,128,40]` **2.56x**,
  `[1,256,9,128,40]` **1.45x** vs the captured baseline — the memoized dispatcher's per-call overhead
  does not erase the win. `VALIDATE_OK` (exit 0). `scripts/export_kda_kernels/verify.py` → `installed: 5 swaps`.
- Workspace strict correctness (thin path, `KDA_RUN_CORRECTNESS=1 KDA_STRICT_CANDIDATE=1`): `4 passed`
  (110 production + regression cases + fallback matrix + candidate-path assertion).

## Notes
- `kda_kernels.install()` patches the module attributes; the dispatcher preloads the promoted impl and
  the impl captures the original baselines first, so its fallback is non-recursive.
- This is the repo's drop-in mechanism; it does not edit the SGLang source tree. The candidate `.cuh`
  is compiled in-place from `kda_kernels/.../_impls/h200/` via `load_jit`. Revert:
  `python3 scripts/export_kda_kernels/export.py --revert h200_diffusion_group_norm_silu__multi_shape`.
