# NCU + roofline report (round 5) — H200, ion-h200-8, GPU 7

Authoritative round-5 evidence. Benchmark: commit `6aaec1397`, GPU 7 validated
idle BEFORE and AFTER the run (`idle_before=util0%/100MiB/procs0`,
`idle_after=util0%/717MiB/procs1` = own CUDA context only; benchmark.py aborts
without writing on a busy/unavailable snapshot). NCU values are from the round-1
collection and remain valid because the kernels are behaviorally unchanged since
commit `9c11e1cc8` (rounds 2-3 changed only `benchmark.py` + docs; rounds 4-5 added a
host-side multi-GPU `CUDAGuard` + registry-callable routing, both benchmark-inert).
H200 HBM3e peak ~4.8 TB/s; SM90, 132 SMs. Raw NCU: `reports/{rms_huge_full,ln_full,rms_huge_source,ln_source}.ncu-rep`.

## Benchmark (round 5, commit 6aaec1397, GPU 7 idle before+after)

| Shape | baseline median | candidate median | speedup |
|---|---|---|---|
| `norm_infer` LN fp32 [8640,5120] | 111.49 µs | 110.00 µs | 1.014× |
| `triton_one_pass_rms_norm` bf16 [648720,128] | 107.94 µs | 98.34 µs | 1.098× |
| `triton_one_pass_rms_norm` bf16 [650040,128] | 108.06 µs | 98.21 µs | 1.100× |
| `triton_one_pass_rms_norm` bf16 [16384,128] | 32.90 µs | 15.66 µs | 2.101× |
| `triton_one_pass_rms_norm` bf16 [4096,128] | 32.56 µs | 15.48 µs | 2.103× |
| `triton_one_pass_rms_norm` bf16 [1320,128] | 32.83 µs | 15.45 µs | 2.124× |

**Geomean (equal-shape) = 1.502×. No per-shape regression.** Wall-clock medians use
synchronized `perf_counter` + `cudaDeviceSynchronize`, applied identically to
baseline and candidate (includes launch + sync overhead). Kernel-only durations
below come from NCU.

## NCU headline metrics (candidate kernels; round-1 collection, kernels unchanged)

| Kernel / shape | grid | kernel duration | DRAM %peak | SM %peak | occupancy | waves/SM | active bound |
|---|---|---|---|---|---|---|---|
| `rms_norm_bf16_n128` [650040,128] | 4224 | 83.78 µs | 75.7% (~3.6 TB/s) | 43.5% | 90.7% | 4.0 | DRAM bandwidth |
| `layer_norm_fp32` (double) [8640,5120] | 8640 | 107.71 µs | 62.7% (~3.3 TB/s) | 56.7% | 34.8% | 21.8 | mixed memory/compute |
| `rms_norm_bf16_n128` [1320,128] | 83 | 3.52 µs | 2.0% | 3.2% | 11.9% | 0.08 | launch/occupancy |

Source counters (`--set source --section SourceCounters`): RMS [650040,128] global
ld/st = 5.47M / 5.20M sectors (matches x-read + y-write, coalesced, no waste);
LN [8640,5120] global ld/st = 16.59M / 5.53M sectors (ld = x + w + b L1 reads, w/b
L2-resident; st = y only). See `analysis/metrics.md`.

## Active-bound diagnosis (six dimensions)

- **RMS huge-M [650040,128] (and [648720,128])**: DRAM-bandwidth-bound at 75.7% of
  peak with 90.7% occupancy and SM only 43.5% — near the attainable HBM streaming
  bound. Source-counter sectors match the byte traffic (no wasted memory).
- **LN [8640,5120] (double-internal)**: **mixed memory/compute** — DRAM 62.7% AND SM
  56.7%, occupancy 34.8%. The double-precision mean/variance/normalize (required to
  meet the strict 1e-5 ceiling on ill-conditioned rows) roughly doubled compute
  intensity vs an fp32-accumulating kernel and lowered occupancy, so it is NOT
  purely bandwidth-bound and NOT at a 75-78% memory-bound practical limit. It
  remains non-regressing (1.016×). Recovering LN throughput while preserving 1e-5
  (occupancy / selective-precision reductions) is a queued follow-up.
- **RMS small/mid-M [1320/4096/16384,128]**: launch/occupancy-bound (0.08 waves for
  1320; the kernel is ~3.5 µs and the GPU is nearly empty). DRAM 2% — bandwidth
  optimization cannot help; the 2.0-2.1× win is lower launch+kernel overhead than the
  baseline Triton config. Further standalone speedup would need callsite fusion / CUDA
  Graphs (out of scope — would change the recovered callsite contract). Not a
  regression, so no evidence-backed no-go is required.

## Conclusion

All six captured shapes are non-regressing (1.014×–2.124×; equal-shape geomean
1.502×). RMS huge-M is memory-bandwidth-bound near the attainable HBM streaming
limit (75.7% of peak); LN (double) is mixed memory/compute (62.7% DRAM / 56.7% SM),
slower than an fp32 kernel would be but correct on adversarial rows; RMS small/mid-M
is launch-bound but still beats the baseline ~2×.

### Caveats / follow-ups
- DRAM %peak is candidate-only; an absolute attainable-bound proof would add a
  measured copy-bandwidth roofline + baseline NCU. Claim is "memory-dominated /
  mixed", not "provably optimal".
- The reported geomean weights every shape equally; a production/time-weighted
  speedup would emphasize the bandwidth-bound huge-M RMS and LN buckets.
- LN double-precision throughput recovery; mid-M RMS launch-config retune.
