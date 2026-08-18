# Profile evidence: H3 sparse backend selection and the dense fallback

## Captured on the shipped 4-GPU H3 speed config (B300, sm_103, TP2 x Ulysses2)

`bench/workloads_h3_towers.json` holds the real per-rank attention shapes. The two
regimes in one model are the whole point of this task:

| regime | shape (per rank) | backend that served it | calls |
| --- | --- | --- | --- |
| video tower | `q[1, 37736, 14, 128]` | `DynamicCudnnSDPAImpl` | long-sequence path |
| audio / short components | `q[1, 26, 16, 128]`, `q[1, 24, 14, 128]`, `q[1, 26, 28, 128]` | `FlashAttentionImpl` (FA4) 200 calls, cuDNN and plain SDPA for the rest | 216 cuDNN + 200 FA4 + 16 SDPA |

So even in the dense configuration the model already splits across three attention
implementations by sequence length. That is the context for the fallback problem:

## The measured problem

With a sparse backend active, sequences below the backend's `min_seq_len` take a
slow fallback. Step-level accounting from our B300 sweep, derived from
`perf_dump` `denoise_steps_ms` and cross-checked against an independent
classification of the dense run:

| step type | dense | with sub-block sparse |
| --- | --- | --- |
| full step | ~418 ms | ~221 ms (near half - the sparse win) |
| `v` step (audio + probe) | ~44 ms | **~191 ms** (the fallback) |
| skipped step | ~11 ms | ~10 ms |

Net effect: the sparse arm gains 10.37 s vs 11.16 s per video (7.1% net) instead of
the ~9 s it should reach, because the fallback eats most of the full-step win.

## Sparse backend scoreboard on B300 (all on top of the same cache schedule)

| backend | time / video | LPIPS (mean / max) | verdict |
| --- | --- | --- | --- |
| sub-block BSA | **10.37 s** | 0.349 / 0.415 | fastest, but deadlocks ~25% of requests (task `minimax_h3__sm103_block_sparse_attention`) |
| cube / flex (`[4,4,4]`) | 13.38 s | 0.522 | loses on both axes |
| NVlabs Sol-Attn (Triton) | 12.87 s | 0.365 | slower than our dense cuDNN baseline |
| cache-only (no sparse) | 11.16 s | 0.293 / 0.399 | current shipped default |

Sol-Attn's own 1.15x is measured against FA3 on H200. Our dense baseline on B300 is
cuDNN SDPA, which is faster, so a Triton sparse implementation cannot win here - a
CuTe sm_103 implementation is what would make it competitive.
