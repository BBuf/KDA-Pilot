# Kernel Shape Inventory — sharegpt_high

- Model: `stepfun-ai/Step-3.5-Flash`
- Dataset: `sharegpt`
- Concurrency: `high`
- Threshold: GPU kernel name share `> 2.0%`
- Total GPU kernel time: `427.7 ms`
- Trace files: `4`

| % GPU | Calls | Category | Shape | SGLang relevant | Kernel | Shape provenance |
|---:|---:|---|---|---|---|---|
| 41.59 | 4788 | memory_bound | ok | True | `void sglang::cross_device_reduce_1stage<__nv_bfloat16, 4>(sglang::RankData*, sglang::RankSignals, sglang::Signal*, __nv_bfloat16*, int, int)` | nearest_preceding_shape_cpu_op: `aten::copy_` {"Concrete Inputs": ["", "", "False"], "Input Dims": [[1, 1], [1, 1], []], "Input Strides": [[4096, 1], [1, 1], []], "Input type": ["int", "int", "Scalar"]} |
| 15.80 | 3024 | moe | ok | True | `fused_moe_kernel` | external_id=1078242: `sglang::inplace_fused_experts` {"Concrete Inputs": ["", "", "", "", "", "", "", "", "True", "False", "False", "False", "False", "False", "False", "", "", "", "", "", "", "", "", "", "", "False"], "Input Dims"... |
| 4.30 | 1812 | quant_gemm | ok | True | `nvjet_tst_32x64_64x16_4x1_v_bz_TNN` | external_id=1079912: `aten::mm` {"Concrete Inputs": ["", ""], "Input Dims": [[16, 4096], [4096, 3584]], "Input Strides": [[4096, 1], [1, 4096]], "Input type": ["c10::BFloat16", "c10::BFloat16"]} |
| 3.28 | 1512 | moe | ok | True | `void moeTopK<256>(float const*, bool const*, float*, int*, int, int, int, int, bool, float const*)` | timestamp_enclosure: `aten::index` {"Concrete Inputs": ["", ""], "Input Dims": [[1603073], []], "Input Strides": [[1], []], "Input type": ["long int", ""]} |
| 3.08 | 4896 | norm | ok | True | `void flashinfer::norm::RMSNormKernel<8u, __nv_bfloat16>(__nv_bfloat16*, __nv_bfloat16*, __nv_bfloat16*, unsigned int, unsigned int, unsigned int, float, float)` | nearest_preceding_shape_cpu_op: `aten::view` {"Concrete Inputs": ["", "[1]"], "Input Dims": [[1], []], "Input Strides": [[1], []], "Input type": ["long int", "ScalarList"]} |
| 2.57 | 1440 | quant_gemm | ok | True | `nvjet_tst_64x8_64x16_4x1_v_bz_splitK_TNT` | nearest_preceding_shape_cpu_op: `aten::copy_` {"Concrete Inputs": ["", "", "False"], "Input Dims": [[1, 1], [1, 1], []], "Input Strides": [[4096, 1], [1, 1], []], "Input type": ["int", "int", "Scalar"]} |

The CSV/JSON siblings contain full sample metadata and trace paths.
