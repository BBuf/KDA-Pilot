# LLM Kernel Task Index: minimax_m27 / B200

- Model: `MiniMaxAI/MiniMax-M2.7`
- Evidence threshold: GPU kernel name share strictly `> 2%`.
- Promotion rule: only rows with an external-id-bound non-empty torch-profiler shape are task candidates.
- Weak timestamp/nearest-preceding fallback rows are retained in audit data but are not promoted.

## Workload Coverage

| Workload | Rows | Strong | Weak | Empty shape | Status |
|---|---:|---:|---:|---:|---|
| `random_low` | 11 | 8 | 1 | 2 | partial, promote strong rows only |
| `random_mid` | 10 | 6 | 3 | 1 | partial, promote strong rows only |
| `random_high` | 9 | 5 | 4 | 0 | partial, promote strong rows only |
| `sharegpt_low` | 11 | 6 | 4 | 1 | partial, promote strong rows only |
| `sharegpt_mid` | 9 | 8 | 1 | 0 | partial, promote strong rows only |
| `sharegpt_high` | 9 | 7 | 1 | 1 | partial, promote strong rows only |

## Task Candidates

| Task id | Category | Workloads | Max % GPU | Shape samples | Kernel |
|---|---|---|---:|---:|---|
| `moe__fused_moe_kernel__c581b7d47d` | `moe` | `random_low`, `random_mid`, `random_high`, `sharegpt_low`, `sharegpt_mid` | 32.52 | 5 | `fused_moe_kernel` |
| `comm__comm__a12cdaa5b4` | `comm` | `random_low`, `random_high`, `sharegpt_low`, `sharegpt_mid`, `sharegpt_high` | 17.19 | 5 | `void (anonymous namespace)::all_reduce_one_shot_push_kernel<__nv_bfloat16, 8u, true>((anonymo...` |
| `gemm__kernel_cutlass_kernel_flashinfernormkernelsfused__1cabd49873` | `gemm` | `random_low` | 12.36 | 1 | `kernel_cutlass_kernel_flashinfernormkernelsfused_add_rmsnormFusedAddRMSNormKernel_object_at__...` |
| `comm__comm__c330990d60` | `comm` | `random_mid`, `sharegpt_high` | 10.87 | 3 | `void (anonymous namespace)::all_reduce_two_shot_kernel<__nv_bfloat16, 8u, true>(host::distrib...` |
| `quant_gemm__sm100_fp8_fp4_gemm_1d1d_impl__1b5539080f` | `quant_gemm` | `random_low` | 7.86 | 1 | `void deep_gemm::sm100_fp8_fp4_gemm_1d1d_impl<(cute::UMMA::Major)0, (cute::UMMA::Major)0, 128u...` |
| `gemm__cutlass3x_sm100_simt_sgemm_f32_f32_f32_f32_f32_1__f50cc3eb45` | `gemm` | `random_mid` | 5.91 | 1 | `cutlass3x_sm100_simt_sgemm_f32_f32_f32_f32_f32_128x128x16_1x1x1_3_tnn_align1_bias_f32_relu` |
| `gemm__cutlass3x_sm100_simt_sgemm_f32_f32_f32_f32_f32_6__79fc92c9dd` | `gemm` | `random_mid`, `sharegpt_mid`, `sharegpt_high` | 5.39 | 3 | `cutlass3x_sm100_simt_sgemm_f32_f32_f32_f32_f32_64x32x16_1x1x1_3_tnn_align1_bias_f32_relu` |
| `attention__fmhasm100fkernel_qkvbfloat16obfloat16h128pagedkv__714e7067df` | `attention` | `random_high`, `sharegpt_mid`, `sharegpt_high` | 5.38 | 5 | `fmhaSm100fKernel_QkvBfloat16OBfloat16H128PagedKvCausalP64VarSeqQ128Kv128PersistentContext` |
| `gemm__kernel2__57e9da75e7` | `gemm` | `sharegpt_low`, `sharegpt_mid`, `sharegpt_high` | 4.60 | 3 | `void cutlass::Kernel2<cutlass_80_simt_sgemm_64x64_8x5_tn_align1>(cutlass_80_simt_sgemm_64x64_...` |
| `attention__fmhasm100fkernel_qkvbfloat16obfloat16h128pagedkv__93f41ffe86` | `attention` | `random_low` | 4.42 | 1 | `fmhaSm100fKernel_QkvBfloat16OBfloat16H128PagedKvCausalP64MultiCtasKvVarSeqQ8Kv128StaticSwapsA...` |
| `gemm__cutlass3x_sm100_simt_sgemm_f32_f32_f32_f32_f32_3__05d58acae0` | `gemm` | `sharegpt_high` | 4.12 | 2 | `cutlass3x_sm100_simt_sgemm_f32_f32_f32_f32_f32_32x32x16_1x1x1_3_tnn_align1_bias_f32_relu` |
| `norm__fusedaddrmsnormkernel__99f19a4e72` | `norm` | `random_low`, `random_mid`, `random_high`, `sharegpt_low`, `sharegpt_mid`, `sharegpt_high` | 3.90 | 6 | `void flashinfer::norm::FusedAddRMSNormKernel<8u, __nv_bfloat16>(__nv_bfloat16*, __nv_bfloat16...` |
| `gemm__cutlass3x_sm100_simt_sgemm_f32_f32_f32_f32_f32_1__b4f87b5018` | `gemm` | `random_high`, `sharegpt_mid` | 3.88 | 2 | `cutlass3x_sm100_simt_sgemm_f32_f32_f32_f32_f32_128x64x16_1x1x1_3_tnn_align1_bias_f32_relu` |
| `comm__comm__515f5a341d` | `comm` | `random_low`, `sharegpt_low` | 2.96 | 3 | `void (anonymous namespace)::all_reduce_one_shot_push_kernel<float, 8u, true>((anonymous names...` |
| `quant_gemm__quant_gemm__3e56f98c58` | `quant_gemm` | `random_low`, `sharegpt_low`, `sharegpt_mid` | 2.57 | 3 | `void (anonymous namespace)::per_token_group_quant_8bit_v2_kernel<(anonymous namespace)::Naive...` |
| `moe__moe_sum_reduce_warp_per_token_vec_kernel__3fc4b40863` | `moe` | `random_mid` | 2.06 | 1 | `void moe_sum_reduce_warp_per_token_vec_kernel<8>(c10::BFloat16 const*, c10::BFloat16*, long, ...` |

Full shape samples and skipped weak/empty rows are in `kernel_task_index.json`.
