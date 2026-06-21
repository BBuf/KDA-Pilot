# Kernel Shape Inventory — random_mid

- Model: `MiniMaxAI/MiniMax-M2.7`
- Dataset: `random`
- Concurrency: `mid`
- Threshold: GPU kernel name share `> 2.0%`
- Total GPU kernel time: `2045.0 ms`
- Trace files: `8`

| % GPU | Calls | Category | Shape | SGLang relevant | Kernel | Shape provenance |
|---:|---:|---|---|---|---|---|
| 31.40 | 8928 | moe | ok | True | `fused_moe_kernel` | external_id=11681: `aten::lift_fresh` {"Concrete Inputs": [""], "Input Dims": [[19]], "Input Strides": [[1]], "Input type": ["float"]} |
| 5.91 | 496 | gemm | ok | True | `cutlass3x_sm100_simt_sgemm_f32_f32_f32_f32_f32_128x128x16_1x1x1_3_tnn_align1_bias_f32_relu` | external_id=11767: `Torch-Compiled Region: 5/1` {} |
| 4.63 | 7000 | comm | ok | True | `void (anonymous namespace)::all_reduce_one_shot_push_kernel<__nv_bfloat16, 8u, true>((anonymous namespace)::AllReducePushData, device::distributed::PushController)` | nearest_preceding_shape_cpu_op: `aten::copy_` {"Concrete Inputs": ["", "", "False"], "Input Dims": [[32], [32], []], "Input Strides": [[1], [1], []], "Input type": ["int", "int", "Scalar"]} |
| 4.54 | 3472 | gemm | ok | True | `void cutlass::Kernel2<cutlass_80_simt_sgemm_64x64_8x5_tn_align1>(cutlass_80_simt_sgemm_64x64_8x5_tn_align1::Params)` | nearest_preceding_shape_cpu_op: `aten::as_strided` {"Concrete Inputs": ["", "[161]", "[1]", "9420984"], "Input Dims": [[204804], [], [], []], "Input Strides": [[1], [], [], []], "Input type": ["int", "ScalarList", "ScalarList", ... |
| 3.32 | 2976 | norm | ok | True | `void flashinfer::norm::FusedAddRMSNormKernel<8u, __nv_bfloat16>(__nv_bfloat16*, __nv_bfloat16*, __nv_bfloat16*, unsigned int, unsigned int, unsigned int, float, float)` | external_id=6760: `Torch-Compiled Region: 5/3` {} |
| 3.29 | 5952 | gemm | ok | True | `kernel_cutlass_kernel_flashinfernormkernelsfused_add_rmsnormFusedAddRMSNormKernel_object_at__tensorptrbf16gmemalign128o307230721_tensorptrbf16gmemalign128o307230721_tensorptrbf16gmemalign_0` | nearest_preceding_shape_cpu_op: `aten::copy_` {"Concrete Inputs": ["", "", "True"], "Input Dims": [[32], [32], []], "Input Strides": [[1], [1], []], "Input type": ["long int", "long int", "Scalar"]} |
| 2.74 | 8928 | quant_gemm | missing | True | `void (anonymous namespace)::per_token_group_quant_8bit_v2_kernel<(anonymous namespace)::NaiveScheduler, 128, 8, __nv_bfloat16, __nv_fp8_e4m3, false, false, false, true, float>(__nv_bfloat16 const*, __nv_fp8_e4m3*, float*, int const*, int, int, int, int, int)` | external_id=11767: `Torch-Compiled Region: 5/1` {} |
| 2.31 | 1000 | comm | ok | True | `void (anonymous namespace)::all_reduce_two_shot_kernel<__nv_bfloat16, 8u, true>(host::distributed::AllReduceData const*, (anonymous namespace)::AllReduceParams, device::distributed::PullController)` | external_id=9204: `Torch-Compiled Region: 5/3` {} |
| 2.06 | 992 | moe | ok | True | `void moe_sum_reduce_warp_per_token_vec_kernel<8>(c10::BFloat16 const*, c10::BFloat16*, long, long, long, long, long, long, float)` | external_id=11767: `Torch-Compiled Region: 5/1` {} |
| 2.03 | 496 | gemm | ok | True | `cutlass3x_sm100_simt_sgemm_f32_f32_f32_f32_f32_64x32x16_1x1x1_3_tnn_align1_bias_f32_relu` | external_id=9204: `Torch-Compiled Region: 5/3` {} |

The CSV/JSON siblings contain full sample metadata and trace paths.
