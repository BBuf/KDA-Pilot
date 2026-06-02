# Roofline / active-bound report — AC-E (round 5)

Hardware: NVIDIA B200 (sm_100), HBM3e ~8 TB/s peak. sglang 0b65588c, CUDA 13.0.88, torch 2.11.0+cu130.
NCU: `--set basic`, per-bucket reports in `reports/*.ncu-rep`, parsed metrics in `analysis/*.txt`
(profiled via the python JIT entrypoint `harness/prof_one.py`; CUDA kernels invoked directly so a
reduced-but-saturating shape exercises the real kernel, not the baseline fallback — `--set full`
on the full 177/333 MB tensors OOM-killed the shared container, so rates were taken at reduced
saturating shapes and combined with full-shape benchmark latency for achieved bandwidth).

Achieved bandwidth uses the FULL production shape's kernel-event latency from the interleaved
benchmark (`benchmark.csv`, cand-0004-dispatch). Bytes = read x + write y (+ tiny cached w/b,
NOT counted as full per-row DRAM, per the plan).

| bucket (production shape) | bytes moved | cand kernel-event | achieved BW | NCU rates (DRAM / Mem / SM / Occ) | active bound | decision |
|---|---|---|---|---|---|---|
| wide-LN helios `[8640,5120]` fp32 | 354 MB | ~67 µs | **~5.3 TB/s (~66% peak)** | 43% / 57% / 36% / 56% | **memory-bandwidth-leaning** | **PROMOTE** (1.19× — float4 + low regs beat the baseline's masked BLOCK_N=8192 lanes) |
| small-RMS `[1320,128]` bf16 | 0.68 MB | ~20 µs | ~0.03 TB/s | 2% / 4% / 11% / 40% | **launch / occupancy** (workload far too small to saturate 148 SMs) | **PROMOTE** (1.6× — one-warp/row has lower launch overhead than the baseline tile) |
| mid-RMS `[4096,128]`/`[16384,128]` bf16 | 2.1 / 8.4 MB | ~20 µs | 0.1-0.4 TB/s | 6% / 12% / 30% / 76% | **launch / occupancy** (partial wave; not yet bandwidth) | **PROMOTE** (1.5-1.7×) |
| large-RMS `[648720,128]`/`[650040,128]` bf16 | 333 MB | ~77 µs (cand) vs ~71 µs (baseline) | cand ~4.3 / baseline ~4.7 TB/s | kUnroll=1: 38% / 47% / 63% / 77% (round 4 full-shape); kUnroll=4: 15/24/42/**41** | **memory-latency + SM-issue; neither warp-per-row variant saturates BW** | **NO-GO → baseline fallback** (parity) |

## Per-bucket reasoning

- **Wide-LN (helios):** ~66% of peak DRAM bandwidth at the full shape; NCU shows memory-leaning (Mem 57% > SM 36%) with occupancy 56%. The candidate (`float4` loads/stores, `vals[≤5]` registers, parallel block reduction) wins 1.19× because the SGLang Triton baseline pads to `BLOCK_N=next_pow2(5120)=8192` and masks ~37% of lanes; the candidate moves only the real 5120 columns with wide transactions. Active bound = **memory bandwidth** (near the attainable region; further gains need a 2-SM/TMA streaming design, out of scope).

- **Small/mid-RMS (1320/4096/16384):** the workloads are tiny (≤8 MB); NCU shows everything < 30% and occupancy 40-76% — the kernel never approaches the bandwidth roofline. Active bound = **launch/occupancy/tail** (a "minimal-launch-latency" regime, exactly the plan's note for the small shape). The candidate wins 1.5-1.7× because one-warp-per-row has lower per-launch and per-tile overhead than the baseline's `BLOCK_SIZE_SEQ×128` tiled launch.

- **Large-RMS (648720/650040):** the only bandwidth-relevant RMS shapes (333 MB). Both the baseline (~4.7 TB/s, ~59% peak) and the candidate (~4.3 TB/s) are below the roofline. NCU shows the dilemma: kUnroll=1 has good occupancy (77%) but is **memory-latency bound** (long-scoreboard 56%); kUnroll=4 adds MLP but **drops occupancy to 41%** (fewer warps) and leans SM-issue (42%). Neither warp-per-row variant matches the baseline's 16-row tile, which amortizes the load pipeline better in this regime. Active bound = **memory-latency / occupancy trade-off the warp-per-row family cannot escape**. Decision: **NO-GO**, fall back to the (faster) Triton baseline → parity, no regression.

## Conclusion
Every production shape is parity-or-better: 4 CUDA wins (wide-LN + small/mid RMS) + 2 large-RMS at parity via documented no-go fallback. Geometric mean (outcome) 1.29× wall / 1.33× kernel. The promoted shapes are each close to their attainable bound (memory-BW for LN; launch/occupancy for small/mid RMS), and the large-RMS no-go is bounded by the memory-latency/occupancy trade-off with NCU + roofline evidence.
