# Results — h200_diffusion_cutedsl_norm_scale_shift__multi_shape

## Conclusion

PROMOTE. The native sm_90a candidate beats the vendored upstream CuTeDSL baseline with an
equal-weight geometric-mean speedup of **1.2708x (session A2) / 1.2747x (session B2)** over the
39 frozen production workloads, reproduced in two independent sessions agreeing within **0.31%**
(honest-lower headline: **1.27x**). Per-row floor policy satisfied: every production row is
>= 0.98x in both sessions except (a) the two DEC-routed wan fp32-row rows at 0.976-0.991 carrying
the documented named bound (NCU-evidenced; see `docs/dispatch.md`), and (b) one one-session
measurement transient (below). 161 correctness checks pass (production 40/40 including routing
bookkeeping, canonical grid 110/110, negative probes 11/11); the vendored snapshot is bitwise-
identical to real SGLang at the pinned commit (two-process parity 10/10).

## Provenance

- Task: `kernels/h200_diffusion_cutedsl_norm_scale_shift__multi_shape`, target NVIDIA H200.
- Baseline: vendored SGLang `main` @ `133254086bf1f5b887c8c99d311719102d58a7eb`
  (`docs/baseline_source.md`; resolution 2026-06-04T15:00:08Z).
- Candidate source hash: `dbdb0d9759c5` (sha1-12 of `solution/csrc/norm_scale_shift.cuh`,
  verified identical local/remote).
- Environment: ion8-h200 (`ion-h200-8`), container `sglang_bbuf`, torch 2.11.0+cu130, CUDA
  13.0 (nvcc 13.0.r13.0), cutlass-dsl 4.5.0, tvm-ffi; build flags `-std=c++20 -O3
  --expt-relaxed-constexpr -DSGL_CUDA_ARCH=900` (snapshot `load_jit` defaults; no fast-math,
  both sides symmetric).
- Final evidence GPU: `REMOTE_GPU_ID=2` (NVIDIA H200, idle-verified 0% / 0 MiB / no compute
  apps before, between, and after both sessions; `logs/final_chain_gpu2.log`). An earlier
  same-config two-session chain on GPU 0 was DISCARDED after a foreign job landed mid-run
  (`docs/run_log.md`).
- Exact commands (workspace `/home/sglang-omni/bbuf/kda/k16_h200_nss/task`):
  - `CUDA_VISIBLE_DEVICES=2 python3 bench/benchmark.py --device cuda:0 --seed 1234 --out logs/results_final_a2.jsonl`
  - `CUDA_VISIBLE_DEVICES=2 python3 bench/benchmark.py --device cuda:0 --seed 5678 --out logs/results_final_b2.jsonl`
  - Correctness: `CUDA_VISIBLE_DEVICES=0 python3 bench/correctness.py --mode {production,grid,probes} --device cuda:0`
  - Methodology fixed by `bench/benchmark.py` (verbatim template copy): isolated subprocess per
    workload, 7 trials, warmup 10, inner-loop calibration to ~1000us (cap 4096), fresh seeded
    inputs per trial, deterministic interleaved A/B, CUDA events primary + wall-clock secondary,
    per-side median/mean/std/min/p10/p90 + raw samples in the JSONL artifacts.

## Headline

| Session | Geomean (39 production rows) | Arith mean | Min | Max | Passed |
|---|---|---|---|---|---|
| A2 (seed 1234) | **1.2708** | 1.3119 | 0.7841* | 2.0074 | 49/49 |
| B2 (seed 5678) | **1.2747** | 1.3113 | 0.9859 | 1.8742 | 49/49 |

Cross-session window 0.31%. The earlier v1 anchor session (GPU 0, pre-routing) measured 1.2887
with the two unrouted fp32-row rows at 0.948/0.951.

*A2 minimum is a one-session transient on `nss-b1-s18144-d3072-bf16-s1SD.fp32`: B2 measured
1.0084, the v1 anchor 1.0092, and a targeted idle-GPU recheck (`--seed 9012 --only <row>`,
`logs/results_outlier_recheck.jsonl`) measured 1.0071 with candidate samples 158.9-159.4us.
The A2 geomean above retains the transient as recorded (no number replaced).

## Per-row comparison (A2 / B2 speedups, A2 medians in us)

| Workload | Base us | Cand us | A2 | B2 |
|---|---|---|---|---|
| nss s19 d3072 1D.bf16 | 51.88 | 28.04 | 1.8501 | 1.8198 |
| nss s47 d3072 1D.bf16 | 50.97 | 27.68 | 1.8413 | 1.8267 |
| nss s55 d3072 1D.bf16 | 49.59 | 27.08 | 1.8314 | 1.8087 |
| nss s101 d1536 11D.bf16 | 41.90 | 27.77 | 1.5085 | 1.5000 |
| nss s189 d3072 1D.bf16 | 51.45 | 27.78 | 1.8520 | 1.8742 |
| nss s195 d3072 1D.bf16 | 59.14 | 29.46 | 2.0074 | 1.8511 |
| nss s997 d4096 1D.bf16 | 50.81 | 27.84 | 1.8254 | 1.8296 |
| nss s1004 d4096 1D.bf16 | 58.69 | 30.15 | 1.9463 | 1.8534 |
| nss s4096 d3072 11D.bf16 | 44.07 | 27.47 | 1.6043 | 1.5154 |
| nss s7904 d4096 1D.bf16 | 53.28 | 44.43 | 1.1993 | 1.1944 |
| nss s8424 d3072 11D.bf16 | 46.87 | 36.17 | 1.2960 | 1.2785 |
| nss s8640 d5120 1SD.bf16 | 92.33 | 89.14 | 1.0357 | 1.0361 |
| nss s11040 d5120 1SD.fp32 | 163.78 | 162.96 | 1.0050 | 1.0058 |
| nss s18144 d3072 1SD.bf16 | 110.10 | 108.06 | 1.0189 | 1.0203 |
| nss s18144 d3072 1SD.fp32 | 161.34 | 205.76* | 0.7841* | 1.0084 |
| nss s27030 d3072 1D.bf16 | 118.00 | 106.25 | 1.1106 | 1.1199 |
| nss s27085 d3072 1D.bf16 | 118.77 | 106.32 | 1.1171 | 1.1100 |
| nss s37044 d5120 11D.fp32 [routed] | 284.89 | 287.49 | 0.9910 | 0.9859 |
| nss s37800 d5120 11D.fp32 [routed] | 286.49 | 293.62 | 0.9757 | 0.9885 |
| nss s44100 d5120 11D.bf16 | 336.36 | 306.12 | 1.0988 | 1.1000 |
| nss s74088 d5120 11D.bf16 | 577.84 | 523.63 | 1.1035 | 1.0970 |
| nss s75600 d5120 11D.bf16 | 580.16 | 526.51 | 1.1019 | 1.1122 |
| nss s176400 d5120 11D.bf16 | 1369.50 | 1221.47 | 1.1212 | 1.1237 |
| srnss s19 d3072 g11D 1D.bf16 | 58.93 | 38.03 | 1.5496 | 1.5881 |
| srnss s47 d3072 g11D 1D.bf16 | 59.57 | 39.86 | 1.4944 | 1.5831 |
| srnss s55 d3072 g1D 1D.bf16 | 62.61 | 38.74 | 1.6161 | 1.6935 |
| srnss s101 d1536 gnone 11D.bf16 | 51.86 | 35.72 | 1.4518 | 1.3410 |
| srnss s189 d3072 g11D 1D.bf16 | 59.93 | 37.84 | 1.5836 | 1.6138 |
| srnss s195 d3072 g11D 1D.bf16 | 60.20 | 37.93 | 1.5871 | 1.6008 |
| srnss s4096 d3072 g11D 11D.bf16 | 50.37 | 37.70 | 1.3359 | 1.3391 |
| srnss s8424 d3072 g11D 11D.bf16 | 56.71 | 54.60 | 1.0386 | 1.0373 |
| srnss s18144 d3072 g1SD.fp32 wD.fp32 s1.bf16 | 163.76 | 163.03 | 1.0045 | 1.0036 |
| srnss s18144 d3072 gnone 1SD.fp32 | 211.40 | 209.67 | 1.0083 | 1.0061 |
| srnss s27030 d3072 g1D 1D.bf16 | 177.12 | 168.19 | 1.0531 | 1.0494 |
| srnss s37044 d5120 g11D.fp32 wD.fp32 s1.bf16 | 449.95 | 398.46 | 1.1292 | 1.1256 |
| srnss s37044 d5120 gnone 11D.fp32 | 385.70 | 388.72 | 0.9922 | 0.9935 |
| srnss s37800 d5120 g11D.fp32 wD.fp32 s1.bf16 | 458.41 | 412.58 | 1.1111 | 1.1197 |
| srnss s37800 d5120 gnone 11D.fp32 | 389.39 | 396.30 | 0.9826 | 0.9898 |
| srnss s44100 d5120 gnone 11D.bf16 | 448.59 | 448.39 | 1.0004 | 0.9979 |

Full statistics (median/mean/std/min/p10/p90 + raw samples per side per row, both sessions) live
in `logs/results_final_a2.jsonl` / `logs/results_final_b2.jsonl` (workspace evidence; the
small per-row summary above is the committed record). The non-headline regression-grid rows
(production=false) all passed in both sessions.

## Bound analysis (roofline-style, per bucket class)

- **Small/short rows (S=19..4096, also 1D-scale mid rows): host-dispatch floor.** Device kernels
  are 3-10us; the measured 27-30us (nss) / 36-40us (srnss) candidate medians are the per-call
  wrapper-inclusive floor. The 1.34-2.01x wins come from replacing the baseline's per-call Python
  (validation, `broadcast_tensor_for_bsfd` rearrange/expand, compile-cache key construction over
  every tensor) with a thin stride classifier. CAVEAT (required): these are wrapper-inclusive
  eager-call throughput numbers — CUDA-event windows over amplified inner loops include the
  stream idle gaps caused by host enqueue latency, and wall-clock medians agree within ~2%
  (e.g., s195 nss: 59.7us wall baseline vs 29.7us wall candidate). They are NOT isolated device-
  kernel durations and may shrink under CUDA-graph replay or if a future baseline hoists its
  host work.
- **Mid/huge bf16 row-broadcast rows (S=27030..176400): mixed issue/DRAM.** e.g. nss s176400
  d5120: 3.61 GB moved in 1221us = 2.96 TB/s ~= 62% of the 4.8 TB/s peak; the 1.10-1.12x comes
  from leaner per-element issue (fp32-register pipeline, no per-pass reconversion), not extra
  bandwidth headroom.
- **srnss huge bf16 (s44100): DRAM-bound parity.** 2x activation traffic (residual read +
  res_out write): 1.81 GB in 448us = 4.03 TB/s ~= 84% of peak on both sides — at the bound;
  1.00x is the honest outcome.
- **Per-token (1SD) rows: at the operand-stream bound.** bf16 variants win 1.02-1.04; fp32
  variants are parity (1.00-1.01) with the heaviest streams; consistent with the bound.
- **Routed wan fp32-row rows: named bound.** Native kernel 0.948-0.951 from exposed operand-load
  latency (NCU r1: short_scoreboard 6.49 vs 2.69 at identical geometry/regs/bytes); both
  occupancy-neutral fixes measured worse (prefetch storm 620us; early-load register cliff
  489us vs 381us). Routed to the baseline kernel; residual 0.976-0.991 is the nested custom-op
  dispatch hop (~5-8us host on ~290us calls). Accepted under the per-row policy with this named
  bound; see `docs/dispatch.md`.
- **wan affine srnss rows: 1.11-1.13 native win** from fusing the fp32 weight/bias affine into
  the single pass.

## Correctness summary

- Production rows: 40/40 (39 signatures + routing bookkeeping: zero unexpected fallbacks; the
  declared routed bucket counted separately) — `logs/correctness_final.json`.
- Canonical regression grid (contract SHAPES x dtypes x norm types x affine modes x 9 layouts,
  BF1D divisibility rejection): 110/110 — `logs/correctness_grid.json`.
- Negative probes (wrong-formula detectability, argument order, NaN propagation, empty rows,
  CPU/cross-device, non-tensor, non-contiguous, misaligned, BF1D rejection, fallback counters,
  high-mean/low-variance stress): 11/11 — `logs/correctness_probes_final.json`.
- Oracle: upstream-canonical fp32 reference; static tolerances 5e-2 (non-fp32) / 1e-5 (fp32);
  dynamic bound candidate_err <= 2x baseline_err + 1e-6 on every checked output.
- Snapshot parity vs real SGLang @ pinned commit: 10/10 bitwise (`bench/parity_check.py`).
