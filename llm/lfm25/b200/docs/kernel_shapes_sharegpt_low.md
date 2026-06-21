# Kernel Shape Inventory — sharegpt_low

- Model: `LiquidAI/LFM2.5-8B-A1B`
- Dataset: `sharegpt`
- Concurrency: `low`
- Threshold: GPU kernel name share `> 2.0%`
- Total GPU kernel time: `22.0 ms`
- Trace files: `1`

| % GPU | Calls | Category | Shape | SGLang relevant | Kernel | Shape provenance |
|---:|---:|---|---|---|---|---|
| 34.12 | 396 | moe | ok | True | `fused_moe_kernel` | external_id=43183: `sglang::inplace_fused_experts` {"Concrete Inputs": ["", "", "", "", "", "", "", "", "True", "False", "False", "False", "False", "False", "False", "", "", "", "", "", "", "", "", "", "", "False", ""], "Input D... |
| 7.00 | 192 | quant_gemm | ok | True | `nvjet_sm100_tst_16x64_64x16_4x1_v_bz_TNN` | timestamp_enclosure: `aten::slice` {"Concrete Inputs": ["", "0", "0", "1", "1"], "Input Dims": [[512], [], [], [], []], "Input Strides": [[1], [], [], [], []], "Input type": ["long int", "Scalar", "Scalar", "Scal... |
| 4.85 | 441 | gemm | ok | True | `kernel_cutlass_kernel_flashinfernormkernelsrmsnormRMSNormKernel_object_at__tensorptrbf16gmemalign128o204820481_tensorptrbf16gmemalign16o20481_tensorptrbf16gmemalign128o204820481___True_4__0` | nearest_preceding_shape_cpu_op: `aten::empty_strided` {"Concrete Inputs": ["[624, 2048]", "[2048, 1]", "15", "0", "", "False"], "Input Dims": [[], [], [], [], [], []], "Input Strides": [[], [], [], [], [], []], "Input type": ["Scal... |
| 4.35 | 144 | quant_gemm | ok | True | `nvjet_sm100_tst_64x8_64x16_4x1_v_bz_TNT` | nearest_preceding_shape_cpu_op: `aten::cat` {"Concrete Inputs": ["", "0"], "Input Dims": [[[465363], [1]], []], "Input Strides": [[[1], [1]], []], "Input type": ["TensorList", "Scalar"]} |
| 3.89 | 176 | moe | ok | True | `void moe_align_block_size_small_batch_expert_kernel<int, 256>(int const*, int*, int*, int*, int, int, unsigned long, bool, int)` | nearest_preceding_shape_cpu_op: `aten::as_strided` {"Concrete Inputs": ["", "[726]", "[1]", "1"], "Input Dims": [[727], [], [], []], "Input Strides": [[1], [], [], []], "Input type": ["long int", "ScalarList", "ScalarList", "Sca... |
| 3.25 | 9 | quant_gemm | ok | True | `nvjet_sm100_tst_128x8_64x12_2x1_v_bz_TNT` | external_id=45203: `aten::mm` {"Concrete Inputs": ["", ""], "Input Dims": [[1, 2048], [2048, 128000]], "Input Strides": [[2048, 1], [1, 2048]], "Input type": ["c10::BFloat16", "c10::BFloat16"]} |
| 3.16 | 216 | other | ok | True | `void (anonymous namespace)::act_and_mul_kernel<__nv_bfloat16, ((anonymous namespace)::ActivationKind)0, true, false>((anonymous namespace)::ActivationParams)` | external_id=43192: `sglang::_run_activation_inplace` {"Concrete Inputs": ["", "", ""], "Input Dims": [[], [2496, 3584], [2496, 1792]], "Input Strides": [[], [3584, 1], [1792, 1]], "Input type": ["", "c10::BFloat16", "c10::BFloat16"]} |
| 2.91 | 176 | quant_gemm | ok | True | `nvjet_sm100_tst_64x8_64x16_1x1_h_bz_splitK_TNT` | nearest_preceding_shape_cpu_op: `aten::to` {"Concrete Inputs": ["", "4", "False", "False", ""], "Input Dims": [[1], [], [], [], []], "Input Strides": [[1], [], [], [], []], "Input type": ["long int", "Scalar", "Scalar", ... |
| 2.01 | 48 | attention | ok | True | `void flashinfer::BatchPrefillWithPagedKVCacheKernel<flashinfer::KernelTraits<(flashinfer::MaskMode)0, 16u, 1u, 4u, 4u, 4u, 1u, 4u, (flashinfer::PosEncodingMode)0, __nv_bfloat16, __nv_bfloat16, __nv_bfloat16, float, int, flashinfer::DefaultAttention<false, false, false, false> >, PagedParams>(PagedParams)` | nearest_preceding_shape_cpu_op: `aten::add` {"Concrete Inputs": ["", "", "1"], "Input Dims": [[1], [1], []], "Input Strides": [[1], [1], []], "Input type": ["int", "int", "Scalar"]} |

The CSV/JSON siblings contain full sample metadata and trace paths.
