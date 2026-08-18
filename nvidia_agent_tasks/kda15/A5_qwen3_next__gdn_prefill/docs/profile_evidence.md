# Profile evidence: GDN chunk prefill (Qwen3-Next-80B-A3B)

| op | real calls | distinct signatures | rows kept |
| --- | ---: | ---: | ---: |
| `gdn_recompute_w_u` | 3744 | 13 | 11 |
| `gdn_chunk_delta_h` | 3744 | 13 | 11 |
| `gdn_chunk_o` | 3744 | 13 | 11 |
| `gdn_chunk_prefill` | 3744 | 13 | 11 |

Representative shapes:

- `gdn_recompute_w_u`: k[1, 103, 2, 128]:bfloat16, v[1, 103, 4, 128]:bfloat16, beta[1, 103, 4]:float32, g_cumsum[1, 103, 4]:float32, A[1, 103, 4, 64]:bfloat16, cu_seqlens[2]:int32, chunk_indices[2, 2]:int32
- `gdn_chunk_delta_h`: k[1, 103, 2, 128]:bfloat16, w[1, 103, 4, 128]:bfloat16, u[1, 103, 4, 128]:bfloat16, g[1, 103, 4]:float32, initial_state[10715, 4, 128, 128]:float32, initial_state_indices[1]:int32, cu_seqlens[2]:int32, chunk_indices[2, 2]:int32
- `gdn_chunk_o`: q[1, 103, 2, 128]:bfloat16, k[1, 103, 2, 128]:bfloat16, v[1, 103, 4, 128]:bfloat16, h[1, 2, 4, 128, 128]:bfloat16, g[1, 103, 4]:float32, cu_seqlens[2]:int32
- `gdn_chunk_prefill`: q[1, 103, 2, 128]:bfloat16, k[1, 103, 2, 128]:bfloat16, v[1, 103, 4, 128]:bfloat16, g[1, 103, 4]:float32, beta[1, 103, 4]:float32, initial_state[10715, 4, 128, 128]:float32, initial_state_indices[1]:int32, cu_seqlens[2]:int32, chunk_indices[2, 2]:int32

Read `capture_provenance.md` for the two findings that shape this task: the FLA
Triton chunk path is live on B300 while the FLA *recurrent decode* path is not, and
the synthetic-output groups were replaced by real GSM8K groups on this model.
