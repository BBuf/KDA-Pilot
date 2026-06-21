# Kernel Shape Inventory — sharegpt_high

- Model: `zai-org/GLM-4.7-Flash`
- Dataset: `sharegpt`
- Concurrency: `high`
- Threshold: GPU kernel name share `> 2.0%`
- Total GPU kernel time: `228.8 ms`
- Trace files: `1`

| % GPU | Calls | Category | Shape | SGLang relevant | Kernel | Shape provenance |
|---:|---:|---|---|---|---|---|
| 29.47 | 828 | moe | ok | True | `fused_moe_kernel` | nearest_preceding_shape_cpu_op: `aten::empty_strided` {"Concrete Inputs": ["[96]", "[1]", "4", "0", "", "False"], "Input Dims": [[], [], [], [], [], []], "Input Strides": [[], [], [], [], [], []], "Input type": ["ScalarList", "Scal... |
| 26.43 | 235 | other | ok | True | `_fwd_kernel` | external_id=69661: `sglang::unified_attention_with_output` {"Concrete Inputs": ["", "", "", "", "True", "16", "", "", "", "", "", "", ""], "Input Dims": [[80, 20, 576], [80, 1, 576], [80, 1, 512], [80, 10240], [], [], [], [], [], [], []... |

The CSV/JSON siblings contain full sample metadata and trace paths.
