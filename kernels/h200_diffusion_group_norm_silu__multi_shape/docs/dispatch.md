# Dispatch decision table — h200_diffusion_group_norm_silu__multi_shape

Evidence: ion8-h200 GPU 7 (idle), `no_grad`, CUDA-event timing warmup25/iters100, triton
entry, vs the SGLang Triton baseline. `group_size = (channels/num_groups) * spatial`.
Geomean (final) = **1.4487x** over 48 production shapes (canonical `benchmark.csv`: full
baseline+candidate median/mean/std/min/p10/p90 + per-row `path`); correctness 110/110 (strict).

## Buckets

| Bucket | group_size | Path chosen | Representative (base_us -> cand_us, speedup) | Promote/Reject |
|---|---|---|---|---|
| small | `< 65536` | candidate SMALL (1 CTA/group) | `[1,512,2,12,10]` 38.8->21.6 (1.86x); `[1,512,5,32,10]` 39->24.7 (1.58x) | PROMOTE candidate |
| medium | `65536 .. 900000` | candidate LARGE (3-stage multi-CTA) | `[1,512,3,128,40]` 102->38 (2.68x); `[1,256,9,128,40]` 81->39 (2.07x); `[1,512,9,128,40]` 83->70 (1.28x) | PROMOTE candidate |
| giant | `>= 900000` | SGLang Triton baseline (fallback) | `[1,256,17,256,256]` baseline 426us; candidate large path 607-671us (0.63-0.70x) | REJECT candidate large path -> baseline |

## Crossover (why 900,000)
Sorting all 48 production shapes by group_size and candidate-vs-baseline speedup (v3 sweep,
`benchmark_v3.csv`) shows a clean, monotone transition with NO overlap:
- every shape with `group_size <= 884,736` had speedup >= 1.0 (candidate wins),
- every shape with `group_size >= 983,040` had speedup < 1.0 (candidate loses).
`_GIANT_THRESH = 900_000` sits in that gap. This is a shape-BUCKET boundary (BW-bound giants
vs overhead-bound small/medium), not per-shape overfitting.

## Why the candidate loses on giants (NCU, profile/v2_gns/REPORT.md)
On `[1,512,9,128,128]`: candidate large path sm__throughput 66.5%, dram__throughput 31.2%,
achieved occupancy 39.8%, 52 regs. It is COMPUTE/occupancy-bound, NOT BW-bound. The baseline
chunked path reaches ~4000 GB/s (~84% of the H200's ~4.8 TB/s peak; a plain `x*2` copy hits
~4200 GB/s), i.e. near the attainable bound for a two-read groupnorm. Tried v3 channel-hoist
(helped: 1.31x->1.38x) and v4 `__launch_bounds__(6)` (did not help: 1.374x, reverted). The
L2-residency / 2N-traffic lever was REFUTED (the candidate isn't BW-bound; the baseline is
already near-peak). Hence the giants are routed to the near-peak baseline = near-bound.

## Notes
- The 4 routed giants nearest the threshold measure 0.93-0.96x vs the raw baseline: a small
  Python dispatch tax (optimized_wrapper -> _can_use -> fallback) over calling the baseline
  directly, not a kernel regression. A thinner fast-path for the fallback would recover it.
- fp32 / bf16-out-of-support / non-contiguous / grad / non-affine etc. also fall back (correctness).
