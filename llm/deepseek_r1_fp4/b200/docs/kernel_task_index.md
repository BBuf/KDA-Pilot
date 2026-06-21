# LLM Kernel Task Index: deepseek_r1_fp4 / B200

- Model: `nvidia/DeepSeek-R1-0528-FP4-v2`
- Evidence threshold: GPU kernel name share strictly `> 2%`.
- Promotion rule: only rows with an external-id-bound non-empty torch-profiler shape are task candidates.
- Weak timestamp/nearest-preceding fallback rows are retained in audit data but are not promoted.

## Workload Coverage

| Workload | Rows | Strong | Weak | Empty shape | Status |
|---|---:|---:|---:|---:|---|
| `random_low` | 6 | 3 | 3 | 0 | partial, promote strong rows only |
| `random_mid` | 8 | 3 | 5 | 0 | partial, promote strong rows only |
| `random_high` | 10 | 4 | 6 | 0 | partial, promote strong rows only |
| `sharegpt_low` | 7 | 3 | 4 | 0 | partial, promote strong rows only |
| `sharegpt_mid` | 12 | 6 | 6 | 0 | partial, promote strong rows only |
| `sharegpt_high` | 9 | 7 | 2 | 0 | partial, promote strong rows only |

## Task Candidates

| Task id | Category | Workloads | Max % GPU | Shape samples | Kernel |
|---|---|---|---:|---:|---|
| `comm__allreduce_fusion_kernel_oneshot_lamport__b9d8384154` | `comm` | `random_low`, `random_mid`, `random_high`, `sharegpt_low`, `sharegpt_mid`, `sharegpt_high` | 34.50 | 11 | `void flashinfer::trtllm_allreduce_fusion::allreduce_fusion_kernel_oneshot_lamport<(flashinfer...` |
| `quant_gemm__nvjet_sm100_tst_64x8_64x16_1x4_h_bz_splitk_tnt__5a2ad7d133` | `quant_gemm` | `random_low`, `random_mid`, `random_high` | 18.41 | 3 | `nvjet_sm100_tst_64x8_64x16_1x4_h_bz_splitK_TNT` |
| `gemm__router_gemm_kernel__ee9078b477` | `gemm` | `sharegpt_low`, `sharegpt_mid`, `sharegpt_high` | 17.09 | 3 | `void flashinfer::trtllm_dsv3_router_gemm::router_gemm_kernel<__nv_bfloat16, float, 128, 8, 16...` |
| `quant_gemm__nvjet_sm100_tst_64x24_64x16_1x2_h_bz_splitk_tnt__a2d138c1c3` | `quant_gemm` | `random_low`, `random_mid`, `random_high` | 11.11 | 2 | `nvjet_sm100_tst_64x24_64x16_1x2_h_bz_splitK_TNT` |
| `gemm__fused_a_gemm_kernel__23e7519307` | `gemm` | `sharegpt_low`, `sharegpt_mid`, `sharegpt_high` | 10.78 | 3 | `void fused_a_gemm_kernel<1, 2112, 7168, 16, 16, 256, 12>(__nv_bfloat16*, __nv_bfloat16 const*...` |
| `comm__allreduce_fusion_kernel_twoshot_sync__c36567c3ee` | `comm` | `random_high`, `sharegpt_high` | 10.16 | 6 | `void flashinfer::trtllm_allreduce_fusion::allreduce_fusion_kernel_twoshot_sync<(flashinfer::t...` |
| `gemm__router_gemm_kernel__11c0c72e30` | `gemm` | `sharegpt_mid` | 6.91 | 2 | `void flashinfer::trtllm_dsv3_router_gemm::router_gemm_kernel<__nv_bfloat16, float, 128, 8, 6,...` |
| `quant_gemm__nvjet_sm100_tst_64x8_64x16_2x4_h_bz_splitk_tnt__9c371f4925` | `quant_gemm` | `sharegpt_high` | 5.18 | 2 | `nvjet_sm100_tst_64x8_64x16_2x4_h_bz_splitK_TNT` |
| `gemm__fused_a_gemm_kernel__bda001cd80` | `gemm` | `sharegpt_mid` | 3.50 | 2 | `void fused_a_gemm_kernel<1, 2112, 7168, 16, 8, 256, 16>(__nv_bfloat16*, __nv_bfloat16 const*,...` |
| `quant_gemm__nvjet_sm100_tst_64x16_64x16_1x2_h_bz_splitk_tnt__9b5d3e2ac1` | `quant_gemm` | `sharegpt_high` | 3.44 | 2 | `nvjet_sm100_tst_64x16_64x16_1x2_h_bz_splitK_TNT` |
| `quant_gemm__nvjet_sm100_tst_64x40_64x16_1x2_h_bz_splitk_tnt__45f40efe12` | `quant_gemm` | `sharegpt_mid`, `sharegpt_high` | 3.31 | 4 | `nvjet_sm100_tst_64x40_64x16_1x2_h_bz_splitK_TNT` |

Full shape samples and skipped weak/empty rows are in `kernel_task_index.json`.
