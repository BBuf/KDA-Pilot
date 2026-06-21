# Kernel Shape Inventory — sharegpt_high

- Model: `LiquidAI/LFM2.5-8B-A1B`
- Dataset: `sharegpt`
- Concurrency: `high`
- Threshold: GPU kernel name share `> 2.0%`
- Total GPU kernel time: `164.0 ms`
- Trace files: `1`

| % GPU | Calls | Category | Shape | SGLang relevant | Kernel | Shape provenance |
|---:|---:|---|---|---|---|---|
| 42.22 | 396 | moe | ok | True | `fused_moe_kernel` | external_id=73867: `sglang::inplace_fused_experts` {"Concrete Inputs": ["", "", "", "", "", "", "", "", "True", "False", "False", "False", "False", "False", "False", "", "", "", "", "", "", "", "", "", "", "False", ""], "Input D... |
| 6.59 | 78 | quant_gemm | ok | True | `nvjet_sm100_tst_128x256_64x6_2x1_2cta_v_bz_TNT` | external_id=71751: `aten::mm` {"Concrete Inputs": ["", ""], "Input Dims": [[16384, 2048], [2048, 14336]], "Input Strides": [[2048, 1], [1, 2048]], "Input type": ["c10::BFloat16", "c10::BFloat16"]} |
| 3.73 | 216 | other | ok | True | `void (anonymous namespace)::act_and_mul_kernel<__nv_bfloat16, ((anonymous namespace)::ActivationKind)0, true, false>((anonymous namespace)::ActivationParams)` | external_id=71939: `sglang::_run_activation_inplace` {"Concrete Inputs": ["", "", ""], "Input Dims": [[], [65536, 3584], [65536, 1792]], "Input Strides": [[], [3584, 1], [1792, 1]], "Input type": ["", "c10::BFloat16", "c10::BFloat... |
| 2.23 | 24 | attention | ok | True | `void flashinfer::BatchPrefillWithRaggedKVCacheKernel<flashinfer::KernelTraits<(flashinfer::MaskMode)1, 128u, 2u, 4u, 4u, 4u, 4u, 1u, (flashinfer::PosEncodingMode)0, __nv_bfloat16, __nv_bfloat16, __nv_bfloat16, float, int, flashinfer::DefaultAttention<false, false, false, false> >, RaggedParams>(RaggedParams)` | nearest_preceding_shape_cpu_op: `aten::copy_` {"Concrete Inputs": ["", "", "False"], "Input Dims": [[2048, 16384], [2048, 16384], []], "Input Strides": [[16384, 1], [1, 2048], []], "Input type": ["c10::BFloat16", "c10::BFlo... |
| 2.15 | 48 | quant_gemm | ok | True | `nvjet_sm100_tst_256x128_64x5_2x1_2cta_v_bz_TNT` | external_id=77936: `aten::mm` {"Concrete Inputs": ["", ""], "Input Dims": [[5930, 2048], [2048, 14336]], "Input Strides": [[2048, 1], [1, 2048]], "Input type": ["c10::BFloat16", "c10::BFloat16"]} |

The CSV/JSON siblings contain full sample metadata and trace paths.
