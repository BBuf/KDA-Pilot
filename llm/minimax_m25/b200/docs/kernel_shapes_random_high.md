# Kernel Shape Inventory — random_high

- Model: `MiniMaxAI/MiniMax-M2.5`
- Dataset: `random`
- Concurrency: `high`
- Threshold: GPU kernel name share `> 2.0%`
- Total GPU kernel time: `1668.6 ms`
- Trace files: `8`

| % GPU | Calls | Category | Shape | SGLang relevant | Kernel | Shape provenance |
|---:|---:|---|---|---|---|---|
| 31.73 | 8928 | moe | ok | True | `fused_moe_kernel` | external_id=29145: `Torch-Compiled Region: 5/3` {} |
| 9.65 | 6000 | comm | ok | True | `void (anonymous namespace)::all_reduce_two_shot_kernel<__half, 8u, true>(host::distributed::AllReduceData const*, (anonymous namespace)::AllReduceParams, device::distributed::PullController)` | external_id=35566: `Torch-Compiled Region: 5/3` {} |
| 9.32 | 8928 | quant_gemm | ok | True | `_w8a8_block_fp8_matmul` | external_id=26296: `Torch-Compiled Region: 5/3` {} |
| 6.04 | 1488 | gemm | missing | True | `cutlass3x_sm100_simt_sgemm_f32_f32_f32_f32_f32_32x32x16_1x1x1_3_tnn_align1_bias_f32_relu` | external_id=29145: `Torch-Compiled Region: 5/3` {} |
| 4.19 | 1984 | gemm | missing | True | `void cutlass::Kernel2<cutlass_80_simt_sgemm_64x64_8x5_tn_align1>(cutlass_80_simt_sgemm_64x64_8x5_tn_align1::Params)` | external_id=23451: `Torch-Compiled Region: 5/3` {} |
| 3.61 | 3472 | attention | ok | True | `fmhaSm100fKernel_QkvFp16OFp16H128PagedKvCausalP64VarSeqQ128Kv128PersistentContext` | external_id=32354: `sglang::unified_attention_with_output` {"Concrete Inputs": ["", "", "", "", "True", "0", "", "", "", "", "", "", ""], "Input Dims": [[768, 768], [768, 1, 128], [768, 1, 128], [768, 768], [], [], [], [], [], [], [], [... |
| 3.57 | 3000 | comm | ok | True | `void (anonymous namespace)::all_reduce_one_shot_push_kernel<__half, 8u, true>((anonymous namespace)::AllReducePushData, device::distributed::PushController)` | nearest_preceding_shape_cpu_op: `aten::copy_` {"Concrete Inputs": ["", "", "False"], "Input Dims": [[104], [104], []], "Input Strides": [[1], [1], []], "Input type": ["int", "int", "Scalar"]} |
| 2.63 | 17856 | quant_gemm | missing | True | `void (anonymous namespace)::per_token_group_quant_8bit_v2_kernel<(anonymous namespace)::NaiveScheduler, 128, 8, __half, __nv_fp8_e4m3, false, false, false, true, float>(__half const*, __nv_fp8_e4m3*, float*, int const*, int, int, int, int, int)` | external_id=29145: `Torch-Compiled Region: 5/3` {} |
| 2.54 | 6944 | norm | missing | True | `void flashinfer::norm::FusedAddRMSNormKernel<8u, __half>(__half*, __half*, __half*, unsigned int, unsigned int, unsigned int, float, float)` | external_id=18574: `Torch-Compiled Region: 5/3` {} |

The CSV/JSON siblings contain full sample metadata and trace paths.
