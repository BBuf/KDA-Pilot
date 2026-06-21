# GLM-5.2 B200 Kernel Interface Task Index

- Generated at: `2026-06-21T03:46:33Z`
- Source capture dir: `glm_52/b200/capture`
- Task count: `21`
- Evidence policy: runtime capture at SGLang kernel Python interfaces.

## Category Counts

| Category | Tasks |
|---|---:|
| `attention` | 1 |
| `cache` | 1 |
| `comm` | 3 |
| `norm` | 3 |
| `other` | 6 |
| `quant_gemm` | 1 |
| `quantization` | 3 |
| `rope` | 1 |
| `sampling` | 2 |

## Tasks

| Task id | Category | Interface | Calls | Variants | Workloads |
|---|---|---|---:|---:|---|
| `jit_kernel_per_token_group_quant_8bit_v2_per_token_group_quant_8bit_v2_custom_op` | `quantization` | `jit_kernel.per_token_group_quant_8bit_v2._per_token_group_quant_8bit_v2_custom_op` | 115949 | 2958 | `random_low`, `random_mid`, `random_high`, `sharegpt_low`, `sharegpt_mid`, `sharegpt_high` |
| `jit_kernel_per_token_group_quant_8bit_v2_per_token_group_quant_8bit_v2` | `quantization` | `jit_kernel.per_token_group_quant_8bit_v2.per_token_group_quant_8bit_v2` | 115949 | 2958 | `random_low`, `random_mid`, `random_high`, `sharegpt_low`, `sharegpt_mid`, `sharegpt_high` |
| `srt_layers_quantization_fp8_kernel_deep_gemm_fp8_fp8_bf16_nt` | `quant_gemm` | `srt.layers.quantization.fp8_kernel.deep_gemm_fp8_fp8_bf16_nt` | 105613 | 1365 | `random_low`, `random_mid`, `random_high`, `sharegpt_low`, `sharegpt_mid`, `sharegpt_high` |
| `sglang_quant_method_fp8_linear_method_apply` | `quantization` | `sglang.quant_method.Fp8LinearMethod.apply` | 105613 | 1365 | `random_low`, `random_mid`, `random_high`, `sharegpt_low`, `sharegpt_mid`, `sharegpt_high` |
| `sgl_kernel_rmsnorm` | `norm` | `sgl_kernel.rmsnorm` | 37098 | 393 | `random_low`, `random_mid`, `random_high`, `sharegpt_low`, `sharegpt_mid`, `sharegpt_high` |
| `sgl_kernel_fused_add_rmsnorm` | `norm` | `sgl_kernel.fused_add_rmsnorm` | 36178 | 131 | `random_low`, `random_mid`, `random_high`, `sharegpt_low`, `sharegpt_mid`, `sharegpt_high` |
| `jit_kernel_activation_run_activation_inplace` | `other` | `jit_kernel.activation._run_activation_inplace` | 25876 | 2448 | `random_low`, `random_mid`, `random_high`, `sharegpt_low`, `sharegpt_mid`, `sharegpt_high` |
| `jit_kernel_rope_apply_rope_inplace` | `rope` | `jit_kernel.rope.apply_rope_inplace` | 25181 | 262 | `random_low`, `random_mid`, `random_high`, `sharegpt_low`, `sharegpt_mid`, `sharegpt_high` |
| `srt_layers_attention_base_attn_backend_attention_backend_forward` | `attention` | `srt.layers.attention.base_attn_backend.AttentionBackend.forward` | 18091 | 456 | `random_low`, `random_mid`, `random_high`, `sharegpt_low`, `sharegpt_mid`, `sharegpt_high` |
| `jit_kernel_grouped_topk_jit_grouped_topk_op` | `sampling` | `jit_kernel.grouped_topk._jit_grouped_topk_op` | 17404 | 131 | `random_low`, `random_mid`, `random_high`, `sharegpt_low`, `sharegpt_mid`, `sharegpt_high` |
| `jit_kernel_hadamard_hadamard_transform` | `other` | `jit_kernel.hadamard.hadamard_transform` | 11336 | 226 | `random_low`, `random_mid`, `random_high`, `sharegpt_low`, `sharegpt_mid`, `sharegpt_high` |
| `jit_kernel_fused_store_index_cache_fused_store_index_k_cache` | `cache` | `jit_kernel.fused_store_index_cache.fused_store_index_k_cache` | 7090 | 131 | `random_low`, `random_mid`, `random_high`, `sharegpt_low`, `sharegpt_mid`, `sharegpt_high` |
| `srt_layers_layernorm_layernorm` | `norm` | `srt.layers.layernorm.layernorm` | 7090 | 131 | `random_low`, `random_mid`, `random_high`, `sharegpt_low`, `sharegpt_mid`, `sharegpt_high` |
| `sgl_kernel_fast_topk_transform_fused` | `sampling` | `sgl_kernel.fast_topk_transform_fused` | 4246 | 247 | `random_low`, `random_mid`, `random_high`, `sharegpt_low`, `sharegpt_mid`, `sharegpt_high` |
| `jit_kernel_all_reduce_get_custom_all_reduce_cls_custom_all_reduce_obj_real_all_reduce` | `comm` | `jit_kernel.all_reduce.get_custom_all_reduce_cls.CustomAllReduceObjReal.all_reduce` | 1936 | 296 | `random_low`, `random_mid`, `random_high`, `sharegpt_low`, `sharegpt_mid`, `sharegpt_high` |
| `srt_distributed_parallel_state_outplace_all_reduce` | `comm` | `srt.distributed.parallel_state.outplace_all_reduce` | 1936 | 296 | `random_low`, `random_mid`, `random_high`, `sharegpt_low`, `sharegpt_mid`, `sharegpt_high` |
| `srt_distributed_parallel_state_reg_all_gather_into_tensor` | `other` | `srt.distributed.parallel_state.reg_all_gather_into_tensor` | 1288 | 312 | `random_low`, `random_mid`, `random_high`, `sharegpt_low`, `sharegpt_mid`, `sharegpt_high` |
| `srt_distributed_parallel_state_reg_reduce_scatter_tensor` | `other` | `srt.distributed.parallel_state.reg_reduce_scatter_tensor` | 504 | 80 | `random_mid`, `random_high`, `sharegpt_mid`, `sharegpt_high` |
| `srt_distributed_parallel_state_inplace_all_reduce` | `comm` | `srt.distributed.parallel_state.inplace_all_reduce` | 192 | 32 | `random_mid`, `random_high`, `sharegpt_mid`, `sharegpt_high` |
| `sgl_kernel_build_tree_kernel_efficient` | `other` | `sgl_kernel.build_tree_kernel_efficient` | 187 | 187 | `random_low`, `random_mid`, `random_high`, `sharegpt_low`, `sharegpt_mid`, `sharegpt_high` |
| `sgl_kernel_verify_tree_greedy` | `other` | `sgl_kernel.verify_tree_greedy` | 187 | 95 | `random_low`, `random_mid`, `random_high`, `sharegpt_low`, `sharegpt_mid`, `sharegpt_high` |
