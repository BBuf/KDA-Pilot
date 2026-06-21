# LLM Kernel Task Index: minimax_m3 / B200

- Model: `MiniMaxAI/MiniMax-M3-MXFP8`
- Evidence threshold: GPU kernel name share strictly `> 2%`.
- Promotion rule: only rows with an external-id-bound non-empty torch-profiler shape are task candidates.
- Weak timestamp/nearest-preceding fallback rows are retained in audit data but are not promoted.

## Workload Coverage

| Workload | Rows | Strong | Weak | Empty shape | Status |
|---|---:|---:|---:|---:|---|
| `random_low` | 7 | 2 | 3 | 2 | partial, promote strong rows only |
| `random_mid` | 8 | 3 | 1 | 4 | partial, promote strong rows only |
| `random_high` | 8 | 4 | 2 | 2 | partial, promote strong rows only |
| `sharegpt_low` | 7 | 0 | 4 | 3 | weak/empty only, do not promote |
| `sharegpt_mid` | 8 | 4 | 1 | 3 | partial, promote strong rows only |
| `sharegpt_high` | 8 | 3 | 1 | 4 | partial, promote strong rows only |

## Task Candidates

| Task id | Category | Workloads | Max % GPU | Shape samples | Kernel |
|---|---|---|---:|---:|---|
| `comm__comm__a12cdaa5b4` | `comm` | `random_low`, `random_high` | 22.60 | 2 | `void (anonymous namespace)::all_reduce_one_shot_push_kernel<__nv_bfloat16, 8u, true>((anonymo...` |
| `comm__nccldevkernel_allreduce_sum_bf16_ring_ll__05a3ee6241` | `comm` | `random_mid`, `random_high`, `sharegpt_mid`, `sharegpt_high` | 21.06 | 11 | `ncclDevKernel_AllReduce_Sum_bf16_RING_LL(ncclDevKernelArgsStorage<4096ul>)` |
| `quant_gemm__sm100_fp8_fp4_gemm_1d1d_impl__a5fefd5915` | `quant_gemm` | `sharegpt_high` | 12.00 | 1 | `void deep_gemm::sm100_fp8_fp4_gemm_1d1d_impl<(cute::UMMA::Major)0, (cute::UMMA::Major)0, 32u,...` |
| `norm__fusedaddrmsnormkernel__99f19a4e72` | `norm` | `random_mid`, `random_high` | 11.68 | 2 | `void flashinfer::norm::FusedAddRMSNormKernel<8u, __nv_bfloat16>(__nv_bfloat16*, __nv_bfloat16...` |
| `comm__comm__c330990d60` | `comm` | `sharegpt_mid`, `sharegpt_high` | 9.02 | 2 | `void (anonymous namespace)::all_reduce_two_shot_kernel<__nv_bfloat16, 8u, true>(host::distrib...` |
| `quant_gemm__sm100_fp8_fp4_gemm_1d1d_impl__da3d08e584` | `quant_gemm` | `random_low`, `sharegpt_mid` | 8.05 | 2 | `void deep_gemm::sm100_fp8_fp4_gemm_1d1d_impl<(cute::UMMA::Major)0, (cute::UMMA::Major)0, 32u,...` |
| `quant_gemm__mxfp8_block_scaled_matmul_kernel__c1f7ae88f6` | `quant_gemm` | `random_high`, `sharegpt_mid` | 5.85 | 2 | `_mxfp8_block_scaled_matmul_kernel` |
| `gemm__post_reorder_deepgemm_triton_kernel__c1c4bb0a0a` | `gemm` | `random_mid` | 2.78 | 1 | `post_reorder_deepgemm_triton_kernel` |

Full shape samples and skipped weak/empty rows are in `kernel_task_index.json`.
