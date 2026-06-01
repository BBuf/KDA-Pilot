# Performance analysis — `h200_diffusion_qknorm_rope__multi_shape`

Hardware: NVIDIA H200 (SM90, Hopper), HBM3e peak bandwidth ~4.8 TB/s, 132 SMs.
Candidate: native CUDA port of the sibling B200 kernel (2-heads-per-warp float4
production path), `src=00a0686e2e29c665`. Baseline: SGLang
`fused_inplace_qknorm_rope` (JIT CUDA). Numbers from `benchmark.csv`
(GPU 7 idle, CUDA-event timing, pristine inputs per sample).

## Why this op is memory-bound

Per `(token, head)` head-vector the kernel does an fp32 RMS reduction over 128
elements (≈128 mul-add), 128 scale-by-weight, and 64 interleaved rotations
(≈4 FLOP each) — a few hundred FLOPs over 256 read + 256 written bytes (bf16
q and k). Arithmetic intensity is O(1) FLOP/byte, far left of the H200 ridge
point (~4.8 TB/s vs ~67 TFLOP/s fp32 → ridge ≈ 14 FLOP/byte). The op is a DRAM
read-modify-write; the achievable bound is HBM3e bandwidth on the large shapes
and kernel-launch / wave-underfill latency on the tiny shapes.

## Effective DRAM bytes (lower bound)

Dominant traffic = q and k read+write (in place): `bytes ≈ T·H·1024` (2 tensors
× 128 elems × 2 B × {read+write}); plus unique cos/sin `T·512 B` (float32,
largely L2-resident across the H heads of a token); weights negligible.

| Shape (T×H) | DRAM bytes | baseline µs | cand µs | baseline GB/s | cand GB/s | cand % of 4.8 TB/s | speedup |
|---|---|---|---|---|---|---|---|
| qwen-edit 8424×24 | 211.3 MB | 83.30 | 70.78 | 2537 | 2986 | 62% | 1.177× |
| zimage 4128×30 | 128.9 MB | 53.89 | 46.18 | 2393 | 2792 | 58% | 1.167× |
| zimage 4096×30 | 127.9 MB | 54.05 | 45.84 | 2367 | 2791 | 58% | 1.179× |
| qwen 4096×24 | 102.8 MB | 45.58 | 38.53 | 2255 | 2667 | 56% | 1.183× |
| tiny 19–195 (T<256) | <5 MB | ~16.3–16.9 | ~14.2–14.4 | — (latency-bound) | — | — | 1.13–1.17× |

## Reading

- Large shapes (4096–8424 tokens): the candidate sustains ~56–62% of HBM3e peak,
  up from the baseline's ~47–53%. The op is bandwidth-bound; the candidate's
  16-byte (`float4`) vectorized 2-heads-per-warp path raises bytes-in-flight and
  closes part of the gap. Nsight Compute (AC-5) **confirmed** the residual gap is
  memory-LATENCY (long-scoreboard ~47% of warp cycles, DRAM only ~45-51% of base-clock
  peak, occupancy already 81-85%), i.e. waiting on the irreducible q/k global loads --
  not occupancy or vector width. The one bounded lever (shared-memory cos/sin staging) is
  recorded as a future direction; the candidate is near the attainable bound for this
  kernel class. See `profile/round0_ncu/REPORT.md`.
- Tiny shapes (T ≤ 195): far too little data to fill 132 SMs (e.g. 19 tokens ×
  24 heads ≈ 228 warps in the 2-head path vs thousands of resident-warp slots);
  these are launch / underfill-latency-bound. The candidate's ~14 µs floor vs the
  baseline's ~16 µs reflects lower per-launch overhead, not bandwidth. Per the
  plan's DEC-2, an evidence-backed baseline/near-baseline result is acceptable
  here once NCU confirms the launch/underfill bound.

> Status: COMPLETE. Analytical roofline + NCU `--set full` profiles for the large-H24 /
> large-H30 / tiny buckets are done (`profile/round0_ncu/REPORT.md`); the active bound and
> near-bound-or-no-go conclusion are recorded there.
>
> Note: the per-shape baseline/candidate µs in the table above are from the round-0
> lighter-gate run; the current end-to-end geomean (with the hardened safety gate) is ~1.11×
> (run-to-run ~1.09–1.13; large shapes stable ~1.14–1.16×, launch-bound tiny shapes noisy). The
> kernel-level bandwidth percentages are essentially unchanged (the gate is a host-side Python
> cost, not a kernel cost).
