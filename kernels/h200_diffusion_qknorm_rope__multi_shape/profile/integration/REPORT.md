# Integrated-overlay validation — qknorm_rope / h200

Validates the **promoted production path** (what `patches/sglang_kda_kernels.patch`
activates), not just the workspace `src/`: `import sglang` →
`kda_kernels.install()` swaps `sglang.jit_kernel.diffusion.qknorm_rope.fused_inplace_qknorm_rope`
to the family dispatcher → the dispatcher routes a CUDA `(9,0)` call to the
promoted h200 wrapper. The task-level `tests/test_correctness.py` (27/27) covers
the kernel via `src/`; this covers the install/dispatch/build plumbing on real
H200 hardware.

## Environment

- Host `ion-h200-8`, container `sglang_omni_bbuf_kda`, **idle GPU 7** (util 0%, ~100 MiB).
- sglang repo checkout `c47f0e7cd` via `PYTHONPATH=/home/sglang-omni/bbuf/repos/sglang/python`;
  flashinfer 0.6.1; torch 2.9.1+cu129.
- Overlay under test = this repo's `kda_kernels/` placed on `PYTHONPATH`.

## Commands

```bash
# patch applies cleanly to the current sglang HEAD (read-only check)
cd /home/sglang-omni/bbuf/repos/sglang && git apply --check patches/sglang_kda_kernels.patch   # -> Checking patch python/sglang/__init__.py... (clean)

# integrated overlay validation (idle H200)
PYTHONPATH=<kernel-pilot>:/home/sglang-omni/bbuf/repos/sglang/python CUDA_VISIBLE_DEVICES=7 \
  python profile/integration/validate_overlay.py
```

## Result (idle H200 GPU 7)

`install()` reports `('...qknorm_rope:fused_inplace_qknorm_rope', '...', 'swapped')`;
`swapped.__module__ == kda_kernels.diffusion.qknorm_rope._dispatcher`; every shape
routes `path=cuda`, returns `None`, and matches the oracle to 1 bf16 ulp
(maxd 0.0625, ATOL=8e-2/RTOL=1e-2).

| shape | base µs | overlay µs | speedup |
|---|---|---|---|
| qwen__T4096_H24 | 44.93 | 39.50 | 1.137× |
| qwen__T19_H24 | 16.13 | 15.58 | 1.035× |
| qwen__T47_H24 | 16.16 | 15.65 | 1.033× |
| qwen_edit__T8424_H24 | 83.09 | 72.10 | 1.153× |
| qwen_edit__T195_H24 | 16.45 | 15.68 | 1.049× |
| qwen_edit__T189_H24 | 16.53 | 15.55 | 1.063× |
| zimage__T4096_H30 | 53.86 | 47.42 | 1.136× |
| zimage__T32_H30 | 16.19 | 15.71 | 1.031× |
| zimage__T4128_H30 | 54.14 | 47.65 | 1.136× |

**GEOMEAN = 1.0846× over 9 shapes; CORRECTNESS PASS; every shape ≥ 1.03× (no regressions).**

## Why the dispatcher was optimized (required to reach this)

The first integrated run regressed to **0.898× geomean** even though the kernel
itself is faster. Isolating the path (`base` vs `wrapper_direct` vs `dispatched`)
showed the kernel wins (`wrapper_direct/base` = 1.08–1.17×) but the generic Python
**dispatcher added a flat ~5.2 µs/call** — dominated by `torch.cuda.get_device_capability`
(~1.95 µs) plus per-call `getattr`, dict-of-dict lookups, a tensor-iterator
generator, and extra call frames. On launch-bound tiny shapes (~15 µs) that tax
turned a real win into a 0.82× loss.

Fix (in `scripts/export_kda_kernels/export.py`, the dispatcher template, then
regenerated into `kda_kernels/diffusion/qknorm_rope/_dispatcher.py`): memoize the
resolved target callable per `(fn_name, device_index)` so the steady-state hot
path skips capability probing, module import, and attribute lookup; read
`KDA_FORCE_ARCH` once at import; inline the cache fast path into each generated
dispatch function. Behavior is unchanged (same per-device routing, same baseline
fallback for unsupported arch/CPU, same recursion-safe preload); only the
per-call cost changes.

Per-call dispatch overhead, before → after:

| shape | dispatch_oh before | dispatch_oh after |
|---|---|---|
| tiny_T47 | 5.22 µs | 0.77 µs |
| small_T195 | 5.18 µs | 0.74 µs |
| large_T4096 | 4.96 µs | 0.70 µs |
| large_T8424 | 5.30 µs | 0.85 µs |
