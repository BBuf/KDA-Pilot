# Profile evidence: DSA sparse attention (DeepSeek-V4-Flash)

## `workloads.json` (model: `deepseek-ai/DeepSeek-V4-Flash`)

| op | real calls | distinct signatures | rows kept |
| --- | ---: | ---: | ---: |
| `dsa_compress_forward` | 576603 | 1722 | 11 |
| `dsa_compress_norm_rope_store` | 576603 | 1743 | 12 |
| `dsa_fused_q_indexer_rope_hadamard_quant` | 195301 | 574 | 6 |
| `dsa_topk_transform_v2` | 189085 | 348 | 6 |
| `dsa_paged_mqa_logits_metadata` | 9301 | 574 | 6 |
| `dsa_topk_transform` | 6216 | 233 | 18 |

Representative shapes (largest / smallest kept row per op):

- `dsa_compress_forward` hottest: kv_score_buffer[40143, 4, 512]:float32, kv_score_input[1, 512]:float32, ape[8, 128]:float32
  - another operating point: kv_score_buffer[40143, 4, 2048]:float32, kv_score_input[15415, 2048]:float32, ape[8, 512]:float32
- `dsa_compress_norm_rope_store` hottest: kv[1, 128]:float32, norm_weight[128]:float32, freq_cis[1048576, 32]:complex64, out_loc[1]:int64, kvcache[100358, 8448]:uint8
  - another operating point: kv[0, 512]:float32, norm_weight[512]:float32, freq_cis[1048576, 32]:complex64, out_loc[2]:int64, kvcache[100358, 1728]:uint8
- `dsa_fused_q_indexer_rope_hadamard_quant` hottest: q_input[1, 64, 128]:bfloat16, weight[1, 64]:bfloat16, freqs_cis[1048576, 32]:complex64, positions[1]:int32
  - another operating point: q_input[15415, 64, 128]:bfloat16, weight[15415, 64]:bfloat16, freqs_cis[1048576, 32]:complex64, positions[15415]:int32
- `dsa_topk_transform_v2` hottest: scores[1, 262208]:float32, seq_lens[1]:int32, page_tables[1, 4097]:int32, out_page_indices[1, 512]:int32, metadata[2, 2]:int32
  - another operating point: scores[256, 262208]:float32 (non-contig), seq_lens[256]:int32, page_tables[256, 4097]:int32, out_page_indices[256, 512]:int32, metadata[257, 2]:int32
- `dsa_paged_mqa_logits_metadata` hottest: seq_lens[1, 1]:int32
  - another operating point: seq_lens[15415, 1]:int32
- `dsa_topk_transform` hottest: scores[198, 192]:float32 (non-contig), seq_lens[198]:int32, page_tables[198, 3]:int32, out_page_indices[198, 512]:int32, out_raw_indices[198, 512]:int32
  - another operating point: scores[733, 192]:float32 (non-contig), seq_lens[733]:int32, page_tables[733, 3]:int32, out_page_indices[733, 512]:int32, out_raw_indices[733, 512]:int32


Call counts are real traffic only: every call observed before a capture-group
label was active (start-up, CUDA-graph capture, autotune) is kept separately in
the `warmup_only_shapes` section of the source manifest and never enters a
workload row. See `../docs/workload_capture.md`.

**What actually runs on the recommended B300 path** (this is the useful half of the evidence):
the compression, indexer-quant and top-k transform entry points fire in every one of the nine
capture groups, while `tilelang_sparse_fwd`, `triton_sparse_mla_fwd` and the DeepGEMM/CuTe-DSL
paged-MQA-logits variants fired **0 times** - on this checkpoint and backend they are dead code.
Optimizing them would repeat a mistake we have already made once (a bit-exact router kernel that
turned out to be fused away in the recommended deployment).

GSM8K accuracy of the capture run: **0.980** (200 questions, 5-shot) and **1.000** (16-shot).
