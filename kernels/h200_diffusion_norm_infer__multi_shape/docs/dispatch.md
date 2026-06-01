# Dispatcher decision table — h200_diffusion_norm_infer__multi_shape

The native CUDA fast path intercepts ONLY the six captured production signatures
(exact shape + dtype + flags + eps=1e-6 + contiguous + 16B-aligned + H200 cap 9.0).
Everything else falls back to the SGLang baseline. Two specialized kernels (no
single universal kernel) because the buckets have different bounds.

Round-1 measurements (commit `9c11e1cc8`, idle GPU 7):

| Bucket | Signature | Kernel | baseline → candidate (median) | speedup | NCU active bound | Decision |
|---|---|---|---|---|---|---|
| small image (FP32 LN) | `norm_infer` fp32 [8640,5120] w+b | `layer_norm_fp32` (double) | 111.8 → 110.5 µs | 1.011× | mixed mem/compute (DRAM 62.7% / SM 56.7%) | **promote** |
| large video (RMS huge-M) | rms bf16 [648720,128] | `rms_norm_bf16_n128` | 108.3 → 98.9 µs | 1.095× | DRAM 75.7% peak | **promote** |
| large video (RMS huge-M) | rms bf16 [650040,128] | `rms_norm_bf16_n128` | 108.3 → 98.5 µs | 1.100× | DRAM (memory-bound) | **promote** |
| small video (RMS) | rms bf16 [16384,128] | `rms_norm_bf16_n128` | 32.5 → 16.0 µs | 2.023× | launch/occupancy | **promote** |
| small image (RMS) | rms bf16 [4096,128] | `rms_norm_bf16_n128` | 32.7 → 15.5 µs | 2.111× | launch/occupancy | **promote** |
| tiny (RMS) | rms bf16 [1320,128] | `rms_norm_bf16_n128` | 32.6 → 15.6 µs | 2.093× | launch (0.08 waves) | **promote** |

Geomean (equal-shape) = **1.488×**. No per-shape regression → no evidence-backed
no-go was required this round; both `EXPORTS` functions promoted to
`kda_kernels/diffusion/norm_infer/_impls/h200/`.

The FP32 LN kernel uses double-precision internal math (required to meet the strict
1e-5 ceiling on adversarial rows); this costs ~26% kernel time vs the round-0
fp32-fast variant (1.119× → 1.011×, still non-regressing) and makes it
compute-influenced rather than purely bandwidth-bound. RMS small/mid-M wall-clock
speedups vary run-to-run (host-side sync overhead dominates the ~3 µs kernel).

Notes:
- Huge-M RMS and FP32 LN are memory-bandwidth-bound at ~75–78% of peak HBM
  (near the practical streaming bound).
- Tiny/mid-M RMS (1320/4096/16384) are launch/occupancy-bound (≪1 wave) but still
  beat the baseline ~2.5× because the candidate has lower launch+kernel overhead
  than the baseline Triton config; no further standalone speedup without callsite
  fusion (out of scope).
- A single config (256 threads/CTA; RMS 16 rows/CTA + grid cap 132×32; LN 1 CTA/row)
  covers all M via grid-stride; shape-specialized launch configs were not needed
  to be non-regressing, though mid-M RMS could be retuned for more headroom in a
  later round (see solutions.jsonl follow-ups).
