# GLM-5.2 B200 Kernel Interface Task Index

- Generated at: `2026-06-21T03:15:29Z`
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
| `quantization__per_token_group_quant_8bit_v2_custom_op__eb1d2152bb` | `quantization` | `jit_kernel.per_token_group_quant_8bit_v2._per_token_group_quant_8bit_v2_custom_op` | 115949 | 2958 | `random_low`, `random_mid`, `random_high`, `sharegpt_low`, `sharegpt_mid`, `sharegpt_high` |
| `quantization__per_token_group_quant_8bit_v2__03c021eb2f` | `quantization` | `jit_kernel.per_token_group_quant_8bit_v2.per_token_group_quant_8bit_v2` | 115949 | 2958 | `random_low`, `random_mid`, `random_high`, `sharegpt_low`, `sharegpt_mid`, `sharegpt_high` |
| `quant_gemm__deep_gemm_fp8_fp8_bf16_nt__f3c54a6228` | `quant_gemm` | `srt.layers.quantization.fp8_kernel.deep_gemm_fp8_fp8_bf16_nt` | 105613 | 1365 | `random_low`, `random_mid`, `random_high`, `sharegpt_low`, `sharegpt_mid`, `sharegpt_high` |
| `quantization__apply__c3f0003e7c` | `quantization` | `sglang.quant_method.Fp8LinearMethod.apply` | 105613 | 1365 | `random_low`, `random_mid`, `random_high`, `sharegpt_low`, `sharegpt_mid`, `sharegpt_high` |
| `norm__rmsnorm__8f7f96efdf` | `norm` | `sgl_kernel.rmsnorm` | 37098 | 393 | `random_low`, `random_mid`, `random_high`, `sharegpt_low`, `sharegpt_mid`, `sharegpt_high` |
| `norm__fused_add_rmsnorm__4e69c34461` | `norm` | `sgl_kernel.fused_add_rmsnorm` | 36178 | 131 | `random_low`, `random_mid`, `random_high`, `sharegpt_low`, `sharegpt_mid`, `sharegpt_high` |
| `other__run_activation_inplace__1ac0230230` | `other` | `jit_kernel.activation._run_activation_inplace` | 25876 | 2448 | `random_low`, `random_mid`, `random_high`, `sharegpt_low`, `sharegpt_mid`, `sharegpt_high` |
| `rope__apply_rope_inplace__9e6515d072` | `rope` | `jit_kernel.rope.apply_rope_inplace` | 25181 | 262 | `random_low`, `random_mid`, `random_high`, `sharegpt_low`, `sharegpt_mid`, `sharegpt_high` |
| `attention__forward__f3dacf0427` | `attention` | `srt.layers.attention.base_attn_backend.AttentionBackend.forward` | 18091 | 456 | `random_low`, `random_mid`, `random_high`, `sharegpt_low`, `sharegpt_mid`, `sharegpt_high` |
| `sampling__jit_grouped_topk_op__5cf9ac8b5b` | `sampling` | `jit_kernel.grouped_topk._jit_grouped_topk_op` | 17404 | 131 | `random_low`, `random_mid`, `random_high`, `sharegpt_low`, `sharegpt_mid`, `sharegpt_high` |
| `other__hadamard_transform__cc31b5dd39` | `other` | `jit_kernel.hadamard.hadamard_transform` | 11336 | 226 | `random_low`, `random_mid`, `random_high`, `sharegpt_low`, `sharegpt_mid`, `sharegpt_high` |
| `cache__fused_store_index_k_cache__b10aa99250` | `cache` | `jit_kernel.fused_store_index_cache.fused_store_index_k_cache` | 7090 | 131 | `random_low`, `random_mid`, `random_high`, `sharegpt_low`, `sharegpt_mid`, `sharegpt_high` |
| `norm__layernorm__d0997fc888` | `norm` | `srt.layers.layernorm.layernorm` | 7090 | 131 | `random_low`, `random_mid`, `random_high`, `sharegpt_low`, `sharegpt_mid`, `sharegpt_high` |
| `sampling__fast_topk_transform_fused__89e0cb0c80` | `sampling` | `sgl_kernel.fast_topk_transform_fused` | 4246 | 247 | `random_low`, `random_mid`, `random_high`, `sharegpt_low`, `sharegpt_mid`, `sharegpt_high` |
| `comm__all_reduce__7daec0f627` | `comm` | `jit_kernel.all_reduce.get_custom_all_reduce_cls.CustomAllReduceObjReal.all_reduce` | 1936 | 296 | `random_low`, `random_mid`, `random_high`, `sharegpt_low`, `sharegpt_mid`, `sharegpt_high` |
| `comm__outplace_all_reduce__14189a6faa` | `comm` | `srt.distributed.parallel_state.outplace_all_reduce` | 1936 | 296 | `random_low`, `random_mid`, `random_high`, `sharegpt_low`, `sharegpt_mid`, `sharegpt_high` |
| `other__reg_all_gather_into_tensor__c94ff4a932` | `other` | `srt.distributed.parallel_state.reg_all_gather_into_tensor` | 1288 | 312 | `random_low`, `random_mid`, `random_high`, `sharegpt_low`, `sharegpt_mid`, `sharegpt_high` |
| `other__reg_reduce_scatter_tensor__5a98408e62` | `other` | `srt.distributed.parallel_state.reg_reduce_scatter_tensor` | 504 | 80 | `random_mid`, `random_high`, `sharegpt_mid`, `sharegpt_high` |
| `comm__inplace_all_reduce__54240e94b1` | `comm` | `srt.distributed.parallel_state.inplace_all_reduce` | 192 | 32 | `random_mid`, `random_high`, `sharegpt_mid`, `sharegpt_high` |
| `other__build_tree_kernel_efficient__c6e1d6a278` | `other` | `sgl_kernel.build_tree_kernel_efficient` | 187 | 187 | `random_low`, `random_mid`, `random_high`, `sharegpt_low`, `sharegpt_mid`, `sharegpt_high` |
| `other__verify_tree_greedy__c247a164f9` | `other` | `sgl_kernel.verify_tree_greedy` | 187 | 95 | `random_low`, `random_mid`, `random_high`, `sharegpt_low`, `sharegpt_mid`, `sharegpt_high` |
