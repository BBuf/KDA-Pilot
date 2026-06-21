# LLM Kernel Task Index: glm_5 / B200

- Model: `nvidia/GLM-5-NVFP4`
- Evidence threshold: GPU kernel name share strictly `> 2%`.
- Promotion rule: only rows with an external-id-bound non-empty torch-profiler shape are task candidates.
- Weak timestamp/nearest-preceding fallback rows are retained in audit data but are not promoted.

## Workload Coverage

| Workload | Rows | Strong | Weak | Empty shape | Status |
|---|---:|---:|---:|---:|---|
| `random_low` | 12 | 1 | 9 | 2 | partial, promote strong rows only |
| `random_mid` | 10 | 3 | 5 | 2 | partial, promote strong rows only |
| `random_high` | 8 | 3 | 5 | 0 | partial, promote strong rows only |
| `sharegpt_low` | 11 | 0 | 8 | 3 | weak/empty only, do not promote |
| `sharegpt_mid` | 12 | 3 | 7 | 2 | partial, promote strong rows only |
| `sharegpt_high` | 10 | 3 | 5 | 2 | partial, promote strong rows only |

## Task Candidates

| Task id | Category | Workloads | Max % GPU | Shape samples | Kernel |
|---|---|---|---:|---:|---|
| `quant_gemm__nvjet_sm100_tst_128x256_64x6_2x1_2cta_v_bz_tnt__73699af3d3` | `quant_gemm` | `random_mid`, `random_high`, `sharegpt_mid`, `sharegpt_high` | 18.55 | 12 | `nvjet_sm100_tst_128x256_64x6_2x1_2cta_v_bz_TNT` |
| `comm__nccldevkernel_allreduce_sum_bf16_ring_ll__05a3ee6241` | `comm` | `sharegpt_mid` | 14.65 | 4 | `ncclDevKernel_AllReduce_Sum_bf16_RING_LL(ncclDevKernelArgsStorage<4096ul>)` |
| `other__other__00ff8f7a29` | `other` | `sharegpt_mid`, `sharegpt_high` | 3.73 | 6 | `void (anonymous namespace)::fast_hadamard_transform_kernel<(anonymous namespace)::FastHadamar...` |
| `quant_gemm__kernel_cutlass_kernel_flashinferquantizationkern__71028ab958` | `quant_gemm` | `random_low` | 2.98 | 1 | `kernel_cutlass_kernel_flashinferquantizationkernelsnvfp4_quantizeNVFP4QuantizeSwizzledKernel_...` |
| `quant_gemm__nvjet_sm100_tst_192x288_64x5_2x1_2cta_v_bz_tnt__e6357e6463` | `quant_gemm` | `sharegpt_high` | 2.62 | 3 | `nvjet_sm100_tst_192x288_64x5_2x1_2cta_v_bz_TNT` |
| `quant_gemm__nvjet_sm100_tst_256x128_64x5_2x2_2cta_h_bz_tnt__d6cc26eceb` | `quant_gemm` | `random_mid` | 2.40 | 1 | `nvjet_sm100_tst_256x128_64x5_2x2_2cta_h_bz_TNT` |
| `gemm__kernel_cutlass_kernel_flashinfergemmkernelsdense__e9481e7b7d` | `gemm` | `random_mid`, `random_high` | 2.26 | 4 | `kernel_cutlass_kernel_flashinfergemmkernelsdense_blockscaled_gemm_sm100Sm100BlockScaledPersis...` |
| `comm__allreduce_fusion_kernel_twoshot_sync__022bef8d42` | `comm` | `random_high` | 2.02 | 1 | `void flashinfer::trtllm_allreduce_fusion::allreduce_fusion_kernel_twoshot_sync<(flashinfer::t...` |

Full shape samples and skipped weak/empty rows are in `kernel_task_index.json`.
