# LLM Kernel Task Index: kimi_linear / B200

- Model: `moonshotai/Kimi-Linear-48B-A3B-Instruct`
- Evidence threshold: GPU kernel name share strictly `> 2%`.
- Promotion rule: only rows with an external-id-bound non-empty torch-profiler shape are task candidates.
- Weak timestamp/nearest-preceding fallback rows are retained in audit data but are not promoted.

## Workload Coverage

| Workload | Rows | Strong | Weak | Empty shape | Status |
|---|---:|---:|---:|---:|---|
| `random_low` | 10 | 2 | 8 | 0 | partial, promote strong rows only |
| `random_mid` | 0 | 0 | 0 | 0 | no >2% SGLang/actionable row |
| `random_high` | 5 | 4 | 1 | 0 | partial, promote strong rows only |
| `sharegpt_low` | 6 | 4 | 2 | 0 | partial, promote strong rows only |
| `sharegpt_mid` | 3 | 3 | 0 | 0 | strong |
| `sharegpt_high` | 8 | 5 | 3 | 0 | partial, promote strong rows only |

## Task Candidates

| Task id | Category | Workloads | Max % GPU | Shape samples | Kernel |
|---|---|---|---:|---:|---|
| `comm__comm__0821f7c6e6` | `comm` | `random_high`, `sharegpt_low`, `sharegpt_mid`, `sharegpt_high` | 50.27 | 5 | `void (anonymous namespace)::all_reduce_one_shot_push_kernel<__nv_bfloat16, 4u, true>((anonymo...` |
| `moe__fused_moe_kernel__c581b7d47d` | `moe` | `random_low`, `random_high`, `sharegpt_low`, `sharegpt_mid`, `sharegpt_high` | 26.35 | 12 | `fused_moe_kernel` |
| `norm__fusedaddrmsnormkernel__99f19a4e72` | `norm` | `sharegpt_low`, `sharegpt_mid` | 25.98 | 3 | `void flashinfer::norm::FusedAddRMSNormKernel<8u, __nv_bfloat16>(__nv_bfloat16*, __nv_bfloat16...` |
| `other__other__56d7fd43dd` | `other` | `random_low` | 3.37 | 1 | `void (anonymous namespace)::act_and_mul_kernel<__nv_bfloat16, ((anonymous namespace)::Activat...` |
| `comm__comm__9dd2e02622` | `comm` | `sharegpt_high` | 3.05 | 2 | `void (anonymous namespace)::all_reduce_two_shot_kernel<__nv_bfloat16, 4u, true>(host::distrib...` |
| `quant_gemm__nvjet_sm100_tst_128x256_64x6_2x1_2cta_v_bz_tnt__73699af3d3` | `quant_gemm` | `random_high`, `sharegpt_high` | 2.88 | 12 | `nvjet_sm100_tst_128x256_64x6_2x1_2cta_v_bz_TNT` |
| `moe__moe_sum_reduce_warp_per_token_vec_kernel__3fc4b40863` | `moe` | `random_high`, `sharegpt_high` | 2.47 | 12 | `void moe_sum_reduce_warp_per_token_vec_kernel<8>(c10::BFloat16 const*, c10::BFloat16*, long, ...` |
| `quant_gemm__nvjet_sm100_tst_32x64_64x16_4x1_v_bz_splitk_tnn__0fa651efdd` | `quant_gemm` | `sharegpt_low` | 2.04 | 1 | `nvjet_sm100_tst_32x64_64x16_4x1_v_bz_splitK_TNN` |

Full shape samples and skipped weak/empty rows are in `kernel_task_index.json`.
