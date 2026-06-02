# NCU + roofline — candidate v2 (native_cuda_v2_vectorized), near-bound + faster than baseline

- Host `ion-h200-8`, GPU 7 (NVIDIA H200, HBM3e ≈ 4.8 TB/s), container `sglang_bbuf`, sglang `c47f0e7cd` (≡ pinned `6965fe0ee`). kernel-pilot `be7bb20f1`, .cuh `42f21a8882a6`.
- NCU `--set full` + `--set source --section SourceCounters`, `KDA_PROFILE=1` (`-lineinfo`), post-warmup steady launch, `harness/` = `prof_entry.py`. Binary `*_full.ncu-rep` + `*_source.ncu-rep` kept under `REMOTE_KDA_DIR/work/profile/ncu_v2_20260602_065439/reports/` (1.2–1.3 MB / 0.18–0.23 MB; not committed). Parsed metrics: `analysis/metrics.csv`.

## v2 optimizations (from the Round-4 SM/instruction-bound diagnosis)
- Eliminated per-thread runtime div/mod via fixed grid geometry (one block per token / per `(b,s)`) + power-of-2 shift/mask indexing.
- 128-bit vectorized bf16 loads/stores (`AlignedVector<bf16x2,4>` = 8 bf16).
- Standard `cos`/`sin` loaded once per token into shared memory, reused across all heads.
- Numerics preserved (standard fp32 FMA + round-on-store; LTX-2 `(x*cos)->bf16`).

## Bound shift (v1 → v2), NCU SOL
| shape | kernel µs v1→v2 | DRAM% v1→v2 | SM% v1→v2 | occ% | active bound v2 |
|---|---|---|---|---|---|
| std hunyuanvideo | 299.5 → **90.6** | 22.9 → **75.0** | 80.4 → 37.5 | 81.4 | **memory-bandwidth** (~80% of HBM roofline, ideal ~72µs) |
| ltx2 S=6144 half64 | 120.1 → **34.6** | 24.2 → **79.5** | 77.0 → 42.3 | 81.0 | **memory-bandwidth** (~90% of roofline, ideal ~31µs) |

The active bound moved from SM/instruction-throughput (v1) to **HBM bandwidth** (v2) at ~75–79% DRAM (3.6–3.8 TB/s) — i.e. the kernels are **near the attainable bound**. The remaining ~10–20% headroom to the analytical roofline is small and typical (L2 traffic, address overhead).

## Result vs baseline (the headline)
Fair measurement (register module cached; allocation-fair; idle GPU 7):
- **Wall-clock benchmark geomean = 1.296×** over the 6 dedup shapes (1.12×–1.49×); see `benchmark.csv`.
- **GPU-kernel (CUDA-event) geomean = 1.297×** (std 1.37×; ltx2 1.00×–1.46×).
- The candidate is **faster than the autotuned SGLang Triton baseline on all 6 production shapes**, and is correct (6/6, CUDA route, bf16-noise).

Note: an earlier "0.21–0.25× (slower)" reading was a harness artifact — `candidate()` re-`exec`'d `register.py` per call (~120–150µs CPU import overhead) which `baseline()` did not; fixed by caching the register module. The kernels were already near-bound; the artifact only inflated the candidate's measured wall-clock.

## Active-bound / completion assessment (AC-5)
Both representative buckets are memory-bandwidth bound at ~75–79% DRAM and within ~10–20% of the analytical HBM roofline, AND the candidate beats the strong autotuned baseline by ~1.3× geomean. This is a near-attainable-bound result. Further gains (e.g., L2/cache-policy tuning, the tiny-shape wrapper overhead) are small; the candidate is in the near-bound regime for the important buckets. The tiny LTX-2 S=126 remains overhead-sensitive but still wins (1.42×) under the fair harness.
