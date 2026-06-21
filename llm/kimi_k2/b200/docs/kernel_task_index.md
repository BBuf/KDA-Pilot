# LLM Kernel Task Index: kimi_k2 / B200

- Model: `moonshotai/Kimi-K2-Instruct`
- Evidence threshold: GPU kernel name share strictly `> 2%`.
- Promotion rule: only rows with an external-id-bound non-empty torch-profiler shape are task candidates.
- Weak timestamp/nearest-preceding fallback rows are retained in audit data but are not promoted.

## Workload Coverage

| Workload | Rows | Strong | Weak | Empty shape | Status |
|---|---:|---:|---:|---:|---|
| `random_low` | 10 | 4 | 6 | 0 | partial, promote strong rows only |
| `random_mid` | 7 | 5 | 2 | 0 | partial, promote strong rows only |
| `random_high` | 8 | 2 | 6 | 0 | partial, promote strong rows only |
| `sharegpt_low` | 11 | 0 | 11 | 0 | weak/empty only, do not promote |
| `sharegpt_mid` | 11 | 4 | 7 | 0 | partial, promote strong rows only |
| `sharegpt_high` | 12 | 1 | 11 | 0 | partial, promote strong rows only |

## Task Candidates

| Task id | Category | Workloads | Max % GPU | Shape samples | Kernel |
|---|---|---|---:|---:|---|
| `quant_gemm__sm100_fp8_fp4_gemm_1d1d_impl__1b5539080f` | `quant_gemm` | `random_low` | 13.49 | 1 | `void deep_gemm::sm100_fp8_fp4_gemm_1d1d_impl<(cute::UMMA::Major)0, (cute::UMMA::Major)0, 128u...` |
| `quant_gemm__per_token_group_quant_8bit_kernel__cd3c819d72` | `quant_gemm` | `random_low`, `random_mid`, `sharegpt_mid` | 12.64 | 4 | `void per_token_group_quant_8bit_kernel<NaiveScheduler, 128, 8, __nv_bfloat16, c10::Float8_e4m...` |
| `comm__allreduce_fusion_kernel_oneshot_lamport__b9d8384154` | `comm` | `random_low` | 11.11 | 1 | `void flashinfer::trtllm_allreduce_fusion::allreduce_fusion_kernel_oneshot_lamport<(flashinfer...` |
| `quant_gemm__bmm_e4m3_e4m3e4m3_fp32_t128x64x128u2_s6_et64x64__046d851f0c` | `quant_gemm` | `random_mid`, `sharegpt_mid` | 11.04 | 2 | `bmm_E4m3_E4m3E4m3_Fp32_t128x64x128u2_s6_et64x64_m64x64x32_c1x1x1_rM_TN_transOut_noShfl_dsFp8_...` |
| `quant_gemm__sm100_fp8_fp4_gemm_1d1d_impl__45bdd89e95` | `quant_gemm` | `random_mid` | 9.81 | 1 | `void deep_gemm::sm100_fp8_fp4_gemm_1d1d_impl<(cute::UMMA::Major)0, (cute::UMMA::Major)0, 128u...` |
| `quant_gemm__bmm_bfloat16_e4m3e4m3_fp32_t128x64x128u2_s6_et64__4becbe9f88` | `quant_gemm` | `random_mid`, `sharegpt_mid` | 7.39 | 2 | `bmm_Bfloat16_E4m3E4m3_Fp32_t128x64x128u2_s6_et64x64_m64x64x32_c1x1x1_rM_TN_transOut_noShfl_ds...` |
| `quant_gemm__bmm_bfloat16_e4m3e4m3_fp32_t128x32x128u2_s6_et64__c89f39b356` | `quant_gemm` | `random_high` | 6.40 | 1 | `bmm_Bfloat16_E4m3E4m3_Fp32_t128x32x128u2_s6_et64x32_m64x32x32_c1x1x1_rM_TN_transOut_noShfl_ds...` |
| `quant_gemm__bmm_e4m3_e4m3e4m3_fp32_t128x32x128u2_s6_et64x32__b94ba45f4c` | `quant_gemm` | `random_high` | 6.22 | 1 | `bmm_E4m3_E4m3E4m3_Fp32_t128x32x128u2_s6_et64x32_m64x32x32_c1x1x1_rM_TN_transOut_noShfl_dsFp8_...` |
| `attention__batchmlapagedattentionkernel__752074e08d` | `attention` | `sharegpt_high` | 4.70 | 5 | `void flashinfer::mla::BatchMLAPagedAttentionKernel<flashinfer::mla::KernelTraits<true, 2u, tr...` |
| `quant_gemm__sm100_fp8_fp4_gemm_1d1d_impl__b219c86d5b` | `quant_gemm` | `random_mid` | 3.79 | 1 | `void deep_gemm::sm100_fp8_fp4_gemm_1d1d_impl<(cute::UMMA::Major)0, (cute::UMMA::Major)0, 128u...` |
| `quant_gemm__bmm_e4m3_e4m3e4m3_fp32_t128x8x128u2_s8_et64x8_m6__499a6a5a0c` | `quant_gemm` | `random_low` | 2.75 | 1 | `bmm_E4m3_E4m3E4m3_Fp32_t128x8x128u2_s8_et64x8_m64x8x32_c1x1x1_rM_TN_transOut_noShfl_dsFp8_sch...` |
| `moe__finalizekernelvecload__00edba12eb` | `moe` | `sharegpt_mid` | 2.55 | 1 | `void moe::dev::finalize::finalizeKernelVecLoad<moe::dev::finalize::KernelParams<cutlass::bflo...` |

Full shape samples and skipped weak/empty rows are in `kernel_task_index.json`.
