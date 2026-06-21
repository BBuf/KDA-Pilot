# Kernel Shape Inventory — random_mid

- Model: `MiniMaxAI/MiniMax-M2.5`
- Dataset: `random`
- Concurrency: `mid`
- Threshold: GPU kernel name share `> 2.0%`
- Total GPU kernel time: `2264.8 ms`
- Trace files: `8`

| % GPU | Calls | Category | Shape | SGLang relevant | Kernel | Shape provenance |
|---:|---:|---|---|---|---|---|
| 28.50 | 8928 | moe | ok | True | `fused_moe_kernel` | external_id=11627: `Torch-Compiled Region: 5/1` {} |
| 9.98 | 8928 | quant_gemm | ok | True | `_w8a8_block_fp8_matmul` | external_id=11627: `Torch-Compiled Region: 5/1` {} |
| 5.32 | 496 | gemm | ok | True | `cutlass3x_sm100_simt_sgemm_f32_f32_f32_f32_f32_128x128x16_1x1x1_3_tnn_align1_bias_f32_relu` | external_id=11701: `aten::as_strided` {"Concrete Inputs": ["", "[8943, 1, 128]", "[1024, 128, 1]", "0"], "Input Dims": [[9216, 1, 128], [], [], []], "Input Strides": [[1024, 128, 1], [], [], []], "Input type": ["c10... |
| 4.38 | 7000 | comm | ok | True | `void (anonymous namespace)::all_reduce_one_shot_push_kernel<__half, 8u, true>((anonymous namespace)::AllReducePushData, device::distributed::PushController)` | nearest_preceding_shape_cpu_op: `aten::copy_` {"Concrete Inputs": ["", "", "False"], "Input Dims": [[32], [32], []], "Input Strides": [[1], [1], []], "Input type": ["int", "int", "Scalar"]} |
| 4.10 | 3472 | gemm | ok | True | `void cutlass::Kernel2<cutlass_80_simt_sgemm_64x64_8x5_tn_align1>(cutlass_80_simt_sgemm_64x64_8x5_tn_align1::Params)` | nearest_preceding_shape_cpu_op: `aten::as_strided` {"Concrete Inputs": ["", "[24]", "[1]", "64"], "Input Dims": [[88], [], [], []], "Input Strides": [[1], [], [], []], "Input type": ["long int", "ScalarList", "ScalarList", "Scal... |
| 3.61 | 17856 | quant_gemm | ok | True | `void (anonymous namespace)::per_token_group_quant_8bit_v2_kernel<(anonymous namespace)::NaiveScheduler, 128, 8, __half, __nv_fp8_e4m3, false, false, false, true, float>(__half const*, __nv_fp8_e4m3*, float*, int const*, int, int, int, int, int)` | external_id=11701: `aten::as_strided` {"Concrete Inputs": ["", "[8943, 1, 128]", "[1024, 128, 1]", "0"], "Input Dims": [[9216, 1, 128], [], [], []], "Input Strides": [[1024, 128, 1], [], [], []], "Input type": ["c10... |
| 3.34 | 992 | moe | ok | True | `void moe_sum_reduce_kernel_warp_token_topk<c10::Half, 8, 4>(c10::Half const*, c10::Half*, long, long, long, long, long, at::OpMathType<c10::Half>::type)` | external_id=11701: `aten::as_strided` {"Concrete Inputs": ["", "[8943, 1, 128]", "[1024, 128, 1]", "0"], "Input Dims": [[9216, 1, 128], [], [], []], "Input Strides": [[1024, 128, 1], [], [], []], "Input type": ["c10... |
| 2.95 | 2976 | norm | ok | True | `void flashinfer::norm::FusedAddRMSNormKernel<8u, __half>(__half*, __half*, __half*, unsigned int, unsigned int, unsigned int, float, float)` | external_id=6694: `aten::empty_strided` {"Concrete Inputs": ["[39, 6, 128]", "[768, 128, 1]", "5", "0", "", "False"], "Input Dims": [[], [], [], [], [], []], "Input Strides": [[], [], [], [], [], []], "Input type": ["... |
| 2.91 | 5952 | gemm | ok | True | `kernel_cutlass_kernel_flashinfernormkernelsfused_add_rmsnormFusedAddRMSNormKernel_object_at__tensorptrf16gmemalign128o307230721_tensorptrf16gmemalign128o307230721_tensorptrf16gmemalign16o_0` | timestamp_enclosure: `gloo:broadcast` {"Concrete Inputs": [""], "Input Dims": [[1]], "Input Strides": [[1]], "Input type": ["long int"]} |
| 2.08 | 1000 | comm | ok | True | `void (anonymous namespace)::all_reduce_two_shot_kernel<__half, 8u, true>(host::distributed::AllReduceData const*, (anonymous namespace)::AllReduceParams, device::distributed::PullController)` | external_id=9120: `sglang::unified_attention_with_output` {"Concrete Inputs": ["", "", "", "", "True", "2", "", "", "", "", "", "", ""], "Input Dims": [[832, 768], [832, 1, 128], [832, 1, 128], [832, 768], [], [], [], [], [], [], [], [... |

The CSV/JSON siblings contain full sample metadata and trace paths.
