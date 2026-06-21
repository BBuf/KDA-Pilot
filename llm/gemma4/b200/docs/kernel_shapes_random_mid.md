# Kernel Shape Inventory — random_mid

- Model: `google/gemma-4-26B-A4B-it`
- Dataset: `random`
- Concurrency: `mid`
- Threshold: GPU kernel name share `> 2.0%`
- Total GPU kernel time: `166.5 ms`
- Trace files: `1`

| % GPU | Calls | Category | Shape | SGLang relevant | Kernel | Shape provenance |
|---:|---:|---|---|---|---|---|
| 45.23 | 540 | moe | ok | True | `fused_moe_kernel` | external_id=11287: `sglang::inplace_fused_experts` {"Concrete Inputs": ["", "", "", "", "", "", "", "", "True", "False", "False", "False", "False", "False", "False", "", "", "", "", "", "", "", "", "", "", "False", ""], "Input D... |
| 6.05 | 65 | quant_gemm | ok | True | `nvjet_sm100_tst_128x256_64x6_2x1_2cta_v_bz_TNT` | external_id=11313: `aten::mm` {"Concrete Inputs": ["", ""], "Input Dims": [[11254, 2816], [2816, 10240]], "Input Strides": [[2816, 1], [1, 2816]], "Input type": ["c10::BFloat16", "c10::BFloat16"]} |
| 5.50 | 270 | gemm | ok | True | `_gemma_qkv_rmsnorm_kernel` | nearest_preceding_shape_cpu_op: `aten::empty` {"Concrete Inputs": ["[32]", "4", "", "", "False", ""], "Input Dims": [[], [], [], [], [], []], "Input Strides": [[], [], [], [], [], []], "Input type": ["ScalarList", "Scalar",... |
| 4.67 | 25 | quant_gemm | ok | True | `nvjet_sm100_tst_128x192_64x7_2x1_2cta_v_bz_TNT` | external_id=11413: `aten::mm` {"Concrete Inputs": ["", ""], "Input Dims": [[11254, 2816], [2816, 8192]], "Input Strides": [[2816, 1], [1, 2816]], "Input type": ["c10::BFloat16", "c10::BFloat16"]} |
| 4.04 | 1089 | gemm | ok | True | `kernel_cutlass_kernel_flashinfernormkernelsrmsnormRMSNormKernel_object_at__tensorptrbf16gmemalign128o281628161_tensorptrbf16gmemalign16o28161_tensorptrbf16gmemalign128o281628161___True_4__0` | nearest_preceding_shape_cpu_op: `aten::empty` {"Concrete Inputs": ["[32]", "4", "", "", "False", ""], "Input Dims": [[], [], [], [], [], []], "Input Strides": [[], [], [], [], [], []], "Input type": ["ScalarList", "Scalar",... |
| 3.54 | 175 | attention | ok | True | `fmhaSm100fKernel_QkvBfloat16OBfloat16H256PagedKvSlidingOrChunkedCausalP64VarSeqQ8Kv128PersistentSwapsAbForGen` | nearest_preceding_shape_cpu_op: `aten::resolve_neg` {"Concrete Inputs": [""], "Input Dims": [[32]], "Input Strides": [[1]], "Input type": ["long int"]} |
| 3.21 | 30 | quant_gemm | ok | True | `nvjet_sm100_tst_128x256_64x4_1x2_h_bz_TNT` | external_id=11562: `aten::mm` {"Concrete Inputs": ["", ""], "Input Dims": [[11254, 2816], [2816, 4224]], "Input Strides": [[2816, 1], [1, 2816]], "Input type": ["c10::BFloat16", "c10::BFloat16"]} |
| 2.16 | 270 | other | ok | True | `void (anonymous namespace)::act_and_mul_kernel<__nv_bfloat16, ((anonymous namespace)::ActivationKind)1, true, false>((anonymous namespace)::ActivationParams)` | external_id=11396: `sglang::_run_activation_inplace` {"Concrete Inputs": ["", "", ""], "Input Dims": [[], [90032, 1408], [90032, 704]], "Input Strides": [[], [1408, 1], [704, 1]], "Input type": ["", "c10::BFloat16", "c10::BFloat16"]} |
| 2.15 | 50 | attention | ok | True | `fmhaSm100fKernel_QkvBfloat16OBfloat16H256PagedKvSlidingOrChunkedCausalP64VarSeqQ128Kv128PersistentContext` | nearest_preceding_shape_cpu_op: `aten::empty` {"Concrete Inputs": ["[32]", "4", "", "", "False", ""], "Input Dims": [[], [], [], [], [], []], "Input Strides": [[], [], [], [], [], []], "Input type": ["ScalarList", "Scalar",... |
| 2.05 | 385 | quant_gemm | ok | True | `nvjet_sm100_tst_32x64_64x16_4x1_v_bz_TNN` | nearest_preceding_shape_cpu_op: `aten::copy_` {"Concrete Inputs": ["", "", "False"], "Input Dims": [[32, 16], [32, 16], []], "Input Strides": [[4096, 1], [16, 1], []], "Input type": ["int", "int", "Scalar"]} |

The CSV/JSON siblings contain full sample metadata and trace paths.
