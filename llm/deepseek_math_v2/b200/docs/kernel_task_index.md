# LLM Kernel Task Index: deepseek_math_v2 / B200

- Model: `deepseek-ai/DeepSeek-Math-V2`
- Evidence threshold: GPU kernel name share strictly `> 2%`.
- Promotion rule: only rows with an external-id-bound non-empty torch-profiler shape are task candidates.
- Weak timestamp/nearest-preceding fallback rows are retained in audit data but are not promoted.

## Workload Coverage

| Workload | Rows | Strong | Weak | Empty shape | Status |
|---|---:|---:|---:|---:|---|
| `random_low` | 7 | 1 | 3 | 3 | partial, promote strong rows only |
| `random_mid` | 1 | 1 | 0 | 0 | strong |
| `random_high` | 10 | 1 | 2 | 7 | partial, promote strong rows only |
| `sharegpt_low` | 6 | 0 | 4 | 2 | weak/empty only, do not promote |
| `sharegpt_mid` | 12 | 5 | 4 | 3 | partial, promote strong rows only |
| `sharegpt_high` | 10 | 1 | 2 | 7 | partial, promote strong rows only |

## Task Candidates

| Task id | Category | Workloads | Max % GPU | Shape samples | Kernel |
|---|---|---|---:|---:|---|
| `quant_gemm__nvjet_sm100_tst_64x16_64x16_2x4_2cta_h_bz_splitk__6dd18c84c0` | `quant_gemm` | `random_low` | 11.70 | 1 | `nvjet_sm100_tst_64x16_64x16_2x4_2cta_h_bz_splitK_TNT` |
| `quant_gemm__bmm_e4m3_e4m3e4m3_fp32_t128x64x128u2_s6_et64x64__046d851f0c` | `quant_gemm` | `sharegpt_mid` | 7.19 | 1 | `bmm_E4m3_E4m3E4m3_Fp32_t128x64x128u2_s6_et64x64_m64x64x32_c1x1x1_rM_TN_transOut_noShfl_dsFp8_...` |
| `quant_gemm__sm100_fp8_fp4_gemm_1d1d_impl__45bdd89e95` | `quant_gemm` | `random_mid`, `sharegpt_mid` | 5.81 | 2 | `void deep_gemm::sm100_fp8_fp4_gemm_1d1d_impl<(cute::UMMA::Major)0, (cute::UMMA::Major)0, 128u...` |
| `attention__fmhasm100fkernel_qkve4m3obfloat16hqk576hv512page__c1886e8cff` | `attention` | `random_high`, `sharegpt_high` | 5.00 | 12 | `fmhaSm100fKernel_QkvE4m3OBfloat16HQk576HV512PagedKvDenseStaticTokenSparseP1VarSeqQ16Kv128Pers...` |
| `moe__activationdeepseekkernel__b7453c53aa` | `moe` | `sharegpt_mid` | 4.80 | 2 | `void moe::dev::activation::activationDeepSeekKernel<moe::dev::activation::KernelParams<cutlas...` |
| `quant_gemm__bmm_bfloat16_e4m3e4m3_fp32_t128x64x128u2_s6_et64__4becbe9f88` | `quant_gemm` | `sharegpt_mid` | 3.90 | 2 | `bmm_Bfloat16_E4m3E4m3_Fp32_t128x64x128u2_s6_et64x64_m64x64x32_c1x1x1_rM_TN_transOut_noShfl_ds...` |
| `other__other__00ff8f7a29` | `other` | `sharegpt_mid` | 3.80 | 1 | `void (anonymous namespace)::fast_hadamard_transform_kernel<(anonymous namespace)::FastHadamar...` |

Full shape samples and skipped weak/empty rows are in `kernel_task_index.json`.
