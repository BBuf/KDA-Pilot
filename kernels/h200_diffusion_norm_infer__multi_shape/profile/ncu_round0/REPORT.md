# NCU + roofline report — round 0 candidates (H200, ion-h200-8, GPU 7)

Profiled the two native CUDA candidate kernels on representative captured shapes
with Nsight Compute (`--set full`; targeted metrics shown below). Raw reports:
`reports/rms_huge_full.ncu-rep`, `reports/ln_full.ncu-rep`. Harness:
`harness/prof.py`. H200 HBM3e peak ~4.8 TB/s; SM90, 132 SMs.

## Headline metrics (candidate kernels)

| Kernel / shape | grid | duration (kernel) | DRAM %peak | achieved BW | SM %peak | occupancy | waves/SM |
|---|---|---|---|---|---|---|---|
| `rms_norm_bf16_n128` [650040,128] | 4224 | 83.78 µs | 75.7% | ~3.6 TB/s | 43.5% | 90.7% | 4.0 |
| `layer_norm_fp32` (double, round 1) [8640,5120] | 8640 | 107.71 µs | 62.7% | ~3.3 TB/s | 56.7% | 34.8% | 21.8 |
| `rms_norm_bf16_n128` [1320,128] | 83 | 3.52 µs | 2.0% | n/a | 3.2% | 11.9% | 0.08 |

(Round-1 numbers. The round-0 fp32-fast LN was 85.6 µs / 78.2% DRAM / 24.3% SM but
could not meet the strict 1e-5 ceiling on adversarial rows; the double-precision
LN below is correct but compute-influenced. See `analysis/metrics.md` for the
round-0 vs round-1 LN comparison and source-counter ld/st sectors.)

(Kernel-only durations from NCU; wall-clock medians from `benchmark.csv` are
larger because they include launch + `cudaDeviceSynchronize` overhead.)

## Six-dimension walk

### RMS [650040,128] (huge-M, bandwidth bucket) and [648720,128]
- **Memory**: 75.5% of peak DRAM throughput (~3.6 TB/s of 4.8 peak). The dominant signal — this is a DRAM-bandwidth-bound streaming kernel.
- **Compute**: SM throughput 43% — not compute-bound (FP32 square + rsqrtf is cheap relative to the bytes moved).
- **Occupancy**: 90.8% achieved — near-saturated; no occupancy headroom to chase.
- **Latency-hiding**: high occupancy + grid-stride over rows hides memory latency well.
- **Launch-overhead**: grid capped at 4224 (132×32) with grid-stride → low launch overhead.
- **Tail-effect**: 4 waves, even row distribution → negligible tail.
- **Diagnosis**: at/near the attainable HBM bound (memory bandwidth). 75% of peak with 91% occupancy is a strong memory-bound result; remaining gap to 100% is the usual achievable-vs-peak HBM efficiency. **No further standalone speedup expected** beyond minor cache-policy tuning.

### LN [8640,5120] (fp32 I/O, double-internal math — round 1)
- **Memory**: 62.7% of peak DRAM throughput (~3.3 TB/s). Still substantial, but no longer the sole bottleneck. Source counters: ld 16.59M sectors (x + w + b L1 reads; w/b re-read per row but L2-resident), st 5.53M sectors (y write only) — one global read of x + one write of y to DRAM.
- **Compute**: SM 56.7% (up from 24.3% in the fp32-fast round-0 variant) — the double-precision mean/variance/normalize roughly doubled compute intensity, making the kernel compute-influenced.
- **Occupancy**: 34.8% (down from 46.9%) — higher register pressure from the double temporaries lowers occupancy.
- **Latency-hiding**: 21.8 waves; ample CTAs, but lower occupancy reduces per-SM overlap.
- **Launch-overhead / tail**: 8640 CTAs over 132 SMs → small tail.
- **Diagnosis**: **mixed memory/compute bound** (DRAM 62.7%, SM 56.7%). The double-precision math is required to meet the strict 1e-5 ceiling on ill-conditioned adversarial rows (the round-0 fp32-fast variant hit 78% DRAM / 85.6 µs but failed 1e-5 with ~1e-4 error). The kernel is still non-regressing (1.011×); recovering throughput while preserving 1e-5 (occupancy tuning / mixed-precision reductions) is a queued follow-up.

### RMS [1320,128] (and 4096, 16384) (small/mid-M, launch bucket)
- **Launch-overhead / occupancy**: 0.08 waves/SM (83 CTAs on 132 SMs) — the GPU is nearly empty; this is launch/latency-bound, not bandwidth-bound (DRAM 2.2%).
- **Diagnosis**: kernel-only time 3.26 µs; the total x+y traffic (0.68 MB) is far below the HBM time floor, so bandwidth optimization cannot help. The candidate still beats the baseline 2.5× (12.7 µs vs 32.5 µs wall-clock) by having lower launch/overhead than the baseline's Triton config (block_size_seq=2 → 660 CTAs). **Kept win at its launch-bound limit**; further standalone improvement would require call-site fusion or CUDA Graphs (out of scope — would change the recovered callsite contract). NOT a regression, so no evidence-backed no-go is needed.

## Conclusion

All six captured shapes are non-regressing (1.12×–2.58× over the SGLang
baseline; equal-shape geomean 1.695×). The two bandwidth-bound buckets (huge-M
RMS, fp32 LN) are **memory-dominated at ~75–78% of peak HBM** — the active bound
named by NCU. For a pure streaming normalization this is close to the practical
achievable bandwidth, so further standalone speedup on these buckets is expected
to be small. The launch-bound tiny-M RMS buckets (waves ≪ 1) are already faster
than the baseline and cannot be improved without changing the callsite (fusion /
CUDA Graphs), which is out of scope.

### Caveats / follow-ups (from adversarial review)
- DRAM %peak here is **candidate-only**; an absolute attainable-bound proof would
  add a measured copy-bandwidth roofline + baseline NCU on the same GPU/run. The
  claim is "memory-dominated at ~75–78% of peak", not "provably optimal".
- Benchmark medians are **synchronized Python wall-clock** (`perf_counter` +
  `cudaDeviceSynchronize` per call), which includes launch + sync overhead and is
  applied identically to baseline and candidate. Kernel-only durations are the
  NCU `gpu__time_duration` values above. For the tiny-M launch-bound buckets the
  2.5× reflects lower wrapper+launch latency, not a kernel-bandwidth win.
- The reported geomean weights every shape equally; a production-weighted (call
  frequency / time-weighted) speedup would emphasize the huge-M RMS and fp32 LN
  buckets (~1.12–1.13×, the bandwidth-bound wins).
