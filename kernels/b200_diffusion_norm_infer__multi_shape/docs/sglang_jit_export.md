# SGLang `jit_kernel` export — `b200_diffusion_norm_infer__multi_shape`

How the promoted candidate kernels are wired into SGLang's public diffusion-norm
entry points through the `jit_kernel` / tvm-ffi stack, and the in-SGLang
validation evidence (AC-G).

The candidate `.cuh` and this document live in the kernel folder; the SGLang-side
edits live in a **disposable, isolated worktree** of the active checkout and are
documented here, not promoted into the shared dev checkout (Mandatory Constraint:
don't mutate shared checkouts in place).

## Isolation method

The active container's `sglang` is an **editable install** from
`/sgl-workspace/sglang/python` (a git repo). Its editable `.pth` appends a
finder *after* `PathFinder` in `sys.meta_path`, so a `PYTHONPATH` entry shadows
it (verified empirically). Therefore:

```bash
# isolated worktree off the active commit (edb1b3f), shared checkout untouched
git -C /sgl-workspace/sglang worktree add --detach \
    /home/sglang-omni/bbuf/worktrees/sglang-export-k05 HEAD
# all validation runs with the worktree shadowing the install:
PYTHONPATH=/home/sglang-omni/bbuf/worktrees/sglang-export-k05/python python ...
# teardown when done:
git -C /sgl-workspace/sglang worktree remove --force \
    /home/sglang-omni/bbuf/worktrees/sglang-export-k05
```

Every validation below printed `sglang.__file__` inside the worktree, confirming
the edited copy (not the shared install) was exercised.

## SGLang files touched (in the worktree)

| File | Change |
|---|---|
| `python/sglang/jit_kernel/csrc/diffusion/diffusion_norm_infer.cuh` | **new** — the candidate kernels (copied from this folder's `src/norm_cuda/diffusion_norm_infer.cuh`, git blob `9a63efa1`, 10256 B). |
| `python/sglang/jit_kernel/diffusion/cuda_norm_infer.py` | **new** — CUDA driver: `load_jit` builders + support predicates + `maybe_*` entry points (ported from this folder's `src/register.py`). |
| `python/sglang/jit_kernel/diffusion/triton/norm.py` | **edit** — public `norm_infer` tries `maybe_norm_infer_cuda(...)` first, else falls through to the existing Triton body. |
| `python/sglang/jit_kernel/diffusion/triton/rmsnorm_onepass.py` | **edit** — public `triton_one_pass_rms_norm` tries `maybe_rms_onepass_cuda(...)` first, else the existing Triton one-pass baseline. |

Both public signatures are preserved exactly:
`norm_infer(x, weight, bias, eps, is_rms_norm=False, out=None)` and
`triton_one_pass_rms_norm(x, w, eps=1e-6)`.

## Wrapper / template names (header-only `load_jit`)

Mirrors `diffusion/qknorm_rope.py`: `@cache_once` module builders, relative
`cuda_files`, header-only `TVM_FFI_DLL_EXPORT_TYPED_FUNC` wrappers.

```python
# LayerNorm (fp32)
load_jit("b200_diffnorm_ln", "k05cand_v2", *make_cpp_args(dtype),
         cuda_files=["diffusion/diffusion_norm_infer.cuh"],
         cuda_wrappers=[("norm_infer_ln", f"LayerNormInferKernel<{args}>::run")])
# RMSNorm (bf16, D=128)
load_jit("b200_diffnorm_rms", "k05cand_v2", *make_cpp_args(dim, k_unroll, dtype),
         cuda_files=["diffusion/diffusion_norm_infer.cuh"],
         cuda_wrappers=[("rms_onepass", f"RmsNormOnepassKernel<{args}>::run")])
```

Generated JIT shims (`cuda.cu`) for the two production families:

```cpp
#include ".../sglang-export-k05/python/sglang/jit_kernel/csrc/diffusion/diffusion_norm_infer.cuh"
TVM_FFI_DLL_EXPORT_TYPED_FUNC(norm_infer_ln, (LayerNormInferKernel<fp32_t>::run));
TVM_FFI_DLL_EXPORT_TYPED_FUNC(rms_onepass,   (RmsNormOnepassKernel<128, 1, bf16_t>::run));
```

## Cache key / stale-JIT guard

`load_jit`'s `module_name = "sgl_kernel_jit_" + "_".join(markers)` — keyed by the
marker args, **not** the `.cuh` content. The marker `"k05cand_v2"` is (a) distinct
from every other `jit_kernel` module (no build-dir collision; built dirs are
`sgl_kernel_jit_b200_diffnorm_{ln,rms}_k05cand_v2_...`) and (b) the stale-JIT
guard: **bump it on any `.cuh` edit** to force a fresh build dir.

## Compile flags — NO `--use_fast_math`

Captured from the export's actual `build.ninja` (`/root/.cache/tvm-ffi/sgl_kernel_jit_b200_diffnorm_*_k05cand_v2_*`):

```
cuda_cflags = -Xcompiler -fPIC -std=c++17 -O2 -gencode=arch=compute_100,code=sm_100 \
              -DSGL_CUDA_ARCH=1000 -std=c++20 -O3 --expt-relaxed-constexpr -I<tvm_ffi> \
              -I<worktree>/python/sglang/jit_kernel/include
```

`grep -ciE "use_fast_math|ffast-math|--fmad|-ftz"` over both build dirs returns
**0**. These are SGLang's `jit_kernel` defaults (`-std=c++20 -O3
--expt-relaxed-constexpr` + arch); the driver passes no `extra_cuda_cflags`. The
include path is the worktree's, confirming the build used the worktree `.cuh`.

## Routing gates + fallback

`cuda_norm_infer.py` routes to CUDA ONLY for an explicit allowlist of captured
production + regression shapes, with full input validation; otherwise the
`maybe_*` functions return `None` and the public entry point runs its Triton
baseline. Identical predicates to `src/register.py`:
- **LN → CUDA** iff fp32, 2-D, contiguous, `is_rms_norm=False`, `(M,N) ∈ _SUPPORTED_LN`, weight+bias contiguous `(N,)` same device/dtype, `out` None-or-matching, AND `x`/`weight`/`bias`/`out` `data_ptr()` 16-byte aligned (`float4` loads).
- **RMS → CUDA** iff bf16, exactly 2-D, contiguous, `(S,D) ∈ _SUPPORTED_RMS` (D=128), `w` contiguous `(D,)` same device/dtype, AND `x`/`w` `data_ptr()` 8-byte aligned (`AlignedVector<bf16,4>` loads).
- **Alignment gate** (mirrors `src/register.py`): a tensor can be `is_contiguous()` yet be a view with a non-zero storage offset whose base is not vector-aligned; such views fall back to the Triton baseline (verified in `val_export.py`: misaligned LN/RMS views → baseline).
- The two large-S RMS production shapes (648720, 650040) are deliberately **not**
  allowlisted → they fall back (documented no-go, parity).

Env switches: `SGLANG_DIFFNORM_CUDA=0` disables the CUDA path entirely;
`SGLANG_DIFFNORM_CUDA_STRICT=1` makes a *supported* shape raise on a build/run
failure instead of silently falling back (so a broken build can't masquerade as a
pass). Unsupported shapes always fall back regardless of strict.

## In-SGLang validation (idle B200, worktree `edb1b3f`, via the public entry points)

1. **Correctness oracle** — `jit_kernel/tests/diffusion/test_qwen_image_modulation.py`
   (calls the public `norm_infer`), full range (fp16/bf16/fp32 × batch{1,2,4} ×
   seq{6,33,128,257} × hidden{512,1024,1536,3072}), `SGLANG_DIFFNORM_CUDA_STRICT=1`:
   **288 passed in 22.07s**. The fp32 allowlisted shapes ran the substituted CUDA
   LayerNorm (strict) and matched the fused-modulation reference to 1e-5; fp16/bf16
   and non-allowlisted fp32 shapes fell back to Triton and passed.

2. **Unsupported-signature fallback** — fp16 LayerNorm `(128,512)` and bf16 RMS
   `(999,128)`: `maybe_*` return `None`, the public entry points return the
   Triton-baseline result, and no exception is raised even under strict mode.

3. **Production smoke benchmark** — public entry points, CUDA on vs off,
   interleaved (60 iters, median ratio):

   | shape | baseline µs | cand µs | speedup (median / best) | matches dispatch |
   |---|---|---|---|---|
   | helios LN `[8640,5120]` fp32 | 82.30 | 70.89 | 1.16× / 1.19× | ✓ (~1.17×) |
   | RMS `[1320,128]` bf16 | 31.21 | 20.02 | 1.56× / 3.64× | ✓ (~1.64×) |
   | RMS `[4096,128]` bf16 | 31.22 | 20.75 | 1.51× / 1.71× | ✓ (~1.63×) |
   | RMS `[16384,128]` bf16 | 31.39 | 22.35 | 1.41× / 3.51× | ✓ (~1.53×) |
   | RMS `[648720,128]` bf16 | 76.03 | 76.88 | 0.99× | ✓ (no-go fallback, parity) |
   | RMS `[650040,128]` bf16 | 76.17 | 77.49 | 0.99× | ✓ (no-go fallback, parity) |

   Smoke geomean 1.25× wall — the pattern matches the dispatch table (LN ~1.16×,
   small/mid RMS ~1.4–1.56×, large-RMS parity). Medians run slightly below the
   canonical figures in `benchmark.csv` / `docs/dispatch.md` because this is a
   lighter interleaved smoke harness on a shared GPU; the authoritative
   promotion numbers remain those in `benchmark.csv` (geomean 1.29× wall).

## Notes

- Env drift: the active container is now `sglang edb1b3f` (the earlier rounds
  recorded `0b65588c`; the shared box re-provisioned the container during round 5).
  The export was built and validated against `edb1b3f`.
- The worktree (`/home/sglang-omni/bbuf/worktrees/sglang-export-k05`) is
  disposable; remove with `git worktree remove --force` (command above). The
  authoritative candidate sources stay in this kernel folder.
