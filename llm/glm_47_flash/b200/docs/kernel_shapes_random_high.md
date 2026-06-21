# Kernel Shape Inventory — random_high

- Model: `zai-org/GLM-4.7-Flash`
- Dataset: `random`
- Concurrency: `high`
- Threshold: GPU kernel name share `> 2.0%`
- Total GPU kernel time: `181.7 ms`
- Trace files: `1`

| % GPU | Calls | Category | Shape | SGLang relevant | Kernel | Shape provenance |
|---:|---:|---|---|---|---|---|
| 35.25 | 423 | other | ok | True | `_fwd_kernel` | external_id=35285: `sglang::unified_attention_with_output` {"Concrete Inputs": ["", "", "", "", "True", "5", "", "", "", "", "", "", ""], "Input Dims": [[24, 20, 576], [24, 1, 576], [24, 1, 512], [24, 10240], [], [], [], [], [], [], [],... |
| 27.34 | 828 | moe | missing | True | `fused_moe_kernel` | external_id=35145: `Torch-Compiled Region: 5/0` {} |

The CSV/JSON siblings contain full sample metadata and trace paths.
