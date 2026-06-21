# Kernel Shape Inventory — sharegpt_mid

- Model: `moonshotai/Kimi-K2.6`
- Dataset: `sharegpt`
- Concurrency: `mid`
- Threshold: GPU kernel name share `> 2.0%`
- Total GPU kernel time: `5175.0 ms`
- Trace files: `8`

| % GPU | Calls | Category | Shape | SGLang relevant | Kernel | Shape provenance |
|---:|---:|---|---|---|---|---|
| 30.02 | 7744 | comm | ok | True | `void flashinfer::trtllm_allreduce_fusion::allreduce_fusion_kernel_oneshot_lamport<(flashinfer::trtllm_allreduce_fusion::AllReduceFusionPattern)1, __nv_bfloat16, 8, false, false>(flashinfer::trtllm_allreduce_fusion::AllReduceFusionParams<__nv_bfloat16>)` | external_id=108234: `sglang::flashinfer_allreduce_residual_rmsnorm` {"Concrete Inputs": ["", "", "", "1.0000000000000001e-05", "2048", "", "False", "False", "True"], "Input Dims": [[1, 7168], [1, 7168], [7168], [], [], [], [], [], []], "Input St... |
| 7.73 | 488 | gemm | ok | True | `void fused_a_gemm_kernel<1, 2112, 7168, 16, 8, 256, 16>(__nv_bfloat16*, __nv_bfloat16 const*, __nv_bfloat16 const*, int)` | external_id=107260: `sgl_kernel::dsv3_fused_a_gemm` {"Concrete Inputs": ["", "", ""], "Input Dims": [[1, 2112], [1, 7168], [7168, 2112]], "Input Strides": [[2112, 1], [7168, 1], [1, 7168]], "Input type": ["c10::BFloat16", "c10::B... |
| 7.20 | 488 | gemm | ok | True | `void fused_a_gemm_kernel<1, 2112, 7168, 16, 16, 256, 12>(__nv_bfloat16*, __nv_bfloat16 const*, __nv_bfloat16 const*, int)` | external_id=78533: `sgl_kernel::dsv3_fused_a_gemm` {"Concrete Inputs": ["", "", ""], "Input Dims": [[15, 2112], [15, 7168], [7168, 2112]], "Input Strides": [[2112, 1], [7168, 1], [1, 7168]], "Input type": ["c10::BFloat16", "c10:... |
| 5.27 | 2880 | quant_gemm | ok | True | `bmm_Bfloat16_MxInt4Bfloat16_castBfloat16_Fp32_Ab32_t128x16x256u2_s3_et128x16_m256x16x16_c2x1x1_rM_BN_transOut_schPd2x1x2x3_biasBfloat16Mn_bN_tma_tmaSf_rgTma_clmp_swiGlu_dynB_sm100f` | nearest_preceding_shape_cpu_op: `aten::as_strided` {"Concrete Inputs": ["", "[0]", "[1]", "110083696"], "Input Dims": [[257], [], [], []], "Input Strides": [[1], [], [], []], "Input type": ["int", "ScalarList", "ScalarList", "Sc... |
| 4.52 | 480 | quant_gemm | ok | True | `bmm_Bfloat16_MxInt4Bfloat16_castBfloat16_Fp32_Ab32_t128x64x256u2_s3_et128x64_m128x64x16_c1x1x1_rM_BN_transOut_schPd2x1x2x3_bN_tma_tmaSf_rgTma_clmp_swiGlu_dynB_sm100f` | nearest_preceding_shape_cpu_op: `aten::empty` {"Concrete Inputs": ["[60352, 7168]", "15", "", "", "", ""], "Input Dims": [[], [], [], [], [], []], "Input Strides": [[], [], [], [], [], []], "Input type": ["ScalarList", "Sca... |
| 3.02 | 2880 | quant_gemm | ok | True | `bmm_Bfloat16_MxInt4Bfloat16_castBfloat16_Fp32_Ab32_t128x16x256_s3_et128x16_m256x16x16_c2x1x1_rM_BN_transOut_schPd2x1x2x3_bN_rgTma_clmp_dynB_sm100f` | nearest_preceding_shape_cpu_op: `aten::copy_` {"Concrete Inputs": ["", "", "True"], "Input Dims": [[32], [32], []], "Input Strides": [[1], [1], []], "Input type": ["long int", "long int", "Scalar"]} |
| 2.51 | 480 | quant_gemm | ok | True | `bmm_Bfloat16_MxInt4Bfloat16_castBfloat16_Fp32_Ab32_t128x64x256_s3_et128x64_m128x64x16_c1x1x1_rM_BN_transOut_schPd2x1x2x3_bN_rgTma_clmp_dynB_sm100f` | timestamp_enclosure: `aten::mm` {"Concrete Inputs": ["", ""], "Input Dims": [[4527, 256], [256, 7168]], "Input Strides": [[256, 1], [1, 256]], "Input type": ["c10::BFloat16", "c10::BFloat16"]} |

The CSV/JSON siblings contain full sample metadata and trace paths.
