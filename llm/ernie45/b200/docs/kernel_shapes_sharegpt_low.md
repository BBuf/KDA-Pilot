# Kernel Shape Inventory — sharegpt_low

- Model: `baidu/ERNIE-4.5-21B-A3B-PT`
- Dataset: `sharegpt`
- Concurrency: `low`
- Threshold: GPU kernel name share `> 2.0%`
- Total GPU kernel time: `30.6 ms`
- Trace files: `1`

| % GPU | Calls | Category | Shape | SGLang relevant | Kernel | Shape provenance |
|---:|---:|---|---|---|---|---|
| 35.86 | 486 | moe | missing | True | `fused_moe_kernel` | external_id=18651: `Torch-Compiled Region: 4/1` {} |
| 18.05 | 719 | quant_gemm | ok | True | `nvjet_sm100_tst_32x64_64x16_4x1_v_bz_TNN` | nearest_preceding_shape_cpu_op: `aten::resolve_neg` {"Concrete Inputs": [""], "Input Dims": [[1]], "Input Strides": [[1]], "Input type": ["long int"]} |
| 5.96 | 224 | attention | ok | True | `fmhaSm100fKernel_QkvBfloat16OBfloat16H128PagedKvCausalP64MultiCtasKvVarSeqQ8Kv128StaticSwapsAbForGen` | nearest_preceding_shape_cpu_op: `aten::resolve_neg` {"Concrete Inputs": [""], "Input Dims": [[1]], "Input Strides": [[1]], "Input type": ["long int"]} |
| 5.65 | 216 | quant_gemm | ok | True | `nvjet_sm100_tst_64x8_64x16_4x1_v_bz_TNT` | timestamp_enclosure: `aten::index` {"Concrete Inputs": ["", ""], "Input Dims": [[4097], []], "Input Strides": [[1], []], "Input type": ["long int", ""]} |
| 4.46 | 448 | gemm | ok | True | `kernel_cutlass_kernel_flashinfernormkernelsfused_add_rmsnormFusedAddRMSNormKernel_object_at__tensorptrbf16gmemalign128o256025601_tensorptrbf16gmemalign128o256025601_tensorptrbf16gmemalign_0` | nearest_preceding_shape_cpu_op: `aten::resolve_neg` {"Concrete Inputs": [""], "Input Dims": [[1]], "Input Strides": [[1]], "Input type": ["long int"]} |
| 3.07 | 216 | quant_gemm | ok | True | `nvjet_sm100_tst_32x64_64x16_2x1_v_bz_splitK_TNN` | nearest_preceding_shape_cpu_op: `aten::resolve_neg` {"Concrete Inputs": [""], "Input Dims": [[1]], "Input Strides": [[1]], "Input type": ["long int"]} |
| 2.43 | 252 | rope | ok | True | `void (anonymous namespace)::fused_rope_kernel<false, 128l, true, __nv_bfloat16, long, 16u>((anonymous namespace)::FusedRopeParams)` | external_id=18651: `Torch-Compiled Region: 4/1` {} |
| 2.30 | 9 | quant_gemm | ok | True | `nvjet_sm100_tst_64x8_64x16_2x1_v_bz_TNT` | nearest_preceding_shape_cpu_op: `aten::add` {"Concrete Inputs": ["", "", "1"], "Input Dims": [[1], [], []], "Input Strides": [[1], [], []], "Input type": ["int", "long int", "Scalar"]} |
| 2.16 | 243 | moe | ok | True | `void moe_align_block_size_kernel<int>(int const*, int*, int*, int*, int, int, unsigned long, int*, bool, int, int)` | nearest_preceding_shape_cpu_op: `aten::resolve_neg` {"Concrete Inputs": [""], "Input Dims": [[1]], "Input Strides": [[1]], "Input type": ["long int"]} |

The CSV/JSON siblings contain full sample metadata and trace paths.
