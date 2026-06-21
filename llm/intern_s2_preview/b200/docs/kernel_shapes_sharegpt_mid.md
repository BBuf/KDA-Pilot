# Kernel Shape Inventory — sharegpt_mid

- Model: `internLM/Intern-S2-Preview`
- Dataset: `sharegpt`
- Concurrency: `mid`
- Threshold: GPU kernel name share `> 2.0%`
- Total GPU kernel time: `3093.4 ms`
- Trace files: `8`

| % GPU | Calls | Category | Shape | SGLang relevant | Kernel | Shape provenance |
|---:|---:|---|---|---|---|---|
| 34.90 | 5056 | comm | ok | True | `void flashinfer::trtllm_allreduce_fusion::allreduce_fusion_kernel_oneshot_lamport<(flashinfer::trtllm_allreduce_fusion::AllReduceFusionPattern)1, __nv_bfloat16, 8, false, false>(flashinfer::trtllm_allreduce_fusion::AllReduceFusionParams<__nv_bfloat16>)` | external_id=88554: `aten::empty` {"Concrete Inputs": ["[512]", "3", "", "", "", ""], "Input Dims": [[], [], [], [], [], []], "Input Strides": [[], [], [], [], [], []], "Input type": ["ScalarList", "Scalar", "",... |
| 9.98 | 320 | quant_gemm | ok | True | `nvjet_sm100_tst_64x8_64x16_2x4_h_bz_splitK_TNT` | external_id=88572: `aten::empty_like` {"Concrete Inputs": ["", "", "", "", "False", ""], "Input Dims": [[46, 2048], [], [], [], [], []], "Input Strides": [[2048, 1], [], [], [], [], []], "Input type": ["c10::BFloat1... |
| 9.04 | 640 | quant_gemm | ok | True | `nvjet_sm100_tst_64x8_64x16_1x2_h_bz_TNT` | external_id=89659: `aten::transpose` {"Concrete Inputs": ["", "0", "1"], "Input Dims": [[1, 2048], [], []], "Input Strides": [[2048, 1], [], []], "Input type": ["c10::BFloat16", "Scalar", "Scalar"]} |
| 5.44 | 640 | quant_gemm | ok | True | `nvjet_sm100_tst_64x8_64x16_2x4_h_bz_TNT` | external_id=108518: `aten::view` {"Concrete Inputs": ["", "[-1]"], "Input Dims": [[267, 2048], []], "Input Strides": [[2048, 1], []], "Input type": ["c10::BFloat16", "ScalarList"]} |

The CSV/JSON siblings contain full sample metadata and trace paths.
