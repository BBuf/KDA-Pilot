# Results

> **Status: INTERIM (Round 1).** Correctness is verified bitwise on B200 and the
> immutable baseline numbers are established, but the current candidate is the
> initial *correct-by-construction scalar* kernel and is **slower than the
> baseline** (production geometric-mean speedup **0.63×**). This is neither a
> promotable win nor an evidence-backed no-go yet — the optimized kernel (task9)
> is the next round.

## Setup
- GPU: NVIDIA B200 (`ion-b200`, GPU 0, idle before/after); see `docs/run_log.md`.
- Baseline: copied SGLang Triton `_fused_cat_pad_5d_kernel` @ `67b2a9e` via destination-passing `baseline/binding.py`.
- Candidate (this round): scalar one-thread-per-output transliteration (`solution/kernel.cu`).
- Tolerance: bitwise exact (`atol=0, rtol=0`); all 10 workloads passed the A/B correctness gate. Timing: CUDA events, inner-loop amplification, interleaved A/B (template defaults).

## Per-shape results (baseline vs initial scalar candidate)

| Workload | Headline | baseline median (µs) | candidate median (µs) | speedup |
|----------|:--------:|---------------------:|----------------------:|--------:|
| `prod_c1024_t1_h30_w52__cache1`  | ✅ | 25.512  | 36.172   | 0.705 |
| `prod_c1024_t1_h30_w52__cache2`  | ✅ | 25.881  | 37.122   | 0.697 |
| `prod_c1024_t2_h60_w104__cache1` | ✅ | 109.064 | 173.104  | 0.630 |
| `prod_c1024_t2_h60_w104__cache2` | ✅ | 108.886 | 181.216  | 0.601 |
| `prod_c512_t4_h120_w208__cache1` | ✅ | 312.360 | 511.120  | 0.611 |
| `prod_c512_t4_h120_w208__cache2` | ✅ | 313.416 | 524.672  | 0.597 |
| `prod_c256_t4_h240_w416__cache1` | ✅ | 613.056 | 1002.496 | 0.611 |
| `prod_c256_t4_h240_w416__cache2` | ✅ | 617.552 | 1032.992 | 0.598 |
| `reg_cache_null` (non-headline)       | — | 25.437  | 35.029   | 0.726 |
| `reg_no_pad_cat_only` (non-headline)  | — | 25.264  | 24.680   | 1.024 |

**Production headline:** equal-weight geometric-mean speedup **0.630×** (arith mean 0.631×, min 0.597×, max 0.705×).

## Reading the result
- The op is DRAM-bandwidth-bound pure data movement. The scalar candidate issues one
  thread per output element with 64-bit flat-index arithmetic and per-element loads,
  which underperforms Triton's `block_size=256` vectorized copy — hence 0.6–0.7× on the
  padded production shapes.
- The cat-only regression row (`reg_no_pad_cat_only`, a pure contiguous copy with no
  spatial borders) is already ~1.0×, confirming the deficit is in the bordered/strided
  interior-copy path, not raw copy throughput.

## Next (Round 2)
- task8 (analyze/KernelWiki): rank optimized designs.
- task9: row-oriented CTA mapping over `(N,C,D_out,H_out)`, vectorized interior W-copy
  (alignment-gated, scalar prologue/tail for the `W_l=1` shift), bounded zero-border path,
  `cache_t=1/2` handling — re-run correctness after each edit, then re-benchmark.
- task11 (analyze): NCU/roofline (achieved GB/s vs B200 sustainable bandwidth) to confirm
  the bound and guide edits.
