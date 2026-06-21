# LLM Kernel Task Index: deepseek_v4 / B200

- Model: `deepseek-ai/DeepSeek-V4-Flash`
- Evidence threshold: GPU kernel name share strictly `> 2%`.
- Promotion rule: only rows with an external-id-bound non-empty torch-profiler shape are task candidates.
- Weak timestamp/nearest-preceding fallback rows are retained in audit data but are not promoted.

## Workload Coverage

| Workload | Rows | Strong | Weak | Empty shape | Status |
|---|---:|---:|---:|---:|---|
| `random_low` | 2 | 1 | 1 | 0 | partial, promote strong rows only |
| `random_mid` | 4 | 1 | 3 | 0 | partial, promote strong rows only |
| `random_high` | 3 | 2 | 1 | 0 | partial, promote strong rows only |
| `sharegpt_low` | 3 | 1 | 2 | 0 | partial, promote strong rows only |
| `sharegpt_mid` | 4 | 3 | 1 | 0 | partial, promote strong rows only |
| `sharegpt_high` | 4 | 3 | 1 | 0 | partial, promote strong rows only |

## Task Candidates

| Task id | Category | Workloads | Max % GPU | Shape samples | Kernel |
|---|---|---|---:|---:|---|
| `comm__comm__9dd2e02622` | `comm` | `random_high`, `sharegpt_mid`, `sharegpt_high` | 47.23 | 9 | `void (anonymous namespace)::all_reduce_two_shot_kernel<__nv_bfloat16, 4u, true>(host::distrib...` |
| `comm__comm__0821f7c6e6` | `comm` | `random_low`, `random_mid`, `random_high`, `sharegpt_low`, `sharegpt_mid`, `sharegpt_high` | 36.16 | 5 | `void (anonymous namespace)::all_reduce_one_shot_push_kernel<__nv_bfloat16, 4u, true>((anonymo...` |
| `quant_gemm__flash_fwd_splitkv_mla_fp8_sparse_kernel__852500f4e2` | `quant_gemm` | `sharegpt_mid`, `sharegpt_high` | 4.11 | 3 | `void sm100::decode::head64::flash_fwd_splitkv_mla_fp8_sparse_kernel<sm100::decode::head64::Ke...` |

Full shape samples and skipped weak/empty rows are in `kernel_task_index.json`.
