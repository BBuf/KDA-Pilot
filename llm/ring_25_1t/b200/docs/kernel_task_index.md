# LLM Kernel Task Index: ring_25_1t / B200

- Model: `inclusionAI/Ring-2.5-1T`
- Evidence threshold: GPU kernel name share strictly `> 2%`.
- Promotion rule: only rows with an external-id-bound non-empty torch-profiler shape are task candidates.
- Weak timestamp/nearest-preceding fallback rows are retained in audit data but are not promoted.

## Workload Coverage

| Workload | Rows | Strong | Weak | Empty shape | Status |
|---|---:|---:|---:|---:|---|
| `random_low` | 5 | 3 | 2 | 0 | partial, promote strong rows only |
| `random_mid` | 7 | 5 | 2 | 0 | partial, promote strong rows only |
| `random_high` | 7 | 6 | 1 | 0 | partial, promote strong rows only |
| `sharegpt_low` | 5 | 2 | 3 | 0 | partial, promote strong rows only |
| `sharegpt_mid` | 9 | 7 | 2 | 0 | partial, promote strong rows only |
| `sharegpt_high` | 7 | 6 | 1 | 0 | partial, promote strong rows only |

## Task Candidates

| Task id | Category | Workloads | Max % GPU | Shape samples | Kernel |
|---|---|---|---:|---:|---|
| `moe__fused_moe_kernel__c581b7d47d` | `moe` | `random_low`, `random_mid`, `random_high`, `sharegpt_low`, `sharegpt_mid`, `sharegpt_high` | 32.31 | 12 | `fused_moe_kernel` |
| `comm__comm__a12cdaa5b4` | `comm` | `random_low`, `random_mid`, `sharegpt_low`, `sharegpt_mid`, `sharegpt_high` | 31.39 | 4 | `void (anonymous namespace)::all_reduce_one_shot_push_kernel<__nv_bfloat16, 8u, true>((anonymo...` |
| `gemm__kernel_cutlass_kernel_flashinfernormkernelsfused__b25a796c5c` | `gemm` | `random_low` | 27.79 | 2 | `kernel_cutlass_kernel_flashinfernormkernelsfused_add_rmsnormFusedAddRMSNormKernel_object_at__...` |
| `comm__comm__c330990d60` | `comm` | `sharegpt_high` | 15.99 | 1 | `void (anonymous namespace)::all_reduce_two_shot_kernel<__nv_bfloat16, 8u, true>(host::distrib...` |
| `gemm__cutlass3x_sm100_simt_sgemm_f32_f32_f32_f32_f32_1__f50cc3eb45` | `gemm` | `random_high`, `sharegpt_mid` | 10.76 | 3 | `cutlass3x_sm100_simt_sgemm_f32_f32_f32_f32_f32_128x128x16_1x1x1_3_tnn_align1_bias_f32_relu` |
| `gemm__cutlass3x_sm100_simt_sgemm_f32_f32_f32_f32_f32_6__d89eb792f0` | `gemm` | `random_mid` | 7.57 | 2 | `cutlass3x_sm100_simt_sgemm_f32_f32_f32_f32_f32_64x64x16_1x1x1_3_tnn_align1_bias_f32_relu` |
| `gemm__zn7cutlass13device_kernelins_4gemm6kernel13gemmu__4de9240811` | `gemm` | `random_mid`, `random_high`, `sharegpt_mid`, `sharegpt_high` | 6.93 | 5 | `_ZN7cutlass13device_kernelINS_4gemm6kernel13GemmUniversalIN4cute5tupleIJiiiiEEENS1_10collecti...` |
| `memory_bound__unrolled_elementwise_kernel__64bf90af3d` | `memory_bound` | `random_high`, `sharegpt_mid` | 4.96 | 4 | `void at::native::unrolled_elementwise_kernel<at::native::direct_copy_kernel_cuda(at::TensorIt...` |
| `quant_gemm__per_token_quant_fp8_kernel__f9fa21beab` | `quant_gemm` | `random_mid`, `random_high`, `sharegpt_mid` | 4.37 | 9 | `void per_token_quant_fp8_kernel<__nv_bfloat16, __nv_fp8_e4m3, 8, 16, false>(__nv_bfloat16 con...` |
| `moe__moe_sum_reduce_warp_per_token_vec_kernel__3fc4b40863` | `moe` | `random_high`, `sharegpt_mid` | 3.25 | 5 | `void moe_sum_reduce_warp_per_token_vec_kernel<8>(c10::BFloat16 const*, c10::BFloat16*, long, ...` |
| `gemm__cutlass3x_sm100_simt_sgemm_f32_f32_f32_f32_f32_1__b4f87b5018` | `gemm` | `sharegpt_high` | 3.03 | 2 | `cutlass3x_sm100_simt_sgemm_f32_f32_f32_f32_f32_128x64x16_1x1x1_3_tnn_align1_bias_f32_relu` |
| `gemm__zn7cutlass13device_kernelins_4gemm6kernel13gemmu__12e4691976` | `gemm` | `sharegpt_high` | 2.18 | 1 | `_ZN7cutlass13device_kernelINS_4gemm6kernel13GemmUniversalIN4cute5tupleIJiiiiEEENS1_10collecti...` |

Full shape samples and skipped weak/empty rows are in `kernel_task_index.json`.
