# KDA Prompt: kimi_k26__sgl_kernel_dsv3_fused_a_gemm

Target GPU: NVIDIA B200. Optimize the SGLang kernel behind:

- `sgl_kernel.dsv3_fused_a_gemm`

**39.0% of total GPU time** on `moonshotai/Kimi-K2.6` (cookbook-aligned profile, peak
`random_low`) — a genuine end-to-end target selected by profiler e2e share. Family
`linear_gemm`, category `quant_gemm`.

See `docs/profile_evidence.md` for the per-scenario %-of-GPU, GPU kernels, shapes,
the cookbook deployment, and the scenario to re-run for the e2e A/B. Follow
`llm/docs/llm_kernel_optimization_rules.md` (CUDA, no DSL) + `llm/docs/llm_correctness_contract.md`.
