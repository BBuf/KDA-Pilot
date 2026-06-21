# Kernel Shape Inventory — sharegpt_mid

- Model: `MiniMaxAI/MiniMax-M2.5`
- Dataset: `sharegpt`
- Concurrency: `mid`
- Threshold: GPU kernel name share `> 2.0%`
- Total GPU kernel time: `2202.2 ms`
- Trace files: `8`

| % GPU | Calls | Category | Shape | SGLang relevant | Kernel | Shape provenance |
|---:|---:|---|---|---|---|---|
| 28.53 | 8928 | moe | ok | True | `fused_moe_kernel` | external_id=54662: `aten::as_strided` {"Concrete Inputs": ["", "[5524, 768]", "[768, 1]", "0"], "Input Dims": [[5632, 768], [], [], []], "Input Strides": [[768, 1], [], [], []], "Input type": ["c10::Half", "ScalarLi... |
| 9.81 | 8928 | quant_gemm | ok | True | `_w8a8_block_fp8_matmul` | external_id=54662: `aten::as_strided` {"Concrete Inputs": ["", "[5524, 768]", "[768, 1]", "0"], "Input Dims": [[5632, 768], [], [], []], "Input Strides": [[768, 1], [], [], []], "Input type": ["c10::Half", "ScalarLi... |
| 4.98 | 496 | gemm | ok | True | `cutlass3x_sm100_simt_sgemm_f32_f32_f32_f32_f32_64x32x16_1x1x1_3_tnn_align1_bias_f32_relu` | external_id=54662: `aten::as_strided` {"Concrete Inputs": ["", "[5524, 768]", "[768, 1]", "0"], "Input Dims": [[5632, 768], [], [], []], "Input Strides": [[768, 1], [], [], []], "Input type": ["c10::Half", "ScalarLi... |
| 3.66 | 2976 | gemm | ok | True | `void cutlass::Kernel2<cutlass_80_simt_sgemm_64x64_8x5_tn_align1>(cutlass_80_simt_sgemm_64x64_8x5_tn_align1::Params)` | external_id=46792: `aten::as_strided` {"Concrete Inputs": ["", "[64859, 1, 64, 128]", "[8192, 8192, 128, 1]", ""], "Input Dims": [[64859, 1, 64, 128], [], [], []], "Input Strides": [[8192, 128, 128, 1], [], [], []],... |
| 3.48 | 17856 | quant_gemm | ok | True | `void (anonymous namespace)::per_token_group_quant_8bit_v2_kernel<(anonymous namespace)::NaiveScheduler, 128, 8, __half, __nv_fp8_e4m3, false, false, false, true, float>(__half const*, __nv_fp8_e4m3*, float*, int const*, int, int, int, int, int)` | external_id=54662: `aten::as_strided` {"Concrete Inputs": ["", "[5524, 768]", "[768, 1]", "0"], "Input Dims": [[5632, 768], [], [], []], "Input Strides": [[768, 1], [], [], []], "Input type": ["c10::Half", "ScalarLi... |
| 3.22 | 6000 | comm | ok | True | `void (anonymous namespace)::all_reduce_one_shot_push_kernel<__half, 8u, true>((anonymous namespace)::AllReducePushData, device::distributed::PushController)` | external_id=46792: `aten::as_strided` {"Concrete Inputs": ["", "[64859, 1, 64, 128]", "[8192, 8192, 128, 1]", ""], "Input Dims": [[64859, 1, 64, 128], [], [], []], "Input Strides": [[8192, 128, 128, 1], [], [], []],... |
| 3.21 | 1488 | moe | ok | True | `void moe_sum_reduce_kernel_warp_token_topk<c10::Half, 8, 4>(c10::Half const*, c10::Half*, long, long, long, long, long, at::OpMathType<c10::Half>::type)` | external_id=54662: `aten::as_strided` {"Concrete Inputs": ["", "[5524, 768]", "[768, 1]", "0"], "Input Dims": [[5632, 768], [], [], []], "Input Strides": [[768, 1], [], [], []], "Input type": ["c10::Half", "ScalarLi... |
| 3.00 | 3968 | norm | ok | True | `void flashinfer::norm::FusedAddRMSNormKernel<8u, __half>(__half*, __half*, __half*, unsigned int, unsigned int, unsigned int, float, float)` | external_id=46792: `aten::as_strided` {"Concrete Inputs": ["", "[64859, 1, 64, 128]", "[8192, 8192, 128, 1]", ""], "Input Dims": [[64859, 1, 64, 128], [], [], []], "Input Strides": [[8192, 128, 128, 1], [], [], []],... |
| 2.88 | 496 | gemm | ok | True | `cutlass3x_sm100_simt_sgemm_f32_f32_f32_f32_f32_128x64x16_1x1x1_3_tnn_align1_bias_f32_relu` | external_id=51817: `aten::as_strided` {"Concrete Inputs": ["", "[3027, 1, 128]", "[128, 128, 1]", "0"], "Input Dims": [[3072, 1, 128], [], [], []], "Input Strides": [[128, 128, 1], [], [], []], "Input type": ["c10::... |
| 2.70 | 1984 | attention | ok | True | `fmhaSm100fKernel_QkvFp16OFp16H128PagedKvCausalP64VarSeqQ128Kv128PersistentContext` | external_id=54664: `aten::view` {"Concrete Inputs": ["", "[-1, 128]"], "Input Dims": [[5524, 1, 128], []], "Input Strides": [[1024, 128, 1], []], "Input type": ["c10::Half", "ScalarList"]} |
| 2.51 | 4960 | gemm | ok | True | `kernel_cutlass_kernel_flashinfernormkernelsfused_add_rmsnormFusedAddRMSNormKernel_object_at__tensorptrf16gmemalign128o307230721_tensorptrf16gmemalign128o307230721_tensorptrf16gmemalign16o_0` | nearest_preceding_shape_cpu_op: `aten::as_strided` {"Concrete Inputs": ["", "[32, 1]", "[1, 0]", ""], "Input Dims": [[32], [], [], []], "Input Strides": [[1], [], [], []], "Input type": ["long int", "ScalarList", "ScalarList", ""]} |

The CSV/JSON siblings contain full sample metadata and trace paths.
