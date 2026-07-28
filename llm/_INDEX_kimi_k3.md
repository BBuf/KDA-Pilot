# kimi_k3 — standalone kernel task selection

- Model: `moonshotai/Kimi-K3` (tp=8)
- Task mode: standalone single-GPU kernel optimization from captured workload files.
- Kept: max serving-profile GPU-time share `>= 3.0%`, non-comm, non-trtllm-MoE

| task | category | family | max % GPU | peak scenario | clean op |
|---|---|---|---:|---|---|
| `kimi_k3__sglang_cutedsl_tgv_bf16_gemm` | quant_gemm | linear_gemm | 41.2% | random_low | yes |
| `kimi_k3__sglang_attn_res_aggregate` | attention | attn_residual | 18.2% | sharegpt_high | mapped |
| `kimi_k3__sglang_kda_fused_decode` | attention | kda_fused_decode | 3.6% | random_high | mapped |

## Dropped < 3.0%

- attention: 2.7%
- moe_route_radix: 2.2%
- situ_and_mul: 2.0%
- per_token_group_quant: 1.6%
- pack_topk_ids_triton_kernel: 0.9%
- void_sglang_add3_kernel_true_tru: 0.8%
- rmsnorm: 0.8%
- kda_linear_attn: 0.7%
- attention_mla: 0.7%
- causal_conv1d: 0.3%
- void_at_native_elementwise_kerne: 0.1%
- void_at_native_index_elementwise: 0.1%
- void_at_native_vectorized_elemen: 0.1%
- void_at_native_unrolled_elementw: 0.1%
- void_at_native_reduce_kernel_512: 0.1%

## Excluded (comm / trtllm fused-MoE)

- void sglang::all_reduce_pull_res_kernel<8u, false, true (comm, comm): up to 27.9%
- bmm_MxE4m3_MxE2m1MxE4m3_Fp32_Ab32_Bb32_Cb32_t128x8x512_ (moe, fused_moe_trtllm): up to 26.6%
- bmm_Bfloat16_MxE2m1MxE4m3_Fp32_Ab32_Bb32_t128x8x512_s3_ (moe, fused_moe_trtllm): up to 19.1%
- void sglang::all_reduce_push_res_kernel<8u, true, true> (comm, comm): up to 15.4%
- void sglang::all_reduce_pull_res_kernel<8u, true, true> (comm, comm): up to 14.0%
- void (anonymous namespace)::all_reduce_kernel<(anonymou (comm, comm): up to 8.0%
- void sglang::all_reduce_push_norm_cluster_kernel<8u, 7u (comm, comm): up to 5.5%
- void sglang::all_reduce_pull_norm_kernel<2u, true>(sgla (comm, comm): up to 3.1%
- void moe::dev::routing::routingCustom::routingIndicesCl (moe, fused_moe_trtllm): up to 2.7%
- void moe::dev::routing::routingCustom::routingIndicesBl (moe, fused_moe_trtllm): up to 2.5%
