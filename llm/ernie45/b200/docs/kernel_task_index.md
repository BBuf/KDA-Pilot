# LLM Kernel Task Index: ernie45 / B200

- Model: `baidu/ERNIE-4.5-21B-A3B-PT`
- Evidence threshold: GPU kernel name share strictly `> 2%`.
- Promotion rule: only rows with an external-id-bound non-empty torch-profiler shape are task candidates.
- Weak timestamp/nearest-preceding fallback rows are retained in audit data but are not promoted.

## Workload Coverage

| Workload | Rows | Strong | Weak | Empty shape | Status |
|---|---:|---:|---:|---:|---|
| `random_low` | 9 | 0 | 7 | 2 | weak/empty only, do not promote |
| `random_mid` | 6 | 1 | 1 | 4 | partial, promote strong rows only |
| `random_high` | 4 | 1 | 2 | 1 | partial, promote strong rows only |
| `sharegpt_low` | 9 | 1 | 7 | 1 | partial, promote strong rows only |
| `sharegpt_mid` | 4 | 1 | 1 | 2 | partial, promote strong rows only |
| `sharegpt_high` | 4 | 1 | 2 | 1 | partial, promote strong rows only |

## Task Candidates

| Task id | Category | Workloads | Max % GPU | Shape samples | Kernel |
|---|---|---|---:|---:|---|
| `attention__fmhasm100fkernel_qkvbfloat16obfloat16h128pagedkv__714e7067df` | `attention` | `random_mid`, `random_high`, `sharegpt_mid`, `sharegpt_high` | 4.48 | 12 | `fmhaSm100fKernel_QkvBfloat16OBfloat16H128PagedKvCausalP64VarSeqQ128Kv128PersistentContext` |
| `quant_gemm__nvjet_sm100_tst_64x8_64x16_2x1_v_bz_tnt__9e496c72b7` | `quant_gemm` | `sharegpt_low` | 2.30 | 1 | `nvjet_sm100_tst_64x8_64x16_2x1_v_bz_TNT` |

Full shape samples and skipped weak/empty rows are in `kernel_task_index.json`.
