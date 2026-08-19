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
workload row. See `../docs/workload_capture.md`.

These are the **dense** shapes captured from the shipped 4-GPU H3 speed config, which is the
correctness reference and the performance bar for the sparse kernel. Note the two regimes in one
model: the video tower runs `q[1, 37736, 14, 128]` (per rank, 14 heads after TP2 x Ulysses2)
while the audio tower runs `q[1, 26, 16, 128]` - the short-sequence regime whose fallback is the
second lever described below.

To capture the sparse arm's block-schedule metadata, re-run the same command with the sub-block
backend selected; the capture hook already wraps
`SubBlockSparseAttentionImpl.forward` / `forward_varlen`. Expect ~25% of requests to hang - that
is the bug this task is about.

## The sparse arm is runnable on sm_103, and here is the exact recipe

`bench/run_sparse_arm.sh` is the script we ran tonight; it completed a full 49-step
generation on 4x B300 without hanging (the hang is ~25% per request, so a single clean run
proves nothing about the bug - it proves the recipe works). What it needs:

* the SGLang worktree with the two SM103 enablement commits (`Enable SubBlock sparse
  attention on SM103`, `Support renamed FlashInfer blk64 entry point`) plus the local
  patch to `subblock_sparse_attn.py`;
* the patched FlashInfer checkout on `PYTHONPATH` (the upstream blk64 kernel is built
  `-gencode=arch=compute_100a,code=sm_100a`, so **sm_103 has no cubin** and the backend's
  own guard only compares the major version - it accepts 10.3 and fails later);
* `SGLANG_SUBBLOCK_SM103_BSA=1`;
* `--attention-backend subblock_sparse_attn --attention-backend-config
  '{"sparsity":0.75,"n_k":4,"n_q":4,"skip_first_steps":10,"skip_first_layers":0,"min_seq_len":4096}'`.

Note `min_seq_len: 4096`: every sequence below it takes the dense fallback, which is why
H3's 24-26 token audio components never enter the sparse path - see
the fallback section below.

### Capture gap, stated plainly

Our hook wrapped `SubBlockSparseAttentionImpl.forward` / `forward_varlen` and the run did
use the backend ("Using subblock_sparse_attn attention backend"), yet those entries
recorded 0 calls while the text-encoder's FA path recorded 4 - i.e. the DiT worker
processes did not report. So this task ships the dense reference shapes, the schedule
parameters above, the forensics, and a runnable recipe, but **not** a captured BSA payload.
The block grid is derivable: 37,736 tokens per rank, `n_q=n_k=4`, sparsity 0.75, head_dim
128 (the kernel's hard limit), skipping the first 10 steps and no layers.

## The dense fallback next to it (was a separate task, folded in here)

With a sparse backend active, every sequence below the backend's `min_seq_len` (4096 in
the shipped config) takes a dense fallback, and on H3 that fallback is expensive enough
to eat most of the sparse win. Step-level accounting from the B300 sweep, derived from
`perf_dump` `denoise_steps_ms` and cross-checked against an independent classification of
the dense run:

| step type | dense arm | with sub-block sparse |
| --- | --- | --- |
| full step | ~418 ms | ~221 ms (near half - the sparse win) |
| `v` step (audio + probe) | ~44 ms | **~191 ms** (the fallback) |
| skipped step | ~11 ms | ~10 ms |

Net: the sparse arm lands at 10.37 s vs 11.16 s per video (7.1% net) instead of the ~9 s
the full-step win alone implies. So a candidate kernel is only worth shipping if the
short-sequence path stays at the dense-path cost - which is why the gate below includes
"no regression on the non-sparse branch".

Sparse backend scoreboard on B300, all on top of the same cache schedule:

| backend | time / video | LPIPS (mean / max) | verdict |
| --- | --- | --- | --- |
| sub-block BSA | **10.37 s** | 0.349 / 0.415 | fastest, deadlocks ~25% of requests - this task |
| cube / flex (`[4,4,4]`) | 13.38 s | 0.522 | loses on both axes |
| NVlabs Sol-Attn (Triton) | 12.87 s | 0.365 | slower than our dense cuDNN baseline |
| cache-only (no sparse) | 11.16 s | 0.293 / 0.399 | current shipped default |
