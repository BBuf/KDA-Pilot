# LLM Kernel Task Index: nemotron3_nano / B200

- Model: `nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B-FP8`
- Evidence threshold: GPU kernel name share strictly `> 2%`.
- Promotion rule: only rows with an external-id-bound non-empty torch-profiler shape are task candidates.
- Weak timestamp/nearest-preceding fallback rows are retained in audit data but are not promoted.

## Workload Coverage

| Workload | Rows | Strong | Weak | Empty shape | Status |
|---|---:|---:|---:|---:|---|
| `random_low` | 13 | 0 | 13 | 0 | weak/empty only, do not promote |
| `random_mid` | 11 | 7 | 4 | 0 | partial, promote strong rows only |
| `random_high` | 8 | 6 | 2 | 0 | partial, promote strong rows only |
| `sharegpt_low` | 14 | 2 | 12 | 0 | partial, promote strong rows only |
| `sharegpt_mid` | 10 | 6 | 4 | 0 | partial, promote strong rows only |
| `sharegpt_high` | 8 | 6 | 2 | 0 | partial, promote strong rows only |

## Task Candidates

| Task id | Category | Workloads | Max % GPU | Shape samples | Kernel |
|---|---|---|---:|---:|---|
| `other__chunk_scan_fwd_kernel__e84657f454` | `other` | `random_mid`, `random_high`, `sharegpt_mid`, `sharegpt_high` | 20.57 | 12 | `_chunk_scan_fwd_kernel` |
| `other__chunk_state_fwd_kernel__0be5776788` | `other` | `random_mid`, `random_high`, `sharegpt_mid`, `sharegpt_high` | 14.32 | 12 | `_chunk_state_fwd_kernel` |
| `other__state_passing_fwd_kernel__535fed3fd8` | `other` | `random_mid`, `random_high`, `sharegpt_mid`, `sharegpt_high` | 10.18 | 12 | `_state_passing_fwd_kernel` |
| `gemm__zn7cutlass13device_kernelins_4gemm6kernel13gemmu__4de9240811` | `gemm` | `random_mid`, `random_high`, `sharegpt_mid`, `sharegpt_high` | 6.61 | 3 | `_ZN7cutlass13device_kernelINS_4gemm6kernel13GemmUniversalIN4cute5tupleIJiiiiEEENS1_10collecti...` |
| `quant_gemm__nvjet_sm100_tst_128x8_64x12_2x1_v_bz_tnt__da4bd0e0be` | `quant_gemm` | `sharegpt_low` | 3.44 | 1 | `nvjet_sm100_tst_128x8_64x12_2x1_v_bz_TNT` |
| `other__chunk_state_varlen_kernel__82b12abbf7` | `other` | `random_mid`, `random_high`, `sharegpt_mid`, `sharegpt_high` | 3.11 | 12 | `_chunk_state_varlen_kernel` |
| `quant_gemm__nvjet_sm100_tst_128x256_64x6_2x1_2cta_v_bz_tnt__73699af3d3` | `quant_gemm` | `random_mid` | 2.25 | 2 | `nvjet_sm100_tst_128x256_64x6_2x1_2cta_v_bz_TNT` |
| `quant_gemm__batchprefillwithpagedkvcachekernel__e9a92f2480` | `quant_gemm` | `sharegpt_mid`, `sharegpt_high` | 2.21 | 12 | `void flashinfer::BatchPrefillWithPagedKVCacheKernel<flashinfer::KernelTraits<(flashinfer::Mas...` |
| `other__bmm_chunk_fwd_kernel__80637095a1` | `other` | `random_mid`, `random_high` | 2.20 | 12 | `_bmm_chunk_fwd_kernel` |
| `gemm__zn7cutlass13device_kernelins_4gemm6kernel13gemmu__64c6383c7f` | `gemm` | `sharegpt_low` | 2.11 | 1 | `_ZN7cutlass13device_kernelINS_4gemm6kernel13GemmUniversalIN4cute5tupleIJiiiiEEENS1_10collecti...` |

Full shape samples and skipped weak/empty rows are in `kernel_task_index.json`.
