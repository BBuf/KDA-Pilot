# KDA Prompt: ling_26__linear_gemm

Target GPU: NVIDIA B200. Optimize the SGLang kernel behind:

- `<confirm via capture; profiler family=linear_gemm>`

**12.1% of total GPU time** on `inclusionAI/Ling-2.6-flash` (cookbook-aligned profile, peak
`random_mid`) — a genuine end-to-end target selected by profiler e2e share. Family
`linear_gemm`, category `gemm`.

See `docs/profile_evidence.md` for the per-scenario %-of-GPU, GPU kernels, shapes,
the cookbook deployment, and the scenario to re-run for the e2e A/B. Follow
`llm/docs/llm_kernel_optimization_rules.md` (CUDA, no DSL) + `llm/docs/llm_correctness_contract.md`.
