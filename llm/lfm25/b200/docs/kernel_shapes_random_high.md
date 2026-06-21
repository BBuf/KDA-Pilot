# Kernel Shape Inventory — random_high

- Model: `LiquidAI/LFM2.5-8B-A1B`
- Dataset: `random`
- Concurrency: `high`
- Threshold: GPU kernel name share `> 2.0%`
- Total GPU kernel time: `211.0 ms`
- Trace files: `1`

| % GPU | Calls | Category | Shape | SGLang relevant | Kernel | Shape provenance |
|---:|---:|---|---|---|---|---|
| 45.03 | 396 | moe | ok | True | `fused_moe_kernel` | external_id=32201: `sglang::inplace_fused_experts` {"Concrete Inputs": ["", "", "", "", "", "", "", "", "True", "False", "False", "False", "False", "False", "False", "", "", "", "", "", "", "", "", "", "", "False", ""], "Input D... |
| 11.24 | 200 | quant_gemm | ok | True | `nvjet_sm100_tst_128x256_64x6_2x1_2cta_v_bz_TNT` | external_id=30085: `aten::mm` {"Concrete Inputs": ["", ""], "Input Dims": [[16384, 2048], [2048, 14336]], "Input Strides": [[2048, 1], [1, 2048]], "Input type": ["c10::BFloat16", "c10::BFloat16"]} |
| 4.35 | 216 | other | ok | True | `void (anonymous namespace)::act_and_mul_kernel<__nv_bfloat16, ((anonymous namespace)::ActivationKind)0, true, false>((anonymous namespace)::ActivationParams)` | external_id=30273: `sglang::_run_activation_inplace` {"Concrete Inputs": ["", "", ""], "Input Dims": [[], [65536, 3584], [65536, 1792]], "Input Strides": [[], [3584, 1], [1792, 1]], "Input type": ["", "c10::BFloat16", "c10::BFloat... |

The CSV/JSON siblings contain full sample metadata and trace paths.
