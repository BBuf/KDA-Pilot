# KDA Prompt: ring_25_1t__void_at_native_unrolled_elementw

Target GPU: NVIDIA B200. Optimize the SGLang kernel behind:

- `<confirm via capture; profiler family=void_at_native_unrolled_elementw>`

**5.0% of total GPU time** on `inclusionAI/Ring-2.5-1T` (cookbook-aligned profile, peak
`random_high`) — a genuine end-to-end target selected by profiler e2e share. Family
`void_at_native_unrolled_elementw`, category `memory_bound`.

See `docs/profile_evidence.md` for the per-scenario %-of-GPU, GPU kernels, shapes,
the cookbook deployment, and the scenario to re-run for the e2e A/B. Follow
`llm/docs/llm_kernel_optimization_rules.md` (CUDA, no DSL) + `llm/docs/llm_correctness_contract.md`.
