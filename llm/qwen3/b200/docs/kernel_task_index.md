# LLM Kernel Task Index: qwen3 / B200

- Model: `Qwen/Qwen3-235B-A22B-Instruct-2507`
- Evidence threshold: GPU kernel name share strictly `> 2%`.
- Promotion rule: only rows with an external-id-bound non-empty torch-profiler shape are task candidates.
- Weak timestamp/nearest-preceding fallback rows are retained in audit data but are not promoted.

## Workload Coverage

| Workload | Rows | Strong | Weak | Empty shape | Status |
|---|---:|---:|---:|---:|---|
| `random_low` | 14 | 5 | 9 | 0 | partial, promote strong rows only |
| `random_mid` | 13 | 5 | 8 | 0 | partial, promote strong rows only |
| `random_high` | 14 | 6 | 8 | 0 | partial, promote strong rows only |
| `sharegpt_low` | 12 | 3 | 9 | 0 | partial, promote strong rows only |
| `sharegpt_mid` | 12 | 5 | 7 | 0 | partial, promote strong rows only |
| `sharegpt_high` | 15 | 2 | 13 | 0 | partial, promote strong rows only |

## Task Candidates

| Task id | Category | Workloads | Max % GPU | Shape samples | Kernel |
|---|---|---|---:|---:|---|
| `comm__allreduce_fusion_kernel_oneshot_lamport__b9d8384154` | `comm` | `random_low`, `random_mid`, `random_high`, `sharegpt_low`, `sharegpt_mid` | 20.02 | 6 | `void flashinfer::trtllm_allreduce_fusion::allreduce_fusion_kernel_oneshot_lamport<(flashinfer...` |
| `comm__nccldevkernel_allreduce_sum_bf16_ring_ll__05a3ee6241` | `comm` | `random_mid`, `sharegpt_mid` | 17.77 | 2 | `ncclDevKernel_AllReduce_Sum_bf16_RING_LL(ncclDevKernelArgsStorage<4096ul>)` |
| `other__bmm_bfloat16_bfloat16bfloat16_fp32_t128x64x128u2__6847e74d41` | `other` | `random_high` | 5.71 | 1 | `bmm_Bfloat16_Bfloat16Bfloat16_Fp32_t128x64x128u2_s5_et128x64_m256x64x16_c2x1x1_rM_BN_transOut...` |
| `comm__allreduce_fusion_kernel_twoshot_sync__c36567c3ee` | `comm` | `random_mid`, `random_high` | 5.54 | 2 | `void flashinfer::trtllm_allreduce_fusion::allreduce_fusion_kernel_twoshot_sync<(flashinfer::t...` |
| `attention__fmhasm100fkernel_qkvbfloat16obfloat16h128pagedkv__714e7067df` | `attention` | `random_high`, `sharegpt_mid`, `sharegpt_high` | 5.22 | 12 | `fmhaSm100fKernel_QkvBfloat16OBfloat16H128PagedKvCausalP64VarSeqQ128Kv128PersistentContext` |
| `comm__comm__c330990d60` | `comm` | `sharegpt_high` | 4.46 | 2 | `void (anonymous namespace)::all_reduce_two_shot_kernel<__nv_bfloat16, 8u, true>(host::distrib...` |
| `moe__finalizekernel__6a7a068b8f` | `moe` | `random_low` | 4.28 | 1 | `void moe::dev::finalize::finalizeKernel<moe::dev::finalize::KernelParams<cutlass::bfloat16_t,...` |
| `moe__finalizekernelvecload__00edba12eb` | `moe` | `random_mid`, `random_high`, `sharegpt_mid` | 4.08 | 3 | `void moe::dev::finalize::finalizeKernelVecLoad<moe::dev::finalize::KernelParams<cutlass::bflo...` |
| `quant_gemm__nvjet_sm100_tst_64x8_64x16_2x4_h_bz_splitk_tnt__9c371f4925` | `quant_gemm` | `sharegpt_low` | 4.03 | 1 | `nvjet_sm100_tst_64x8_64x16_2x4_h_bz_splitK_TNT` |
| `other__bmm_bfloat16_bfloat16bfloat16_fp32_t128x64x128_s__752b69c4ca` | `other` | `random_high`, `sharegpt_mid` | 3.96 | 2 | `bmm_Bfloat16_Bfloat16Bfloat16_Fp32_t128x64x128_s5_et128x64_m256x64x16_c2x1x1_rM_BN_transOut_s...` |
| `other__bmm_bfloat16_bfloat16bfloat16_fp32_t128x8x128u2__7b9748cb9a` | `other` | `random_low` | 3.75 | 1 | `bmm_Bfloat16_Bfloat16Bfloat16_Fp32_t128x8x128u2_s5_et128x8_m128x8x16_c1x1x1_rM_BN_transOut_sc...` |
| `other__bmm_bfloat16_bfloat16bfloat16_fp32_t128x8x128_s5__5a06314350` | `other` | `random_low` | 2.23 | 1 | `bmm_Bfloat16_Bfloat16Bfloat16_Fp32_t128x8x128_s5_et128x8_m128x8x16_c1x1x1_rM_BN_transOut_schP...` |
| `quant_gemm__nvjet_sm100_tst_64x16_64x16_2x4_2cta_h_bz_splitk__6dd18c84c0` | `quant_gemm` | `random_low` | 2.19 | 1 | `nvjet_sm100_tst_64x16_64x16_2x4_2cta_h_bz_splitK_TNT` |
| `quant_gemm__nvjet_sm100_tst_128x256_64x6_2x1_2cta_v_bz_tnt__73699af3d3` | `quant_gemm` | `random_mid` | 2.08 | 1 | `nvjet_sm100_tst_128x256_64x6_2x1_2cta_v_bz_TNT` |
| `quant_gemm__nvjet_sm100_tst_64x16_64x16_2x2_2cta_h_bz_tnt__fcf149f0b2` | `quant_gemm` | `sharegpt_low` | 2.03 | 1 | `nvjet_sm100_tst_64x16_64x16_2x2_2cta_h_bz_TNT` |

Full shape samples and skipped weak/empty rows are in `kernel_task_index.json`.
