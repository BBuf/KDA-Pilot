# Results — h200_diffusion_cutedsl_norm_scale_shift__multi_shape

## Conclusion

PROMOTE. The native sm_90a candidate beats the vendored upstream CuTeDSL baseline with an
equal-weight geometric-mean speedup of **1.2795x (session A3) / 1.2763x (session B3)** over the
39 frozen production workloads, reproduced within **0.25%** across the two final sessions and
consistent with two earlier clean sessions on a different idle GPU (A2 1.2708 / B2 1.2747 on
GPU 2) — honest-lower headline across all four clean sessions: **1.27x**. Per-row floor policy
satisfied: every production row >= 0.98x in both final sessions except the two DEC-routed wan
fp32-row rows (0.9757-0.9897) carrying the documented named bound (`docs/dispatch.md`).
Harness symmetry validated by a baseline-vs-baseline run (geomean **0.9992**). 162 correctness
checks pass (production 40/40 incl. routing bookkeeping, canonical grid 110/110, negative probes
12/12 incl. checker-based NaN and Inf injection); the vendored snapshot is bitwise-identical to
real SGLang at the pinned commit (two-process parity 10/10).

## Provenance

- Task: `kernels/h200_diffusion_cutedsl_norm_scale_shift__multi_shape`, target NVIDIA H200.
- Baseline: vendored SGLang `main` @ `133254086bf1f5b887c8c99d311719102d58a7eb`
  (`docs/baseline_source.md`; resolution 2026-06-04T15:00:08Z).
- Candidate source hash: `dbdb0d9759c5` (sha1-12 of `solution/csrc/norm_scale_shift.cuh`).
- Environment: ion8-h200 (`ion-h200-8`), container `sglang_bbuf`, torch 2.11.0+cu130, CUDA 13.0
  (nvcc 13.0.r13.0), cutlass-dsl 4.5.0, tvm-ffi; build flags `-std=c++20 -O3
  --expt-relaxed-constexpr -DSGL_CUDA_ARCH=900` (snapshot `load_jit` defaults; no fast-math,
  both sides symmetric).
- Final evidence GPU: physical index 3, UUID `GPU-6b4aba65-49ad-a9b2-0fa8-d2dbcb96a34b`
  (NVIDIA H200), pinned via `CUDA_VISIBLE_DEVICES=3`. Machine-readable identity and idle
  evidence (GPU inventory + per-UUID compute-app snapshots before/after, hostname, device
  mapping, source hashes, run seed, per-trial seeds and A/B orders) are embedded in every
  results JSONL by the task-local provenance extensions (`docs/benchmark_method.md`). The A3
  pre-run compute-app snapshot is clean; the only GPU-3 processes ever observed in the
  before/after snapshots are the chain's own just-exited sequential workers (monotonic task
  PIDs, 0% utilization at every snapshot, each gone by the next step) — no foreign workload.
- History: two earlier clean sessions on GPU 2 (A2/B2, same config, pre-extension provenance)
  agree within 0.7% of A3/B3; a GPU-0 session pair was DISCARDED after a foreign 112 GiB job
  landed mid-run (`docs/run_log.md`).
- Exact commands (workspace `/home/sglang-omni/bbuf/kda/k16_h200_nss/task`):
  - `CUDA_VISIBLE_DEVICES=3 python3 bench/benchmark.py --device cuda:0 --seed 4242 --candidate-impl baseline --out logs/results_bvb.jsonl`
  - `CUDA_VISIBLE_DEVICES=3 python3 bench/benchmark.py --device cuda:0 --seed 1234 --out logs/results_final_a3.jsonl`
  - `CUDA_VISIBLE_DEVICES=3 python3 bench/benchmark.py --device cuda:0 --seed 5678 --out logs/results_final_b3.jsonl`
  - Correctness: `CUDA_VISIBLE_DEVICES=<idle-gpu> python3 bench/correctness.py --mode {production,grid,probes} --device cuda:0`
  - Methodology fixed by `bench/benchmark.py` (template timing policy untouched; task-local
    provenance extensions documented in `docs/benchmark_method.md`): isolated subprocess per
    workload, 7 trials, warmup 10, inner-loop calibration to ~1000us (cap 4096), fresh seeded
    inputs per trial, deterministic interleaved A/B, CUDA events primary + wall-clock secondary,
    per-side median/mean/std/min/p10/p90 + raw samples in the JSONL artifacts.

## Headline

| Session | Mode | Geomean (39 production rows) | Min | Max | Passed |
|---|---|---|---|---|---|
| BVB (seed 4242) | baseline-vs-baseline sanity | **0.9992** | 0.9655 | 1.0267 | 49/49 |
| A3 (seed 1234) | candidate | **1.2795** | 0.9757 | 2.0936 | 49/49 |
| B3 (seed 5678) | candidate | **1.2763** | 0.9814 | 1.8690 | 49/49 |
| A2 / B2 (GPU 2, earlier clean sessions) | candidate | 1.2708 / 1.2747 | — | — | 49/49 each |

Cross-session window A3/B3: 0.25%; across all four clean sessions: 0.7%. The earlier v1 anchor
session (GPU 0, pre-routing) measured 1.2887 with the two unrouted fp32-row rows at 0.948/0.951.
A one-session transient seen in A2 on `nss s18144 fp32 1SD` (0.784; targeted idle recheck 1.0071)
did not recur: that row reads 1.0075 / 1.0085 in A3/B3.

## Per-row comparison (A3 medians in us; A3 / B3 speedups)

| Workload | Base us | Cand us | A3 | B3 |
|---|---|---|---|---|
| nss s1004 d4096 s1D.bf16-s1D.bf16 | 50.95 | 27.20 | 1.8730 | 1.8315 |
| nss s101 d1536 s11D.bf16-s11D.bf16 | 41.75 | 27.52 | 1.5168 | 1.5439 |
| nss s11040 d5120 s1SD.fp32-s1SD.fp32 | 163.63 | 162.47 | 1.0072 | 1.0063 |
| nss s176400 d5120 s11D.bf16-s11D.bf16 | 1374.66 | 1220.67 | 1.1261 | 1.0963 |
| nss s18144 d3072 s1SD.bf16-s1SD.bf16 | 110.08 | 108.16 | 1.0177 | 1.0201 |
| nss s18144 d3072 s1SD.fp32-s1SD.fp32 | 160.22 | 159.02 | 1.0075 | 1.0085 |
| nss s189 d3072 s1D.bf16-s1D.bf16 | 51.32 | 28.10 | 1.8262 | 1.7883 |
| nss s19 d3072 s1D.bf16-s1D.bf16 | 51.49 | 27.89 | 1.8462 | 1.8513 |
| nss s195 d3072 s1D.bf16-s1D.bf16 | 50.83 | 27.82 | 1.8269 | 1.8476 |
| nss s27030 d3072 s1D.bf16-s1D.bf16 | 118.33 | 106.07 | 1.1156 | 1.1093 |
| nss s27085 d3072 s1D.bf16-s1D.bf16 | 118.36 | 106.35 | 1.1130 | 1.1065 |
| nss s37044 d5120 s11D.fp32-s11D.fp32 [routed] | 283.62 | 286.56 | 0.9897 | 0.9886 |
| nss s37800 d5120 s11D.fp32-s11D.fp32 [routed] | 286.30 | 293.44 | 0.9757 | 0.9814 |
| nss s4096 d3072 s11D.bf16-s11D.bf16 | 43.43 | 27.13 | 1.6011 | 1.5257 |
| nss s44100 d5120 s11D.bf16-s11D.bf16 | 335.95 | 305.86 | 1.0984 | 1.1036 |
| nss s47 d3072 s1D.bf16-s1D.bf16 | 51.18 | 27.88 | 1.8357 | 1.8480 |
| nss s55 d3072 s1D.bf16-s1D.bf16 | 51.30 | 27.92 | 1.8372 | 1.8344 |
| nss s74088 d5120 s11D.bf16-s11D.bf16 | 565.58 | 516.26 | 1.0955 | 1.0947 |
| nss s75600 d5120 s11D.bf16-s11D.bf16 | 583.14 | 523.42 | 1.1141 | 1.1171 |
| nss s7904 d4096 s1D.bf16-s1D.bf16 | 53.73 | 44.48 | 1.2080 | 1.1923 |
| nss s8424 d3072 s11D.bf16-s11D.bf16 | 46.33 | 36.61 | 1.2653 | 1.2492 |
| nss s8640 d5120 s1SD.bf16-s1SD.bf16 | 92.40 | 89.43 | 1.0332 | 1.0355 |
| nss s997 d4096 s1D.bf16-s1D.bf16 | 57.73 | 27.57 | 2.0936 | 1.8690 |
| srnss s101 d1536 gnone-s11D.bf16-s11D.bf16 | 46.70 | 35.00 | 1.3341 | 1.3344 |
| srnss s18144 d3072 g1SD.fp32-wD.fp32-s1.bf16-s1.bf16 | 163.44 | 163.22 | 1.0013 | 1.0041 |
| srnss s18144 d3072 gnone-s1SD.fp32-s1SD.fp32 | 211.10 | 209.67 | 1.0068 | 1.0044 |
| srnss s189 d3072 g11D.bf16-s1D.bf16-s1D.bf16 | 60.67 | 37.19 | 1.6316 | 1.6154 |
| srnss s19 d3072 g11D.bf16-s1D.bf16-s1D.bf16 | 59.01 | 37.02 | 1.5939 | 1.5727 |
| srnss s195 d3072 g11D.bf16-s1D.bf16-s1D.bf16 | 60.03 | 37.72 | 1.5915 | 1.5929 |
| srnss s27030 d3072 g1D.bf16-s1D.bf16-s1D.bf16 | 176.12 | 168.02 | 1.0483 | 1.1093 |
| srnss s37044 d5120 g11D.fp32-wD.fp32-s1.bf16-s1.bf16 | 446.33 | 396.35 | 1.1261 | 1.1271 |
| srnss s37044 d5120 gnone-s11D.fp32-s11D.fp32 | 384.11 | 386.82 | 0.9930 | 0.9962 |
| srnss s37800 d5120 g11D.fp32-wD.fp32-s1.bf16-s1.bf16 | 454.56 | 405.96 | 1.1197 | 1.1196 |
| srnss s37800 d5120 gnone-s11D.fp32-s11D.fp32 | 389.84 | 396.22 | 0.9839 | 0.9903 |
| srnss s4096 d3072 g11D.bf16-s11D.bf16-s11D.bf16 | 49.89 | 37.70 | 1.3235 | 1.3382 |
| srnss s44100 d5120 gnone-s11D.bf16-s11D.bf16 | 448.65 | 448.09 | 1.0012 | 1.0003 |
| srnss s47 d3072 g11D.bf16-s1D.bf16-s1D.bf16 | 58.18 | 37.35 | 1.5579 | 1.5781 |
| srnss s55 d3072 g1D.bf16-s1D.bf16-s1D.bf16 | 62.22 | 37.33 | 1.6668 | 1.7505 |
| srnss s8424 d3072 g11D.bf16-s11D.bf16-s11D.bf16 | 56.56 | 54.67 | 1.0345 | 1.0364 |

Full statistics (median/mean/std/min/p10/p90 + raw samples per side per row, plus per-row
trial seeds, A/B orders, selected-GPU identity) live in `logs/results_final_a3.jsonl` /
`logs/results_final_b3.jsonl` / `logs/results_bvb.jsonl` (workspace evidence; the per-row
summary above is the committed record). The non-headline regression-grid rows
(production=false) all passed in every session.

## Bound analysis (roofline-style, per bucket class)

- **Small/short rows (S=19..4096, also 1D-scale mid rows): host-dispatch floor.** Device kernels
  are 3-10us; the measured 27-38us candidate medians are the per-call wrapper-inclusive floor.
  The 1.32-2.09x wins come from replacing the baseline's per-call Python (validation,
  `broadcast_tensor_for_bsfd` rearrange/expand, compile-cache key construction over every
  tensor) with a thin stride classifier. CAVEAT (required): these are wrapper-inclusive
  eager-call throughput numbers — CUDA-event windows over amplified inner loops include the
  stream idle gaps caused by host enqueue latency, and wall-clock medians agree within ~2%.
  They are NOT isolated device-kernel durations and may shrink under CUDA-graph replay or if a
  future baseline hoists its host work.
- **Mid/huge bf16 row-broadcast rows (S=27030..176400): mixed issue/DRAM.** e.g. nss s176400
  d5120: 3.61 GB moved in 1221us = 2.96 TB/s ~= 62% of the 4.8 TB/s peak; the 1.10-1.13x comes
  from leaner per-element issue (fp32-register pipeline, no per-pass reconversion), not extra
  bandwidth headroom.
- **srnss huge bf16 (s44100): DRAM-bound parity.** 2x activation traffic (residual read +
  res_out write): 1.81 GB in 448us = 4.03 TB/s ~= 84% of peak on both sides — at the bound;
  1.00x is the honest outcome.
- **Per-token (1SD) rows: at the operand-stream bound.** bf16 variants win 1.02-1.04; fp32
  variants are parity (1.00-1.01) with the heaviest streams; consistent with the bound.
- **Routed wan fp32-row rows: named bound.** Native kernel measured 0.948-0.951 from exposed
  operand-load latency (NCU r1: short_scoreboard 6.49 vs 2.69 at identical geometry/regs/bytes);
  both occupancy-neutral fixes measured worse (prefetch storm 620us; early-load register cliff
  489us vs 381us). Routed to the baseline kernel; residual 0.976-0.990 is the nested custom-op
  dispatch hop (~5-8us host on ~290us calls). Accepted under the per-row policy with this named
  bound; see `docs/dispatch.md`.
- **wan affine srnss rows: 1.12-1.13 native win** from fusing the fp32 weight/bias affine into
  the single pass.

## Correctness summary

- Production rows: 40/40 (39 signatures + routing bookkeeping: zero unexpected fallbacks; the
  declared routed bucket's call count asserted, routed_calls=2) — `logs/correctness_final.json`,
  `logs/correctness_postaudit.json`.
- Canonical regression grid (contract SHAPES x dtypes x norm types x affine modes x 9 layouts,
  BF1D divisibility rejection): 110/110 — `logs/correctness_grid.json`.
- Negative probes: 12/12 — `logs/correctness_probes_r1.json` — wrong-formula detectability,
  argument order, checker-based NaN injection, checker-based Inf injection (both must be flagged
  by the comparison checker, not merely propagate), empty rows, CPU/cross-device, non-tensor,
  non-contiguous, misaligned, BF1D rejection, fallback counters, high-mean/low-variance stress.
- Oracle: upstream-canonical fp32 reference; static tolerances 5e-2 (non-fp32) / 1e-5 (fp32);
  dynamic bound candidate_err <= 2x baseline_err + 1e-6 on every checked output.
- Harness symmetry: baseline-vs-baseline geomean 0.9992 (min 0.9655 / max 1.0267 over the 39
  production rows) — `logs/results_bvb.jsonl`.
- Snapshot parity vs real SGLang @ pinned commit: 10/10 bitwise (`bench/parity_check.py`).
