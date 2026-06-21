# Kernel Shape Inventory — sharegpt_mid

- Model: `MiniMaxAI/MiniMax-M2`
- Dataset: `sharegpt`
- Concurrency: `mid`
- Threshold: GPU kernel name share `> 2.0%`
- Total GPU kernel time: `1308.8 ms`
- Trace files: `4`

| % GPU | Calls | Category | Shape | SGLang relevant | Kernel | Shape provenance |
|---:|---:|---|---|---|---|---|
| 43.36 | 4464 | moe | ok | True | `fused_moe_kernel` | external_id=44058: `aten::as_strided` {"Concrete Inputs": ["", "[25357, 2, 64, 128]", "[16384, 128, 256, 1]", ""], "Input Dims": [[25357, 64, 2, 128], [], [], []], "Input Strides": [[16384, 256, 128, 1], [], [], []]... |
| 10.92 | 4464 | quant_gemm | ok | True | `_w8a8_block_fp8_matmul` | external_id=44058: `aten::as_strided` {"Concrete Inputs": ["", "[25357, 2, 64, 128]", "[16384, 128, 256, 1]", ""], "Input Dims": [[25357, 64, 2, 128], [], [], []], "Input Strides": [[16384, 256, 128, 1], [], [], []]... |
| 4.16 | 248 | gemm | ok | True | `cutlass3x_sm100_simt_sgemm_f32_f32_f32_f32_f32_64x32x16_1x1x1_3_tnn_align1_bias_f32_relu` | external_id=44058: `aten::as_strided` {"Concrete Inputs": ["", "[25357, 2, 64, 128]", "[16384, 128, 256, 1]", ""], "Input Dims": [[25357, 64, 2, 128], [], [], []], "Input Strides": [[16384, 256, 128, 1], [], [], []]... |
| 3.05 | 1488 | gemm | ok | True | `void cutlass::Kernel2<cutlass_80_simt_sgemm_64x64_8x5_tn_align1>(cutlass_80_simt_sgemm_64x64_8x5_tn_align1::Params)` | external_id=36487: `Torch-Compiled Region: 5/3` {} |
| 2.83 | 992 | attention | ok | True | `fmhaSm100fKernel_QkvFp16OFp16H128PagedKvCausalP64VarSeqQ128Kv128PersistentContext` | external_id=44060: `aten::empty_strided` {"Concrete Inputs": ["[5524, 12, 128]", "[1536, 128, 1]", "5", "0", "", "False"], "Input Dims": [[], [], [], [], [], []], "Input Strides": [[], [], [], [], [], []], "Input type"... |
| 2.72 | 744 | moe | ok | True | `void moe_sum_reduce_kernel_warp_token_topk<c10::Half, 8, 4>(c10::Half const*, c10::Half*, long, long, long, long, long, at::OpMathType<c10::Half>::type)` | external_id=44058: `aten::as_strided` {"Concrete Inputs": ["", "[25357, 2, 64, 128]", "[16384, 128, 256, 1]", ""], "Input Dims": [[25357, 64, 2, 128], [], [], []], "Input Strides": [[16384, 256, 128, 1], [], [], []]... |
| 2.40 | 248 | gemm | ok | True | `cutlass3x_sm100_simt_sgemm_f32_f32_f32_f32_f32_128x64x16_1x1x1_3_tnn_align1_bias_f32_relu` | external_id=41346: `aten::view` {"Concrete Inputs": ["", "[-1, 12, 128]"], "Input Dims": [[3027, 1536], []], "Input Strides": [[1536, 1], []], "Input type": ["c10::Half", "ScalarList"]} |
| 2.23 | 1984 | norm | ok | True | `void flashinfer::norm::FusedAddRMSNormKernel<8u, __half>(__half*, __half*, __half*, unsigned int, unsigned int, unsigned int, float, float)` | external_id=36587: `aten::slice` {"Concrete Inputs": ["", "0", "0", "59", "1"], "Input Dims": [[64, 2, 128], [], [], [], []], "Input Strides": [[2048, 128, 1], [], [], [], []], "Input type": ["c10::Half", "Scal... |
| 2.09 | 8928 | quant_gemm | ok | True | `void (anonymous namespace)::per_token_group_quant_8bit_v2_kernel<(anonymous namespace)::NaiveScheduler, 128, 8, __half, __nv_fp8_e4m3, false, false, false, true, float>(__half const*, __nv_fp8_e4m3*, float*, int const*, int, int, int, int, int)` | external_id=44058: `aten::as_strided` {"Concrete Inputs": ["", "[25357, 2, 64, 128]", "[16384, 128, 256, 1]", ""], "Input Dims": [[25357, 64, 2, 128], [], [], []], "Input Strides": [[16384, 256, 128, 1], [], [], []]... |

The CSV/JSON siblings contain full sample metadata and trace paths.
