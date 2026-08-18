# Profile evidence: Triton unified attention (GLM-4.7-Flash)

## `workloads.json` (model: `zai-org/GLM-4.7-Flash`)

| op | real calls | distinct signatures | rows kept |
| --- | ---: | ---: | ---: |
| `triton_fused_moe_gemm` | 571044 | 420 | 8 |
| `triton_decode_attention_grouped` | 286419 | 5010 | 18 |
| `triton_decode_attention` | 286419 | 5010 | 18 |
| `triton_extend_attention` | 5311 | 104 | 14 |

Representative shapes (largest / smallest kept row per op):

- `triton_fused_moe_gemm` hottest: A[1, 2048]:bfloat16, B[65, 3072, 2048]:bfloat16, C[5, 3072]:bfloat16, topk_weights[1, 5]:float32, topk_ids[1, 5]:int32, sorted_token_ids[80]:int32
  - another operating point: A[16384, 2048]:bfloat16, B[65, 3072, 2048]:bfloat16, C[81920, 3072]:bfloat16, topk_weights[16384, 5]:float32, topk_ids[16384, 5]:int32, sorted_token_ids[86078]:int32
- `triton_decode_attention_grouped` hottest: q[1, 20, 576]:bfloat16, k_buffer[3689231, 1, 576]:bfloat16, v_buffer[3689231, 1, 512]:bfloat16 (non-contig), o[1, 20, 512]:bfloat16, kv_indptr[2]:int32, kv_indices[108]:int64
  - another operating point: q[16, 20, 576]:bfloat16, k_buffer[3689231, 1, 576]:bfloat16, v_buffer[3689231, 1, 512]:bfloat16 (non-contig), o[16, 20, 512]:bfloat16, kv_indptr[17]:int32, kv_indices[47075]:int64
- `triton_decode_attention` hottest: q[1, 20, 576]:bfloat16, k_buffer[3689231, 1, 576]:bfloat16, v_buffer[3689231, 1, 512]:bfloat16 (non-contig), o[1, 20, 512]:bfloat16, kv_indptr[2]:int32, kv_indices[108]:int64
  - another operating point: q[16, 20, 576]:bfloat16, k_buffer[3689231, 1, 576]:bfloat16, v_buffer[3689231, 1, 512]:bfloat16 (non-contig), o[16, 20, 512]:bfloat16, kv_indptr[17]:int32, kv_indices[47075]:int64
- `triton_extend_attention` hottest: q_extend[51, 20, 576]:bfloat16, k_extend[51, 1, 576]:bfloat16, v_extend[51, 1, 512]:bfloat16, o_extend[51, 20, 512]:bfloat16, k_buffer[3689231, 1, 576]:bfloat16, v_buffer[3689231, 1, 512]:bfloat16 (non-contig)
  - another operating point: q_extend[2215, 20, 576]:bfloat16, k_extend[2215, 1, 576]:bfloat16, v_extend[2215, 1, 512]:bfloat16, o_extend[2215, 20, 512]:bfloat16, k_buffer[3689231, 1, 576]:bfloat16, v_buffer[3689231, 1, 512]:bfloat16 (non-contig)


Call counts are real traffic only: every call observed before a capture-group
label was active (start-up, CUDA-graph capture, autotune) is kept separately in
the `warmup_only_shapes` section of the source manifest and never enters a
workload row. See `../docs/workload_capture.md`.

**Cross-check:** 75.3% of total serving GPU time in the earlier cookbook-aligned sweep (peak
ShareGPT / concurrency 32). The cookbook recipe for this model prescribes
`--attention-backend triton`, so this Triton kernel is the production attention path, not a
fallback. GSM8K accuracy of the capture run: **0.820** (100 questions, 5-shot).

The KV pool is multi-GB, so payloads store the gathered rows a call actually reads; rebuild a
compact pool from `in_k_buffer__gathered` + `in_k_buffer__rows`.
