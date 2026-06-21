# LLM Kernel Task Index: glm_52 / B200

- Model: `zai-org/GLM-5.2-FP8`
- Evidence threshold: GPU kernel name share strictly `> 2%`.
- Promotion rule: only rows with an external-id-bound non-empty torch-profiler shape are task candidates.
- Weak timestamp/nearest-preceding fallback rows are retained in audit data but are not promoted.

## Workload Coverage

| Workload | Rows | Strong | Weak | Empty shape | Status |
|---|---:|---:|---:|---:|---|
| `random_low` | 9 | 4 | 5 | 0 | partial, promote strong rows only |
| `random_mid` | 11 | 1 | 10 | 0 | partial, promote strong rows only |
| `random_high` | 10 | 1 | 9 | 0 | partial, promote strong rows only |
| `sharegpt_low` | 9 | 1 | 8 | 0 | partial, promote strong rows only |
| `sharegpt_mid` | 4 | 0 | 4 | 0 | weak/empty only, do not promote |
| `sharegpt_high` | 7 | 0 | 7 | 0 | weak/empty only, do not promote |

## Task Candidates

| Task id | Category | Workloads | Max % GPU | Shape samples | Kernel |
|---|---|---|---:|---:|---|
| `moe_comm__notify_dispatch__4a6d3ee17e` | `moe_comm` | `random_low` | 32.86 | 1 | `void deep_ep::intranode::notify_dispatch<8>(int const*, int*, int const*, int*, int, int, int...` |
| `quant_gemm__sm100_fp8_fp4_gemm_1d1d_impl__1b5539080f` | `quant_gemm` | `random_low`, `random_mid`, `sharegpt_low` | 11.68 | 12 | `void deep_gemm::sm100_fp8_fp4_gemm_1d1d_impl<(cute::UMMA::Major)0, (cute::UMMA::Major)0, 128u...` |
| `moe_comm__cached_notify_combine__3b8f1bd9fe` | `moe_comm` | `random_low` | 4.86 | 1 | `void deep_ep::intranode::cached_notify_combine<8>(void**, int*, int, int, int, int**, int)` |
| `comm__comm__a12cdaa5b4` | `comm` | `random_low` | 2.39 | 3 | `void (anonymous namespace)::all_reduce_one_shot_push_kernel<__nv_bfloat16, 8u, true>((anonymo...` |
| `quant_gemm__sm100_fp8_fp4_gemm_1d1d_impl__45bdd89e95` | `quant_gemm` | `random_high` | 2.14 | 8 | `void deep_gemm::sm100_fp8_fp4_gemm_1d1d_impl<(cute::UMMA::Major)0, (cute::UMMA::Major)0, 128u...` |

Full shape samples and skipped weak/empty rows are in `kernel_task_index.json`.
