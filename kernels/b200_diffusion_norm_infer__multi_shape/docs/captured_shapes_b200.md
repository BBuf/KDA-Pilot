# Captured shapes for `b200_diffusion_norm_infer__multi_shape`

Every row below is a live SGLang diffusion benchmark capture. No analytical fallback shapes are included.

| Preset | Kernel | Tensor shapes | Other args | Evidence |
|---|---|---|---|---|
| helios | `norm.norm_infer` | arg0=`[8640, 5120]/float32C` ; arg1=`[5120]/float32C` ; arg2=`[5120]/float32C` | eps=`1e-06` ; is_rms_norm=`False` | ion-b200 call 1 |
| hunyuanvideo | `rmsnorm_onepass.triton_one_pass_rms_norm` | arg0=`[648720, 128]/bfloat16C` ; arg1=`[128]/bfloat16C` | arg2=`1e-06` | ion-b200 call 1 |
| hunyuanvideo | `rmsnorm_onepass.triton_one_pass_rms_norm` | arg0=`[1320, 128]/bfloat16C` ; arg1=`[128]/bfloat16C` | arg2=`1e-06` | ion-b200 call 3 |
| hunyuanvideo | `rmsnorm_onepass.triton_one_pass_rms_norm` | arg0=`[650040, 128]/bfloat16C` ; arg1=`[128]/bfloat16C` | arg2=`1e-06` | ion-b200 call 81 |
| zimage | `rmsnorm_onepass.triton_one_pass_rms_norm` | arg0=`[16384, 128]/bfloat16C` ; arg1=`[128]/bfloat16C` | arg2=`1e-06` | ion-b200 call 1 |
| zimage | `rmsnorm_onepass.triton_one_pass_rms_norm` | arg0=`[4096, 128]/bfloat16C` ; arg1=`[128]/bfloat16C` | arg2=`1e-06` | ion-b200 call 2 |

Legend: `<shape>/<dtype>/C|NC` where `C`=contiguous, `NC`=non-contiguous.
