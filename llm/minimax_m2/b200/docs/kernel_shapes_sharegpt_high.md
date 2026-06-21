# Kernel Shape Inventory — sharegpt_high

- Model: `MiniMaxAI/MiniMax-M2`
- Dataset: `sharegpt`
- Concurrency: `high`
- Threshold: GPU kernel name share `> 2.0%`
- Total GPU kernel time: `1032.6 ms`
- Trace files: `4`

| % GPU | Calls | Category | Shape | SGLang relevant | Kernel | Shape provenance |
|---:|---:|---|---|---|---|---|
| 47.91 | 4464 | moe | ok | True | `fused_moe_kernel` | external_id=57752: `Torch-Compiled Region: 5/2` {} |
| 10.03 | 4464 | quant_gemm | ok | True | `_w8a8_block_fp8_matmul` | external_id=57540: `aten::slice` {"Concrete Inputs": ["", "0", "-1", "9223372036854775807", "1"], "Input Dims": [[256], [], [], [], []], "Input Strides": [[1], [], [], [], []], "Input type": ["long int", "Scala... |
| 5.05 | 1736 | gemm | ok | True | `void cutlass::Kernel2<cutlass_80_simt_sgemm_64x64_8x5_tn_align1>(cutlass_80_simt_sgemm_64x64_8x5_tn_align1::Params)` | external_id=54508: `Torch-Compiled Region: 5/3` {} |
| 3.53 | 3500 | comm | ok | True | `void (anonymous namespace)::all_reduce_one_shot_push_kernel<__half, 4u, true>((anonymous namespace)::AllReducePushData, device::distributed::PushController)` | external_id=54508: `Torch-Compiled Region: 5/3` {} |
| 3.47 | 1240 | attention | ok | True | `fmhaSm100fKernel_QkvFp16OFp16H128PagedKvCausalP64VarSeqQ128Kv128PersistentContext` | external_id=57754: `sglang::unified_attention_with_output` {"Concrete Inputs": ["", "", "", "", "True", "0", "", "", "", "", "", "", ""], "Input Dims": [[2560, 1536], [2560, 2, 128], [2560, 2, 128], [2560, 1536], [], [], [], [], [], [],... |
| 3.47 | 1000 | comm | ok | True | `void (anonymous namespace)::all_reduce_two_shot_kernel<__half, 4u, true>(host::distributed::AllReduceData const*, (anonymous namespace)::AllReduceParams, device::distributed::PullController)` | external_id=57540: `aten::slice` {"Concrete Inputs": ["", "0", "-1", "9223372036854775807", "1"], "Input Dims": [[256], [], [], [], []], "Input Strides": [[1], [], [], [], []], "Input type": ["long int", "Scala... |
| 3.02 | 248 | gemm | ok | True | `cutlass3x_sm100_simt_sgemm_f32_f32_f32_f32_f32_128x64x16_1x1x1_3_tnn_align1_bias_f32_relu` | external_id=57540: `aten::slice` {"Concrete Inputs": ["", "0", "-1", "9223372036854775807", "1"], "Input Dims": [[256], [], [], [], []], "Input Strides": [[1], [], [], [], []], "Input type": ["long int", "Scala... |
| 2.21 | 2480 | norm | ok | True | `void flashinfer::norm::FusedAddRMSNormKernel<8u, __half>(__half*, __half*, __half*, unsigned int, unsigned int, unsigned int, float, float)` | external_id=49904: `Torch-Compiled Region: 5/3` {} |
| 2.18 | 992 | attention | ok | True | `fmhaSm100fKernel_QkvFp16OFp16H128PagedKvCausalP64VarSeqQ8Kv128PersistentSwapsAbForGen` | nearest_preceding_shape_cpu_op: `aten::as_strided` {"Concrete Inputs": ["", "[320]", "[1]", "228659756"], "Input Dims": [[371], [], [], []], "Input Strides": [[1], [], [], []], "Input type": ["int", "ScalarList", "ScalarList", "... |

The CSV/JSON siblings contain full sample metadata and trace paths.
