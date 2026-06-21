# LLM Kernel Task Index: glm_51 / B200

- Model: `zai-org/GLM-5.1-FP8`
- Evidence threshold: GPU kernel name share strictly `> 2%`.
- Promotion rule: only rows with an external-id-bound non-empty torch-profiler shape are task candidates.
- Weak timestamp/nearest-preceding fallback rows are retained in audit data but are not promoted.

## Workload Coverage

| Workload | Rows | Strong | Weak | Empty shape | Status |
|---|---:|---:|---:|---:|---|
| `random_low` | 5 | 4 | 1 | 0 | partial, promote strong rows only |
| `random_mid` | 7 | 5 | 2 | 0 | partial, promote strong rows only |
| `random_high` | 5 | 3 | 2 | 0 | partial, promote strong rows only |
| `sharegpt_low` | 4 | 3 | 1 | 0 | partial, promote strong rows only |
| `sharegpt_mid` | 5 | 2 | 3 | 0 | partial, promote strong rows only |
| `sharegpt_high` | 5 | 4 | 1 | 0 | partial, promote strong rows only |

## Task Candidates

| Task id | Category | Workloads | Max % GPU | Shape samples | Kernel |
|---|---|---|---:|---:|---|
| `comm__allreduce_fusion_kernel_oneshot_lamport__b9d8384154` | `comm` | `random_low`, `random_mid`, `random_high`, `sharegpt_low`, `sharegpt_mid`, `sharegpt_high` | 36.73 | 10 | `void flashinfer::trtllm_allreduce_fusion::allreduce_fusion_kernel_oneshot_lamport<(flashinfer...` |
| `quant_gemm__nvjet_sm100_tst_32x64_64x16_4x1_v_bz_splitk_tnn__0fa651efdd` | `quant_gemm` | `sharegpt_low`, `sharegpt_mid`, `sharegpt_high` | 18.18 | 4 | `nvjet_sm100_tst_32x64_64x16_4x1_v_bz_splitK_TNN` |
| `quant_gemm__nvjet_sm100_tst_64x8_64x16_2x4_h_bz_splitk_tnt__9c371f4925` | `quant_gemm` | `random_low`, `random_mid`, `random_high`, `sharegpt_high` | 16.68 | 5 | `nvjet_sm100_tst_64x8_64x16_2x4_h_bz_splitK_TNT` |
| `comm__allreduce_fusion_kernel_twoshot_sync__c36567c3ee` | `comm` | `random_high`, `sharegpt_high` | 15.77 | 5 | `void flashinfer::trtllm_allreduce_fusion::allreduce_fusion_kernel_twoshot_sync<(flashinfer::t...` |
| `quant_gemm__bmm_e4m3_e4m3e4m3_fp32_t128x64x128u2_s6_et64x64__046d851f0c` | `quant_gemm` | `random_mid` | 4.75 | 2 | `bmm_E4m3_E4m3E4m3_Fp32_t128x64x128u2_s6_et64x64_m64x64x32_c1x1x1_rM_TN_transOut_noShfl_dsFp8_...` |
| `quant_gemm__bmm_bfloat16_e4m3e4m3_fp32_t128x64x128u2_s6_et64__4becbe9f88` | `quant_gemm` | `random_mid` | 3.95 | 1 | `bmm_Bfloat16_E4m3E4m3_Fp32_t128x64x128u2_s6_et64x64_m64x64x32_c1x1x1_rM_TN_transOut_noShfl_ds...` |
| `quant_gemm__sm100_fp8_fp4_gemm_1d1d_impl__1b5539080f` | `quant_gemm` | `random_low`, `sharegpt_low` | 3.87 | 2 | `void deep_gemm::sm100_fp8_fp4_gemm_1d1d_impl<(cute::UMMA::Major)0, (cute::UMMA::Major)0, 128u...` |
| `comm__comm__c330990d60` | `comm` | `random_mid` | 2.78 | 2 | `void (anonymous namespace)::all_reduce_two_shot_kernel<__nv_bfloat16, 8u, true>(host::distrib...` |
| `quant_gemm__bmm_bfloat16_e4m3e4m3_fp32_t128x8x128u2_s8_et64x__a76a258cda` | `quant_gemm` | `random_low` | 2.13 | 2 | `bmm_Bfloat16_E4m3E4m3_Fp32_t128x8x128u2_s8_et64x8_m64x8x32_c1x1x1_rM_TN_transOut_noShfl_dsFp8...` |

Full shape samples and skipped weak/empty rows are in `kernel_task_index.json`.
