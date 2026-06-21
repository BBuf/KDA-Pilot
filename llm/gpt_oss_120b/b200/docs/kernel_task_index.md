# LLM Kernel Task Index: gpt_oss_120b / B200

- Model: `openai/gpt-oss-120b`
- Evidence threshold: GPU kernel name share strictly `> 2%`.
- Promotion rule: only rows with an external-id-bound non-empty torch-profiler shape are task candidates.
- Weak timestamp/nearest-preceding fallback rows are retained in audit data but are not promoted.

## Workload Coverage

| Workload | Rows | Strong | Weak | Empty shape | Status |
|---|---:|---:|---:|---:|---|
| `random_low` | 14 | 13 | 0 | 1 | partial, promote strong rows only |
| `random_mid` | 12 | 4 | 5 | 3 | partial, promote strong rows only |
| `random_high` | 10 | 3 | 5 | 2 | partial, promote strong rows only |
| `sharegpt_low` | 11 | 0 | 6 | 5 | weak/empty only, do not promote |
| `sharegpt_mid` | 11 | 1 | 2 | 8 | partial, promote strong rows only |
| `sharegpt_high` | 12 | 6 | 5 | 1 | partial, promote strong rows only |

## Task Candidates

| Task id | Category | Workloads | Max % GPU | Shape samples | Kernel |
|---|---|---|---:|---:|---|
| `comm__allreduce_fusion_kernel_oneshot_lamport__b9d8384154` | `comm` | `random_low`, `random_mid`, `sharegpt_high` | 23.07 | 4 | `void flashinfer::trtllm_allreduce_fusion::allreduce_fusion_kernel_oneshot_lamport<(flashinfer...` |
| `quant_gemm__nvjet_sm100_tst_32x64_64x16_4x1_v_bz_splitk_bias__3509350c64` | `quant_gemm` | `random_low` | 15.41 | 1 | `nvjet_sm100_tst_32x64_64x16_4x1_v_bz_splitK_bias_TNN` |
| `quant_gemm__nvjet_sm100_tst_32x64_64x16_4x2_2cta_h_bz_splitk__c3a28d9056` | `quant_gemm` | `random_high`, `sharegpt_high` | 10.49 | 2 | `nvjet_sm100_tst_32x64_64x16_4x2_2cta_h_bz_splitK_bias_TNN` |
| `quant_gemm__nvjet_sm100_tst_64x16_64x16_2x4_2cta_h_bz_splitk__9848c26550` | `quant_gemm` | `random_low`, `random_mid` | 9.46 | 2 | `nvjet_sm100_tst_64x16_64x16_2x4_2cta_h_bz_splitK_bias_TNT` |
| `comm__comm__c330990d60` | `comm` | `sharegpt_high` | 8.07 | 2 | `void (anonymous namespace)::all_reduce_two_shot_kernel<__nv_bfloat16, 8u, true>(host::distrib...` |
| `quant_gemm__bmm_mxe4m3_mxe2m1mxe4m3_fp32_ab32_bb32_cb32_t128__b812b12ca9` | `quant_gemm` | `random_mid` | 5.22 | 1 | `bmm_MxE4m3_MxE2m1MxE4m3_Fp32_Ab32_Bb32_Cb32_t128x128x256u2_s4_et128x32_m256x128x32_c2x1x1_rM_...` |
| `quant_gemm__bmm_mxe4m3_mxe2m1mxe4m3_fp32_ab32_bb32_cb32_t128__8fa85901dd` | `quant_gemm` | `sharegpt_mid` | 3.85 | 1 | `bmm_MxE4m3_MxE2m1MxE4m3_Fp32_Ab32_Bb32_Cb32_t128x128x256_s4x4x4x4x1x4_et128x32_m256x128x32_c2...` |
| `quant_gemm__nvjet_sm100_tst_64x32_64x16_2x4_2cta_h_bz_splitk__9158475f4f` | `quant_gemm` | `sharegpt_high` | 3.80 | 1 | `nvjet_sm100_tst_64x32_64x16_2x4_2cta_h_bz_splitK_bias_TNT` |
| `quant_gemm__bmm_mxe4m3_mxe2m1mxe4m3_fp32_ab32_bb32_cb32_t128__7622b539bc` | `quant_gemm` | `random_high` | 3.18 | 1 | `bmm_MxE4m3_MxE2m1MxE4m3_Fp32_Ab32_Bb32_Cb32_t128x16x256u2_s6_et128x16_m256x16x32_c2x1x1_rM_TN...` |
| `quant_gemm__quantize_with_block_size__040f8fdcd0` | `quant_gemm` | `random_low`, `random_mid` | 3.04 | 2 | `void tensorrt_llm::kernels::quantize_with_block_size<(tensorrt_llm::BlockScaleQuantizationTyp...` |
| `moe__finalizekernel__6a7a068b8f` | `moe` | `random_low` | 2.94 | 1 | `void moe::dev::finalize::finalizeKernel<moe::dev::finalize::KernelParams<cutlass::bfloat16_t,...` |
| `quant_gemm__bmm_mxe4m3_mxe2m1mxe4m3_fp32_ab32_bb32_cb32_t128__a3c2ece668` | `quant_gemm` | `random_low` | 2.94 | 1 | `bmm_MxE4m3_MxE2m1MxE4m3_Fp32_Ab32_Bb32_Cb32_t128x16x256u2_s6_et128x16_m256x16x32_c2x1x1_rM_TN...` |
| `attention__fmhasm100fkernel_qkvbfloat16obfloat16h64pagedkvc__2d54ccf3a0` | `attention` | `random_low` | 2.91 | 3 | `fmhaSm100fKernel_QkvBfloat16OBfloat16H64PagedKvCausalP64MultiCtasKvVarSeqQ8Kv128StaticSwapsAb...` |
| `comm__comm__a12cdaa5b4` | `comm` | `random_low` | 2.80 | 4 | `void (anonymous namespace)::all_reduce_one_shot_push_kernel<__nv_bfloat16, 8u, true>((anonymo...` |
| `quant_gemm__nvjet_sm100_tst_24x64_64x16_4x1_v_bz_tnn__b371524b5a` | `quant_gemm` | `random_low` | 2.66 | 2 | `nvjet_sm100_tst_24x64_64x16_4x1_v_bz_TNN` |
| `moe__routingindicesblockkernel__4a05d9bb7f` | `moe` | `random_low` | 2.58 | 1 | `void moe::dev::routing::routingCustom::routingIndicesBlockKernel<moe::dev::routing::routingCu...` |
| `attention__fmhasm100fkernel_qkvbfloat16obfloat16h64pagedkvc__06f947c5f9` | `attention` | `sharegpt_high` | 2.55 | 3 | `fmhaSm100fKernel_QkvBfloat16OBfloat16H64PagedKvCausalP64VarSeqQ128Kv128PersistentContext` |
| `gemm__kernel_cutlass_kernel_flashinfernormkernelsrmsno__008eb9166b` | `gemm` | `random_low` | 2.46 | 4 | `kernel_cutlass_kernel_flashinfernormkernelsrmsnormRMSNormKernel_object_at__tensorptrbf16gmema...` |
| `attention__fmhasm100fkernel_qkvbfloat16obfloat16h64pagedkvs__aacc0ffbdb` | `attention` | `random_low` | 2.39 | 2 | `fmhaSm100fKernel_QkvBfloat16OBfloat16H64PagedKvSlidingOrChunkedCausalP64VarSeqQ8Kv128Persiste...` |
| `quant_gemm__bmm_mxe4m3_mxe2m1mxe4m3_fp32_ab32_bb32_cb32_t128__a4ce2c467f` | `quant_gemm` | `random_low` | 2.25 | 1 | `bmm_MxE4m3_MxE2m1MxE4m3_Fp32_Ab32_Bb32_Cb32_t128x16x256_s5_et128x16_m256x16x32_c2x1x1_rM_TN_t...` |
| `quant_gemm__bmm_bfloat16_mxe2m1mxe4m3_fp32_ab32_bb32_t128x16__9bcd4dcdd8` | `quant_gemm` | `random_high` | 2.21 | 1 | `bmm_Bfloat16_MxE2m1MxE4m3_Fp32_Ab32_Bb32_t128x16x256_s4_et128x16_m128x16x32_c1x1x1_rM_TN_tran...` |
| `moe__finalizekernelvecload__00edba12eb` | `moe` | `sharegpt_high` | 2.18 | 1 | `void moe::dev::finalize::finalizeKernelVecLoad<moe::dev::finalize::KernelParams<cutlass::bflo...` |

Full shape samples and skipped weak/empty rows are in `kernel_task_index.json`.
