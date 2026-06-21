# Kernel Shape Inventory — sharegpt_mid

- Model: `deepseek-ai/DeepSeek-V3`
- Dataset: `sharegpt`
- Concurrency: `mid`
- Threshold: GPU kernel name share `> 2.0%`
- Total GPU kernel time: `7655.1 ms`
- Trace files: `8`

| % GPU | Calls | Category | Shape | SGLang relevant | Kernel | Shape provenance |
|---:|---:|---|---|---|---|---|
| 29.21 | 7904 | comm | ok | True | `void flashinfer::trtllm_allreduce_fusion::allreduce_fusion_kernel_oneshot_lamport<(flashinfer::trtllm_allreduce_fusion::AllReduceFusionPattern)1, __nv_bfloat16, 8, false, false>(flashinfer::trtllm_allreduce_fusion::AllReduceFusionParams<__nv_bfloat16>)` | external_id=148847: `aten::unsqueeze_` {"Concrete Inputs": ["", "1"], "Input Dims": [[1], []], "Input Strides": [[1], []], "Input type": ["int", "Scalar"]} |
| 7.28 | 472 | gemm | ok | True | `void flashinfer::trtllm_dsv3_router_gemm::router_gemm_kernel<__nv_bfloat16, float, 128, 8, 6, 256, 7168>(float*, __nv_bfloat16 const*, __nv_bfloat16 const*)` | external_id=148860: `aten::_to_copy` {"Concrete Inputs": ["", "4", "", "", "", "False", ""], "Input Dims": [[1, 1], [], [], [], [], [], []], "Input Strides": [[1, 1], [], [], [], [], [], []], "Input type": ["int", ... |
| 5.60 | 472 | gemm | ok | True | `void flashinfer::trtllm_dsv3_router_gemm::router_gemm_kernel<__nv_bfloat16, float, 128, 8, 16, 256, 7168>(float*, __nv_bfloat16 const*, __nv_bfloat16 const*)` | external_id=115350: `aten::empty` {"Concrete Inputs": ["[16, 2112]", "15", "0", "", "False", ""], "Input Dims": [[], [], [], [], [], []], "Input Strides": [[], [], [], [], [], []], "Input type": ["ScalarList", "... |
| 4.03 | 2124 | quant_gemm | ok | True | `bmm_E4m3_E4m3E4m3_Fp32_t128x16x128u2_s6_et64x16_m64x16x32_c1x1x1_rM_TN_transOut_noShfl_dsFp8_schPd4x2x2x3_bN_tma_tmaSf_rgTma_clmp_lbW2_dynB_sm100f` | nearest_preceding_shape_cpu_op: `aten::as_strided` {"Concrete Inputs": ["", "[6489]", "[1]", "0"], "Input Dims": [[6489], [], [], []], "Input Strides": [[1], [], [], []], "Input type": ["long int", "ScalarList", "ScalarList", "S... |
| 2.35 | 472 | quant_gemm | ok | True | `bmm_E4m3_E4m3E4m3_Fp32_t128x64x128u2_s6_et64x64_m64x64x32_c1x1x1_rM_TN_transOut_noShfl_dsFp8_schPd4x2x2x3_bN_tma_tmaSf_rgTma_clmp_lbW4_dynB_sm100f` | external_id=116969: `sglang::trtllm_fp8_block_scale_moe_wrapper` {"Concrete Inputs": ["", "", "", "", "", "", "", "", "256", "8", "8", "4", "256", "0", "256", "2.5", "2", "False", "0", "", "8192", "1", "3"], "Input Dims": [[5397, 256], [256],... |
| 2.04 | 2976 | attention | ok | True | `fmhaSm100fKernel_QkvBfloat16OBfloat16HQk576HV512PagedKvDenseP64VarSeqQ16Kv128PersistentSwapsAbForGen` | timestamp_enclosure: `aten::_unique2` {"Concrete Inputs": ["", "True", "False", "False"], "Input Dims": [[30], [], [], []], "Input Strides": [[1], [], [], []], "Input type": ["int", "Scalar", "Scalar", "Scalar"]} |

The CSV/JSON siblings contain full sample metadata and trace paths.
