# Kernel Shape Inventory — random_mid

- Model: `zai-org/GLM-4.7-Flash`
- Dataset: `random`
- Concurrency: `mid`
- Threshold: GPU kernel name share `> 2.0%`
- Total GPU kernel time: `463.1 ms`
- Trace files: `1`

| % GPU | Calls | Category | Shape | SGLang relevant | Kernel | Shape provenance |
|---:|---:|---|---|---|---|---|
| 41.11 | 188 | other | ok | True | `_fwd_kernel` | nearest_preceding_shape_cpu_op: `aten::as_strided` {"Concrete Inputs": ["", "[1873326, 1, 512]", "[576, 576, 1]", "0"], "Input Dims": [[1873326, 1, 576], [], [], []], "Input Strides": [[576, 576, 1], [], [], []], "Input type": [... |
| 30.39 | 828 | moe | ok | True | `fused_moe_kernel` | external_id=16135: `sglang::inplace_fused_experts` {"Concrete Inputs": ["", "", "", "", "", "", "", "", "True", "False", "False", "False", "False", "False", "False", "", "", "", "", "", "", "", "1.8", "", "", "False", ""], "Inpu... |

The CSV/JSON siblings contain full sample metadata and trace paths.
