# Profile evidence: Mamba-2 SSM + causal conv1d (Nemotron-3-Nano)

## `workloads.json` (model: `nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B-FP8`)

| op | real calls | distinct signatures | rows kept |
| --- | ---: | ---: | ---: |
| `causal_conv1d_decode` | 275863 | 348 | 5 |
| `mamba2_chunk_cumsum` | 7130 | 217 | 14 |
| `mamba2_chunk_state` | 7130 | 217 | 14 |
| `causal_conv1d_prefill` | 7130 | 222 | 15 |
| `mamba2_state_passing` | 7130 | 223 | 15 |
| `mamba2_chunk_scan` | 7130 | 223 | 15 |
| `mamba2_chunk_state_varlen` | 7130 | 223 | 15 |
| `mamba2_chunk_scan_combined_fwd` | 7130 | 223 | 15 |
| `mamba2_chunk_scan_combined` | 7130 | 223 | 15 |

Representative shapes (largest / smallest kept row per op):

- `causal_conv1d_decode` hottest: x[1, 6144]:bfloat16, conv_state[2183, 6144, 3]:bfloat16, weight[6144, 4]:bfloat16, bias[6144]:bfloat16, conv_state_indices[1]:int32
  - another operating point: x[256, 6144]:bfloat16 (non-contig), conv_state[2183, 6144, 3]:bfloat16, weight[6144, 4]:bfloat16, bias[6144]:bfloat16, conv_state_indices[256]:int32
- `mamba2_chunk_cumsum` hottest: dt[1, 16384, 64]:bfloat16 (non-contig), A[64]:float32, dt_bias[64]:bfloat16
  - another operating point: dt[1, 864, 64]:bfloat16 (non-contig), A[64]:float32, dt_bias[64]:bfloat16
- `mamba2_chunk_state` hottest: B[1, 16384, 8, 128]:bfloat16 (non-contig), x[1, 16384, 64, 64]:bfloat16 (non-contig), dt[1, 64, 128, 128]:float32, dA_cumsum[1, 64, 128, 128]:float32, seq_idx[1, 16384]:int32
  - another operating point: B[1, 864, 8, 128]:bfloat16 (non-contig), x[1, 864, 64, 64]:bfloat16 (non-contig), dt[1, 64, 7, 128]:float32, dA_cumsum[1, 64, 7, 128]:float32, seq_idx[1, 864]:int32
- `causal_conv1d_prefill` hottest: x[6144, 66]:bfloat16 (non-contig), weight[6144, 4]:bfloat16, bias[6144]:bfloat16, conv_states[2183, 6144, 3]:bfloat16, query_start_loc[2]:int32, cache_indices[1]:int32
  - another operating point: x[6144, 864]:bfloat16 (non-contig), weight[6144, 4]:bfloat16, bias[6144]:bfloat16, conv_states[2183, 6144, 3]:bfloat16, query_start_loc[2]:int32, cache_indices[1]:int32
- `mamba2_state_passing` hottest: states[1, 1, 64, 8192]:float32, dA_cumsum[1, 64, 1, 128]:float32, initial_states[1, 64, 8192]:float32, seq_idx[1, 66]:int32, chunk_offsets[1]:int32
  - another operating point: states[1, 7, 64, 8192]:float32, dA_cumsum[1, 64, 7, 128]:float32, seq_idx[1, 864]:int32
- `mamba2_chunk_scan` hottest: cb[1, 1, 8, 128, 128]:float32, x[1, 66, 64, 64]:bfloat16 (non-contig), dt[1, 64, 1, 128]:float32, dA_cumsum[1, 64, 1, 128]:float32, C[1, 66, 8, 128]:bfloat16 (non-contig), states[1, 1, 64, 64, 128]:float32
  - another operating point: cb[1, 7, 8, 128, 128]:float32, x[1, 864, 64, 64]:bfloat16 (non-contig), dt[1, 64, 7, 128]:float32, dA_cumsum[1, 64, 7, 128]:float32, C[1, 864, 8, 128]:bfloat16 (non-contig), states[1, 7, 64, 64, 128]:float32
- `mamba2_chunk_state_varlen` hottest: B[66, 8, 128]:bfloat16 (non-contig), x[66, 64, 64]:bfloat16 (non-contig), dt[64, 1, 128]:float32, dA_cumsum[64, 1, 128]:float32, cu_seqlens[2]:int32, chunk_states[1, 64, 64, 128]:float32
  - another operating point: B[864, 8, 128]:bfloat16 (non-contig), x[864, 64, 64]:bfloat16 (non-contig), dt[64, 7, 128]:float32, dA_cumsum[64, 7, 128]:float32, cu_seqlens[2]:int32, chunk_states[7, 64, 64, 128]:float32
- `mamba2_chunk_scan_combined_fwd` hottest: x[1, 66, 64, 64]:bfloat16 (non-contig), dt[1, 66, 64]:bfloat16 (non-contig), A[64]:float32, B[1, 66, 8, 128]:bfloat16 (non-contig), C[1, 66, 8, 128]:bfloat16 (non-contig), D[64]:bfloat16
  - another operating point: x[1, 864, 64, 64]:bfloat16 (non-contig), dt[1, 864, 64]:bfloat16 (non-contig), A[64]:float32, B[1, 864, 8, 128]:bfloat16 (non-contig), C[1, 864, 8, 128]:bfloat16 (non-contig), D[64]:bfloat16
- `mamba2_chunk_scan_combined` hottest: x[1, 66, 64, 64]:bfloat16 (non-contig), dt[1, 66, 64]:bfloat16 (non-contig), A[64]:float32, B[1, 66, 8, 128]:bfloat16 (non-contig), C[1, 66, 8, 128]:bfloat16 (non-contig), D[64]:bfloat16
  - another operating point: x[1, 864, 64, 64]:bfloat16 (non-contig), dt[1, 864, 64]:bfloat16 (non-contig), A[64]:float32, B[1, 864, 8, 128]:bfloat16 (non-contig), C[1, 864, 8, 128]:bfloat16 (non-contig), D[64]:bfloat16


Call counts are real traffic only: every call observed before a capture-group
label was active (start-up, CUDA-graph capture, autotune) is kept separately in
the `warmup_only_shapes` section of the source manifest and never enters a
workload row. See `../../docs/workload_capture.md`.

**Cross-check from the earlier cookbook-aligned torch-profiler sweep:** this kernel family is
**55.8% of total serving GPU time** (peak ShareGPT / concurrency 32; 22.7-55.8% across the six
scenarios). The Triton fused-MoE path was wrapped in the same capture and fired **0 times** on
B300 for this FP8 checkpoint - the MoE goes through a fused vendor backend, so it is not a
target for this model.

`bench/tensors/A1_conv1d_decode_chain16/` holds 16 consecutive real decode steps of
`causal_conv1d_update` (state rows before and after each step, byte-chained) - that is the
correctness oracle described in `../../docs/anti_hack_contract.md`.
