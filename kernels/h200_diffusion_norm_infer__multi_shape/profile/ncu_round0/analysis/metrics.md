# Parsed NCU metrics (round 0) — ion-h200-8, GPU 7, H200 SM90

Raw reports: `../reports/{rms_huge_full,ln_full}.ncu-rep` (`--set full`).

```
rms_norm_bf16_n128  [650040,128]  grid=4224  block=256
  gpu__dram_throughput.avg.pct_of_peak_sustained_elapsed   75.46 %
  gpu__time_duration.sum                                   83.81 us
  sm__throughput.avg.pct_of_peak_sustained_elapsed         43.07 %
  sm__warps_active.avg.pct_of_peak_sustained_active        90.84 %
  launch__waves_per_multiprocessor                          4.00
  -> active bound: DRAM bandwidth (~3.6 TB/s; near attainable HBM bound)

rms_norm_bf16_n128  [1320,128]    grid=83    block=256
  gpu__dram_throughput...pct                                2.16 %
  gpu__time_duration.sum                                    3.26 us
  sm__throughput...pct                                      3.37 %
  sm__warps_active...pct                                   12.16 %
  launch__waves_per_multiprocessor                          0.08
  -> active bound: launch/occupancy (<<1 wave); bandwidth optimization cannot help

layer_norm_fp32     [8640,5120]   grid=8640  block=256
  gpu__dram_throughput...pct                               78.23 %
  gpu__time_duration.sum                                   85.63 us
  sm__throughput...pct                                     24.31 %
  sm__warps_active...pct                                   46.88 %
  launch__waves_per_multiprocessor                         16.36
  -> active bound: DRAM bandwidth (~3.75 TB/s; near attainable HBM bound)
```

Conclusion: bandwidth-bound buckets (huge-M RMS, fp32 LN) sit at ~75-78% of peak
HBM with NCU-named memory bound; tiny-M RMS is launch-bound (0.08 waves) yet still
2.5x faster than baseline. Candidates are at/near the attainable bound for every
important bucket. See ../REPORT.md.
