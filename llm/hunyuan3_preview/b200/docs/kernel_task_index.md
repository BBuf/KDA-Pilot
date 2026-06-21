# LLM Kernel Task Index: hunyuan3_preview / B200

- Model: `tencent/Hy3-preview`
- Evidence threshold: GPU kernel name share strictly `> 2%`.
- Promotion rule: only rows with an external-id-bound non-empty torch-profiler shape are task candidates.
- Weak timestamp/nearest-preceding fallback rows are retained in audit data but are not promoted.

## Workload Coverage

| Workload | Rows | Strong | Weak | Empty shape | Status |
|---|---:|---:|---:|---:|---|
| `random_low` | 7 | 5 | 2 | 0 | partial, promote strong rows only |
| `random_mid` | 7 | 4 | 3 | 0 | partial, promote strong rows only |
| `random_high` | 3 | 2 | 1 | 0 | partial, promote strong rows only |
| `sharegpt_low` | 5 | 2 | 3 | 0 | partial, promote strong rows only |
| `sharegpt_mid` | 5 | 3 | 2 | 0 | partial, promote strong rows only |
| `sharegpt_high` | 4 | 2 | 2 | 0 | partial, promote strong rows only |

## Task Candidates

| Task id | Category | Workloads | Max % GPU | Shape samples | Kernel |
|---|---|---|---:|---:|---|
| `memory_bound__cross_device_reduce_1stage__8c4d51bdf2` | `memory_bound` | `sharegpt_mid`, `sharegpt_high` | 44.46 | 4 | `void sglang::cross_device_reduce_1stage<__half, 8>(sglang::RankData*, sglang::RankSignals, sg...` |
| `memory_bound__cross_device_reduce_2stage__9697743b4f` | `memory_bound` | `random_low`, `random_high` | 40.12 | 3 | `void sglang::cross_device_reduce_2stage<__half, 8>(sglang::RankData*, sglang::RankSignals, sg...` |
| `moe__fused_moe_kernel__c581b7d47d` | `moe` | `random_low`, `random_mid`, `random_high`, `sharegpt_low`, `sharegpt_mid`, `sharegpt_high` | 34.73 | 10 | `fused_moe_kernel` |
| `comm__nccldevkernel_allreduce_sum_f16_ring_ll__29d2bcd930` | `comm` | `random_mid` | 9.78 | 2 | `ncclDevKernel_AllReduce_Sum_f16_RING_LL(ncclDevKernelArgsStorage<4096ul>)` |
| `gemm__cutlass3x_sm100_simt_sgemm_f32_f32_f32_f32_f32_6__fc9ff25e8d` | `gemm` | `random_mid`, `sharegpt_mid` | 4.08 | 5 | `cutlass3x_sm100_simt_sgemm_f32_f32_f32_f32_f32_64x128x16_1x1x1_3_tnn_align1_bias_f32_relu` |
| `gemm__kernel2__57e9da75e7` | `gemm` | `random_low`, `sharegpt_low` | 3.88 | 3 | `void cutlass::Kernel2<cutlass_80_simt_sgemm_64x64_8x5_tn_align1>(cutlass_80_simt_sgemm_64x64_...` |
| `quant_gemm__nvjet_hsh_32x64_64x16_4x1_v_bz_splitk_tnn__be91d90e63` | `quant_gemm` | `random_low` | 3.08 | 1 | `nvjet_hsh_32x64_64x16_4x1_v_bz_splitK_TNN` |
| `moe__moe_sum_reduce_kernel_warp_token_topk__43207a7c49` | `moe` | `random_mid` | 2.78 | 2 | `void moe_sum_reduce_kernel_warp_token_topk<c10::Half, 8, 4>(c10::Half const*, c10::Half*, lon...` |
| `gemm__kernel_cutlass_kernel_flashinfernormkernelsfused__73220359bf` | `gemm` | `random_low` | 2.24 | 5 | `kernel_cutlass_kernel_flashinfernormkernelsfused_add_rmsnormFusedAddRMSNormKernel_object_at__...` |

Full shape samples and skipped weak/empty rows are in `kernel_task_index.json`.
