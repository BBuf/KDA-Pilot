# Captured shapes for `b200_diffusion_fuse_scale_shift__multi_shape`

Every row below is a live SGLang diffusion benchmark capture. No analytical fallback shapes are included.

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

Legend: `<shape>/<dtype>/C|NC` where `C`=contiguous, `NC`=non-contiguous.
