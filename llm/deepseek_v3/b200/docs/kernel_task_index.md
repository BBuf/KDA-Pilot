# LLM Kernel Task Index: deepseek_v3 / B200

- Model: `deepseek-ai/DeepSeek-V3`
- Evidence threshold: GPU kernel name share strictly `> 2%`.
- Promotion rule: only rows with an external-id-bound non-empty torch-profiler shape are task candidates.
- Weak timestamp/nearest-preceding fallback rows are retained in audit data but are not promoted.

## Workload Coverage

| Workload | Rows | Strong | Weak | Empty shape | Status |
|---|---:|---:|---:|---:|---|
| `random_low` | 6 | 4 | 2 | 0 | partial, promote strong rows only |
| `random_mid` | 6 | 4 | 2 | 0 | partial, promote strong rows only |
| `random_high` | 6 | 5 | 1 | 0 | partial, promote strong rows only |
| `sharegpt_low` | 7 | 5 | 2 | 0 | partial, promote strong rows only |
| `sharegpt_mid` | 6 | 4 | 2 | 0 | partial, promote strong rows only |
| `sharegpt_high` | 7 | 7 | 0 | 0 | strong |

## Task Candidates

| Task id | Category | Workloads | Max % GPU | Shape samples | Kernel |
|---|---|---|---:|---:|---|
| `comm__allreduce_fusion_kernel_oneshot_lamport__b9d8384154` | `comm` | `random_low`, `random_mid`, `random_high`, `sharegpt_low`, `sharegpt_mid`, `sharegpt_high` | 35.03 | 11 | `void flashinfer::trtllm_allreduce_fusion::allreduce_fusion_kernel_oneshot_lamport<(flashinfer...` |
| `comm__allreduce_fusion_kernel_twoshot_sync__c36567c3ee` | `comm` | `random_high`, `sharegpt_high` | 16.61 | 4 | `void flashinfer::trtllm_allreduce_fusion::allreduce_fusion_kernel_twoshot_sync<(flashinfer::t...` |
| `quant_gemm__nvjet_sm100_tst_64x8_64x16_1x4_h_bz_splitk_tnt__5a2ad7d133` | `quant_gemm` | `random_low`, `random_mid`, `random_high`, `sharegpt_high` | 14.14 | 3 | `nvjet_sm100_tst_64x8_64x16_1x4_h_bz_splitK_TNT` |
| `gemm__router_gemm_kernel__ee9078b477` | `gemm` | `sharegpt_low`, `sharegpt_mid`, `sharegpt_high` | 14.12 | 3 | `void flashinfer::trtllm_dsv3_router_gemm::router_gemm_kernel<__nv_bfloat16, float, 128, 8, 16...` |
| `quant_gemm__bmm_e4m3_e4m3e4m3_fp32_t128x32x128u2_s6_et64x32__b94ba45f4c` | `quant_gemm` | `random_high`, `sharegpt_high` | 11.24 | 3 | `bmm_E4m3_E4m3E4m3_Fp32_t128x32x128u2_s6_et64x32_m64x32x32_c1x1x1_rM_TN_transOut_noShfl_dsFp8_...` |
| `gemm__router_gemm_kernel__11c0c72e30` | `gemm` | `sharegpt_mid` | 7.28 | 2 | `void flashinfer::trtllm_dsv3_router_gemm::router_gemm_kernel<__nv_bfloat16, float, 128, 8, 6,...` |
| `quant_gemm__nvjet_sm100_tst_64x8_64x16_2x4_h_bz_splitk_tnt__9c371f4925` | `quant_gemm` | `sharegpt_high` | 6.03 | 2 | `nvjet_sm100_tst_64x8_64x16_2x4_h_bz_splitK_TNT` |
| `quant_gemm__bmm_bfloat16_e4m3e4m3_fp32_t128x32x128u2_s6_et64__c89f39b356` | `quant_gemm` | `random_high`, `sharegpt_high` | 5.18 | 3 | `bmm_Bfloat16_E4m3E4m3_Fp32_t128x32x128u2_s6_et64x32_m64x32x32_c1x1x1_rM_TN_transOut_noShfl_ds...` |
| `quant_gemm__bmm_e4m3_e4m3e4m3_fp32_t128x64x128u2_s6_et64x64__046d851f0c` | `quant_gemm` | `random_mid`, `sharegpt_mid` | 4.54 | 2 | `bmm_E4m3_E4m3E4m3_Fp32_t128x64x128u2_s6_et64x64_m64x64x32_c1x1x1_rM_TN_transOut_noShfl_dsFp8_...` |
| `quant_gemm__bmm_bfloat16_e4m3e4m3_fp32_t128x64x128u2_s6_et64__4becbe9f88` | `quant_gemm` | `random_mid` | 3.84 | 1 | `bmm_Bfloat16_E4m3E4m3_Fp32_t128x64x128u2_s6_et64x64_m64x64x32_c1x1x1_rM_TN_transOut_noShfl_ds...` |
| `quant_gemm__bmm_bfloat16_e4m3e4m3_fp32_t128x8x128u2_s8_et64x__a76a258cda` | `quant_gemm` | `random_low`, `sharegpt_low` | 2.45 | 4 | `bmm_Bfloat16_E4m3E4m3_Fp32_t128x8x128u2_s8_et64x8_m64x8x32_c1x1x1_rM_TN_transOut_noShfl_dsFp8...` |
| `comm__comm__a12cdaa5b4` | `comm` | `random_low`, `sharegpt_low` | 2.06 | 2 | `void (anonymous namespace)::all_reduce_one_shot_push_kernel<__nv_bfloat16, 8u, true>((anonymo...` |
| `quant_gemm__bmm_e4m3_e4m3e4m3_fp32_t128x8x128u2_s8_et64x8_m6__1a03d7854b` | `quant_gemm` | `sharegpt_low` | 2.00 | 2 | `bmm_E4m3_E4m3E4m3_Fp32_t128x8x128u2_s8_et64x8_m64x8x32_c1x1x1_rM_TN_transOut_noShfl_dsFp8_sch...` |

Full shape samples and skipped weak/empty rows are in `kernel_task_index.json`.
