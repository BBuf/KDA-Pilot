# Kernel Shape Inventory — random_low

- Model: `google/gemma-4-26B-A4B-it`
- Dataset: `random`
- Concurrency: `low`
- Threshold: GPU kernel name share `> 2.0%`
- Total GPU kernel time: `41.1 ms`
- Trace files: `1`

| % GPU | Calls | Category | Shape | SGLang relevant | Kernel | Shape provenance |
|---:|---:|---|---|---|---|---|
| 22.87 | 540 | moe | ok | True | `fused_moe_kernel` | external_id=457: `sglang::inplace_fused_experts` {"Concrete Inputs": ["", "", "", "", "", "", "", "", "True", "False", "False", "False", "False", "False", "False", "", "", "", "", "", "", "", "", "", "", "False", ""], "Input D... |
| 10.40 | 480 | quant_gemm | ok | True | `nvjet_sm100_tst_32x64_64x16_4x1_v_bz_TNN` | timestamp_enclosure: `aten::argmax` {"Concrete Inputs": ["", "-1", "False"], "Input Dims": [[1, 262144], [], []], "Input Strides": [[262144, 1], [], []], "Input type": ["float", "Scalar", "Scalar"]} |
| 8.57 | 270 | gemm | ok | True | `_gemma_qkv_rmsnorm_kernel` | external_id=889: `aten::_reshape_alias` {"Concrete Inputs": ["", "[38, 8, 256]", "[8192, 256, 1]"], "Input Dims": [[38, 2048], [], []], "Input Strides": [[8192, 1], [], []], "Input type": ["c10::BFloat16", "ScalarList... |
| 7.90 | 1089 | gemm | ok | True | `kernel_cutlass_kernel_flashinfernormkernelsrmsnormRMSNormKernel_object_at__tensorptrbf16gmemalign128o281628161_tensorptrbf16gmemalign16o28161_tensorptrbf16gmemalign128o281628161___True_4__0` | nearest_preceding_shape_cpu_op: `aten::copy_` {"Concrete Inputs": ["", "", "False"], "Input Dims": [[1, 1], [1, 1], []], "Input Strides": [[4096, 1], [1, 1], []], "Input type": ["int", "int", "Scalar"]} |
| 5.20 | 280 | quant_gemm | ok | True | `nvjet_sm100_tst_64x8_64x16_4x1_v_bz_splitK_TNT` | nearest_preceding_shape_cpu_op: `aten::copy_` {"Concrete Inputs": ["", "", "False"], "Input Dims": [[1, 1], [1, 1], []], "Input Strides": [[4096, 1], [1, 1], []], "Input type": ["int", "int", "Scalar"]} |
| 5.11 | 200 | quant_gemm | ok | True | `nvjet_sm100_tst_64x8_64x16_4x1_v_bz_TNT` | timestamp_enclosure: `aten::_index_put_impl_` {"Concrete Inputs": ["", "", "", "False", "False"], "Input Dims": [[2049], [], [], [], []], "Input Strides": [[1], [], [], [], []], "Input type": ["long int", "", "long int", "S... |
| 4.82 | 9 | quant_gemm | ok | True | `nvjet_sm100_tst_256x8_64x6_2x1_v_bz_TNT` | nearest_preceding_shape_cpu_op: `aten::copy_` {"Concrete Inputs": ["", "", "True"], "Input Dims": [[1], [1], []], "Input Strides": [[1], [1], []], "Input type": ["long int", "long int", "Scalar"]} |
| 4.07 | 200 | attention | ok | True | `fmhaSm100fKernel_QkvBfloat16OBfloat16H256PagedKvSlidingOrChunkedCausalP64MultiCtasKvCgaVarSeqQ8Kv128StaticSwapsAbForGen` | nearest_preceding_shape_cpu_op: `aten::resolve_neg` {"Concrete Inputs": [""], "Input Dims": [[1]], "Input Strides": [[1]], "Input type": ["long int"]} |
| 2.54 | 240 | quant_gemm | ok | True | `nvjet_sm100_tst_32x64_64x16_4x1_v_bz_splitK_TNN` | nearest_preceding_shape_cpu_op: `aten::as_strided` {"Concrete Inputs": ["", "[38]", "[1]", "0"], "Input Dims": [[38], [], [], []], "Input Strides": [[1], [], [], []], "Input type": ["long int", "ScalarList", "ScalarList", "Scala... |
| 2.20 | 270 | gemm | ok | True | `kernel_cutlass_kernel_flashinfernormkernelsfused_add_rmsnormFusedAddRMSNormKernel_object_at__tensorptrbf16gmemalign128o281628161_tensorptrbf16gmemalign128o281628161_tensorptrbf16gmemalign_0` | external_id=2404: `aten::view` {"Concrete Inputs": ["", "[-1, 2048]"], "Input Dims": [[38, 8, 256], []], "Input Strides": [[8192, 256, 1], []], "Input type": ["c10::BFloat16", "ScalarList"]} |
| 2.11 | 270 | gemm | ok | True | `_gemma_dual_rmsnorm_residual_kernel` | timestamp_enclosure: `aten::argmax` {"Concrete Inputs": ["", "-1", "False"], "Input Dims": [[1, 262144], [], []], "Input Strides": [[262144, 1], [], []], "Input type": ["float", "Scalar", "Scalar"]} |

The CSV/JSON siblings contain full sample metadata and trace paths.
