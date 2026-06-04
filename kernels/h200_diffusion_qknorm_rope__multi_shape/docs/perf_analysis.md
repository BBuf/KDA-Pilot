# Roofline + bound analysis — fused_qknorm_rope (H200, sm_90, bf16)

Candidate: `fused_qknorm_rope_warp2` (2-heads-per-warp float4), `src/csrc/qknorm_rope_kernel.cuh`.
Hardware: NVIDIA H200 (HBM3e, ~4.8 TB/s boost peak). Evidence: `profile/round_warp2_*` NCU reports
(`reports/full.ncu-rep` on REMOTE_KDA_DIR), `benchmark.csv`.

## Memory traffic model (per kernel, dominant terms)
Per (token, head) work item the kernel reads one head of q or k (head_dim bf16) and writes it back;
q_weight/k_weight (head_dim bf16) and the per-token cos/sin row (rope_dim f32) are reused across all
heads of a token and the two tensors, so they are L2/L1-amortized; positions is one int per token.
- Dominant DRAM bytes/work-item ≈ read 256 B + write 256 B = **512 B** (head_dim=128 bf16).
- Amortized: weights (256 B, read once, cached), cos/sin (rope_dim·4 = 512 B/token, reused over 48 heads),
  positions (8 B/token).

For **qwen_t4096** (tokens=4096, q_heads=k_heads=24 → 48 work items/token):
- q+k read+write ≈ 4096·48·512 B ≈ **100.7 MB** (+ cos/sin ≈ 2.1 MB + weights negligible) ≈ **~103 MB**.
- Measured candidate module latency = **38.08 µs** ⇒ effective DRAM BW ≈ 103 MB / 38.08 µs ≈ **2.70 TB/s**
  ≈ **~56 % of HBM3e boost peak**. Baseline = 40.77 µs ⇒ ≈ 2.53 TB/s (~53 %).

## NCU bound (qwen_t4096, warp2, -lineinfo, GPU7 idle)
| Metric | Value | Reading |
|---|---|---|
| Duration | 39.33 µs | matches benchmark |
| DRAM Throughput | **39.56 %** of peak | NOT bandwidth-saturated |
| Compute (SM) Throughput | 58.1 % | moderate |
| SM Busy | 62.2 % | |
| L2 Hit Rate | 49.9 % | cos/sin + weight reuse partial |
| Dominant warp stall | **long-scoreboard 58.2 %** of 18.2 avg cycles | **memory-latency-bound** |
| Achieved Occupancy | 72.68 % (theoretical 75 %) | register-limited (38 reg/thread) |
| Waves Per SM | 1 | |

## Diagnosis
Large shapes are **memory-latency-bound**, not bandwidth-bound: DRAM is only ~40 % of peak while the
long-scoreboard stall (waiting on global loads) dominates at 58 %. The 2-heads-per-warp float4 path
beats the one-head baseline (module 1.07–1.08× on large) by issuing **wider memory work per warp**
(one 128-bit load/store per lane) and halving launched warps — improving memory-level parallelism /
latency hiding per the Codex D1 analysis — even though its achieved occupancy (72.7 %) is slightly
below the baseline's (~81–85 %) due to higher register pressure (38 reg/thread).

**Near the attainable bound:** for an elementwise kernel whose irreducible traffic is the q/k
read+write, a latency-bound profile at ~40 % DRAM with long-scoreboard dominant and ~73 % occupancy is
characteristic of being near the attainable bound. The remaining gap to a hypothetical BW-saturated
ceiling is latency, not throughput; closing it would require lowering register pressure to raise
occupancy (bounded upside, risks correctness/complexity) — a ranked future direction, not pursued
since the candidate already clears the >5 % large-shape win bar (Codex no-go threshold).

## Tiny shapes (qwen_t19, T≤195) — NCU (warp2, -lineinfo, GPU7 idle)
| Metric | Value | Reading |
|---|---|---|
| Duration (device) | 4.13 µs | kernel body only |
| DRAM Throughput | 1.25 % | negligible data |
| Compute (SM) Throughput | 3.30 % | idle |
| SM Busy | 15.0 % | |
| Grid Size | 57 blocks (on 132 SMs) | under-subscribed |
| Waves Per SM | 0.07 | massively underfilled |
| Achieved Occupancy | 12.4 % (theoretical 75 %) | launch/underfill-bound |

Launch/underfill-bound: only 57 blocks (0.07 waves/SM, 12.4 % occupancy) — the GPU is nearly empty,
and the ~8.5 µs benchmark module-level time is dominated by launch/dispatch overhead, not the 4.13 µs
of device work. Kernel-body optimization has no leverage here (candidate module ~0.99×, within noise);
the end-to-end win on tiny shapes comes from the lean Python dispatch (wrapper-level ~1.10×). This is an
evidence-backed **no-go for kernel-side tiny-shape optimization** (closing it would require launch
fusion / CUDA-graph capture / batching adjacent ops — outside this kernel's boundary). Matches prior
art (~13 % occupancy).

## Conclusion
The candidate is an **evidence-backed win near the attainable bound**: large shapes are
memory-latency-bound (warp2 gives 1.069–1.085× module / 1.065–1.080× wrapper via wider per-warp memory
work), tiny shapes are launch-bound (kernel no-go; lean dispatch gives ~1.05–1.09× wrapper). All-9
geomean (d3-final, src 4f70cda7, GPU7 external idle verified): **wrapper 1.0723×, module 1.0268×**. No
further RLCR iteration is warranted on the kernel — the remaining gap on large shapes is memory latency
(not throughput), and tiny shapes are launch-bound. (The NCU bound figures above were collected on the
byte-identical warp2 rope_dim=128 machine code; round-0 d2 reported 1.0992×/1.0285× with an lru_cache
wrapper — superseded.)

---

# Continuation addendum (2026-06-04) — `cossin-vec` (`6669bd218e336c9d`)

Environment: torch 2.11.0+cu130 / nvcc 13.0, container `sglang_bbuf`, SGLang pin `c47f0e7cd`
(worktree), GPU 7 externally idle per batch. Full NCU report: `profile/round_cossin_vec/REPORT.md`.

## What changed in the bound picture
The prior "near the attainable bound" verdict had a hidden lever: under the current toolchain the
incumbent compiles to 38 registers/thread, capping theoretical occupancy at 75%. Replacing the
warp2 path's eight scalar cos/sin `__ldg` loads with two 128-bit quartet loads (static unrolled
indexing) freed 6 registers → **32/thread, exactly the H200 100%-theoretical-occupancy boundary**
(64K regs/SM ÷ 2048 threads):

| qwen_t4096 (module) | incumbent | cossin-vec |
|---|---|---|
| Duration | 38.13 µs | **33.97 µs** |
| Theoretical / achieved occupancy | 75% / 72.5% | **100% / 90.4%** |
| Occupancy-capped grid | 792 | 1056 |
| Memory throughput | 2.005 TB/s (41.7% DRAM peak) | **2.245 TB/s (46.8%)** |
| Long-scoreboard | 10.6 cyc/issued inst | 11.8 (amortized over 57.8 vs 46.4 warps/SM) |

Roofline (irreducible-traffic model, ~103 MB per qwen_t4096 call): effective application-level
bandwidth 103 MB / 33.97 µs ≈ **3.03 TB/s ≈ 63% of HBM3e boost peak** (was ≈2.70 TB/s / 56%).
DRAM-level throughput 46.8% of peak — the kernel remains memory-LATENCY-bound, not
bandwidth-saturated.

## Remaining headroom (why the round stops here)
Post-change long-scoreboard attribution (source counters): 45% q/k input unpack (the irreducible
read of the tensor being normalized), 34% norm-apply chain, 14.5% positions→row-address LEA, ~6%
cos/sin consumers. The two bounded follow-ups were adjudicated:
- Load hoist above the reduction (attacking the LEA share): REJECTED — extends quartet live ranges,
  registers 32→40, theoretical occupancy back to 75% (achieved 63.8–65%), measured gain small and
  shrinking across runs (large 1.0148×→1.0085×).
- Shared-memory cos/sin staging: SKIPPED with evidence — ~6% residual cos/sin stalls cannot pay for
  block-wide synchronization at 90% occupancy in a 34 µs kernel.
With occupancy at 90.4% achieved / 100% theoretical, waves/SM=1, and the dominant stalls on
irreducible input traffic, the candidate is at the attainable bound for this kernel class on H200.
Tiny shapes (T≤195) remain launch/underfill-bound — kernel no-go stands (module-level parity
0.997–1.011 across all continuation measurements).

## Outcome metrics (module level, interleaved A/B/C, externally idle)
- vs incumbent d3-final: **all-9 geomean 1.0622×, large 1.1424×** (1.134–1.148 per shape).
- vs SGLang baseline: all-9 1.1009×, large 1.2373× (B-leg reproduced 1.2356/1.2367 in two more runs).
- In-SGLang in-tree arbiter (shipping integration, both legs through the identical public op):
  **geomean 1.0945×**, large 1.188–1.222×, parity-or-speedup on every shape.
