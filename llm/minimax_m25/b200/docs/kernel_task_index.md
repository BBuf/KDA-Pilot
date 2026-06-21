# LLM Kernel Task Index: minimax_m25 / B200

- Model: `MiniMaxAI/MiniMax-M2.5`
- Evidence threshold: GPU kernel name share strictly `> 2%`.
- Promotion rule: only rows with an external-id-bound non-empty torch-profiler shape are task candidates.
- Weak timestamp/nearest-preceding fallback rows are retained in audit data but are not promoted.

## Workload Coverage

| Workload | Rows | Strong | Weak | Empty shape | Status |
|---|---:|---:|---:|---:|---|
| `random_low` | 9 | 9 | 0 | 0 | strong |
| `random_mid` | 10 | 8 | 2 | 0 | partial, promote strong rows only |
| `random_high` | 9 | 3 | 2 | 4 | partial, promote strong rows only |
| `sharegpt_low` | 10 | 0 | 5 | 5 | weak/empty only, do not promote |
| `sharegpt_mid` | 11 | 10 | 1 | 0 | partial, promote strong rows only |
| `sharegpt_high` | 10 | 9 | 1 | 0 | partial, promote strong rows only |

## Task Candidates

| Task id | Category | Workloads | Max % GPU | Shape samples | Kernel |
|---|---|---|---:|---:|---|
| `moe__fused_moe_kernel__c581b7d47d` | `moe` | `random_low`, `random_mid`, `random_high`, `sharegpt_mid`, `sharegpt_high` | 31.73 | 6 | `fused_moe_kernel` |
| `quant_gemm__w8a8_block_fp8_matmul__c1e3573b4b` | `quant_gemm` | `random_low`, `random_mid`, `sharegpt_mid`, `sharegpt_high` | 20.52 | 7 | `_w8a8_block_fp8_matmul` |
| `comm__comm__2f32ca6996` | `comm` | `random_low`, `sharegpt_mid`, `sharegpt_high` | 13.92 | 4 | `void (anonymous namespace)::all_reduce_one_shot_push_kernel<__half, 8u, true>((anonymous name...` |
| `gemm__kernel_cutlass_kernel_flashinfernormkernelsfused__7e8fbc5467` | `gemm` | `random_low` | 10.79 | 1 | `kernel_cutlass_kernel_flashinfernormkernelsfused_add_rmsnormFusedAddRMSNormKernel_object_at__...` |
| `comm__comm__9cd2963a17` | `comm` | `random_mid`, `random_high`, `sharegpt_high` | 9.65 | 4 | `void (anonymous namespace)::all_reduce_two_shot_kernel<__half, 8u, true>(host::distributed::A...` |
| `gemm__cutlass3x_sm100_simt_sgemm_f32_f32_f32_f32_f32_3__05d58acae0` | `gemm` | `sharegpt_high` | 5.94 | 2 | `cutlass3x_sm100_simt_sgemm_f32_f32_f32_f32_f32_32x32x16_1x1x1_3_tnn_align1_bias_f32_relu` |
| `gemm__cutlass3x_sm100_simt_sgemm_f32_f32_f32_f32_f32_1__f50cc3eb45` | `gemm` | `random_mid` | 5.32 | 1 | `cutlass3x_sm100_simt_sgemm_f32_f32_f32_f32_f32_128x128x16_1x1x1_3_tnn_align1_bias_f32_relu` |
| `attention__fmhasm100fkernel_qkvfp16ofp16h128pagedkvcausalp6__073fbd3338` | `attention` | `random_high`, `sharegpt_mid`, `sharegpt_high` | 5.20 | 9 | `fmhaSm100fKernel_QkvFp16OFp16H128PagedKvCausalP64VarSeqQ128Kv128PersistentContext` |
| `gemm__cutlass3x_sm100_simt_sgemm_f32_f32_f32_f32_f32_6__79fc92c9dd` | `gemm` | `sharegpt_mid` | 4.98 | 1 | `cutlass3x_sm100_simt_sgemm_f32_f32_f32_f32_f32_64x32x16_1x1x1_3_tnn_align1_bias_f32_relu` |
| `quant_gemm__quant_gemm__067e4625ab` | `quant_gemm` | `random_low`, `random_mid`, `sharegpt_mid`, `sharegpt_high` | 4.16 | 5 | `void (anonymous namespace)::per_token_group_quant_8bit_v2_kernel<(anonymous namespace)::Naive...` |
| `gemm__kernel2__57e9da75e7` | `gemm` | `random_mid`, `sharegpt_mid`, `sharegpt_high` | 4.10 | 3 | `void cutlass::Kernel2<cutlass_80_simt_sgemm_64x64_8x5_tn_align1>(cutlass_80_simt_sgemm_64x64_...` |
| `attention__fmhasm100fkernel_qkvfp16ofp16h128pagedkvcausalp6__aa44949e31` | `attention` | `random_low` | 3.98 | 1 | `fmhaSm100fKernel_QkvFp16OFp16H128PagedKvCausalP64MultiCtasKvVarSeqQ8Kv128StaticSwapsAbForGen` |
| `moe__moe_sum_reduce_kernel_warp_token_topk__43207a7c49` | `moe` | `random_mid`, `sharegpt_mid` | 3.34 | 2 | `void moe_sum_reduce_kernel_warp_token_topk<c10::Half, 8, 4>(c10::Half const*, c10::Half*, lon...` |
| `moe__moe_align_block_size_small_batch_expert_kernel__2c9f928b16` | `moe` | `random_low` | 3.08 | 1 | `void moe_align_block_size_small_batch_expert_kernel<int, 256>(int const*, int*, int*, int*, i...` |
| `norm__fusedaddrmsnormkernel__cb17ae6b12` | `norm` | `random_low`, `random_mid`, `sharegpt_mid`, `sharegpt_high` | 3.00 | 4 | `void flashinfer::norm::FusedAddRMSNormKernel<8u, __half>(__half*, __half*, __half*, unsigned ...` |
| `gemm__cutlass3x_sm100_simt_sgemm_f32_f32_f32_f32_f32_1__b4f87b5018` | `gemm` | `sharegpt_mid` | 2.88 | 1 | `cutlass3x_sm100_simt_sgemm_f32_f32_f32_f32_f32_128x64x16_1x1x1_3_tnn_align1_bias_f32_relu` |
| `comm__comm__515f5a341d` | `comm` | `random_low` | 2.61 | 1 | `void (anonymous namespace)::all_reduce_one_shot_push_kernel<float, 8u, true>((anonymous names...` |

Full shape samples and skipped weak/empty rows are in `kernel_task_index.json`.
