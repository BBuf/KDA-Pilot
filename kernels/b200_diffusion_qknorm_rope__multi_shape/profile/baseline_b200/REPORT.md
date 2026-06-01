# NCU Report — SGLang fused-qknorm-rope baseline on B200

Run: `baseline_b200` | host `innomatrix-us-adc-smb200-0003` | container `sglang_bbuf`
| physical GPU 4 (NVIDIA B200, sm_100, 148 SMs) | commit `68a32061`.
Kernel: `fused_qknorm_rope_warp<128, 128, is_neox=0, use_pdl=1, bf16, int64>`
(the current SGLang baseline; PDL is ON because `is_arch_support_pdl()` is true on B200).
Method: `ncu --set full -k regex:qknorm -s 5 -c 1` on a Python entrypoint (warmup ×5,
then the profiled steady-state launch). Reports: `reports/{small,large}_full.ncu-rep`
(remote); parsed metrics in `analysis/{small,large}_raw.csv`. Profiling one launch
(`-c 1`); per-line stall attribution (`--set source`) needs `-lineinfo` and is
deferred to the candidate harness.

Cross-reference: isolated benchmark medians (commit `68a32061`, `benchmark.csv`):
small `qwen B19` baseline = 60.67µs; large `qwen-edit B8424` baseline = 95.55µs.

## Representative shapes

| metric | small `qwen B19/H24` | large `qwen-edit B8424/H24` |
|---|---|---|
| device time `gpu__time_duration.sum` | **7.55 µs** | **109.6 µs** |
| isolated benchmark median (end-to-end) | **60.67 µs** | 95.55 µs |
| compute SOL `sm__throughput…elapsed` | 2.6 % | 60.3 % |
| memory SOL `gpu__compute_memory_throughput…elapsed` | 2.5 % | 50.2 % |
| DRAM read %peak `dram__bytes_read.sum…elapsed` | 0.43 % | **12.8 %** |
| DRAM write %peak | 0 % | 5.2 % |
| DRAM bytes (read / write) | 249.6 KB / 0 | 107.8 MB / 44.0 MB |
| L2 hit `lts__t_sector_hit_rate.pct` | 46.5 % | 50.0 % |
| achieved occupancy `sm__warps_active…active` | **12.7 %** | 88.9 % |
| theoretical occupancy | 100 % | 100 % |
| grid size / block size | 114 / 256 | 1184 / 256 |
| waves per SM `launch__waves_per_multiprocessor` | **0.10** | 1.0 |
| registers/thread | 32 | 32 |
| top stall (ratio) | long_scoreboard 11.2 | long_scoreboard 11.9 |
| next stalls | no_instruction 3.0; short_scoreboard 2.4; wait 2.0 | wait 2.4; short_scoreboard 1.4; math_pipe_throttle 1.0 |

## Named active bound

### Small shapes (19–195 tokens): launch / dispatch-overhead bound
The device kernel runs in **7.55 µs**, but the isolated end-to-end latency is
**60.67 µs** — so **~53 µs (~88 %)** is host-side dispatch/launch overhead (the torch
`register_custom_op` dispatch + the JIT module lookup + `cudaLaunchKernel`), captured
in the CUDA-event window because the GPU idles between the start marker and the kernel.
This is the same failure mode as the prior H200 ~5 µs/call dispatcher tax — here ~10×
larger relative to the kernel. The kernel *itself* is also tiny-grid bound: grid = 114
blocks < 148 SMs, `waves/SM` = 0.10, achieved occupancy 12.7 % — it cannot fill the GPU.
**Implication:** the win is in the call path (zero-overhead dispatcher, avoiding the
custom-op wrapper, PDL A/B), NOT the device kernel. Device-side micro-opts are capped
at the ~7.55 µs the kernel already takes. This MUST be measured on the integrated
install path (per AC-4) because in a real pipeline the dispatch overhead may overlap
with adjacent ops and partially hide.

### Large shapes (4096–8424 tokens): memory-latency-bound, NOT DRAM-bandwidth-bound
This corrects the seed-roofline assumption. At only **12.8 % DRAM read %peak** (5.2 %
write) the kernel is **not** bandwidth-bound; achieved DRAM BW ≈ (107.8+44 MB)/109.6 µs
≈ 1.4 TB/s, ~17 % of B200's ~8 TB/s. The dominant stall is **long_scoreboard (11.9
ratio)** — warps waiting on global/L2 load latency — at 88.9 % occupancy, with compute
SOL 60 % and memory SOL 50 %, L2 hit 50 %. So the large kernel is a moderately-utilized,
**memory-latency / mixed compute-memory** kernel, not a bandwidth wall.
**Implication:** headroom is limited (already 60 % compute SOL, 89 % occupancy). Any
gain would come from cutting load latency / redundant traffic (e.g. higher L2 reuse on
the float32 cos_sin_cache, which is re-read per head; L2 hit is only 50 %) or reducing
instruction count — NOT from a bandwidth-oriented rewrite. An evidence-backed no-go on
large shapes is plausible; confirm against a candidate before concluding.

## Next steps (ranked by evidence)
1. Small shapes — attack the ~53 µs dispatch overhead via the integrated install path
   (zero-overhead dispatcher) + PDL-off A/B; device kernel is already ~7.55 µs.
2. Large shapes — investigate cos_sin_cache L2 reuse (hit only 50 %) and load-latency
   hiding; treat as likely near-bound until a candidate shows otherwise.
3. `--set source` (with a `-lineinfo` candidate harness) for per-line long_scoreboard
   attribution once a `.cu/.cuh` candidate exists.
