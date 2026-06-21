# LLM Kernel Task Index: deepseek_v32 / B200

- Model: `nvidia/DeepSeek-V3.2-NVFP4`
- Evidence threshold: GPU kernel name share strictly `> 2%`.
- Promotion rule: only rows with an external-id-bound non-empty torch-profiler shape are task candidates.
- Weak timestamp/nearest-preceding fallback rows are retained in audit data but are not promoted.

## Workload Coverage

| Workload | Rows | Strong | Weak | Empty shape | Status |
|---|---:|---:|---:|---:|---|
| `random_low` | 10 | 1 | 5 | 4 | partial, promote strong rows only |
| `random_mid` | 7 | 4 | 3 | 0 | partial, promote strong rows only |
| `random_high` | 12 | 4 | 6 | 2 | partial, promote strong rows only |
| `sharegpt_low` | 10 | 0 | 6 | 4 | weak/empty only, do not promote |
| `sharegpt_mid` | 12 | 4 | 6 | 2 | partial, promote strong rows only |
| `sharegpt_high` | 12 | 5 | 3 | 4 | partial, promote strong rows only |

## Task Candidates

| Task id | Category | Workloads | Max % GPU | Shape samples | Kernel |
|---|---|---|---:|---:|---|
| `comm__nccldevkernel_allreduce_sum_bf16_ring_ll__05a3ee6241` | `comm` | `random_mid`, `sharegpt_mid` | 57.13 | 7 | `ncclDevKernel_AllReduce_Sum_bf16_RING_LL(ncclDevKernelArgsStorage<4096ul>)` |
| `comm__allreduce_fusion_kernel_twoshot_sync__022bef8d42` | `comm` | `random_high`, `sharegpt_high` | 7.20 | 3 | `void flashinfer::trtllm_allreduce_fusion::allreduce_fusion_kernel_twoshot_sync<(flashinfer::t...` |
| `attention__fmhasm100fkernel_qkve4m3obfloat16hqk576hv512page__ff06b37547` | `attention` | `random_high`, `sharegpt_high` | 6.49 | 12 | `fmhaSm100fKernel_QkvE4m3OBfloat16HQk576HV512PagedKvDenseStaticTokenSparseP1VarSeqQ32Kv128Pers...` |
| `quant_gemm__bmm_e2m1_e2m1e2m1_fp32_ab16_bb16_cb16_t128x128x5__4ad8ff352d` | `quant_gemm` | `sharegpt_high` | 4.41 | 1 | `bmm_E2m1_E2m1E2m1_Fp32_Ab16_Bb16_Cb16_t128x128x512_s3x3x3x3x1x3_et128x32_m256x128x64_c2x1x1_r...` |
| `other__other__00ff8f7a29` | `other` | `sharegpt_mid` | 4.04 | 2 | `void (anonymous namespace)::fast_hadamard_transform_kernel<(anonymous namespace)::FastHadamar...` |
| `gemm__kernel_cutlass_kernel_flashinfergemmkernelsdense__e9481e7b7d` | `gemm` | `random_mid`, `sharegpt_mid` | 3.57 | 6 | `kernel_cutlass_kernel_flashinfergemmkernelsdense_blockscaled_gemm_sm100Sm100BlockScaledPersis...` |
| `quant_gemm__kernel_cutlass_kernel_flashinferquantizationkern__48d759a0a4` | `quant_gemm` | `random_low` | 3.19 | 1 | `kernel_cutlass_kernel_flashinferquantizationkernelsnvfp4_quantizeNVFP4QuantizeSwizzledKernel_...` |
| `comm__allreduce_fusion_kernel_oneshot_lamport__3a58812ac0` | `comm` | `random_mid` | 3.02 | 1 | `void flashinfer::trtllm_allreduce_fusion::allreduce_fusion_kernel_oneshot_lamport<(flashinfer...` |
| `quant_gemm__nvjet_sm100_tst_128x256_64x6_2x1_2cta_v_bz_tnt__73699af3d3` | `quant_gemm` | `random_high` | 2.79 | 3 | `nvjet_sm100_tst_128x256_64x6_2x1_2cta_v_bz_TNT` |
| `gemm__kernel_cutlass_kernel_flashinfergemmkernelsdense__dcb59f24e5` | `gemm` | `random_high`, `sharegpt_high` | 2.61 | 3 | `kernel_cutlass_kernel_flashinfergemmkernelsdense_blockscaled_gemm_sm100Sm100BlockScaledPersis...` |
| `quant_gemm__bmm_bfloat16_e2m1e2m1_fp32_ab16_bb16_t128x32x512__5ea7167b72` | `quant_gemm` | `sharegpt_high` | 2.54 | 1 | `bmm_Bfloat16_E2m1E2m1_Fp32_Ab16_Bb16_t128x32x512_s4_et128x32_m256x32x64_c2x1x1_rM_TN_transOut...` |
| `quant_gemm__nvjet_sm100_tst_128x256_64x4_1x2_h_bz_tnt__4e6ebe36b4` | `quant_gemm` | `sharegpt_mid` | 2.17 | 1 | `nvjet_sm100_tst_128x256_64x4_1x2_h_bz_TNT` |
| `quant_gemm__nvjet_sm100_tst_64x16_64x16_2x4_2cta_h_bz_splitk__6dd18c84c0` | `quant_gemm` | `random_mid` | 2.00 | 1 | `nvjet_sm100_tst_64x16_64x16_2x4_2cta_h_bz_splitK_TNT` |

Full shape samples and skipped weak/empty rows are in `kernel_task_index.json`.
