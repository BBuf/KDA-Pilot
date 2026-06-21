# LLM Kernel Task Index: step35_flash / B200

- Model: `stepfun-ai/Step-3.5-Flash`
- Evidence threshold: GPU kernel name share strictly `> 2%`.
- Promotion rule: only rows with an external-id-bound non-empty torch-profiler shape are task candidates.
- Weak timestamp/nearest-preceding fallback rows are retained in audit data but are not promoted.

## Workload Coverage

| Workload | Rows | Strong | Weak | Empty shape | Status |
|---|---:|---:|---:|---:|---|
| `random_low` | 6 | 6 | 0 | 0 | strong |
| `random_mid` | 6 | 3 | 3 | 0 | partial, promote strong rows only |
| `random_high` | 6 | 4 | 2 | 0 | partial, promote strong rows only |
| `sharegpt_low` | 6 | 4 | 2 | 0 | partial, promote strong rows only |
| `sharegpt_mid` | 6 | 4 | 2 | 0 | partial, promote strong rows only |
| `sharegpt_high` | 6 | 3 | 3 | 0 | partial, promote strong rows only |

## Task Candidates

| Task id | Category | Workloads | Max % GPU | Shape samples | Kernel |
|---|---|---|---:|---:|---|
| `memory_bound__cross_device_reduce_1stage__3aeea98c14` | `memory_bound` | `random_low`, `random_mid`, `random_high`, `sharegpt_low`, `sharegpt_mid`, `sharegpt_high` | 49.34 | 7 | `void sglang::cross_device_reduce_1stage<__nv_bfloat16, 4>(sglang::RankData*, sglang::RankSign...` |
| `moe__fused_moe_kernel__c581b7d47d` | `moe` | `random_low`, `random_mid`, `random_high`, `sharegpt_low`, `sharegpt_mid`, `sharegpt_high` | 16.13 | 4 | `fused_moe_kernel` |
| `quant_gemm__nvjet_tst_32x64_64x16_4x1_v_bz_tnn__c85dd5ae4a` | `quant_gemm` | `random_low`, `sharegpt_low`, `sharegpt_mid`, `sharegpt_high` | 4.30 | 6 | `nvjet_tst_32x64_64x16_4x1_v_bz_TNN` |
| `norm__rmsnormkernel__1f38514bcf` | `norm` | `random_low`, `random_mid`, `random_high`, `sharegpt_low`, `sharegpt_mid` | 2.92 | 7 | `void flashinfer::norm::RMSNormKernel<8u, __nv_bfloat16>(__nv_bfloat16*, __nv_bfloat16*, __nv_...` |
| `moe__moetopk__283e0afb8e` | `moe` | `random_low`, `random_high` | 2.85 | 6 | `void moeTopK<256>(float const*, bool const*, float*, int*, int, int, int, int, bool, float co...` |
| `quant_gemm__nvjet_tst_64x8_64x16_4x1_v_bz_splitk_tnt__2a7c8f8911` | `quant_gemm` | `random_low` | 2.19 | 5 | `nvjet_tst_64x8_64x16_4x1_v_bz_splitK_TNT` |

Full shape samples and skipped weak/empty rows are in `kernel_task_index.json`.
