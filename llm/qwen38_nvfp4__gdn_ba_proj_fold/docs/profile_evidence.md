# Profile evidence — bs=1 decode step, RTX PRO 6000 (SM120)

Source: torch-profiler kernel trace captured on the target GPU on 2026-08-14
serving `RadixArk/Qwen3.8-27B-NVFP4` (revision 5b4377e58) with the cookbook
flags (`--mamba-ssm-dtype bfloat16 --kv-cache-dtype fp8_e4m3
--disable-radix-cache`, TP1). Decode window isolated via the 48
`fused_recurrent_gated_delta_rule_packed_decode` markers per step; 4 clean
steps aggregated. Wall/step 13.39 ms matches the independently benchmarked ITL
of 13.36 ms.

| share | GPU/step | calls/step | kernel |
|---:|---:|---:|---|
| 50.5% | 7091 us | 129 | cutlass GemmUniversal (flashinfer mm_fp4, NVFP4 W4A4 MLP + lm_head) |
| 34.0% | 4771 us | 128 | sglang::sm120_fp8_gemv_kernel (attn/GDN FP8 projections) |
| 2.6% | 370 us | 48 | cuBLAS reduce_1Block_kernel (in_proj_ba pair, part 2) |
| 2.2% | 315 us | 16 | flashinfer::BatchPrefillWithPagedKVCacheKernel |
| 1.8% | 252 us | 128 | flashinfer fused_add_rmsnorm |
| 1.2% | 165 us | 48 | cuBLAS dot_kernel (in_proj_ba pair, part 1) |
| 1.2% | 165 us | 128 | _static_quant_fp8 |
| 1.1% | 156 us | 48 | fused_recurrent_gated_delta_rule_packed_decode_kernel |
| 1.0% | 141 us | 81 | tensorrt_llm quantize_with_block_size |
| 0.8% | 117 us | 48 | tensorrt_llm cvt_fp16_to_fp4_expert |
| 0.6% | 86 us | 48 | _fused_qkvzba_causal_conv1d_update_contiguous_kernel |
| 0.5% | 71 us | 48 | _layer_norm_fwd_1pass_kernel |
| ... | ~340 us | ~270 | remaining elementwise/rope/copy glue |

Weight-bandwidth check: GEMV/GEMM families sum to 11.9 ms/step ~= 16.5 GB of
resident weights / 1.46 TB/s -> the M=1 path is already ~95% of copy peak. The
optimization headroom targeted by these tasks is therefore (a) keeping the
M in [2,16] DSpark verify tiers on the same weight-stream bound instead of the
cuBLAS tiny-M cliff, and (b) the non-GEMM launch/glue tail.

Model geometry (config.json, exact): hidden 5120, intermediate 17408, attn 24q/
4kv x head 256, GDN 16 k-heads / 48 v-heads x 128 (ratio 3), conv kernel 4,
64 layers (48 GDN + 16 attn, interval 4), vocab 248320.
