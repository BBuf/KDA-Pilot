# LLM Kernel Task Index: poolside_laguna_xs2 / B200

- Model: `poolside/Laguna-XS.2-FP8`
- Evidence threshold: GPU kernel name share strictly `> 2%`.
- Promotion rule: only rows with an external-id-bound non-empty torch-profiler shape are task candidates.
- Weak timestamp/nearest-preceding fallback rows are retained in audit data but are not promoted.

## Workload Coverage

| Workload | Rows | Strong | Weak | Empty shape | Status |
|---|---:|---:|---:|---:|---|
| `random_low` | 8 | 8 | 0 | 0 | strong |
| `random_mid` | 14 | 12 | 2 | 0 | partial, promote strong rows only |
| `random_high` | 10 | 5 | 5 | 0 | partial, promote strong rows only |
| `sharegpt_low` | 8 | 0 | 6 | 2 | weak/empty only, do not promote |
| `sharegpt_mid` | 8 | 5 | 1 | 2 | partial, promote strong rows only |
| `sharegpt_high` | 7 | 7 | 0 | 0 | strong |

## Task Candidates

| Task id | Category | Workloads | Max % GPU | Shape samples | Kernel |
|---|---|---|---:|---:|---|
| `moe__fused_moe_kernel__c581b7d47d` | `moe` | `random_low`, `random_mid`, `random_high`, `sharegpt_high` | 20.20 | 4 | `fused_moe_kernel` |
| `comm__comm__9dd2e02622` | `comm` | `random_high`, `sharegpt_high` | 12.60 | 3 | `void (anonymous namespace)::all_reduce_two_shot_kernel<__nv_bfloat16, 4u, true>(host::distrib...` |
| `comm__nccldevkernel_allreduce_sum_bf16_ring_ll__05a3ee6241` | `comm` | `random_mid` | 9.66 | 1 | `ncclDevKernel_AllReduce_Sum_bf16_RING_LL(ncclDevKernelArgsStorage<4096ul>)` |
| `comm__comm__0821f7c6e6` | `comm` | `random_low`, `random_mid`, `sharegpt_mid`, `sharegpt_high` | 9.03 | 7 | `void (anonymous namespace)::all_reduce_one_shot_push_kernel<__nv_bfloat16, 4u, true>((anonymo...` |
| `quant_gemm__sm100_fp8_fp4_gemm_1d1d_impl__1b5539080f` | `quant_gemm` | `random_low` | 6.64 | 2 | `void deep_gemm::sm100_fp8_fp4_gemm_1d1d_impl<(cute::UMMA::Major)0, (cute::UMMA::Major)0, 128u...` |
| `gemm__cutlass3x_sm100_simt_sgemm_f32_f32_f32_f32_f32_6__d89eb792f0` | `gemm` | `random_mid` | 6.57 | 1 | `cutlass3x_sm100_simt_sgemm_f32_f32_f32_f32_f32_64x64x16_1x1x1_3_tnn_align1_bias_f32_relu` |
| `norm__fusedaddrmsnormkernel__99f19a4e72` | `norm` | `random_low`, `random_mid`, `random_high`, `sharegpt_mid`, `sharegpt_high` | 6.42 | 7 | `void flashinfer::norm::FusedAddRMSNormKernel<8u, __nv_bfloat16>(__nv_bfloat16*, __nv_bfloat16...` |
| `gemm__kernel_cutlass_kernel_flashinfernormkernelsfused__e2b3243700` | `gemm` | `random_low` | 5.85 | 1 | `kernel_cutlass_kernel_flashinfernormkernelsfused_add_rmsnormFusedAddRMSNormKernel_object_at__...` |
| `quant_gemm__nvjet_sm100_tst_16x64_64x16_4x1_v_bz_tnn__e3baf7ff46` | `quant_gemm` | `random_low` | 5.80 | 2 | `nvjet_sm100_tst_16x64_64x16_4x1_v_bz_TNN` |
| `gemm__cutlass3x_sm100_simt_sgemm_f32_f32_f32_f32_f32_1__f50cc3eb45` | `gemm` | `sharegpt_mid` | 5.00 | 1 | `cutlass3x_sm100_simt_sgemm_f32_f32_f32_f32_f32_128x128x16_1x1x1_3_tnn_align1_bias_f32_relu` |
| `gemm__cutlass3x_sm100_simt_sgemm_f32_f32_f32_f32_f32_3__05d58acae0` | `gemm` | `sharegpt_mid`, `sharegpt_high` | 4.88 | 3 | `cutlass3x_sm100_simt_sgemm_f32_f32_f32_f32_f32_32x32x16_1x1x1_3_tnn_align1_bias_f32_relu` |
| `attention__fmhasm100fkernel_qkvbfloat16obfloat16h128pagedkv__6f150a74e8` | `attention` | `random_mid`, `random_high`, `sharegpt_mid`, `sharegpt_high` | 3.77 | 12 | `fmhaSm100fKernel_QkvBfloat16OBfloat16H128PagedKvSlidingOrChunkedCausalP64VarSeqQ128Kv128Persi...` |
| `gemm__kernel2__57e9da75e7` | `gemm` | `random_mid`, `sharegpt_high` | 3.70 | 2 | `void cutlass::Kernel2<cutlass_80_simt_sgemm_64x64_8x5_tn_align1>(cutlass_80_simt_sgemm_64x64_...` |
| `memory_bound__unrolled_elementwise_kernel__64bf90af3d` | `memory_bound` | `random_mid` | 3.38 | 1 | `void at::native::unrolled_elementwise_kernel<at::native::direct_copy_kernel_cuda(at::TensorIt...` |
| `gemm__cutlass3x_sm100_simt_sgemm_f32_f32_f32_f32_f32_1__b4f87b5018` | `gemm` | `random_high` | 3.27 | 1 | `cutlass3x_sm100_simt_sgemm_f32_f32_f32_f32_f32_128x64x16_1x1x1_3_tnn_align1_bias_f32_relu` |
| `quant_gemm__nvjet_sm100_tst_128x256_64x6_2x1_2cta_v_bz_tnt__73699af3d3` | `quant_gemm` | `random_mid` | 3.16 | 1 | `nvjet_sm100_tst_128x256_64x6_2x1_2cta_v_bz_TNT` |
| `attention__fmhasm100fkernel_qkvbfloat16obfloat16h128pagedkv__599a6ae214` | `attention` | `random_low` | 2.93 | 1 | `fmhaSm100fKernel_QkvBfloat16OBfloat16H128PagedKvSlidingOrChunkedCausalP64MultiCtasKvCgaVarSeq...` |
| `quant_gemm__nvjet_sm100_tst_32x64_64x16_4x1_v_bz_tnn__7ccfc913b8` | `quant_gemm` | `random_low` | 2.75 | 2 | `nvjet_sm100_tst_32x64_64x16_4x1_v_bz_TNN` |
| `other__other__56d7fd43dd` | `other` | `random_mid` | 2.28 | 1 | `void (anonymous namespace)::act_and_mul_kernel<__nv_bfloat16, ((anonymous namespace)::Activat...` |
| `memory_bound__elementwise_kernel__4a3a288972` | `memory_bound` | `random_mid` | 2.20 | 1 | `void at::native::elementwise_kernel<128, 4, at::native::gpu_kernel_impl_nocast<at::native::Bi...` |
| `moe__count_and_sort_expert_tokens_kernel__0439b481ab` | `moe` | `random_mid` | 2.05 | 1 | `void count_and_sort_expert_tokens_kernel<int>(int const*, int*, int*, unsigned long)` |

Full shape samples and skipped weak/empty rows are in `kernel_task_index.json`.
