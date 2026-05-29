# Diffusion Shape Ledger (live SGLang benchmark captures)

This ledger contains only shapes captured from real SGLang diffusion benchmark preset runs. Derived/model-config-only shapes are excluded.

## `diffusion_cutedsl_norm_scale_shift__multi_shape`

### `b200`

| Preset | Kernel | Tensor shapes | Other args | Evidence |
|---|---|---|---|---|
| firered-edit-1.0 | `scale_residual_norm_scale_shift.fused_norm_scale_shift` | arg0=`[1, 8424, 3072]/bfloat16C` ; arg3=`[1, 1, 3072]/bfloat16C` ; arg4=`[1, 1, 3072]/bfloat16C` | arg1=`None` ; arg2=`None` ; arg5=`layer` ; arg6=`1e-06` | ion-b200 call 1 |
| firered-edit-1.0 | `scale_residual_norm_scale_shift.fused_scale_residual_norm_scale_shift` | arg0=`[1, 8424, 3072]/bfloat16C` ; arg1=`[1, 8424, 3072]/bfloat16C` ; arg2=`[1, 1, 3072]/bfloat16C` ; arg5=`[1, 1, 3072]/bfloat16C` ; arg6=`[1, 1, 3072]/bfloat16C` | arg3=`None` ; arg4=`None` ; arg7=`layer` ; arg8=`1e-06` | ion-b200 call 1 |
| helios | `scale_residual_norm_scale_shift.fused_norm_scale_shift` | arg0=`[1, 11040, 5120]/bfloat16C` ; arg3=`[1, 11040, 5120]/float32C` ; arg4=`[1, 11040, 5120]/float32C` | arg1=`None` ; arg2=`None` ; arg5=`layer` ; arg6=`1e-06` | ion-b200 call 1 |
| helios | `scale_residual_norm_scale_shift.fused_norm_scale_shift` | arg0=`[1, 8640, 5120]/bfloat16C` ; arg3=`[1, 8640, 5120]/bfloat16C` ; arg4=`[1, 8640, 5120]/bfloat16C` | arg1=`None` ; arg2=`None` ; arg5=`layer` ; arg6=`1e-06` | ion-b200 call 81 |
| hunyuanvideo | `scale_residual_norm_scale_shift.fused_norm_scale_shift` | arg0=`[1, 27030, 3072]/bfloat16C` ; arg3=`[1, 3072]/bfloat16C` ; arg4=`[1, 3072]/bfloat16C` | arg1=`None` ; arg2=`None` ; arg5=`layer` ; arg6=`1e-06` | ion-b200 call 1 |
| hunyuanvideo | `scale_residual_norm_scale_shift.fused_norm_scale_shift` | arg0=`[1, 55, 3072]/bfloat16C` ; arg3=`[1, 3072]/bfloat16C` ; arg4=`[1, 3072]/bfloat16C` | arg1=`None` ; arg2=`None` ; arg5=`layer` ; arg6=`1e-06` | ion-b200 call 2 |
| hunyuanvideo | `scale_residual_norm_scale_shift.fused_norm_scale_shift` | arg0=`[1, 27085, 3072]/bfloat16C` ; arg3=`[1, 3072]/bfloat16C` ; arg4=`[1, 3072]/bfloat16C` | arg1=`None` ; arg2=`None` ; arg5=`layer` ; arg6=`1e-06` | ion-b200 call 41 |
| hunyuanvideo | `scale_residual_norm_scale_shift.fused_scale_residual_norm_scale_shift` | arg0=`[1, 27030, 3072]/bfloat16C` ; arg1=`[1, 27030, 3072]/bfloat16C` ; arg2=`[1, 3072]/bfloat16C` ; arg5=`[1, 3072]/bfloat16C` ; arg6=`[1, 3072]/bfloat16C` | arg3=`None` ; arg4=`None` ; arg7=`layer` ; arg8=`1e-06` | ion-b200 call 1 |
| hunyuanvideo | `scale_residual_norm_scale_shift.fused_scale_residual_norm_scale_shift` | arg0=`[1, 55, 3072]/bfloat16C` ; arg1=`[1, 55, 3072]/bfloat16C` ; arg2=`[1, 3072]/bfloat16C` ; arg5=`[1, 3072]/bfloat16C` ; arg6=`[1, 3072]/bfloat16C` | arg3=`None` ; arg4=`None` ; arg7=`layer` ; arg8=`1e-06` | ion-b200 call 2 |
| joyai-edit | `scale_residual_norm_scale_shift.fused_norm_scale_shift` | arg0=`[1, 7904, 4096]/bfloat16C` ; arg3=`[1, 4096]/bfloat16C` ; arg4=`[1, 4096]/bfloat16C` | arg1=`None` ; arg2=`None` ; arg5=`layer` ; arg6=`1e-06` | ion-b200 call 1 |
| joyai-edit | `scale_residual_norm_scale_shift.fused_norm_scale_shift` | arg0=`[1, 1004, 4096]/bfloat16C` ; arg3=`[1, 4096]/bfloat16C` ; arg4=`[1, 4096]/bfloat16C` | arg1=`None` ; arg2=`None` ; arg5=`layer` ; arg6=`1e-06` | ion-b200 call 2 |
| joyai-edit | `scale_residual_norm_scale_shift.fused_norm_scale_shift` | arg0=`[1, 997, 4096]/bfloat16C` ; arg3=`[1, 4096]/bfloat16C` ; arg4=`[1, 4096]/bfloat16C` | arg1=`None` ; arg2=`None` ; arg5=`layer` ; arg6=`1e-06` | ion-b200 call 2 |
| mova-720p | `scale_residual_norm_scale_shift.fused_norm_scale_shift` | arg0=`[1, 44100, 5120]/bfloat16C` ; arg3=`[1, 1, 5120]/bfloat16C` ; arg4=`[1, 1, 5120]/bfloat16C` | arg1=`None` ; arg2=`None` ; arg5=`layer` ; arg6=`1e-06` | ion-b200 call 1 |
| mova-720p | `scale_residual_norm_scale_shift.fused_norm_scale_shift` | arg0=`[1, 101, 1536]/bfloat16C` ; arg3=`[1, 1, 1536]/bfloat16C` ; arg4=`[1, 1, 1536]/bfloat16C` | arg1=`None` ; arg2=`None` ; arg5=`layer` ; arg6=`1e-06` | ion-b200 call 2 |
| mova-720p | `scale_residual_norm_scale_shift.fused_norm_scale_shift` | arg0=`[1, 176400, 5120]/bfloat16C` ; arg3=`[1, 1, 5120]/bfloat16C` ; arg4=`[1, 1, 5120]/bfloat16C` | arg1=`None` ; arg2=`None` ; arg5=`layer` ; arg6=`1e-06` | ion-b200 call 71 |
| mova-720p | `scale_residual_norm_scale_shift.fused_scale_residual_norm_scale_shift` | arg0=`[1, 44100, 5120]/bfloat16C` ; arg1=`[1, 44100, 5120]/bfloat16C` ; arg5=`[1, 1, 5120]/bfloat16C` ; arg6=`[1, 1, 5120]/bfloat16C` | arg2=`None` ; arg3=`None` ; arg4=`None` ; arg7=`layer` ; arg8=`1e-06` | ion-b200 call 1 |
| mova-720p | `scale_residual_norm_scale_shift.fused_scale_residual_norm_scale_shift` | arg0=`[1, 101, 1536]/bfloat16C` ; arg1=`[1, 101, 1536]/bfloat16C` ; arg5=`[1, 1, 1536]/bfloat16C` ; arg6=`[1, 1, 1536]/bfloat16C` | arg2=`None` ; arg3=`None` ; arg4=`None` ; arg7=`layer` ; arg8=`1e-06` | ion-b200 call 2 |
| qwen | `scale_residual_norm_scale_shift.fused_norm_scale_shift` | arg0=`[1, 4096, 3072]/bfloat16C` ; arg3=`[1, 1, 3072]/bfloat16C` ; arg4=`[1, 1, 3072]/bfloat16C` | arg1=`None` ; arg2=`None` ; arg5=`layer` ; arg6=`1e-06` | ion-b200 call 1 |
| qwen | `scale_residual_norm_scale_shift.fused_norm_scale_shift` | arg0=`[1, 19, 3072]/bfloat16C` ; arg3=`[1, 3072]/bfloat16C` ; arg4=`[1, 3072]/bfloat16C` | arg1=`None` ; arg2=`None` ; arg5=`layer` ; arg6=`1e-06` | ion-b200 call 2 |
| qwen | `scale_residual_norm_scale_shift.fused_norm_scale_shift` | arg0=`[1, 47, 3072]/bfloat16C` ; arg3=`[1, 3072]/bfloat16C` ; arg4=`[1, 3072]/bfloat16C` | arg1=`None` ; arg2=`None` ; arg5=`layer` ; arg6=`1e-06` | ion-b200 call 122 |
| qwen | `scale_residual_norm_scale_shift.fused_scale_residual_norm_scale_shift` | arg0=`[1, 4096, 3072]/bfloat16C` ; arg1=`[1, 4096, 3072]/bfloat16C` ; arg2=`[1, 1, 3072]/bfloat16C` ; arg5=`[1, 1, 3072]/bfloat16C` ; arg6=`[1, 1, 3072]/bfloat16C` | arg3=`None` ; arg4=`None` ; arg7=`layer` ; arg8=`1e-06` | ion-b200 call 1 |
| qwen | `scale_residual_norm_scale_shift.fused_scale_residual_norm_scale_shift` | arg0=`[1, 19, 3072]/bfloat16C` ; arg1=`[1, 19, 3072]/bfloat16C` ; arg2=`[1, 1, 3072]/bfloat16C` ; arg5=`[1, 3072]/bfloat16C` ; arg6=`[1, 3072]/bfloat16C` | arg3=`None` ; arg4=`None` ; arg7=`layer` ; arg8=`1e-06` | ion-b200 call 2 |
| qwen | `scale_residual_norm_scale_shift.fused_scale_residual_norm_scale_shift` | arg0=`[1, 47, 3072]/bfloat16C` ; arg1=`[1, 47, 3072]/bfloat16C` ; arg2=`[1, 1, 3072]/bfloat16C` ; arg5=`[1, 3072]/bfloat16C` ; arg6=`[1, 3072]/bfloat16C` | arg3=`None` ; arg4=`None` ; arg7=`layer` ; arg8=`1e-06` | ion-b200 call 122 |
| qwen-edit | `scale_residual_norm_scale_shift.fused_norm_scale_shift` | arg0=`[1, 195, 3072]/bfloat16C` ; arg3=`[1, 3072]/bfloat16C` ; arg4=`[1, 3072]/bfloat16C` | arg1=`None` ; arg2=`None` ; arg5=`layer` ; arg6=`1e-06` | ion-b200 call 1 |
| qwen-edit | `scale_residual_norm_scale_shift.fused_norm_scale_shift` | arg0=`[1, 189, 3072]/bfloat16C` ; arg3=`[1, 3072]/bfloat16C` ; arg4=`[1, 3072]/bfloat16C` | arg1=`None` ; arg2=`None` ; arg5=`layer` ; arg6=`1e-06` | ion-b200 call 61 |
| qwen-edit | `scale_residual_norm_scale_shift.fused_scale_residual_norm_scale_shift` | arg0=`[1, 195, 3072]/bfloat16C` ; arg1=`[1, 195, 3072]/bfloat16C` ; arg2=`[1, 1, 3072]/bfloat16C` ; arg5=`[1, 3072]/bfloat16C` ; arg6=`[1, 3072]/bfloat16C` | arg3=`None` ; arg4=`None` ; arg7=`layer` ; arg8=`1e-06` | ion-b200 call 1 |
| qwen-edit | `scale_residual_norm_scale_shift.fused_scale_residual_norm_scale_shift` | arg0=`[1, 189, 3072]/bfloat16C` ; arg1=`[1, 189, 3072]/bfloat16C` ; arg2=`[1, 1, 3072]/bfloat16C` ; arg5=`[1, 3072]/bfloat16C` ; arg6=`[1, 3072]/bfloat16C` | arg3=`None` ; arg4=`None` ; arg7=`layer` ; arg8=`1e-06` | ion-b200 call 61 |
| wan-i2v | `scale_residual_norm_scale_shift.fused_norm_scale_shift` | arg0=`[1, 37044, 5120]/bfloat16C` ; arg3=`[1, 1, 5120]/float32C` ; arg4=`[1, 1, 5120]/float32C` | arg1=`None` ; arg2=`None` ; arg5=`layer` ; arg6=`1e-06` | ion-b200 call 1 |
| wan-i2v | `scale_residual_norm_scale_shift.fused_norm_scale_shift` | arg0=`[1, 37044, 5120]/bfloat16C` ; arg3=`[1, 1, 5120]/float32C` ; arg4=`[1, 1, 5120]/float32C` | arg1=`None` ; arg2=`None` ; arg5=`layer` ; arg6=`1e-06` | ion-b200 call 2 |
| wan-i2v | `scale_residual_norm_scale_shift.fused_norm_scale_shift` | arg0=`[1, 74088, 5120]/bfloat16C` ; arg3=`[1, 1, 5120]/bfloat16C` ; arg4=`[1, 1, 5120]/bfloat16C` | arg1=`None` ; arg2=`None` ; arg5=`layer` ; arg6=`1e-06` | ion-b200 call 41 |
| wan-i2v | `scale_residual_norm_scale_shift.fused_scale_residual_norm_scale_shift` | arg0=`[1, 37044, 5120]/bfloat16C` ; arg1=`[1, 37044, 5120]/bfloat16C` ; arg2=`[1, 1, 5120]/float32C` ; arg3=`[5120]/float32C` ; arg4=`[5120]/float32C` ; arg5=`[1]/bfloat16C` ; arg6=`[1]/bfloat16C` | arg7=`layer` ; arg8=`1e-06` | ion-b200 call 1 |
| wan-i2v | `scale_residual_norm_scale_shift.fused_scale_residual_norm_scale_shift` | arg0=`[1, 37044, 5120]/bfloat16C` ; arg1=`[1, 37044, 5120]/bfloat16C` ; arg5=`[1, 1, 5120]/float32C` ; arg6=`[1, 1, 5120]/float32C` | arg2=`None` ; arg3=`None` ; arg4=`None` ; arg7=`layer` ; arg8=`1e-06` | ion-b200 call 2 |
| wan-i2v | `scale_residual_norm_scale_shift.fused_scale_residual_norm_scale_shift` | arg0=`[1, 37044, 5120]/bfloat16C` ; arg1=`[1, 37044, 5120]/bfloat16C` ; arg2=`[1, 1, 5120]/float32C` ; arg3=`[5120]/float32C` ; arg4=`[5120]/float32C` ; arg5=`[1]/bfloat16C` ; arg6=`[1]/bfloat16C` | arg7=`layer` ; arg8=`1e-06` | ion-b200 call 3 |
| wan-t2v | `scale_residual_norm_scale_shift.fused_norm_scale_shift` | arg0=`[1, 37800, 5120]/bfloat16C` ; arg3=`[1, 1, 5120]/float32C` ; arg4=`[1, 1, 5120]/float32C` | arg1=`None` ; arg2=`None` ; arg5=`layer` ; arg6=`1e-06` | ion-b200 call 1 |
| wan-t2v | `scale_residual_norm_scale_shift.fused_norm_scale_shift` | arg0=`[1, 37800, 5120]/bfloat16C` ; arg3=`[1, 1, 5120]/float32C` ; arg4=`[1, 1, 5120]/float32C` | arg1=`None` ; arg2=`None` ; arg5=`layer` ; arg6=`1e-06` | ion-b200 call 2 |
| wan-t2v | `scale_residual_norm_scale_shift.fused_norm_scale_shift` | arg0=`[1, 75600, 5120]/bfloat16C` ; arg3=`[1, 1, 5120]/bfloat16C` ; arg4=`[1, 1, 5120]/bfloat16C` | arg1=`None` ; arg2=`None` ; arg5=`layer` ; arg6=`1e-06` | ion-b200 call 41 |
| wan-t2v | `scale_residual_norm_scale_shift.fused_scale_residual_norm_scale_shift` | arg0=`[1, 37800, 5120]/bfloat16C` ; arg1=`[1, 37800, 5120]/bfloat16C` ; arg2=`[1, 1, 5120]/float32C` ; arg3=`[5120]/float32C` ; arg4=`[5120]/float32C` ; arg5=`[1]/bfloat16C` ; arg6=`[1]/bfloat16C` | arg7=`layer` ; arg8=`1e-06` | ion-b200 call 1 |
| wan-t2v | `scale_residual_norm_scale_shift.fused_scale_residual_norm_scale_shift` | arg0=`[1, 37800, 5120]/bfloat16C` ; arg1=`[1, 37800, 5120]/bfloat16C` ; arg5=`[1, 1, 5120]/float32C` ; arg6=`[1, 1, 5120]/float32C` | arg2=`None` ; arg3=`None` ; arg4=`None` ; arg7=`layer` ; arg8=`1e-06` | ion-b200 call 2 |
| wan-t2v | `scale_residual_norm_scale_shift.fused_scale_residual_norm_scale_shift` | arg0=`[1, 37800, 5120]/bfloat16C` ; arg1=`[1, 37800, 5120]/bfloat16C` ; arg2=`[1, 1, 5120]/float32C` ; arg3=`[5120]/float32C` ; arg4=`[5120]/float32C` ; arg5=`[1]/bfloat16C` ; arg6=`[1]/bfloat16C` | arg7=`layer` ; arg8=`1e-06` | ion-b200 call 3 |
| wan-ti2v | `scale_residual_norm_scale_shift.fused_norm_scale_shift` | arg0=`[1, 18144, 3072]/bfloat16C` ; arg3=`[1, 18144, 3072]/float32C` ; arg4=`[1, 18144, 3072]/float32C` | arg1=`None` ; arg2=`None` ; arg5=`layer` ; arg6=`1e-06` | ion-b200 call 1 |
| wan-ti2v | `scale_residual_norm_scale_shift.fused_norm_scale_shift` | arg0=`[1, 18144, 3072]/bfloat16C` ; arg3=`[1, 18144, 3072]/bfloat16C` ; arg4=`[1, 18144, 3072]/bfloat16C` | arg1=`None` ; arg2=`None` ; arg5=`layer` ; arg6=`1e-06` | ion-b200 call 31 |
| wan-ti2v | `scale_residual_norm_scale_shift.fused_scale_residual_norm_scale_shift` | arg0=`[1, 18144, 3072]/bfloat16C` ; arg1=`[1, 18144, 3072]/bfloat16C` ; arg2=`[1, 18144, 3072]/float32C` ; arg3=`[3072]/float32C` ; arg4=`[3072]/float32C` ; arg5=`[1]/bfloat16C` ; arg6=`[1]/bfloat16C` | arg7=`layer` ; arg8=`1e-06` | ion-b200 call 1 |
| wan-ti2v | `scale_residual_norm_scale_shift.fused_scale_residual_norm_scale_shift` | arg0=`[1, 18144, 3072]/bfloat16C` ; arg1=`[1, 18144, 3072]/bfloat16C` ; arg5=`[1, 18144, 3072]/float32C` ; arg6=`[1, 18144, 3072]/float32C` | arg2=`None` ; arg3=`None` ; arg4=`None` ; arg7=`layer` ; arg8=`1e-06` | ion-b200 call 2 |

### `h200`

| Preset | Kernel | Tensor shapes | Other args | Evidence |
|---|---|---|---|---|
| firered-edit-1.0 | `scale_residual_norm_scale_shift.fused_norm_scale_shift` | arg0=`[1, 8424, 3072]/bfloat16C` ; arg3=`[1, 1, 3072]/bfloat16C` ; arg4=`[1, 1, 3072]/bfloat16C` | arg1=`None` ; arg2=`None` ; arg5=`layer` ; arg6=`1e-06` | ion8-h200 call 1 |
| firered-edit-1.0 | `scale_residual_norm_scale_shift.fused_scale_residual_norm_scale_shift` | arg0=`[1, 8424, 3072]/bfloat16C` ; arg1=`[1, 8424, 3072]/bfloat16C` ; arg2=`[1, 1, 3072]/bfloat16C` ; arg5=`[1, 1, 3072]/bfloat16C` ; arg6=`[1, 1, 3072]/bfloat16C` | arg3=`None` ; arg4=`None` ; arg7=`layer` ; arg8=`1e-06` | ion8-h200 call 1 |
| helios | `scale_residual_norm_scale_shift.fused_norm_scale_shift` | arg0=`[1, 11040, 5120]/bfloat16C` ; arg3=`[1, 11040, 5120]/float32C` ; arg4=`[1, 11040, 5120]/float32C` | arg1=`None` ; arg2=`None` ; arg5=`layer` ; arg6=`1e-06` | ion8-h200 call 1 |
| helios | `scale_residual_norm_scale_shift.fused_norm_scale_shift` | arg0=`[1, 8640, 5120]/bfloat16C` ; arg3=`[1, 8640, 5120]/bfloat16C` ; arg4=`[1, 8640, 5120]/bfloat16C` | arg1=`None` ; arg2=`None` ; arg5=`layer` ; arg6=`1e-06` | ion8-h200 call 81 |
| hunyuanvideo | `scale_residual_norm_scale_shift.fused_norm_scale_shift` | arg0=`[1, 27030, 3072]/bfloat16C` ; arg3=`[1, 3072]/bfloat16C` ; arg4=`[1, 3072]/bfloat16C` | arg1=`None` ; arg2=`None` ; arg5=`layer` ; arg6=`1e-06` | ion8-h200 call 1 |
| hunyuanvideo | `scale_residual_norm_scale_shift.fused_norm_scale_shift` | arg0=`[1, 55, 3072]/bfloat16C` ; arg3=`[1, 3072]/bfloat16C` ; arg4=`[1, 3072]/bfloat16C` | arg1=`None` ; arg2=`None` ; arg5=`layer` ; arg6=`1e-06` | ion8-h200 call 2 |
| hunyuanvideo | `scale_residual_norm_scale_shift.fused_norm_scale_shift` | arg0=`[1, 27085, 3072]/bfloat16C` ; arg3=`[1, 3072]/bfloat16C` ; arg4=`[1, 3072]/bfloat16C` | arg1=`None` ; arg2=`None` ; arg5=`layer` ; arg6=`1e-06` | ion8-h200 call 41 |
| hunyuanvideo | `scale_residual_norm_scale_shift.fused_scale_residual_norm_scale_shift` | arg0=`[1, 27030, 3072]/bfloat16C` ; arg1=`[1, 27030, 3072]/bfloat16C` ; arg2=`[1, 3072]/bfloat16C` ; arg5=`[1, 3072]/bfloat16C` ; arg6=`[1, 3072]/bfloat16C` | arg3=`None` ; arg4=`None` ; arg7=`layer` ; arg8=`1e-06` | ion8-h200 call 1 |
| hunyuanvideo | `scale_residual_norm_scale_shift.fused_scale_residual_norm_scale_shift` | arg0=`[1, 55, 3072]/bfloat16C` ; arg1=`[1, 55, 3072]/bfloat16C` ; arg2=`[1, 3072]/bfloat16C` ; arg5=`[1, 3072]/bfloat16C` ; arg6=`[1, 3072]/bfloat16C` | arg3=`None` ; arg4=`None` ; arg7=`layer` ; arg8=`1e-06` | ion8-h200 call 2 |
| mova-720p | `scale_residual_norm_scale_shift.fused_norm_scale_shift` | arg0=`[1, 44100, 5120]/bfloat16C` ; arg3=`[1, 1, 5120]/bfloat16C` ; arg4=`[1, 1, 5120]/bfloat16C` | arg1=`None` ; arg2=`None` ; arg5=`layer` ; arg6=`1e-06` | ion8-h200 call 1 |
| mova-720p | `scale_residual_norm_scale_shift.fused_norm_scale_shift` | arg0=`[1, 101, 1536]/bfloat16C` ; arg3=`[1, 1, 1536]/bfloat16C` ; arg4=`[1, 1, 1536]/bfloat16C` | arg1=`None` ; arg2=`None` ; arg5=`layer` ; arg6=`1e-06` | ion8-h200 call 2 |
| mova-720p | `scale_residual_norm_scale_shift.fused_norm_scale_shift` | arg0=`[1, 176400, 5120]/bfloat16C` ; arg3=`[1, 1, 5120]/bfloat16C` ; arg4=`[1, 1, 5120]/bfloat16C` | arg1=`None` ; arg2=`None` ; arg5=`layer` ; arg6=`1e-06` | ion8-h200 call 71 |
| mova-720p | `scale_residual_norm_scale_shift.fused_scale_residual_norm_scale_shift` | arg0=`[1, 44100, 5120]/bfloat16C` ; arg1=`[1, 44100, 5120]/bfloat16C` ; arg5=`[1, 1, 5120]/bfloat16C` ; arg6=`[1, 1, 5120]/bfloat16C` | arg2=`None` ; arg3=`None` ; arg4=`None` ; arg7=`layer` ; arg8=`1e-06` | ion8-h200 call 1 |
| mova-720p | `scale_residual_norm_scale_shift.fused_scale_residual_norm_scale_shift` | arg0=`[1, 101, 1536]/bfloat16C` ; arg1=`[1, 101, 1536]/bfloat16C` ; arg5=`[1, 1, 1536]/bfloat16C` ; arg6=`[1, 1, 1536]/bfloat16C` | arg2=`None` ; arg3=`None` ; arg4=`None` ; arg7=`layer` ; arg8=`1e-06` | ion8-h200 call 2 |
| qwen | `scale_residual_norm_scale_shift.fused_norm_scale_shift` | arg0=`[1, 4096, 3072]/bfloat16C` ; arg3=`[1, 1, 3072]/bfloat16C` ; arg4=`[1, 1, 3072]/bfloat16C` | arg1=`None` ; arg2=`None` ; arg5=`layer` ; arg6=`1e-06` | ion8-h200 call 1 |
| qwen | `scale_residual_norm_scale_shift.fused_norm_scale_shift` | arg0=`[1, 19, 3072]/bfloat16C` ; arg3=`[1, 3072]/bfloat16C` ; arg4=`[1, 3072]/bfloat16C` | arg1=`None` ; arg2=`None` ; arg5=`layer` ; arg6=`1e-06` | ion8-h200 call 2 |
| qwen | `scale_residual_norm_scale_shift.fused_norm_scale_shift` | arg0=`[1, 47, 3072]/bfloat16C` ; arg3=`[1, 3072]/bfloat16C` ; arg4=`[1, 3072]/bfloat16C` | arg1=`None` ; arg2=`None` ; arg5=`layer` ; arg6=`1e-06` | ion8-h200 call 122 |
| qwen | `scale_residual_norm_scale_shift.fused_scale_residual_norm_scale_shift` | arg0=`[1, 4096, 3072]/bfloat16C` ; arg1=`[1, 4096, 3072]/bfloat16C` ; arg2=`[1, 1, 3072]/bfloat16C` ; arg5=`[1, 1, 3072]/bfloat16C` ; arg6=`[1, 1, 3072]/bfloat16C` | arg3=`None` ; arg4=`None` ; arg7=`layer` ; arg8=`1e-06` | ion8-h200 call 1 |
| qwen | `scale_residual_norm_scale_shift.fused_scale_residual_norm_scale_shift` | arg0=`[1, 19, 3072]/bfloat16C` ; arg1=`[1, 19, 3072]/bfloat16C` ; arg2=`[1, 1, 3072]/bfloat16C` ; arg5=`[1, 3072]/bfloat16C` ; arg6=`[1, 3072]/bfloat16C` | arg3=`None` ; arg4=`None` ; arg7=`layer` ; arg8=`1e-06` | ion8-h200 call 2 |
| qwen | `scale_residual_norm_scale_shift.fused_scale_residual_norm_scale_shift` | arg0=`[1, 47, 3072]/bfloat16C` ; arg1=`[1, 47, 3072]/bfloat16C` ; arg2=`[1, 1, 3072]/bfloat16C` ; arg5=`[1, 3072]/bfloat16C` ; arg6=`[1, 3072]/bfloat16C` | arg3=`None` ; arg4=`None` ; arg7=`layer` ; arg8=`1e-06` | ion8-h200 call 122 |
| qwen-edit | `scale_residual_norm_scale_shift.fused_norm_scale_shift` | arg0=`[1, 195, 3072]/bfloat16C` ; arg3=`[1, 3072]/bfloat16C` ; arg4=`[1, 3072]/bfloat16C` | arg1=`None` ; arg2=`None` ; arg5=`layer` ; arg6=`1e-06` | ion8-h200 call 1 |
| qwen-edit | `scale_residual_norm_scale_shift.fused_norm_scale_shift` | arg0=`[1, 189, 3072]/bfloat16C` ; arg3=`[1, 3072]/bfloat16C` ; arg4=`[1, 3072]/bfloat16C` | arg1=`None` ; arg2=`None` ; arg5=`layer` ; arg6=`1e-06` | ion8-h200 call 61 |
| qwen-edit | `scale_residual_norm_scale_shift.fused_scale_residual_norm_scale_shift` | arg0=`[1, 195, 3072]/bfloat16C` ; arg1=`[1, 195, 3072]/bfloat16C` ; arg2=`[1, 1, 3072]/bfloat16C` ; arg5=`[1, 3072]/bfloat16C` ; arg6=`[1, 3072]/bfloat16C` | arg3=`None` ; arg4=`None` ; arg7=`layer` ; arg8=`1e-06` | ion8-h200 call 1 |
| qwen-edit | `scale_residual_norm_scale_shift.fused_scale_residual_norm_scale_shift` | arg0=`[1, 189, 3072]/bfloat16C` ; arg1=`[1, 189, 3072]/bfloat16C` ; arg2=`[1, 1, 3072]/bfloat16C` ; arg5=`[1, 3072]/bfloat16C` ; arg6=`[1, 3072]/bfloat16C` | arg3=`None` ; arg4=`None` ; arg7=`layer` ; arg8=`1e-06` | ion8-h200 call 61 |
| wan-i2v | `scale_residual_norm_scale_shift.fused_norm_scale_shift` | arg0=`[1, 37044, 5120]/bfloat16C` ; arg3=`[1, 1, 5120]/float32C` ; arg4=`[1, 1, 5120]/float32C` | arg1=`None` ; arg2=`None` ; arg5=`layer` ; arg6=`1e-06` | ion8-h200 call 1 |
| wan-i2v | `scale_residual_norm_scale_shift.fused_norm_scale_shift` | arg0=`[1, 37044, 5120]/bfloat16C` ; arg3=`[1, 1, 5120]/float32C` ; arg4=`[1, 1, 5120]/float32C` | arg1=`None` ; arg2=`None` ; arg5=`layer` ; arg6=`1e-06` | ion8-h200 call 2 |
| wan-i2v | `scale_residual_norm_scale_shift.fused_norm_scale_shift` | arg0=`[1, 74088, 5120]/bfloat16C` ; arg3=`[1, 1, 5120]/bfloat16C` ; arg4=`[1, 1, 5120]/bfloat16C` | arg1=`None` ; arg2=`None` ; arg5=`layer` ; arg6=`1e-06` | ion8-h200 call 41 |
| wan-i2v | `scale_residual_norm_scale_shift.fused_scale_residual_norm_scale_shift` | arg0=`[1, 37044, 5120]/bfloat16C` ; arg1=`[1, 37044, 5120]/bfloat16C` ; arg2=`[1, 1, 5120]/float32C` ; arg3=`[5120]/float32C` ; arg4=`[5120]/float32C` ; arg5=`[1]/bfloat16C` ; arg6=`[1]/bfloat16C` | arg7=`layer` ; arg8=`1e-06` | ion8-h200 call 1 |
| wan-i2v | `scale_residual_norm_scale_shift.fused_scale_residual_norm_scale_shift` | arg0=`[1, 37044, 5120]/bfloat16C` ; arg1=`[1, 37044, 5120]/bfloat16C` ; arg5=`[1, 1, 5120]/float32C` ; arg6=`[1, 1, 5120]/float32C` | arg2=`None` ; arg3=`None` ; arg4=`None` ; arg7=`layer` ; arg8=`1e-06` | ion8-h200 call 2 |
| wan-i2v | `scale_residual_norm_scale_shift.fused_scale_residual_norm_scale_shift` | arg0=`[1, 37044, 5120]/bfloat16C` ; arg1=`[1, 37044, 5120]/bfloat16C` ; arg2=`[1, 1, 5120]/float32C` ; arg3=`[5120]/float32C` ; arg4=`[5120]/float32C` ; arg5=`[1]/bfloat16C` ; arg6=`[1]/bfloat16C` | arg7=`layer` ; arg8=`1e-06` | ion8-h200 call 3 |
| wan-t2v | `scale_residual_norm_scale_shift.fused_norm_scale_shift` | arg0=`[1, 37800, 5120]/bfloat16C` ; arg3=`[1, 1, 5120]/float32C` ; arg4=`[1, 1, 5120]/float32C` | arg1=`None` ; arg2=`None` ; arg5=`layer` ; arg6=`1e-06` | ion8-h200 call 1 |
| wan-t2v | `scale_residual_norm_scale_shift.fused_norm_scale_shift` | arg0=`[1, 37800, 5120]/bfloat16C` ; arg3=`[1, 1, 5120]/float32C` ; arg4=`[1, 1, 5120]/float32C` | arg1=`None` ; arg2=`None` ; arg5=`layer` ; arg6=`1e-06` | ion8-h200 call 2 |
| wan-t2v | `scale_residual_norm_scale_shift.fused_norm_scale_shift` | arg0=`[1, 75600, 5120]/bfloat16C` ; arg3=`[1, 1, 5120]/bfloat16C` ; arg4=`[1, 1, 5120]/bfloat16C` | arg1=`None` ; arg2=`None` ; arg5=`layer` ; arg6=`1e-06` | ion8-h200 call 41 |
| wan-t2v | `scale_residual_norm_scale_shift.fused_scale_residual_norm_scale_shift` | arg0=`[1, 37800, 5120]/bfloat16C` ; arg1=`[1, 37800, 5120]/bfloat16C` ; arg2=`[1, 1, 5120]/float32C` ; arg3=`[5120]/float32C` ; arg4=`[5120]/float32C` ; arg5=`[1]/bfloat16C` ; arg6=`[1]/bfloat16C` | arg7=`layer` ; arg8=`1e-06` | ion8-h200 call 1 |
| wan-t2v | `scale_residual_norm_scale_shift.fused_scale_residual_norm_scale_shift` | arg0=`[1, 37800, 5120]/bfloat16C` ; arg1=`[1, 37800, 5120]/bfloat16C` ; arg5=`[1, 1, 5120]/float32C` ; arg6=`[1, 1, 5120]/float32C` | arg2=`None` ; arg3=`None` ; arg4=`None` ; arg7=`layer` ; arg8=`1e-06` | ion8-h200 call 2 |
| wan-t2v | `scale_residual_norm_scale_shift.fused_scale_residual_norm_scale_shift` | arg0=`[1, 37800, 5120]/bfloat16C` ; arg1=`[1, 37800, 5120]/bfloat16C` ; arg2=`[1, 1, 5120]/float32C` ; arg3=`[5120]/float32C` ; arg4=`[5120]/float32C` ; arg5=`[1]/bfloat16C` ; arg6=`[1]/bfloat16C` | arg7=`layer` ; arg8=`1e-06` | ion8-h200 call 3 |
| wan-ti2v | `scale_residual_norm_scale_shift.fused_norm_scale_shift` | arg0=`[1, 18144, 3072]/bfloat16C` ; arg3=`[1, 18144, 3072]/float32C` ; arg4=`[1, 18144, 3072]/float32C` | arg1=`None` ; arg2=`None` ; arg5=`layer` ; arg6=`1e-06` | ion8-h200 call 1 |
| wan-ti2v | `scale_residual_norm_scale_shift.fused_norm_scale_shift` | arg0=`[1, 18144, 3072]/bfloat16C` ; arg3=`[1, 18144, 3072]/bfloat16C` ; arg4=`[1, 18144, 3072]/bfloat16C` | arg1=`None` ; arg2=`None` ; arg5=`layer` ; arg6=`1e-06` | ion8-h200 call 31 |
| wan-ti2v | `scale_residual_norm_scale_shift.fused_scale_residual_norm_scale_shift` | arg0=`[1, 18144, 3072]/bfloat16C` ; arg1=`[1, 18144, 3072]/bfloat16C` ; arg2=`[1, 18144, 3072]/float32C` ; arg3=`[3072]/float32C` ; arg4=`[3072]/float32C` ; arg5=`[1]/bfloat16C` ; arg6=`[1]/bfloat16C` | arg7=`layer` ; arg8=`1e-06` | ion8-h200 call 1 |
| wan-ti2v | `scale_residual_norm_scale_shift.fused_scale_residual_norm_scale_shift` | arg0=`[1, 18144, 3072]/bfloat16C` ; arg1=`[1, 18144, 3072]/bfloat16C` ; arg5=`[1, 18144, 3072]/float32C` ; arg6=`[1, 18144, 3072]/float32C` | arg2=`None` ; arg3=`None` ; arg4=`None` ; arg7=`layer` ; arg8=`1e-06` | ion8-h200 call 2 |

## `diffusion_cutedsl_norm_tanh_mul_add__multi_shape`

### `b200`

| Preset | Kernel | Tensor shapes | Other args | Evidence |
|---|---|---|---|---|
| zimage | `norm_tanh_mul_add_norm_scale.fused_norm_tanh_mul_add` | arg0=`[1, 4096, 3840]/bfloat16C` ; arg1=`[3840]/bfloat16C` ; arg3=`[1, 1, 3840]/bfloat16C` ; arg4=`[1, 4096, 3840]/bfloat16C` | arg2=`None` ; arg5=`rms` ; arg6=`1e-05` | ion-b200 call 1 |
| zimage | `norm_tanh_mul_add_norm_scale.fused_norm_tanh_mul_add` | arg0=`[1, 4128, 3840]/bfloat16C` ; arg1=`[3840]/bfloat16C` ; arg3=`[1, 1, 3840]/bfloat16C` ; arg4=`[1, 4128, 3840]/bfloat16C` | arg2=`None` ; arg5=`rms` ; arg6=`1e-05` | ion-b200 call 3 |
| zimage | `norm_tanh_mul_add_norm_scale.fused_norm_tanh_mul_add_norm_scale` | arg0=`[1, 4096, 3840]/bfloat16C` ; arg1=`[3840]/bfloat16C` ; arg3=`[1, 1, 3840]/bfloat16C` ; arg4=`[1, 4096, 3840]/bfloat16C` ; arg5=`[3840]/bfloat16C` ; arg7=`[1, 1, 3840]/bfloat16C` | arg2=`None` ; arg6=`None` ; arg8=`rms` ; arg9=`1e-05` | ion-b200 call 1 |
| zimage | `norm_tanh_mul_add_norm_scale.fused_norm_tanh_mul_add_norm_scale` | arg0=`[1, 4128, 3840]/bfloat16C` ; arg1=`[3840]/bfloat16C` ; arg3=`[1, 1, 3840]/bfloat16C` ; arg4=`[1, 4128, 3840]/bfloat16C` ; arg5=`[3840]/bfloat16C` ; arg7=`[1, 1, 3840]/bfloat16C` | arg2=`None` ; arg6=`None` ; arg8=`rms` ; arg9=`1e-05` | ion-b200 call 3 |

### `h200`

| Preset | Kernel | Tensor shapes | Other args | Evidence |
|---|---|---|---|---|
| zimage | `norm_tanh_mul_add_norm_scale.fused_norm_tanh_mul_add` | arg0=`[1, 4096, 3840]/bfloat16C` ; arg1=`[3840]/bfloat16C` ; arg3=`[1, 1, 3840]/bfloat16C` ; arg4=`[1, 4096, 3840]/bfloat16C` | arg2=`None` ; arg5=`rms` ; arg6=`1e-05` | ion8-h200 call 1 |
| zimage | `norm_tanh_mul_add_norm_scale.fused_norm_tanh_mul_add` | arg0=`[1, 4128, 3840]/bfloat16C` ; arg1=`[3840]/bfloat16C` ; arg3=`[1, 1, 3840]/bfloat16C` ; arg4=`[1, 4128, 3840]/bfloat16C` | arg2=`None` ; arg5=`rms` ; arg6=`1e-05` | ion8-h200 call 3 |
| zimage | `norm_tanh_mul_add_norm_scale.fused_norm_tanh_mul_add_norm_scale` | arg0=`[1, 4096, 3840]/bfloat16C` ; arg1=`[3840]/bfloat16C` ; arg3=`[1, 1, 3840]/bfloat16C` ; arg4=`[1, 4096, 3840]/bfloat16C` ; arg5=`[3840]/bfloat16C` ; arg7=`[1, 1, 3840]/bfloat16C` | arg2=`None` ; arg6=`None` ; arg8=`rms` ; arg9=`1e-05` | ion8-h200 call 1 |
| zimage | `norm_tanh_mul_add_norm_scale.fused_norm_tanh_mul_add_norm_scale` | arg0=`[1, 4128, 3840]/bfloat16C` ; arg1=`[3840]/bfloat16C` ; arg3=`[1, 1, 3840]/bfloat16C` ; arg4=`[1, 4128, 3840]/bfloat16C` ; arg5=`[3840]/bfloat16C` ; arg7=`[1, 1, 3840]/bfloat16C` | arg2=`None` ; arg6=`None` ; arg8=`rms` ; arg9=`1e-05` | ion8-h200 call 3 |

## `diffusion_fuse_scale_shift__multi_shape`

### `b200`

| Preset | Kernel | Tensor shapes | Other args | Evidence |
|---|---|---|---|---|
| firered-edit-1.0 | `scale_shift.fuse_scale_shift_kernel` | arg0=`[1, 8424, 3072]/bfloat16C` ; arg1=`[1, 1, 3072]/bfloat16C` ; arg2=`[1, 8424, 3072]/bfloat16C` | scale_constant=`0` | ion-b200 call 1 |
| hunyuanvideo | `scale_shift.fuse_scale_shift_kernel` | arg0=`[1, 27030, 3072]/bfloat16C` ; arg1=`[1, 3072]/bfloat16C` ; arg2=`[1, 27030, 3072]/bfloat16C` | scale_constant=`0` | ion-b200 call 1 |
| hunyuanvideo | `scale_shift.fuse_scale_shift_kernel` | arg0=`[1, 55, 3072]/bfloat16C` ; arg1=`[1, 3072]/bfloat16C` ; arg2=`[1, 55, 3072]/bfloat16C` | scale_constant=`0` | ion-b200 call 2 |
| hunyuanvideo | `scale_shift.fuse_scale_shift_kernel` | arg0=`[1, 27085, 3072]/bfloat16C` ; arg1=`[1, 3072]/bfloat16C` ; arg2=`[1, 27085, 3072]/bfloat16C` | scale_constant=`0` | ion-b200 call 41 |
| qwen | `scale_shift.fuse_scale_shift_kernel` | arg0=`[1, 4096, 3072]/bfloat16C` ; arg1=`[1, 1, 3072]/bfloat16C` ; arg2=`[1, 4096, 3072]/bfloat16C` | scale_constant=`0` | ion-b200 call 1 |
| qwen | `scale_shift.fuse_scale_shift_kernel` | arg0=`[1, 19, 3072]/bfloat16C` ; arg1=`[1, 1, 3072]/bfloat16C` ; arg2=`[1, 19, 3072]/bfloat16C` | scale_constant=`0` | ion-b200 call 2 |
| qwen | `scale_shift.fuse_scale_shift_kernel` | arg0=`[1, 47, 3072]/bfloat16C` ; arg1=`[1, 1, 3072]/bfloat16C` ; arg2=`[1, 47, 3072]/bfloat16C` | scale_constant=`0` | ion-b200 call 122 |
| qwen-edit | `scale_shift.fuse_layernorm_scale_shift_gate_select01_kernel` | arg0=`[1, 8424, 3072]/bfloat16C` ; scale0=`[1, 3072]/bfloat16C` ; shift0=`[1, 3072]/bfloat16C` ; gate0=`[1, 3072]/bfloat16C` ; scale1=`[1, 3072]/bfloat16C` ; shift1=`[1, 3072]/bfloat16C` ; gate1=`[1, 3072]/bfloat16C` ; index=`[1, 8424]/int32C` | weight=`None` ; bias=`None` ; eps=`1e-06` | ion-b200 call 1 |
| qwen-edit | `scale_shift.fuse_residual_layernorm_scale_shift_gate_select01_kernel` | arg0=`[1, 8424, 3072]/bfloat16C` ; residual=`[1, 8424, 3072]/bfloat16C` ; residual_gate=`[1, 8424, 3072]/bfloat16C` ; scale0=`[1, 3072]/bfloat16C` ; shift0=`[1, 3072]/bfloat16C` ; gate0=`[1, 3072]/bfloat16C` ; scale1=`[1, 3072]/bfloat16C` ; shift1=`[1, 3072]/bfloat16C` ; gate1=`[1, 3072]/bfloat16C` ; index=`[1, 8424]/int32C` | weight=`None` ; bias=`None` ; eps=`1e-06` | ion-b200 call 1 |
| qwen-edit | `scale_shift.fuse_scale_shift_kernel` | arg0=`[1, 8424, 3072]/bfloat16C` ; arg1=`[1, 8424, 3072]/bfloat16C` ; arg2=`[1, 8424, 3072]/bfloat16C` | scale_constant=`0` | ion-b200 call 1 |
| qwen-edit | `scale_shift.fuse_scale_shift_kernel` | arg0=`[1, 195, 3072]/bfloat16C` ; arg1=`[1, 1, 3072]/bfloat16C` ; arg2=`[1, 195, 3072]/bfloat16C` | scale_constant=`0` | ion-b200 call 2 |
| qwen-edit | `scale_shift.fuse_scale_shift_kernel` | arg0=`[1, 189, 3072]/bfloat16C` ; arg1=`[1, 1, 3072]/bfloat16C` ; arg2=`[1, 189, 3072]/bfloat16C` | scale_constant=`0` | ion-b200 call 122 |
| wan-i2v | `scale_shift.fuse_scale_shift_kernel` | arg0=`[1, 37044, 5120]/bfloat16C` ; arg1=`[1, 1, 5120]/float32C` ; arg2=`[1, 37044, 5120]/bfloat16C` | scale_constant=`0` | ion-b200 call 1 |
| wan-t2v | `scale_shift.fuse_scale_shift_kernel` | arg0=`[1, 37800, 5120]/bfloat16C` ; arg1=`[1, 1, 5120]/float32C` ; arg2=`[1, 37800, 5120]/bfloat16C` | scale_constant=`0` | ion-b200 call 1 |
| wan-ti2v | `scale_shift.fuse_scale_shift_kernel` | arg0=`[1, 18144, 3072]/bfloat16C` ; arg1=`[1, 18144, 3072]/float32NC` ; arg2=`[1, 18144, 3072]/bfloat16C` | scale_constant=`0` | ion-b200 call 1 |

### `h200`

| Preset | Kernel | Tensor shapes | Other args | Evidence |
|---|---|---|---|---|
| firered-edit-1.0 | `scale_shift.fuse_scale_shift_kernel` | arg0=`[1, 8424, 3072]/bfloat16C` ; arg1=`[1, 1, 3072]/bfloat16C` ; arg2=`[1, 8424, 3072]/bfloat16C` | scale_constant=`0` | ion8-h200 call 1 |
| hunyuanvideo | `scale_shift.fuse_scale_shift_kernel` | arg0=`[1, 27030, 3072]/bfloat16C` ; arg1=`[1, 3072]/bfloat16C` ; arg2=`[1, 27030, 3072]/bfloat16C` | scale_constant=`0` | ion8-h200 call 1 |
| hunyuanvideo | `scale_shift.fuse_scale_shift_kernel` | arg0=`[1, 55, 3072]/bfloat16C` ; arg1=`[1, 3072]/bfloat16C` ; arg2=`[1, 55, 3072]/bfloat16C` | scale_constant=`0` | ion8-h200 call 2 |
| hunyuanvideo | `scale_shift.fuse_scale_shift_kernel` | arg0=`[1, 27085, 3072]/bfloat16C` ; arg1=`[1, 3072]/bfloat16C` ; arg2=`[1, 27085, 3072]/bfloat16C` | scale_constant=`0` | ion8-h200 call 41 |
| qwen | `scale_shift.fuse_scale_shift_kernel` | arg0=`[1, 4096, 3072]/bfloat16C` ; arg1=`[1, 1, 3072]/bfloat16C` ; arg2=`[1, 4096, 3072]/bfloat16C` | scale_constant=`0` | ion8-h200 call 1 |
| qwen | `scale_shift.fuse_scale_shift_kernel` | arg0=`[1, 19, 3072]/bfloat16C` ; arg1=`[1, 1, 3072]/bfloat16C` ; arg2=`[1, 19, 3072]/bfloat16C` | scale_constant=`0` | ion8-h200 call 2 |
| qwen | `scale_shift.fuse_scale_shift_kernel` | arg0=`[1, 47, 3072]/bfloat16C` ; arg1=`[1, 1, 3072]/bfloat16C` ; arg2=`[1, 47, 3072]/bfloat16C` | scale_constant=`0` | ion8-h200 call 122 |
| qwen-edit | `scale_shift.fuse_layernorm_scale_shift_gate_select01_kernel` | arg0=`[1, 8424, 3072]/bfloat16C` ; scale0=`[1, 3072]/bfloat16C` ; shift0=`[1, 3072]/bfloat16C` ; gate0=`[1, 3072]/bfloat16C` ; scale1=`[1, 3072]/bfloat16C` ; shift1=`[1, 3072]/bfloat16C` ; gate1=`[1, 3072]/bfloat16C` ; index=`[1, 8424]/int32C` | weight=`None` ; bias=`None` ; eps=`1e-06` | ion8-h200 call 1 |
| qwen-edit | `scale_shift.fuse_residual_layernorm_scale_shift_gate_select01_kernel` | arg0=`[1, 8424, 3072]/bfloat16C` ; residual=`[1, 8424, 3072]/bfloat16C` ; residual_gate=`[1, 8424, 3072]/bfloat16C` ; scale0=`[1, 3072]/bfloat16C` ; shift0=`[1, 3072]/bfloat16C` ; gate0=`[1, 3072]/bfloat16C` ; scale1=`[1, 3072]/bfloat16C` ; shift1=`[1, 3072]/bfloat16C` ; gate1=`[1, 3072]/bfloat16C` ; index=`[1, 8424]/int32C` | weight=`None` ; bias=`None` ; eps=`1e-06` | ion8-h200 call 1 |
| qwen-edit | `scale_shift.fuse_scale_shift_kernel` | arg0=`[1, 8424, 3072]/bfloat16C` ; arg1=`[1, 8424, 3072]/bfloat16C` ; arg2=`[1, 8424, 3072]/bfloat16C` | scale_constant=`0` | ion8-h200 call 1 |
| qwen-edit | `scale_shift.fuse_scale_shift_kernel` | arg0=`[1, 195, 3072]/bfloat16C` ; arg1=`[1, 1, 3072]/bfloat16C` ; arg2=`[1, 195, 3072]/bfloat16C` | scale_constant=`0` | ion8-h200 call 2 |
| qwen-edit | `scale_shift.fuse_scale_shift_kernel` | arg0=`[1, 189, 3072]/bfloat16C` ; arg1=`[1, 1, 3072]/bfloat16C` ; arg2=`[1, 189, 3072]/bfloat16C` | scale_constant=`0` | ion8-h200 call 122 |
| wan-i2v | `scale_shift.fuse_scale_shift_kernel` | arg0=`[1, 37044, 5120]/bfloat16C` ; arg1=`[1, 1, 5120]/float32C` ; arg2=`[1, 37044, 5120]/bfloat16C` | scale_constant=`0` | ion8-h200 call 1 |
| wan-t2v | `scale_shift.fuse_scale_shift_kernel` | arg0=`[1, 37800, 5120]/bfloat16C` ; arg1=`[1, 1, 5120]/float32C` ; arg2=`[1, 37800, 5120]/bfloat16C` | scale_constant=`0` | ion8-h200 call 1 |
| wan-ti2v | `scale_shift.fuse_scale_shift_kernel` | arg0=`[1, 18144, 3072]/bfloat16C` ; arg1=`[1, 18144, 3072]/float32NC` ; arg2=`[1, 18144, 3072]/bfloat16C` | scale_constant=`0` | ion8-h200 call 1 |

## `diffusion_group_norm_silu__multi_shape`

### `b200`

| Preset | Kernel | Tensor shapes | Other args | Evidence |
|---|---|---|---|---|
| hunyuanvideo | `group_norm_silu.apply_group_norm_silu` | arg0=`[1, 512, 5, 32, 32]/float16C` | arg1=`<GroupNorm>` ; arg2=`<SiLU>` | ion-b200 call 1 |
| hunyuanvideo | `group_norm_silu.apply_group_norm_silu` | arg0=`[1, 512, 5, 32, 32]/float16NC` | arg1=`<GroupNorm>` ; arg2=`<SiLU>` | ion-b200 call 2 |
| hunyuanvideo | `group_norm_silu.apply_group_norm_silu` | arg0=`[1, 512, 5, 64, 64]/float16C` | arg1=`<GroupNorm>` ; arg2=`<SiLU>` | ion-b200 call 11 |
| hunyuanvideo | `group_norm_silu.apply_group_norm_silu` | arg0=`[1, 512, 5, 64, 64]/float16NC` | arg1=`<GroupNorm>` ; arg2=`<SiLU>` | ion-b200 call 12 |
| hunyuanvideo | `group_norm_silu.apply_group_norm_silu` | arg0=`[1, 512, 9, 128, 128]/float16C` | arg1=`<GroupNorm>` ; arg2=`<SiLU>` | ion-b200 call 17 |
| hunyuanvideo | `group_norm_silu.apply_group_norm_silu` | arg0=`[1, 256, 9, 128, 128]/float16NC` | arg1=`<GroupNorm>` ; arg2=`<SiLU>` | ion-b200 call 18 |
| hunyuanvideo | `group_norm_silu.apply_group_norm_silu` | arg0=`[1, 256, 9, 128, 128]/float16C` | arg1=`<GroupNorm>` ; arg2=`<SiLU>` | ion-b200 call 19 |
| hunyuanvideo | `group_norm_silu.apply_group_norm_silu` | arg0=`[1, 256, 17, 256, 256]/float16C` | arg1=`<GroupNorm>` ; arg2=`<SiLU>` | ion-b200 call 23 |
| hunyuanvideo | `group_norm_silu.apply_group_norm_silu` | arg0=`[1, 128, 17, 256, 256]/float16NC` | arg1=`<GroupNorm>` ; arg2=`<SiLU>` | ion-b200 call 24 |
| hunyuanvideo | `group_norm_silu.apply_group_norm_silu` | arg0=`[1, 128, 17, 256, 256]/float16C` | arg1=`<GroupNorm>` ; arg2=`<SiLU>` | ion-b200 call 25 |
| hunyuanvideo | `group_norm_silu.apply_group_norm_silu` | arg0=`[1, 512, 5, 32, 10]/float16C` | arg1=`<GroupNorm>` ; arg2=`<SiLU>` | ion-b200 call 117 |
| hunyuanvideo | `group_norm_silu.apply_group_norm_silu` | arg0=`[1, 512, 5, 32, 10]/float16NC` | arg1=`<GroupNorm>` ; arg2=`<SiLU>` | ion-b200 call 118 |
| hunyuanvideo | `group_norm_silu.apply_group_norm_silu` | arg0=`[1, 512, 5, 64, 20]/float16C` | arg1=`<GroupNorm>` ; arg2=`<SiLU>` | ion-b200 call 127 |
| hunyuanvideo | `group_norm_silu.apply_group_norm_silu` | arg0=`[1, 512, 5, 64, 20]/float16NC` | arg1=`<GroupNorm>` ; arg2=`<SiLU>` | ion-b200 call 128 |
| hunyuanvideo | `group_norm_silu.apply_group_norm_silu` | arg0=`[1, 512, 9, 128, 40]/float16C` | arg1=`<GroupNorm>` ; arg2=`<SiLU>` | ion-b200 call 133 |
| hunyuanvideo | `group_norm_silu.apply_group_norm_silu` | arg0=`[1, 256, 9, 128, 40]/float16NC` | arg1=`<GroupNorm>` ; arg2=`<SiLU>` | ion-b200 call 134 |
| hunyuanvideo | `group_norm_silu.apply_group_norm_silu` | arg0=`[1, 256, 9, 128, 40]/float16C` | arg1=`<GroupNorm>` ; arg2=`<SiLU>` | ion-b200 call 135 |
| hunyuanvideo | `group_norm_silu.apply_group_norm_silu` | arg0=`[1, 256, 17, 256, 80]/float16C` | arg1=`<GroupNorm>` ; arg2=`<SiLU>` | ion-b200 call 139 |
| hunyuanvideo | `group_norm_silu.apply_group_norm_silu` | arg0=`[1, 128, 17, 256, 80]/float16NC` | arg1=`<GroupNorm>` ; arg2=`<SiLU>` | ion-b200 call 140 |
| hunyuanvideo | `group_norm_silu.apply_group_norm_silu` | arg0=`[1, 128, 17, 256, 80]/float16C` | arg1=`<GroupNorm>` ; arg2=`<SiLU>` | ion-b200 call 141 |
| hunyuanvideo | `group_norm_silu.apply_group_norm_silu` | arg0=`[1, 512, 5, 12, 32]/float16C` | arg1=`<GroupNorm>` ; arg2=`<SiLU>` | ion-b200 call 291 |
| hunyuanvideo | `group_norm_silu.apply_group_norm_silu` | arg0=`[1, 512, 5, 12, 32]/float16NC` | arg1=`<GroupNorm>` ; arg2=`<SiLU>` | ion-b200 call 292 |
| hunyuanvideo | `group_norm_silu.apply_group_norm_silu` | arg0=`[1, 512, 5, 24, 64]/float16C` | arg1=`<GroupNorm>` ; arg2=`<SiLU>` | ion-b200 call 301 |
| hunyuanvideo | `group_norm_silu.apply_group_norm_silu` | arg0=`[1, 512, 5, 24, 64]/float16NC` | arg1=`<GroupNorm>` ; arg2=`<SiLU>` | ion-b200 call 302 |
| hunyuanvideo | `group_norm_silu.apply_group_norm_silu` | arg0=`[1, 512, 9, 48, 128]/float16C` | arg1=`<GroupNorm>` ; arg2=`<SiLU>` | ion-b200 call 307 |
| hunyuanvideo | `group_norm_silu.apply_group_norm_silu` | arg0=`[1, 256, 9, 48, 128]/float16NC` | arg1=`<GroupNorm>` ; arg2=`<SiLU>` | ion-b200 call 308 |
| hunyuanvideo | `group_norm_silu.apply_group_norm_silu` | arg0=`[1, 256, 9, 48, 128]/float16C` | arg1=`<GroupNorm>` ; arg2=`<SiLU>` | ion-b200 call 309 |
| hunyuanvideo | `group_norm_silu.apply_group_norm_silu` | arg0=`[1, 256, 17, 96, 256]/float16C` | arg1=`<GroupNorm>` ; arg2=`<SiLU>` | ion-b200 call 313 |
| hunyuanvideo | `group_norm_silu.apply_group_norm_silu` | arg0=`[1, 128, 17, 96, 256]/float16NC` | arg1=`<GroupNorm>` ; arg2=`<SiLU>` | ion-b200 call 314 |
| hunyuanvideo | `group_norm_silu.apply_group_norm_silu` | arg0=`[1, 128, 17, 96, 256]/float16C` | arg1=`<GroupNorm>` ; arg2=`<SiLU>` | ion-b200 call 315 |
| hunyuanvideo | `group_norm_silu.apply_group_norm_silu` | arg0=`[1, 512, 5, 12, 10]/float16C` | arg1=`<GroupNorm>` ; arg2=`<SiLU>` | ion-b200 call 407 |
| hunyuanvideo | `group_norm_silu.apply_group_norm_silu` | arg0=`[1, 512, 5, 12, 10]/float16NC` | arg1=`<GroupNorm>` ; arg2=`<SiLU>` | ion-b200 call 408 |
| hunyuanvideo | `group_norm_silu.apply_group_norm_silu` | arg0=`[1, 512, 5, 24, 20]/float16C` | arg1=`<GroupNorm>` ; arg2=`<SiLU>` | ion-b200 call 417 |
| hunyuanvideo | `group_norm_silu.apply_group_norm_silu` | arg0=`[1, 512, 5, 24, 20]/float16NC` | arg1=`<GroupNorm>` ; arg2=`<SiLU>` | ion-b200 call 418 |
| hunyuanvideo | `group_norm_silu.apply_group_norm_silu` | arg0=`[1, 512, 9, 48, 40]/float16C` | arg1=`<GroupNorm>` ; arg2=`<SiLU>` | ion-b200 call 423 |
| hunyuanvideo | `group_norm_silu.apply_group_norm_silu` | arg0=`[1, 256, 9, 48, 40]/float16NC` | arg1=`<GroupNorm>` ; arg2=`<SiLU>` | ion-b200 call 424 |
| hunyuanvideo | `group_norm_silu.apply_group_norm_silu` | arg0=`[1, 256, 9, 48, 40]/float16C` | arg1=`<GroupNorm>` ; arg2=`<SiLU>` | ion-b200 call 425 |
| hunyuanvideo | `group_norm_silu.apply_group_norm_silu` | arg0=`[1, 256, 17, 96, 80]/float16C` | arg1=`<GroupNorm>` ; arg2=`<SiLU>` | ion-b200 call 429 |
| hunyuanvideo | `group_norm_silu.apply_group_norm_silu` | arg0=`[1, 128, 17, 96, 80]/float16NC` | arg1=`<GroupNorm>` ; arg2=`<SiLU>` | ion-b200 call 430 |
| hunyuanvideo | `group_norm_silu.apply_group_norm_silu` | arg0=`[1, 128, 17, 96, 80]/float16C` | arg1=`<GroupNorm>` ; arg2=`<SiLU>` | ion-b200 call 431 |
| hunyuanvideo | `group_norm_silu.apply_group_norm_silu` | arg0=`[1, 512, 2, 32, 32]/float16C` | arg1=`<GroupNorm>` ; arg2=`<SiLU>` | ion-b200 call 2176 |
| hunyuanvideo | `group_norm_silu.apply_group_norm_silu` | arg0=`[1, 512, 2, 32, 32]/float16NC` | arg1=`<GroupNorm>` ; arg2=`<SiLU>` | ion-b200 call 2177 |
| hunyuanvideo | `group_norm_silu.apply_group_norm_silu` | arg0=`[1, 512, 2, 64, 64]/float16C` | arg1=`<GroupNorm>` ; arg2=`<SiLU>` | ion-b200 call 2186 |
| hunyuanvideo | `group_norm_silu.apply_group_norm_silu` | arg0=`[1, 512, 2, 64, 64]/float16NC` | arg1=`<GroupNorm>` ; arg2=`<SiLU>` | ion-b200 call 2187 |
| hunyuanvideo | `group_norm_silu.apply_group_norm_silu` | arg0=`[1, 512, 3, 128, 128]/float16C` | arg1=`<GroupNorm>` ; arg2=`<SiLU>` | ion-b200 call 2192 |
| hunyuanvideo | `group_norm_silu.apply_group_norm_silu` | arg0=`[1, 256, 3, 128, 128]/float16NC` | arg1=`<GroupNorm>` ; arg2=`<SiLU>` | ion-b200 call 2193 |
| hunyuanvideo | `group_norm_silu.apply_group_norm_silu` | arg0=`[1, 256, 3, 128, 128]/float16C` | arg1=`<GroupNorm>` ; arg2=`<SiLU>` | ion-b200 call 2194 |
| hunyuanvideo | `group_norm_silu.apply_group_norm_silu` | arg0=`[1, 256, 5, 256, 256]/float16C` | arg1=`<GroupNorm>` ; arg2=`<SiLU>` | ion-b200 call 2198 |
| hunyuanvideo | `group_norm_silu.apply_group_norm_silu` | arg0=`[1, 128, 5, 256, 256]/float16NC` | arg1=`<GroupNorm>` ; arg2=`<SiLU>` | ion-b200 call 2199 |
| hunyuanvideo | `group_norm_silu.apply_group_norm_silu` | arg0=`[1, 128, 5, 256, 256]/float16C` | arg1=`<GroupNorm>` ; arg2=`<SiLU>` | ion-b200 call 2200 |
| hunyuanvideo | `group_norm_silu.apply_group_norm_silu` | arg0=`[1, 512, 2, 32, 10]/float16C` | arg1=`<GroupNorm>` ; arg2=`<SiLU>` | ion-b200 call 2292 |
| hunyuanvideo | `group_norm_silu.apply_group_norm_silu` | arg0=`[1, 512, 2, 32, 10]/float16NC` | arg1=`<GroupNorm>` ; arg2=`<SiLU>` | ion-b200 call 2293 |
| hunyuanvideo | `group_norm_silu.apply_group_norm_silu` | arg0=`[1, 512, 2, 64, 20]/float16C` | arg1=`<GroupNorm>` ; arg2=`<SiLU>` | ion-b200 call 2302 |
| hunyuanvideo | `group_norm_silu.apply_group_norm_silu` | arg0=`[1, 512, 2, 64, 20]/float16NC` | arg1=`<GroupNorm>` ; arg2=`<SiLU>` | ion-b200 call 2303 |
| hunyuanvideo | `group_norm_silu.apply_group_norm_silu` | arg0=`[1, 512, 3, 128, 40]/float16C` | arg1=`<GroupNorm>` ; arg2=`<SiLU>` | ion-b200 call 2308 |
| hunyuanvideo | `group_norm_silu.apply_group_norm_silu` | arg0=`[1, 256, 3, 128, 40]/float16NC` | arg1=`<GroupNorm>` ; arg2=`<SiLU>` | ion-b200 call 2309 |
| hunyuanvideo | `group_norm_silu.apply_group_norm_silu` | arg0=`[1, 256, 3, 128, 40]/float16C` | arg1=`<GroupNorm>` ; arg2=`<SiLU>` | ion-b200 call 2310 |
| hunyuanvideo | `group_norm_silu.apply_group_norm_silu` | arg0=`[1, 256, 5, 256, 80]/float16C` | arg1=`<GroupNorm>` ; arg2=`<SiLU>` | ion-b200 call 2314 |
| hunyuanvideo | `group_norm_silu.apply_group_norm_silu` | arg0=`[1, 128, 5, 256, 80]/float16NC` | arg1=`<GroupNorm>` ; arg2=`<SiLU>` | ion-b200 call 2315 |
| hunyuanvideo | `group_norm_silu.apply_group_norm_silu` | arg0=`[1, 128, 5, 256, 80]/float16C` | arg1=`<GroupNorm>` ; arg2=`<SiLU>` | ion-b200 call 2316 |
| hunyuanvideo | `group_norm_silu.apply_group_norm_silu` | arg0=`[1, 512, 2, 12, 32]/float16C` | arg1=`<GroupNorm>` ; arg2=`<SiLU>` | ion-b200 call 2466 |
| hunyuanvideo | `group_norm_silu.apply_group_norm_silu` | arg0=`[1, 512, 2, 12, 32]/float16NC` | arg1=`<GroupNorm>` ; arg2=`<SiLU>` | ion-b200 call 2467 |
| hunyuanvideo | `group_norm_silu.apply_group_norm_silu` | arg0=`[1, 512, 2, 24, 64]/float16C` | arg1=`<GroupNorm>` ; arg2=`<SiLU>` | ion-b200 call 2476 |
| hunyuanvideo | `group_norm_silu.apply_group_norm_silu` | arg0=`[1, 512, 2, 24, 64]/float16NC` | arg1=`<GroupNorm>` ; arg2=`<SiLU>` | ion-b200 call 2477 |
| hunyuanvideo | `group_norm_silu.apply_group_norm_silu` | arg0=`[1, 512, 3, 48, 128]/float16C` | arg1=`<GroupNorm>` ; arg2=`<SiLU>` | ion-b200 call 2482 |
| hunyuanvideo | `group_norm_silu.apply_group_norm_silu` | arg0=`[1, 256, 3, 48, 128]/float16NC` | arg1=`<GroupNorm>` ; arg2=`<SiLU>` | ion-b200 call 2483 |
| hunyuanvideo | `group_norm_silu.apply_group_norm_silu` | arg0=`[1, 256, 3, 48, 128]/float16C` | arg1=`<GroupNorm>` ; arg2=`<SiLU>` | ion-b200 call 2484 |
| hunyuanvideo | `group_norm_silu.apply_group_norm_silu` | arg0=`[1, 256, 5, 96, 256]/float16C` | arg1=`<GroupNorm>` ; arg2=`<SiLU>` | ion-b200 call 2488 |
| hunyuanvideo | `group_norm_silu.apply_group_norm_silu` | arg0=`[1, 128, 5, 96, 256]/float16NC` | arg1=`<GroupNorm>` ; arg2=`<SiLU>` | ion-b200 call 2489 |
| hunyuanvideo | `group_norm_silu.apply_group_norm_silu` | arg0=`[1, 128, 5, 96, 256]/float16C` | arg1=`<GroupNorm>` ; arg2=`<SiLU>` | ion-b200 call 2490 |
| hunyuanvideo | `group_norm_silu.apply_group_norm_silu` | arg0=`[1, 512, 2, 12, 10]/float16C` | arg1=`<GroupNorm>` ; arg2=`<SiLU>` | ion-b200 call 2582 |
| hunyuanvideo | `group_norm_silu.apply_group_norm_silu` | arg0=`[1, 512, 2, 12, 10]/float16NC` | arg1=`<GroupNorm>` ; arg2=`<SiLU>` | ion-b200 call 2583 |
| hunyuanvideo | `group_norm_silu.apply_group_norm_silu` | arg0=`[1, 512, 2, 24, 20]/float16C` | arg1=`<GroupNorm>` ; arg2=`<SiLU>` | ion-b200 call 2592 |
| hunyuanvideo | `group_norm_silu.apply_group_norm_silu` | arg0=`[1, 512, 2, 24, 20]/float16NC` | arg1=`<GroupNorm>` ; arg2=`<SiLU>` | ion-b200 call 2593 |
| hunyuanvideo | `group_norm_silu.apply_group_norm_silu` | arg0=`[1, 512, 3, 48, 40]/float16C` | arg1=`<GroupNorm>` ; arg2=`<SiLU>` | ion-b200 call 2598 |
| hunyuanvideo | `group_norm_silu.apply_group_norm_silu` | arg0=`[1, 256, 3, 48, 40]/float16NC` | arg1=`<GroupNorm>` ; arg2=`<SiLU>` | ion-b200 call 2599 |
| hunyuanvideo | `group_norm_silu.apply_group_norm_silu` | arg0=`[1, 256, 3, 48, 40]/float16C` | arg1=`<GroupNorm>` ; arg2=`<SiLU>` | ion-b200 call 2600 |
| hunyuanvideo | `group_norm_silu.apply_group_norm_silu` | arg0=`[1, 256, 5, 96, 80]/float16C` | arg1=`<GroupNorm>` ; arg2=`<SiLU>` | ion-b200 call 2604 |
| hunyuanvideo | `group_norm_silu.apply_group_norm_silu` | arg0=`[1, 128, 5, 96, 80]/float16NC` | arg1=`<GroupNorm>` ; arg2=`<SiLU>` | ion-b200 call 2605 |
| hunyuanvideo | `group_norm_silu.apply_group_norm_silu` | arg0=`[1, 128, 5, 96, 80]/float16C` | arg1=`<GroupNorm>` ; arg2=`<SiLU>` | ion-b200 call 2606 |
| hunyuanvideo | `group_norm_silu.triton_group_norm_silu` | arg0=`[1, 512, 5, 32, 32]/float16C` ; arg1=`[512]/float16C` ; arg2=`[512]/float16C` | num_groups=`32` ; eps=`1e-06` | ion-b200 call 1 |
| hunyuanvideo | `group_norm_silu.triton_group_norm_silu` | arg0=`[1, 512, 5, 32, 32]/float16NC` ; arg1=`[512]/float16C` ; arg2=`[512]/float16C` | num_groups=`32` ; eps=`1e-06` | ion-b200 call 2 |
| hunyuanvideo | `group_norm_silu.triton_group_norm_silu` | arg0=`[1, 512, 5, 64, 64]/float16C` ; arg1=`[512]/float16C` ; arg2=`[512]/float16C` | num_groups=`32` ; eps=`1e-06` | ion-b200 call 11 |
| hunyuanvideo | `group_norm_silu.triton_group_norm_silu` | arg0=`[1, 512, 5, 64, 64]/float16NC` ; arg1=`[512]/float16C` ; arg2=`[512]/float16C` | num_groups=`32` ; eps=`1e-06` | ion-b200 call 12 |
| hunyuanvideo | `group_norm_silu.triton_group_norm_silu` | arg0=`[1, 512, 9, 128, 128]/float16C` ; arg1=`[512]/float16C` ; arg2=`[512]/float16C` | num_groups=`32` ; eps=`1e-06` | ion-b200 call 17 |
| hunyuanvideo | `group_norm_silu.triton_group_norm_silu` | arg0=`[1, 256, 9, 128, 128]/float16NC` ; arg1=`[256]/float16C` ; arg2=`[256]/float16C` | num_groups=`32` ; eps=`1e-06` | ion-b200 call 18 |
| hunyuanvideo | `group_norm_silu.triton_group_norm_silu` | arg0=`[1, 256, 9, 128, 128]/float16C` ; arg1=`[256]/float16C` ; arg2=`[256]/float16C` | num_groups=`32` ; eps=`1e-06` | ion-b200 call 19 |
| hunyuanvideo | `group_norm_silu.triton_group_norm_silu` | arg0=`[1, 256, 17, 256, 256]/float16C` ; arg1=`[256]/float16C` ; arg2=`[256]/float16C` | num_groups=`32` ; eps=`1e-06` | ion-b200 call 23 |
| hunyuanvideo | `group_norm_silu.triton_group_norm_silu` | arg0=`[1, 128, 17, 256, 256]/float16NC` ; arg1=`[128]/float16C` ; arg2=`[128]/float16C` | num_groups=`32` ; eps=`1e-06` | ion-b200 call 24 |
| hunyuanvideo | `group_norm_silu.triton_group_norm_silu` | arg0=`[1, 128, 17, 256, 256]/float16C` ; arg1=`[128]/float16C` ; arg2=`[128]/float16C` | num_groups=`32` ; eps=`1e-06` | ion-b200 call 25 |
| hunyuanvideo | `group_norm_silu.triton_group_norm_silu` | arg0=`[1, 512, 5, 32, 10]/float16C` ; arg1=`[512]/float16C` ; arg2=`[512]/float16C` | num_groups=`32` ; eps=`1e-06` | ion-b200 call 117 |
| hunyuanvideo | `group_norm_silu.triton_group_norm_silu` | arg0=`[1, 512, 5, 32, 10]/float16NC` ; arg1=`[512]/float16C` ; arg2=`[512]/float16C` | num_groups=`32` ; eps=`1e-06` | ion-b200 call 118 |
| hunyuanvideo | `group_norm_silu.triton_group_norm_silu` | arg0=`[1, 512, 5, 64, 20]/float16C` ; arg1=`[512]/float16C` ; arg2=`[512]/float16C` | num_groups=`32` ; eps=`1e-06` | ion-b200 call 127 |
| hunyuanvideo | `group_norm_silu.triton_group_norm_silu` | arg0=`[1, 512, 5, 64, 20]/float16NC` ; arg1=`[512]/float16C` ; arg2=`[512]/float16C` | num_groups=`32` ; eps=`1e-06` | ion-b200 call 128 |
| hunyuanvideo | `group_norm_silu.triton_group_norm_silu` | arg0=`[1, 512, 9, 128, 40]/float16C` ; arg1=`[512]/float16C` ; arg2=`[512]/float16C` | num_groups=`32` ; eps=`1e-06` | ion-b200 call 133 |
| hunyuanvideo | `group_norm_silu.triton_group_norm_silu` | arg0=`[1, 256, 9, 128, 40]/float16NC` ; arg1=`[256]/float16C` ; arg2=`[256]/float16C` | num_groups=`32` ; eps=`1e-06` | ion-b200 call 134 |
| hunyuanvideo | `group_norm_silu.triton_group_norm_silu` | arg0=`[1, 256, 9, 128, 40]/float16C` ; arg1=`[256]/float16C` ; arg2=`[256]/float16C` | num_groups=`32` ; eps=`1e-06` | ion-b200 call 135 |
| hunyuanvideo | `group_norm_silu.triton_group_norm_silu` | arg0=`[1, 256, 17, 256, 80]/float16C` ; arg1=`[256]/float16C` ; arg2=`[256]/float16C` | num_groups=`32` ; eps=`1e-06` | ion-b200 call 139 |
| hunyuanvideo | `group_norm_silu.triton_group_norm_silu` | arg0=`[1, 128, 17, 256, 80]/float16NC` ; arg1=`[128]/float16C` ; arg2=`[128]/float16C` | num_groups=`32` ; eps=`1e-06` | ion-b200 call 140 |
| hunyuanvideo | `group_norm_silu.triton_group_norm_silu` | arg0=`[1, 128, 17, 256, 80]/float16C` ; arg1=`[128]/float16C` ; arg2=`[128]/float16C` | num_groups=`32` ; eps=`1e-06` | ion-b200 call 141 |
| hunyuanvideo | `group_norm_silu.triton_group_norm_silu` | arg0=`[1, 512, 5, 12, 32]/float16C` ; arg1=`[512]/float16C` ; arg2=`[512]/float16C` | num_groups=`32` ; eps=`1e-06` | ion-b200 call 291 |
| hunyuanvideo | `group_norm_silu.triton_group_norm_silu` | arg0=`[1, 512, 5, 12, 32]/float16NC` ; arg1=`[512]/float16C` ; arg2=`[512]/float16C` | num_groups=`32` ; eps=`1e-06` | ion-b200 call 292 |
| hunyuanvideo | `group_norm_silu.triton_group_norm_silu` | arg0=`[1, 512, 5, 24, 64]/float16C` ; arg1=`[512]/float16C` ; arg2=`[512]/float16C` | num_groups=`32` ; eps=`1e-06` | ion-b200 call 301 |
| hunyuanvideo | `group_norm_silu.triton_group_norm_silu` | arg0=`[1, 512, 5, 24, 64]/float16NC` ; arg1=`[512]/float16C` ; arg2=`[512]/float16C` | num_groups=`32` ; eps=`1e-06` | ion-b200 call 302 |
| hunyuanvideo | `group_norm_silu.triton_group_norm_silu` | arg0=`[1, 512, 9, 48, 128]/float16C` ; arg1=`[512]/float16C` ; arg2=`[512]/float16C` | num_groups=`32` ; eps=`1e-06` | ion-b200 call 307 |
| hunyuanvideo | `group_norm_silu.triton_group_norm_silu` | arg0=`[1, 256, 9, 48, 128]/float16NC` ; arg1=`[256]/float16C` ; arg2=`[256]/float16C` | num_groups=`32` ; eps=`1e-06` | ion-b200 call 308 |
| hunyuanvideo | `group_norm_silu.triton_group_norm_silu` | arg0=`[1, 256, 9, 48, 128]/float16C` ; arg1=`[256]/float16C` ; arg2=`[256]/float16C` | num_groups=`32` ; eps=`1e-06` | ion-b200 call 309 |
| hunyuanvideo | `group_norm_silu.triton_group_norm_silu` | arg0=`[1, 256, 17, 96, 256]/float16C` ; arg1=`[256]/float16C` ; arg2=`[256]/float16C` | num_groups=`32` ; eps=`1e-06` | ion-b200 call 313 |
| hunyuanvideo | `group_norm_silu.triton_group_norm_silu` | arg0=`[1, 128, 17, 96, 256]/float16NC` ; arg1=`[128]/float16C` ; arg2=`[128]/float16C` | num_groups=`32` ; eps=`1e-06` | ion-b200 call 314 |
| hunyuanvideo | `group_norm_silu.triton_group_norm_silu` | arg0=`[1, 128, 17, 96, 256]/float16C` ; arg1=`[128]/float16C` ; arg2=`[128]/float16C` | num_groups=`32` ; eps=`1e-06` | ion-b200 call 315 |
| hunyuanvideo | `group_norm_silu.triton_group_norm_silu` | arg0=`[1, 512, 5, 12, 10]/float16C` ; arg1=`[512]/float16C` ; arg2=`[512]/float16C` | num_groups=`32` ; eps=`1e-06` | ion-b200 call 407 |
| hunyuanvideo | `group_norm_silu.triton_group_norm_silu` | arg0=`[1, 512, 5, 12, 10]/float16NC` ; arg1=`[512]/float16C` ; arg2=`[512]/float16C` | num_groups=`32` ; eps=`1e-06` | ion-b200 call 408 |
| hunyuanvideo | `group_norm_silu.triton_group_norm_silu` | arg0=`[1, 512, 5, 24, 20]/float16C` ; arg1=`[512]/float16C` ; arg2=`[512]/float16C` | num_groups=`32` ; eps=`1e-06` | ion-b200 call 417 |
| hunyuanvideo | `group_norm_silu.triton_group_norm_silu` | arg0=`[1, 512, 5, 24, 20]/float16NC` ; arg1=`[512]/float16C` ; arg2=`[512]/float16C` | num_groups=`32` ; eps=`1e-06` | ion-b200 call 418 |
| hunyuanvideo | `group_norm_silu.triton_group_norm_silu` | arg0=`[1, 512, 9, 48, 40]/float16C` ; arg1=`[512]/float16C` ; arg2=`[512]/float16C` | num_groups=`32` ; eps=`1e-06` | ion-b200 call 423 |
| hunyuanvideo | `group_norm_silu.triton_group_norm_silu` | arg0=`[1, 256, 9, 48, 40]/float16NC` ; arg1=`[256]/float16C` ; arg2=`[256]/float16C` | num_groups=`32` ; eps=`1e-06` | ion-b200 call 424 |
| hunyuanvideo | `group_norm_silu.triton_group_norm_silu` | arg0=`[1, 256, 9, 48, 40]/float16C` ; arg1=`[256]/float16C` ; arg2=`[256]/float16C` | num_groups=`32` ; eps=`1e-06` | ion-b200 call 425 |
| hunyuanvideo | `group_norm_silu.triton_group_norm_silu` | arg0=`[1, 256, 17, 96, 80]/float16C` ; arg1=`[256]/float16C` ; arg2=`[256]/float16C` | num_groups=`32` ; eps=`1e-06` | ion-b200 call 429 |
| hunyuanvideo | `group_norm_silu.triton_group_norm_silu` | arg0=`[1, 128, 17, 96, 80]/float16NC` ; arg1=`[128]/float16C` ; arg2=`[128]/float16C` | num_groups=`32` ; eps=`1e-06` | ion-b200 call 430 |
| hunyuanvideo | `group_norm_silu.triton_group_norm_silu` | arg0=`[1, 128, 17, 96, 80]/float16C` ; arg1=`[128]/float16C` ; arg2=`[128]/float16C` | num_groups=`32` ; eps=`1e-06` | ion-b200 call 431 |
| hunyuanvideo | `group_norm_silu.triton_group_norm_silu` | arg0=`[1, 512, 2, 32, 32]/float16C` ; arg1=`[512]/float16C` ; arg2=`[512]/float16C` | num_groups=`32` ; eps=`1e-06` | ion-b200 call 2176 |
| hunyuanvideo | `group_norm_silu.triton_group_norm_silu` | arg0=`[1, 512, 2, 32, 32]/float16NC` ; arg1=`[512]/float16C` ; arg2=`[512]/float16C` | num_groups=`32` ; eps=`1e-06` | ion-b200 call 2177 |
| hunyuanvideo | `group_norm_silu.triton_group_norm_silu` | arg0=`[1, 512, 2, 64, 64]/float16C` ; arg1=`[512]/float16C` ; arg2=`[512]/float16C` | num_groups=`32` ; eps=`1e-06` | ion-b200 call 2186 |
| hunyuanvideo | `group_norm_silu.triton_group_norm_silu` | arg0=`[1, 512, 2, 64, 64]/float16NC` ; arg1=`[512]/float16C` ; arg2=`[512]/float16C` | num_groups=`32` ; eps=`1e-06` | ion-b200 call 2187 |
| hunyuanvideo | `group_norm_silu.triton_group_norm_silu` | arg0=`[1, 512, 3, 128, 128]/float16C` ; arg1=`[512]/float16C` ; arg2=`[512]/float16C` | num_groups=`32` ; eps=`1e-06` | ion-b200 call 2192 |
| hunyuanvideo | `group_norm_silu.triton_group_norm_silu` | arg0=`[1, 256, 3, 128, 128]/float16NC` ; arg1=`[256]/float16C` ; arg2=`[256]/float16C` | num_groups=`32` ; eps=`1e-06` | ion-b200 call 2193 |
| hunyuanvideo | `group_norm_silu.triton_group_norm_silu` | arg0=`[1, 256, 3, 128, 128]/float16C` ; arg1=`[256]/float16C` ; arg2=`[256]/float16C` | num_groups=`32` ; eps=`1e-06` | ion-b200 call 2194 |
| hunyuanvideo | `group_norm_silu.triton_group_norm_silu` | arg0=`[1, 256, 5, 256, 256]/float16C` ; arg1=`[256]/float16C` ; arg2=`[256]/float16C` | num_groups=`32` ; eps=`1e-06` | ion-b200 call 2198 |
| hunyuanvideo | `group_norm_silu.triton_group_norm_silu` | arg0=`[1, 128, 5, 256, 256]/float16NC` ; arg1=`[128]/float16C` ; arg2=`[128]/float16C` | num_groups=`32` ; eps=`1e-06` | ion-b200 call 2199 |
| hunyuanvideo | `group_norm_silu.triton_group_norm_silu` | arg0=`[1, 128, 5, 256, 256]/float16C` ; arg1=`[128]/float16C` ; arg2=`[128]/float16C` | num_groups=`32` ; eps=`1e-06` | ion-b200 call 2200 |
| hunyuanvideo | `group_norm_silu.triton_group_norm_silu` | arg0=`[1, 512, 2, 32, 10]/float16C` ; arg1=`[512]/float16C` ; arg2=`[512]/float16C` | num_groups=`32` ; eps=`1e-06` | ion-b200 call 2292 |
| hunyuanvideo | `group_norm_silu.triton_group_norm_silu` | arg0=`[1, 512, 2, 32, 10]/float16NC` ; arg1=`[512]/float16C` ; arg2=`[512]/float16C` | num_groups=`32` ; eps=`1e-06` | ion-b200 call 2293 |
| hunyuanvideo | `group_norm_silu.triton_group_norm_silu` | arg0=`[1, 512, 2, 64, 20]/float16C` ; arg1=`[512]/float16C` ; arg2=`[512]/float16C` | num_groups=`32` ; eps=`1e-06` | ion-b200 call 2302 |
| hunyuanvideo | `group_norm_silu.triton_group_norm_silu` | arg0=`[1, 512, 2, 64, 20]/float16NC` ; arg1=`[512]/float16C` ; arg2=`[512]/float16C` | num_groups=`32` ; eps=`1e-06` | ion-b200 call 2303 |
| hunyuanvideo | `group_norm_silu.triton_group_norm_silu` | arg0=`[1, 512, 3, 128, 40]/float16C` ; arg1=`[512]/float16C` ; arg2=`[512]/float16C` | num_groups=`32` ; eps=`1e-06` | ion-b200 call 2308 |
| hunyuanvideo | `group_norm_silu.triton_group_norm_silu` | arg0=`[1, 256, 3, 128, 40]/float16NC` ; arg1=`[256]/float16C` ; arg2=`[256]/float16C` | num_groups=`32` ; eps=`1e-06` | ion-b200 call 2309 |
| hunyuanvideo | `group_norm_silu.triton_group_norm_silu` | arg0=`[1, 256, 3, 128, 40]/float16C` ; arg1=`[256]/float16C` ; arg2=`[256]/float16C` | num_groups=`32` ; eps=`1e-06` | ion-b200 call 2310 |
| hunyuanvideo | `group_norm_silu.triton_group_norm_silu` | arg0=`[1, 256, 5, 256, 80]/float16C` ; arg1=`[256]/float16C` ; arg2=`[256]/float16C` | num_groups=`32` ; eps=`1e-06` | ion-b200 call 2314 |
| hunyuanvideo | `group_norm_silu.triton_group_norm_silu` | arg0=`[1, 128, 5, 256, 80]/float16NC` ; arg1=`[128]/float16C` ; arg2=`[128]/float16C` | num_groups=`32` ; eps=`1e-06` | ion-b200 call 2315 |
| hunyuanvideo | `group_norm_silu.triton_group_norm_silu` | arg0=`[1, 128, 5, 256, 80]/float16C` ; arg1=`[128]/float16C` ; arg2=`[128]/float16C` | num_groups=`32` ; eps=`1e-06` | ion-b200 call 2316 |
| hunyuanvideo | `group_norm_silu.triton_group_norm_silu` | arg0=`[1, 512, 2, 12, 32]/float16C` ; arg1=`[512]/float16C` ; arg2=`[512]/float16C` | num_groups=`32` ; eps=`1e-06` | ion-b200 call 2466 |
| hunyuanvideo | `group_norm_silu.triton_group_norm_silu` | arg0=`[1, 512, 2, 12, 32]/float16NC` ; arg1=`[512]/float16C` ; arg2=`[512]/float16C` | num_groups=`32` ; eps=`1e-06` | ion-b200 call 2467 |
| hunyuanvideo | `group_norm_silu.triton_group_norm_silu` | arg0=`[1, 512, 2, 24, 64]/float16C` ; arg1=`[512]/float16C` ; arg2=`[512]/float16C` | num_groups=`32` ; eps=`1e-06` | ion-b200 call 2476 |
| hunyuanvideo | `group_norm_silu.triton_group_norm_silu` | arg0=`[1, 512, 2, 24, 64]/float16NC` ; arg1=`[512]/float16C` ; arg2=`[512]/float16C` | num_groups=`32` ; eps=`1e-06` | ion-b200 call 2477 |
| hunyuanvideo | `group_norm_silu.triton_group_norm_silu` | arg0=`[1, 512, 3, 48, 128]/float16C` ; arg1=`[512]/float16C` ; arg2=`[512]/float16C` | num_groups=`32` ; eps=`1e-06` | ion-b200 call 2482 |
| hunyuanvideo | `group_norm_silu.triton_group_norm_silu` | arg0=`[1, 256, 3, 48, 128]/float16NC` ; arg1=`[256]/float16C` ; arg2=`[256]/float16C` | num_groups=`32` ; eps=`1e-06` | ion-b200 call 2483 |
| hunyuanvideo | `group_norm_silu.triton_group_norm_silu` | arg0=`[1, 256, 3, 48, 128]/float16C` ; arg1=`[256]/float16C` ; arg2=`[256]/float16C` | num_groups=`32` ; eps=`1e-06` | ion-b200 call 2484 |
| hunyuanvideo | `group_norm_silu.triton_group_norm_silu` | arg0=`[1, 256, 5, 96, 256]/float16C` ; arg1=`[256]/float16C` ; arg2=`[256]/float16C` | num_groups=`32` ; eps=`1e-06` | ion-b200 call 2488 |
| hunyuanvideo | `group_norm_silu.triton_group_norm_silu` | arg0=`[1, 128, 5, 96, 256]/float16NC` ; arg1=`[128]/float16C` ; arg2=`[128]/float16C` | num_groups=`32` ; eps=`1e-06` | ion-b200 call 2489 |
| hunyuanvideo | `group_norm_silu.triton_group_norm_silu` | arg0=`[1, 128, 5, 96, 256]/float16C` ; arg1=`[128]/float16C` ; arg2=`[128]/float16C` | num_groups=`32` ; eps=`1e-06` | ion-b200 call 2490 |
| hunyuanvideo | `group_norm_silu.triton_group_norm_silu` | arg0=`[1, 512, 2, 12, 10]/float16C` ; arg1=`[512]/float16C` ; arg2=`[512]/float16C` | num_groups=`32` ; eps=`1e-06` | ion-b200 call 2582 |
| hunyuanvideo | `group_norm_silu.triton_group_norm_silu` | arg0=`[1, 512, 2, 12, 10]/float16NC` ; arg1=`[512]/float16C` ; arg2=`[512]/float16C` | num_groups=`32` ; eps=`1e-06` | ion-b200 call 2583 |
| hunyuanvideo | `group_norm_silu.triton_group_norm_silu` | arg0=`[1, 512, 2, 24, 20]/float16C` ; arg1=`[512]/float16C` ; arg2=`[512]/float16C` | num_groups=`32` ; eps=`1e-06` | ion-b200 call 2592 |
| hunyuanvideo | `group_norm_silu.triton_group_norm_silu` | arg0=`[1, 512, 2, 24, 20]/float16NC` ; arg1=`[512]/float16C` ; arg2=`[512]/float16C` | num_groups=`32` ; eps=`1e-06` | ion-b200 call 2593 |
| hunyuanvideo | `group_norm_silu.triton_group_norm_silu` | arg0=`[1, 512, 3, 48, 40]/float16C` ; arg1=`[512]/float16C` ; arg2=`[512]/float16C` | num_groups=`32` ; eps=`1e-06` | ion-b200 call 2598 |
| hunyuanvideo | `group_norm_silu.triton_group_norm_silu` | arg0=`[1, 256, 3, 48, 40]/float16NC` ; arg1=`[256]/float16C` ; arg2=`[256]/float16C` | num_groups=`32` ; eps=`1e-06` | ion-b200 call 2599 |
| hunyuanvideo | `group_norm_silu.triton_group_norm_silu` | arg0=`[1, 256, 3, 48, 40]/float16C` ; arg1=`[256]/float16C` ; arg2=`[256]/float16C` | num_groups=`32` ; eps=`1e-06` | ion-b200 call 2600 |
| hunyuanvideo | `group_norm_silu.triton_group_norm_silu` | arg0=`[1, 256, 5, 96, 80]/float16C` ; arg1=`[256]/float16C` ; arg2=`[256]/float16C` | num_groups=`32` ; eps=`1e-06` | ion-b200 call 2604 |
| hunyuanvideo | `group_norm_silu.triton_group_norm_silu` | arg0=`[1, 128, 5, 96, 80]/float16NC` ; arg1=`[128]/float16C` ; arg2=`[128]/float16C` | num_groups=`32` ; eps=`1e-06` | ion-b200 call 2605 |
| hunyuanvideo | `group_norm_silu.triton_group_norm_silu` | arg0=`[1, 128, 5, 96, 80]/float16C` ; arg1=`[128]/float16C` ; arg2=`[128]/float16C` | num_groups=`32` ; eps=`1e-06` | ion-b200 call 2606 |

### `h200`

| Preset | Kernel | Tensor shapes | Other args | Evidence |
|---|---|---|---|---|
| hunyuanvideo | `group_norm_silu.apply_group_norm_silu` | arg0=`[1, 512, 5, 32, 32]/float16C` | arg1=`<GroupNorm>` ; arg2=`<SiLU>` | ion8-h200 call 1 |
| hunyuanvideo | `group_norm_silu.apply_group_norm_silu` | arg0=`[1, 512, 5, 64, 64]/float16C` | arg1=`<GroupNorm>` ; arg2=`<SiLU>` | ion8-h200 call 11 |
| hunyuanvideo | `group_norm_silu.apply_group_norm_silu` | arg0=`[1, 512, 9, 128, 128]/float16C` | arg1=`<GroupNorm>` ; arg2=`<SiLU>` | ion8-h200 call 17 |
| hunyuanvideo | `group_norm_silu.apply_group_norm_silu` | arg0=`[1, 256, 9, 128, 128]/float16C` | arg1=`<GroupNorm>` ; arg2=`<SiLU>` | ion8-h200 call 18 |
| hunyuanvideo | `group_norm_silu.apply_group_norm_silu` | arg0=`[1, 256, 17, 256, 256]/float16C` | arg1=`<GroupNorm>` ; arg2=`<SiLU>` | ion8-h200 call 23 |
| hunyuanvideo | `group_norm_silu.apply_group_norm_silu` | arg0=`[1, 128, 17, 256, 256]/float16C` | arg1=`<GroupNorm>` ; arg2=`<SiLU>` | ion8-h200 call 24 |
| hunyuanvideo | `group_norm_silu.apply_group_norm_silu` | arg0=`[1, 512, 5, 32, 10]/float16C` | arg1=`<GroupNorm>` ; arg2=`<SiLU>` | ion8-h200 call 117 |
| hunyuanvideo | `group_norm_silu.apply_group_norm_silu` | arg0=`[1, 512, 5, 64, 20]/float16C` | arg1=`<GroupNorm>` ; arg2=`<SiLU>` | ion8-h200 call 127 |
| hunyuanvideo | `group_norm_silu.apply_group_norm_silu` | arg0=`[1, 512, 9, 128, 40]/float16C` | arg1=`<GroupNorm>` ; arg2=`<SiLU>` | ion8-h200 call 133 |
| hunyuanvideo | `group_norm_silu.apply_group_norm_silu` | arg0=`[1, 256, 9, 128, 40]/float16C` | arg1=`<GroupNorm>` ; arg2=`<SiLU>` | ion8-h200 call 134 |
| hunyuanvideo | `group_norm_silu.apply_group_norm_silu` | arg0=`[1, 256, 17, 256, 80]/float16C` | arg1=`<GroupNorm>` ; arg2=`<SiLU>` | ion8-h200 call 139 |
| hunyuanvideo | `group_norm_silu.apply_group_norm_silu` | arg0=`[1, 128, 17, 256, 80]/float16C` | arg1=`<GroupNorm>` ; arg2=`<SiLU>` | ion8-h200 call 140 |
| hunyuanvideo | `group_norm_silu.apply_group_norm_silu` | arg0=`[1, 512, 5, 12, 32]/float16C` | arg1=`<GroupNorm>` ; arg2=`<SiLU>` | ion8-h200 call 291 |
| hunyuanvideo | `group_norm_silu.apply_group_norm_silu` | arg0=`[1, 512, 5, 24, 64]/float16C` | arg1=`<GroupNorm>` ; arg2=`<SiLU>` | ion8-h200 call 301 |
| hunyuanvideo | `group_norm_silu.apply_group_norm_silu` | arg0=`[1, 512, 9, 48, 128]/float16C` | arg1=`<GroupNorm>` ; arg2=`<SiLU>` | ion8-h200 call 307 |
| hunyuanvideo | `group_norm_silu.apply_group_norm_silu` | arg0=`[1, 256, 9, 48, 128]/float16C` | arg1=`<GroupNorm>` ; arg2=`<SiLU>` | ion8-h200 call 308 |
| hunyuanvideo | `group_norm_silu.apply_group_norm_silu` | arg0=`[1, 256, 17, 96, 256]/float16C` | arg1=`<GroupNorm>` ; arg2=`<SiLU>` | ion8-h200 call 313 |
| hunyuanvideo | `group_norm_silu.apply_group_norm_silu` | arg0=`[1, 128, 17, 96, 256]/float16C` | arg1=`<GroupNorm>` ; arg2=`<SiLU>` | ion8-h200 call 314 |
| hunyuanvideo | `group_norm_silu.apply_group_norm_silu` | arg0=`[1, 512, 5, 12, 10]/float16C` | arg1=`<GroupNorm>` ; arg2=`<SiLU>` | ion8-h200 call 407 |
| hunyuanvideo | `group_norm_silu.apply_group_norm_silu` | arg0=`[1, 512, 5, 24, 20]/float16C` | arg1=`<GroupNorm>` ; arg2=`<SiLU>` | ion8-h200 call 417 |
| hunyuanvideo | `group_norm_silu.apply_group_norm_silu` | arg0=`[1, 512, 9, 48, 40]/float16C` | arg1=`<GroupNorm>` ; arg2=`<SiLU>` | ion8-h200 call 423 |
| hunyuanvideo | `group_norm_silu.apply_group_norm_silu` | arg0=`[1, 256, 9, 48, 40]/float16C` | arg1=`<GroupNorm>` ; arg2=`<SiLU>` | ion8-h200 call 424 |
| hunyuanvideo | `group_norm_silu.apply_group_norm_silu` | arg0=`[1, 256, 17, 96, 80]/float16C` | arg1=`<GroupNorm>` ; arg2=`<SiLU>` | ion8-h200 call 429 |
| hunyuanvideo | `group_norm_silu.apply_group_norm_silu` | arg0=`[1, 128, 17, 96, 80]/float16C` | arg1=`<GroupNorm>` ; arg2=`<SiLU>` | ion8-h200 call 430 |
| hunyuanvideo | `group_norm_silu.apply_group_norm_silu` | arg0=`[1, 512, 2, 32, 32]/float16C` | arg1=`<GroupNorm>` ; arg2=`<SiLU>` | ion8-h200 call 2176 |
| hunyuanvideo | `group_norm_silu.apply_group_norm_silu` | arg0=`[1, 512, 2, 64, 64]/float16C` | arg1=`<GroupNorm>` ; arg2=`<SiLU>` | ion8-h200 call 2186 |
| hunyuanvideo | `group_norm_silu.apply_group_norm_silu` | arg0=`[1, 512, 3, 128, 128]/float16C` | arg1=`<GroupNorm>` ; arg2=`<SiLU>` | ion8-h200 call 2192 |
| hunyuanvideo | `group_norm_silu.apply_group_norm_silu` | arg0=`[1, 256, 3, 128, 128]/float16C` | arg1=`<GroupNorm>` ; arg2=`<SiLU>` | ion8-h200 call 2193 |
| hunyuanvideo | `group_norm_silu.apply_group_norm_silu` | arg0=`[1, 256, 5, 256, 256]/float16C` | arg1=`<GroupNorm>` ; arg2=`<SiLU>` | ion8-h200 call 2198 |
| hunyuanvideo | `group_norm_silu.apply_group_norm_silu` | arg0=`[1, 128, 5, 256, 256]/float16C` | arg1=`<GroupNorm>` ; arg2=`<SiLU>` | ion8-h200 call 2199 |
| hunyuanvideo | `group_norm_silu.apply_group_norm_silu` | arg0=`[1, 512, 2, 32, 10]/float16C` | arg1=`<GroupNorm>` ; arg2=`<SiLU>` | ion8-h200 call 2292 |
| hunyuanvideo | `group_norm_silu.apply_group_norm_silu` | arg0=`[1, 512, 2, 64, 20]/float16C` | arg1=`<GroupNorm>` ; arg2=`<SiLU>` | ion8-h200 call 2302 |
| hunyuanvideo | `group_norm_silu.apply_group_norm_silu` | arg0=`[1, 512, 3, 128, 40]/float16C` | arg1=`<GroupNorm>` ; arg2=`<SiLU>` | ion8-h200 call 2308 |
| hunyuanvideo | `group_norm_silu.apply_group_norm_silu` | arg0=`[1, 256, 3, 128, 40]/float16C` | arg1=`<GroupNorm>` ; arg2=`<SiLU>` | ion8-h200 call 2309 |
| hunyuanvideo | `group_norm_silu.apply_group_norm_silu` | arg0=`[1, 256, 5, 256, 80]/float16C` | arg1=`<GroupNorm>` ; arg2=`<SiLU>` | ion8-h200 call 2314 |
| hunyuanvideo | `group_norm_silu.apply_group_norm_silu` | arg0=`[1, 128, 5, 256, 80]/float16C` | arg1=`<GroupNorm>` ; arg2=`<SiLU>` | ion8-h200 call 2315 |
| hunyuanvideo | `group_norm_silu.apply_group_norm_silu` | arg0=`[1, 512, 2, 12, 32]/float16C` | arg1=`<GroupNorm>` ; arg2=`<SiLU>` | ion8-h200 call 2466 |
| hunyuanvideo | `group_norm_silu.apply_group_norm_silu` | arg0=`[1, 512, 2, 24, 64]/float16C` | arg1=`<GroupNorm>` ; arg2=`<SiLU>` | ion8-h200 call 2476 |
| hunyuanvideo | `group_norm_silu.apply_group_norm_silu` | arg0=`[1, 512, 3, 48, 128]/float16C` | arg1=`<GroupNorm>` ; arg2=`<SiLU>` | ion8-h200 call 2482 |
| hunyuanvideo | `group_norm_silu.apply_group_norm_silu` | arg0=`[1, 256, 3, 48, 128]/float16C` | arg1=`<GroupNorm>` ; arg2=`<SiLU>` | ion8-h200 call 2483 |
| hunyuanvideo | `group_norm_silu.apply_group_norm_silu` | arg0=`[1, 256, 5, 96, 256]/float16C` | arg1=`<GroupNorm>` ; arg2=`<SiLU>` | ion8-h200 call 2488 |
| hunyuanvideo | `group_norm_silu.apply_group_norm_silu` | arg0=`[1, 128, 5, 96, 256]/float16C` | arg1=`<GroupNorm>` ; arg2=`<SiLU>` | ion8-h200 call 2489 |
| hunyuanvideo | `group_norm_silu.apply_group_norm_silu` | arg0=`[1, 512, 2, 12, 10]/float16C` | arg1=`<GroupNorm>` ; arg2=`<SiLU>` | ion8-h200 call 2582 |
| hunyuanvideo | `group_norm_silu.apply_group_norm_silu` | arg0=`[1, 512, 2, 24, 20]/float16C` | arg1=`<GroupNorm>` ; arg2=`<SiLU>` | ion8-h200 call 2592 |
| hunyuanvideo | `group_norm_silu.apply_group_norm_silu` | arg0=`[1, 512, 3, 48, 40]/float16C` | arg1=`<GroupNorm>` ; arg2=`<SiLU>` | ion8-h200 call 2598 |
| hunyuanvideo | `group_norm_silu.apply_group_norm_silu` | arg0=`[1, 256, 3, 48, 40]/float16C` | arg1=`<GroupNorm>` ; arg2=`<SiLU>` | ion8-h200 call 2599 |
| hunyuanvideo | `group_norm_silu.apply_group_norm_silu` | arg0=`[1, 256, 5, 96, 80]/float16C` | arg1=`<GroupNorm>` ; arg2=`<SiLU>` | ion8-h200 call 2604 |
| hunyuanvideo | `group_norm_silu.apply_group_norm_silu` | arg0=`[1, 128, 5, 96, 80]/float16C` | arg1=`<GroupNorm>` ; arg2=`<SiLU>` | ion8-h200 call 2605 |
| hunyuanvideo | `group_norm_silu.triton_group_norm_silu` | arg0=`[1, 512, 5, 32, 32]/float16C` ; arg1=`[512]/float16C` ; arg2=`[512]/float16C` | num_groups=`32` ; eps=`1e-06` | ion8-h200 call 1 |
| hunyuanvideo | `group_norm_silu.triton_group_norm_silu` | arg0=`[1, 512, 5, 64, 64]/float16C` ; arg1=`[512]/float16C` ; arg2=`[512]/float16C` | num_groups=`32` ; eps=`1e-06` | ion8-h200 call 11 |
| hunyuanvideo | `group_norm_silu.triton_group_norm_silu` | arg0=`[1, 512, 9, 128, 128]/float16C` ; arg1=`[512]/float16C` ; arg2=`[512]/float16C` | num_groups=`32` ; eps=`1e-06` | ion8-h200 call 17 |
| hunyuanvideo | `group_norm_silu.triton_group_norm_silu` | arg0=`[1, 256, 9, 128, 128]/float16C` ; arg1=`[256]/float16C` ; arg2=`[256]/float16C` | num_groups=`32` ; eps=`1e-06` | ion8-h200 call 18 |
| hunyuanvideo | `group_norm_silu.triton_group_norm_silu` | arg0=`[1, 256, 17, 256, 256]/float16C` ; arg1=`[256]/float16C` ; arg2=`[256]/float16C` | num_groups=`32` ; eps=`1e-06` | ion8-h200 call 23 |
| hunyuanvideo | `group_norm_silu.triton_group_norm_silu` | arg0=`[1, 128, 17, 256, 256]/float16C` ; arg1=`[128]/float16C` ; arg2=`[128]/float16C` | num_groups=`32` ; eps=`1e-06` | ion8-h200 call 24 |
| hunyuanvideo | `group_norm_silu.triton_group_norm_silu` | arg0=`[1, 512, 5, 32, 10]/float16C` ; arg1=`[512]/float16C` ; arg2=`[512]/float16C` | num_groups=`32` ; eps=`1e-06` | ion8-h200 call 117 |
| hunyuanvideo | `group_norm_silu.triton_group_norm_silu` | arg0=`[1, 512, 5, 64, 20]/float16C` ; arg1=`[512]/float16C` ; arg2=`[512]/float16C` | num_groups=`32` ; eps=`1e-06` | ion8-h200 call 127 |
| hunyuanvideo | `group_norm_silu.triton_group_norm_silu` | arg0=`[1, 512, 9, 128, 40]/float16C` ; arg1=`[512]/float16C` ; arg2=`[512]/float16C` | num_groups=`32` ; eps=`1e-06` | ion8-h200 call 133 |
| hunyuanvideo | `group_norm_silu.triton_group_norm_silu` | arg0=`[1, 256, 9, 128, 40]/float16C` ; arg1=`[256]/float16C` ; arg2=`[256]/float16C` | num_groups=`32` ; eps=`1e-06` | ion8-h200 call 134 |
| hunyuanvideo | `group_norm_silu.triton_group_norm_silu` | arg0=`[1, 256, 17, 256, 80]/float16C` ; arg1=`[256]/float16C` ; arg2=`[256]/float16C` | num_groups=`32` ; eps=`1e-06` | ion8-h200 call 139 |
| hunyuanvideo | `group_norm_silu.triton_group_norm_silu` | arg0=`[1, 128, 17, 256, 80]/float16C` ; arg1=`[128]/float16C` ; arg2=`[128]/float16C` | num_groups=`32` ; eps=`1e-06` | ion8-h200 call 140 |
| hunyuanvideo | `group_norm_silu.triton_group_norm_silu` | arg0=`[1, 512, 5, 12, 32]/float16C` ; arg1=`[512]/float16C` ; arg2=`[512]/float16C` | num_groups=`32` ; eps=`1e-06` | ion8-h200 call 291 |
| hunyuanvideo | `group_norm_silu.triton_group_norm_silu` | arg0=`[1, 512, 5, 24, 64]/float16C` ; arg1=`[512]/float16C` ; arg2=`[512]/float16C` | num_groups=`32` ; eps=`1e-06` | ion8-h200 call 301 |
| hunyuanvideo | `group_norm_silu.triton_group_norm_silu` | arg0=`[1, 512, 9, 48, 128]/float16C` ; arg1=`[512]/float16C` ; arg2=`[512]/float16C` | num_groups=`32` ; eps=`1e-06` | ion8-h200 call 307 |
| hunyuanvideo | `group_norm_silu.triton_group_norm_silu` | arg0=`[1, 256, 9, 48, 128]/float16C` ; arg1=`[256]/float16C` ; arg2=`[256]/float16C` | num_groups=`32` ; eps=`1e-06` | ion8-h200 call 308 |
| hunyuanvideo | `group_norm_silu.triton_group_norm_silu` | arg0=`[1, 256, 17, 96, 256]/float16C` ; arg1=`[256]/float16C` ; arg2=`[256]/float16C` | num_groups=`32` ; eps=`1e-06` | ion8-h200 call 313 |
| hunyuanvideo | `group_norm_silu.triton_group_norm_silu` | arg0=`[1, 128, 17, 96, 256]/float16C` ; arg1=`[128]/float16C` ; arg2=`[128]/float16C` | num_groups=`32` ; eps=`1e-06` | ion8-h200 call 314 |
| hunyuanvideo | `group_norm_silu.triton_group_norm_silu` | arg0=`[1, 512, 5, 12, 10]/float16C` ; arg1=`[512]/float16C` ; arg2=`[512]/float16C` | num_groups=`32` ; eps=`1e-06` | ion8-h200 call 407 |
| hunyuanvideo | `group_norm_silu.triton_group_norm_silu` | arg0=`[1, 512, 5, 24, 20]/float16C` ; arg1=`[512]/float16C` ; arg2=`[512]/float16C` | num_groups=`32` ; eps=`1e-06` | ion8-h200 call 417 |
| hunyuanvideo | `group_norm_silu.triton_group_norm_silu` | arg0=`[1, 512, 9, 48, 40]/float16C` ; arg1=`[512]/float16C` ; arg2=`[512]/float16C` | num_groups=`32` ; eps=`1e-06` | ion8-h200 call 423 |
| hunyuanvideo | `group_norm_silu.triton_group_norm_silu` | arg0=`[1, 256, 9, 48, 40]/float16C` ; arg1=`[256]/float16C` ; arg2=`[256]/float16C` | num_groups=`32` ; eps=`1e-06` | ion8-h200 call 424 |
| hunyuanvideo | `group_norm_silu.triton_group_norm_silu` | arg0=`[1, 256, 17, 96, 80]/float16C` ; arg1=`[256]/float16C` ; arg2=`[256]/float16C` | num_groups=`32` ; eps=`1e-06` | ion8-h200 call 429 |
| hunyuanvideo | `group_norm_silu.triton_group_norm_silu` | arg0=`[1, 128, 17, 96, 80]/float16C` ; arg1=`[128]/float16C` ; arg2=`[128]/float16C` | num_groups=`32` ; eps=`1e-06` | ion8-h200 call 430 |
| hunyuanvideo | `group_norm_silu.triton_group_norm_silu` | arg0=`[1, 512, 2, 32, 32]/float16C` ; arg1=`[512]/float16C` ; arg2=`[512]/float16C` | num_groups=`32` ; eps=`1e-06` | ion8-h200 call 2176 |
| hunyuanvideo | `group_norm_silu.triton_group_norm_silu` | arg0=`[1, 512, 2, 64, 64]/float16C` ; arg1=`[512]/float16C` ; arg2=`[512]/float16C` | num_groups=`32` ; eps=`1e-06` | ion8-h200 call 2186 |
| hunyuanvideo | `group_norm_silu.triton_group_norm_silu` | arg0=`[1, 512, 3, 128, 128]/float16C` ; arg1=`[512]/float16C` ; arg2=`[512]/float16C` | num_groups=`32` ; eps=`1e-06` | ion8-h200 call 2192 |
| hunyuanvideo | `group_norm_silu.triton_group_norm_silu` | arg0=`[1, 256, 3, 128, 128]/float16C` ; arg1=`[256]/float16C` ; arg2=`[256]/float16C` | num_groups=`32` ; eps=`1e-06` | ion8-h200 call 2193 |
| hunyuanvideo | `group_norm_silu.triton_group_norm_silu` | arg0=`[1, 256, 5, 256, 256]/float16C` ; arg1=`[256]/float16C` ; arg2=`[256]/float16C` | num_groups=`32` ; eps=`1e-06` | ion8-h200 call 2198 |
| hunyuanvideo | `group_norm_silu.triton_group_norm_silu` | arg0=`[1, 128, 5, 256, 256]/float16C` ; arg1=`[128]/float16C` ; arg2=`[128]/float16C` | num_groups=`32` ; eps=`1e-06` | ion8-h200 call 2199 |
| hunyuanvideo | `group_norm_silu.triton_group_norm_silu` | arg0=`[1, 512, 2, 32, 10]/float16C` ; arg1=`[512]/float16C` ; arg2=`[512]/float16C` | num_groups=`32` ; eps=`1e-06` | ion8-h200 call 2292 |
| hunyuanvideo | `group_norm_silu.triton_group_norm_silu` | arg0=`[1, 512, 2, 64, 20]/float16C` ; arg1=`[512]/float16C` ; arg2=`[512]/float16C` | num_groups=`32` ; eps=`1e-06` | ion8-h200 call 2302 |
| hunyuanvideo | `group_norm_silu.triton_group_norm_silu` | arg0=`[1, 512, 3, 128, 40]/float16C` ; arg1=`[512]/float16C` ; arg2=`[512]/float16C` | num_groups=`32` ; eps=`1e-06` | ion8-h200 call 2308 |
| hunyuanvideo | `group_norm_silu.triton_group_norm_silu` | arg0=`[1, 256, 3, 128, 40]/float16C` ; arg1=`[256]/float16C` ; arg2=`[256]/float16C` | num_groups=`32` ; eps=`1e-06` | ion8-h200 call 2309 |
| hunyuanvideo | `group_norm_silu.triton_group_norm_silu` | arg0=`[1, 256, 5, 256, 80]/float16C` ; arg1=`[256]/float16C` ; arg2=`[256]/float16C` | num_groups=`32` ; eps=`1e-06` | ion8-h200 call 2314 |
| hunyuanvideo | `group_norm_silu.triton_group_norm_silu` | arg0=`[1, 128, 5, 256, 80]/float16C` ; arg1=`[128]/float16C` ; arg2=`[128]/float16C` | num_groups=`32` ; eps=`1e-06` | ion8-h200 call 2315 |
| hunyuanvideo | `group_norm_silu.triton_group_norm_silu` | arg0=`[1, 512, 2, 12, 32]/float16C` ; arg1=`[512]/float16C` ; arg2=`[512]/float16C` | num_groups=`32` ; eps=`1e-06` | ion8-h200 call 2466 |
| hunyuanvideo | `group_norm_silu.triton_group_norm_silu` | arg0=`[1, 512, 2, 24, 64]/float16C` ; arg1=`[512]/float16C` ; arg2=`[512]/float16C` | num_groups=`32` ; eps=`1e-06` | ion8-h200 call 2476 |
| hunyuanvideo | `group_norm_silu.triton_group_norm_silu` | arg0=`[1, 512, 3, 48, 128]/float16C` ; arg1=`[512]/float16C` ; arg2=`[512]/float16C` | num_groups=`32` ; eps=`1e-06` | ion8-h200 call 2482 |
| hunyuanvideo | `group_norm_silu.triton_group_norm_silu` | arg0=`[1, 256, 3, 48, 128]/float16C` ; arg1=`[256]/float16C` ; arg2=`[256]/float16C` | num_groups=`32` ; eps=`1e-06` | ion8-h200 call 2483 |
| hunyuanvideo | `group_norm_silu.triton_group_norm_silu` | arg0=`[1, 256, 5, 96, 256]/float16C` ; arg1=`[256]/float16C` ; arg2=`[256]/float16C` | num_groups=`32` ; eps=`1e-06` | ion8-h200 call 2488 |
| hunyuanvideo | `group_norm_silu.triton_group_norm_silu` | arg0=`[1, 128, 5, 96, 256]/float16C` ; arg1=`[128]/float16C` ; arg2=`[128]/float16C` | num_groups=`32` ; eps=`1e-06` | ion8-h200 call 2489 |
| hunyuanvideo | `group_norm_silu.triton_group_norm_silu` | arg0=`[1, 512, 2, 12, 10]/float16C` ; arg1=`[512]/float16C` ; arg2=`[512]/float16C` | num_groups=`32` ; eps=`1e-06` | ion8-h200 call 2582 |
| hunyuanvideo | `group_norm_silu.triton_group_norm_silu` | arg0=`[1, 512, 2, 24, 20]/float16C` ; arg1=`[512]/float16C` ; arg2=`[512]/float16C` | num_groups=`32` ; eps=`1e-06` | ion8-h200 call 2592 |
| hunyuanvideo | `group_norm_silu.triton_group_norm_silu` | arg0=`[1, 512, 3, 48, 40]/float16C` ; arg1=`[512]/float16C` ; arg2=`[512]/float16C` | num_groups=`32` ; eps=`1e-06` | ion8-h200 call 2598 |
| hunyuanvideo | `group_norm_silu.triton_group_norm_silu` | arg0=`[1, 256, 3, 48, 40]/float16C` ; arg1=`[256]/float16C` ; arg2=`[256]/float16C` | num_groups=`32` ; eps=`1e-06` | ion8-h200 call 2599 |
| hunyuanvideo | `group_norm_silu.triton_group_norm_silu` | arg0=`[1, 256, 5, 96, 80]/float16C` ; arg1=`[256]/float16C` ; arg2=`[256]/float16C` | num_groups=`32` ; eps=`1e-06` | ion8-h200 call 2604 |
| hunyuanvideo | `group_norm_silu.triton_group_norm_silu` | arg0=`[1, 128, 5, 96, 80]/float16C` ; arg1=`[128]/float16C` ; arg2=`[128]/float16C` | num_groups=`32` ; eps=`1e-06` | ion8-h200 call 2605 |

## `diffusion_norm_infer__multi_shape`

### `b200`

| Preset | Kernel | Tensor shapes | Other args | Evidence |
|---|---|---|---|---|
| helios | `norm.norm_infer` | arg0=`[8640, 5120]/float32C` ; arg1=`[5120]/float32C` ; arg2=`[5120]/float32C` | eps=`1e-06` ; is_rms_norm=`False` | ion-b200 call 1 |
| hunyuanvideo | `rmsnorm_onepass.triton_one_pass_rms_norm` | arg0=`[648720, 128]/bfloat16C` ; arg1=`[128]/bfloat16C` | arg2=`1e-06` | ion-b200 call 1 |
| hunyuanvideo | `rmsnorm_onepass.triton_one_pass_rms_norm` | arg0=`[1320, 128]/bfloat16C` ; arg1=`[128]/bfloat16C` | arg2=`1e-06` | ion-b200 call 3 |
| hunyuanvideo | `rmsnorm_onepass.triton_one_pass_rms_norm` | arg0=`[650040, 128]/bfloat16C` ; arg1=`[128]/bfloat16C` | arg2=`1e-06` | ion-b200 call 81 |
| zimage | `rmsnorm_onepass.triton_one_pass_rms_norm` | arg0=`[16384, 128]/bfloat16C` ; arg1=`[128]/bfloat16C` | arg2=`1e-06` | ion-b200 call 1 |
| zimage | `rmsnorm_onepass.triton_one_pass_rms_norm` | arg0=`[4096, 128]/bfloat16C` ; arg1=`[128]/bfloat16C` | arg2=`1e-06` | ion-b200 call 2 |

### `h200`

| Preset | Kernel | Tensor shapes | Other args | Evidence |
|---|---|---|---|---|
| helios | `norm.norm_infer` | arg0=`[8640, 5120]/float32C` ; arg1=`[5120]/float32C` ; arg2=`[5120]/float32C` | eps=`1e-06` ; is_rms_norm=`False` | ion8-h200 call 1 |
| hunyuanvideo | `rmsnorm_onepass.triton_one_pass_rms_norm` | arg0=`[648720, 128]/bfloat16C` ; arg1=`[128]/bfloat16C` | arg2=`1e-06` | ion8-h200 call 1 |
| hunyuanvideo | `rmsnorm_onepass.triton_one_pass_rms_norm` | arg0=`[1320, 128]/bfloat16C` ; arg1=`[128]/bfloat16C` | arg2=`1e-06` | ion8-h200 call 3 |
| hunyuanvideo | `rmsnorm_onepass.triton_one_pass_rms_norm` | arg0=`[650040, 128]/bfloat16C` ; arg1=`[128]/bfloat16C` | arg2=`1e-06` | ion8-h200 call 81 |
| zimage | `rmsnorm_onepass.triton_one_pass_rms_norm` | arg0=`[16384, 128]/bfloat16C` ; arg1=`[128]/bfloat16C` | arg2=`1e-06` | ion8-h200 call 1 |
| zimage | `rmsnorm_onepass.triton_one_pass_rms_norm` | arg0=`[4096, 128]/bfloat16C` ; arg1=`[128]/bfloat16C` | arg2=`1e-06` | ion8-h200 call 2 |

## `diffusion_qknorm_rope__multi_shape`

### `b200`

| Preset | Kernel | Tensor shapes | Other args | Evidence |
|---|---|---|---|---|
| joyai-edit | `qknorm_rope.fused_inplace_qknorm_rope` | q=`[7904, 32, 128]/bfloat16C` ; k=`[7904, 32, 128]/bfloat16C` ; q_weight=`[128]/bfloat16C` ; k_weight=`[128]/bfloat16C` ; cos_sin_cache=`[7904, 128]/float32C` ; positions=`[7904]/int64C` | is_neox=`False` ; eps=`1e-06` ; head_dim=`128` ; rope_dim=`128` | ion-b200 call 1 |
| qwen | `qknorm_rope.fused_inplace_qknorm_rope` | q=`[4096, 24, 128]/bfloat16C` ; k=`[4096, 24, 128]/bfloat16C` ; q_weight=`[128]/bfloat16C` ; k_weight=`[128]/bfloat16C` ; cos_sin_cache=`[4096, 128]/float32C` ; positions=`[4096]/int64C` | is_neox=`False` ; eps=`1e-06` ; head_dim=`128` ; rope_dim=`128` | ion-b200 call 1 |
| qwen | `qknorm_rope.fused_inplace_qknorm_rope` | q=`[19, 24, 128]/bfloat16C` ; k=`[19, 24, 128]/bfloat16C` ; q_weight=`[128]/bfloat16C` ; k_weight=`[128]/bfloat16C` ; cos_sin_cache=`[19, 128]/float32C` ; positions=`[19]/int64C` | is_neox=`False` ; eps=`1e-06` ; head_dim=`128` ; rope_dim=`128` | ion-b200 call 2 |
| qwen | `qknorm_rope.fused_inplace_qknorm_rope` | q=`[47, 24, 128]/bfloat16C` ; k=`[47, 24, 128]/bfloat16C` ; q_weight=`[128]/bfloat16C` ; k_weight=`[128]/bfloat16C` ; cos_sin_cache=`[47, 128]/float32C` ; positions=`[47]/int64C` | is_neox=`False` ; eps=`1e-06` ; head_dim=`128` ; rope_dim=`128` | ion-b200 call 122 |
| qwen-edit | `qknorm_rope.fused_inplace_qknorm_rope` | q=`[8424, 24, 128]/bfloat16C` ; k=`[8424, 24, 128]/bfloat16C` ; q_weight=`[128]/bfloat16C` ; k_weight=`[128]/bfloat16C` ; cos_sin_cache=`[8424, 128]/float32C` ; positions=`[8424]/int64C` | is_neox=`False` ; eps=`1e-06` ; head_dim=`128` ; rope_dim=`128` | ion-b200 call 1 |
| qwen-edit | `qknorm_rope.fused_inplace_qknorm_rope` | q=`[195, 24, 128]/bfloat16C` ; k=`[195, 24, 128]/bfloat16C` ; q_weight=`[128]/bfloat16C` ; k_weight=`[128]/bfloat16C` ; cos_sin_cache=`[195, 128]/float32C` ; positions=`[195]/int64C` | is_neox=`False` ; eps=`1e-06` ; head_dim=`128` ; rope_dim=`128` | ion-b200 call 2 |
| qwen-edit | `qknorm_rope.fused_inplace_qknorm_rope` | q=`[189, 24, 128]/bfloat16C` ; k=`[189, 24, 128]/bfloat16C` ; q_weight=`[128]/bfloat16C` ; k_weight=`[128]/bfloat16C` ; cos_sin_cache=`[189, 128]/float32C` ; positions=`[189]/int64C` | is_neox=`False` ; eps=`1e-06` ; head_dim=`128` ; rope_dim=`128` | ion-b200 call 122 |
| zimage | `qknorm_rope.fused_inplace_qknorm_rope` | q=`[4096, 30, 128]/bfloat16C` ; k=`[4096, 30, 128]/bfloat16C` ; q_weight=`[128]/bfloat16C` ; k_weight=`[128]/bfloat16C` ; cos_sin_cache=`[4096, 128]/float32C` ; positions=`[4096]/int64C` | is_neox=`False` ; eps=`1e-05` ; head_dim=`128` ; rope_dim=`128` | ion-b200 call 1 |
| zimage | `qknorm_rope.fused_inplace_qknorm_rope` | q=`[32, 30, 128]/bfloat16C` ; k=`[32, 30, 128]/bfloat16C` ; q_weight=`[128]/bfloat16C` ; k_weight=`[128]/bfloat16C` ; cos_sin_cache=`[32, 128]/float32C` ; positions=`[32]/int64C` | is_neox=`False` ; eps=`1e-05` ; head_dim=`128` ; rope_dim=`128` | ion-b200 call 3 |
| zimage | `qknorm_rope.fused_inplace_qknorm_rope` | q=`[4128, 30, 128]/bfloat16C` ; k=`[4128, 30, 128]/bfloat16C` ; q_weight=`[128]/bfloat16C` ; k_weight=`[128]/bfloat16C` ; cos_sin_cache=`[4128, 128]/float32C` ; positions=`[4128]/int64C` | is_neox=`False` ; eps=`1e-05` ; head_dim=`128` ; rope_dim=`128` | ion-b200 call 5 |

### `h200`

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

## `diffusion_rms_norm_fn__multi_shape`

### `b200`

No live call signatures captured.

### `h200`

No live call signatures captured.

## `diffusion_rotary_embedding__multi_shape`

### `b200`

| Preset | Kernel | Tensor shapes | Other args | Evidence |
|---|---|---|---|---|
| hunyuanvideo | `rotary.apply_rotary_embedding` | arg0=`[1, 27030, 24, 128]/bfloat16C` ; arg1=`[27030, 64]/float32C` ; arg2=`[27030, 64]/float32C` | arg3=`False` | ion-b200 call 1 |
| hunyuanvideo | `rotary.apply_rotary_embedding` | arg0=`[1, 27030, 24, 128]/bfloat16C` ; arg1=`[27030, 64]/float32C` ; arg2=`[27030, 64]/float32C` | arg3=`False` | ion-b200 call 41 |
| ltx23-ti2v-two-stage | `ltx2_rotary.apply_ltx2_split_rotary_emb` | arg0=`[1, 1536, 4096]/bfloat16C` ; arg1=`[1, 32, 1536, 64]/bfloat16NC` ; arg2=`[1, 32, 1536, 64]/bfloat16NC` | (none) | ion-b200 call 1 |
| ltx23-ti2v-two-stage | `ltx2_rotary.apply_ltx2_split_rotary_emb` | arg0=`[1, 126, 2048]/bfloat16C` ; arg1=`[1, 32, 126, 32]/bfloat16NC` ; arg2=`[1, 32, 126, 32]/bfloat16NC` | (none) | ion-b200 call 3 |
| ltx23-ti2v-two-stage | `ltx2_rotary.apply_ltx2_split_rotary_emb` | arg0=`[1, 1536, 2048]/bfloat16C` ; arg1=`[1, 32, 1536, 32]/bfloat16NC` ; arg2=`[1, 32, 1536, 32]/bfloat16NC` | (none) | ion-b200 call 5 |
| ltx23-ti2v-two-stage | `ltx2_rotary.apply_ltx2_split_rotary_emb` | arg0=`[1, 6144, 4096]/bfloat16C` ; arg1=`[1, 32, 6144, 64]/bfloat16NC` ; arg2=`[1, 32, 6144, 64]/bfloat16NC` | (none) | ion-b200 call 765 |
| ltx23-ti2v-two-stage | `ltx2_rotary.apply_ltx2_split_rotary_emb` | arg0=`[1, 6144, 2048]/bfloat16C` ; arg1=`[1, 32, 6144, 32]/bfloat16NC` ; arg2=`[1, 32, 6144, 32]/bfloat16NC` | (none) | ion-b200 call 769 |
| ltx23-two-stage | `ltx2_rotary.apply_ltx2_split_rotary_emb` | arg0=`[2, 6144, 4096]/bfloat16C` ; arg1=`[2, 32, 6144, 64]/bfloat16NC` ; arg2=`[2, 32, 6144, 64]/bfloat16NC` | (none) | ion-b200 call 1 |
| ltx23-two-stage | `ltx2_rotary.apply_ltx2_split_rotary_emb` | arg0=`[2, 126, 2048]/bfloat16C` ; arg1=`[2, 32, 126, 32]/bfloat16NC` ; arg2=`[2, 32, 126, 32]/bfloat16NC` | (none) | ion-b200 call 3 |
| ltx23-two-stage | `ltx2_rotary.apply_ltx2_split_rotary_emb` | arg0=`[2, 6144, 2048]/bfloat16C` ; arg1=`[2, 32, 6144, 32]/bfloat16NC` ; arg2=`[2, 32, 6144, 32]/bfloat16NC` | (none) | ion-b200 call 5 |
| ltx23-two-stage | `ltx2_rotary.apply_ltx2_split_rotary_emb` | arg0=`[1, 24576, 4096]/bfloat16C` ; arg1=`[1, 32, 24576, 64]/bfloat16NC` ; arg2=`[1, 32, 24576, 64]/bfloat16NC` | (none) | ion-b200 call 385 |
| ltx23-two-stage | `ltx2_rotary.apply_ltx2_split_rotary_emb` | arg0=`[1, 24576, 2048]/bfloat16C` ; arg1=`[1, 32, 24576, 32]/bfloat16NC` ; arg2=`[1, 32, 24576, 32]/bfloat16NC` | (none) | ion-b200 call 389 |

### `h200`

| Preset | Kernel | Tensor shapes | Other args | Evidence |
|---|---|---|---|---|
| hunyuanvideo | `rotary.apply_rotary_embedding` | arg0=`[1, 27030, 24, 128]/bfloat16C` ; arg1=`[27030, 64]/float32C` ; arg2=`[27030, 64]/float32C` | arg3=`False` | ion8-h200 call 1 |
| hunyuanvideo | `rotary.apply_rotary_embedding` | arg0=`[1, 27030, 24, 128]/bfloat16C` ; arg1=`[27030, 64]/float32C` ; arg2=`[27030, 64]/float32C` | arg3=`False` | ion8-h200 call 41 |
| ltx2 | `ltx2_rotary.apply_ltx2_split_rotary_emb` | arg0=`[1, 1536, 4096]/bfloat16C` ; arg1=`[1, 32, 1536, 64]/bfloat16NC` ; arg2=`[1, 32, 1536, 64]/bfloat16NC` | (none) | ion8-h200 call 1 |
| ltx2 | `ltx2_rotary.apply_ltx2_split_rotary_emb` | arg0=`[1, 126, 2048]/bfloat16C` ; arg1=`[1, 32, 126, 32]/bfloat16NC` ; arg2=`[1, 32, 126, 32]/bfloat16NC` | (none) | ion8-h200 call 3 |
| ltx2 | `ltx2_rotary.apply_ltx2_split_rotary_emb` | arg0=`[1, 1536, 2048]/bfloat16C` ; arg1=`[1, 32, 1536, 32]/bfloat16NC` ; arg2=`[1, 32, 1536, 32]/bfloat16NC` | (none) | ion8-h200 call 5 |
| ltx2 | `ltx2_rotary.apply_ltx2_split_rotary_emb` | arg0=`[1, 6144, 4096]/bfloat16C` ; arg1=`[1, 32, 6144, 64]/bfloat16NC` ; arg2=`[1, 32, 6144, 64]/bfloat16NC` | (none) | ion8-h200 call 385 |
| ltx2 | `ltx2_rotary.apply_ltx2_split_rotary_emb` | arg0=`[1, 6144, 2048]/bfloat16C` ; arg1=`[1, 32, 6144, 32]/bfloat16NC` ; arg2=`[1, 32, 6144, 32]/bfloat16NC` | (none) | ion8-h200 call 389 |

