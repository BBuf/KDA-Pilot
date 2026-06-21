# LLM Kernel Task Index: qwen3_coder_next / B200

- Model: `Qwen/Qwen3-Coder-Next`
- Evidence threshold: GPU kernel name share strictly `> 2%`.
- Promotion rule: only rows with an external-id-bound non-empty torch-profiler shape are task candidates.
- Weak timestamp/nearest-preceding fallback rows are retained in audit data but are not promoted.

## Workload Coverage

| Workload | Rows | Strong | Weak | Empty shape | Status |
|---|---:|---:|---:|---:|---|
| `random_low` | 7 | 4 | 3 | 0 | partial, promote strong rows only |
| `random_mid` | 10 | 4 | 6 | 0 | partial, promote strong rows only |
| `random_high` | 8 | 4 | 4 | 0 | partial, promote strong rows only |
| `sharegpt_low` | 10 | 3 | 7 | 0 | partial, promote strong rows only |
| `sharegpt_mid` | 8 | 4 | 4 | 0 | partial, promote strong rows only |
| `sharegpt_high` | 11 | 7 | 4 | 0 | partial, promote strong rows only |

## Task Candidates

| Task id | Category | Workloads | Max % GPU | Shape samples | Kernel |
|---|---|---|---:|---:|---|
| `comm__allreduce_fusion_kernel_oneshot_lamport__6c0d31268f` | `comm` | `random_low`, `random_mid`, `random_high`, `sharegpt_low`, `sharegpt_mid`, `sharegpt_high` | 34.40 | 12 | `void flashinfer::trtllm_allreduce_fusion::allreduce_fusion_kernel_oneshot_lamport<(flashinfer...` |
| `quant_gemm__nvjet_sm100_tst_64x8_64x16_2x4_h_bz_tnt__ca430502d1` | `quant_gemm` | `random_low`, `random_mid`, `random_high`, `sharegpt_low`, `sharegpt_mid`, `sharegpt_high` | 16.74 | 7 | `nvjet_sm100_tst_64x8_64x16_2x4_h_bz_TNT` |
| `quant_gemm__nvjet_sm100_tst_128x24_64x11_4x2_h_bz_tnt__e2e334a3a9` | `quant_gemm` | `random_low`, `random_mid`, `random_high` | 10.40 | 3 | `nvjet_sm100_tst_128x24_64x11_4x2_h_bz_TNT` |
| `quant_gemm__nvjet_sm100_tst_64x16_64x16_1x2_h_bz_tnt__966d42b281` | `quant_gemm` | `sharegpt_mid` | 6.98 | 1 | `nvjet_sm100_tst_64x16_64x16_1x2_h_bz_TNT` |
| `quant_gemm__nvjet_sm100_tst_128x256_64x6_2x1_2cta_v_bz_tnt__73699af3d3` | `quant_gemm` | `random_mid`, `random_high`, `sharegpt_high` | 6.21 | 7 | `nvjet_sm100_tst_128x256_64x6_2x1_2cta_v_bz_TNT` |
| `quant_gemm__nvjet_sm100_tst_64x24_64x16_4x1_v_bz_tnt__aa9d0bf29f` | `quant_gemm` | `sharegpt_low`, `sharegpt_mid`, `sharegpt_high` | 4.83 | 2 | `nvjet_sm100_tst_64x24_64x16_4x1_v_bz_TNT` |
| `comm__nccldevkernel_allreduce_sum_bf16_ring_ll__05a3ee6241` | `comm` | `sharegpt_high` | 4.37 | 5 | `ncclDevKernel_AllReduce_Sum_bf16_RING_LL(ncclDevKernelArgsStorage<4096ul>)` |
| `quant_gemm__nvjet_sm100_tst_64x24_64x16_1x2_h_bz_tnt__232ed8d6b8` | `quant_gemm` | `random_low` | 3.84 | 1 | `nvjet_sm100_tst_64x24_64x16_1x2_h_bz_TNT` |
| `quant_gemm__nvjet_sm100_tst_64x64_64x16_2x1_2cta_v_bz_tnt__754283498e` | `quant_gemm` | `sharegpt_high` | 3.82 | 2 | `nvjet_sm100_tst_64x64_64x16_2x1_2cta_v_bz_TNT` |
| `quant_gemm__nvjet_sm100_tst_8x64_64x16_4x1_v_bz_tnn__3decc0e67f` | `quant_gemm` | `sharegpt_high` | 2.82 | 2 | `nvjet_sm100_tst_8x64_64x16_4x1_v_bz_TNN` |

Full shape samples and skipped weak/empty rows are in `kernel_task_index.json`.
