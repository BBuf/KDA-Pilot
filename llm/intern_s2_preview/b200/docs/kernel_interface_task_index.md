# internlm/Intern-S2-Preview-FP8 B200 Kernel Interface Task Index

- Generated at: `2026-06-21T10:26:39Z`
- Model slug: `intern_s2_preview`
- Source capture dir: `/data/bbuf/kda-pilot/llm/intern_s2_preview/b200/capture`
- Task count: `14`
- Evidence policy: runtime capture at SGLang kernel Python interfaces.

## Category Counts

| Category | Tasks |
|---|---:|
| `cache` | 1 |
| `comm` | 4 |
| `moe` | 1 |
| `norm` | 2 |
| `other` | 1 |
| `quant_gemm` | 1 |
| `quantization` | 4 |

## Tasks

| Task id | Category | Interface | Calls | Variants | Workloads |
|---|---|---|---:|---:|---|
| `jit_kernel_per_token_group_quant_8bit_v2_per_token_group_quant_8bit_v2_custom_op` | `quantization` | `jit_kernel.per_token_group_quant_8bit_v2._per_token_group_quant_8bit_v2_custom_op` | 30800 | 496 | `random_low`, `random_mid`, `random_high`, `sharegpt_low`, `sharegpt_mid`, `sharegpt_high` |
| `jit_kernel_per_token_group_quant_8bit_v2_per_token_group_quant_8bit_v2` | `quantization` | `jit_kernel.per_token_group_quant_8bit_v2.per_token_group_quant_8bit_v2` | 30800 | 496 | `random_low`, `random_mid`, `random_high`, `sharegpt_low`, `sharegpt_mid`, `sharegpt_high` |
| `sglang_quant_method_unquantized_linear_method_apply` | `quantization` | `sglang.quant_method.UnquantizedLinearMethod.apply` | 28600 | 496 | `random_low`, `random_mid`, `random_high`, `sharegpt_low`, `sharegpt_mid`, `sharegpt_high` |
| `srt_layers_quantization_fp8_kernel_deep_gemm_fp8_fp8_bf16_nt` | `quant_gemm` | `srt.layers.quantization.fp8_kernel.deep_gemm_fp8_fp8_bf16_nt` | 22000 | 496 | `random_low`, `random_mid`, `random_high`, `sharegpt_low`, `sharegpt_mid`, `sharegpt_high` |
| `sglang_quant_method_fp8_linear_method_apply` | `quantization` | `sglang.quant_method.Fp8LinearMethod.apply` | 22000 | 496 | `random_low`, `random_mid`, `random_high`, `sharegpt_low`, `sharegpt_mid`, `sharegpt_high` |
| `sgl_kernel_gemma_fused_add_rmsnorm` | `norm` | `sgl_kernel.gemma_fused_add_rmsnorm` | 17600 | 124 | `random_low`, `random_mid`, `random_high`, `sharegpt_low`, `sharegpt_mid`, `sharegpt_high` |
| `jit_kernel_all_reduce_get_custom_all_reduce_cls_custom_all_reduce_obj_real_all_reduce` | `comm` | `jit_kernel.all_reduce.get_custom_all_reduce_cls.CustomAllReduceObjReal.all_reduce` | 16200 | 104 | `random_low`, `random_mid`, `random_high`, `sharegpt_low`, `sharegpt_mid`, `sharegpt_high` |
| `srt_distributed_parallel_state_outplace_all_reduce` | `comm` | `srt.distributed.parallel_state.outplace_all_reduce` | 16200 | 104 | `random_low`, `random_mid`, `random_high`, `sharegpt_low`, `sharegpt_mid`, `sharegpt_high` |
| `srt_layers_moe_flashinfer_trtllm_moe_trtllm_fp8_block_scale_moe_wrapper` | `moe` | `srt.layers.moe.flashinfer_trtllm_moe.trtllm_fp8_block_scale_moe_wrapper` | 8800 | 124 | `random_low`, `random_mid`, `random_high`, `sharegpt_low`, `sharegpt_mid`, `sharegpt_high` |
| `jit_kernel_activation_run_activation_inplace` | `other` | `jit_kernel.activation._run_activation_inplace` | 8800 | 124 | `random_low`, `random_mid`, `random_high`, `sharegpt_low`, `sharegpt_mid`, `sharegpt_high` |
| `sgl_kernel_gemma_rmsnorm` | `norm` | `sgl_kernel.gemma_rmsnorm` | 4620 | 372 | `random_low`, `random_mid`, `random_high`, `sharegpt_low`, `sharegpt_mid`, `sharegpt_high` |
| `jit_kernel_kvcache_store_cache` | `cache` | `jit_kernel.kvcache.store_cache` | 2200 | 124 | `random_low`, `random_mid`, `random_high`, `sharegpt_low`, `sharegpt_mid`, `sharegpt_high` |
| `srt_distributed_parallel_state_inplace_all_reduce` | `comm` | `srt.distributed.parallel_state.inplace_all_reduce` | 1620 | 20 | `random_mid`, `random_high`, `sharegpt_mid`, `sharegpt_high` |
| `srt_distributed_parallel_state_reg_all_gather_into_tensor` | `comm` | `srt.distributed.parallel_state.reg_all_gather_into_tensor` | 220 | 116 | `random_low`, `random_mid`, `random_high`, `sharegpt_low`, `sharegpt_mid`, `sharegpt_high` |
