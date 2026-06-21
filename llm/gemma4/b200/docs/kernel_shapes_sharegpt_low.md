# Kernel Shape Inventory — sharegpt_low

- Model: `google/gemma-4-26B-A4B-it`
- Dataset: `sharegpt`
- Concurrency: `low`
- Threshold: GPU kernel name share `> 2.0%`
- Total GPU kernel time: `40.4 ms`
- Trace files: `1`

| % GPU | Calls | Category | Shape | SGLang relevant | Kernel | Shape provenance |
|---:|---:|---|---|---|---|---|
| 21.68 | 540 | moe | ok | True | `fused_moe_kernel` | external_id=31812: `sglang::inplace_fused_experts` {"Concrete Inputs": ["", "", "", "", "", "", "", "", "True", "False", "False", "False", "False", "False", "False", "", "", "", "", "", "", "", "", "", "", "False", ""], "Input D... |
| 11.02 | 510 | quant_gemm | ok | True | `nvjet_sm100_tst_32x64_64x16_4x1_v_bz_TNN` | timestamp_enclosure: `aten::copy_` {"Concrete Inputs": ["", "", "True"], "Input Dims": [[1], [1], []], "Input Strides": [[1], [1], []], "Input type": ["long int", "long int", "Scalar"]} |
| 8.71 | 270 | gemm | ok | True | `_gemma_qkv_rmsnorm_kernel` | nearest_preceding_shape_cpu_op: `aten::as_strided` {"Concrete Inputs": ["", "[17, 2048]", "[8192, 1]", "6144"], "Input Dims": [[17, 8192], [], [], []], "Input Strides": [[8192, 1], [], [], []], "Input type": ["c10::BFloat16", "S... |
| 8.04 | 1089 | gemm | ok | True | `kernel_cutlass_kernel_flashinfernormkernelsrmsnormRMSNormKernel_object_at__tensorptrbf16gmemalign128o281628161_tensorptrbf16gmemalign16o28161_tensorptrbf16gmemalign128o281628161___True_4__0` | nearest_preceding_shape_cpu_op: `aten::resolve_neg` {"Concrete Inputs": [""], "Input Dims": [[1]], "Input Strides": [[1]], "Input type": ["long int"]} |
| 5.30 | 280 | quant_gemm | ok | True | `nvjet_sm100_tst_64x8_64x16_4x1_v_bz_splitK_TNT` | nearest_preceding_shape_cpu_op: `aten::copy_` {"Concrete Inputs": ["", "", "False"], "Input Dims": [[1, 1], [1, 1], []], "Input Strides": [[4096, 1], [1, 1], []], "Input type": ["int", "int", "Scalar"]} |
| 5.20 | 200 | quant_gemm | ok | True | `nvjet_sm100_tst_64x8_64x16_4x1_v_bz_TNT` | timestamp_enclosure: `aten::sub` {"Concrete Inputs": ["", "", "1"], "Input Dims": [[1], [], []], "Input Strides": [[1], [], []], "Input type": ["long int", "long int", "Scalar"]} |
| 4.90 | 9 | quant_gemm | ok | True | `nvjet_sm100_tst_256x8_64x6_2x1_v_bz_TNT` | nearest_preceding_shape_cpu_op: `aten::copy_` {"Concrete Inputs": ["", "", "True"], "Input Dims": [[1], [1], []], "Input Strides": [[1], [1], []], "Input type": ["long int", "long int", "Scalar"]} |
| 4.14 | 200 | attention | ok | True | `fmhaSm100fKernel_QkvBfloat16OBfloat16H256PagedKvSlidingOrChunkedCausalP64MultiCtasKvCgaVarSeqQ8Kv128StaticSwapsAbForGen` | nearest_preceding_shape_cpu_op: `aten::as_strided` {"Concrete Inputs": ["", "[1, 262144]", "[262144, 1]", "0"], "Input Dims": [[1, 262144], [], [], []], "Input Strides": [[262144, 1], [], [], []], "Input type": ["float", "Scalar... |
| 2.58 | 240 | quant_gemm | ok | True | `nvjet_sm100_tst_32x64_64x16_4x1_v_bz_splitK_TNN` | timestamp_enclosure: `aten::copy_` {"Concrete Inputs": ["", "", "False"], "Input Dims": [[1], [1], []], "Input Strides": [[1], [1], []], "Input type": ["int", "int", "Scalar"]} |
| 2.22 | 270 | gemm | ok | True | `kernel_cutlass_kernel_flashinfernormkernelsfused_add_rmsnormFusedAddRMSNormKernel_object_at__tensorptrbf16gmemalign128o281628161_tensorptrbf16gmemalign128o281628161_tensorptrbf16gmemalign_0` | nearest_preceding_shape_cpu_op: `aten::empty_strided` {"Concrete Inputs": ["[17, 2816]", "[2816, 1]", "15", "0", "", "False"], "Input Dims": [[], [], [], [], [], []], "Input Strides": [[], [], [], [], [], []], "Input type": ["Scala... |
| 2.14 | 270 | gemm | ok | True | `_gemma_dual_rmsnorm_residual_kernel` | timestamp_enclosure: `aten::index` {"Concrete Inputs": ["", ""], "Input Dims": [[2049, 262148], []], "Input Strides": [[262148, 1], []], "Input type": ["int", ""]} |

The CSV/JSON siblings contain full sample metadata and trace paths.
