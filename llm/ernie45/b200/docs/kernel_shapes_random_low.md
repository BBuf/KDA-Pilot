# Kernel Shape Inventory — random_low

- Model: `baidu/ERNIE-4.5-21B-A3B-PT`
- Dataset: `random`
- Concurrency: `low`
- Threshold: GPU kernel name share `> 2.0%`
- Total GPU kernel time: `31.3 ms`
- Trace files: `1`

| % GPU | Calls | Category | Shape | SGLang relevant | Kernel | Shape provenance |
|---:|---:|---|---|---|---|---|
| 37.00 | 486 | moe | missing | True | `fused_moe_kernel` | external_id=219: `Torch-Compiled Region: 4/1` {} |
| 16.50 | 664 | quant_gemm | ok | True | `nvjet_sm100_tst_32x64_64x16_4x1_v_bz_TNN` | nearest_preceding_shape_cpu_op: `aten::resolve_neg` {"Concrete Inputs": [""], "Input Dims": [[1]], "Input Strides": [[1]], "Input type": ["long int"]} |
| 5.83 | 224 | attention | ok | True | `fmhaSm100fKernel_QkvBfloat16OBfloat16H128PagedKvCausalP64MultiCtasKvVarSeqQ8Kv128StaticSwapsAbForGen` | nearest_preceding_shape_cpu_op: `aten::resolve_neg` {"Concrete Inputs": [""], "Input Dims": [[1]], "Input Strides": [[1]], "Input type": ["long int"]} |
| 5.54 | 216 | quant_gemm | ok | True | `nvjet_sm100_tst_64x8_64x16_4x1_v_bz_TNT` | nearest_preceding_shape_cpu_op: `aten::copy_` {"Concrete Inputs": ["", "", "False"], "Input Dims": [[1, 1], [1, 1], []], "Input Strides": [[2048, 1], [1, 1], []], "Input type": ["int", "int", "Scalar"]} |
| 4.34 | 448 | gemm | ok | True | `kernel_cutlass_kernel_flashinfernormkernelsfused_add_rmsnormFusedAddRMSNormKernel_object_at__tensorptrbf16gmemalign128o256025601_tensorptrbf16gmemalign128o256025601_tensorptrbf16gmemalign_0` | nearest_preceding_shape_cpu_op: `aten::resolve_neg` {"Concrete Inputs": [""], "Input Dims": [[1]], "Input Strides": [[1]], "Input type": ["long int"]} |
| 3.01 | 216 | quant_gemm | ok | True | `nvjet_sm100_tst_32x64_64x16_2x1_v_bz_splitK_TNN` | nearest_preceding_shape_cpu_op: `aten::resolve_neg` {"Concrete Inputs": [""], "Input Dims": [[1]], "Input Strides": [[1]], "Input type": ["long int"]} |
| 2.33 | 252 | rope | missing | True | `void (anonymous namespace)::fused_rope_kernel<false, 128l, true, __nv_bfloat16, long, 16u>((anonymous namespace)::FusedRopeParams)` | external_id=219: `Torch-Compiled Region: 4/1` {} |
| 2.25 | 9 | quant_gemm | ok | True | `nvjet_sm100_tst_64x8_64x16_2x1_v_bz_TNT` | nearest_preceding_shape_cpu_op: `aten::copy_` {"Concrete Inputs": ["", "", "True"], "Input Dims": [[1], [1], []], "Input Strides": [[1], [1], []], "Input type": ["long int", "long int", "Scalar"]} |
| 2.10 | 243 | moe | ok | True | `void moe_align_block_size_kernel<int>(int const*, int*, int*, int*, int, int, unsigned long, int*, bool, int, int)` | nearest_preceding_shape_cpu_op: `aten::view` {"Concrete Inputs": ["", "[1]"], "Input Dims": [[1], []], "Input Strides": [[1], []], "Input type": ["long int", "ScalarList"]} |

The CSV/JSON siblings contain full sample metadata and trace paths.
