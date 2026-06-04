# Dispatch — h200_diffusion_cutedsl_norm_scale_shift__multi_shape

The candidate exposes the two public entry points as `kda_nss::` custom ops and routes each call
by operand classification (`solution/binding.py::_classify_operand`): activation must be bf16
`[1, S, D]` contiguous/aligned with `D % 256 == 0`, `D <= 8192`; scale/shift/gate classify as
`scalar [1]`, `row` (`[D]`/`[1,D]`/`[1,1,D]` views), or `token` (`[1,S,D]`); weight/bias must be
fp32 `[D]` when present. Anything else — fp16/fp32 activations, rms norm, B>1 activations (the
contract check requires `x.shape[0] == 1`; only captured-production batch geometry is verified
native), 4-D BF1D frames, CPU/cross-device operands, misaligned or non-contiguous storage, zero
rows, affine `fused_norm_scale_shift`, unknown combos — falls closed to the vendored CuTeDSL
baseline (`fallback` dispatch counters). Shipped kernel config: 16-byte per-thread vectors (one 128-bit
transaction), two-pass layer variance, no PDL, no fast-math.

Latency/speedup columns: final sessions A2/B2 medians on idle H200 GPU 2
(`logs/results_final_a2.jsonl` / `_b2.jsonl`), candidate-vs-baseline per-workload speedup.

## Native buckets

| Bucket (combo key) | Route | Production rows | Speedup A2 / B2 | Reason |
|---|---|---|---|---|
| nss, row-class bf16 scale/shift | `nss_row_bf16_v16` | qwen S=19/47, qwen-edit/firered-1.1 S=189/195, hunyuanvideo S=55/27030/27085, joyai S=997/1004/7904 (D=4096) | 1.11-2.01 (small-S rows 1.83-2.01, mid 1.11-1.20) | host-dispatch floor dominates small S (see results.md caveat); mid rows win on issue efficiency |
| nss, row-class bf16, 11D views | same bucket | qwen S=4096, firered S=8424, mova S=101/44100/176400, wan bf16 S=74088/75600 | 1.04-1.60 | same bucket; huge rows 1.10-1.12 near the DRAM knee |
| nss, token-class bf16 (`[1,S,D]`) | `nss_token_bf16_v16` | helios S=8640, wan-ti2v S=18144 | 1.02-1.04 | per-token streams near bound |
| nss, token-class fp32 | `nss_token_fp32_v16` | helios S=11040, wan-ti2v S=18144 | 1.00-1.01 | heaviest operand streams at the bound (parity; A2's 0.784 on wan-ti2v fp32 was a one-session transient — targeted recheck 1.0071, samples 158.9-159.4us) |
| srnss, gated row bf16 | `srnss_grow_bf16_row_bf16_v16` | qwen/qwen-edit/firered-1.1 S=19..8424, hunyuanvideo S=55/27030, qwen S=4096 | 1.04-1.69 | small-S host floor + mid-row issue wins |
| srnss, gate-free row bf16 | `srnss_gnone_row_bf16_v16` | mova S=101/44100 | 1.00 (S=44100), 1.34-1.45 (S=101) | S=44100 carries 2x activation traffic at 84% of DRAM peak -> bound-parity |
| srnss, gate-free row/token fp32 | `srnss_gnone_{row,token}_fp32_v16` | wan-i2v/t2v S=37044/37800, wan-ti2v S=18144 | 0.98-1.01 | residual variants at the DRAM bound; within noise of parity |
| srnss, fp32 affine + fp32 gate, scalar bf16 scale/shift | `srnss_g{row,token}_fp32_wb_scalar_bf16_v16` | wan-i2v/t2v S=37044/37800, wan-ti2v S=18144 | 1.00-1.13 | fused affine saves a separate weight/bias pass |

## Routed bucket (per the task's per-row regression policy)

| Bucket | Route | Production rows | Speedup A2 / B2 | Named bound |
|---|---|---|---|---|
| nss, row-class **fp32** scale/shift | vendored baseline (`routed` counter, not `fallback`) | wan-t2v S=37800, wan-i2v S=37044 (D=5120) | 0.976/0.989 and 0.991/0.986 | Native kernel measured 0.948-0.951: NCU r1 shows identical geometry/regs/bytes vs the CuTeDSL kernel but exposed operand-load latency (short_scoreboard 6.49 vs 2.69/issue). Two occupancy-neutral fixes measured and rejected: `prefetch.global.L1` pre-stats (LSU flood from per-thread prefetches of shared row operands: 620us vs 381us) and early raw register loads (40 regs -> 2 CTAs/SM: 489us). Routing restores the baseline kernel; the residual 1-2.5% is the nested custom-op dispatch hop (~5-8us host per call on ~290us kernels), accepted as the named bound for these two rows. |

## Measured-and-rejected config levers (kept compiled-in, env-selectable for reproduction)

- `KDA_VEC_BYTES_BF16=32` (two 128-bit transactions/thread, half block size): full-sweep geomean
  1.2475 vs 1.2887; srnss bf16 rows -28% (`logs/results_sweep_v32.jsonl`). H200 prefers 16B —
  inverts the B200 result for this family.
- `KDA_EARLY_OPS=1` (early raw scale/shift loads): fixes the stall signature
  (short_scoreboard 6.49 -> 4.3) but costs 32 -> 40 regs and the 3->2 CTAs/SM occupancy cliff
  at 640-thread blocks (`profile/r1-nss-fp32row-s37800/reports/candidate_r3eo.ncu-rep`).
- PTX `prefetch.global.L1` pre-stats: removed from source after measurement
  (`candidate_r2pf.ncu-rep`); see git history.
- Single-round Welford statistics (`kTwoPassVariance=false` instantiation path): retained from
  the B200 prior art as a documented lever; not re-measured on H200 because no bucket is
  reduction-bound (the binding does not emit these variants).
