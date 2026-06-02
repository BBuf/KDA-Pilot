# Roofline / active-bound report — AC-E (round 5)

Hardware: NVIDIA B200 (sm_100), HBM3e ~8 TB/s peak. sglang 0b65588c, CUDA 13.0.88, torch 2.11.0+cu130.
NCU: `--set basic`, per-bucket reports in `reports/*.ncu-rep`, parsed metrics in `analysis/*.txt`
(profiled via the python JIT entrypoint `harness/prof_one.py`; CUDA kernels invoked directly so the
profiled shape exercises the real kernel, not the baseline fallback). The small/mid-RMS production
shapes (`[1320,128]`, `[4096,128]`, `[16384,128]`; ≤8 MB) are profiled at their FULL production
shape — one report per shape (`rms1320`/`rms4096`/`rms16384`). Only the wide-LN and large-RMS
buckets needed a reduced-but-saturating proxy: `--set full` on the full 177/333 MB tensors
OOM-killed the shared container, so those rates were taken at reduced saturating shapes
(throughput/occupancy/stall rates are row-count-independent once saturated) and combined with
full-shape benchmark latency for achieved bandwidth.

Achieved bandwidth uses the FULL production shape's kernel-event latency from the interleaved
benchmark (`benchmark.csv`, cand-0004-dispatch). Bytes = read x + write y (+ tiny cached w/b,
NOT counted as full per-row DRAM, per the plan).

| bucket (production shape) | bytes moved | cand kernel-event | achieved BW | NCU rates (DRAM / Mem / SM / Occ) | active bound | decision |
|---|---|---|---|---|---|---|
| wide-LN helios `[8640,5120]` fp32 | 354 MB | ~67 µs | **~5.3 TB/s (~66% peak)** | 43% / 57% / 36% / 56% | **memory-bandwidth-leaning** | **PROMOTE** (1.19× — float4 + low regs beat the baseline's masked BLOCK_N=8192 lanes) |
| small-RMS `[1320,128]` bf16 (`rms1320`) | 0.68 MB | 20.4 µs (NCU kernel-only 6.85 µs) | ~0.03 TB/s | 0.8% / 2.6% / 3.6% / **15%** | **launch / occupancy** (only ~1320 rows ≈ 41 warps — the GPU is mostly idle; occ 15% is the most under-filled of all buckets) | **PROMOTE** (1.70× — one-warp/row has lower launch overhead than the baseline tile) |
| mid-RMS `[4096,128]` bf16 (`rms4096`) | 2.1 MB | 20.4 µs (NCU kernel-only 7.36 µs) | ~0.10 TB/s | 2.2% / 3.9% / 10.6% / **40%** | **launch / occupancy** (partial wave; nowhere near bandwidth) | **PROMOTE** (1.71×) |
| mid-RMS `[16384,128]` bf16 (`rms16384`) | 8.4 MB | 21.1 µs (NCU kernel-only 10.11 µs) | ~0.40 TB/s | 6.2% / 11.6% / 29.8% / **76%** | **launch / occupancy** (partial wave; not yet bandwidth) | **PROMOTE** (1.66×) |
| large-RMS `[648720,128]`/`[650040,128]` bf16 | 333 MB | ~77 µs (cand) vs ~71 µs (baseline) | cand ~4.3 / baseline ~4.7 TB/s | kUnroll=1: 38% / 47% / 63% / 77% (round 4 full-shape); kUnroll=4: 15/24/42/**41** | **memory-latency + SM-issue; neither warp-per-row variant saturates BW** | **NO-GO → baseline fallback** (parity) |

## Per-bucket reasoning

- **Wide-LN (helios):** ~66% of peak DRAM bandwidth at the full shape; NCU shows memory-leaning (Mem 57% > SM 36%) with occupancy 56%. The candidate (`float4` loads/stores, `vals[≤5]` registers, parallel block reduction) wins 1.19× because the SGLang Triton baseline pads to `BLOCK_N=next_pow2(5120)=8192` and masks ~37% of lanes; the candidate moves only the real 5120 columns with wide transactions. Active bound = **memory bandwidth** (near the attainable region; further gains need a 2-SM/TMA streaming design, out of scope).

- **Small/mid-RMS (1320 / 4096 / 16384):** the workloads are tiny (0.68–8.4 MB); every NCU meter is < 30% and occupancy climbs monotonically with row-count — **15% at S=1320, 40% at S=4096, 76% at S=16384** — so the kernel never approaches the bandwidth roofline. The launch-bound nature is direct: the measured per-call kernel-event latency (~20 µs) is ~2–3× the pure-kernel NCU `Duration` (6.85 / 7.36 / 10.11 µs), i.e. launch/dispatch/sync overhead dominates the wall time, not the loads or the compute. Active bound = **launch / occupancy / tail** (the plan's "minimal-launch-latency" regime; most acute at the smallest shape S=1320, where 15% occupancy leaves the GPU largely idle). The candidate wins 1.66–1.71× because one-warp-per-row has lower per-launch and per-tile overhead than the baseline's `BLOCK_SIZE_SEQ×128` tiled launch. Evidence: `reports/rms1320.ncu-rep` (small) + `reports/rms4096.ncu-rep`, `reports/rms16384.ncu-rep` (mid).

- **Large-RMS (648720/650040):** the only bandwidth-relevant RMS shapes (333 MB). Both the baseline (~4.7 TB/s, ~59% peak) and the candidate (~4.3 TB/s) are below the roofline. NCU shows the dilemma: kUnroll=1 has good occupancy (77%) but is **memory-latency bound** (long-scoreboard 56%); kUnroll=4 adds MLP but **drops occupancy to 41%** (fewer warps) and leans SM-issue (42%). Neither warp-per-row variant matches the baseline's 16-row tile, which amortizes the load pipeline better in this regime. Active bound = **memory-latency / occupancy trade-off the warp-per-row family cannot escape**. Decision: **NO-GO**, fall back to the (faster) Triton baseline → parity, no regression.

## Conclusion
Every production shape is parity-or-better: 4 CUDA wins (wide-LN + small/mid RMS) + 2 large-RMS at parity via documented no-go fallback. Geometric mean (outcome) 1.29× wall / 1.33× kernel. The promoted shapes are each close to their attainable bound (memory-BW for LN; launch/occupancy for small/mid RMS), and the large-RMS no-go is bounded by the memory-latency/occupancy trade-off with NCU + roofline evidence.
