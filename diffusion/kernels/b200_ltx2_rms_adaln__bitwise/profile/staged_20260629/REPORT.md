# NCU Report — staged candidate modulation kernel (task12)

Nsight Compute on NVIDIA B200 (`ion-b200`, GPU 6, idle), container `sglang_bbuf`,
CUDA 13.0. Kernel: `rms_adaln_modulation_kernel` (the candidate's fused
`normed * (1+scale) + shift` pass; the shared `at::rms_norm` step is excluded by
`-k regex:rms_adaln_modulation`). Raw reports: `video.ncu-rep`, `audio.ncu-rep`
(local only, gitignored). Command:
`CUDA_VISIBLE_DEVICES=6 ncu -k regex:rms_adaln_modulation -s 5 -c 1 -o <out> --metrics <set> python3 bench/profile_one.py B S D`.

## Metrics

| Metric | Video `[1,6144,4096]` | Audio `[2,126,2048]` |
|--------|----------------------:|---------------------:|
| Duration (modulation kernel) | 45.76 µs | 7.26 µs |
| DRAM bytes read | 151.01 MB | 3.11 MB |
| DRAM bytes write | 29.25 MB | ~0 MB |
| **DRAM throughput (% peak)** | **51.4 %** | 5.6 % |
| SM throughput (% peak) | 62.7 % | 7.8 % |
| Achieved occupancy | 60.2 % | 20.3 % |
| Grid / block | 6144 / 512 | 252 / 256 |

## Interpretation

- **Video (large rows): memory-bound.** Reads ≈ `normed + scale + shift` (3 × 50.3 MB ≈ 151 MB, matches), DRAM at 51.4 % of peak (≈ 3.9 TB/s of B200's ~8 TB/s HBM3e), 60 % occupancy. This is the dominant cost of the candidate (~45.8 µs of the ~54 µs total; the shared `at::rms_norm` is the remainder). The ~2× end-to-end speedup comes from collapsing eager's three elementwise modulation launches + two full-size temporaries into this single fused pass. There is bandwidth headroom (~51 %), so a future memory-tuning pass (occupancy / launch shape) could push it further — but the kernel is correct and bit-locked, so any change must re-pass the bitwise gate.
- **Audio (small rows): launch / latency-bound.** Only 252 blocks on 148 SMs (~1.7 blocks/SM) → 20 % occupancy, 5.6 % DRAM. The problem is too small to saturate the GPU; the ~2× speedup here is from issuing one fused kernel instead of three elementwise launches (launch-overhead reduction), not bandwidth.

## Relation to task10 (fused kernel)
A fully-fused single kernel would remove the `normed` write+read (~2 of the 6 array passes), the obvious next bandwidth win. But the `bench/probe_fused.py` probe shows a custom single-kernel fp32 RMS reduction does **not** reproduce `at::rms_norm`'s `normed` bits (43–248 elements differ per large row, ~0.0002 %, 1 ULP) — so a fused kernel cannot be bit-exact. NCU confirms the staged kernel is memory-bound but correct; the fused path is a no-go for the bitwise contract (see `docs/dispatch.md`).
