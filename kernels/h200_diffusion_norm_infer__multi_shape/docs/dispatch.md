# Dispatcher decision table — h200_diffusion_norm_infer__multi_shape

The native CUDA fast path intercepts ONLY the six captured production signatures
(exact shape + dtype + rank-1 weight/bias/w exact length + flags + eps=1e-6 +
contiguous + 16B-aligned + H200 cap 9.0). Everything else falls back to the SGLang
baseline. Two specialized kernels (no single universal kernel) because the buckets
have different active bounds.

Round-5 measurements (commit `6aaec1397`, idle GPU 7 validated before AND after:
idle_before util0%/100MiB/procs0, idle_after util0%/717MiB/procs1; geomean from `benchmark.csv`):

| Bucket | Signature | Kernel | baseline → candidate (median) | speedup | NCU active bound | Decision |
|---|---|---|---|---|---|---|
| small image (FP32 LN) | `norm_infer` fp32 [8640,5120] w+b | `layer_norm_fp32` (double) | 111.5 → 110.0 µs | 1.014× | mixed memory/compute (DRAM 62.7% / SM 56.7%) | **promote** |
| large video (RMS huge-M) | rms bf16 [648720,128] | `rms_norm_bf16_n128` | 107.9 → 98.3 µs | 1.098× | DRAM 75.7% peak | **promote** |
| large video (RMS huge-M) | rms bf16 [650040,128] | `rms_norm_bf16_n128` | 108.1 → 98.2 µs | 1.100× | DRAM bandwidth | **promote** |
| small video (RMS) | rms bf16 [16384,128] | `rms_norm_bf16_n128` | 32.9 → 15.7 µs | 2.101× | launch/occupancy | **promote** |
| small image (RMS) | rms bf16 [4096,128] | `rms_norm_bf16_n128` | 32.6 → 15.5 µs | 2.103× | launch/occupancy | **promote** |
| tiny (RMS) | rms bf16 [1320,128] | `rms_norm_bf16_n128` | 32.8 → 15.5 µs | 2.124× | launch (0.08 waves) | **promote** |

Geomean (equal-shape) = **1.502×**. No per-shape regression → no evidence-backed
no-go was required; both `EXPORTS` functions promoted to
`kda_kernels/diffusion/norm_infer/_impls/h200/`.

Notes:
- RMS huge-M is DRAM-bandwidth-bound at ~75.7% of peak HBM (near the attainable
  streaming limit).
- FP32 LN is **mixed memory/compute** (DRAM 62.7% / SM 56.7%), NOT memory-bound at a
  75-78% practical limit: the double-precision internal math (required for the strict
  1e-5 ceiling on adversarial rows) roughly doubled compute intensity and lowered
  occupancy. It is non-regressing (1.016×); throughput recovery is a queued follow-up.
- RMS small/mid-M (1320/4096/16384) is launch/occupancy-bound (≪1 wave) but still
  beats the baseline ~2× via lower launch+kernel overhead; no further standalone
  speedup without callsite fusion (out of scope). Their wall-clock speedups vary
  run-to-run because the ~3.5 µs kernel is dominated by host-side sync overhead.
- A single config (256 threads/CTA; RMS 16 rows/CTA + grid cap 132×32 grid-stride;
  LN 1 CTA/row) covers all M; shape-specialized launch configs were not needed to be
  non-regressing (mid-M RMS retune is a queued follow-up).
