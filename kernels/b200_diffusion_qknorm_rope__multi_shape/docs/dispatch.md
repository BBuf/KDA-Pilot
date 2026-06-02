# Dispatch decision table — b200_diffusion_qknorm_rope__multi_shape

> **FINAL OUTCOME (supersedes the overlay no-go below):** the kernel ships via an **in-tree
> `.cuh` placement** in SGLang (keeping SGLang's own `register_custom_op` → **torch.compile-safe**),
> not the `kda_kernels` overlay. In-tree device geomean **~1.07–1.12x** (large 1.10–1.33x, small
> parity), correctness 10/10. See `docs/sglang_jit_export.md`. The sections below describe the
> (un-promoted) overlay dispatcher and its eager install-path numbers, kept for contrast — the
> overlay drops `register_custom_op` and is NOT torch.compile-safe.

`optimized_wrapper` (in `src/wrapper.py`, forwarded by `src/register.py`) is an
**exact-shape, fail-closed dispatcher**. It reads **no environment variables**.

- Staged CUDA kernel (`QKNormRopeStagedKernel`, CTA-per-token cos/sin staging) is selected
  ONLY for the exact large captured **`(num_tokens, num_heads, eps)`** production rows AND
  the full production contract: `head_dim=128`, `rope_dim=128`, `is_neox=False`; q/k/weights
  bf16; `cos_sin_cache` float32; `positions` int64; q/k/weights contiguous + 16-byte aligned;
  q/k non-overlapping. The five staged rows are `{(7904,32,1e-6), (4096,24,1e-6),
  (8424,24,1e-6), (4096,30,1e-5), (4128,30,1e-5)}`.
- **Everything else** — the 5 small captured rows, any non-captured `(tokens,heads)`, a
  captured `(tokens,heads)` with the wrong `eps`, any non-production dtype/dim/flag/layout,
  or non-contiguous/misaligned/aliased tensors → **SGLang baseline fallback** (explicit,
  before the C++ `TensorMatcher`). On the installed overlay the fallback calls the captured
  ORIGINAL baseline (non-recursive); off-overlay it calls the SGLang baseline directly.

`KDA_CAND_VARIANT={warp,staged}` is a **diagnostic-only** switch for `benchmark.py
--device-fair` (it picks which device kernel the symmetric A/B builds); it has NO effect on
the public `optimized_wrapper`.

## The bottom line: evidence-backed NO-GO on the production install path

The staged kernel is a **real device win** but a **net regression once installed** through the
`kda_kernels` overlay. It is **NOT promoted**. Full write-up: `docs/sglang_jit_export.md`.

| metric (idle B200, GPU 4) | geomean | per-shape |
|---|---|---|
| **Literal install path** (`kda_kernels.install()`; baseline custom-op vs INSTALLED symbol) | **0.9301x / 0.9185x** (regression) | joyai 1.21x; qwen 0.97x; qwen-edit 1.00x; zimage 0.93x/0.93x; **5 small 0.85–0.87x** |
| Device-fair (symmetric direct-JIT, both kernels) | 1.0679x | large 1.10–1.26x; small 0.98–1.00x |
| Device-fair warp faithful-port sanity | 0.9999x | confirms the device-fair comparison is fair |

### Per-shape install-path detail (run 1, `benchmark.csv` `*__install` rows)
| shape | bucket | route | base µs | installed µs | install speedup |
|-------|--------|-------|---------|--------------|-----------------|
| joyai-edit B7904/H32 | large | staged | 91.1 | 75.3 | **1.21x** |
| qwen B4096/H24 | large | staged | 58.4 | 60.1 | 0.97x |
| qwen-edit B8424/H24 | large | staged | 102.8 | 103.0 | 1.00x |
| zimage B4096/H30 | large | staged | 78.1 | 84.1 | 0.93x |
| zimage B4128/H30 | large | staged | 77.5 | 83.8 | 0.93x |
| qwen B19/H24 | small | baseline | 64.8 | 74.6 | 0.87x |
| qwen B47/H24 | small | baseline | 64.0 | 74.5 | 0.86x |
| qwen-edit B195/H24 | small | baseline | 64.4 | 74.2 | 0.87x |
| qwen-edit B189/H24 | small | baseline | 64.1 | 74.7 | 0.86x |
| zimage B32/H30 | small | baseline | 65.0 | 75.0 | 0.87x |

### Why the device win does not survive (named active bound)
The production active bound is **host-side dispatch/launch overhead**, not the device kernel.
The device-fair→install gap (1.07x → 0.93x) is the **overlay per-call Python dispatch tax**
(generated dispatcher + wrapper frame + gate, ~7 µs more than the baseline's C-level
`register_custom_op`). Only joyai-edit B7904/H32 has a device saving (~18 µs) big enough to
overcome it; the other four large shapes save 4.5–11 µs (parity-to-loss after the tax), and
the five small shapes are dispatch-bound (~9.7 µs device vs ~65 µs end-to-end) so they have
no device saving to offset any interception cost → ~0.86x. Equal-weight geomean over the 10
rows is therefore < 1 on the install path.

## Why small shapes route to baseline (NCU evidence)
`profile/baseline_b200/REPORT.md`: small shapes are **launch/dispatch-bound** — the device
kernel is only ~7.55 µs vs ~60 µs end-to-end (~88% host dispatch), and the grid is tiny
(114 < 148 SMs, 0.10 waves/SM). Staging needs more CTAs per token, so it does not help
(device-fair ~1.0x). The device kernel is not the small-shape bottleneck.

## Why large shapes route to staged (NCU evidence)
`profile/staged_b200/REPORT.md`: staging cuts `long_scoreboard` 11.9 → 9.29 and device time
109.6 → 88.1 µs on B8424 (the float32 cos/sin row is staged once per token and reused across
heads instead of re-read per head). This device win is real and reproduces (device-fair
1.10–1.26x on the large bucket) — but it is smaller than the overlay dispatch tax for all but
the largest shape, so it does not yield a net install-path win.

## Reproduce
```bash
# device-fair (symmetric, isolates the device kernel):
CUDA_VISIBLE_DEVICES=4 KDA_CAND_VARIANT=staged PYTHONPATH=<repo-root> python benchmark.py --device-fair
# literal install path (the production claim):
python3 scripts/export_kda_kernels/export.py b200_diffusion_qknorm_rope__multi_shape
CUDA_VISIBLE_DEVICES=4 PYTHONPATH=<repo-root> python benchmark.py --integrated
```
