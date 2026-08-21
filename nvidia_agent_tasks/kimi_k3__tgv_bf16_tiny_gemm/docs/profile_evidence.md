# Profile evidence: Kimi-K3 low-latency BF16 GEMM

| op | real calls | distinct signatures | rows kept |
| --- | ---: | ---: | ---: |
| `k3_tiny_gemm` | 433,920 | 44 | 7 |
| `k3_tiny_n_gemm_bf16` | 213,096 | 15 | 4 |
| `k3_tiny_k_gemm_bf16` | 163,416 | 11 | 11 |

## Which entry point produces which kernel

The original B300 capture also contained `cutedsl_bf16_gemm*`, which produces the
SM100-only `TgvGemmCuteExtKernel_*` family. Those entry points are excluded from the H200
task. The remaining portable path is:

* `kimi_k3_tiny_gemm` is a K3-specific **shape dispatcher**; its fast paths are
  `tiny_n_gemm_bf16` / `tiny_k_gemm_bf16`, and the kernel that appears in the profile is
  **`sglang::tiny_n_gemm_kernel<16u, 144u, 7168u, 1u, ...>` at 1.64%**. Outside its
  dispatch tables it falls through to `F.linear` (nvjet / cuBLAS), which is part of the
  25.8% 'other GEMM' block below.

## Measured GPU-time share (CUDA graphs enabled, TP8, random 1k/256 cc16)

| family | share |
| --- | ---: |
| MoE (trtllm bmm / routing / finalize) | 31.91% |
| other GEMM incl. `F.linear` fallbacks (nvjet / cuBLAS) | 25.80% |
| collectives | 14.17% |
| **TGV CuTe GEMM (`cutedsl_bf16_gemm*`)** | **7.69%** |
| quant / elementwise / norm | 5.06% |
| KDA linear attention | 3.55% |
| MLA attention | 2.80% |
| **`tiny_n_gemm_kernel` (`kimi_k3_tiny_gemm` fast path)** | **1.64%** |

Raw table: `../docs/profiles/kernel_shapes_kimi_k3_1k256_cc16.json`. The TGV measurements
remain useful capture provenance, but they are not part of the H200 benchmark or score.

## Representative shapes

- `k3_tiny_gemm`: x[1, 7168]:bfloat16, w[144, 7168]:bfloat16
- `k3_tiny_n_gemm_bf16`: x[1, 7168]:bfloat16, w[144, 7168]:bfloat16
- `k3_tiny_k_gemm_bf16`: x[1, 128]:bfloat16, w[1536, 128]:bfloat16

Call counts are real traffic only; warmup-only signatures are excluded. GSM8K accuracy
of the capture run: 1.000 at 5-shot serial and 16-shot 16-way.
