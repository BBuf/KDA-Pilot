# KDA Prompt: glm_46__rmsnorm

Target GPU: NVIDIA B200. Optimize the SGLang kernel behind:

- `<confirm via capture; profiler family=rmsnorm>`

**3.4% of total GPU time** on `zai-org/GLM-4.6-FP8` (cookbook-aligned profile, peak
`sharegpt_mid`) — a genuine end-to-end target selected by profiler e2e share. Family
`rmsnorm`, category `norm`.

See `docs/profile_evidence.md` for the per-scenario %-of-GPU, GPU kernels, shapes,
the cookbook deployment, and the scenario to re-run for the e2e A/B. Follow
`llm/docs/llm_kernel_optimization_rules.md` (CUDA, no DSL) + `llm/docs/llm_correctness_contract.md`.
