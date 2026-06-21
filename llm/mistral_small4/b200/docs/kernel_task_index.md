# LLM Kernel Task Index: mistral_small4 / B200

- Model: `mistralai/Mistral-Small-4-119B-2603`
- Evidence threshold: GPU kernel name share strictly `> 2%`.
- Promotion rule: only rows with an external-id-bound non-empty torch-profiler shape are task candidates.
- Weak timestamp/nearest-preceding fallback rows are retained in audit data but are not promoted.

## Workload Coverage

| Workload | Rows | Strong | Weak | Empty shape | Status |
|---|---:|---:|---:|---:|---|
| `random_low` | 13 | 6 | 7 | 0 | partial, promote strong rows only |
| `random_mid` | 10 | 4 | 6 | 0 | partial, promote strong rows only |
| `random_high` | 10 | 4 | 6 | 0 | partial, promote strong rows only |
| `sharegpt_low` | 13 | 5 | 8 | 0 | partial, promote strong rows only |
| `sharegpt_mid` | 11 | 3 | 8 | 0 | partial, promote strong rows only |
| `sharegpt_high` | 11 | 7 | 4 | 0 | partial, promote strong rows only |

## Task Candidates

| Task id | Category | Workloads | Max % GPU | Shape samples | Kernel |
|---|---|---|---:|---:|---|
| `other__bmm_e4m3_e4m3e4m3_fp32_btokbfloat16_t128x8x256u2__289939218c` | `other` | `random_low`, `random_mid`, `sharegpt_high` | 24.76 | 2 | `bmm_E4m3_E4m3E4m3_Fp32_BtokBfloat16_t128x8x256u2_s6_et128x8_m128x8x32_c1x1x1_rM_TN_transOut_s...` |
| `other__bmm_e4m3_e4m3e4m3_fp32_btokbfloat16_t128x64x256u__367dbbacb2` | `other` | `random_mid`, `sharegpt_mid`, `sharegpt_high` | 15.90 | 3 | `bmm_E4m3_E4m3E4m3_Fp32_BtokBfloat16_t128x64x256u2_s5_et128x64_m256x64x32_c2x1x1_rM_TN_transOu...` |
| `other__bmm_bfloat16_e4m3e4m3_fp32_t128x8x256u2_s6_et128__3f1fbbead9` | `other` | `random_low`, `sharegpt_low`, `sharegpt_high` | 13.72 | 3 | `bmm_Bfloat16_E4m3E4m3_Fp32_t128x8x256u2_s6_et128x8_m128x8x32_c1x1x1_rM_TN_transOut_schPd2x1x2...` |
| `other__bmm_e4m3_e4m3e4m3_fp32_btokbfloat16_t128x64x256__1f84a24079` | `other` | `random_high` | 11.02 | 1 | `bmm_E4m3_E4m3E4m3_Fp32_BtokBfloat16_t128x64x256_s5_et128x64_m256x64x32_c2x1x1_rM_TN_transOut_...` |
| `gemm__zn7cutlass13device_kernelins_4gemm6kernel13gemmu__4de9240811` | `gemm` | `random_mid`, `random_high`, `sharegpt_mid`, `sharegpt_high` | 10.62 | 4 | `_ZN7cutlass13device_kernelINS_4gemm6kernel13GemmUniversalIN4cute5tupleIJiiiiEEENS1_10collecti...` |
| `other__bmm_bfloat16_e4m3e4m3_fp32_t128x64x128u2_s8_et12__c427b3d287` | `other` | `random_mid`, `random_high`, `sharegpt_mid`, `sharegpt_high` | 9.05 | 4 | `bmm_Bfloat16_E4m3E4m3_Fp32_t128x64x128u2_s8_et128x64_m256x64x32_c2x1x1_rM_TN_transOut_schPd2x...` |
| `other__bmm_e4m3_e4m3e4m3_fp32_btokbfloat16_t128x8x256_s__61f9b2c116` | `other` | `sharegpt_low` | 7.00 | 1 | `bmm_E4m3_E4m3E4m3_Fp32_BtokBfloat16_t128x8x256_s6_et128x8_m128x8x32_c1x1x1_rM_TN_transOut_sch...` |
| `other__bmm_e4m3_e4m3e4m3_fp32_btokbfloat16_t128x32x256u__903abd17eb` | `other` | `sharegpt_high` | 5.83 | 1 | `bmm_E4m3_E4m3E4m3_Fp32_BtokBfloat16_t128x32x256u2_s5_et128x32_m128x32x32_c1x1x1_rM_TN_transOu...` |
| `gemm__kernel_cutlass_kernel_flashinfernormkernelsfused__d299f79010` | `gemm` | `random_low` | 3.67 | 1 | `kernel_cutlass_kernel_flashinfernormkernelsfused_add_rmsnormFusedAddRMSNormKernel_object_at__...` |
| `other__bmm_bfloat16_e4m3e4m3_fp32_t128x32x256u2_s5_et12__2a028e90fc` | `other` | `sharegpt_high` | 3.03 | 1 | `bmm_Bfloat16_E4m3E4m3_Fp32_t128x32x256u2_s5_et128x32_m128x32x32_c1x1x1_rM_TN_transOut_schPd2x...` |
| `other__bmm_bfloat16_e4m3e4m3_fp32_t128x64x128_s8_et128x__f5292701d4` | `other` | `random_high` | 3.02 | 1 | `bmm_Bfloat16_E4m3E4m3_Fp32_t128x64x128_s8_et128x64_m256x64x32_c2x1x1_rM_TN_transOut_schPd2x1x...` |
| `quant_gemm__nvjet_sm100_tst_128x8_64x12_2x1_v_bz_tnt__da4bd0e0be` | `quant_gemm` | `random_low`, `sharegpt_low` | 2.91 | 1 | `nvjet_sm100_tst_128x8_64x12_2x1_v_bz_TNT` |
| `gemm__zn7cutlass13device_kernelins_4gemm6kernel13gemmu__64c6383c7f` | `gemm` | `random_low`, `sharegpt_low` | 2.71 | 2 | `_ZN7cutlass13device_kernelINS_4gemm6kernel13GemmUniversalIN4cute5tupleIJiiiiEEENS1_10collecti...` |
| `moe__finalizekernel__6a7a068b8f` | `moe` | `random_low`, `sharegpt_low` | 2.47 | 2 | `void moe::dev::finalize::finalizeKernel<moe::dev::finalize::KernelParams<cutlass::bfloat16_t,...` |

Full shape samples and skipped weak/empty rows are in `kernel_task_index.json`.
