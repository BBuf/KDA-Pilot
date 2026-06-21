# LLM Kernel Task Index: glm_47_flash / B200

- Model: `zai-org/GLM-4.7-Flash`
- Evidence threshold: GPU kernel name share strictly `> 2%`.
- Promotion rule: only rows with an external-id-bound non-empty torch-profiler shape are task candidates.
- Weak timestamp/nearest-preceding fallback rows are retained in audit data but are not promoted.

## Workload Coverage

| Workload | Rows | Strong | Weak | Empty shape | Status |
|---|---:|---:|---:|---:|---|
| `random_low` | 6 | 0 | 5 | 1 | weak/empty only, do not promote |
| `random_mid` | 2 | 1 | 1 | 0 | partial, promote strong rows only |
| `random_high` | 2 | 1 | 0 | 1 | partial, promote strong rows only |
| `sharegpt_low` | 7 | 1 | 5 | 1 | partial, promote strong rows only |
| `sharegpt_mid` | 2 | 1 | 1 | 0 | partial, promote strong rows only |
| `sharegpt_high` | 2 | 1 | 1 | 0 | partial, promote strong rows only |

## Task Candidates

| Task id | Category | Workloads | Max % GPU | Shape samples | Kernel |
|---|---|---|---:|---:|---|
| `other__fwd_kernel__d4406e9fc7` | `other` | `random_high`, `sharegpt_low`, `sharegpt_high` | 35.25 | 12 | `_fwd_kernel` |
| `moe__fused_moe_kernel__c581b7d47d` | `moe` | `random_mid`, `sharegpt_mid` | 30.39 | 2 | `fused_moe_kernel` |

Full shape samples and skipped weak/empty rows are in `kernel_task_index.json`.
