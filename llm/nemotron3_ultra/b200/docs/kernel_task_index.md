# LLM Kernel Task Index: nemotron3_ultra / B200

- Model: `nvidia/NVIDIA-Nemotron-3-Ultra-550B-A55B-NVFP4`
- Evidence threshold: GPU kernel name share strictly `> 2%`.
- Promotion rule: only rows with an external-id-bound non-empty torch-profiler shape are task candidates.
- Weak timestamp/nearest-preceding fallback rows are retained in audit data but are not promoted.

## Workload Coverage

| Workload | Rows | Strong | Weak | Empty shape | Status |
|---|---:|---:|---:|---:|---|
| `random_low` | 12 | 8 | 4 | 0 | partial, promote strong rows only |
| `random_mid` | 10 | 3 | 7 | 0 | partial, promote strong rows only |
| `random_high` | 7 | 4 | 3 | 0 | partial, promote strong rows only |
| `sharegpt_low` | 12 | 4 | 8 | 0 | partial, promote strong rows only |
| `sharegpt_mid` | 10 | 4 | 6 | 0 | partial, promote strong rows only |
| `sharegpt_high` | 8 | 4 | 4 | 0 | partial, promote strong rows only |

## Task Candidates

| Task id | Category | Workloads | Max % GPU | Shape samples | Kernel |
|---|---|---|---:|---:|---|
| `comm__comm__0821f7c6e6` | `comm` | `sharegpt_low`, `sharegpt_mid`, `sharegpt_high` | 14.66 | 5 | `void (anonymous namespace)::all_reduce_one_shot_push_kernel<__nv_bfloat16, 4u, true>((anonymo...` |
| `gemm__cutlass3x_sm100_simt_sgemm_f32_f32_f32_f32_f32_1__b4f87b5018` | `gemm` | `random_mid`, `random_high`, `sharegpt_high` | 10.45 | 8 | `cutlass3x_sm100_simt_sgemm_f32_f32_f32_f32_f32_128x64x16_1x1x1_3_tnn_align1_bias_f32_relu` |
| `gemm__zn7cutlass13device_kernelins_4gemm6kernel13gemmu__4de9240811` | `gemm` | `random_mid`, `random_high`, `sharegpt_mid`, `sharegpt_high` | 9.70 | 6 | `_ZN7cutlass13device_kernelINS_4gemm6kernel13GemmUniversalIN4cute5tupleIJiiiiEEENS1_10collecti...` |
| `gemm__kernel2__57e9da75e7` | `gemm` | `random_low`, `sharegpt_low` | 9.14 | 2 | `void cutlass::Kernel2<cutlass_80_simt_sgemm_64x64_8x5_tn_align1>(cutlass_80_simt_sgemm_64x64_...` |
| `gemm__cutlass3x_sm100_simt_sgemm_f32_f32_f32_f32_f32_1__f50cc3eb45` | `gemm` | `random_high`, `sharegpt_mid` | 7.62 | 5 | `cutlass3x_sm100_simt_sgemm_f32_f32_f32_f32_f32_128x128x16_1x1x1_3_tnn_align1_bias_f32_relu` |
| `quant_gemm__bmm_bfloat16_e2m1e2m1_fp32_ba16_bb16_t128x8x256__356913f9ce` | `quant_gemm` | `random_low` | 4.81 | 1 | `bmm_Bfloat16_E2m1E2m1_Fp32_bA16_bB16_t128x8x256_s6_et128x8_m128x8x64_c1x1x1_16dp256b_rM_TN_tr...` |
| `gemm__kernel_cutlass_kernel_flashinfernormkernelsfused__b25a796c5c` | `gemm` | `random_low` | 4.32 | 4 | `kernel_cutlass_kernel_flashinfernormkernelsfused_add_rmsnormFusedAddRMSNormKernel_object_at__...` |
| `quant_gemm__nvjet_sm100_tst_128x256_64x6_2x1_2cta_v_bz_tnt__73699af3d3` | `quant_gemm` | `random_mid`, `random_high`, `sharegpt_high` | 4.21 | 12 | `nvjet_sm100_tst_128x256_64x6_2x1_2cta_v_bz_TNT` |
| `quant_gemm__nvjet_sm100_tst_64x8_64x16_4x1_v_bz_splitk_tnt__9737e212e3` | `quant_gemm` | `random_low`, `sharegpt_low` | 3.70 | 1 | `nvjet_sm100_tst_64x8_64x16_4x1_v_bz_splitK_TNT` |
| `quant_gemm__nvjet_sm100_tst_64x8_64x16_4x1_v_bz_tnt__563a596b8e` | `quant_gemm` | `random_low`, `sharegpt_low` | 3.13 | 4 | `nvjet_sm100_tst_64x8_64x16_4x1_v_bz_TNT` |
| `quant_gemm__bmm_e2m1_e2m1e2m1_fp32_ba16_bb16_bc16_t128x8x512__678b6e3c8c` | `quant_gemm` | `random_low` | 2.99 | 3 | `bmm_E2m1_E2m1E2m1_Fp32_bA16_bB16_bC16_t128x8x512_s5_et128x8_m128x8x64_c1x1x1_16dp256b_rM_TN_t...` |
| `comm__comm__9dd2e02622` | `comm` | `sharegpt_mid` | 2.99 | 2 | `void (anonymous namespace)::all_reduce_two_shot_kernel<__nv_bfloat16, 4u, true>(host::distrib...` |
| `quant_gemm__bmm_e2m1_e2m1e2m1_fp32_ba16_bb16_bc16_t128x8x512__f3159eb78b` | `quant_gemm` | `random_low` | 2.97 | 3 | `bmm_E2m1_E2m1E2m1_Fp32_bA16_bB16_bC16_t128x8x512u2_s5_et128x8_m128x8x64_c1x1x1_16dp256b_rM_TN...` |
| `moe__finalizekernel__03599d3c6d` | `moe` | `random_low` | 2.38 | 1 | `void moe::dev::finalize::finalizeKernel<moe::dev::finalize::KernelParams<cutlass::bfloat16_t,...` |

Full shape samples and skipped weak/empty rows are in `kernel_task_index.json`.
