# Kernel Shape Inventory — random_mid

- Model: `baidu/ERNIE-4.5-21B-A3B-PT`
- Dataset: `random`
- Concurrency: `mid`
- Threshold: GPU kernel name share `> 2.0%`
- Total GPU kernel time: `142.5 ms`
- Trace files: `1`

| % GPU | Calls | Category | Shape | SGLang relevant | Kernel | Shape provenance |
|---:|---:|---|---|---|---|---|
| 63.38 | 486 | moe | missing | True | `fused_moe_kernel` | external_id=5338: `Torch-Compiled Region: 4/1` {} |
| 6.74 | 84 | quant_gemm | missing | True | `nvjet_sm100_tst_128x256_64x6_2x1_2cta_v_bz_TNT` | external_id=5338: `Torch-Compiled Region: 4/1` {} |
| 4.19 | 27 | quant_gemm | missing | True | `nvjet_sm100_tst_128x256_64x6_2x2_2cta_h_bz_TNT` | external_id=5338: `Torch-Compiled Region: 4/1` {} |
| 2.60 | 498 | quant_gemm | ok | True | `nvjet_sm100_tst_32x64_64x16_4x1_v_bz_TNN` | timestamp_enclosure: `aten::_index_put_impl_` {"Concrete Inputs": ["", "", "", "False", "False"], "Input Dims": [[4097, 131076], [], [32], [], []], "Input Strides": [[131076, 1], [], [1], [], []], "Input type": ["int", "", ... |
| 2.35 | 84 | attention | ok | True | `fmhaSm100fKernel_QkvBfloat16OBfloat16H128PagedKvCausalP64VarSeqQ128Kv128PersistentContext` | external_id=6177: `sglang::unified_attention_with_output` {"Concrete Inputs": ["", "", "", "", "True", "27", "", "", "", "", "", "", ""], "Input Dims": [[11264, 2560], [11264, 4, 128], [11264, 4, 128], [11264, 2560], [], [], [], [], []... |
| 2.16 | 168 | norm | missing | True | `void flashinfer::norm::FusedAddRMSNormKernel<8u, __nv_bfloat16>(__nv_bfloat16*, __nv_bfloat16*, __nv_bfloat16*, unsigned int, unsigned int, unsigned int, float, float)` | external_id=5338: `Torch-Compiled Region: 4/1` {} |

The CSV/JSON siblings contain full sample metadata and trace paths.
