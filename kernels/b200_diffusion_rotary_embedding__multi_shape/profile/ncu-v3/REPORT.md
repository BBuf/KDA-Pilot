# NCU Report — ncu-v3: continuation candidates (cuda-v6 standard win; half32 D5 decision), B200 / sm_100

> Continuation-run profiling (k09, 2026-06-04). Prior map: `profile/ncu-v2/REPORT.md` (cuda-v4).
> Candidate under profile: `cuda-v6` (src `317e2fab7ade`) — standard kernel changed (cos/sin
> register hoist + full-pass 128-thread blocks); LTX-2 kernel byte-identical to cuda-v4.

- Host/GPU: `ion-b200` (innomatrix-us-adc-smb200-0003), container `sglang_bbuf`, NVIDIA B200 GPU 1 (idle-gated 0%/0MiB before and after), driver 580.126.20, CC 10.0.
- Environment: SGLang `edb1b3f8f` (container checkout; see BASELINE SHIFT in `docs/draft.md`), torch 2.11.0+cu130, triton 3.6.0, nvcc 13.0, tvm_ffi 0.1.9.
- Harness: `harness/profile_one.py` (8 warmed launches; NCU profiles one). Collection:
  `ncu --set full --target-processes all -k regex:rotary --launch-skip 6 --launch-count 1`.
  Reports: `reports/std_v6.ncu-rep`, `reports/half32_24576_v6.ncu-rep`; parsed text in `analysis/`.
  (SourceCounters set waived this run: the decision questions — active bound per bucket and the
  D5 go/no-go — are answered by section-level metrics; no per-line stall attribution needed.)

## Measured (NCU full set, warmed launch; durations are replay-inflated — clean CUDA-event medians govern)

| Kernel / shape | Duration (replay) | DRAM SOL % | Compute (SM) SOL % | L1/TEX % | L2 % | Achieved Occ % | Regs | Block | Waves/SM |
|---|---|---|---|---|---|---|---|---|---|
| `standard_rotary_kernel<128>` cuda-v6, 1×27030×24×128 | 64.99 µs | **69.82** | 47.14 | 60.90 | 51.46 | 87.64 | 30 | 128 | 11.41 |
| `ltx2_split_rotary_kernel<32>` (unchanged), 1×24576×2048 | 53.57 µs | **76.08** | 63.66 | 61.36 | 56.49 | 85.03 | 32 | 128 | 10.38 |

Prior cuda-v4 standard row (ncu-v2): DRAM 59.1 / SM 62.1 / occ 80.2 — the v6 hoist + full-pass
blocks moved the kernel from compute/BW-balanced to clearly **memory-paced** (DRAM +10.7 pts,
compute −15 pts), which is what the instruction diet was supposed to do.

## Six-dimension walk (per ncu-report-skill)

1. **Compute** — standard now 47% (was 62%): no longer co-limiting. NCU's fused/non-fused FP32 rule
   (Est 6%) is not actionable without changing the rotation math contract, and compute is not the wall.
2. **Memory** — dominant for both. standard 69.8% DRAM SOL (clean-benchmark effective ≈ 346 MB /
   57.7 µs ≈ 6.0 TB/s ≈ 75% of ~8 TB/s). half32-large 76.1% (≈ 302 MB / 49.5 µs ≈ 6.1 TB/s). No
   sectors-per-request or uncoalesced-access rule fired for either kernel — access is clean.
3. **Occupancy** — healthy: 87.6% / 85.0%; not the limiter.
4. **Latency-hiding** — standard's dominant stall: L1TEX long-scoreboard 20.6 cyc/warp (NCU Est 30%).
   Tested directly with cuda-v7 (register double-buffer of the x vector): **zero movement**
   (57.73/57.74/57.76 vs 57.7 µs). With 11.4 waves and 87.6% occupancy the SM has ample warps; the
   stall signature reflects DRAM queueing, not insufficient per-thread MLP.
5. **Launch-overhead** — unchanged story for the small LTX-2 shapes (ncu-v2: 0.05 waves/SM). New
   evidence this run: halving the small-shape grid (cuda-v5's two-rows-per-CTA) regressed
   1×126×2048 by 12% — the small bucket is hypersensitive to launch/grid shape and sits at its floor.
6. **Tail** — large shapes have 10–11 waves; tail negligible.

## Decisions from this evidence

- **Standard bucket: cuda-v6 is at its attainable bound.** Two NCU-motivated levers were tried:
  instruction diet (v6: 61.86 → 57.7 µs, 1.071× over cuda-v4, gate-passed) and per-thread MLP
  (v7: rejected, zero movement). Compute is at 47% (not limiting), occupancy 87.6%, access clean —
  remaining gap to the ~82–85% ceiling is DRAM-queue efficiency inherent to the three-stream
  (bf16 x-read + fp32 cos/sin + bf16 write) pattern. **D3 (bf16-packed math) = no-go by evidence:**
  a compute diet cannot speed up a kernel whose compute pipe is half idle.
- **LTX-2 large-half32: no-go (cuda-v4/v6 kernel already at bound).** 76.1% DRAM SOL, clean
  coalescing, no LSU/sector rule fired → the Codex-required evidence bar for D5 (256-bit loads /
  cache hints) is NOT met; the ~9-point gap to half64's 85.3% is attributed to the halved per-row
  byte granularity of the layout, not an addressable instruction or cache lever. D1 (two-rows-per-
  CTA) measured 1.0006× on this shape — residency math confirmed by experiment.
- **LTX-2 small: no-go** (launch floor; reinforced by the v5 grid-halving regression). Host-side
  dispatch-cost work (old D4) is out of this run's gate per the Codex triage review.
- **LTX-2 large-half64: no-go stands** (kernel unchanged; ncu-v2's 85.3% DRAM SOL row remains valid).

## Roofline summary (clean CUDA-event medians, B200 HBM3e ≈ 8 TB/s)

| Bucket | Bytes | cuda-v6 median | Eff. BW | % peak | vs cuda-v4 | Active bound |
|---|---|---|---|---|---|---|
| standard 1×27030×24×128 | ~346 MB | 57.7 µs | ~6.0 TB/s | ~75% | 1.0709–1.0718× | DRAM bandwidth (queue-paced) |
| LTX-2 large half64 | ~604 MB | 92.5 µs | ~6.5 TB/s | ~82% | 1.0000× | DRAM bandwidth (ceiling) |
| LTX-2 large half32 | ~302 MB | 49.5 µs | ~6.1 TB/s | ~76% | 1.0000–1.0006× | DRAM bandwidth (layout granularity) |
| LTX-2 small (126…1536) | ≤ 25 MB | 21–22 µs | ≤ 1 TB/s | ≤ 12% | within noise | launch/latency floor |
