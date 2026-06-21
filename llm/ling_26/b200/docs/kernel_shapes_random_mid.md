# Kernel Shape Inventory — random_mid

- Model: `inclusionAI/Ling-2.6-flash`
- Dataset: `random`
- Concurrency: `mid`
- Threshold: GPU kernel name share `> 2.0%`
- Total GPU kernel time: `854.9 ms`
- Trace files: `4`

| % GPU | Calls | Category | Shape | SGLang relevant | Kernel | Shape provenance |
|---:|---:|---|---|---|---|---|
| 32.32 | 2232 | moe | ok | True | `fused_moe_kernel` | external_id=21855: `sglang::inplace_fused_experts` {"Concrete Inputs": ["", "", "", "", "", "", "", "", "True", "False", "False", "False", "False", "False", "False", "", "", "", "", "", "", "", "2.5", "", "", "False", ""], "Inpu... |
| 8.64 | 2080 | comm | ok | True | `void (anonymous namespace)::all_reduce_one_shot_push_kernel<__nv_bfloat16, 4u, true>((anonymous namespace)::AllReducePushData, device::distributed::PushController)` | nearest_preceding_shape_cpu_op: `aten::sub` {"Concrete Inputs": ["", "", "1"], "Input Dims": [[32], [32], []], "Input Strides": [[1], [1], []], "Input type": ["int", "int", "Scalar"]} |
| 7.47 | 2304 | gemm | ok | True | `kernel_cutlass_kernel_flashinfernormkernelsfused_add_rmsnormFusedAddRMSNormKernel_object_at__tensorptrbf16gmemalign128o409640961_tensorptrbf16gmemalign128o409640961_tensorptrbf16gmemalign_0` | nearest_preceding_shape_cpu_op: `sglang::outplace_all_reduce` {"Concrete Inputs": ["", "", ""], "Input Dims": [[39, 4096], [], []], "Input Strides": [[4096, 1], [], []], "Input type": ["c10::BFloat16", "", ""]} |
| 6.66 | 124 | gemm | ok | True | `cutlass3x_sm100_simt_sgemm_f32_f32_f32_f32_f32_64x64x16_1x1x1_3_tnn_align1_bias_f32_relu` | external_id=19289: `aten::mm` {"Concrete Inputs": ["", ""], "Input Dims": [[9780, 4096], [4096, 256]], "Input Strides": [[4096, 1], [1, 4096]], "Input type": ["float", "float"]} |
| 3.32 | 992 | gemm | ok | True | `void cutlass::Kernel2<cutlass_80_simt_sgemm_64x64_8x5_tn_align1>(cutlass_80_simt_sgemm_64x64_8x5_tn_align1::Params)` | nearest_preceding_shape_cpu_op: `aten::copy_` {"Concrete Inputs": ["", "", "True"], "Input Dims": [[32], [32], []], "Input Strides": [[1], [1], []], "Input type": ["long int", "long int", "Scalar"]} |
| 2.14 | 128 | quant_gemm | ok | True | `nvjet_sm100_tst_256x224_64x4_2x2_2cta_h_bz_TNT` | external_id=18962: `aten::mm` {"Concrete Inputs": ["", ""], "Input Dims": [[9780, 4096], [4096, 3072]], "Input Strides": [[4096, 1], [1, 4096]], "Input type": ["c10::BFloat16", "c10::BFloat16"]} |

The CSV/JSON siblings contain full sample metadata and trace paths.
