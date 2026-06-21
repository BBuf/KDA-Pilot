# Kernel Shape Inventory — sharegpt_low

- Model: `MiniMaxAI/MiniMax-M2.5`
- Dataset: `sharegpt`
- Concurrency: `low`
- Threshold: GPU kernel name share `> 2.0%`
- Total GPU kernel time: `735.1 ms`
- Trace files: `8`

| % GPU | Calls | Category | Shape | SGLang relevant | Kernel | Shape provenance |
|---:|---:|---|---|---|---|---|
| 20.46 | 8928 | quant_gemm | ok | True | `_w8a8_block_fp8_matmul` | external_id=40318: `Torch-Compiled Region: 5/3` {} |
| 15.77 | 8928 | moe | missing | True | `fused_moe_kernel` | external_id=40318: `Torch-Compiled Region: 5/3` {} |
| 13.30 | 9000 | comm | missing | True | `void (anonymous namespace)::all_reduce_one_shot_push_kernel<__half, 8u, true>((anonymous namespace)::AllReducePushData, device::distributed::PushController)` | external_id=40318: `Torch-Compiled Region: 5/3` {} |
| 10.78 | 7936 | gemm | ok | True | `kernel_cutlass_kernel_flashinfernormkernelsfused_add_rmsnormFusedAddRMSNormKernel_object_at__tensorptrf16gmemalign128o307230721_tensorptrf16gmemalign128o307230721_tensorptrf16gmemalign16o_0` | timestamp_enclosure: `aten::cat` {"Concrete Inputs": ["", "0"], "Input Dims": [[[64], [576]], []], "Input Strides": [[[1], [1]], []], "Input type": ["TensorList", "Scalar"]} |
| 4.19 | 17856 | quant_gemm | ok | True | `void (anonymous namespace)::per_token_group_quant_8bit_v2_kernel<(anonymous namespace)::NaiveScheduler, 128, 8, __half, __nv_fp8_e4m3, false, false, false, true, float>(__half const*, __nv_fp8_e4m3*, float*, int const*, int, int, int, int, int)` | nearest_preceding_shape_cpu_op: `aten::cat` {"Concrete Inputs": ["", "0"], "Input Dims": [[[64], [576]], []], "Input Strides": [[[1], [1]], []], "Input type": ["TensorList", "Scalar"]} |
| 4.09 | 3968 | attention | ok | True | `fmhaSm100fKernel_QkvFp16OFp16H128PagedKvCausalP64MultiCtasKvVarSeqQ8Kv128StaticSwapsAbForGen` | timestamp_enclosure: `aten::cat` {"Concrete Inputs": ["", "0"], "Input Dims": [[[640], [59]], []], "Input Strides": [[[1], [1]], []], "Input type": ["TensorList", "Scalar"]} |
| 3.13 | 4464 | moe | missing | True | `void moe_align_block_size_small_batch_expert_kernel<int, 256>(int const*, int*, int*, int*, int, int, unsigned long, bool, int)` | external_id=40318: `Torch-Compiled Region: 5/3` {} |
| 2.58 | 4464 | comm | ok | True | `void (anonymous namespace)::all_reduce_one_shot_push_kernel<float, 8u, true>((anonymous namespace)::AllReducePushData, device::distributed::PushController)` | timestamp_enclosure: `aten::slice` {"Concrete Inputs": ["", "0", "640", "640", "1"], "Input Dims": [[196612], [], [], [], []], "Input Strides": [[1], [], [], [], []], "Input type": ["int", "Scalar", "Scalar", "Sc... |
| 2.07 | 992 | norm | missing | True | `void flashinfer::norm::FusedAddRMSNormKernel<8u, __half>(__half*, __half*, __half*, unsigned int, unsigned int, unsigned int, float, float)` | external_id=40318: `Torch-Compiled Region: 5/3` {} |
| 2.03 | 496 | gemm | missing | True | `void cutlass::Kernel2<cutlass_80_simt_sgemm_64x64_8x5_tn_align1>(cutlass_80_simt_sgemm_64x64_8x5_tn_align1::Params)` | external_id=40318: `Torch-Compiled Region: 5/3` {} |

The CSV/JSON siblings contain full sample metadata and trace paths.
