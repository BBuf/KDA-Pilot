# KDA Prompt: glm_5__void_anonymous_namespace_fast_ha

Target GPU: NVIDIA B200. Optimize the SGLang kernel behind:

- `<confirm via capture; profiler family=void_anonymous_namespace_fast_ha>`

**3.7% of total GPU time** on `nvidia/GLM-5-NVFP4` (cookbook-aligned profile, peak
`sharegpt_high`) — a genuine end-to-end target selected by profiler e2e share. Family
`void_anonymous_namespace_fast_ha`, category `other`.

See `docs/profile_evidence.md` for the per-scenario %-of-GPU, GPU kernels, shapes,
the cookbook deployment, and the scenario to re-run for the e2e A/B. Follow
`llm/docs/llm_kernel_optimization_rules.md` (CUDA, no DSL) + `llm/docs/llm_correctness_contract.md`.
