# In-SGLang export + drop-in replacement (AC-8)

The native CUDA candidate is exported **inside SGLang** through `jit_kernel`/tvm-ffi
(`load_jit` + `make_cpp_args` + `cache_once`; **no `--use_fast_math`**), and the two
public diffusion RoPE symbols are replaced with the candidate to prove a real drop-in:

- `sglang.jit_kernel.diffusion.triton.rotary:apply_rotary_embedding`
- `sglang.jit_kernel.diffusion.triton.ltx2_rotary:apply_ltx2_split_rotary_emb`

## How the export works

1. `_build_jit_module()` calls SGLang `load_jit("kda_rotary_embedding", <make_cpp_args(dtype)>, <source-hash>,
   cuda_files=[<absolute path to src/csrc/rotary_embedding.cuh>],
   cuda_wrappers=[("standard_rope","StandardRopeKernel<bf16_t>::run"),("ltx2_split_rope","Ltx2SplitRopeKernel<bf16_t>::run")])`.
   `load_jit` joins `cuda_files` under `<sglang>/jit_kernel/csrc`, but pathlib keeps an absolute
   path as-is, so the workspace `.cuh` compiles in place and **nothing is written into the SGLang
   checkout** (the `sgl_kernel` headers it `#include`s still resolve through `load_jit`'s default
   include dirs). The promoted `kda_kernels` overlay builds the same way from its own `_impls/<arch>/csrc/`.
2. The loader is wrapped in SGLang `cache_once`, keyed by `(dtype, source_hash, profile)`,
   so an edited `.cuh` (new hash) rebuilds and the hot path does no per-call file I/O.
   Compile flags match the SGLang jit build (`-DSGL_CUDA_ARCH=900 -std=c++20 -O3 --expt-relaxed-constexpr`); profiling adds only `-lineinfo`.
3. `tests/sglang_export_test.py` captures the original baselines, asserts the captured
   symbols *are* the public SGLang symbols, then sets the public attributes to the
   candidate and exercises correctness / fallback / a smoke benchmark via the public
   names, restoring the originals in a `finally` block.

## Provenance (this export run)

| Field | Value |
|---|---|
| Host | `ion-h200-8` (login `sglang-omni`), container `sglang_bbuf` |
| GPU | id **7**, NVIDIA H200 |
| GPU idle before | util 0%, mem 62 / 143771 MiB |
| GPU idle after | util 0% (single-device run pinned via `CUDA_VISIBLE_DEVICES=7`) |
| SGLang commit | `c47f0e7cdde48ddc718e3c6ee8bc87bebee2e8ff` |
| Oracle equivalence | `rotary.py` sha1 `81fb5ffeaf387903c45da1b62accce5b1e275039`, `ltx2_rotary.py` sha1 `3408d9084b4cc9e92cbd3dbd584fa7ec5f8d5d4b` — byte-identical to pinned `6965fe0ee` |
| Date | 2026-06-02 |

### Commands

```bash
# correctness gate after switching to cache_once (sanity that the loader still builds & is correct)
CUDA_VISIBLE_DEVICES=7 PYTHONPATH=<sglang>/python KDA_RUN_CORRECTNESS=1 \
  KDA_SGLANG_ORACLE_COMMIT=c47f0e7cd python -m pytest tests/test_correctness.py -q
#   -> 6 passed

# in-SGLang export + drop-in replacement test
CUDA_VISIBLE_DEVICES=7 PYTHONPATH=<sglang>/python python tests/sglang_export_test.py
#   -> EXPORT_TEST: PASS
```

## Results

**Correctness via the public SGLang symbols (all 6 production shapes):** candidate ==
original baseline within `atol=rtol=1e-2`, and every supported shape takes the `"cuda"`
route. ✅

| case | route | candidate == baseline |
|---|---|---|
| `hunyuanvideo__std__B1_T27030_H24_D128__bf16` | cuda | ✅ |
| `ltx2__B1_S1536_H32_half64__bf16` | cuda | ✅ |
| `ltx2__B1_S126_H32_half32__bf16` | cuda | ✅ |
| `ltx2__B1_S1536_H32_half32__bf16` | cuda | ✅ |
| `ltx2__B1_S6144_H32_half64__bf16` | cuda | ✅ |
| `ltx2__B1_S6144_H32_half32__bf16` | cuda | ✅ |

**Fallback via the public symbol:** an fp16 standard call resolves to the `baseline`
route (not CUDA) and returns the input dtype. ✅

**Smoke benchmark (in-SGLang, candidate via the public symbol vs the original baseline,
median µs, warmup 20 / iters 50):**

| case | baseline µs | candidate µs | speedup |
|---|---|---|---|
| `hunyuanvideo__std__B1_T27030_H24_D128__bf16` | 157.42 | 105.96 | 1.486× |
| `ltx2__B1_S1536_H32_half64__bf16` | 26.75 | 21.81 | 1.227× |
| `ltx2__B1_S126_H32_half32__bf16` | 22.96 | 16.34 | 1.405× |
| `ltx2__B1_S1536_H32_half32__bf16` | 23.87 | 18.52 | 1.289× |
| `ltx2__B1_S6144_H32_half64__bf16` | 58.67 | 53.07 | 1.106× |
| `ltx2__B1_S6144_H32_half32__bf16` | 40.64 | 33.94 | 1.198× |
| **geomean** | | | **1.279×** |

The smoke-benchmark geomean (1.279×) is slightly below the dedicated `benchmark.py`
geomean (1.296×) because the smoke harness uses fewer iterations (50 vs 100); both agree
the candidate is faster on all 6 shapes. The dedicated `benchmark.csv` remains the
headline source.

## Reversibility / non-invasiveness

The build writes **nothing** into the SGLang checkout: the `.cuh` compiles in place from its
absolute workspace path (only the JIT build cache is populated). The public-symbol replacement
in the test is restored in a `finally` block. The user approved the `load_jit` build + the final
in-SGLang test.

## Re-verification (marker scrub + absolute-path build)

Two later changes were re-validated on GPU 7, both producing a byte-identical compiled kernel:
(1) a comment-only marker scrub changed the `.cuh` hash `42f21a8882a6` → `e6588f9edfe7`;
(2) `wrapper.py` switched from copying the `.cuh` into the SGLang checkout to compiling it from
its absolute path (`cuda_files=[<abs .cuh>]`). After clearing the JIT cache and **removing** the
previously-placed checkout `.cuh`, the fresh absolute-path build passed: correctness gate `6 passed`,
in-SGLang `EXPORT_TEST: PASS` (6/6 CUDA route, fp16 fallback, smoke geomean ≈1.27×), and the SGLang
checkout was confirmed **not** re-created (no checkout write). This is the build path the promoted
`kda_kernels` overlay uses.
