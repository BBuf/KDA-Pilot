# LLM Kernel Task Index: lfm25 / B200

- Model: `LiquidAI/LFM2.5-8B-A1B`
- Evidence threshold: GPU kernel name share strictly `> 2%`.
- Promotion rule: only rows with an external-id-bound non-empty torch-profiler shape are task candidates.
- Weak timestamp/nearest-preceding fallback rows are retained in audit data but are not promoted.

## Workload Coverage

| Workload | Rows | Strong | Weak | Empty shape | Status |
|---|---:|---:|---:|---:|---|
| `random_low` | 9 | 4 | 5 | 0 | partial, promote strong rows only |
| `random_mid` | 4 | 3 | 1 | 0 | partial, promote strong rows only |
| `random_high` | 3 | 3 | 0 | 0 | strong |
| `sharegpt_low` | 9 | 3 | 6 | 0 | partial, promote strong rows only |
| `sharegpt_mid` | 5 | 3 | 2 | 0 | partial, promote strong rows only |
| `sharegpt_high` | 5 | 4 | 1 | 0 | partial, promote strong rows only |

## Task Candidates

| Task id | Category | Workloads | Max % GPU | Shape samples | Kernel |
|---|---|---|---:|---:|---|
| `moe__fused_moe_kernel__c581b7d47d` | `moe` | `random_low`, `random_mid`, `random_high`, `sharegpt_low`, `sharegpt_mid`, `sharegpt_high` | 50.52 | 5 | `fused_moe_kernel` |
| `quant_gemm__nvjet_sm100_tst_128x256_64x6_2x1_2cta_v_bz_tnt__73699af3d3` | `quant_gemm` | `random_mid`, `random_high`, `sharegpt_mid`, `sharegpt_high` | 11.24 | 11 | `nvjet_sm100_tst_128x256_64x6_2x1_2cta_v_bz_TNT` |
| `moe__moe_align_block_size_small_batch_expert_kernel__2c9f928b16` | `moe` | `random_low` | 5.09 | 1 | `void moe_align_block_size_small_batch_expert_kernel<int, 256>(int const*, int*, int*, int*, i...` |
| `other__other__56d7fd43dd` | `other` | `random_low`, `random_mid`, `random_high`, `sharegpt_low`, `sharegpt_mid`, `sharegpt_high` | 4.35 | 9 | `void (anonymous namespace)::act_and_mul_kernel<__nv_bfloat16, ((anonymous namespace)::Activat...` |
| `quant_gemm__nvjet_sm100_tst_128x8_64x12_2x1_v_bz_tnt__da4bd0e0be` | `quant_gemm` | `random_low`, `sharegpt_low` | 3.51 | 1 | `nvjet_sm100_tst_128x8_64x12_2x1_v_bz_TNT` |
| `quant_gemm__nvjet_sm100_tst_256x128_64x5_2x1_2cta_v_bz_tnt__a8b8dd3c28` | `quant_gemm` | `sharegpt_high` | 2.15 | 3 | `nvjet_sm100_tst_256x128_64x5_2x1_2cta_v_bz_TNT` |

Full shape samples and skipped weak/empty rows are in `kernel_task_index.json`.
