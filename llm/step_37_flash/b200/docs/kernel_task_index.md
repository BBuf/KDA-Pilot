# LLM Kernel Task Index: step_37_flash / B200

- Model: `stepfun-ai/Step-3.7-Flash-NVFP4`
- Evidence threshold: GPU kernel name share strictly `> 2%`.
- Promotion rule: only rows with an external-id-bound non-empty torch-profiler shape are task candidates.
- Weak timestamp/nearest-preceding fallback rows are retained in audit data but are not promoted.

## Workload Coverage

| Workload | Rows | Strong | Weak | Empty shape | Status |
|---|---:|---:|---:|---:|---|
| `random_low` | 4 | 3 | 1 | 0 | partial, promote strong rows only |
| `random_mid` | 6 | 5 | 1 | 0 | partial, promote strong rows only |
| `random_high` | 5 | 3 | 2 | 0 | partial, promote strong rows only |
| `sharegpt_low` | 3 | 1 | 2 | 0 | partial, promote strong rows only |
| `sharegpt_mid` | 4 | 3 | 1 | 0 | partial, promote strong rows only |
| `sharegpt_high` | 3 | 2 | 1 | 0 | partial, promote strong rows only |

## Task Candidates

| Task id | Category | Workloads | Max % GPU | Shape samples | Kernel |
|---|---|---|---:|---:|---|
| `comm__comm__a12cdaa5b4` | `comm` | `random_low`, `random_mid`, `sharegpt_low`, `sharegpt_mid`, `sharegpt_high` | 38.59 | 5 | `void (anonymous namespace)::all_reduce_one_shot_push_kernel<__nv_bfloat16, 8u, true>((anonymo...` |
| `comm__comm__c330990d60` | `comm` | `random_high`, `sharegpt_mid`, `sharegpt_high` | 33.29 | 4 | `void (anonymous namespace)::all_reduce_two_shot_kernel<__nv_bfloat16, 8u, true>(host::distrib...` |
| `gemm__kernel_cutlass_kernel_flashinfernormkernelsfused__d299f79010` | `gemm` | `random_low` | 32.09 | 1 | `kernel_cutlass_kernel_flashinfernormkernelsfused_add_rmsnormFusedAddRMSNormKernel_object_at__...` |
| `gemm__cutlass3x_sm100_simt_sgemm_f32_f32_f32_f32_f32_1__f50cc3eb45` | `gemm` | `random_mid` | 7.68 | 2 | `cutlass3x_sm100_simt_sgemm_f32_f32_f32_f32_f32_128x128x16_1x1x1_3_tnn_align1_bias_f32_relu` |
| `gemm__cutlass3x_sm100_simt_sgemm_f32_f32_f32_f32_f32_6__d89eb792f0` | `gemm` | `sharegpt_mid` | 4.48 | 2 | `cutlass3x_sm100_simt_sgemm_f32_f32_f32_f32_f32_64x64x16_1x1x1_3_tnn_align1_bias_f32_relu` |
| `gemm__kernel2__57e9da75e7` | `gemm` | `random_mid`, `random_high` | 4.03 | 2 | `void cutlass::Kernel2<cutlass_80_simt_sgemm_64x64_8x5_tn_align1>(cutlass_80_simt_sgemm_64x64_...` |
| `moe__moetopk__283e0afb8e` | `moe` | `random_low`, `random_mid` | 2.94 | 3 | `void moeTopK<256>(float const*, bool const*, float*, int*, int, int, int, int, bool, float co...` |
| `gemm__cutlass3x_sm100_simt_sgemm_f32_f32_f32_f32_f32_6__fc9ff25e8d` | `gemm` | `random_high` | 2.85 | 2 | `cutlass3x_sm100_simt_sgemm_f32_f32_f32_f32_f32_64x128x16_1x1x1_3_tnn_align1_bias_f32_relu` |
| `quant_gemm__nvjet_sm100_tst_128x256_64x6_2x1_2cta_v_bz_tnt__73699af3d3` | `quant_gemm` | `random_mid` | 2.46 | 2 | `nvjet_sm100_tst_128x256_64x6_2x1_2cta_v_bz_TNT` |

Full shape samples and skipped weak/empty rows are in `kernel_task_index.json`.
