# Profile evidence - bs=1, RTX PRO 6000 (sm_120), 4k-in/1k-out

## DSpark verify steps (block 8 -> M=T=9), torch-profiler, 58 verify steps

| share | GPU total | calls | kernel |
|---:|---:|---:|---|
| 40.7% | 716.9 ms | 7798 | cutlass GemmUniversal (flashinfer mm_fp4: NVFP4 W4A4 MLP + lm_head) |
| 10.3% | 181.5 ms | 2784 | cuBLAS sm89_xmma e4m3 64x128 tiles (FP8 projections, M=9) |
| 8.4% | 148.1 ms | 4640 | cuBLAS sm89_xmma e4m3 32x64 tiles (FP8 projections, M=9) |
| 7.6% | 133.4 ms | 4160 | cutlass::Kernel2 (cuBLAS fp8 epilogue family) |
| 3.1% | 54.5 ms | 1250 | flashinfer BatchPrefill (verify attention) |
| 2.6% | 46.6 ms | 2784 | fused_sigmoid_gating_delta_rule_update_kernel (GDN verify, T=9) |
| 2.2% | 38.3 ms | 3840 | tensorrt_llm cvt_fp16_to_fp4 (activation quant) |
| 1.8% | 31.2 ms | 8132 | flashinfer fused_add_rmsnorm |
| 1.4% | 24.2 ms | 2880 | fused_qkvzba_split_reshape_cat_contiguous |
| 1.3% | 23.5 ms | 2784 | causal_conv1d_update |
| 0.7% | 13.2 ms | 7584 | _static_quant_fp8 |

Headline: `sglang::sm120_fp8_gemv_kernel` (34.0% of the plain-decode step, ~95% of
copy bandwidth) does not appear at all under DSpark - the whole FP8 family falls
to tiny-M cuBLAS tiles (~27% of the verify step across the three rows above).

## Plain decode (M=1) reference, same GPU class, same model family

| share | per-step | calls/step | kernel |
|---:|---:|---:|---|
| 50.5% | 7.09 ms | 129 | cutlass GemmUniversal (mm_fp4, M=1) |
| 34.0% | 4.77 ms | 128 | sglang::sm120_fp8_gemv_kernel |
| 3.8% | 0.54 ms | 96 | cuBLAS dot+reduce (in_proj_ba bf16 5120->96) |
| 2.6% | 0.37 ms | 32 | flashinfer attention |
| ~5% | ~0.7 ms | ~450 | norms + quant glue |
| ~2.3% | ~0.31 ms | ~144 | GDN recurrent + conv update + gated LN |

Model geometry (config.json, exact): hidden 5120, intermediate 17408,
attn 24q/4kv x 256, GDN 16 k-heads / 48 v-heads x 128 (ratio 3), conv kernel 4,
64 layers (48 GDN + 16 attn), vocab 248320.
