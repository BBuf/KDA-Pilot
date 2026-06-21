# Kernel Shape Inventory — sharegpt_high

- Model: `google/gemma-4-26B-A4B-it`
- Dataset: `sharegpt`
- Concurrency: `high`
- Threshold: GPU kernel name share `> 2.0%`
- Total GPU kernel time: `110.9 ms`
- Trace files: `1`

| % GPU | Calls | Category | Shape | SGLang relevant | Kernel | Shape provenance |
|---:|---:|---|---|---|---|---|
| 50.02 | 540 | moe | ok | True | `fused_moe_kernel` | external_id=62016: `sglang::inplace_fused_experts` {"Concrete Inputs": ["", "", "", "", "", "", "", "", "True", "False", "False", "False", "False", "False", "False", "", "", "", "", "", "", "", "", "", "", "False", ""], "Input D... |
| 4.86 | 100 | attention | ok | True | `fmhaSm100fKernel_QkvBfloat16OBfloat16H256PagedKvSlidingOrChunkedCausalP64VarSeqQ8Kv128PersistentSwapsAbForGen` | nearest_preceding_shape_cpu_op: `aten::as_strided` {"Concrete Inputs": ["", "[100, 262144]", "[262144, 1]", "0"], "Input Dims": [[104, 262144], [], [], []], "Input Strides": [[262144, 1], [], [], []], "Input type": ["float", "Sc... |
| 3.90 | 270 | gemm | ok | True | `_gemma_qkv_rmsnorm_kernel` | timestamp_enclosure: `sglang::apply_rope_inplace` {"Concrete Inputs": ["", "", "", "", "True", "0"], "Input Dims": [[1785, 16, 256], [1785, 8, 256], [262400, 256], [1785], [], []], "Input Strides": [[8192, 256, 1], [8192, 256, ... |
| 3.56 | 1089 | gemm | ok | True | `kernel_cutlass_kernel_flashinfernormkernelsrmsnormRMSNormKernel_object_at__tensorptrbf16gmemalign128o281628161_tensorptrbf16gmemalign16o28161_tensorptrbf16gmemalign128o281628161___True_4__0` | nearest_preceding_shape_cpu_op: `aten::empty_strided` {"Concrete Inputs": ["[1785, 2816]", "[2816, 1]", "15", "0", "", "False"], "Input Dims": [[], [], [], [], [], []], "Input Strides": [[], [], [], [], [], []], "Input type": ["Sca... |
| 3.07 | 125 | attention | ok | True | `fmhaSm100fKernel_QkvBfloat16OBfloat16H256PagedKvSlidingOrChunkedCausalP64VarSeqQ128Kv128PersistentContext` | nearest_preceding_shape_cpu_op: `aten::empty_strided` {"Concrete Inputs": ["[1785, 16, 256]", "[4096, 256, 1]", "15", "0", "", "False"], "Input Dims": [[], [], [], [], [], []], "Input Strides": [[], [], [], [], [], []], "Input type... |

The CSV/JSON siblings contain full sample metadata and trace paths.
