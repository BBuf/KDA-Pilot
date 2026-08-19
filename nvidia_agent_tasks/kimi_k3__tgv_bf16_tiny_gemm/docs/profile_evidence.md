# Profile evidence: Kimi-K3 low-latency BF16 GEMM

| op | real calls | distinct signatures | rows kept |
| --- | ---: | ---: | ---: |
| `k3_cutedsl_tgv_bf16_gemm_out` | 571,784 | 21 | 11 |
| `k3_tiny_gemm` | 433,920 | 44 | 11 |
| `k3_cutedsl_tgv_bf16_gemm` | 244,624 | 36 | 11 |
| `k3_tiny_n_gemm_bf16` | 213,096 | 15 | 10 |
| `k3_tiny_k_gemm_bf16` | 163,416 | 11 | 10 |

## Which entry point produces which kernel

These two are easy to conflate - both are 'the K3 bf16 GEMM' - so the profile splits them:

* `cutedsl_bf16_gemm` / `cutedsl_bf16_gemm_out` produce the **`TgvGemmCuteExtKernel_*`**
  kernels: **7.69%** of GPU time (4.99% + 2.70% for the two cta variants). Dispatch is
  `use_cutedsl_bf16_gemm(m, n, k)` in `srt/layers/quantization/unquant.py`.
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

Raw table: `../docs/profiles/kernel_shapes_kimi_k3_1k256_cc16.json`. At **batch 1** the
TGV share rises to **41.2%** - same kernel, different denominator - which is the regime
K3 low-latency serving targets and the reason this path exists.

## Representative shapes

- `k3_cutedsl_tgv_bf16_gemm_out`: x[1, 1536]:bfloat16, weight[7168, 1536]:bfloat16, out[1, 7168]:bfloat16
- `k3_tiny_gemm`: x[1, 7168]:bfloat16, w[144, 7168]:bfloat16
- `k3_cutedsl_tgv_bf16_gemm`: x[1, 7168]:bfloat16, weight[6144, 7168]:bfloat16
- `k3_tiny_n_gemm_bf16`: x[1, 7168]:bfloat16, w[144, 7168]:bfloat16
- `k3_tiny_k_gemm_bf16`: x[1, 128]:bfloat16, w[1536, 128]:bfloat16

Call counts are real traffic only; warmup-only signatures are excluded. GSM8K accuracy
of the capture run: 1.000 at 5-shot serial and 16-shot 16-way.
