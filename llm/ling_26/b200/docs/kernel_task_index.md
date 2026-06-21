# LLM Kernel Task Index: ling_26 / B200

- Model: `inclusionAI/Ling-2.6-flash`
- Evidence threshold: GPU kernel name share strictly `> 2%`.
- Promotion rule: only rows with an external-id-bound non-empty torch-profiler shape are task candidates.
- Weak timestamp/nearest-preceding fallback rows are retained in audit data but are not promoted.

## Workload Coverage

| Workload | Rows | Strong | Weak | Empty shape | Status |
|---|---:|---:|---:|---:|---|
| `random_low` | 4 | 3 | 1 | 0 | partial, promote strong rows only |
| `random_mid` | 6 | 4 | 2 | 0 | partial, promote strong rows only |
| `random_high` | 6 | 4 | 2 | 0 | partial, promote strong rows only |
| `sharegpt_low` | 4 | 2 | 2 | 0 | partial, promote strong rows only |
| `sharegpt_mid` | 6 | 4 | 2 | 0 | partial, promote strong rows only |
| `sharegpt_high` | 5 | 3 | 2 | 0 | partial, promote strong rows only |

## Task Candidates

| Task id | Category | Workloads | Max % GPU | Shape samples | Kernel |
|---|---|---|---:|---:|---|
| `comm__comm__0821f7c6e6` | `comm` | `random_low`, `random_mid`, `random_high`, `sharegpt_low`, `sharegpt_mid`, `sharegpt_high` | 33.85 | 12 | `void (anonymous namespace)::all_reduce_one_shot_push_kernel<__nv_bfloat16, 4u, true>((anonymo...` |
| `moe__fused_moe_kernel__c581b7d47d` | `moe` | `random_low`, `random_mid`, `random_high`, `sharegpt_low`, `sharegpt_mid`, `sharegpt_high` | 32.32 | 12 | `fused_moe_kernel` |
| `gemm__kernel_cutlass_kernel_flashinfernormkernelsfused__d299f79010` | `gemm` | `random_low` | 28.14 | 4 | `kernel_cutlass_kernel_flashinfernormkernelsfused_add_rmsnormFusedAddRMSNormKernel_object_at__...` |
| `comm__comm__9dd2e02622` | `comm` | `random_high`, `sharegpt_high` | 18.50 | 3 | `void (anonymous namespace)::all_reduce_two_shot_kernel<__nv_bfloat16, 4u, true>(host::distrib...` |
| `gemm__cutlass3x_sm100_simt_sgemm_f32_f32_f32_f32_f32_6__d89eb792f0` | `gemm` | `random_mid`, `sharegpt_mid` | 6.66 | 6 | `cutlass3x_sm100_simt_sgemm_f32_f32_f32_f32_f32_64x64x16_1x1x1_3_tnn_align1_bias_f32_relu` |
| `quant_gemm__nvjet_sm100_tst_128x256_64x6_2x1_2cta_v_bz_tnt__73699af3d3` | `quant_gemm` | `sharegpt_mid` | 3.02 | 4 | `nvjet_sm100_tst_128x256_64x6_2x1_2cta_v_bz_TNT` |
| `quant_gemm__nvjet_sm100_tst_256x224_64x4_2x2_2cta_h_bz_tnt__bc8b5d91d3` | `quant_gemm` | `random_mid` | 2.14 | 3 | `nvjet_sm100_tst_256x224_64x4_2x2_2cta_h_bz_TNT` |
| `gemm__kernel2__57e9da75e7` | `gemm` | `random_high` | 2.06 | 1 | `void cutlass::Kernel2<cutlass_80_simt_sgemm_64x64_8x5_tn_align1>(cutlass_80_simt_sgemm_64x64_...` |

Full shape samples and skipped weak/empty rows are in `kernel_task_index.json`.
