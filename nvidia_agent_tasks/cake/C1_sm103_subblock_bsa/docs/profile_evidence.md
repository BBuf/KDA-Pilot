# Profile evidence: MiniMax-H3 attention shapes (dense reference arm)

## `workloads_dense_reference.json` (model: `MiniMaxAI/MiniMax-H3`)

| op | real calls | distinct signatures | rows kept |
| --- | ---: | ---: | ---: |
| `diffusion_attention_cudnn_sdpa` | 216 | 4 | 4 |
| `diffusion_attention_fa4` | 200 | 1 | 1 |
| `diffusion_attention_sdpa` | 16 | 3 | 3 |

Representative shapes (largest / smallest kept row per op):

- `diffusion_attention_cudnn_sdpa` hottest: query[1, 26, 16, 128]:bfloat16, key[1, 26, 2, 128]:bfloat16, value[1, 26, 2, 128]:bfloat16
  - another operating point: query[1, 24, 14, 128]:bfloat16 (non-contig), key[1, 24, 14, 128]:bfloat16 (non-contig), value[1, 24, 14, 128]:bfloat16 (non-contig)
- `diffusion_attention_fa4` hottest: query[1, 26, 16, 128]:bfloat16, key[1, 26, 2, 128]:bfloat16, value[1, 26, 2, 128]:bfloat16
- `diffusion_attention_sdpa` hottest: query[1, 26, 28, 128]:bfloat16 (non-contig), key[1, 26, 28, 128]:bfloat16 (non-contig), value[1, 26, 28, 128]:bfloat16 (non-contig)
  - another operating point: query[1, 24, 14, 128]:bfloat16 (non-contig), key[1, 24, 14, 128]:bfloat16 (non-contig), value[1, 24, 14, 128]:bfloat16 (non-contig)


Call counts are real traffic only: every call observed before a capture-group
label was active (start-up, CUDA-graph capture, autotune) is kept separately in
the `warmup_only_shapes` section of the source manifest and never enters a
workload row. See `../../docs/workload_capture.md`.

These are the **dense** shapes captured from the shipped 4-GPU H3 speed config, which is the
correctness reference and the performance bar for the sparse kernel. Note the two regimes in one
model: the video tower runs `q[1, 37736, 14, 128]` (per rank, 14 heads after TP2 x Ulysses2)
while the audio tower runs `q[1, 26, 16, 128]` - the short-sequence regime whose fallback is the
subject of task C4.

To capture the sparse arm's block-schedule metadata, re-run the same command with the sub-block
backend selected; the capture hook already wraps
`SubBlockSparseAttentionImpl.forward` / `forward_varlen`. Expect ~25% of requests to hang - that
is the bug this task is about.
