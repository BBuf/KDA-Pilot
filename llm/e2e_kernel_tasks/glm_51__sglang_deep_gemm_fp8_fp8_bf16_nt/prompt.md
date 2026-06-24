# KDA Prompt: glm_51__sglang_deep_gemm_fp8_fp8_bf16_nt

Target GPU: NVIDIA B200. Optimize the SGLang kernel behind:

- `sglang.deep_gemm_fp8_fp8_bf16_nt`

**20.6% of total GPU time** on `zai-org/GLM-5.1-FP8` (cookbook-aligned profile, peak
`random_low`) — a genuine end-to-end target selected by profiler e2e share. Family
`linear_gemm`, category `quant_gemm`.

See `docs/profile_evidence.md` for the per-scenario %-of-GPU, GPU kernels, shapes,
the cookbook deployment, and the scenario to re-run for the e2e A/B. Follow
`llm/docs/llm_kernel_optimization_rules.md` (CUDA, no DSL) + `llm/docs/llm_correctness_contract.md`.
