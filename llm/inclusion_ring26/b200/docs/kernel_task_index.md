# LLM Kernel Task Index: inclusion_ring26 / B200

- Model: `inclusionAI/Ring-2.6-1T`
- Evidence threshold: GPU kernel name share strictly `> 2%`.
- Promotion rule: only rows with an external-id-bound non-empty torch-profiler shape are task candidates.
- Weak timestamp/nearest-preceding fallback rows are retained in audit data but are not promoted.

## Workload Coverage

| Workload | Rows | Strong | Weak | Empty shape | Status |
|---|---:|---:|---:|---:|---|
| `random_low` | 5 | 1 | 4 | 0 | partial, promote strong rows only |
| `random_mid` | 9 | 8 | 1 | 0 | partial, promote strong rows only |
| `random_high` | 8 | 7 | 1 | 0 | partial, promote strong rows only |
| `sharegpt_low` | 5 | 1 | 4 | 0 | partial, promote strong rows only |
| `sharegpt_mid` | 7 | 6 | 1 | 0 | partial, promote strong rows only |
| `sharegpt_high` | 8 | 7 | 1 | 0 | partial, promote strong rows only |

## Task Candidates

| Task id | Category | Workloads | Max % GPU | Shape samples | Kernel |
|---|---|---|---:|---:|---|
| `moe__fused_moe_kernel__c581b7d47d` | `moe` | `random_low`, `random_mid`, `random_high`, `sharegpt_low`, `sharegpt_mid`, `sharegpt_high` | 28.29 | 12 | `fused_moe_kernel` |
| `comm__comm__a12cdaa5b4` | `comm` | `random_mid`, `random_high`, `sharegpt_mid`, `sharegpt_high` | 12.20 | 6 | `void (anonymous namespace)::all_reduce_one_shot_push_kernel<__nv_bfloat16, 8u, true>((anonymo...` |
| `comm__nccldevkernel_allreduce_sum_bf16_ring_ll__05a3ee6241` | `comm` | `random_mid` | 10.10 | 2 | `ncclDevKernel_AllReduce_Sum_bf16_RING_LL(ncclDevKernelArgsStorage<4096ul>)` |
| `comm__comm__c330990d60` | `comm` | `random_mid`, `sharegpt_mid`, `sharegpt_high` | 9.09 | 4 | `void (anonymous namespace)::all_reduce_two_shot_kernel<__nv_bfloat16, 8u, true>(host::distrib...` |
| `gemm__cutlass3x_sm100_simt_sgemm_f32_f32_f32_f32_f32_1__f50cc3eb45` | `gemm` | `random_mid`, `random_high`, `sharegpt_high` | 8.74 | 2 | `cutlass3x_sm100_simt_sgemm_f32_f32_f32_f32_f32_128x128x16_1x1x1_3_tnn_align1_bias_f32_relu` |
| `gemm__zn7cutlass13device_kernelins_4gemm6kernel13gemmu__4de9240811` | `gemm` | `random_mid`, `random_high`, `sharegpt_mid`, `sharegpt_high` | 6.88 | 2 | `_ZN7cutlass13device_kernelINS_4gemm6kernel13GemmUniversalIN4cute5tupleIJiiiiEEENS1_10collecti...` |
| `gemm__cutlass3x_sm100_simt_sgemm_f32_f32_f32_f32_f32_6__d89eb792f0` | `gemm` | `random_high`, `sharegpt_mid` | 6.39 | 3 | `cutlass3x_sm100_simt_sgemm_f32_f32_f32_f32_f32_64x64x16_1x1x1_3_tnn_align1_bias_f32_relu` |
| `quant_gemm__per_token_quant_fp8_kernel__f9fa21beab` | `quant_gemm` | `random_mid`, `random_high`, `sharegpt_mid`, `sharegpt_high` | 4.62 | 6 | `void per_token_quant_fp8_kernel<__nv_bfloat16, __nv_fp8_e4m3, 8, 16, false>(__nv_bfloat16 con...` |
| `moe__moe_sum_reduce_warp_per_token_vec_kernel__3fc4b40863` | `moe` | `random_mid`, `random_high`, `sharegpt_high` | 3.26 | 5 | `void moe_sum_reduce_warp_per_token_vec_kernel<8>(c10::BFloat16 const*, c10::BFloat16*, long, ...` |

Full shape samples and skipped weak/empty rows are in `kernel_task_index.json`.
