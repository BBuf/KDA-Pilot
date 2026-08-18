# Profile evidence: Diffusion attention shapes (Wan2.2-TI2V-5B, MiniMax-H3)

## `workloads_wan.json` (model: `Wan-AI/Wan2.2-TI2V-5B-Diffusers`)

| op | real calls | distinct signatures | rows kept |
| --- | ---: | ---: | ---: |
| `diffusion_attention_sdpa` | 60 | 2 | 2 |
| `diffusion_attention_cudnn_sdpa` | 60 | 2 | 2 |
| `diffusion_fused_scale_residual_norm_scale_shift` | 60 | 2 | 2 |
| `diffusion_fused_norm_scale_shift` | 31 | 2 | 2 |

Representative shapes (largest / smallest kept row per op):

- `diffusion_attention_sdpa` hottest: query[1, 8190, 24, 128]:bfloat16, key[1, 8190, 24, 128]:bfloat16, value[1, 8190, 24, 128]:bfloat16
  - another operating point: query[1, 8190, 24, 128]:bfloat16, key[1, 512, 24, 128]:bfloat16, value[1, 512, 24, 128]:bfloat16
- `diffusion_attention_cudnn_sdpa` hottest: query[1, 8190, 24, 128]:bfloat16, key[1, 8190, 24, 128]:bfloat16, value[1, 8190, 24, 128]:bfloat16
  - another operating point: query[1, 8190, 24, 128]:bfloat16, key[1, 512, 24, 128]:bfloat16, value[1, 512, 24, 128]:bfloat16
- `diffusion_fused_scale_residual_norm_scale_shift` hottest: residual[1, 8190, 3072]:bfloat16, x[1, 8190, 3072]:bfloat16, gate[1, 1, 3072]:float32, weight[3072]:float32, bias[3072]:float32, scale[1]:bfloat16
  - another operating point: residual[1, 8190, 3072]:bfloat16, x[1, 8190, 3072]:bfloat16, scale[1, 1, 3072]:float32, shift[1, 1, 3072]:float32
- `diffusion_fused_norm_scale_shift` hottest: x[1, 8190, 3072]:bfloat16, scale[1, 1, 3072]:float32, shift[1, 1, 3072]:float32
  - another operating point: x[1, 8190, 3072]:bfloat16, scale[1, 1, 3072]:bfloat16, shift[1, 1, 3072]:bfloat16

## `workloads_h3.json` (model: `MiniMaxAI/MiniMax-H3`)

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

**Which backend actually serves which shape on sm_103** (captured, not assumed):
`DynamicCudnnSDPAImpl` handles the long video-tower and cross-attention calls, while
`FlashAttentionImpl` (FA4 CuTe) is still selected for one short-sequence H3 component (200 calls
on `q[1, 26, 16, 128]`). Wan2.2-TI2V-5B at 832x480x81 frames gives `q[1, 8190, 24, 128]` self
and `k[1, 512, 24, 128]` cross.

The measured gap that motivates the task (from our earlier B200/B300 A/B on 11 real shapes):
cuDNN 9.19 SDPA beats the vendored FA4 CuTe kernel by **1.24x-1.98x** (Wan2.2-5B self 8.90 ->
6.84 ms; Wan A14B 112 -> 87 ms; LingBot-506K 1416 -> 1021 ms; H3 image tower 1.98x), worth
**1.132x** end-to-end on Wan2.2-5B - which is why sm_100+ diffusion attention now defaults to
cuDNN in our tree.
