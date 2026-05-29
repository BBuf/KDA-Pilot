# Captured shapes for `h200_diffusion_group_norm_silu__multi_shape`

Every row below is a live SGLang diffusion benchmark capture. No analytical fallback shapes are included.

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

Legend: `<shape>/<dtype>/C|NC` where `C`=contiguous, `NC`=non-contiguous.
