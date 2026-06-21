# LLM Kernel Task Index: nemotron3_super / B200

- Model: `nvidia/NVIDIA-Nemotron-3-Super-120B-A12B-BF16`
- Evidence threshold: GPU kernel name share strictly `> 2%`.
- Promotion rule: only rows with an external-id-bound non-empty torch-profiler shape are task candidates.
- Weak timestamp/nearest-preceding fallback rows are retained in audit data but are not promoted.

## Workload Coverage

| Workload | Rows | Strong | Weak | Empty shape | Status |
|---|---:|---:|---:|---:|---|
| `random_low` | 10 | 4 | 6 | 0 | partial, promote strong rows only |
| `random_mid` | 13 | 11 | 2 | 0 | partial, promote strong rows only |
| `random_high` | 13 | 11 | 2 | 0 | partial, promote strong rows only |
| `sharegpt_low` | 10 | 1 | 9 | 0 | partial, promote strong rows only |
| `sharegpt_mid` | 12 | 8 | 4 | 0 | partial, promote strong rows only |
| `sharegpt_high` | 9 | 8 | 1 | 0 | partial, promote strong rows only |

## Task Candidates

| Task id | Category | Workloads | Max % GPU | Shape samples | Kernel |
|---|---|---|---:|---:|---|
| `comm__comm__0821f7c6e6` | `comm` | `random_low`, `random_mid`, `random_high`, `sharegpt_low`, `sharegpt_mid`, `sharegpt_high` | 35.59 | 8 | `void (anonymous namespace)::all_reduce_one_shot_push_kernel<__nv_bfloat16, 4u, true>((anonymo...` |
| `other__chunk_scan_fwd_kernel__e84657f454` | `other` | `random_mid`, `random_high`, `sharegpt_mid` | 12.59 | 12 | `_chunk_scan_fwd_kernel` |
| `comm__nccldevkernel_allreduce_sum_bf16_ring_ll__05a3ee6241` | `comm` | `random_mid`, `random_high`, `sharegpt_mid`, `sharegpt_high` | 10.41 | 9 | `ncclDevKernel_AllReduce_Sum_bf16_RING_LL(ncclDevKernelArgsStorage<4096ul>)` |
| `norm__fusedaddrmsnormkernel__99f19a4e72` | `norm` | `random_low`, `random_mid` | 8.85 | 2 | `void flashinfer::norm::FusedAddRMSNormKernel<8u, __nv_bfloat16>(__nv_bfloat16*, __nv_bfloat16...` |
| `other__chunk_state_fwd_kernel__0be5776788` | `other` | `random_mid`, `random_high`, `sharegpt_mid` | 8.40 | 12 | `_chunk_state_fwd_kernel` |
| `other__bmm_bfloat16_bfloat16bfloat16_fp32_t128x64x128u2__92e5ff29e3` | `other` | `random_mid`, `random_high`, `sharegpt_mid`, `sharegpt_high` | 7.54 | 4 | `bmm_Bfloat16_Bfloat16Bfloat16_Fp32_t128x64x128u2_s5_et128x64_m256x64x16_c2x1x1_rM_BN_transOut...` |
| `other__bmm_bfloat16_bfloat16bfloat16_fp32_t128x64x128u2__605c1c0504` | `other` | `random_mid`, `sharegpt_high` | 7.13 | 2 | `bmm_Bfloat16_Bfloat16Bfloat16_Fp32_t128x64x128u2_s5_et128x64_m256x64x16_c2x1x1_rM_BN_transOut...` |
| `comm__comm__9dd2e02622` | `comm` | `random_mid`, `random_high`, `sharegpt_mid`, `sharegpt_high` | 6.93 | 7 | `void (anonymous namespace)::all_reduce_two_shot_kernel<__nv_bfloat16, 4u, true>(host::distrib...` |
| `other__state_passing_fwd_kernel__535fed3fd8` | `other` | `random_mid`, `random_high`, `sharegpt_mid` | 6.26 | 12 | `_state_passing_fwd_kernel` |
| `quant_gemm__nvjet_sm100_tst_128x256_64x6_2x1_2cta_v_bz_tnt__73699af3d3` | `quant_gemm` | `random_mid`, `random_high`, `sharegpt_mid`, `sharegpt_high` | 6.24 | 10 | `nvjet_sm100_tst_128x256_64x6_2x1_2cta_v_bz_TNT` |
| `quant_gemm__nvjet_sm100_tst_160x192_64x6_1x2_2cta_h_bz_tnn__e63cf68359` | `quant_gemm` | `random_mid`, `random_high`, `sharegpt_high` | 3.48 | 7 | `nvjet_sm100_tst_160x192_64x6_1x2_2cta_h_bz_TNN` |
| `other__bmm_bfloat16_bfloat16bfloat16_fp32_t128x16x128u2__fcc001e5b0` | `other` | `random_low` | 2.99 | 1 | `bmm_Bfloat16_Bfloat16Bfloat16_Fp32_t128x16x128u2_s4_et128x16_m128x16x16_c1x1x1_rM_BN_transOut...` |
| `moe__finalizekernel__03599d3c6d` | `moe` | `random_low` | 2.47 | 1 | `void moe::dev::finalize::finalizeKernel<moe::dev::finalize::KernelParams<cutlass::bfloat16_t,...` |
| `other__bmm_bfloat16_bfloat16bfloat16_fp32_t128x16x128u2__6c1e8996fe` | `other` | `random_high` | 2.38 | 1 | `bmm_Bfloat16_Bfloat16Bfloat16_Fp32_t128x16x128u2_s6_et128x16_m128x16x16_c1x1x1_rM_BN_transOut...` |
| `moe__finalizekernelvecload__600eb198a7` | `moe` | `random_high`, `sharegpt_high` | 2.24 | 2 | `void moe::dev::finalize::finalizeKernelVecLoad<moe::dev::finalize::KernelParams<cutlass::bflo...` |

Full shape samples and skipped weak/empty rows are in `kernel_task_index.json`.
