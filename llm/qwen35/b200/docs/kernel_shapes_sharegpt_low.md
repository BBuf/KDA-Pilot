# Kernel Shape Inventory — sharegpt_low

- Model: `nvidia/Qwen3.5-397B-A17B-NVFP4`
- Dataset: `sharegpt`
- Concurrency: `low`
- Threshold: GPU kernel name share `> 2.0%`
- Total GPU kernel time: `1026.6 ms`
- Trace files: `4`

| % GPU | Calls | Category | Shape | SGLang relevant | Kernel | Shape provenance |
|---:|---:|---|---|---|---|---|
| 38.25 | 4284 | comm | ok | True | `void flashinfer::trtllm_allreduce_fusion::allreduce_fusion_kernel_oneshot_lamport<(flashinfer::trtllm_allreduce_fusion::AllReduceFusionPattern)1, __nv_bfloat16, 4, false, false>(flashinfer::trtllm_allreduce_fusion::AllReduceFusionParams<__nv_bfloat16>)` | external_id=92260: `sglang::flashinfer_allreduce_residual_rmsnorm` {"Concrete Inputs": ["", "", "", "9.9999999999999995e-07", "2048", "", "False", "False", "True"], "Input Dims": [[17, 4096], [17, 4096], [4096], [], [], [], [], [], []], "Input ... |
| 16.75 | 480 | quant_gemm | ok | True | `nvjet_sm100_tst_64x8_64x16_2x4_h_bz_splitK_TNT` | external_id=99148: `aten::mm` {"Concrete Inputs": ["", ""], "Input Dims": [[17, 4096], [4096, 512]], "Input Strides": [[4096, 1], [1, 4096]], "Input type": ["c10::BFloat16", "c10::BFloat16"]} |
| 14.15 | 180 | quant_gemm | ok | True | `nvjet_sm100_tst_64x24_64x16_4x1_v_bz_TNT` | external_id=92277: `aten::mm` {"Concrete Inputs": ["", ""], "Input Dims": [[17, 4096], [4096, 5120]], "Input Strides": [[4096, 1], [1, 4096]], "Input type": ["c10::BFloat16", "c10::BFloat16"]} |
| 4.32 | 60 | quant_gemm | ok | True | `nvjet_sm100_tst_64x24_64x16_2x1_v_bz_splitK_TNT` | external_id=94956: `aten::mm` {"Concrete Inputs": ["", ""], "Input Dims": [[17, 4096], [4096, 4608]], "Input Strides": [[4096, 1], [1, 4096]], "Input type": ["c10::BFloat16", "c10::BFloat16"]} |
| 2.80 | 3360 | quant_gemm | ok | True | `nvjet_sm100_tst_64x8_64x16_4x1_v_bz_TNT` | nearest_preceding_shape_cpu_op: `detach_` {"Concrete Inputs": [""], "Input Dims": [[1]], "Input Strides": [[1]], "Input type": ["long int"]} |
| 2.67 | 3840 | quant_gemm | ok | True | `nvjet_sm100_tst_32x64_64x16_4x1_v_bz_splitK_TNN` | timestamp_enclosure: `aten::index` {"Concrete Inputs": ["", ""], "Input Dims": [[996, 262148], []], "Input Strides": [[262148, 1], []], "Input type": ["int", ""]} |

The CSV/JSON siblings contain full sample metadata and trace paths.
