# Kernel Shape Inventory — random_low

- Model: `stepfun-ai/Step-3.5-Flash`
- Dataset: `random`
- Concurrency: `low`
- Threshold: GPU kernel name share `> 2.0%`
- Total GPU kernel time: `503.4 ms`
- Trace files: `4`

| % GPU | Calls | Category | Shape | SGLang relevant | Kernel | Shape provenance |
|---:|---:|---|---|---|---|---|
| 48.64 | 4788 | memory_bound | ok | True | `void sglang::cross_device_reduce_1stage<__nv_bfloat16, 4>(sglang::RankData*, sglang::RankSignals, sglang::Signal*, __nv_bfloat16*, int, int)` | external_id=21726: `c10d::broadcast_` {"Concrete Inputs": ["", "", "0", "0", "False", "-1"], "Input Dims": [[[1]], [], [], [], [], []], "Input Strides": [[[1]], [], [], [], [], []], "Input type": ["TensorList", "", ... |
| 14.66 | 3024 | moe | ok | True | `fused_moe_kernel` | external_id=425741: `sglang::inplace_fused_experts` {"Concrete Inputs": ["", "", "", "", "", "", "", "", "True", "False", "False", "False", "False", "False", "False", "", "", "", "", "", "", "", "", "", "7.", "False"], "Input Dim... |
| 3.08 | 1536 | quant_gemm | ok | True | `nvjet_tst_32x64_64x16_4x1_v_bz_TNN` | external_id=23753: `aten::empty` {"Concrete Inputs": ["[1]", "4", "0", "", "False", ""], "Input Dims": [[], [], [], [], [], []], "Input Strides": [[], [], [], [], [], []], "Input type": ["ScalarList", "Scalar",... |
| 2.79 | 1512 | moe | ok | True | `void moeTopK<256>(float const*, bool const*, float*, int*, int, int, int, int, bool, float const*)` | external_id=21726: `c10d::broadcast_` {"Concrete Inputs": ["", "", "0", "0", "False", "-1"], "Input Dims": [[[1]], [], [], [], [], []], "Input Strides": [[[1]], [], [], [], [], []], "Input type": ["TensorList", "", ... |
| 2.64 | 4896 | norm | ok | True | `void flashinfer::norm::RMSNormKernel<8u, __nv_bfloat16>(__nv_bfloat16*, __nv_bfloat16*, __nv_bfloat16*, unsigned int, unsigned int, unsigned int, float, float)` | external_id=538414: `sgl_kernel::gemma_rmsnorm` {"Concrete Inputs": ["", "", "", "1.0000000000000001e-05", "True"], "Input Dims": [[38, 4096], [38, 4096], [4096], [], []], "Input Strides": [[4096, 1], [4096, 1], [1], [], []],... |
| 2.19 | 1440 | quant_gemm | ok | True | `nvjet_tst_64x8_64x16_4x1_v_bz_splitK_TNT` | external_id=23753: `aten::empty` {"Concrete Inputs": ["[1]", "4", "0", "", "False", ""], "Input Dims": [[], [], [], [], [], []], "Input Strides": [[], [], [], [], [], []], "Input type": ["ScalarList", "Scalar",... |

The CSV/JSON siblings contain full sample metadata and trace paths.
