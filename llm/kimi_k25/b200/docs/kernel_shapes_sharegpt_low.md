# Kernel Shape Inventory — sharegpt_low

- Model: `moonshotai/Kimi-K2.5`
- Dataset: `sharegpt`
- Concurrency: `low`
- Threshold: GPU kernel name share `> 2.0%`
- Total GPU kernel time: `2122.6 ms`
- Trace files: `8`

| % GPU | Calls | Category | Shape | SGLang relevant | Kernel | Shape provenance |
|---:|---:|---|---|---|---|---|
| 37.56 | 8712 | comm | ok | True | `void flashinfer::trtllm_allreduce_fusion::allreduce_fusion_kernel_oneshot_lamport<(flashinfer::trtllm_allreduce_fusion::AllReduceFusionPattern)1, __nv_bfloat16, 8, false, false>(flashinfer::trtllm_allreduce_fusion::AllReduceFusionParams<__nv_bfloat16>)` | external_id=74069: `sglang::flashinfer_allreduce_residual_rmsnorm` {"Concrete Inputs": ["", "", "", "1.0000000000000001e-05", "2048", "", "False", "False", "False"], "Input Dims": [[15, 7168], [15, 7168], [7168], [], [], [], [], [], []], "Input... |
| 19.70 | 488 | gemm | ok | True | `void fused_a_gemm_kernel<1, 2112, 7168, 16, 16, 256, 12>(__nv_bfloat16*, __nv_bfloat16 const*, __nv_bfloat16 const*, int)` | external_id=74085: `sgl_kernel::dsv3_fused_a_gemm` {"Concrete Inputs": ["", "", ""], "Input Dims": [[15, 2112], [15, 7168], [7168, 2112]], "Input Strides": [[2112, 1], [7168, 1], [1, 7168]], "Input type": ["c10::BFloat16", "c10:... |
| 3.15 | 2340 | quant_gemm | ok | True | `bmm_Bfloat16_MxInt4Bfloat16_castBfloat16_Fp32_Ab32_t128x16x256_s3_et128x16_m256x16x16_c2x1x1_rM_BN_transOut_schPd2x1x2x3_biasBfloat16Mn_bN_tma_tmaSf_rgTma_clmp_swiGlu_dynB_sm100f` | nearest_preceding_shape_cpu_op: `aten::empty` {"Concrete Inputs": ["[1920, 7168]", "15", "", "", "", ""], "Input Dims": [[], [], [], [], [], []], "Input Strides": [[], [], [], [], [], []], "Input type": ["ScalarList", "Scal... |
| 2.46 | 3904 | attention | ok | True | `fmhaSm100fKernel_QkvBfloat16OBfloat16HQk576HV512HVPerCta256PagedKvDenseP64MultiCtasKvVarSeqQ8Kv128StaticSwapsAbForGen` | nearest_preceding_shape_cpu_op: `aten::resolve_neg` {"Concrete Inputs": [""], "Input Dims": [[1]], "Input Strides": [[1]], "Input type": ["long int"]} |
| 2.25 | 11712 | quant_gemm | ok | True | `nvjet_sm100_tst_64x8_64x16_4x1_v_bz_TNT` | timestamp_enclosure: `gloo:broadcast` {"Concrete Inputs": [""], "Input Dims": [[1]], "Input Strides": [[1]], "Input type": ["long int"]} |
| 2.20 | 3840 | quant_gemm | ok | True | `nvjet_sm100_tst_32x64_64x16_4x1_v_bz_splitK_TNN` | timestamp_enclosure: `aten::_to_copy` {"Concrete Inputs": ["", "4", "0", "", "", "True", ""], "Input Dims": [[1], [], [], [], [], [], []], "Input Strides": [[1], [], [], [], [], [], []], "Input type": ["long int", "... |
| 2.12 | 3904 | gemm | ok | True | `void fused_a_gemm_kernel<1, 2112, 7168, 16, 8, 256, 16>(__nv_bfloat16*, __nv_bfloat16 const*, __nv_bfloat16 const*, int)` | timestamp_enclosure: `gloo:broadcast` {"Concrete Inputs": [""], "Input Dims": [[1]], "Input Strides": [[1]], "Input type": ["long int"]} |
| 2.08 | 4320 | quant_gemm | ok | True | `bmm_Bfloat16_MxInt4Bfloat16_castBfloat16_Fp32_Ab32_t128x16x256_s3_et128x16_m128x16x16_c1x1x1_rM_BN_transOut_schPd2x1x2x3_bN_rgTma_clmp_dynB_sm100f` | nearest_preceding_shape_cpu_op: `aten::empty` {"Concrete Inputs": ["[1920, 7168]", "15", "", "", "", ""], "Input Dims": [[], [], [], [], [], []], "Input Strides": [[], [], [], [], [], []], "Input type": ["ScalarList", "Scal... |

The CSV/JSON siblings contain full sample metadata and trace paths.
