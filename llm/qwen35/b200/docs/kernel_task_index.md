# LLM Kernel Task Index: qwen35 / B200

- Model: `nvidia/Qwen3.5-397B-A17B-NVFP4`
- Evidence threshold: GPU kernel name share strictly `> 2%`.
- Promotion rule: only rows with an external-id-bound non-empty torch-profiler shape are task candidates.
- Weak timestamp/nearest-preceding fallback rows are retained in audit data but are not promoted.

## Workload Coverage

| Workload | Rows | Strong | Weak | Empty shape | Status |
|---|---:|---:|---:|---:|---|
| `random_low` | 6 | 5 | 1 | 0 | partial, promote strong rows only |
| `random_mid` | 12 | 5 | 7 | 0 | partial, promote strong rows only |
| `random_high` | 9 | 4 | 5 | 0 | partial, promote strong rows only |
| `sharegpt_low` | 6 | 4 | 2 | 0 | partial, promote strong rows only |
| `sharegpt_mid` | 8 | 5 | 3 | 0 | partial, promote strong rows only |
| `sharegpt_high` | 9 | 6 | 3 | 0 | partial, promote strong rows only |

## Task Candidates

| Task id | Category | Workloads | Max % GPU | Shape samples | Kernel |
|---|---|---|---:|---:|---|
| `comm__allreduce_fusion_kernel_oneshot_lamport__3a58812ac0` | `comm` | `random_low`, `random_mid`, `random_high`, `sharegpt_low`, `sharegpt_mid`, `sharegpt_high` | 41.70 | 10 | `void flashinfer::trtllm_allreduce_fusion::allreduce_fusion_kernel_oneshot_lamport<(flashinfer...` |
| `quant_gemm__nvjet_sm100_tst_64x8_64x16_1x4_h_bz_tnt__52249c10de` | `quant_gemm` | `random_low`, `random_mid`, `random_high` | 20.78 | 5 | `nvjet_sm100_tst_64x8_64x16_1x4_h_bz_TNT` |
| `quant_gemm__nvjet_sm100_tst_64x8_64x16_2x4_h_bz_splitk_tnt__9c371f4925` | `quant_gemm` | `sharegpt_low`, `sharegpt_mid`, `sharegpt_high` | 16.75 | 4 | `nvjet_sm100_tst_64x8_64x16_2x4_h_bz_splitK_TNT` |
| `quant_gemm__nvjet_sm100_tst_64x24_64x16_4x1_v_bz_tnt__aa9d0bf29f` | `quant_gemm` | `sharegpt_low`, `sharegpt_mid`, `sharegpt_high` | 14.15 | 5 | `nvjet_sm100_tst_64x24_64x16_4x1_v_bz_TNT` |
| `quant_gemm__nvjet_sm100_tst_128x24_64x11_4x2_h_bz_tnt__e2e334a3a9` | `quant_gemm` | `random_low`, `random_mid`, `random_high` | 13.99 | 5 | `nvjet_sm100_tst_128x24_64x11_4x2_h_bz_TNT` |
| `quant_gemm__nvjet_sm100_tst_128x256_64x6_2x1_2cta_v_bz_tnt__73699af3d3` | `quant_gemm` | `random_mid`, `random_high`, `sharegpt_mid`, `sharegpt_high` | 11.81 | 7 | `nvjet_sm100_tst_128x256_64x6_2x1_2cta_v_bz_TNT` |
| `comm__allreduce_fusion_kernel_twoshot_sync__022bef8d42` | `comm` | `sharegpt_high` | 5.72 | 2 | `void flashinfer::trtllm_allreduce_fusion::allreduce_fusion_kernel_twoshot_sync<(flashinfer::t...` |
| `quant_gemm__nvjet_sm100_tst_64x32_64x16_2x1_2cta_v_bz_tnt__78a391e355` | `quant_gemm` | `random_low` | 5.55 | 2 | `nvjet_sm100_tst_64x32_64x16_2x1_2cta_v_bz_TNT` |
| `quant_gemm__nvjet_sm100_tst_64x16_64x16_1x2_h_bz_tnt__966d42b281` | `quant_gemm` | `sharegpt_mid` | 4.92 | 2 | `nvjet_sm100_tst_64x16_64x16_1x2_h_bz_TNT` |
| `quant_gemm__nvjet_sm100_tst_256x128_64x5_2x2_2cta_h_bz_tnt__d6cc26eceb` | `quant_gemm` | `random_mid`, `sharegpt_high` | 4.72 | 5 | `nvjet_sm100_tst_256x128_64x5_2x2_2cta_h_bz_TNT` |
| `quant_gemm__nvjet_sm100_tst_64x24_64x16_2x1_v_bz_splitk_tnt__f346bd8e37` | `quant_gemm` | `sharegpt_low` | 4.32 | 1 | `nvjet_sm100_tst_64x24_64x16_2x1_v_bz_splitK_TNT` |
| `comm__comm__0821f7c6e6` | `comm` | `random_low` | 3.38 | 2 | `void (anonymous namespace)::all_reduce_one_shot_push_kernel<__nv_bfloat16, 4u, true>((anonymo...` |

Full shape samples and skipped weak/empty rows are in `kernel_task_index.json`.
