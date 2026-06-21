# Kernel Shape Inventory — sharegpt_mid

- Model: `zai-org/GLM-4.7-Flash`
- Dataset: `sharegpt`
- Concurrency: `mid`
- Threshold: GPU kernel name share `> 2.0%`
- Total GPU kernel time: `1036.2 ms`
- Trace files: `1`

| % GPU | Calls | Category | Shape | SGLang relevant | Kernel | Shape provenance |
|---:|---:|---|---|---|---|---|
| 75.35 | 188 | other | ok | True | `_fwd_kernel` | nearest_preceding_shape_cpu_op: `aten::copy_` {"Concrete Inputs": ["", "", "True"], "Input Dims": [[32], [32], []], "Input Strides": [[1], [1], []], "Input type": ["long int", "long int", "Scalar"]} |
| 12.17 | 828 | moe | ok | True | `fused_moe_kernel` | external_id=55392: `sglang::inplace_fused_experts` {"Concrete Inputs": ["", "", "", "", "", "", "", "", "True", "False", "False", "False", "False", "False", "False", "", "", "", "", "", "", "", "1.8", "", "", "False", ""], "Inpu... |

The CSV/JSON siblings contain full sample metadata and trace paths.
