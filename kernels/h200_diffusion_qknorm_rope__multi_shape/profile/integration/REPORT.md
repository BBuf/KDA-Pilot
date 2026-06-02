# Integrated `kda_kernels` overlay validation — qknorm_rope / H200

Validates the **promoted production path** (what `patches/sglang_kda_kernels.patch` + `PYTHONPATH`
activate), not the thin task-level harness:

```
capture SGLang baseline → kda_kernels.install() → assert the public symbol
  sglang.jit_kernel.diffusion.qknorm_rope:fused_inplace_qknorm_rope was swapped to the generated
  kda dispatcher → call the swapped symbol on the 9 captured shapes → confirm it routes to the h200
  impl (get_last_dispatch()=="cuda"), matches the split oracle, returns None (in place), no NaN →
  benchmark swapped vs baseline → confirm fp16 falls back cleanly.
```

This is the path the [auto-memory lesson](../../../../) flags as the one that matters: a thin
task benchmark ≠ production, because the per-op dispatcher adds per-call cost. The generated
dispatcher here is the zero-overhead design (memoized resolved-target cache, capability probed once),
so the old ~5 µs/call tax (which once dragged the integrated path to 0.898×) is gone.

## Reproduce

```bash
# inside container sglang_omni_bbuf_kda, idle GPU 7
PYTHONPATH=<kernel-pilot-root>:/home/sglang-omni/bbuf/repos/sglang/python \
  CUDA_VISIBLE_DEVICES=7 python3 validate_overlay.py
```

`<kernel-pilot-root>` must contain the `kda_kernels/` overlay under test.

## Environment

| Field | Value |
|---|---|
| Host / container | `ion-h200-8` / `sglang_omni_bbuf_kda` |
| GPU | NVIDIA H200, capability (9, 0), **GPU 7 idle** (util 0%, mem 70 MiB before; 5% tail after) |
| SGLang | `/home/sglang-omni/bbuf/repos/sglang` @ `c47f0e7cd` (0.5.12.dev472) |
| Candidate src | `qknorm_rope_kernel.cuh` sha16 `4f70cda745940c96` (RLCR `d3-final-corrected`, commit `673217af6`) |
| Build | SGLang `load_jit` / `make_cpp_args` / `cache_once`; flags match the diffusion baseline (no `--use_fast_math`) |
| Timing | CUDA events, median of 200 iters, 30 warmup, inputs restored outside the timed region |

## Install() swap

```
install result: ('sglang.jit_kernel.diffusion.qknorm_rope:fused_inplace_qknorm_rope',
                 'kda_kernels.diffusion.qknorm_rope:fused_inplace_qknorm_rope', 'swapped')
swapped.__module__ = kda_kernels.diffusion.qknorm_rope._dispatcher
```

## Correctness — PASS (all 9 captured shapes)

Every shape: `get_last_dispatch()=="cuda"`, returns `None` (in place), no NaN/Inf, and matches the
split oracle (`sglang.jit_kernel.norm.fused_inplace_qknorm` + `flashinfer ... apply_rope_with_cos_sin_cache_inplace`)
at **max abs diff 0.0625 = 1 bf16 ulp**, well within ATOL 8e-2 / RTOL 1e-2.

Fallback contract through the dispatcher: an **fp16 CUDA** call routes to the kda wrapper, takes the
semantic fallback (`get_last_dispatch()=="fallback"`), returns `None`, no NaN — never raises.
(CPU / other-arch inputs route to the SGLang baseline by design, identical to stock behavior.)

## Benchmark — integrated install() path vs SGLang baseline

Per-shape (run 2; base_us / swap_us = median µs):

| shape | tokens | heads | base µs | swap µs | speedup |
|---|---|---|---|---|---|
| qwen__T4096_H24 | 4096 | 24 | 45.25 | 42.85 | 1.056× |
| qwen__T19_H24 | 19 | 24 | 15.81 | 15.97 | 0.990× |
| qwen__T47_H24 | 47 | 24 | 15.73 | 16.03 | 0.981× |
| qwen_edit__T8424_H24 | 8424 | 24 | 83.20 | 77.82 | 1.069× |
| qwen_edit__T195_H24 | 195 | 24 | 16.26 | 16.64 | 0.977× |
| qwen_edit__T189_H24 | 189 | 24 | 16.29 | 16.64 | 0.979× |
| zimage__T4096_H30 | 4096 | 30 | 53.89 | 50.67 | 1.063× |
| zimage__T32_H30 | 32 | 30 | 16.00 | 16.13 | 0.992× |
| zimage__T4128_H30 | 4128 | 30 | 53.98 | 50.80 | 1.063× |

**All-9 geomean: 1.012× (run 1) / 1.018× (run 2).**
**Large shapes (tokens ≥ 4096) geomean: 1.055× / 1.063×.**
Small shapes (tokens ≤ 195): parity (0.97–0.99×).

## Interpretation

- **Large, memory-latency-bound shapes win (~1.06×)** — the 2-heads-per-warp float4 kernel's real
  advantage, and these are the shapes that dominate real diffusion workloads (4096–8424 tokens).
- **Small, launch-bound shapes sit at parity (0.97–0.99×).** They cannot win at the kernel level
  (occupancy ~12%, launch-bound), and the dispatcher frame costs a sub-µs that, on a ~15 µs call,
  shows as ~1–3%. The RLCR *wrapper-level* headline (1.0723×) included tiny-shape wins that came from
  kda's leaner Python wrapper beating SGLang's heavier one; through the dispatcher those Python-only
  wins are neutralized, so the integrated geomean tracks the RLCR **module-level** geomean (1.0268×)
  minus dispatcher overhead. This is the expected, honest production behavior — net positive, with
  the win concentrated where the kernel is actually faster.
- Correctness is exact-to-baseline (1 ulp) and the fallback is intact, so the swap is safe to ship.
