# Captured shapes for `b200_diffusion_cutedsl_norm_tanh_mul_add__multi_shape`

Every row below is a live SGLang diffusion benchmark capture. No analytical fallback shapes are included.

| Preset | Kernel | Tensor shapes | Other args | Evidence |
|---|---|---|---|---|
| zimage | `norm_tanh_mul_add_norm_scale.fused_norm_tanh_mul_add` | arg0=`[1, 4096, 3840]/bfloat16C` ; arg1=`[3840]/bfloat16C` ; arg3=`[1, 1, 3840]/bfloat16C` ; arg4=`[1, 4096, 3840]/bfloat16C` | arg2=`None` ; arg5=`rms` ; arg6=`1e-05` | ion-b200 call 1 |
| zimage | `norm_tanh_mul_add_norm_scale.fused_norm_tanh_mul_add` | arg0=`[1, 4128, 3840]/bfloat16C` ; arg1=`[3840]/bfloat16C` ; arg3=`[1, 1, 3840]/bfloat16C` ; arg4=`[1, 4128, 3840]/bfloat16C` | arg2=`None` ; arg5=`rms` ; arg6=`1e-05` | ion-b200 call 3 |
| zimage | `norm_tanh_mul_add_norm_scale.fused_norm_tanh_mul_add_norm_scale` | arg0=`[1, 4096, 3840]/bfloat16C` ; arg1=`[3840]/bfloat16C` ; arg3=`[1, 1, 3840]/bfloat16C` ; arg4=`[1, 4096, 3840]/bfloat16C` ; arg5=`[3840]/bfloat16C` ; arg7=`[1, 1, 3840]/bfloat16C` | arg2=`None` ; arg6=`None` ; arg8=`rms` ; arg9=`1e-05` | ion-b200 call 1 |
| zimage | `norm_tanh_mul_add_norm_scale.fused_norm_tanh_mul_add_norm_scale` | arg0=`[1, 4128, 3840]/bfloat16C` ; arg1=`[3840]/bfloat16C` ; arg3=`[1, 1, 3840]/bfloat16C` ; arg4=`[1, 4128, 3840]/bfloat16C` ; arg5=`[3840]/bfloat16C` ; arg7=`[1, 1, 3840]/bfloat16C` | arg2=`None` ; arg6=`None` ; arg8=`rms` ; arg9=`1e-05` | ion-b200 call 3 |

Legend: `<shape>/<dtype>/C|NC` where `C`=contiguous, `NC`=non-contiguous.
