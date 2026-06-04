# Unique captured signatures (dedup mapping)

Source: `docs/captured_shapes_b200.jsonl` (43 rows). 39 unique call signatures (geomean basis per DEC-1).

| # | Case ID | Kernel | norm/eps | Models | JSONL rows |
|---|---------|--------|----------|--------|------------|
| 1 | `nss-b1-s8424-d3072-bf16-s11D.bf16-s11D.bf16-eps1e-06` | fused_norm_scale_shift | layer/1e-06 | firered-edit-1.0 | 1 |
| 2 | `srnss-b1-s8424-d3072-bf16-g11D.bf16-s11D.bf16-s11D.bf16-eps1e-06` | fused_scale_residual_norm_scale_shift | layer/1e-06 | firered-edit-1.0 | 2 |
| 3 | `nss-b1-s11040-d5120-bf16-s1SD.fp32-s1SD.fp32-eps1e-06` | fused_norm_scale_shift | layer/1e-06 | helios | 3 |
| 4 | `nss-b1-s8640-d5120-bf16-s1SD.bf16-s1SD.bf16-eps1e-06` | fused_norm_scale_shift | layer/1e-06 | helios | 4 |
| 5 | `nss-b1-s27030-d3072-bf16-s1D.bf16-s1D.bf16-eps1e-06` | fused_norm_scale_shift | layer/1e-06 | hunyuanvideo | 5 |
| 6 | `nss-b1-s55-d3072-bf16-s1D.bf16-s1D.bf16-eps1e-06` | fused_norm_scale_shift | layer/1e-06 | hunyuanvideo | 6 |
| 7 | `nss-b1-s27085-d3072-bf16-s1D.bf16-s1D.bf16-eps1e-06` | fused_norm_scale_shift | layer/1e-06 | hunyuanvideo | 7 |
| 8 | `srnss-b1-s27030-d3072-bf16-g1D.bf16-s1D.bf16-s1D.bf16-eps1e-06` | fused_scale_residual_norm_scale_shift | layer/1e-06 | hunyuanvideo | 8 |
| 9 | `srnss-b1-s55-d3072-bf16-g1D.bf16-s1D.bf16-s1D.bf16-eps1e-06` | fused_scale_residual_norm_scale_shift | layer/1e-06 | hunyuanvideo | 9 |
| 10 | `nss-b1-s7904-d4096-bf16-s1D.bf16-s1D.bf16-eps1e-06` | fused_norm_scale_shift | layer/1e-06 | joyai-edit | 10 |
| 11 | `nss-b1-s1004-d4096-bf16-s1D.bf16-s1D.bf16-eps1e-06` | fused_norm_scale_shift | layer/1e-06 | joyai-edit | 11 |
| 12 | `nss-b1-s997-d4096-bf16-s1D.bf16-s1D.bf16-eps1e-06` | fused_norm_scale_shift | layer/1e-06 | joyai-edit | 12 |
| 13 | `nss-b1-s44100-d5120-bf16-s11D.bf16-s11D.bf16-eps1e-06` | fused_norm_scale_shift | layer/1e-06 | mova-720p | 13 |
| 14 | `nss-b1-s101-d1536-bf16-s11D.bf16-s11D.bf16-eps1e-06` | fused_norm_scale_shift | layer/1e-06 | mova-720p | 14 |
| 15 | `nss-b1-s176400-d5120-bf16-s11D.bf16-s11D.bf16-eps1e-06` | fused_norm_scale_shift | layer/1e-06 | mova-720p | 15 |
| 16 | `srnss-b1-s44100-d5120-bf16-gnone-s11D.bf16-s11D.bf16-eps1e-06` | fused_scale_residual_norm_scale_shift | layer/1e-06 | mova-720p | 16 |
| 17 | `srnss-b1-s101-d1536-bf16-gnone-s11D.bf16-s11D.bf16-eps1e-06` | fused_scale_residual_norm_scale_shift | layer/1e-06 | mova-720p | 17 |
| 18 | `nss-b1-s4096-d3072-bf16-s11D.bf16-s11D.bf16-eps1e-06` | fused_norm_scale_shift | layer/1e-06 | qwen | 18 |
| 19 | `nss-b1-s19-d3072-bf16-s1D.bf16-s1D.bf16-eps1e-06` | fused_norm_scale_shift | layer/1e-06 | qwen | 19 |
| 20 | `nss-b1-s47-d3072-bf16-s1D.bf16-s1D.bf16-eps1e-06` | fused_norm_scale_shift | layer/1e-06 | qwen | 20 |
| 21 | `srnss-b1-s4096-d3072-bf16-g11D.bf16-s11D.bf16-s11D.bf16-eps1e-06` | fused_scale_residual_norm_scale_shift | layer/1e-06 | qwen | 21 |
| 22 | `srnss-b1-s19-d3072-bf16-g11D.bf16-s1D.bf16-s1D.bf16-eps1e-06` | fused_scale_residual_norm_scale_shift | layer/1e-06 | qwen | 22 |
| 23 | `srnss-b1-s47-d3072-bf16-g11D.bf16-s1D.bf16-s1D.bf16-eps1e-06` | fused_scale_residual_norm_scale_shift | layer/1e-06 | qwen | 23 |
| 24 | `nss-b1-s195-d3072-bf16-s1D.bf16-s1D.bf16-eps1e-06` | fused_norm_scale_shift | layer/1e-06 | qwen-edit | 24 |
| 25 | `nss-b1-s189-d3072-bf16-s1D.bf16-s1D.bf16-eps1e-06` | fused_norm_scale_shift | layer/1e-06 | qwen-edit | 25 |
| 26 | `srnss-b1-s195-d3072-bf16-g11D.bf16-s1D.bf16-s1D.bf16-eps1e-06` | fused_scale_residual_norm_scale_shift | layer/1e-06 | qwen-edit | 26 |
| 27 | `srnss-b1-s189-d3072-bf16-g11D.bf16-s1D.bf16-s1D.bf16-eps1e-06` | fused_scale_residual_norm_scale_shift | layer/1e-06 | qwen-edit | 27 |
| 28 | `nss-b1-s37044-d5120-bf16-s11D.fp32-s11D.fp32-eps1e-06` | fused_norm_scale_shift | layer/1e-06 | wan-i2v | 28, 29 |
| 29 | `nss-b1-s74088-d5120-bf16-s11D.bf16-s11D.bf16-eps1e-06` | fused_norm_scale_shift | layer/1e-06 | wan-i2v | 30 |
| 30 | `srnss-b1-s37044-d5120-bf16-g11D.fp32-wD.fp32-s1.bf16-s1.bf16-eps1e-06` | fused_scale_residual_norm_scale_shift | layer/1e-06 | wan-i2v | 31, 33 |
| 31 | `srnss-b1-s37044-d5120-bf16-gnone-s11D.fp32-s11D.fp32-eps1e-06` | fused_scale_residual_norm_scale_shift | layer/1e-06 | wan-i2v | 32 |
| 32 | `nss-b1-s37800-d5120-bf16-s11D.fp32-s11D.fp32-eps1e-06` | fused_norm_scale_shift | layer/1e-06 | wan-t2v | 34, 35 |
| 33 | `nss-b1-s75600-d5120-bf16-s11D.bf16-s11D.bf16-eps1e-06` | fused_norm_scale_shift | layer/1e-06 | wan-t2v | 36 |
| 34 | `srnss-b1-s37800-d5120-bf16-g11D.fp32-wD.fp32-s1.bf16-s1.bf16-eps1e-06` | fused_scale_residual_norm_scale_shift | layer/1e-06 | wan-t2v | 37, 39 |
| 35 | `srnss-b1-s37800-d5120-bf16-gnone-s11D.fp32-s11D.fp32-eps1e-06` | fused_scale_residual_norm_scale_shift | layer/1e-06 | wan-t2v | 38 |
| 36 | `nss-b1-s18144-d3072-bf16-s1SD.fp32-s1SD.fp32-eps1e-06` | fused_norm_scale_shift | layer/1e-06 | wan-ti2v | 40 |
| 37 | `nss-b1-s18144-d3072-bf16-s1SD.bf16-s1SD.bf16-eps1e-06` | fused_norm_scale_shift | layer/1e-06 | wan-ti2v | 41 |
| 38 | `srnss-b1-s18144-d3072-bf16-g1SD.fp32-wD.fp32-s1.bf16-s1.bf16-eps1e-06` | fused_scale_residual_norm_scale_shift | layer/1e-06 | wan-ti2v | 42 |
| 39 | `srnss-b1-s18144-d3072-bf16-gnone-s1SD.fp32-s1SD.fp32-eps1e-06` | fused_scale_residual_norm_scale_shift | layer/1e-06 | wan-ti2v | 43 |
