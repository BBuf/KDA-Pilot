# Profile evidence: kimi_k3__kda_linear_attention

| op | real calls | distinct signatures | rows kept |
| --- | ---: | ---: | ---: |
| `k3_kda_fused_decode` | 308,024 | 38 | 10 |
| `k3_kda_chunk_prefill` | 5,520 | 10 | 9 |

Representative shapes (hottest row per op):

- `k3_kda_fused_decode`: mixed_qkv[1, 4608]:bfloat16, a[1, 1536]:bfloat16, b[1, 12]:bfloat16, conv_states[274, 3, 4608]:bfloat16, w_q_t[4, 1536]:float32, w_k_t[4, 1536]:float32, w_v_t[4, 1536]:float32, conv_bias[4608]:float32, A_log[12]:float32, dt_bias[1536]:float32, onorm_g[1, 1536]:bfloat16, onorm_weight[128]:float32, ssm_states[274, 12, 12
- `k3_kda_chunk_prefill`: q[1, 730, 12, 128]:bfloat16, k[1, 730, 12, 128]:bfloat16, v[1, 730, 12, 128]:bfloat16, g[1, 730, 12, 128]:bfloat16, beta[1, 730, 12]:float32, initial_state[274, 12, 128, 128]:float32, initial_state_indices[1]:int32, cu_seqlens[2]:int32, A_log[1, 1, 12, 1]:float32, dt_bias[1536]:float32

## Measured GPU-time share (CUDA graphs enabled, TP8, random 1k/256 cc16)

| family | share |
| --- | ---: |
| MoE (trtllm bmm / routing / finalize) | 31.91% |
| other GEMM (nvjet / cublas / tiny_n_gemm) | 25.80% |
| collectives (sglang all-reduce family) | 14.17% |
| **TGV bf16 GEMM (`kimi_k3_tiny_gemm`)** | **7.69%** |
| quant / elementwise / norm | 5.06% |
| **KDA linear attention (decode + prefill + conv1d)** | **3.55%** |
| MLA attention | 2.80% |

Raw table: `../docs/profiles/kernel_shapes_kimi_k3_1k256_cc16.json`. Note the operating
point: at **batch 1**, which is the regime Kimi-K3 low-latency serving targets, the TGV
GEMM share rises to **41.2%** - the same kernel, a different denominator. Both numbers are
real; tune against the shipped rows, which span T = 1 to 16,143.
