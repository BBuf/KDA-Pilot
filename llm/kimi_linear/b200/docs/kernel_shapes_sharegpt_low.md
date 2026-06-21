# Kernel Shape Inventory — sharegpt_low

- Model: `moonshotai/Kimi-Linear-48B-A3B-Instruct`
- Dataset: `sharegpt`
- Concurrency: `low`
- Threshold: GPU kernel name share `> 2.0%`
- Total GPU kernel time: `417.4 ms`
- Trace files: `4`

| % GPU | Calls | Category | Shape | SGLang relevant | Kernel | Shape provenance |
|---:|---:|---|---|---|---|---|
| 46.45 | 1980 | comm | ok | True | `void (anonymous namespace)::all_reduce_one_shot_push_kernel<__nv_bfloat16, 4u, true>((anonymous namespace)::AllReducePushData, device::distributed::PushController)` | nearest_preceding_shape_cpu_op: `aten::copy_` {"Concrete Inputs": ["", "", "False"], "Input Dims": [[], [], []], "Input Strides": [[], [], []], "Input type": ["int", "int", "Scalar"]} |
| 25.98 | 216 | norm | ok | True | `void flashinfer::norm::FusedAddRMSNormKernel<8u, __nv_bfloat16>(__nv_bfloat16*, __nv_bfloat16*, __nv_bfloat16*, unsigned int, unsigned int, unsigned int, float, float)` | timestamp_enclosure: `sglang::unified_linear_attention_with_output` {"Concrete Inputs": ["", "", "", "", "21"], "Input Dims": [[16, 3072], [1, 16, 8, 128], [1, 16, 8], [1, 16, 8, 128], []], "Input Strides": [[3336, 1], [16384, 1024, 128, 1], [12... |
| 4.45 | 1872 | moe | ok | True | `fused_moe_kernel` | external_id=115118: `aten::as_strided` {"Concrete Inputs": ["", "[1, 15, 8, 128]", "[15360, 1024, 128, 1]", ""], "Input Dims": [[15, 8, 128], [], [], []], "Input Strides": [[1024, 128, 1], [], [], []], "Input type": ... |
| 2.19 | 1728 | quant_gemm | ok | True | `nvjet_sm100_tst_16x64_64x16_2x1_v_bz_TNN` | nearest_preceding_shape_cpu_op: `aten::copy_` {"Concrete Inputs": ["", "", "False"], "Input Dims": [[2], [2], []], "Input Strides": [[1], [1], []], "Input type": ["int", "int", "Scalar"]} |
| 2.09 | 1728 | gemm | ok | True | `kernel_cutlass_kernel_flashinfernormkernelsfused_add_rmsnormFusedAddRMSNormKernel_object_at__tensorptrbf16gmemalign128o230423041_tensorptrbf16gmemalign128o230423041_tensorptrbf16gmemalign_0` | timestamp_enclosure: `gloo:broadcast` {"Concrete Inputs": [""], "Input Dims": [[1]], "Input Strides": [[1]], "Input type": ["long int"]} |
| 2.04 | 2124 | quant_gemm | ok | True | `nvjet_sm100_tst_32x64_64x16_4x1_v_bz_splitK_TNN` | nearest_preceding_shape_cpu_op: `aten::copy_` {"Concrete Inputs": ["", "", "False"], "Input Dims": [[2], [2], []], "Input Strides": [[1], [1], []], "Input type": ["int", "int", "Scalar"]} |

The CSV/JSON siblings contain full sample metadata and trace paths.
