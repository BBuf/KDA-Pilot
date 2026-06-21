# LLM Kernel Task Index: mimo_v2_flash / B200

- Model: `XiaomiMiMo/MiMo-V2-Flash`
- Evidence threshold: GPU kernel name share strictly `> 2%`.
- Promotion rule: only rows with an external-id-bound non-empty torch-profiler shape are task candidates.
- Weak timestamp/nearest-preceding fallback rows are retained in audit data but are not promoted.

## Workload Coverage

| Workload | Rows | Strong | Weak | Empty shape | Status |
|---|---:|---:|---:|---:|---|
| `random_low` | 2 | 2 | 0 | 0 | strong |
| `random_mid` | 1 | 1 | 0 | 0 | strong |
| `random_high` | 1 | 1 | 0 | 0 | strong |
| `sharegpt_low` | 1 | 1 | 0 | 0 | strong |
| `sharegpt_mid` | 1 | 1 | 0 | 0 | strong |
| `sharegpt_high` | 1 | 1 | 0 | 0 | strong |

## Task Candidates

| Task id | Category | Workloads | Max % GPU | Shape samples | Kernel |
|---|---|---|---:|---:|---|
| `memory_bound__cross_device_reduce_1stage__c8cdabb144` | `memory_bound` | `random_low`, `random_mid`, `random_high`, `sharegpt_low`, `sharegpt_mid`, `sharegpt_high` | 93.86 | 12 | `void sglang::cross_device_reduce_1stage<__nv_bfloat16, 8>(sglang::RankData*, sglang::RankSign...` |
| `memory_bound__cross_device_reduce_2stage__3aef8a3471` | `memory_bound` | `random_low` | 34.97 | 5 | `void sglang::cross_device_reduce_2stage<__nv_bfloat16, 8>(sglang::RankData*, sglang::RankSign...` |

Full shape samples and skipped weak/empty rows are in `kernel_task_index.json`.
