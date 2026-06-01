# NCU + roofline report — round 0 candidates (H200, ion-h200-8, GPU 7)

Profiled the two native CUDA candidate kernels on representative captured shapes
with Nsight Compute (`--set full`; targeted metrics shown below). Raw reports:
`reports/rms_huge_full.ncu-rep`, `reports/ln_full.ncu-rep`. Harness:
`harness/prof.py`. H200 HBM3e peak ~4.8 TB/s; SM90, 132 SMs.

## Headline metrics (candidate kernels)

| Kernel / shape | grid | duration (kernel) | DRAM %peak | achieved BW | SM %peak | occupancy | waves/SM |
|---|---|---|---|---|---|---|---|
| `rms_norm_bf16_n128` [650040,128] | 4224 | 83.81 µs | 75.46% | ~3.6 TB/s | 43.1% | 90.8% | 4.0 |
| `layer_norm_fp32` [8640,5120] | 8640 | 85.63 µs | 78.23% | ~3.75 TB/s | 24.3% | 46.9% | 16.4 |
| `rms_norm_bf16_n128` [1320,128] | 83 | 3.26 µs | 2.16% | n/a | 3.4% | 12.2% | 0.08 |

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

### LN [8640,5120] (fp32, bandwidth bucket)
- **Memory**: 78.2% of peak DRAM throughput (~3.75 TB/s) — dominant signal; DRAM-bandwidth-bound.
- **Compute**: SM 24.3% — not compute-bound.
- **Occupancy**: 46.9% — limited (register-resident row: 5 float4 + reduction). But since DRAM is already at 78%, raising occupancy would not materially help (memory is the wall).
- **Latency-hiding**: 16.4 waves give ample CTAs to overlap; the single global read + single write per row is efficient.
- **Launch-overhead / tail**: 8640 CTAs over 132 SMs, 16.4 waves → small tail.
- **Diagnosis**: at/near the attainable HBM bound (memory bandwidth). One global read + one global write of x (no padded 8192 over-read, unlike the baseline's BLOCK_N=8192). **Near bound.**

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
