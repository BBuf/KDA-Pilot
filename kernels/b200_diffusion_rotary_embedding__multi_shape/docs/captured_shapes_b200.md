# Captured shapes for `b200_diffusion_rotary_embedding__multi_shape`

Every row below is a live SGLang diffusion benchmark capture. No analytical fallback shapes are included.

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

Legend: `<shape>/<dtype>/C|NC` where `C`=contiguous, `NC`=non-contiguous.
