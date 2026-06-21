# LLM Kernel Task Index: kimi_k27_code / B200

- Model: `moonshotai/Kimi-K2.7-Code`
- Evidence threshold: GPU kernel name share strictly `> 2%`.
- Promotion rule: only rows with an external-id-bound non-empty torch-profiler shape are task candidates.
- Weak timestamp/nearest-preceding fallback rows are retained in audit data but are not promoted.

## Workload Coverage

| Workload | Rows | Strong | Weak | Empty shape | Status |
|---|---:|---:|---:|---:|---|
| `random_low` | 13 | 4 | 9 | 0 | partial, promote strong rows only |
| `random_mid` | 7 | 3 | 4 | 0 | partial, promote strong rows only |
| `random_high` | 11 | 3 | 8 | 0 | partial, promote strong rows only |
| `sharegpt_low` | 2 | 2 | 0 | 0 | strong |
| `sharegpt_mid` | 2 | 2 | 0 | 0 | strong |
| `sharegpt_high` | 11 | 6 | 5 | 0 | partial, promote strong rows only |

## Task Candidates

| Task id | Category | Workloads | Max % GPU | Shape samples | Kernel |
|---|---|---|---:|---:|---|
| `comm__allreduce_fusion_kernel_oneshot_lamport__b9d8384154` | `comm` | `random_low`, `random_mid`, `random_high`, `sharegpt_low`, `sharegpt_mid`, `sharegpt_high` | 48.82 | 12 | `void flashinfer::trtllm_allreduce_fusion::allreduce_fusion_kernel_oneshot_lamport<(flashinfer...` |
| `gemm__fused_a_gemm_kernel__23e7519307` | `gemm` | `sharegpt_low`, `sharegpt_high` | 47.74 | 2 | `void fused_a_gemm_kernel<1, 2112, 7168, 16, 16, 256, 12>(__nv_bfloat16*, __nv_bfloat16 const*...` |
| `gemm__fused_a_gemm_kernel__bda001cd80` | `gemm` | `sharegpt_mid` | 42.44 | 2 | `void fused_a_gemm_kernel<1, 2112, 7168, 16, 8, 256, 16>(__nv_bfloat16*, __nv_bfloat16 const*,...` |
| `quant_gemm__nvjet_sm100_tst_64x24_64x16_1x2_h_bz_splitk_tnt__a2d138c1c3` | `quant_gemm` | `random_low`, `random_mid`, `random_high` | 13.43 | 3 | `nvjet_sm100_tst_64x24_64x16_1x2_h_bz_splitK_TNT` |
| `quant_gemm__nvjet_sm100_tst_64x8_64x16_2x2_h_bz_splitk_tnt__03c74298a8` | `quant_gemm` | `random_low`, `random_mid`, `random_high`, `sharegpt_high` | 11.58 | 7 | `nvjet_sm100_tst_64x8_64x16_2x2_h_bz_splitK_TNT` |
| `quant_gemm__nvjet_sm100_tst_64x16_64x16_2x4_2cta_h_bz_splitk__6dd18c84c0` | `quant_gemm` | `sharegpt_high` | 8.16 | 2 | `nvjet_sm100_tst_64x16_64x16_2x4_2cta_h_bz_splitK_TNT` |
| `quant_gemm__nvjet_sm100_tst_64x32_64x16_2x1_2cta_v_bz_splitk__643e7d423b` | `quant_gemm` | `sharegpt_high` | 5.97 | 2 | `nvjet_sm100_tst_64x32_64x16_2x1_2cta_v_bz_splitK_TNT` |
| `quant_gemm__nvjet_sm100_tst_64x40_64x16_1x2_h_bz_splitk_tnt__45f40efe12` | `quant_gemm` | `sharegpt_high` | 2.73 | 2 | `nvjet_sm100_tst_64x40_64x16_1x2_h_bz_splitK_TNT` |
| `comm__comm__a12cdaa5b4` | `comm` | `random_low` | 2.01 | 1 | `void (anonymous namespace)::all_reduce_one_shot_push_kernel<__nv_bfloat16, 8u, true>((anonymo...` |

Full shape samples and skipped weak/empty rows are in `kernel_task_index.json`.
