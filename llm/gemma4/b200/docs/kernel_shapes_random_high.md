# Kernel Shape Inventory — random_high

- Model: `google/gemma-4-26B-A4B-it`
- Dataset: `random`
- Concurrency: `high`
- Threshold: GPU kernel name share `> 2.0%`
- Total GPU kernel time: `121.3 ms`
- Trace files: `1`

| % GPU | Calls | Category | Shape | SGLang relevant | Kernel | Shape provenance |
|---:|---:|---|---|---|---|---|
| 50.81 | 540 | moe | ok | True | `fused_moe_kernel` | external_id=23889: `sglang::inplace_fused_experts` {"Concrete Inputs": ["", "", "", "", "", "", "", "", "True", "False", "False", "False", "False", "False", "False", "", "", "", "", "", "", "", "", "", "", "False", ""], "Input D... |
| 9.24 | 150 | attention | ok | True | `fmhaSm100fKernel_QkvBfloat16OBfloat16H256PagedKvSlidingOrChunkedCausalP64VarSeqQ8Kv128PersistentSwapsAbForGen` | nearest_preceding_shape_cpu_op: `aten::resolve_neg` {"Concrete Inputs": [""], "Input Dims": [[100]], "Input Strides": [[1]], "Input type": ["long int"]} |
| 3.58 | 270 | gemm | ok | True | `_gemma_qkv_rmsnorm_kernel` | nearest_preceding_shape_cpu_op: `aten::as_strided` {"Concrete Inputs": ["", "[8071, 8, 64, 256]", "[131072, 256, 2048, 1]", ""], "Input Dims": [[8071, 64, 8, 256], [], [], []], "Input Strides": [[131072, 2048, 256, 1], [], [], [... |
| 3.45 | 1089 | gemm | ok | True | `kernel_cutlass_kernel_flashinfernormkernelsrmsnormRMSNormKernel_object_at__tensorptrbf16gmemalign128o281628161_tensorptrbf16gmemalign16o28161_tensorptrbf16gmemalign128o281628161___True_4__0` | nearest_preceding_shape_cpu_op: `aten::empty_strided` {"Concrete Inputs": ["[1902, 2816]", "[2816, 1]", "15", "0", "", "False"], "Input Dims": [[], [], [], [], [], []], "Input Strides": [[], [], [], [], [], []], "Input type": ["Sca... |
| 2.80 | 75 | attention | ok | True | `fmhaSm100fKernel_QkvBfloat16OBfloat16H256PagedKvSlidingOrChunkedCausalP64VarSeqQ128Kv128PersistentContext` | nearest_preceding_shape_cpu_op: `aten::empty_strided` {"Concrete Inputs": ["[1902, 16, 256]", "[4096, 256, 1]", "15", "0", "", "False"], "Input Dims": [[], [], [], [], [], []], "Input Strides": [[], [], [], [], [], []], "Input type... |
| 2.17 | 330 | quant_gemm | ok | True | `nvjet_sm100_tst_64x64_64x16_2x2_2cta_h_bz_TNT` | nearest_preceding_shape_cpu_op: `aten::copy_` {"Concrete Inputs": ["", "", "True"], "Input Dims": [[100], [100], []], "Input Strides": [[1], [1], []], "Input type": ["long int", "long int", "Scalar"]} |

The CSV/JSON siblings contain full sample metadata and trace paths.
