# Kernel Shape Inventory — sharegpt_mid

- Model: `deepseek-ai/DeepSeek-V3.1`
- Dataset: `sharegpt`
- Concurrency: `mid`
- Threshold: GPU kernel name share `> 2.0%`
- Total GPU kernel time: `6972.4 ms`
- Trace files: `8`

| % GPU | Calls | Category | Shape | SGLang relevant | Kernel | Shape provenance |
|---:|---:|---|---|---|---|---|
| 30.39 | 7904 | comm | ok | True | `void flashinfer::trtllm_allreduce_fusion::allreduce_fusion_kernel_oneshot_lamport<(flashinfer::trtllm_allreduce_fusion::AllReduceFusionPattern)1, __nv_bfloat16, 8, false, false>(flashinfer::trtllm_allreduce_fusion::AllReduceFusionParams<__nv_bfloat16>)` | external_id=149446: `aten::_to_copy` {"Concrete Inputs": ["", "6", "", "", "", "False", ""], "Input Dims": [[2, 129280], [], [], [], [], [], []], "Input Strides": [[129280, 1], [], [], [], [], [], []], "Input type"... |
| 6.06 | 472 | gemm | ok | True | `void flashinfer::trtllm_dsv3_router_gemm::router_gemm_kernel<__nv_bfloat16, float, 128, 8, 16, 256, 7168>(float*, __nv_bfloat16 const*, __nv_bfloat16 const*)` | external_id=115484: `aten::_to_copy` {"Concrete Inputs": ["", "6", "", "", "", "False", ""], "Input Dims": [[1, 129280], [], [], [], [], [], []], "Input Strides": [[129280, 1], [], [], [], [], [], []], "Input type"... |
| 4.91 | 2478 | quant_gemm | ok | True | `bmm_E4m3_E4m3E4m3_Fp32_t128x16x128u2_s6_et64x16_m64x16x32_c1x1x1_rM_TN_transOut_noShfl_dsFp8_schPd4x2x2x3_bN_tma_tmaSf_rgTma_clmp_lbW2_dynB_sm100f` | nearest_preceding_shape_cpu_op: `aten::cat` {"Concrete Inputs": ["", "0"], "Input Dims": [[[37], [6]], []], "Input Strides": [[[1], [1]], []], "Input type": ["TensorList", "Scalar"]} |
| 2.57 | 472 | quant_gemm | ok | True | `bmm_E4m3_E4m3E4m3_Fp32_t128x64x128u2_s6_et64x64_m64x64x32_c1x1x1_rM_TN_transOut_noShfl_dsFp8_schPd4x2x2x3_bN_tma_tmaSf_rgTma_clmp_lbW4_dynB_sm100f` | external_id=117006: `aten::view` {"Concrete Inputs": ["", "[5333, -1]"], "Input Dims": [[5333, 1, 512], []], "Input Strides": [[512, 512, 1], []], "Input type": ["c10::BFloat16", "ScalarList"]} |
| 2.55 | 2478 | quant_gemm | ok | True | `bmm_Bfloat16_E4m3E4m3_Fp32_t128x16x128_s6_et64x16_m64x16x32_c1x1x1_rM_TN_transOut_noShfl_dsFp8_schPd4x2x2x3_bN_rgTma_clmp_dynB_sm100f` | nearest_preceding_shape_cpu_op: `aten::resolve_neg` {"Concrete Inputs": [""], "Input Dims": [[32]], "Input Strides": [[1]], "Input type": ["int"]} |
| 2.24 | 2976 | attention | ok | True | `fmhaSm100fKernel_QkvBfloat16OBfloat16HQk576HV512PagedKvDenseP64VarSeqQ16Kv128PersistentSwapsAbForGen` | nearest_preceding_shape_cpu_op: `aten::copy_` {"Concrete Inputs": ["", "", "False"], "Input Dims": [[256], [256], []], "Input Strides": [[1], [1], []], "Input type": ["long int", "int", "Scalar"]} |
| 2.11 | 472 | quant_gemm | ok | True | `bmm_Bfloat16_E4m3E4m3_Fp32_t128x64x128u2_s6_et64x64_m64x64x32_c1x1x1_rM_TN_transOut_noShfl_dsFp8_schPd4x2x2x3_bN_rgTma_clmp_dynB_sm100f` | external_id=126054: `aten::view` {"Concrete Inputs": ["", "[5333, -1]"], "Input Dims": [[5333, 1, 512], []], "Input Strides": [[512, 512, 1], []], "Input type": ["c10::BFloat16", "ScalarList"]} |

The CSV/JSON siblings contain full sample metadata and trace paths.
