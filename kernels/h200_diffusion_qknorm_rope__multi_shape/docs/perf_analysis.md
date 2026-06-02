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
