# Kernel Shape Inventory — random_low

- Model: `LiquidAI/LFM2.5-8B-A1B`
- Dataset: `random`
- Concurrency: `low`
- Threshold: GPU kernel name share `> 2.0%`
- Total GPU kernel time: `20.2 ms`
- Trace files: `1`

| % GPU | Calls | Category | Shape | SGLang relevant | Kernel | Shape provenance |
|---:|---:|---|---|---|---|---|
| 32.96 | 396 | moe | ok | True | `fused_moe_kernel` | external_id=743: `sglang::inplace_fused_experts` {"Concrete Inputs": ["", "", "", "", "", "", "", "", "True", "False", "False", "False", "False", "False", "False", "", "", "", "", "", "", "", "", "", "", "False", ""], "Input D... |
| 7.61 | 192 | quant_gemm | ok | True | `nvjet_sm100_tst_16x64_64x16_4x1_v_bz_TNN` | nearest_preceding_shape_cpu_op: `aten::as_strided` {"Concrete Inputs": ["", "[1]", "[1]", "102"], "Input Dims": [[102], [], [], []], "Input Strides": [[1], [], [], []], "Input type": ["long int", "ScalarList", "ScalarList", "Sca... |
| 5.17 | 441 | gemm | ok | True | `kernel_cutlass_kernel_flashinfernormkernelsrmsnormRMSNormKernel_object_at__tensorptrbf16gmemalign128o204820481_tensorptrbf16gmemalign16o20481_tensorptrbf16gmemalign128o204820481___True_4__0` | timestamp_enclosure: `aten::_index_put_impl_` {"Concrete Inputs": ["", "", "", "False", "False"], "Input Dims": [[18, 466682, 2048, 2], [], [18, 1, 2048, 2], [], []], "Input Strides": [[1911529472, 4096, 2, 1], [], [4096, 4... |
| 5.09 | 198 | moe | ok | True | `void moe_align_block_size_small_batch_expert_kernel<int, 256>(int const*, int*, int*, int*, int, int, unsigned long, bool, int)` | external_id=1200: `sgl_kernel::moe_align_block_size` {"Concrete Inputs": ["", "33", "16", "", "", "", "", "True"], "Input Dims": [[103, 4], [], [], [907], [57], [1], [34], []], "Input Strides": [[4, 1], [], [], [1], [1], [1], [1],... |
| 4.74 | 144 | quant_gemm | ok | True | `nvjet_sm100_tst_64x8_64x16_4x1_v_bz_TNT` | nearest_preceding_shape_cpu_op: `aten::cat` {"Concrete Inputs": ["", "0"], "Input Dims": [[[466674], [1]], []], "Input Strides": [[[1], [1]], []], "Input type": ["TensorList", "Scalar"]} |
| 3.51 | 9 | quant_gemm | ok | True | `nvjet_sm100_tst_128x8_64x12_2x1_v_bz_TNT` | nearest_preceding_shape_cpu_op: `aten::copy_` {"Concrete Inputs": ["", "", "False"], "Input Dims": [[2], [2], []], "Input Strides": [[1], [1], []], "Input type": ["int", "int", "Scalar"]} |
| 3.16 | 176 | quant_gemm | ok | True | `nvjet_sm100_tst_64x8_64x16_1x1_h_bz_splitK_TNT` | timestamp_enclosure: `aten::cat` {"Concrete Inputs": ["", "0"], "Input Dims": [[[6222173], [101]], []], "Input Strides": [[[1], [1]], []], "Input type": ["TensorList", "Scalar"]} |
| 2.94 | 216 | other | ok | True | `void (anonymous namespace)::act_and_mul_kernel<__nv_bfloat16, ((anonymous namespace)::ActivationKind)0, true, false>((anonymous namespace)::ActivationParams)` | external_id=662: `sglang::_run_activation_inplace` {"Concrete Inputs": ["", "", ""], "Input Dims": [[], [412, 3584], [412, 1792]], "Input Strides": [[], [3584, 1], [1792, 1]], "Input type": ["", "c10::BFloat16", "c10::BFloat16"]} |
| 2.03 | 48 | attention | ok | True | `void flashinfer::BatchPrefillWithPagedKVCacheKernel<flashinfer::KernelTraits<(flashinfer::MaskMode)0, 16u, 1u, 4u, 4u, 4u, 1u, 4u, (flashinfer::PosEncodingMode)0, __nv_bfloat16, __nv_bfloat16, __nv_bfloat16, float, int, flashinfer::DefaultAttention<false, false, false, false> >, PagedParams>(PagedParams)` | timestamp_enclosure: `aten::ne` {"Concrete Inputs": ["", ""], "Input Dims": [[1, 128000], [1, 128000]], "Input Strides": [[128000, 1], [128000, 1]], "Input type": ["float", "float"]} |

The CSV/JSON siblings contain full sample metadata and trace paths.
