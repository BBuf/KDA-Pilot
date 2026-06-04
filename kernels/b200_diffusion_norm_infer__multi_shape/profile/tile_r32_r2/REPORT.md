# NCU bound report — tiled multi-row RMSNorm winner vs Triton baseline (S=650040, D=128, bf16)

Run: round-2 tile reopen, ion-b200 (= `innomatrix-us-adc-smb200-0003`), NVIDIA B200 GPU 1
(idle; host otherwise loaded), sglang `edb1b3f8f`, CUDA 13.0, driver 580.126.20.
Kernels profiled at the captured production shape `[650040, 128]` bf16 (verbatim):
- `rmsnorm_tiled_kernel<128,32,bf16>` (R=32, persistent whole-wave grid 592×256, the live A/B winner)
- `_rms_norm_tiled_onepass` (SGLang Triton baseline, 16-row tile, grid 40628×128)

Reports: `reports/full.ncu-rep`, `reports/source.ncu-rep` (tiled, `-lineinfo`),
`reports/baseline_full.ncu-rep`; parsed metrics in `analysis/metrics.csv`
(collector: `harness/parse_reports.py`; `-s 3 -c 1`, i.e. 4th launch).

## Key metrics (NCU default clock control = locked base clocks, flushed caches)

| metric | tiled R=32 persistent | Triton baseline |
|---|---|---|
| duration | 74.78 µs | 63.33 µs |
| DRAM throughput (% peak elapsed) | 57.8% | 68.1% |
| DRAM bytes read / write | 166.4 MB / 121.2 MB | 166.4 MB / 120.9 MB |
| SM throughput | 48.4% | 63.8% |
| achieved occupancy | 46.8% (≈ its 50% ceiling: 4 CTA/SM × 8 warps, 56 regs) | 88.5% (32 regs) |
| grid × block | 592 × 256 | 40628 × 128 |
| long-scoreboard stall / issue-active | 8.0% / 55.9% | 6.8% / 70.2% |
| L2 hit rate | ~0% (flushed) | ~0% (flushed) |

`--clock-control none` spot-check (live boost clocks, still NCU-serialized + cache-controlled):
tiled 55.1–55.8 µs (DRAM ~67%); baseline 45.9–49.3 µs (DRAM 78–82%).

## Live interleaved A/B on the same GPU (per-iteration alternation, warm steady state)

tiled 72.3–72.9 µs kernel-event vs pinned baseline 83.1–84.7 µs → tiled wins
1.141–1.161× kernel-event / 1.099–1.110× wall in two independent runs
(paired-bootstrap CI95 lower bounds 1.094–1.152; `benchmark.csv`
`cand-0010-tile-r32-persistent`, `-rep2`).

## Six dimensions (tiled winner)

1. **Compute**: SM 48.4%, issue-active 55.9% — moderate; not compute-bound. The
   16-lane butterfly + fp32 math fits in the issue budget at 46.8% occupancy.
2. **Memory**: DRAM 57.8% locked / ~67% live-clocks isolated. Reads exactly match
   the logical 166.4 MB; DRAM-level writes (121 MB) sit below the logical 166 MB
   because part of the output write-back stays in the 126 MB L2 at kernel end —
   the next kernel in a real pipeline inherits that write-back debt.
3. **Occupancy**: 46.8% achieved ≈ the 50% configuration ceiling (4 resident
   CTAs/SM × 256 threads, 56 registers). Raising it would need fewer registers
   per thread (more rows per CTA inflate the register file: R=32 keeps 2×16B x
   vectors + 8 fp32 weights + accumulators live per lane).
4. **Latency hiding**: long-scoreboard 8.0% — the two-pair MLP (both 16B loads
   issued before either reduction) plus the persistent loop hides global-load
   latency; this was 56% on the no-go warp-per-row kernel. The design goal of the
   re-open condition is met.
5. **Launch overhead**: 592 CTAs once vs 40.6k CTAs (baseline) — the persistent
   schedule removes the CTA launch/drain wave machinery; this is the main reason
   the tile kernel is robust in the back-to-back regime (see below).
6. **Tail effect**: grid-stride over 20,314 tiles ÷ 592 CTAs ≈ 34.3 iterations —
   the 0.3 fractional wave amortizes to <1% tail; no action needed.

## Context-dependence (the headline finding)

The ranking depends on execution context:
- **NCU isolation (serialized, cache-flushed)**: baseline faster (46–49 µs live
  clocks; 78–82% DRAM) than tiled (55–56 µs; ~67%). With a clean L2 and no
  neighboring work, the 88%-occupancy Triton tile streams nearly at the DRAM
  roofline and its 40.6k-CTA launch wave is fully absorbed.
- **Steady-state alternation (live A/B, production-like back-to-back kernels)**:
  tiled faster (72 vs 84 µs). Each launch inherits ~126 MB of dirty L2
  write-back from the previous kernel; the bandwidth-hungry baseline loses ~70%
  of its isolated speed (49→84 µs, achieved BW ~3.4 TB/s), while the
  issue-limited persistent tile loses ~29% (56→72 µs, ~3.97 TB/s) and comes out
  ahead. Both sides of the A/B pay the predecessor's debt symmetrically, and the
  diffusion denoise pipeline (this op runs amid attention/GEMM traffic every
  step) matches the dirty-L2 regime, not the flushed-isolation one.

## Active bound (tiled winner, named)

Mixed memory-bandwidth / issue limit: ~67% DRAM at live clocks in isolation with
SM 38–48% and stalls well-controlled; in the production-like regime its
effective ceiling is set by DRAM write-back contention shared with neighboring
kernels. Occupancy is at its configuration ceiling; the remaining ~33% DRAM
headroom is not reachable without either more resident warps (register-bound) or
removing the write-back debt (outside a single kernel's control).

## Decision input

The live interleaved A/B (the declared promotion lane: same arbiter as the
rebaseline rows, production-like steady state, two independent runs, CI-gated)
says PROMOTE for both huge shapes; the flushed-isolation NCU comparison says the
Triton baseline retains an advantage in clean-cache conditions. Verdict and
routing decision recorded in `docs/dispatch.md` after the round-2 design review
(`solutions.jsonl::cand-0010-tile-r32-persistent`).
