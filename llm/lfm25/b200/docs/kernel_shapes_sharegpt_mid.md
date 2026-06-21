# Kernel Shape Inventory — sharegpt_mid

- Model: `LiquidAI/LFM2.5-8B-A1B`
- Dataset: `sharegpt`
- Concurrency: `mid`
- Threshold: GPU kernel name share `> 2.0%`
- Total GPU kernel time: `87.8 ms`
- Trace files: `1`

| % GPU | Calls | Category | Shape | SGLang relevant | Kernel | Shape provenance |
|---:|---:|---|---|---|---|---|
| 47.66 | 396 | moe | ok | True | `fused_moe_kernel` | external_id=54246: `sglang::inplace_fused_experts` {"Concrete Inputs": ["", "", "", "", "", "", "", "", "True", "False", "False", "False", "False", "False", "False", "", "", "", "", "", "", "", "", "", "", "False", ""], "Input D... |
| 5.65 | 52 | quant_gemm | ok | True | `nvjet_sm100_tst_128x256_64x6_2x1_2cta_v_bz_TNT` | external_id=52304: `aten::mm` {"Concrete Inputs": ["", ""], "Input Dims": [[7193, 2048], [2048, 14336]], "Input Strides": [[2048, 1], [1, 2048]], "Input type": ["c10::BFloat16", "c10::BFloat16"]} |
| 3.51 | 216 | other | ok | True | `void (anonymous namespace)::act_and_mul_kernel<__nv_bfloat16, ((anonymous namespace)::ActivationKind)0, true, false>((anonymous namespace)::ActivationParams)` | external_id=52492: `sglang::_run_activation_inplace` {"Concrete Inputs": ["", "", ""], "Input Dims": [[], [28772, 3584], [28772, 1792]], "Input Strides": [[], [3584, 1], [1792, 1]], "Input type": ["", "c10::BFloat16", "c10::BFloat... |
| 2.52 | 18 | attention | ok | True | `void flashinfer::BatchPrefillWithRaggedKVCacheKernel<flashinfer::KernelTraits<(flashinfer::MaskMode)1, 128u, 2u, 4u, 4u, 4u, 4u, 1u, (flashinfer::PosEncodingMode)0, __nv_bfloat16, __nv_bfloat16, __nv_bfloat16, float, int, flashinfer::DefaultAttention<false, false, false, false> >, RaggedParams>(RaggedParams)` | nearest_preceding_shape_cpu_op: `aten::fill_` {"Concrete Inputs": ["", "0"], "Input Dims": [[5857, 32, 64], []], "Input Strides": [[2048, 64, 1], []], "Input type": ["c10::BFloat16", "Scalar"]} |
| 2.11 | 441 | gemm | ok | True | `kernel_cutlass_kernel_flashinfernormkernelsrmsnormRMSNormKernel_object_at__tensorptrbf16gmemalign128o204820481_tensorptrbf16gmemalign16o20481_tensorptrbf16gmemalign128o204820481___True_4__0` | nearest_preceding_shape_cpu_op: `aten::view` {"Concrete Inputs": ["", "[7193, 8, 64]"], "Input Dims": [[57544, 64], []], "Input Strides": [[64, 1], []], "Input type": ["c10::BFloat16", "ScalarList"]} |

The CSV/JSON siblings contain full sample metadata and trace paths.
