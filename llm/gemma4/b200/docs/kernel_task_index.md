# LLM Kernel Task Index: gemma4 / B200

- Model: `google/gemma-4-26B-A4B-it`
- Evidence threshold: GPU kernel name share strictly `> 2%`.
- Promotion rule: only rows with an external-id-bound non-empty torch-profiler shape are task candidates.
- Weak timestamp/nearest-preceding fallback rows are retained in audit data but are not promoted.

## Workload Coverage

| Workload | Rows | Strong | Weak | Empty shape | Status |
|---|---:|---:|---:|---:|---|
| `random_low` | 11 | 5 | 6 | 0 | partial, promote strong rows only |
| `random_mid` | 10 | 5 | 5 | 0 | partial, promote strong rows only |
| `random_high` | 6 | 1 | 5 | 0 | partial, promote strong rows only |
| `sharegpt_low` | 11 | 2 | 9 | 0 | partial, promote strong rows only |
| `sharegpt_mid` | 8 | 3 | 5 | 0 | partial, promote strong rows only |
| `sharegpt_high` | 5 | 1 | 4 | 0 | partial, promote strong rows only |

## Task Candidates

| Task id | Category | Workloads | Max % GPU | Shape samples | Kernel |
|---|---|---|---:|---:|---|
| `moe__fused_moe_kernel__c581b7d47d` | `moe` | `random_low`, `random_mid`, `random_high`, `sharegpt_low`, `sharegpt_mid`, `sharegpt_high` | 50.81 | 6 | `fused_moe_kernel` |
| `gemm__gemma_qkv_rmsnorm_kernel__c9e8af2caa` | `gemm` | `random_low` | 8.57 | 5 | `_gemma_qkv_rmsnorm_kernel` |
| `quant_gemm__nvjet_sm100_tst_128x192_64x7_2x1_2cta_v_bz_tnt__9c046ec28d` | `quant_gemm` | `random_mid`, `sharegpt_mid` | 7.54 | 3 | `nvjet_sm100_tst_128x192_64x7_2x1_2cta_v_bz_TNT` |
| `quant_gemm__nvjet_sm100_tst_128x256_64x6_2x1_2cta_v_bz_tnt__73699af3d3` | `quant_gemm` | `random_mid`, `sharegpt_mid` | 6.05 | 3 | `nvjet_sm100_tst_128x256_64x6_2x1_2cta_v_bz_TNT` |
| `quant_gemm__nvjet_sm100_tst_256x8_64x6_2x1_v_bz_tnt__7f588c1fef` | `quant_gemm` | `random_low`, `sharegpt_low` | 4.90 | 1 | `nvjet_sm100_tst_256x8_64x6_2x1_v_bz_TNT` |
| `quant_gemm__nvjet_sm100_tst_128x256_64x4_1x2_h_bz_tnt__4e6ebe36b4` | `quant_gemm` | `random_mid` | 3.21 | 1 | `nvjet_sm100_tst_128x256_64x4_1x2_h_bz_TNT` |
| `gemm__kernel_cutlass_kernel_flashinfernormkernelsfused__d54d41be92` | `gemm` | `random_low` | 2.20 | 2 | `kernel_cutlass_kernel_flashinfernormkernelsfused_add_rmsnormFusedAddRMSNormKernel_object_at__...` |
| `other__other__cc8c1ee514` | `other` | `random_mid` | 2.16 | 1 | `void (anonymous namespace)::act_and_mul_kernel<__nv_bfloat16, ((anonymous namespace)::Activat...` |
| `gemm__gemma_dual_rmsnorm_residual_kernel__70a421032f` | `gemm` | `random_low` | 2.11 | 1 | `_gemma_dual_rmsnorm_residual_kernel` |

Full shape samples and skipped weak/empty rows are in `kernel_task_index.json`.
