# Kernel Shape Inventory — sharegpt_mid

- Model: `poolside/Laguna-XS.2-FP8`
- Dataset: `sharegpt`
- Concurrency: `mid`
- Threshold: GPU kernel name share `> 2.0%`
- Total GPU kernel time: `509.3 ms`
- Trace files: `4`

| % GPU | Calls | Category | Shape | SGLang relevant | Kernel | Shape provenance |
|---:|---:|---|---|---|---|---|
| 19.07 | 2808 | moe | missing | True | `fused_moe_kernel` | external_id=37247: `Torch-Compiled Region: 5/1` {} |
| 6.55 | 2592 | comm | ok | True | `void (anonymous namespace)::all_reduce_one_shot_push_kernel<__nv_bfloat16, 4u, true>((anonymous namespace)::AllReducePushData, device::distributed::PushController)` | external_id=35329: `Torch-Compiled Region: 5/3` {} |
| 5.56 | 1600 | norm | ok | True | `void flashinfer::norm::FusedAddRMSNormKernel<8u, __nv_bfloat16>(__nv_bfloat16*, __nv_bfloat16*, __nv_bfloat16*, unsigned int, unsigned int, unsigned int, float, float)` | external_id=34803: `aten::view` {"Concrete Inputs": ["", "[-1, 64, 2, 128]"], "Input Dims": [[4368128, 2, 128], []], "Input Strides": [[256, 128, 1], []], "Input type": ["c10::BFloat16", "ScalarList"]} |
| 5.00 | 156 | gemm | ok | True | `cutlass3x_sm100_simt_sgemm_f32_f32_f32_f32_f32_128x128x16_1x1x1_3_tnn_align1_bias_f32_relu` | external_id=37247: `Torch-Compiled Region: 5/1` {} |
| 4.25 | 468 | gemm | ok | True | `cutlass3x_sm100_simt_sgemm_f32_f32_f32_f32_f32_32x32x16_1x1x1_3_tnn_align1_bias_f32_relu` | external_id=40700: `Torch-Compiled Region: 5/3` {} |
| 2.83 | 320 | quant_gemm | missing | True | `nvjet_sm100_tst_128x256_64x6_2x2_2cta_h_bz_TNT` | external_id=37247: `Torch-Compiled Region: 5/1` {} |
| 2.77 | 600 | attention | ok | True | `fmhaSm100fKernel_QkvBfloat16OBfloat16H128PagedKvSlidingOrChunkedCausalP64VarSeqQ128Kv128PersistentContext` | external_id=38008: `sglang::unified_attention_with_output` {"Concrete Inputs": ["", "", "", "", "True", "23", "", "", ""], "Input Dims": [[8192, 2048], [8192, 2, 128], [8192, 2, 128], [8192, 2048], [], [], [], [], []], "Input Strides": ... |
| 2.48 | 780 | gemm | ok | True | `void cutlass::Kernel2<cutlass_80_simt_sgemm_64x64_8x5_tn_align1>(cutlass_80_simt_sgemm_64x64_8x5_tn_align1::Params)` | nearest_preceding_shape_cpu_op: `aten::view` {"Concrete Inputs": ["", "[31]"], "Input Dims": [[31], []], "Input Strides": [[1], []], "Input type": ["long int", "ScalarList"]} |

The CSV/JSON siblings contain full sample metadata and trace paths.
