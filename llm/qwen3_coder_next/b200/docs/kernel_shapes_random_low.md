# Kernel Shape Inventory — random_low

- Model: `Qwen/Qwen3-Coder-Next`
- Dataset: `random`
- Concurrency: `low`
- Threshold: GPU kernel name share `> 2.0%`
- Total GPU kernel time: `284.2 ms`
- Trace files: `2`

| % GPU | Calls | Category | Shape | SGLang relevant | Kernel | Shape provenance |
|---:|---:|---|---|---|---|---|
| 34.40 | 1710 | comm | ok | True | `void flashinfer::trtllm_allreduce_fusion::allreduce_fusion_kernel_oneshot_lamport<(flashinfer::trtllm_allreduce_fusion::AllReduceFusionPattern)1, __nv_bfloat16, 2, false, false>(flashinfer::trtllm_allreduce_fusion::AllReduceFusionParams<__nv_bfloat16>)` | external_id=2434: `sglang::flashinfer_allreduce_residual_rmsnorm` {"Concrete Inputs": ["", "", "", "9.9999999999999995e-07", "2048", "", "False", "False", "True"], "Input Dims": [[38, 2048], [38, 2048], [2048], [], [], [], [], [], []], "Input ... |
| 16.74 | 192 | quant_gemm | ok | True | `nvjet_sm100_tst_64x8_64x16_2x4_h_bz_TNT` | external_id=2452: `aten::mm` {"Concrete Inputs": ["", ""], "Input Dims": [[38, 2048], [2048, 512]], "Input Strides": [[2048, 1], [1, 2048]], "Input type": ["c10::BFloat16", "c10::BFloat16"]} |
| 10.40 | 72 | quant_gemm | ok | True | `nvjet_sm100_tst_128x24_64x11_4x2_h_bz_TNT` | external_id=7735: `aten::mm` {"Concrete Inputs": ["", ""], "Input Dims": [[38, 2048], [2048, 6144]], "Input Strides": [[2048, 1], [1, 2048]], "Input type": ["c10::BFloat16", "c10::BFloat16"]} |
| 3.84 | 24 | quant_gemm | ok | True | `nvjet_sm100_tst_64x24_64x16_1x2_h_bz_TNT` | external_id=2515: `aten::mm` {"Concrete Inputs": ["", ""], "Input Dims": [[38, 2048], [2048, 4608]], "Input Strides": [[2048, 1], [1, 2048]], "Input type": ["c10::BFloat16", "c10::BFloat16"]} |
| 3.74 | 1728 | quant_gemm | ok | True | `nvjet_sm100_tst_16x64_64x16_4x1_v_bz_TNN` | nearest_preceding_shape_cpu_op: `aten::as_strided` {"Concrete Inputs": ["", "[1, 151936]", "[151936, 1]", "0"], "Input Dims": [[1, 151936], [], [], []], "Input Strides": [[151936, 1], [], [], []], "Input type": ["float", "Scalar... |
| 2.96 | 1536 | quant_gemm | ok | True | `nvjet_sm100_tst_32x64_64x16_4x1_v_bz_splitK_TNN` | nearest_preceding_shape_cpu_op: `aten::as_strided` {"Concrete Inputs": ["", "[1, 151936]", "[151936, 1]", "0"], "Input Dims": [[1, 151936], [], [], []], "Input Strides": [[151936, 1], [], [], []], "Input type": ["float", "Scalar... |
| 2.85 | 768 | quant_gemm | ok | True | `nvjet_sm100_tst_64x8_64x16_4x1_v_bz_TNT` | timestamp_enclosure: `aten::copy_` {"Concrete Inputs": ["", "", "False"], "Input Dims": [[1], [1], []], "Input Strides": [[1], [1], []], "Input type": ["long int", "long int", "Scalar"]} |

The CSV/JSON siblings contain full sample metadata and trace paths.
