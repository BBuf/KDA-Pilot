# LLM Kernel Task Index: kimi_k25 / B200

- Model: `moonshotai/Kimi-K2.5`
- Evidence threshold: GPU kernel name share strictly `> 2%`.
- Promotion rule: only rows with an external-id-bound non-empty torch-profiler shape are task candidates.
- Weak timestamp/nearest-preceding fallback rows are retained in audit data but are not promoted.

## Workload Coverage

| Workload | Rows | Strong | Weak | Empty shape | Status |
|---|---:|---:|---:|---:|---|
| `random_low` | 9 | 3 | 6 | 0 | partial, promote strong rows only |
| `random_mid` | 7 | 3 | 4 | 0 | partial, promote strong rows only |
| `random_high` | 10 | 3 | 7 | 0 | partial, promote strong rows only |
| `sharegpt_low` | 8 | 2 | 6 | 0 | partial, promote strong rows only |
| `sharegpt_mid` | 3 | 3 | 0 | 0 | strong |
| `sharegpt_high` | 9 | 6 | 3 | 0 | partial, promote strong rows only |

## Task Candidates

| Task id | Category | Workloads | Max % GPU | Shape samples | Kernel |
|---|---|---|---:|---:|---|
| `comm__allreduce_fusion_kernel_oneshot_lamport__b9d8384154` | `comm` | `random_low`, `random_mid`, `random_high`, `sharegpt_low`, `sharegpt_mid`, `sharegpt_high` | 41.24 | 12 | `void flashinfer::trtllm_allreduce_fusion::allreduce_fusion_kernel_oneshot_lamport<(flashinfer...` |
| `gemm__fused_a_gemm_kernel__bda001cd80` | `gemm` | `sharegpt_mid` | 31.31 | 1 | `void fused_a_gemm_kernel<1, 2112, 7168, 16, 8, 256, 16>(__nv_bfloat16*, __nv_bfloat16 const*,...` |
| `gemm__fused_a_gemm_kernel__23e7519307` | `gemm` | `sharegpt_low`, `sharegpt_mid`, `sharegpt_high` | 19.70 | 4 | `void fused_a_gemm_kernel<1, 2112, 7168, 16, 16, 256, 12>(__nv_bfloat16*, __nv_bfloat16 const*...` |
| `quant_gemm__nvjet_sm100_tst_64x24_64x16_1x2_h_bz_splitk_tnt__a2d138c1c3` | `quant_gemm` | `random_low`, `random_mid`, `random_high` | 16.85 | 4 | `nvjet_sm100_tst_64x24_64x16_1x2_h_bz_splitK_TNT` |
| `quant_gemm__nvjet_sm100_tst_64x8_64x16_2x2_h_bz_splitk_tnt__03c74298a8` | `quant_gemm` | `random_low`, `random_mid`, `random_high`, `sharegpt_high` | 12.90 | 7 | `nvjet_sm100_tst_64x8_64x16_2x2_h_bz_splitK_TNT` |
| `quant_gemm__nvjet_sm100_tst_64x16_64x16_2x4_2cta_h_bz_splitk__6dd18c84c0` | `quant_gemm` | `sharegpt_high` | 8.78 | 2 | `nvjet_sm100_tst_64x16_64x16_2x4_2cta_h_bz_splitK_TNT` |
| `quant_gemm__nvjet_sm100_tst_64x32_64x16_2x1_2cta_v_bz_splitk__643e7d423b` | `quant_gemm` | `sharegpt_high` | 8.40 | 4 | `nvjet_sm100_tst_64x32_64x16_2x1_2cta_v_bz_splitK_TNT` |
| `quant_gemm__nvjet_sm100_tst_64x40_64x16_1x2_h_bz_splitk_tnt__45f40efe12` | `quant_gemm` | `sharegpt_high` | 4.08 | 2 | `nvjet_sm100_tst_64x40_64x16_1x2_h_bz_splitK_TNT` |

Full shape samples and skipped weak/empty rows are in `kernel_task_index.json`.
