# Kernel Shape Inventory — sharegpt_mid

- Model: `google/gemma-4-26B-A4B-it`
- Dataset: `sharegpt`
- Concurrency: `mid`
- Threshold: GPU kernel name share `> 2.0%`
- Total GPU kernel time: `128.1 ms`
- Trace files: `1`

| % GPU | Calls | Category | Shape | SGLang relevant | Kernel | Shape provenance |
|---:|---:|---|---|---|---|---|
| 43.37 | 540 | moe | ok | True | `fused_moe_kernel` | external_id=44189: `sglang::inplace_fused_experts` {"Concrete Inputs": ["", "", "", "", "", "", "", "", "True", "False", "False", "False", "False", "False", "False", "", "", "", "", "", "", "", "", "", "", "False", ""], "Input D... |
| 7.54 | 85 | quant_gemm | ok | True | `nvjet_sm100_tst_128x192_64x7_2x1_2cta_v_bz_TNT` | external_id=44356: `aten::mm` {"Concrete Inputs": ["", ""], "Input Dims": [[7081, 8192], [8192, 2816]], "Input Strides": [[8192, 1], [1, 8192]], "Input type": ["c10::BFloat16", "c10::BFloat16"]} |
| 5.39 | 270 | gemm | ok | True | `_gemma_qkv_rmsnorm_kernel` | timestamp_enclosure: `aten::nonzero` {"Concrete Inputs": [""], "Input Dims": [[384]], "Input Strides": [[1]], "Input type": ["bool"]} |
| 4.36 | 1089 | gemm | ok | True | `kernel_cutlass_kernel_flashinfernormkernelsrmsnormRMSNormKernel_object_at__tensorptrbf16gmemalign128o281628161_tensorptrbf16gmemalign16o28161_tensorptrbf16gmemalign128o281628161___True_4__0` | timestamp_enclosure: `aten::nonzero` {"Concrete Inputs": [""], "Input Dims": [[384]], "Input Strides": [[1]], "Input type": ["bool"]} |
| 3.20 | 75 | attention | ok | True | `fmhaSm100fKernel_QkvBfloat16OBfloat16H256PagedKvSlidingOrChunkedCausalP64VarSeqQ128Kv128PersistentContext` | timestamp_enclosure: `aten::nonzero` {"Concrete Inputs": [""], "Input Dims": [[384]], "Input Strides": [[1]], "Input type": ["bool"]} |
| 3.12 | 150 | attention | ok | True | `fmhaSm100fKernel_QkvBfloat16OBfloat16H256PagedKvSlidingOrChunkedCausalP64VarSeqQ8Kv128PersistentSwapsAbForGen` | nearest_preceding_shape_cpu_op: `aten::as_strided` {"Concrete Inputs": ["", "[32, 262144]", "[262144, 1]", "0"], "Input Dims": [[32, 262144], [], [], []], "Input Strides": [[262144, 1], [], [], []], "Input type": ["float", "Scal... |
| 2.45 | 30 | quant_gemm | ok | True | `nvjet_sm100_tst_128x256_64x6_2x1_2cta_v_bz_TNT` | external_id=44264: `aten::mm` {"Concrete Inputs": ["", ""], "Input Dims": [[7081, 2816], [2816, 4224]], "Input Strides": [[2816, 1], [1, 2816]], "Input type": ["c10::BFloat16", "c10::BFloat16"]} |
| 2.42 | 360 | quant_gemm | ok | True | `nvjet_sm100_tst_32x64_64x16_4x1_v_bz_TNN` | nearest_preceding_shape_cpu_op: `aten::as_strided` {"Concrete Inputs": ["", "[32, 262144]", "[262144, 1]", "0"], "Input Dims": [[32, 262144], [], [], []], "Input Strides": [[262144, 1], [], [], []], "Input type": ["float", "Scal... |

The CSV/JSON siblings contain full sample metadata and trace paths.
