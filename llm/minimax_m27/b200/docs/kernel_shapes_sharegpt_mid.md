# Kernel Shape Inventory — sharegpt_mid

- Model: `MiniMaxAI/MiniMax-M2.7`
- Dataset: `sharegpt`
- Concurrency: `mid`
- Threshold: GPU kernel name share `> 2.0%`
- Total GPU kernel time: `2044.4 ms`
- Trace files: `8`

| % GPU | Calls | Category | Shape | SGLang relevant | Kernel | Shape provenance |
|---:|---:|---|---|---|---|---|
| 30.62 | 8928 | moe | ok | True | `fused_moe_kernel` | external_id=45892: `aten::as_strided` {"Concrete Inputs": ["", "[5552, 768]", "[768, 1]", "0"], "Input Dims": [[5632, 768], [], [], []], "Input Strides": [[768, 1], [], [], []], "Input type": ["c10::BFloat16", "Scal... |
| 5.39 | 496 | gemm | ok | True | `cutlass3x_sm100_simt_sgemm_f32_f32_f32_f32_f32_64x32x16_1x1x1_3_tnn_align1_bias_f32_relu` | external_id=45892: `aten::as_strided` {"Concrete Inputs": ["", "[5552, 768]", "[768, 1]", "0"], "Input Dims": [[5632, 768], [], [], []], "Input Strides": [[768, 1], [], [], []], "Input type": ["c10::BFloat16", "Scal... |
| 3.94 | 2976 | gemm | ok | True | `void cutlass::Kernel2<cutlass_80_simt_sgemm_64x64_8x5_tn_align1>(cutlass_80_simt_sgemm_64x64_8x5_tn_align1::Params)` | external_id=38022: `aten::view` {"Concrete Inputs": ["", "[-1, 128]"], "Input Dims": [[59, 1, 128], []], "Input Strides": [[1024, 128, 1], []], "Input type": ["c10::BFloat16", "ScalarList"]} |
| 3.51 | 6000 | comm | ok | True | `void (anonymous namespace)::all_reduce_one_shot_push_kernel<__nv_bfloat16, 8u, true>((anonymous namespace)::AllReducePushData, device::distributed::PushController)` | external_id=37942: `Torch-Compiled Region: 5/3` {} |
| 3.28 | 3968 | norm | ok | True | `void flashinfer::norm::FusedAddRMSNormKernel<8u, __nv_bfloat16>(__nv_bfloat16*, __nv_bfloat16*, __nv_bfloat16*, unsigned int, unsigned int, unsigned int, float, float)` | external_id=37942: `Torch-Compiled Region: 5/3` {} |
| 3.12 | 496 | gemm | ok | True | `cutlass3x_sm100_simt_sgemm_f32_f32_f32_f32_f32_128x64x16_1x1x1_3_tnn_align1_bias_f32_relu` | external_id=43038: `aten::as_strided` {"Concrete Inputs": ["", "[64824, 1, 64, 128]", "[8192, 8192, 128, 1]", ""], "Input Dims": [[64824, 1, 64, 128], [], [], []], "Input Strides": [[8192, 128, 128, 1], [], [], []],... |
| 2.85 | 1984 | attention | ok | True | `fmhaSm100fKernel_QkvBfloat16OBfloat16H128PagedKvCausalP64VarSeqQ128Kv128PersistentContext` | external_id=45894: `aten::copy_` {"Concrete Inputs": ["", "", "False"], "Input Dims": [[5552, 768], [5552, 768], []], "Input Strides": [[768, 1], [768, 1], []], "Input type": ["c10::BFloat16", "c10::BFloat16", ... |
| 2.75 | 4960 | gemm | ok | True | `kernel_cutlass_kernel_flashinfernormkernelsfused_add_rmsnormFusedAddRMSNormKernel_object_at__tensorptrbf16gmemalign128o307230721_tensorptrbf16gmemalign128o307230721_tensorptrbf16gmemalign_0` | nearest_preceding_shape_cpu_op: `aten::add` {"Concrete Inputs": ["", "", "1"], "Input Dims": [[32], [], []], "Input Strides": [[1], [], []], "Input type": ["int", "long int", "Scalar"]} |
| 2.57 | 8928 | quant_gemm | ok | True | `void (anonymous namespace)::per_token_group_quant_8bit_v2_kernel<(anonymous namespace)::NaiveScheduler, 128, 8, __nv_bfloat16, __nv_fp8_e4m3, false, false, false, true, float>(__nv_bfloat16 const*, __nv_fp8_e4m3*, float*, int const*, int, int, int, int, int)` | external_id=45892: `aten::as_strided` {"Concrete Inputs": ["", "[5552, 768]", "[768, 1]", "0"], "Input Dims": [[5632, 768], [], [], []], "Input Strides": [[768, 1], [], [], []], "Input type": ["c10::BFloat16", "Scal... |

The CSV/JSON siblings contain full sample metadata and trace paths.
