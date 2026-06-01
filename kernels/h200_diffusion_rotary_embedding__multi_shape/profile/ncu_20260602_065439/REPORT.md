# NCU + roofline bound analysis — candidate v1 (native_cuda_v1_naive_scalar)

- Host `ion-h200-8`, GPU 7 (NVIDIA H200, CC 9.0, HBM3e peak ≈ 4.8 TB/s), container `sglang_bbuf`.
- SGLang `c47f0e7cd` (diffusion RoPE files == pinned `6965fe0ee`). kernel-pilot `723571c91`, .cuh `cce6a0ca1f92`.
- `ncu --set full -k regex:rope_kernel -c 1 -s 8` (post-warmup steady launch), `KDA_PROFILE=1` (`-lineinfo`).
- Binary reports: `<REMOTE_KDA_DIR=…/20260602_065439>/work/profile/ncu_20260602_065439/reports/*.ncu-rep` (kept remote; ~1.1–1.6 MB each). Parsed metrics: `analysis/metrics.csv`.

## Speed-of-Light (from NCU)
| shape | kernel µs | DRAM % | SM % | L2 hit % | achieved occ % | grid |
|---|---|---|---|---|---|---|
| std hunyuanvideo (1,27030,24,128) | 299.5 | 22.9 | **80.4** | 55.0 | 87.6 | 162180×256 |
| ltx2 S=126 half32 | **4.0** | 5.4 | 24.2 | 41.6 | 40.5 | 504×256 |
| ltx2 S=6144 half64 | 120.1 | 24.2 | **77.0** | 33.6 | 88.7 | 49152×256 |

## Active bound per bucket
1. **Large shapes (standard + LTX-2 S≥1536): SM / instruction-throughput bound — NOT memory bandwidth.**
   - SM throughput ~77–80% while DRAM is only ~23% (≈1.1 TB/s of ~4.8 TB/s peak). The SM is saturated, the memory subsystem is idle.
   - Root cause = the naive scalar design: one thread per element-pair, each thread doing **runtime integer div/mod** to decompose `gid → (token, head, half-idx)` (3 div/mods for standard, 4 for LTX-2 — GPU integer division is expensive), plus **single-element bf16 loads/stores** (no vectorization) and per-element fp32 conversions. 41.5M threads × several int-divisions saturates the SM pipes.
   - This corrects the Round-0 assumption that these are simply "memory-bound elementwise" ops: as currently written the candidate is compute/instruction-bound, with large unused bandwidth headroom.

2. **Tiny shape (LTX-2 S=126 half32): launch/occupancy + per-call overhead bound.**
   - Kernel is only **4.0 µs**, but the benchmark wall-clock is ~147 µs → the gap is per-call wrapper + launch overhead (Python gate/`empty_like`/reshape/tvm-ffi call), not the kernel.
   - Only 504 blocks → 40.5% achieved occupancy (under-fills the 132 SMs). The kernel itself is small; the wall-clock comparison vs the baseline (24.6 µs) is dominated by dispatch overhead, which the final in-SGLang export (direct call) removes.

## Roofline (analytical, minimal traffic with cos/sin reuse)
- Standard hunyuanvideo: x(165.9 MB)+out(165.9 MB)+cos/sin(13.8 MB) = 345.6 MB → ideal @4.8 TB/s = **72 µs**. Baseline triton 158 µs ≈ 46% of peak BW; candidate 299 µs is instruction-bound at 23% DRAM, far from the BW roof.
- LTX-2 S=6144 half64: x(50.3)+out(50.3)+cos/sin(50.3) = 151 MB → ideal **31 µs**. Baseline 59.7 µs ≈ 53% peak BW; candidate 120 µs instruction-bound.
- LTX-2 S=126: ~1.5 MB → ideal ~0.3 µs; overhead-dominated regardless.

## Resulting optimization directions (for the next round, ranked by evidence)
1. **Kill per-thread integer div/mod**: map threads to `(token, head, half/pair-idx)` via a fixed block/thread layout (e.g., one block (or warp-set) per token covering all heads, `threadIdx` → contiguous lane index) so indices come from `blockIdx`/`threadIdx` arithmetic without runtime division. Highest expected SM-throughput win.
2. **Vectorize loads/stores**: 128-bit (`float4`/`bf16x8`) aligned loads/stores for x and output (and the contiguous `half`-dim for LTX-2), amortizing address math and raising memory-level parallelism. Targets the 23% DRAM → toward the baseline's ~50% and beyond.
3. **Reuse standard cos/sin across heads**: load the token's `head_size/2` fp32 cos/sin once into shared mem/registers instead of re-reading per head (cuts L2 traffic; L2 hit 55% shows current redundancy).
4. **Tiny-shape path**: the kernel is already 4 µs; reduce per-call wrapper overhead (cache gate decision / minimize Python work) rather than the kernel. The final export removes most of it.

Completion bar (DEC-4): optimize toward the active bound — for large shapes that means raising SM efficiency then approaching the HBM roof (≈72/31 µs); geomean is reported as an outcome. NCU will be re-run after each candidate to confirm the bound shifts.
