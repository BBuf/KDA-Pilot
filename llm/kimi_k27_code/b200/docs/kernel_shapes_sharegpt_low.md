# Kernel Shape Inventory — sharegpt_low

- Model: `moonshotai/Kimi-K2.7-Code`
- Dataset: `sharegpt`
- Concurrency: `low`
- Threshold: GPU kernel name share `> 2.0%`
- Total GPU kernel time: `22300.4 ms`
- Trace files: `8`

| % GPU | Calls | Category | Shape | SGLang relevant | Kernel | Shape provenance |
|---:|---:|---|---|---|---|---|
| 48.82 | 8712 | comm | ok | True | `void flashinfer::trtllm_allreduce_fusion::allreduce_fusion_kernel_oneshot_lamport<(flashinfer::trtllm_allreduce_fusion::AllReduceFusionPattern)1, __nv_bfloat16, 8, false, false>(flashinfer::trtllm_allreduce_fusion::AllReduceFusionParams<__nv_bfloat16>)` | external_id=69995: `sglang::flashinfer_allreduce_residual_rmsnorm` {"Concrete Inputs": ["", "", "", "1.0000000000000001e-05", "2048", "", "False", "False", "False"], "Input Dims": [[15, 7168], [15, 7168], [7168], [], [], [], [], [], []], "Input... |
| 47.74 | 488 | gemm | ok | True | `void fused_a_gemm_kernel<1, 2112, 7168, 16, 16, 256, 12>(__nv_bfloat16*, __nv_bfloat16 const*, __nv_bfloat16 const*, int)` | external_id=70011: `sgl_kernel::dsv3_fused_a_gemm` {"Concrete Inputs": ["", "", ""], "Input Dims": [[15, 2112], [15, 7168], [7168, 2112]], "Input Strides": [[2112, 1], [7168, 1], [1, 7168]], "Input type": ["c10::BFloat16", "c10:... |

The CSV/JSON siblings contain full sample metadata and trace paths.
