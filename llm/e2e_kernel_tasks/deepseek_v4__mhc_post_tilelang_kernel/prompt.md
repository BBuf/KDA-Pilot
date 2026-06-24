# KDA Prompt: deepseek_v4__mhc_post_tilelang_kernel

Target GPU: NVIDIA B200. Optimize the SGLang kernel behind:

- `<confirm via capture; profiler family=mhc_post_tilelang_kernel>`

**4.2% of total GPU time** on `deepseek-ai/DeepSeek-V4-Flash` (cookbook-aligned profile, peak
`random_mid`) — a genuine end-to-end target selected by profiler e2e share. Family
`mhc_post_tilelang_kernel`, category `other`.

See `docs/profile_evidence.md` for the per-scenario %-of-GPU, GPU kernels, shapes,
the cookbook deployment, and the scenario to re-run for the e2e A/B. Follow
`llm/docs/llm_kernel_optimization_rules.md` (CUDA, no DSL) + `llm/docs/llm_correctness_contract.md`.
