# Captured shapes for `h200_diffusion_qknorm_rope__multi_shape`

Every row below is a live SGLang diffusion benchmark capture. No analytical fallback shapes are included.

| Preset | Kernel | Tensor shapes | Other args | Evidence |
|---|---|---|---|---|
| qwen | `qknorm_rope.fused_inplace_qknorm_rope` | q=`[4096, 24, 128]/bfloat16C` ; k=`[4096, 24, 128]/bfloat16C` ; q_weight=`[128]/bfloat16C` ; k_weight=`[128]/bfloat16C` ; cos_sin_cache=`[4096, 128]/float32C` ; positions=`[4096]/int64C` | is_neox=`False` ; eps=`1e-06` ; head_dim=`128` ; rope_dim=`128` | ion8-h200 call 1 |
| qwen | `qknorm_rope.fused_inplace_qknorm_rope` | q=`[19, 24, 128]/bfloat16C` ; k=`[19, 24, 128]/bfloat16C` ; q_weight=`[128]/bfloat16C` ; k_weight=`[128]/bfloat16C` ; cos_sin_cache=`[19, 128]/float32C` ; positions=`[19]/int64C` | is_neox=`False` ; eps=`1e-06` ; head_dim=`128` ; rope_dim=`128` | ion8-h200 call 2 |
| qwen | `qknorm_rope.fused_inplace_qknorm_rope` | q=`[47, 24, 128]/bfloat16C` ; k=`[47, 24, 128]/bfloat16C` ; q_weight=`[128]/bfloat16C` ; k_weight=`[128]/bfloat16C` ; cos_sin_cache=`[47, 128]/float32C` ; positions=`[47]/int64C` | is_neox=`False` ; eps=`1e-06` ; head_dim=`128` ; rope_dim=`128` | ion8-h200 call 122 |
| qwen-edit | `qknorm_rope.fused_inplace_qknorm_rope` | q=`[8424, 24, 128]/bfloat16C` ; k=`[8424, 24, 128]/bfloat16C` ; q_weight=`[128]/bfloat16C` ; k_weight=`[128]/bfloat16C` ; cos_sin_cache=`[8424, 128]/float32C` ; positions=`[8424]/int64C` | is_neox=`False` ; eps=`1e-06` ; head_dim=`128` ; rope_dim=`128` | ion8-h200 call 1 |
| qwen-edit | `qknorm_rope.fused_inplace_qknorm_rope` | q=`[195, 24, 128]/bfloat16C` ; k=`[195, 24, 128]/bfloat16C` ; q_weight=`[128]/bfloat16C` ; k_weight=`[128]/bfloat16C` ; cos_sin_cache=`[195, 128]/float32C` ; positions=`[195]/int64C` | is_neox=`False` ; eps=`1e-06` ; head_dim=`128` ; rope_dim=`128` | ion8-h200 call 2 |
| qwen-edit | `qknorm_rope.fused_inplace_qknorm_rope` | q=`[189, 24, 128]/bfloat16C` ; k=`[189, 24, 128]/bfloat16C` ; q_weight=`[128]/bfloat16C` ; k_weight=`[128]/bfloat16C` ; cos_sin_cache=`[189, 128]/float32C` ; positions=`[189]/int64C` | is_neox=`False` ; eps=`1e-06` ; head_dim=`128` ; rope_dim=`128` | ion8-h200 call 122 |
| zimage | `qknorm_rope.fused_inplace_qknorm_rope` | q=`[4096, 30, 128]/bfloat16C` ; k=`[4096, 30, 128]/bfloat16C` ; q_weight=`[128]/bfloat16C` ; k_weight=`[128]/bfloat16C` ; cos_sin_cache=`[4096, 128]/float32C` ; positions=`[4096]/int64C` | is_neox=`False` ; eps=`1e-05` ; head_dim=`128` ; rope_dim=`128` | ion8-h200 call 1 |
| zimage | `qknorm_rope.fused_inplace_qknorm_rope` | q=`[32, 30, 128]/bfloat16C` ; k=`[32, 30, 128]/bfloat16C` ; q_weight=`[128]/bfloat16C` ; k_weight=`[128]/bfloat16C` ; cos_sin_cache=`[32, 128]/float32C` ; positions=`[32]/int64C` | is_neox=`False` ; eps=`1e-05` ; head_dim=`128` ; rope_dim=`128` | ion8-h200 call 3 |
| zimage | `qknorm_rope.fused_inplace_qknorm_rope` | q=`[4128, 30, 128]/bfloat16C` ; k=`[4128, 30, 128]/bfloat16C` ; q_weight=`[128]/bfloat16C` ; k_weight=`[128]/bfloat16C` ; cos_sin_cache=`[4128, 128]/float32C` ; positions=`[4128]/int64C` | is_neox=`False` ; eps=`1e-05` ; head_dim=`128` ; rope_dim=`128` | ion8-h200 call 5 |

Legend: `<shape>/<dtype>/C|NC` where `C`=contiguous, `NC`=non-contiguous.
