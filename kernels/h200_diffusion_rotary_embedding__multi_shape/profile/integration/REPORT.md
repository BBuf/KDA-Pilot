# Integrated `kda_kernels` overlay validation — rotary_embedding / h200

Validates the **promoted production path** (`patches/sglang_kda_kernels.patch` →
`kda_kernels.install()` → generated `_dispatcher.py` → `_impls/h200/wrapper.py`), not the
thin `kernels/<task>/benchmark.py` wrapper path. This is the check that catches a
per-call dispatcher tax erasing small-shape wins (see the KDA install-path lesson).

## What it asserts
For both swap functions over the 6 deduplicated production shapes, via the **public
SGLang symbols after `install()`**:
- `kda_kernels.install()` reports both keys `swapped`; the SGLang module attributes are
  replaced by the `kda_kernels...rotary_embedding._dispatcher` callables.
- Each call routes to the `h200` impl (`_LAST_DISPATCH == "cuda"`).
- Output matches the captured SGLang baseline within `atol=rtol=1e-2`, NaN/Inf-free.
- Functional contract preserved: a **new** tensor of the input dtype/shape is returned
  (inputs not mutated).
- The swapped symbol is faster than the captured SGLang baseline.

## Environment / provenance
| Field | Value |
|---|---|
| Host | `ion-h200-8` (login `sglang-omni`), container `sglang_bbuf` |
| GPU | id **7**, NVIDIA H200, capability `(9, 0)` — idle (util 0%, 62/143771 MiB) |
| SGLang | source checkout `python/sglang` @ `c47f0e7cd` (carries `jit_kernel.diffusion`; ≡ pinned `6965fe0ee` by file sha1) |
| kernel-pilot | `4e4229fd7` (export-source commit; overlay committed in the successor commit) |
| Overlay under test | synced to `/home/sglang-omni/bbuf/repos/kernel-pilot/kda_kernels` |
| Build path | `load_jit(cuda_files=[<abs _impls/h200/csrc/rotary_embedding.cuh>])`; **no `--use_fast_math`**, no SGLang-checkout write |

### Commands
```bash
# integrated overlay validation
CUDA_VISIBLE_DEVICES=7 PYTHONPATH=/home/sglang-omni/bbuf/repos/kernel-pilot:/home/sglang-omni/bbuf/repos/sglang/python \
    python validate_overlay.py
# package verify
CUDA_VISIBLE_DEVICES=7 PYTHONPATH=<kp>:<sglang>/python python scripts/export_kda_kernels/verify.py
#   -> installed: 2 swaps  (rotary x2 swapped; all other families "skipped: not optimized")
```

## Result (idle H200, GPU 7)
| shape | api | route | new tensor | matches baseline | base µs | swap µs | speedup |
|---|---|---|---|---|---|---|---|
| `hunyuanvideo__std__B1_T27030_H24_D128__bf16` | standard | cuda | ✅ | ✅ (maxd 0.0000) | 155.94 | 103.15 | **1.512×** |
| `ltx2__B1_S1536_H32_half64__bf16` | ltx2 | cuda | ✅ | ✅ | 25.97 | 20.37 | 1.275× |
| `ltx2__B1_S126_H32_half32__bf16` | ltx2 | cuda | ✅ | ✅ | 24.90 | 17.89 | 1.392× |
| `ltx2__B1_S1536_H32_half32__bf16` | ltx2 | cuda | ✅ | ✅ | 25.12 | 18.50 | 1.358× |
| `ltx2__B1_S6144_H32_half64__bf16` | ltx2 | cuda | ✅ | ✅ | 56.13 | 50.40 | 1.114× |
| `ltx2__B1_S6144_H32_half32__bf16` | ltx2 | cuda | ✅ | ✅ | 38.67 | 32.03 | 1.207× |

**Integrated install() geomean = 1.3032× over 6 shapes. CORRECTNESS: PASS. OVERALL: PASS.**

## Reconciliation with the thin task benchmark
- Thin task benchmark (`benchmark.csv`, times `optimized_wrapper`): geomean **1.2955×**.
- Integrated install() overlay (this report, times the swapped public symbol): geomean **1.3032×**.

The two agree (the integrated path is, if anything, marginally faster), confirming the
generated dispatcher's resolved-target memoization (`_TARGET_CACHE` keyed by
`(fn_name, device_index)`) adds no measurable per-call tax — the production overlay
preserves the kernel win on every shape, including the tiny `S=126` bucket. `KDA_SPEEDUP`
is stamped at the thin-bench `1.295504×` (the `benchmark.csv` headline); the integrated
`1.3032×` is the production-path confirmation.
