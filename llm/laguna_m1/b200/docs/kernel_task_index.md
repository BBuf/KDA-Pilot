# LLM Kernel Task Index: laguna_m1 / B200

- Model: `poolside/Laguna-M.1-NVFP4`
- Evidence threshold: GPU kernel name share strictly `> 2%`.
- Promotion rule: only rows with an external-id-bound non-empty torch-profiler shape are task candidates.
- Weak timestamp/nearest-preceding fallback rows are retained in audit data but are not promoted.

## Workload Coverage

| Workload | Rows | Strong | Weak | Empty shape | Status |
|---|---:|---:|---:|---:|---|
| `random_low` | 11 | 9 | 2 | 0 | partial, promote strong rows only |
| `random_mid` | 7 | 5 | 2 | 0 | partial, promote strong rows only |
| `random_high` | 7 | 6 | 1 | 0 | partial, promote strong rows only |
| `sharegpt_low` | 11 | 2 | 9 | 0 | partial, promote strong rows only |
| `sharegpt_mid` | 5 | 4 | 1 | 0 | partial, promote strong rows only |
| `sharegpt_high` | 10 | 3 | 7 | 0 | partial, promote strong rows only |

## Task Candidates

| Task id | Category | Workloads | Max % GPU | Shape samples | Kernel |
|---|---|---|---:|---:|---|
| `quant_gemm__zn7cutlass13device_kernelins_4gemm6kernel13gemmu__f5cea54bc2` | `quant_gemm` | `random_low`, `random_mid`, `random_high`, `sharegpt_low`, `sharegpt_mid`, `sharegpt_high` | 29.53 | 6 | `_ZN7cutlass13device_kernelINS_4gemm6kernel13GemmUniversalINS1_17GroupProblemShapeIN4cute5tupl...` |
| `comm__nccldevkernel_allreduce_sum_bf16_ring_ll__05a3ee6241` | `comm` | `random_mid`, `random_high`, `sharegpt_mid` | 11.71 | 4 | `ncclDevKernel_AllReduce_Sum_bf16_RING_LL(ncclDevKernelArgsStorage<4096ul>)` |
| `comm__comm__a12cdaa5b4` | `comm` | `random_low`, `sharegpt_low` | 8.41 | 2 | `void (anonymous namespace)::all_reduce_one_shot_push_kernel<__nv_bfloat16, 8u, true>((anonymo...` |
| `comm__comm__c330990d60` | `comm` | `random_mid`, `random_high`, `sharegpt_high` | 7.04 | 3 | `void (anonymous namespace)::all_reduce_two_shot_kernel<__nv_bfloat16, 8u, true>(host::distrib...` |
| `moe__compute_expert_blockscale_offsets__80d447739f` | `moe` | `random_low`, `random_high` | 5.73 | 2 | `compute_expert_blockscale_offsets(int const*, int*, int*, int*, long)` |
| `gemm__kernel_cutlass_kernel_flashinfernormkernelsfused__d299f79010` | `gemm` | `random_low` | 5.50 | 2 | `kernel_cutlass_kernel_flashinfernormkernelsfused_add_rmsnormFusedAddRMSNormKernel_object_at__...` |
| `quant_gemm__nvjet_sm100_tst_32x64_64x16_4x1_v_bz_splitk_tnn__0fa651efdd` | `quant_gemm` | `random_low` | 5.03 | 1 | `nvjet_sm100_tst_32x64_64x16_4x1_v_bz_splitK_TNN` |
| `gemm__kernel_cutlass_kernel_flashinfergemmkernelsdense__e9481e7b7d` | `gemm` | `random_low` | 4.78 | 1 | `kernel_cutlass_kernel_flashinfergemmkernelsdense_blockscaled_gemm_sm100Sm100BlockScaledPersis...` |
| `other__apply_shuffle_mul_sum_kernel__e46e17a33d` | `other` | `random_low` | 3.89 | 1 | `void apply_shuffle_mul_sum_kernel<__nv_bfloat16>(__nv_bfloat16 const*, __nv_bfloat16*, int co...` |
| `gemm__kernel2__57e9da75e7` | `gemm` | `random_mid`, `random_high` | 3.69 | 2 | `void cutlass::Kernel2<cutlass_80_simt_sgemm_64x64_8x5_tn_align1>(cutlass_80_simt_sgemm_64x64_...` |
| `gemm__cutlass3x_sm100_simt_sgemm_f32_f32_f32_f32_f32_1__b4f87b5018` | `gemm` | `random_high`, `sharegpt_mid` | 3.51 | 2 | `cutlass3x_sm100_simt_sgemm_f32_f32_f32_f32_f32_128x64x16_1x1x1_3_tnn_align1_bias_f32_relu` |
| `attention__fmhasm100fkernel_qkvbfloat16obfloat16h128pagedkv__93f41ffe86` | `attention` | `random_low` | 3.18 | 1 | `fmhaSm100fKernel_QkvBfloat16OBfloat16H128PagedKvCausalP64MultiCtasKvVarSeqQ8Kv128StaticSwapsA...` |
| `attention__fmhasm100fkernel_qkvbfloat16obfloat16h128pagedkv__714e7067df` | `attention` | `sharegpt_high` | 2.98 | 8 | `fmhaSm100fKernel_QkvBfloat16OBfloat16H128PagedKvCausalP64VarSeqQ128Kv128PersistentContext` |
| `gemm__splitkreduce_kernel__ad3ac66771` | `gemm` | `random_low` | 2.84 | 2 | `void cublasLt::splitKreduce_kernel<32, 16, int, float, __nv_bfloat16, float, __nv_bfloat16, f...` |
| `norm__fusedaddrmsnormkernel__99f19a4e72` | `norm` | `random_mid`, `sharegpt_mid` | 2.73 | 2 | `void flashinfer::norm::FusedAddRMSNormKernel<8u, __nv_bfloat16>(__nv_bfloat16*, __nv_bfloat16...` |

Full shape samples and skipped weak/empty rows are in `kernel_task_index.json`.
