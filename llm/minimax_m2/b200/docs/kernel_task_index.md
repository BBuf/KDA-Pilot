# LLM Kernel Task Index: minimax_m2 / B200

- Model: `MiniMaxAI/MiniMax-M2`
- Evidence threshold: GPU kernel name share strictly `> 2%`.
- Promotion rule: only rows with an external-id-bound non-empty torch-profiler shape are task candidates.
- Weak timestamp/nearest-preceding fallback rows are retained in audit data but are not promoted.

## Workload Coverage

| Workload | Rows | Strong | Weak | Empty shape | Status |
|---|---:|---:|---:|---:|---|
| `random_low` | 8 | 7 | 1 | 0 | partial, promote strong rows only |
| `random_mid` | 8 | 8 | 0 | 0 | strong |
| `random_high` | 9 | 6 | 3 | 0 | partial, promote strong rows only |
| `sharegpt_low` | 8 | 5 | 3 | 0 | partial, promote strong rows only |
| `sharegpt_mid` | 9 | 9 | 0 | 0 | strong |
| `sharegpt_high` | 9 | 8 | 1 | 0 | partial, promote strong rows only |

## Task Candidates

| Task id | Category | Workloads | Max % GPU | Shape samples | Kernel |
|---|---|---|---:|---:|---|
| `moe__fused_moe_kernel__c581b7d47d` | `moe` | `random_low`, `random_mid`, `random_high`, `sharegpt_low`, `sharegpt_mid`, `sharegpt_high` | 48.15 | 6 | `fused_moe_kernel` |
| `quant_gemm__w8a8_block_fp8_matmul__c1e3573b4b` | `quant_gemm` | `random_mid`, `random_high`, `sharegpt_low`, `sharegpt_mid`, `sharegpt_high` | 22.81 | 5 | `_w8a8_block_fp8_matmul` |
| `comm__comm__554010158e` | `comm` | `random_low`, `random_mid`, `random_high`, `sharegpt_low`, `sharegpt_high` | 7.54 | 6 | `void (anonymous namespace)::all_reduce_one_shot_push_kernel<__half, 4u, true>((anonymous name...` |
| `gemm__cutlass3x_sm100_simt_sgemm_f32_f32_f32_f32_f32_6__d89eb792f0` | `gemm` | `random_mid` | 6.38 | 1 | `cutlass3x_sm100_simt_sgemm_f32_f32_f32_f32_f32_64x64x16_1x1x1_3_tnn_align1_bias_f32_relu` |
| `gemm__kernel_cutlass_kernel_flashinfernormkernelsfused__7e8fbc5467` | `gemm` | `random_low` | 6.18 | 1 | `kernel_cutlass_kernel_flashinfernormkernelsfused_add_rmsnormFusedAddRMSNormKernel_object_at__...` |
| `gemm__kernel2__57e9da75e7` | `gemm` | `random_low`, `random_mid`, `sharegpt_low`, `sharegpt_mid`, `sharegpt_high` | 5.05 | 6 | `void cutlass::Kernel2<cutlass_80_simt_sgemm_64x64_8x5_tn_align1>(cutlass_80_simt_sgemm_64x64_...` |
| `quant_gemm__quant_gemm__067e4625ab` | `quant_gemm` | `random_low`, `random_mid`, `sharegpt_mid` | 4.72 | 3 | `void (anonymous namespace)::per_token_group_quant_8bit_v2_kernel<(anonymous namespace)::Naive...` |
| `attention__fmhasm100fkernel_qkvfp16ofp16h128pagedkvcausalp6__aa44949e31` | `attention` | `random_low` | 4.53 | 1 | `fmhaSm100fKernel_QkvFp16OFp16H128PagedKvCausalP64MultiCtasKvVarSeqQ8Kv128StaticSwapsAbForGen` |
| `gemm__cutlass3x_sm100_simt_sgemm_f32_f32_f32_f32_f32_6__79fc92c9dd` | `gemm` | `sharegpt_mid` | 4.16 | 1 | `cutlass3x_sm100_simt_sgemm_f32_f32_f32_f32_f32_64x32x16_1x1x1_3_tnn_align1_bias_f32_relu` |
| `attention__fmhasm100fkernel_qkvfp16ofp16h128pagedkvcausalp6__073fbd3338` | `attention` | `random_high`, `sharegpt_mid`, `sharegpt_high` | 3.47 | 11 | `fmhaSm100fKernel_QkvFp16OFp16H128PagedKvCausalP64VarSeqQ128Kv128PersistentContext` |
| `comm__comm__510fc180fc` | `comm` | `random_high`, `sharegpt_high` | 3.47 | 2 | `void (anonymous namespace)::all_reduce_two_shot_kernel<__half, 4u, true>(host::distributed::A...` |
| `gemm__cutlass3x_sm100_simt_sgemm_f32_f32_f32_f32_f32_1__b4f87b5018` | `gemm` | `random_high`, `sharegpt_mid`, `sharegpt_high` | 3.02 | 3 | `cutlass3x_sm100_simt_sgemm_f32_f32_f32_f32_f32_128x64x16_1x1x1_3_tnn_align1_bias_f32_relu` |
| `moe__moe_sum_reduce_kernel_warp_token_topk__43207a7c49` | `moe` | `random_mid`, `sharegpt_mid` | 2.83 | 2 | `void moe_sum_reduce_kernel_warp_token_topk<c10::Half, 8, 4>(c10::Half const*, c10::Half*, lon...` |
| `norm__fusedaddrmsnormkernel__cb17ae6b12` | `norm` | `random_mid`, `sharegpt_mid`, `sharegpt_high` | 2.76 | 6 | `void flashinfer::norm::FusedAddRMSNormKernel<8u, __half>(__half*, __half*, __half*, unsigned ...` |
| `comm__comm__8929060cd4` | `comm` | `random_low`, `sharegpt_low` | 2.73 | 2 | `void (anonymous namespace)::all_reduce_one_shot_push_kernel<float, 4u, true>((anonymous names...` |

Full shape samples and skipped weak/empty rows are in `kernel_task_index.json`.
