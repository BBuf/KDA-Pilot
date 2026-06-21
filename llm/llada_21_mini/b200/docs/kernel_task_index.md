# LLM Kernel Task Index: llada_21_mini / B200

- Model: `inclusionAI/LLaDA2.1-mini`
- Evidence threshold: GPU kernel name share strictly `> 2%`.
- Promotion rule: only rows with an external-id-bound non-empty torch-profiler shape are task candidates.
- Weak timestamp/nearest-preceding fallback rows are retained in audit data but are not promoted.

## Workload Coverage

| Workload | Rows | Strong | Weak | Empty shape | Status |
|---|---:|---:|---:|---:|---|
| `random_low` | 9 | 7 | 2 | 0 | partial, promote strong rows only |
| `random_mid` | 9 | 0 | 9 | 0 | weak/empty only, do not promote |
| `random_high` | 9 | 0 | 9 | 0 | weak/empty only, do not promote |
| `sharegpt_low` | 9 | 0 | 9 | 0 | weak/empty only, do not promote |
| `sharegpt_mid` | 9 | 0 | 9 | 0 | weak/empty only, do not promote |
| `sharegpt_high` | 9 | 0 | 9 | 0 | weak/empty only, do not promote |

## Task Candidates

| Task id | Category | Workloads | Max % GPU | Shape samples | Kernel |
|---|---|---|---:|---:|---|
| `moe__fused_moe_kernel__c581b7d47d` | `moe` | `random_low` | 32.84 | 6 | `fused_moe_kernel` |
| `gemm__kernel2__57e9da75e7` | `gemm` | `random_low` | 12.39 | 3 | `void cutlass::Kernel2<cutlass_80_simt_sgemm_64x64_8x5_tn_align1>(cutlass_80_simt_sgemm_64x64_...` |
| `gemm__device_kernel__5603f3ec20` | `gemm` | `random_low` | 7.38 | 3 | `void cutlass::device_kernel<cutlass::fmha::kernel::Sm100FmhaFwdKernelTmaWarpspecialized<cute:...` |
| `gemm__kernel_cutlass_kernel_flashinfernormkernelsfused__e2b3243700` | `gemm` | `random_low` | 3.23 | 3 | `kernel_cutlass_kernel_flashinfernormkernelsfused_add_rmsnormFusedAddRMSNormKernel_object_at__...` |
| `quant_gemm__nvjet_sm100_tst_8x64_64x16_4x1_v_bz_tnn__3decc0e67f` | `quant_gemm` | `random_low` | 2.81 | 3 | `nvjet_sm100_tst_8x64_64x16_4x1_v_bz_TNN` |
| `quant_gemm__nvjet_sm100_tst_64x16_64x16_2x2_2cta_h_bz_tnt__fcf149f0b2` | `quant_gemm` | `random_low` | 2.70 | 2 | `nvjet_sm100_tst_64x16_64x16_2x2_2cta_h_bz_TNT` |
| `quant_gemm__nvjet_sm100_tst_384x32_64x4_2x1_2cta_v_bz_tnt__42776567a6` | `quant_gemm` | `random_low` | 2.44 | 3 | `nvjet_sm100_tst_384x32_64x4_2x1_2cta_v_bz_TNT` |

Full shape samples and skipped weak/empty rows are in `kernel_task_index.json`.
