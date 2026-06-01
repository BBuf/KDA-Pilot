# Dispatcher decision table — h200_diffusion_norm_infer__multi_shape

The native CUDA fast path intercepts ONLY the six captured production signatures
(exact shape + dtype + flags + eps=1e-6 + contiguous + 16B-aligned + H200 cap 9.0).
Everything else falls back to the SGLang baseline. Two specialized kernels (no
single universal kernel) because the buckets have different bounds.

| Bucket | Signature | Kernel | baseline → candidate (median) | speedup | NCU active bound | Decision |
|---|---|---|---|---|---|---|
| small image (FP32 LN) | `norm_infer` fp32 [8640,5120] w+b | `layer_norm_fp32` | 112.0 → 100.1 µs | 1.119× | DRAM 78.2% peak | **promote** |
| large video (RMS huge-M) | rms bf16 [648720,128] | `rms_norm_bf16_n128` | 108.3 → 95.9 µs | 1.129× | DRAM 75.5% peak | **promote** |
| large video (RMS huge-M) | rms bf16 [650040,128] | `rms_norm_bf16_n128` | 108.2 → 95.7 µs | 1.130× | DRAM (memory-bound) | **promote** |
| small video (RMS) | rms bf16 [16384,128] | `rms_norm_bf16_n128` | 33.2 → 13.2 µs | 2.506× | launch/occupancy | **promote** |
| small image (RMS) | rms bf16 [4096,128] | `rms_norm_bf16_n128` | 32.8 → 12.7 µs | 2.584× | launch/occupancy | **promote** |
| tiny (RMS) | rms bf16 [1320,128] | `rms_norm_bf16_n128` | 32.5 → 12.7 µs | 2.568× | launch (0.08 waves) | **promote** |

Geomean (equal-shape) = **1.695×**. No per-shape regression → no evidence-backed
no-go was required this round; both `EXPORTS` functions promoted to
`kda_kernels/diffusion/norm_infer/_impls/h200/`.

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
