# LLM Kernel Task Index: llada_21_flash / B200

- Model: `inclusionAI/LLaDA2.1-flash`
- Evidence threshold: GPU kernel name share strictly `> 2%`.
- Promotion rule: only rows with an external-id-bound non-empty torch-profiler shape are task candidates.
- Weak timestamp/nearest-preceding fallback rows are retained in audit data but are not promoted.

## Workload Coverage

| Workload | Rows | Strong | Weak | Empty shape | Status |
|---|---:|---:|---:|---:|---|
| `random_low` | 8 | 7 | 1 | 0 | partial, promote strong rows only |
| `random_mid` | 8 | 0 | 8 | 0 | weak/empty only, do not promote |
| `random_high` | 8 | 0 | 8 | 0 | weak/empty only, do not promote |
| `sharegpt_low` | 8 | 0 | 8 | 0 | weak/empty only, do not promote |
| `sharegpt_mid` | 8 | 0 | 8 | 0 | weak/empty only, do not promote |
| `sharegpt_high` | 8 | 0 | 8 | 0 | weak/empty only, do not promote |

## Task Candidates

| Task id | Category | Workloads | Max % GPU | Shape samples | Kernel |
|---|---|---|---:|---:|---|
| `moe__fused_moe_kernel__c581b7d47d` | `moe` | `random_low` | 44.63 | 3 | `fused_moe_kernel` |
| `gemm__kernel2__57e9da75e7` | `gemm` | `random_low` | 9.05 | 3 | `void cutlass::Kernel2<cutlass_80_simt_sgemm_64x64_8x5_tn_align1>(cutlass_80_simt_sgemm_64x64_...` |
| `gemm__device_kernel__5603f3ec20` | `gemm` | `random_low` | 5.22 | 2 | `void cutlass::device_kernel<cutlass::fmha::kernel::Sm100FmhaFwdKernelTmaWarpspecialized<cute:...` |
| `comm__comm__e96ef2a99d` | `comm` | `random_low` | 4.02 | 2 | `void (anonymous namespace)::all_reduce_one_shot_push_kernel<__nv_bfloat16, 2u, true>((anonymo...` |
| `quant_gemm__nvjet_sm100_tst_64x16_64x16_2x2_2cta_h_bz_tnt__fcf149f0b2` | `quant_gemm` | `random_low` | 3.84 | 2 | `nvjet_sm100_tst_64x16_64x16_2x2_2cta_h_bz_TNT` |
| `gemm__kernel_cutlass_kernel_flashinfernormkernelsfused__d299f79010` | `gemm` | `random_low` | 3.79 | 2 | `kernel_cutlass_kernel_flashinfernormkernelsfused_add_rmsnormFusedAddRMSNormKernel_object_at__...` |
| `quant_gemm__nvjet_sm100_tst_32x64_64x16_4x1_v_bz_tnn__7ccfc913b8` | `quant_gemm` | `random_low` | 2.84 | 2 | `nvjet_sm100_tst_32x64_64x16_4x1_v_bz_TNN` |

Full shape samples and skipped weak/empty rows are in `kernel_task_index.json`.
