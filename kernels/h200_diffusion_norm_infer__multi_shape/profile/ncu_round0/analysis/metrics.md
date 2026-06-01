# Parsed NCU metrics (round 1) — ion-h200-8, GPU 7, H200 SM90

Reports: `../reports/{rms_huge_full,ln_full}.ncu-rep` (`--set full`) and
`../reports/{rms_huge_source,ln_source}.ncu-rep` (`--set source --section SourceCounters`).
LN is the round-1 double-precision kernel; RMS kernel is unchanged.

```
rms_norm_bf16_n128  [650040,128]  grid=4224  block=256
  gpu__dram_throughput...pct                                75.73 %
  gpu__time_duration.sum                                    83.78 us
  sm__throughput...pct                                      43.53 %
  sm__warps_active...pct (occupancy)                        90.74 %
  launch__waves_per_multiprocessor                           4.00
  [source] l1tex global ld / st sectors          5,470,656 / 5,200,320
  [source] global ld / st instructions             358,812 / 325,020
  -> active bound: DRAM bandwidth (~3.6 TB/s). ld/st sectors match the x-read +
     y-write byte traffic (coalesced, no wasted sectors). Near attainable.

rms_norm_bf16_n128  [1320,128]    grid=83    block=256
  gpu__dram_throughput...pct                                 2.02 %
  gpu__time_duration.sum                                     3.52 us
  sm__warps_active...pct                                    11.89 %
  launch__waves_per_multiprocessor                           0.08
  [source] l1tex global ld / st sectors              15,840 / 10,560
  -> active bound: launch/occupancy (<<1 wave). Bandwidth optimization cannot help.

layer_norm_fp32 (double-internal)  [8640,5120]  grid=8640  block=256
  gpu__dram_throughput...pct                                62.67 %
  gpu__time_duration.sum                                   107.71 us
  sm__throughput...pct                                      56.69 %
  sm__warps_active...pct (occupancy)                        34.83 %
  launch__waves_per_multiprocessor                          21.82
  [source] l1tex global ld / st sectors         16,588,800 / 5,529,600
  [source] global ld / st instructions           1,036,800 / 345,600
  -> active bound: MIXED. The double-precision mean/variance/normalize raised SM
     throughput to ~57% and lowered occupancy to ~35%, so the kernel is no longer
     purely bandwidth-bound (DRAM 62.7%, ~3.3 TB/s). ld sectors = x + w + b L1 reads
     (w/b re-read per row but L2-resident); st sectors = y write only.
```

## Round 0 vs Round 1 (LN)

| LN variant | DRAM %peak | SM %peak | occ | kernel us | adversarial 1e-5 | speedup |
|---|---|---|---|---|---|---|
| round 0 fp32-fast | 78.2% | 24.3% | 46.9% | 85.6 | FAIL (err ~1e-4) | 1.119x |
| round 1 double-internal | 62.7% | 56.7% | 34.8% | 107.7 | PASS (err < 1e-5) | 1.011x |

The double-precision math is required to meet the immutable strict 1e-5 ceiling on
ill-conditioned (near-constant / tiny-variance) rows; it costs ~26% kernel time and
makes LN compute-influenced rather than purely memory-bound. LN remains
non-regressing (1.011x). Recovering LN throughput (occupancy / mixed-precision
reductions that still pass 1e-5) is a queued follow-up.

## Conclusion

RMS huge-M is DRAM-bound at ~75% peak (near attainable); RMS tiny-M is launch-bound;
LN (double) is mixed memory/compute at 62.7% DRAM / 56.7% SM, slower but now correct
on adversarial rows. All six shapes non-regressing. See ../REPORT.md.
