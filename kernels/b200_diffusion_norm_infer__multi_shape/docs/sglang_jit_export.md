# SGLang `jit_kernel` export — `b200_diffusion_norm_infer__multi_shape`

> **HISTORICAL — round-1 record.** Everything from here down to the
> "Round-2 export refresh" section describes the round-1 export (its routing
> table predates the large-S promotion, and its `SGLANG_DIFFNORM_CUDA*` env
> vars were round-1-only). The current shipped integration, routing, and
> validation evidence are in the **Round-2 export refresh** section below.

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

---

# Round-2 export refresh (2026-06-04) — tiled large-S RMS included

Round-2 changed the shipping device code (tiled multi-row RMS kernel added to
the `.cuh`) and the routing (large-S allowlisted to the tile kernel), so the
in-SGLang drop-in arbiter was re-run per the same isolation method (fresh
worktree `sglang-export-k05-r2` off the active `edb1b3f8f`, PYTHONPATH
shadowing verified via `sglang.__file__`; torn down after validation, shared
checkout untouched).

## Files placed/edited in the worktree (reproducible from `export/`)

| File | Change |
|---|---|
| `python/sglang/jit_kernel/csrc/diffusion/diffusion_norm_infer.cuh` | **new** — round-2 `.cuh` (adds `RmsNormTiledKernel<128,32,bf16>`; copied verbatim from `src/norm_cuda/diffusion_norm_infer.cuh`). |
| `python/sglang/jit_kernel/diffusion/cuda_norm_infer.py` | **new** — in-tree driver (copy of `export/cuda_norm_infer.py`): `@cache_once` `load_jit` builders, ported support predicates (incl. the 16-byte alignment gate for the tiled route), `maybe_*` entries, and the `SGLANG_DIFFUSION_NORM_CUDA=0` kill switch. |
| `python/sglang/jit_kernel/diffusion/triton/norm.py` | **edit** (`export/apply_worktree_edits.py`) — public `norm_infer` tries `maybe_norm_infer_cuda(...)` first (no custom op on this hot path; public contract byte-compatible). |
| `python/sglang/jit_kernel/diffusion/triton/rmsnorm_onepass.py` | **edit** — the CUDA path goes INSIDE the registered custom-op body `_triton_one_pass_rms_norm_cuda` (registration preserved for EVERY shape on BOTH sides of any A/B; stricter than the round-1 public-level insertion). |

Both public signatures preserved exactly. Wrapper/template names: header-only
`load_jit` markers `diffusion_norm_infer_{ln,rms,rms_tiled}` + `v3` +
`make_cpp_args(...)`; wrappers `("norm_infer_ln", "LayerNormInferKernel<...>::run")`,
`("rms_onepass", "RmsNormOnepassKernel<...>::run")`,
`("rms_tiled", "RmsNormTiledKernel<...>::run")`. No `--use_fast_math`.

## Validation results (GPU 1, idle before/after; host loaded on other GPUs)

- **Oracle**: `test_qwen_image_modulation.py` **288/288** under the worktree (re-passed on the v4 re-run).
- **Output parity** through the public ops (CUDA vs Triton device paths): 6/6.
- **SYMMETRIC shipping A/B** — both sides run the identical, unchanged public
  callable; only the device path differs (kill switch toggled per iteration;
  interleaved; median of 100 after 25 warmup). Symmetry is per entry point:
  - `triton_one_pass_rms_norm`: custom-op-BODY symmetric — the CUDA branch sits
    inside the registered `_triton_one_pass_rms_norm_cuda` body, so the
    `@register_custom_op` registration is exercised identically on both sides
    for every shape.
  - `norm_infer`: public-FUNCTION symmetric — the copied active baseline shows
    the wrapped public `norm_infer` carries NO custom-op registration on its
    hot path (the `diffusion_layer_norm_fwd_impl_cuda` registration belongs to
    the separate `_layer_norm_fwd` helper, which this entry point does not
    call); both sides therefore run the same plain public function, and there
    is no registration to preserve or bypass. (Empirical confirmation: the
    pinned-lane parity measured the LN host-layer delta at ~1.00×.)

| shape | wall | kernel-event |
|---|---|---|
| helios `[8640,5120]` fp32 LN | 1.2146× | 1.2479× |
| rms `[1320,128]` | 1.6726× | 1.6937× |
| rms `[4096,128]` | 1.6660× | 1.6880× |
| rms `[16384,128]` | 1.6612× | 1.6824× |
| rms `[648720,128]` | **1.0913×** | **1.1082×** |
| rms `[650040,128]` | **1.0881×** | **1.1061×** |
| **geomean** | **1.3722×** | **1.3946×** |

(Numbers above are the v4 arbiter re-run — the kernel's segmented reduction
gained half-warp shuffle masks after the initial round-2 run, so the arbiter
was re-executed with the fixed `.cuh`; the superseded first-run numbers
(geomean 1.3724×/1.3942×) are retained in `solutions.jsonl::cand-0012`.)

- **Fallback**: fp16 LN, D=256 RMS, rank-3 RMS all served through the public
  ops (Triton path) with the CUDA paths enabled.
- **Device-vs-host decomposition**: the host layer is IDENTICAL on both sides
  by construction (same registered op), so the deltas above are pure device.
  Cross-checks agree: the pinned-lane device-only A/B gave 1.10–1.16× on the
  huge shapes and the separately measured custom-op tax (1.05–1.06× there) is
  paid equally by both sides here — no host-layer effect is claimed as a kernel
  win.

Validation script: `export/run_export_validation.py` (PASS). Worktree removed
after validation (`git worktree remove --force`); shared checkout verified
clean.
