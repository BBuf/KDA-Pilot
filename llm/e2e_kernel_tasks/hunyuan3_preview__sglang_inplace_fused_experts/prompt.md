# KDA Prompt: hunyuan3_preview__sglang_inplace_fused_experts

Target GPU: NVIDIA B200. Optimize the SGLang kernel behind:

- `sglang.inplace_fused_experts`

**34.7% of total GPU time** on `tencent/Hy3-preview` (cookbook-aligned profile, peak
`random_mid`) — a genuine end-to-end target selected by profiler e2e share. Family
`fused_moe_triton`, category `moe`. Triton MoE expert-GEMM (sglang's own fused_experts/fused_moe kernel) — single-GPU optimizable; NOT the comm-fused trtllm MoE path (excluded).

See `docs/profile_evidence.md` for the per-scenario %-of-GPU, GPU kernels, shapes,
the cookbook deployment, and the scenario to re-run for the e2e A/B. Follow
`llm/docs/llm_kernel_optimization_rules.md` (CUDA, no DSL) + `llm/docs/llm_correctness_contract.md`.
