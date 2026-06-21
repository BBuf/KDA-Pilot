# Kernel Shape Inventory — sharegpt_high

- Model: `internLM/Intern-S2-Preview`
- Dataset: `sharegpt`
- Concurrency: `high`
- Threshold: GPU kernel name share `> 2.0%`
- Total GPU kernel time: `4937.1 ms`
- Trace files: `8`

| % GPU | Calls | Category | Shape | SGLang relevant | Kernel | Shape provenance |
|---:|---:|---|---|---|---|---|
| 33.66 | 4424 | comm | ok | True | `void flashinfer::trtllm_allreduce_fusion::allreduce_fusion_kernel_oneshot_lamport<(flashinfer::trtllm_allreduce_fusion::AllReduceFusionPattern)1, __nv_bfloat16, 8, false, false>(flashinfer::trtllm_allreduce_fusion::AllReduceFusionParams<__nv_bfloat16>)` | external_id=117886: `sglang::flashinfer_allreduce_residual_rmsnorm` {"Concrete Inputs": ["", "", "", "9.9999999999999995e-07", "2048", "", "False", "False", "True"], "Input Dims": [[17, 2048], [17, 2048], [2048], [], [], [], [], [], []], "Input ... |
| 10.91 | 3200 | quant_gemm | ok | True | `nvjet_sm100_tst_64x8_64x16_2x4_h_bz_TNT` | external_id=117903: `aten::mm` {"Concrete Inputs": ["", ""], "Input Dims": [[17, 2048], [2048, 1536]], "Input Strides": [[2048, 1], [1, 2048]], "Input type": ["c10::BFloat16", "c10::BFloat16"]} |
| 5.99 | 640 | quant_gemm | ok | True | `nvjet_sm100_tst_64x8_64x16_2x4_h_bz_splitK_TNT` | external_id=117676: `aten::mm` {"Concrete Inputs": ["", ""], "Input Dims": [[17, 2048], [2048, 128]], "Input Strides": [[2048, 1], [1, 2048]], "Input type": ["c10::BFloat16", "c10::BFloat16"]} |
| 4.80 | 640 | quant_gemm | ok | True | `nvjet_sm100_tst_64x16_64x16_2x4_2cta_h_bz_TNT` | external_id=156174: `aten::mm` {"Concrete Inputs": ["", ""], "Input Dims": [[632, 2048], [2048, 128]], "Input Strides": [[2048, 1], [1, 2048]], "Input type": ["c10::BFloat16", "c10::BFloat16"]} |

The CSV/JSON siblings contain full sample metadata and trace paths.
