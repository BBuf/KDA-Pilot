# Kernel Shape Inventory — sharegpt_high

- Model: `zai-org/GLM-5.1-FP8`
- Dataset: `sharegpt`
- Concurrency: `high`
- Threshold: GPU kernel name share `> 2.0%`
- Total GPU kernel time: `12765.7 ms`
- Trace files: `8`

| % GPU | Calls | Category | Shape | SGLang relevant | Kernel | Shape provenance |
|---:|---:|---|---|---|---|---|
| 36.73 | 10064 | comm | ok | True | `void flashinfer::trtllm_allreduce_fusion::allreduce_fusion_kernel_oneshot_lamport<(flashinfer::trtllm_allreduce_fusion::AllReduceFusionPattern)1, __nv_bfloat16, 8, false, false>(flashinfer::trtllm_allreduce_fusion::AllReduceFusionParams<__nv_bfloat16>)` | external_id=337558: `aten::copy_` {"Concrete Inputs": ["", "", "False"], "Input Dims": [[], [], []], "Input Strides": [[], [], []], "Input type": ["int", "long int", "Scalar"]} |
| 13.39 | 1248 | comm | ok | True | `void flashinfer::trtllm_allreduce_fusion::allreduce_fusion_kernel_twoshot_sync<(flashinfer::trtllm_allreduce_fusion::AllReduceFusionPattern)1, __nv_bfloat16, 8, false>(flashinfer::trtllm_allreduce_fusion::AllReduceFusionParams<__nv_bfloat16>, std::array<int, 8>, std::array<int, 8>)` | external_id=290949: `sglang::flashinfer_allreduce_residual_rmsnorm` {"Concrete Inputs": ["", "", "", "1.0000000000000001e-05", "2048", "", "False", "False", "True"], "Input Dims": [[1269, 6144], [1269, 6144], [6144], [], [], [], [], [], []], "In... |
| 6.16 | 1216 | quant_gemm | ok | True | `nvjet_sm100_tst_64x8_64x16_2x4_h_bz_splitK_TNT` | external_id=337575: `aten::item` {"Concrete Inputs": [""], "Input Dims": [[]], "Input Strides": [[]], "Input type": ["long int"]} |
| 5.86 | 608 | quant_gemm | ok | True | `nvjet_sm100_tst_32x64_64x16_4x1_v_bz_splitK_TNN` | external_id=261893: `aten::mm` {"Concrete Inputs": ["", ""], "Input Dims": [[16, 6144], [6144, 256]], "Input Strides": [[6144, 1], [1, 6144]], "Input type": ["c10::BFloat16", "c10::BFloat16"]} |
| 2.97 | 3040 | quant_gemm | ok | True | `bmm_E4m3_E4m3E4m3_Fp32_t128x16x128u2_s6_et64x16_m64x16x32_c1x1x1_rM_TN_transOut_noShfl_dsFp8_schPd4x2x2x3_bN_tma_tmaSf_rgTma_clmp_lbW2_dynB_sm100f` | timestamp_enclosure: `aten::copy_` {"Concrete Inputs": ["", "", "False"], "Input Dims": [[1], [1], []], "Input Strides": [[1], [1], []], "Input type": ["long unsigned int", "long unsigned int", "Scalar"]} |

The CSV/JSON siblings contain full sample metadata and trace paths.
