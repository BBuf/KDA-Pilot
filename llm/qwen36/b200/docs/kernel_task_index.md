# LLM Kernel Task Index: qwen36 / B200

- Model: `Qwen/Qwen3.6-35B-A3B-FP8`
- Evidence threshold: GPU kernel name share strictly `> 2%`.
- Promotion rule: only rows with an external-id-bound non-empty torch-profiler shape are task candidates.
- Weak timestamp/nearest-preceding fallback rows are retained in audit data but are not promoted.

## Workload Coverage

| Workload | Rows | Strong | Weak | Empty shape | Status |
|---|---:|---:|---:|---:|---|
| `random_low` | 8 | 3 | 5 | 0 | partial, promote strong rows only |
| `random_mid` | 8 | 4 | 4 | 0 | partial, promote strong rows only |
| `random_high` | 7 | 5 | 2 | 0 | partial, promote strong rows only |
| `sharegpt_low` | 9 | 4 | 5 | 0 | partial, promote strong rows only |
| `sharegpt_mid` | 7 | 7 | 0 | 0 | strong |
| `sharegpt_high` | 7 | 5 | 2 | 0 | partial, promote strong rows only |

## Task Candidates

| Task id | Category | Workloads | Max % GPU | Shape samples | Kernel |
|---|---|---|---:|---:|---|
| `quant_gemm__sm100_fp8_fp4_gemm_1d1d_impl__1b5539080f` | `quant_gemm` | `sharegpt_low`, `sharegpt_mid` | 16.12 | 2 | `void deep_gemm::sm100_fp8_fp4_gemm_1d1d_impl<(cute::UMMA::Major)0, (cute::UMMA::Major)0, 128u...` |
| `quant_gemm__bmm_e4m3_e4m3e4m3_fp32_t128x16x128u2_s6_et64x16__22f263f216` | `quant_gemm` | `sharegpt_high` | 12.84 | 1 | `bmm_E4m3_E4m3E4m3_Fp32_t128x16x128u2_s6_et64x16_m64x16x32_c1x1x1_rM_TN_transOut_noShfl_dsFp8_...` |
| `quant_gemm__bmm_e4m3_e4m3e4m3_fp32_t128x64x128u2_s6_et64x64__046d851f0c` | `quant_gemm` | `random_mid`, `random_high`, `sharegpt_mid` | 11.83 | 3 | `bmm_E4m3_E4m3E4m3_Fp32_t128x64x128u2_s6_et64x64_m64x64x32_c1x1x1_rM_TN_transOut_noShfl_dsFp8_...` |
| `quant_gemm__bmm_e4m3_e4m3e4m3_fp32_t128x8x128u2_s8_et64x8_m6__499a6a5a0c` | `quant_gemm` | `random_low`, `sharegpt_low`, `sharegpt_mid`, `sharegpt_high` | 10.76 | 5 | `bmm_E4m3_E4m3E4m3_Fp32_t128x8x128u2_s8_et64x8_m64x8x32_c1x1x1_rM_TN_transOut_noShfl_dsFp8_sch...` |
| `quant_gemm__bmm_bfloat16_e4m3e4m3_fp32_t128x8x128u2_s8_et64x__a76a258cda` | `quant_gemm` | `random_low`, `sharegpt_mid` | 7.76 | 3 | `bmm_Bfloat16_E4m3E4m3_Fp32_t128x8x128u2_s8_et64x8_m64x8x32_c1x1x1_rM_TN_transOut_noShfl_dsFp8...` |
| `moe__activationdeepseekkernel__b7453c53aa` | `moe` | `random_mid`, `random_high`, `sharegpt_mid`, `sharegpt_high` | 6.94 | 4 | `void moe::dev::activation::activationDeepSeekKernel<moe::dev::activation::KernelParams<cutlas...` |
| `quant_gemm__bmm_bfloat16_e4m3e4m3_fp32_t128x64x128u2_s6_et64__4becbe9f88` | `quant_gemm` | `random_mid`, `random_high`, `sharegpt_mid` | 6.10 | 3 | `bmm_Bfloat16_E4m3E4m3_Fp32_t128x64x128u2_s6_et64x64_m64x64x32_c1x1x1_rM_TN_transOut_noShfl_ds...` |
| `quant_gemm__sm100_fp8_fp4_gemm_1d1d_impl__45bdd89e95` | `quant_gemm` | `random_mid`, `random_high`, `sharegpt_mid` | 4.87 | 3 | `void deep_gemm::sm100_fp8_fp4_gemm_1d1d_impl<(cute::UMMA::Major)0, (cute::UMMA::Major)0, 128u...` |
| `moe__activationdeepseekkernel__215271b2b9` | `moe` | `sharegpt_low` | 3.51 | 1 | `void moe::dev::activation::activationDeepSeekKernel<moe::dev::activation::KernelParams<cutlas...` |
| `quant_gemm__bmm_e4m3_e4m3e4m3_fp32_t128x32x128u2_s6_et64x32__b94ba45f4c` | `quant_gemm` | `sharegpt_high` | 3.07 | 1 | `bmm_E4m3_E4m3E4m3_Fp32_t128x32x128u2_s6_et64x32_m64x32x32_c1x1x1_rM_TN_transOut_noShfl_dsFp8_...` |
| `moe__finalizekernel__6a7a068b8f` | `moe` | `random_low`, `sharegpt_low` | 2.64 | 2 | `void moe::dev::finalize::finalizeKernel<moe::dev::finalize::KernelParams<cutlass::bfloat16_t,...` |
| `moe__finalizekernelvecload__00edba12eb` | `moe` | `random_high` | 2.14 | 1 | `void moe::dev::finalize::finalizeKernelVecLoad<moe::dev::finalize::KernelParams<cutlass::bflo...` |
| `quant_gemm__bmm_bfloat16_e4m3e4m3_fp32_t128x16x128u2_s6_et64__a8443b40b0` | `quant_gemm` | `sharegpt_high` | 2.07 | 1 | `bmm_Bfloat16_E4m3E4m3_Fp32_t128x16x128u2_s6_et64x16_m64x16x32_c1x1x1_rM_TN_transOut_noShfl_ds...` |

Full shape samples and skipped weak/empty rows are in `kernel_task_index.json`.
