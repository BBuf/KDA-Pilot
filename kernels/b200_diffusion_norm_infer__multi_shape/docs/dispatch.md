# Dispatch table — b200_diffusion_norm_infer__multi_shape

Final per-bucket routing for the six production shapes. The dispatcher
(`src/register.py`) routes a shape to the native CUDA kernel iff it matches the
explicit allowlist + input validation; everything else falls back to the SGLang
Triton baseline. Measured on idle NVIDIA B200 (interleaved A/B, cand-0004-dispatch;
sglang 0b65588c, CUDA 13.0.88, torch 2.11.0+cu130). Speedups are baseline/candidate
median (wall-clock primary; kernel-event in parens). Geomean (outcome): 1.29× wall /
1.33× kernel. Evidence: `benchmark.csv`, `solutions.jsonl::cand-0004-dispatch`,
`profile/ac_e_r5/REPORT.md`, `profile/rms_largeS_r4/REPORT.md`.

## Support predicates (`src/register.py`)
- **LN → CUDA** iff: `fp32`, 2-D, contiguous, `is_rms_norm=False`, `(M,N) ∈ _SUPPORTED_LN`, and weight+bias non-None, contiguous, `shape==(N,)`, same device+dtype; `out` is None or `shape==x.shape` + same device/dtype + contiguous.
- **RMS → CUDA** iff: `bf16`, exactly 2-D, contiguous, `(S,D) ∈ _SUPPORTED_RMS` (i.e. `D==128` and `S ∈ {1320,4096,16384}` for production + regression-small), and `w` non-None, contiguous, `shape==(D,)`, same device+dtype.
- **Everything else → SGLang baseline fallback** (fp16/bf16 LN, `is_rms_norm=True`, N/S/D outside the table, non-contiguous, wrong device/dtype/shape, higher-rank, invalid `out`). Verified by `tests/test_correctness.py::test_fallback_routing` (15 cases).

## Per-shape decision

| Production shape | dtype | owner (kernel) | baseline µs | candidate µs | speedup (wall / kernel) | active bound | decision |
|---|---|---|---|---|---|---|---|
| helios `[8640,5120]` | fp32 LN | **CUDA** `LayerNormInferKernel<fp32_t>` (float4, parallel reduce) | 82.96 | 71.10 | **1.17× / 1.19×** | memory-bandwidth (~66% peak; `ac_e_r5/reports/ln.ncu-rep`) | **PROMOTE** |
| hunyuanvideo `[1320,128]` | bf16 RMS | **CUDA** `RmsNormOnepassKernel<128,1,bf16_t>` | 33.36 | 20.37 | **1.64× / 1.70×** | launch/occupancy (occ 15%; `ac_e_r5/reports/rms1320.ncu-rep`) | **PROMOTE** |
| zimage `[4096,128]` | bf16 RMS | **CUDA** `RmsNormOnepassKernel<128,1,bf16_t>` | 32.87 | 20.16 | **1.63× / 1.71×** | launch/occupancy (occ 40%; `ac_e_r5/reports/rms4096.ncu-rep`) | **PROMOTE** |
| zimage `[16384,128]` | bf16 RMS | **CUDA** `RmsNormOnepassKernel<128,1,bf16_t>` | 33.45 | 21.88 | **1.53× / 1.66×** | launch/occupancy (partial wave, occ 76%; `ac_e_r5/reports/rms16384.ncu-rep`) | **PROMOTE** |
| hunyuanvideo `[648720,128]` | bf16 RMS | **SGLang baseline (fallback)** | 77.00 | 78.24 (CUDA, not used) | ~1.0× (fallback) | memory-latency + occupancy | **NO-GO → fallback** |
| hunyuanvideo `[650040,128]` | bf16 RMS | **SGLang baseline (fallback)** | 76.72 | 78.47 (CUDA, not used) | ~1.0× (fallback) | memory-latency + occupancy | **NO-GO → fallback** |

## Large-RMS no-go package (AC-12)
- **Correctness:** the CUDA RMS kernel is correct at large S (validated rounds 0-3, and kUnroll variants in round 4).
- **Attempts:** one-warp-per-row (kUnroll=1) and the MLP grid-stride variant (kUnroll=2/4/8). Best (kUnroll=4) ~77 µs vs baseline ~71 µs (interleaved, idle B200).
- **Benchmark:** ~0.84-0.92× across runs; not parity-or-better at any tried config.
- **NCU/roofline:** `profile/rms_largeS_r4/REPORT.md` + `profile/ac_e_r5/` — not bandwidth-saturated (~4.3-4.7 TB/s, ~55-59% peak); kUnroll=1 is memory-latency bound (long-scoreboard 56%, occ 77%), kUnroll=4 trades occupancy (41%) for MLP. Neither warp-per-row variant matches the baseline's 16-row tile.
- **Named active bound:** memory-load latency vs occupancy trade-off intrinsic to the warp-per-row family for `D=128` huge-S streaming RMS.
- **Decision:** fall back to the SGLang Triton baseline (faster) → parity, no production regression. Re-open only if a tile-based CUDA RMS (multi-row-per-block, shared load pipeline) is implemented and beats the baseline.

## Summary
6/6 production shapes parity-or-better: **4 CUDA promotions** + **2 documented no-go fallbacks** (parity). Geomean 1.29× wall / 1.33× kernel reported as an outcome, not a pass/fail threshold (per the prompt).
