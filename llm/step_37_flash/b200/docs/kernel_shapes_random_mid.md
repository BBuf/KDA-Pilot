# Kernel Shape Inventory — random_mid

- Model: `stepfun-ai/Step-3.7-Flash-NVFP4`
- Dataset: `random`
- Concurrency: `mid`
- Threshold: GPU kernel name share `> 2.0%`
- Total GPU kernel time: `2697.1 ms`
- Trace files: `8`

| % GPU | Calls | Category | Shape | SGLang relevant | Kernel | Shape provenance |
|---:|---:|---|---|---|---|---|
| 23.47 | 5824 | comm | ok | True | `void (anonymous namespace)::all_reduce_one_shot_push_kernel<__nv_bfloat16, 8u, true>((anonymous namespace)::AllReducePushData, device::distributed::PushController)` | nearest_preceding_shape_cpu_op: `aten::copy_` {"Concrete Inputs": ["", "", "False"], "Input Dims": [[32], [32], []], "Input Strides": [[1], [1], []], "Input type": ["long int", "long int", "Scalar"]} |
| 23.05 | 6480 | gemm | ok | True | `kernel_cutlass_kernel_flashinfernormkernelsfused_add_rmsnormFusedAddRMSNormKernel_object_at__tensorptrbf16gmemalign128o409640961_tensorptrbf16gmemalign128o409640961_tensorptrbf16gmemalign_0` | timestamp_enclosure: `aten::transpose` {"Concrete Inputs": ["", "0", "1"], "Input Dims": [[320, 4096], [], []], "Input Strides": [[4096, 1], [], []], "Input type": ["c10::BFloat16", "Scalar", "Scalar"]} |
| 7.68 | 336 | gemm | ok | True | `cutlass3x_sm100_simt_sgemm_f32_f32_f32_f32_f32_128x128x16_1x1x1_3_tnn_align1_bias_f32_relu` | external_id=20676: `aten::mm` {"Concrete Inputs": ["", ""], "Input Dims": [[12438, 4096], [4096, 288]], "Input Strides": [[4096, 1], [1, 4096]], "Input type": ["float", "float"]} |
| 2.94 | 3024 | moe | ok | True | `void moeTopK<256>(float const*, bool const*, float*, int*, int, int, int, int, bool, float const*)` | external_id=20679: `sgl_kernel::topk_sigmoid` {"Concrete Inputs": ["", "", "", "True", ""], "Input Dims": [[12438, 8], [12438, 8], [12438, 288], [], [288]], "Input Strides": [[8, 1], [8, 1], [288, 1], [], [1]], "Input type"... |
| 2.79 | 2688 | gemm | ok | True | `void cutlass::Kernel2<cutlass_80_simt_sgemm_64x64_8x5_tn_align1>(cutlass_80_simt_sgemm_64x64_8x5_tn_align1::Params)` | nearest_preceding_shape_cpu_op: `aten::as_strided` {"Concrete Inputs": ["", "[26]", "[1]", "832"], "Input Dims": [[858], [], [], []], "Input Strides": [[1], [], [], []], "Input type": ["long int", "ScalarList", "ScalarList", "Sc... |
| 2.46 | 672 | quant_gemm | ok | True | `nvjet_sm100_tst_128x256_64x6_2x1_2cta_v_bz_TNT` | external_id=20346: `aten::mm` {"Concrete Inputs": ["", ""], "Input Dims": [[12438, 4096], [4096, 2816]], "Input Strides": [[4096, 1], [1, 4096]], "Input type": ["c10::BFloat16", "c10::BFloat16"]} |

The CSV/JSON siblings contain full sample metadata and trace paths.
