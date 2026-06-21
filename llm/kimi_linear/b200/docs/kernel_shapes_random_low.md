# Kernel Shape Inventory — random_low

- Model: `moonshotai/Kimi-Linear-48B-A3B-Instruct`
- Dataset: `random`
- Concurrency: `low`
- Threshold: GPU kernel name share `> 2.0%`
- Total GPU kernel time: `155.8 ms`
- Trace files: `4`

| % GPU | Calls | Category | Shape | SGLang relevant | Kernel | Shape provenance |
|---:|---:|---|---|---|---|---|
| 15.99 | 1980 | comm | ok | True | `void (anonymous namespace)::all_reduce_one_shot_push_kernel<__nv_bfloat16, 4u, true>((anonymous namespace)::AllReducePushData, device::distributed::PushController)` | timestamp_enclosure: `aten::gt` {"Concrete Inputs": ["", "0"], "Input Dims": [[1], []], "Input Strides": [[1], []], "Input type": ["int", "Scalar"]} |
| 14.79 | 1872 | moe | ok | True | `fused_moe_kernel` | external_id=300: `aten::copy_` {"Concrete Inputs": ["", "", "False"], "Input Dims": [[1], [1], []], "Input Strides": [[1], [1], []], "Input type": ["int", "int", "Scalar"]} |
| 8.58 | 216 | norm | ok | True | `void flashinfer::norm::FusedAddRMSNormKernel<8u, __nv_bfloat16>(__nv_bfloat16*, __nv_bfloat16*, __nv_bfloat16*, unsigned int, unsigned int, unsigned int, float, float)` | timestamp_enclosure: `aten::gt` {"Concrete Inputs": ["", "0"], "Input Dims": [[1], []], "Input Strides": [[1], []], "Input type": ["int", "Scalar"]} |
| 5.87 | 1728 | quant_gemm | ok | True | `nvjet_sm100_tst_16x64_64x16_2x1_v_bz_TNN` | timestamp_enclosure: `aten::_index_put_impl_` {"Concrete Inputs": ["", "", "", "False", "False"], "Input Dims": [[3577], [], [], [], []], "Input Strides": [[1], [], [], [], []], "Input type": ["long int", "", "long int", "S... |
| 5.62 | 1728 | gemm | ok | True | `kernel_cutlass_kernel_flashinfernormkernelsfused_add_rmsnormFusedAddRMSNormKernel_object_at__tensorptrbf16gmemalign128o230423041_tensorptrbf16gmemalign128o230423041_tensorptrbf16gmemalign_0` | nearest_preceding_shape_cpu_op: `aten::_foreach_copy_` {"Concrete Inputs": ["", "", "False"], "Input Dims": [[[1], [1], [1], [1]], [[1], [1], [1], [1]], []], "Input Strides": [[[1], [1], [1], [1]], [[1], [1], [1], [1]], []], "Input ... |
| 4.83 | 1888 | quant_gemm | ok | True | `nvjet_sm100_tst_32x64_64x16_4x1_v_bz_splitK_TNN` | nearest_preceding_shape_cpu_op: `aten::copy_` {"Concrete Inputs": ["", "", "False"], "Input Dims": [[2], [2], []], "Input Strides": [[1], [1], []], "Input type": ["int", "int", "Scalar"]} |
| 3.37 | 1908 | other | ok | True | `void (anonymous namespace)::act_and_mul_kernel<__nv_bfloat16, ((anonymous namespace)::ActivationKind)0, true, false>((anonymous namespace)::ActivationParams)` | timestamp_enclosure: `sglang::unified_linear_attention_with_output` {"Concrete Inputs": ["", "", "", "", "1"], "Input Dims": [[48, 3072], [1, 48, 8, 128], [1, 48, 8], [1, 48, 8, 128], []], "Input Strides": [[3336, 1], [49152, 1024, 128, 1], [384... |
| 3.31 | 640 | quant_gemm | ok | True | `nvjet_sm100_tst_32x64_64x16_4x1_v_bz_TNN` | nearest_preceding_shape_cpu_op: `detach_` {"Concrete Inputs": [""], "Input Dims": [[1]], "Input Strides": [[1]], "Input type": ["long int"]} |
| 2.79 | 224 | attention | ok | True | `void flashinfer::mla::BatchMLAPagedAttentionKernel<flashinfer::mla::KernelTraits<false, 2u, true, 512u, 64u, 64u, 64u, __nv_bfloat16, __nv_bfloat16, __nv_bfloat16, int>, flashinfer::MLAParams<__nv_bfloat16, __nv_bfloat16, __nv_bfloat16, int> >(flashinfer::MLAParams<__nv_bfloat16, __nv_bfloat16, __nv_bfloat16, int>)` | nearest_preceding_shape_cpu_op: `aten::copy_` {"Concrete Inputs": ["", "", "False"], "Input Dims": [[2], [2], []], "Input Strides": [[1], [1], []], "Input type": ["int", "int", "Scalar"]} |
| 2.53 | 944 | quant_gemm | ok | True | `nvjet_sm100_tst_16x64_64x16_4x1_v_bz_TNN` | nearest_preceding_shape_cpu_op: `aten::copy_` {"Concrete Inputs": ["", "", "False"], "Input Dims": [[2], [2], []], "Input Strides": [[1], [1], []], "Input type": ["int", "int", "Scalar"]} |

The CSV/JSON siblings contain full sample metadata and trace paths.
