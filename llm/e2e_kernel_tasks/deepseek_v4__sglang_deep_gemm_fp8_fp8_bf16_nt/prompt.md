# KDA Prompt: deepseek_v4__sglang_deep_gemm_fp8_fp8_bf16_nt

Target GPU: NVIDIA B200. Optimize the SGLang kernel behind:

- `sglang.deep_gemm_fp8_fp8_bf16_nt`

**15.9% of total GPU time** on `deepseek-ai/DeepSeek-V4-Flash` (cookbook-aligned profile, peak
`random_mid`) — a genuine end-to-end target selected by profiler e2e share. Family
`linear_gemm`, category `quant_gemm`.

See `docs/profile_evidence.md` for the per-scenario %-of-GPU, GPU kernels, shapes,
the cookbook deployment, and the scenario to re-run for the e2e A/B. Follow
`llm/docs/llm_kernel_optimization_rules.md` (CUDA, no DSL) + `llm/docs/llm_correctness_contract.md`.
