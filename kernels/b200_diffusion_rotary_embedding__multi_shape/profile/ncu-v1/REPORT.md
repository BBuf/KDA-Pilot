# NCU + Roofline report — cuda-v1 rotary candidate (B200, run ncu-v1)

Host `ion-b200`, container `sglang_bbuf`, idle B200 GPU 3. Candidate kp_commit `fb7427793`.
Tool: Nsight Compute `ncu --set full` (the `external/ncu-report-skill` submodule was empty/uninitialized,
so metrics were parsed directly from `ncu --import --page details`; the same six-dimension analysis is
applied below). Reports: `profile/ncu-v1/reports/{std,ltx2_large}.ncu-rep`.

## NCU Speed-of-Light (profiled launch, candidate kernels)

| Bucket | Kernel | Duration (ncu) | Memory SOL | DRAM SOL | Compute SOL | Achieved Occupancy | Mem throughput |
|---|---|---|---|---|---|---|---|
| standard-large `[1,27030,24,128]` | `rope_std_kernel` | 93.0 µs | **60.0%** | 49.3% | 52.5% | 82.6% | 3.29 TB/s |
| LTX-2 large `[1,24576,4096]` | `ltx2_split_kernel<64>` | 99.7 µs | **85.7%** | **85.7%** | 73.0% | 85.3% | 5.71 TB/s |

(ncu single-launch durations run longer than the warm CUDA-event medians in `benchmark.csv` — 75/99 µs —
because ncu serializes/instruments; the SOL *ratios* are the bound-naming signal, not the absolute µs.)

## Roofline (effective bytes moved vs achieved DRAM bandwidth; B200 HBM3e peak ≈ 8 TB/s)

Effective bytes = x read + out write (both bf16, out-of-place) + cos/sin reads. Achieved BW = bytes / candidate median (benchmark.csv).

| Bucket | bytes moved | baseline µs / BW | candidate µs / BW | speedup | active bound |
|---|---|---|---|---|---|
| standard-large | ~345.9 MB | 133.9 / 2.58 TB/s | 75.5 / **4.58 TB/s** (~57% peak) | 1.77× | memory-leaning, NOT saturated (60% SOL) — headroom exists; win comes from 128-bit vectorization + cos/sin reuse across 24 heads vs baseline 2.58 TB/s |
| LTX-2 large (24576) | ~603.9 MB | 104.5 / 5.78 TB/s | 98.7 / **6.12 TB/s** (~76% peak, 85.7% ncu SOL) | 1.06× | **DRAM-bandwidth bound, near roofline** — both impls saturate BW; ~14% headroom to SOL peak; little left to win |
| LTX-2 mid (6144) | ~150.9 MB | 40.4 / 3.73 TB/s | 33.6 / **4.49 TB/s** | 1.20× | partial BW saturation (same kernel as large; interpolates) — roofline-only, not separately ncu'd |
| LTX-2 small (126) | ~1.55 MB | 21.6 / 0.072 TB/s | 14.9 / **0.10 TB/s** | 1.46× | **launch/latency bound** — 0.10 TB/s is ~1.3% of peak; the ~15 µs is launch/dispatch overhead, not bandwidth; candidate wins via a lighter native launch path. roofline-only (bound obvious from size) |

## Six-dimension read (the two profiled buckets)
- **Compute**: not the bound (52% std, 73% ltx2-large SOL). Trivial arithmetic (a few FMAs/element); tensor cores irrelevant — confirms the Round-0 scoping that tcgen05/TMEM are not applicable.
- **Memory**: the dominant axis. LTX-2-large at 85.7% DRAM SOL = bandwidth-bound; standard at 60% = sub-saturated.
- **Occupancy**: healthy (82–85%); 32 regs/thread, ~21 waves/SM — not occupancy limited.
- **Latency-hiding**: adequate at large sizes (high occupancy hides latency); dominates only at the 126-token tail.
- **Launch-overhead**: the active bound for the 126-token bucket (sub-MB data).
- **Tail-effect**: 20–23 waves/SM → minor quantization tail, not limiting.

## Diagnosis & promotion implication
- The candidate is **memory-bandwidth / launch-latency bound** across the table (as predicted) and **near the attainable bound on the wall-clock-dominant large LTX-2 bucket (85.7% DRAM SOL)** — chasing more there has diminishing returns, so promoting cuda-v1 is justified rather than continuing to optimize.
- The standard kernel has residual headroom (60% memory SOL) — a future multi-token-per-CTA variant could push BW higher — but it already wins **1.77×**, the largest absolute win, so further tuning is optional, not blocking.
- Net: correct on every captured shape, beats baseline everywhere (geomean 1.3676×), with a named active bound per bucket. **Promote cuda-v1** (both entry points).

## Notes
- `external/ncu-report-skill` submodule was empty (not initialized); profiling followed its documented pattern (`profile/<run>/{harness,reports}`, `ncu --set full`, six-dimension walk) using raw `ncu` parsing.
- mid (6144) and small (126) buckets were not separately ncu-profiled: mid runs the identical `ltx2_split_kernel` as large (same bound, interpolated), and small is unambiguously launch-bound from its sub-MB footprint and ~15 µs floor. Both are covered by roofline above.
