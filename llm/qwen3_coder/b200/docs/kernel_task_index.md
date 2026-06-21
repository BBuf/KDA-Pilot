# LLM Kernel Task Index: qwen3_coder / B200

- Model: `Qwen/Qwen3-Coder-480B-A35B-Instruct-FP8`
- Evidence threshold: GPU kernel name share strictly `> 2%`.
- Promotion rule: only rows with an external-id-bound non-empty torch-profiler shape are task candidates.
- Weak timestamp/nearest-preceding fallback rows are retained in audit data but are not promoted.

## Workload Coverage

| Workload | Rows | Strong | Weak | Empty shape | Status |
|---|---:|---:|---:|---:|---|
| `random_low` | 10 | 8 | 2 | 0 | partial, promote strong rows only |
| `random_mid` | 9 | 4 | 5 | 0 | partial, promote strong rows only |
| `random_high` | 13 | 7 | 6 | 0 | partial, promote strong rows only |
| `sharegpt_low` | 11 | 3 | 8 | 0 | partial, promote strong rows only |
| `sharegpt_mid` | 14 | 9 | 5 | 0 | partial, promote strong rows only |
| `sharegpt_high` | 13 | 7 | 6 | 0 | partial, promote strong rows only |

## Task Candidates

| Task id | Category | Workloads | Max % GPU | Shape samples | Kernel |
|---|---|---|---:|---:|---|
| `comm__allreduce_fusion_kernel_oneshot_lamport__b9d8384154` | `comm` | `random_low`, `random_high`, `sharegpt_low`, `sharegpt_mid`, `sharegpt_high` | 22.61 | 8 | `void flashinfer::trtllm_allreduce_fusion::allreduce_fusion_kernel_oneshot_lamport<(flashinfer...` |
| `comm__nccldevkernel_allreduce_sum_bf16_ring_ll__05a3ee6241` | `comm` | `random_mid`, `sharegpt_mid` | 16.30 | 3 | `ncclDevKernel_AllReduce_Sum_bf16_RING_LL(ncclDevKernelArgsStorage<4096ul>)` |
| `quant_gemm__bmm_e4m3_e4m3e4m3_fp32_t128x32x128u2_s6_et64x32__b94ba45f4c` | `quant_gemm` | `sharegpt_high` | 11.82 | 1 | `bmm_E4m3_E4m3E4m3_Fp32_t128x32x128u2_s6_et64x32_m64x32x32_c1x1x1_rM_TN_transOut_noShfl_dsFp8_...` |
| `quant_gemm__sm100_fp8_fp4_gemm_1d1d_impl__1b5539080f` | `quant_gemm` | `random_low` | 10.57 | 1 | `void deep_gemm::sm100_fp8_fp4_gemm_1d1d_impl<(cute::UMMA::Major)0, (cute::UMMA::Major)0, 128u...` |
| `moe__activationdeepseekkernel__b7453c53aa` | `moe` | `random_mid`, `random_high`, `sharegpt_mid` | 10.56 | 3 | `void moe::dev::activation::activationDeepSeekKernel<moe::dev::activation::KernelParams<cutlas...` |
| `quant_gemm__bmm_e4m3_e4m3e4m3_fp32_t128x64x128u2_s6_et64x64__046d851f0c` | `quant_gemm` | `random_mid`, `sharegpt_mid` | 10.35 | 2 | `bmm_E4m3_E4m3E4m3_Fp32_t128x64x128u2_s6_et64x64_m64x64x32_c1x1x1_rM_TN_transOut_noShfl_dsFp8_...` |
| `comm__allreduce_fusion_kernel_twoshot_sync__c36567c3ee` | `comm` | `random_high`, `sharegpt_high` | 9.21 | 3 | `void flashinfer::trtllm_allreduce_fusion::allreduce_fusion_kernel_twoshot_sync<(flashinfer::t...` |
| `quant_gemm__nvjet_sm100_tst_32x64_64x16_4x1_v_bz_splitk_tnn__0fa651efdd` | `quant_gemm` | `random_low`, `sharegpt_mid` | 7.55 | 2 | `nvjet_sm100_tst_32x64_64x16_4x1_v_bz_splitK_TNN` |
| `quant_gemm__bmm_e4m3_e4m3e4m3_fp32_t128x128x128u2_s5_et64x12__9b5b17030b` | `quant_gemm` | `random_high`, `sharegpt_mid` | 5.78 | 2 | `bmm_E4m3_E4m3E4m3_Fp32_t128x128x128u2_s5_et64x128_m64x128x32_c1x1x1_rM_TN_transOut_noShfl_dsF...` |
| `quant_gemm__bmm_bfloat16_e4m3e4m3_fp32_t128x32x128u2_s6_et64__c89f39b356` | `quant_gemm` | `sharegpt_high` | 5.70 | 1 | `bmm_Bfloat16_E4m3E4m3_Fp32_t128x32x128u2_s6_et64x32_m64x32x32_c1x1x1_rM_TN_transOut_noShfl_ds...` |
| `quant_gemm__bmm_bfloat16_e4m3e4m3_fp32_t128x64x128u2_s6_et64__4becbe9f88` | `quant_gemm` | `random_mid`, `sharegpt_mid` | 5.11 | 2 | `bmm_Bfloat16_E4m3E4m3_Fp32_t128x64x128u2_s6_et64x64_m64x64x32_c1x1x1_rM_TN_transOut_noShfl_ds...` |
| `attention__fmhasm100fkernel_qkvbfloat16obfloat16h128pagedkv__568b7763f6` | `attention` | `random_high`, `sharegpt_mid`, `sharegpt_high` | 4.66 | 9 | `fmhaSm100fKernel_QkvBfloat16OBfloat16H128PagedKvCausalP32VarSeqQ128Kv128PersistentContext` |
| `quant_gemm__bmm_e4m3_e4m3e4m3_fp32_t128x16x128u2_s6_et64x16__ce0096e802` | `quant_gemm` | `random_low` | 4.50 | 1 | `bmm_E4m3_E4m3E4m3_Fp32_t128x16x128u2_s6_et64x16_m64x16x32_c1x1x1_rM_TN_transOut_noShfl_dsFp8_...` |
| `quant_gemm__bmm_e4m3_e4m3e4m3_fp32_t128x8x128u2_s8_et64x8_m6__499a6a5a0c` | `quant_gemm` | `sharegpt_low` | 3.41 | 1 | `bmm_E4m3_E4m3E4m3_Fp32_t128x8x128u2_s8_et64x8_m64x8x32_c1x1x1_rM_TN_transOut_noShfl_dsFp8_sch...` |
| `quant_gemm__bmm_bfloat16_e4m3e4m3_fp32_t128x16x128u2_s6_et64__227f208451` | `quant_gemm` | `random_low` | 2.73 | 1 | `bmm_Bfloat16_E4m3E4m3_Fp32_t128x16x128u2_s6_et64x16_m64x16x32_c1x1x1_rM_TN_transOut_noShfl_ds...` |
| `moe__finalizekernel__6a7a068b8f` | `moe` | `random_low`, `sharegpt_low` | 2.57 | 2 | `void moe::dev::finalize::finalizeKernel<moe::dev::finalize::KernelParams<cutlass::bfloat16_t,...` |
| `quant_gemm__bmm_bfloat16_e4m3e4m3_fp32_t128x128x128u2_s5_et6__fa74e90124` | `quant_gemm` | `random_high`, `sharegpt_mid` | 2.51 | 2 | `bmm_Bfloat16_E4m3E4m3_Fp32_t128x128x128u2_s5_et64x128_m64x128x32_c1x1x1_rM_TN_transOut_noShfl...` |
| `moe__finalizekernelvecload__00edba12eb` | `moe` | `random_high` | 2.42 | 1 | `void moe::dev::finalize::finalizeKernelVecLoad<moe::dev::finalize::KernelParams<cutlass::bflo...` |
| `comm__comm__c330990d60` | `comm` | `sharegpt_high` | 2.24 | 2 | `void (anonymous namespace)::all_reduce_two_shot_kernel<__nv_bfloat16, 8u, true>(host::distrib...` |
| `moe__activationdeepseekkernel__215271b2b9` | `moe` | `random_low` | 2.21 | 1 | `void moe::dev::activation::activationDeepSeekKernel<moe::dev::activation::KernelParams<cutlas...` |
| `moe__routingindicesblockkernel__76644116ce` | `moe` | `random_low` | 2.17 | 1 | `void moe::dev::routing::routingCustom::routingIndicesBlockKernel<moe::dev::routing::routingCu...` |
| `quant_gemm__bmm_e4m3_e4m3e4m3_fp32_t128x64x128u2_s6_et64x64__584406dfb2` | `quant_gemm` | `sharegpt_high` | 2.05 | 1 | `bmm_E4m3_E4m3E4m3_Fp32_t128x64x128u2_s6_et64x64_m64x64x32_c1x1x1_rM_TN_transOut_noShfl_dsFp8_...` |

Full shape samples and skipped weak/empty rows are in `kernel_task_index.json`.
