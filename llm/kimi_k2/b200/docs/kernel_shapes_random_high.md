# Kernel Shape Inventory — random_high

- Model: `moonshotai/Kimi-K2-Instruct`
- Dataset: `random`
- Concurrency: `high`
- Threshold: GPU kernel name share `> 2.0%`
- Total GPU kernel time: `3648.7 ms`
- Trace files: `8`

| % GPU | Calls | Category | Shape | SGLang relevant | Kernel | Shape provenance |
|---:|---:|---|---|---|---|---|
| 13.32 | 2520 | quant_gemm | ok | True | `bmm_E4m3_E4m3E4m3_Fp32_t128x32x128u2_s6_et64x32_m64x32x32_c1x1x1_rM_TN_transOut_noShfl_dsFp8_schedS_bN_tma_tmaSf_rgTma_clmp_lbW2_dynB_sm100f` | nearest_preceding_shape_cpu_op: `aten::as_strided` {"Concrete Inputs": ["", "[100, 163840]", "[163840, 1]", "0"], "Input Dims": [[104, 163840], [], [], []], "Input Strides": [[163840, 1], [], [], []], "Input type": ["float", "Sc... |
| 6.40 | 1560 | quant_gemm | ok | True | `bmm_Bfloat16_E4m3E4m3_Fp32_t128x32x128u2_s6_et64x32_m64x32x32_c1x1x1_rM_TN_transOut_noShfl_dsFp8_schPd4x2x2x3_bN_rgTma_clmp_dynB_sm100f` | external_id=43285: `sglang::trtllm_fp8_block_scale_moe_wrapper` {"Concrete Inputs": ["", "", "", "", "", "", "", "", "384", "8", "1", "1", "256", "0", "384", "2.827", "2", "False", "0", "", "4096", "1", "3"], "Input Dims": [[2555, 384], [384... |
| 6.24 | 22936 | quant_gemm | ok | True | `void per_token_group_quant_8bit_kernel<NaiveScheduler, 128, 8, __nv_bfloat16, c10::Float8_e4m3fn, true, true, false, unsigned int>(__nv_bfloat16 const*, c10::Float8_e4m3fn*, unsigned int*, int const*, int, int, int, int, int)` | timestamp_enclosure: `sglang::unified_attention_with_output` {"Concrete Inputs": ["", "", "", "", "True", "5", "", "", "", "", "", "", ""], "Input Dims": [[48, 8, 512], [48, 1, 512], [48, 1, 512], [48, 4096], [], [], [48, 8, 64], [48, 1, ... |
| 6.22 | 840 | quant_gemm | ok | True | `bmm_E4m3_E4m3E4m3_Fp32_t128x32x128u2_s6_et64x32_m64x32x32_c1x1x1_rM_TN_transOut_noShfl_dsFp8_schPd4x2x2x3_bN_tma_tmaSf_rgTma_clmp_lbW2_dynB_sm100f` | external_id=51405: `sglang::trtllm_fp8_block_scale_moe_wrapper` {"Concrete Inputs": ["", "", "", "", "", "", "", "", "384", "8", "1", "1", "256", "0", "384", "2.827", "2", "False", "0", "", "4096", "1", "3"], "Input Dims": [[2555, 384], [384... |
| 4.99 | 1800 | quant_gemm | ok | True | `bmm_Bfloat16_E4m3E4m3_Fp32_t128x32x128_s6_et64x32_m64x32x32_c1x1x1_rM_TN_transOut_noShfl_dsFp8_schPd4x2x2x3_bN_rgTma_clmp_dynB_sm100f` | nearest_preceding_shape_cpu_op: `aten::copy_` {"Concrete Inputs": ["", "", "True"], "Input Dims": [[100], [100], []], "Input Strides": [[1], [1], []], "Input type": ["long int", "long int", "Scalar"]} |
| 4.75 | 6776 | comm | ok | True | `void flashinfer::trtllm_allreduce_fusion::allreduce_fusion_kernel_oneshot_lamport<(flashinfer::trtllm_allreduce_fusion::AllReduceFusionPattern)1, __nv_bfloat16, 8, false, false>(flashinfer::trtllm_allreduce_fusion::AllReduceFusionParams<__nv_bfloat16>)` | timestamp_enclosure: `aten::slice` {"Concrete Inputs": ["", "0", "0", "38", "1"], "Input Dims": [[48, 1, 64], [], [], [], []], "Input Strides": [[2112, 64, 1], [], [], [], []], "Input type": ["c10::BFloat16", "Sc... |
| 2.90 | 480 | quant_gemm | ok | True | `bmm_E4m3_E4m3E4m3_Fp32_t128x64x128u2_s6_et64x64_m64x64x32_c1x1x1_rM_TN_transOut_noShfl_dsFp8_schPd4x2x2x3_bN_tma_tmaSf_rgTma_clmp_lbW4_dynB_sm100f` | timestamp_enclosure: `aten::mm` {"Concrete Inputs": ["", ""], "Input Dims": [[17, 7168], [7168, 20480]], "Input Strides": [[7168, 1], [1, 7168]], "Input type": ["c10::BFloat16", "c10::BFloat16"]} |
| 2.62 | 2928 | attention | ok | True | `fmhaSm100fKernel_QkvBfloat16OBfloat16HQk576HV512PagedKvDenseP64VarSeqQ8Kv128PersistentSwapsAbForGen` | nearest_preceding_shape_cpu_op: `aten::as_strided` {"Concrete Inputs": ["", "[31]", "[1]", "512"], "Input Dims": [[543], [], [], []], "Input Strides": [[1], [], [], []], "Input type": ["long int", "ScalarList", "ScalarList", "Sc... |

The CSV/JSON siblings contain full sample metadata and trace paths.
