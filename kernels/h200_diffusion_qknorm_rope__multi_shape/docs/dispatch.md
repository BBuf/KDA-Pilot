# Dispatcher decision — h200_diffusion_qknorm_rope__multi_shape

**Decision: a single universal kernel — 2-heads-per-warp — for the entire captured
shape regime (bf16, head_dim=128, rope_dim=128, is_neox=False, equal Q/K heads,
int32/int64 positions). No per-bucket dispatch is warranted.** Everything outside this
regime routes via the `_supported` gate to one of two safe fallbacks: the **SGLang CUDA
baseline** for layouts it can still run (e.g. is_neox / other head_dim/rope_dim, but still
bf16 / contiguous / 16-byte-aligned / non-aliased / same-device / int32-64 positions), or the
**portable PyTorch reference** (`_reference_qknorm_rope`) for anything it cannot (CPU,
device-mismatch, non-contiguous, misaligned, aliased, fp16, exotic position dtype). See
`interface.md` for the full fallback table.

## Evidence: 2-head vs 1-head warp mapping on H200 (GPU 7, idle)

`profile/round0_ncu/bench_variants.py` — direct kernel calls (no wrapper overhead),
pristine inputs per sample, CUDA-event median; `maxdiff` = max abs diff between the
1-head and 2-head outputs (both already validated against the oracle).

| Shape (T×H) | 2-head µs | 1-head µs | 2-head speedup vs 1-head | maxdiff | Chosen |
|---|---|---|---|---|---|
| large_h24 8424×24 | 65.66 | 79.78 | 1.215× | 0.0156 | 2-head |
| large_h30 4128×30 | 41.09 | 49.09 | 1.195× | 0.0312 | 2-head |
| qwen_4096 4096×24 | 33.50 | 40.19 | 1.200× | 0.0156 | 2-head |
| tiny_47 47×24 | 9.22 | 9.18 | 1.003× (tie) | 0.0156 | 2-head (tie) |
| tiny_19 19×24 | 9.22 | 9.22 | 1.000× (tie) | 0.0078 | 2-head (tie) |

The 2-heads-per-warp path (16 lanes/head, 8 bf16/lane via `float4`) wins by ~1.20–1.22×
on the large shapes — more bytes in flight per warp (memory-level parallelism) on the
bandwidth/latency-bound large buckets — and ties the 1-head path on the launch-bound tiny
shapes. `maxdiff ≤ 0.0312` (one bf16 quantum; both within ATOL=8e-2/RTOL=1e-2 vs the
oracle) confirms the two mappings are numerically equivalent. Since 2-head wins-or-ties
everywhere, a per-bucket dispatcher would add complexity with no benefit.

## Per-bucket promote/reject (vs SGLang baseline, end-to-end via the wrapper)

| Bucket | baseline µs | candidate µs (2-head) | speedup | active bound (NCU) | decision |
|---|---|---|---|---|---|
| large_h24 8424×24 | 83.30 | 70.78 | 1.177× | memory-latency (long-scoreboard ~47%, DRAM 51%) | promote |
| large_h30 4128×30 | 53.89 | 46.18 | 1.167× | memory-latency (DRAM 45%) | promote |
| qwen 4096×24 | 45.58 | 38.53 | 1.183× | memory-latency | promote |
| zimage 4096×30 | 54.05 | 45.84 | 1.179× | memory-latency | promote |
| zimage 4128×30 | 53.89 | 46.18 | 1.167× | memory-latency | promote |
| tiny (19/32/47/189/195) | ~16.3–16.9 | ~14.2–14.4 | 1.13–1.17× | launch/underfill | promote (near-baseline win from lower launch overhead) |

Geomean over the 9 captured shapes: **~1.11×** (run-to-run ~1.09–1.13; large shapes stable
~1.14–1.16×, launch-bound tiny shapes noisy; the per-bucket
baseline/candidate µs in the table above are from the round-0 lighter-gate run and are
illustrative -- the 2-head-vs-1-head variant comparison and the dispatch decision are
unaffected). The runtime gate guarantees the 2-head
preconditions (even Q+K head count — H=24→48 and H=30→60 are both even; 16-byte alignment;
no q/k aliasing) before invoking the kernel, and falls back to the SGLang baseline
otherwise. See `profile/round0_ncu/REPORT.md` for the bound analysis.
