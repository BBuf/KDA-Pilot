# Kernel Shape Inventory — sharegpt_mid

- Model: `inclusionAI/Ling-2.6-flash`
- Dataset: `sharegpt`
- Concurrency: `mid`
- Threshold: GPU kernel name share `> 2.0%`
- Total GPU kernel time: `1073.6 ms`
- Trace files: `4`

| % GPU | Calls | Category | Shape | SGLang relevant | Kernel | Shape provenance |
|---:|---:|---|---|---|---|---|
| 26.15 | 2232 | moe | ok | True | `fused_moe_kernel` | external_id=64135: `sglang::inplace_fused_experts` {"Concrete Inputs": ["", "", "", "", "", "", "", "", "True", "False", "False", "False", "False", "False", "False", "", "", "", "", "", "", "", "2.5", "", "", "False", ""], "Inpu... |
| 13.52 | 2304 | gemm | ok | True | `kernel_cutlass_kernel_flashinfernormkernelsfused_add_rmsnormFusedAddRMSNormKernel_object_at__tensorptrbf16gmemalign128o409640961_tensorptrbf16gmemalign128o409640961_tensorptrbf16gmemalign_0` | nearest_preceding_shape_cpu_op: `aten::view` {"Concrete Inputs": ["", "[-1, 4096]"], "Input Dims": [[44, 4096], []], "Input Strides": [[4096, 1], []], "Input type": ["c10::BFloat16", "ScalarList"]} |
| 13.48 | 2080 | comm | ok | True | `void (anonymous namespace)::all_reduce_one_shot_push_kernel<__nv_bfloat16, 4u, true>((anonymous namespace)::AllReducePushData, device::distributed::PushController)` | external_id=58465: `aten::as_strided` {"Concrete Inputs": ["", "[44, 1024]", "[3072, 1]", "1024"], "Input Dims": [[44, 3072], [], [], []], "Input Strides": [[3072, 1], [], [], []], "Input type": ["float", "ScalarLis... |
| 6.29 | 124 | gemm | ok | True | `cutlass3x_sm100_simt_sgemm_f32_f32_f32_f32_f32_64x64x16_1x1x1_3_tnn_align1_bias_f32_relu` | external_id=65869: `aten::mm` {"Concrete Inputs": ["", ""], "Input Dims": [[12199, 4096], [4096, 256]], "Input Strides": [[4096, 1], [1, 4096]], "Input type": ["float", "float"]} |
| 3.02 | 280 | quant_gemm | ok | True | `nvjet_sm100_tst_128x256_64x6_2x1_2cta_v_bz_TNT` | external_id=63939: `aten::mm` {"Concrete Inputs": ["", ""], "Input Dims": [[12199, 4096], [4096, 4608]], "Input Strides": [[4096, 1], [1, 4096]], "Input type": ["c10::BFloat16", "c10::BFloat16"]} |
| 2.67 | 992 | gemm | ok | True | `void cutlass::Kernel2<cutlass_80_simt_sgemm_64x64_8x5_tn_align1>(cutlass_80_simt_sgemm_64x64_8x5_tn_align1::Params)` | nearest_preceding_shape_cpu_op: `aten::as_strided` {"Concrete Inputs": ["", "[0]", "[1]", "384"], "Input Dims": [[384], [], [], []], "Input Strides": [[1], [], [], []], "Input type": ["long int", "ScalarList", "ScalarList", "Sca... |

The CSV/JSON siblings contain full sample metadata and trace paths.
