# Profile evidence: kimi_k3__tgv_bf16_tiny_gemm

| op | real calls | distinct signatures | rows kept |
| --- | ---: | ---: | ---: |
| `k3_tiny_gemm` | 627,088 | 96 | 13 |

Representative shapes (hottest row per op):

- `k3_tiny_gemm`: x[1, 7168]:bfloat16, w[144, 7168]:bfloat16

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
