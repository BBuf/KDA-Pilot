# LLM Kernel Task Index: qwen3_next / B200

- Model: `Qwen/Qwen3-Next-80B-A3B-Instruct`
- Evidence threshold: GPU kernel name share strictly `> 2%`.
- Promotion rule: only rows with an external-id-bound non-empty torch-profiler shape are task candidates.
- Weak timestamp/nearest-preceding fallback rows are retained in audit data but are not promoted.

## Workload Coverage

| Workload | Rows | Strong | Weak | Empty shape | Status |
|---|---:|---:|---:|---:|---|
| `random_low` | 6 | 3 | 3 | 0 | partial, promote strong rows only |
| `random_mid` | 7 | 4 | 3 | 0 | partial, promote strong rows only |
| `random_high` | 6 | 3 | 3 | 0 | partial, promote strong rows only |
| `sharegpt_low` | 4 | 3 | 1 | 0 | partial, promote strong rows only |
| `sharegpt_mid` | 4 | 4 | 0 | 0 | strong |
| `sharegpt_high` | 5 | 5 | 0 | 0 | strong |

## Task Candidates

| Task id | Category | Workloads | Max % GPU | Shape samples | Kernel |
|---|---|---|---:|---:|---|
| `comm__allreduce_fusion_kernel_oneshot_lamport__b9d8384154` | `comm` | `random_low`, `random_mid`, `random_high`, `sharegpt_low`, `sharegpt_mid`, `sharegpt_high` | 44.30 | 12 | `void flashinfer::trtllm_allreduce_fusion::allreduce_fusion_kernel_oneshot_lamport<(flashinfer...` |
| `quant_gemm__nvjet_sm100_tst_64x8_64x16_2x4_h_bz_splitk_tnt__9c371f4925` | `quant_gemm` | `random_low`, `random_mid`, `random_high`, `sharegpt_low`, `sharegpt_mid`, `sharegpt_high` | 25.37 | 8 | `nvjet_sm100_tst_64x8_64x16_2x4_h_bz_splitK_TNT` |
| `quant_gemm__nvjet_sm100_tst_16x64_64x16_4x1_v_bz_tnn__e3baf7ff46` | `quant_gemm` | `random_low`, `random_mid`, `random_high` | 20.15 | 3 | `nvjet_sm100_tst_16x64_64x16_4x1_v_bz_TNN` |
| `quant_gemm__nvjet_sm100_tst_64x8_64x16_2x4_h_bz_tnt__ca430502d1` | `quant_gemm` | `sharegpt_low`, `sharegpt_mid`, `sharegpt_high` | 18.35 | 6 | `nvjet_sm100_tst_64x8_64x16_2x4_h_bz_TNT` |
| `comm__allreduce_fusion_kernel_twoshot_sync__c36567c3ee` | `comm` | `random_mid`, `sharegpt_high` | 16.11 | 4 | `void flashinfer::trtllm_allreduce_fusion::allreduce_fusion_kernel_twoshot_sync<(flashinfer::t...` |
| `quant_gemm__nvjet_sm100_tst_64x8_64x16_1x2_h_bz_tnt__2857e52688` | `quant_gemm` | `sharegpt_mid` | 7.24 | 2 | `nvjet_sm100_tst_64x8_64x16_1x2_h_bz_TNT` |
| `comm__comm__c330990d60` | `comm` | `sharegpt_high` | 2.29 | 2 | `void (anonymous namespace)::all_reduce_two_shot_kernel<__nv_bfloat16, 8u, true>(host::distrib...` |

Full shape samples and skipped weak/empty rows are in `kernel_task_index.json`.
