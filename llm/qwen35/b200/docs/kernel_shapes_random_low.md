# Kernel Shape Inventory — random_low

- Model: `nvidia/Qwen3.5-397B-A17B-NVFP4`
- Dataset: `random`
- Concurrency: `low`
- Threshold: GPU kernel name share `> 2.0%`
- Total GPU kernel time: `2387.5 ms`
- Trace files: `4`

| % GPU | Calls | Category | Shape | SGLang relevant | Kernel | Shape provenance |
|---:|---:|---|---|---|---|---|
| 41.70 | 4284 | comm | ok | True | `void flashinfer::trtllm_allreduce_fusion::allreduce_fusion_kernel_oneshot_lamport<(flashinfer::trtllm_allreduce_fusion::AllReduceFusionPattern)1, __nv_bfloat16, 4, false, false>(flashinfer::trtllm_allreduce_fusion::AllReduceFusionParams<__nv_bfloat16>)` | external_id=5455: `sglang::flashinfer_allreduce_residual_rmsnorm` {"Concrete Inputs": ["", "", "", "9.9999999999999995e-07", "2048", "", "False", "False", "True"], "Input Dims": [[38, 4096], [38, 4096], [4096], [], [], [], [], [], []], "Input ... |
| 20.78 | 480 | quant_gemm | ok | True | `nvjet_sm100_tst_64x8_64x16_1x4_h_bz_TNT` | external_id=5473: `aten::mm` {"Concrete Inputs": ["", ""], "Input Dims": [[38, 4096], [4096, 512]], "Input Strides": [[4096, 1], [1, 4096]], "Input type": ["c10::BFloat16", "c10::BFloat16"]} |
| 13.99 | 180 | quant_gemm | ok | True | `nvjet_sm100_tst_128x24_64x11_4x2_h_bz_TNT` | external_id=11788: `aten::empty` {"Concrete Inputs": ["[38, 16, 128]", "15", "", "", "False", ""], "Input Dims": [[], [], [], [], [], []], "Input Strides": [[], [], [], [], [], []], "Input type": ["ScalarList",... |
| 5.55 | 60 | quant_gemm | ok | True | `nvjet_sm100_tst_64x32_64x16_2x1_2cta_v_bz_TNT` | external_id=9825: `aten::mm` {"Concrete Inputs": ["", ""], "Input Dims": [[38, 4096], [4096, 4608]], "Input Strides": [[4096, 1], [1, 4096]], "Input type": ["c10::BFloat16", "c10::BFloat16"]} |
| 3.38 | 72 | comm | ok | True | `void (anonymous namespace)::all_reduce_one_shot_push_kernel<__nv_bfloat16, 4u, true>((anonymous namespace)::AllReducePushData, device::distributed::PushController)` | nearest_preceding_shape_cpu_op: `aten::copy_` {"Concrete Inputs": ["", "", "False"], "Input Dims": [[38], [38], []], "Input Strides": [[1], [1], []], "Input type": ["long int", "int", "Scalar"]} |
| 2.62 | 36 | gemm | ok | True | `kernel_cutlass_kernel_flashinfernormkernelsrmsnormRMSNormKernel_object_at__tensorptrbf16gmemalign128o409640961_tensorptrbf16gmemalign16o40961_tensorptrbf16gmemalign128o409640961___True_2__0` | nearest_preceding_shape_cpu_op: `aten::copy_` {"Concrete Inputs": ["", "", "False"], "Input Dims": [[38], [38], []], "Input Strides": [[1], [1], []], "Input type": ["long int", "int", "Scalar"]} |

The CSV/JSON siblings contain full sample metadata and trace paths.
