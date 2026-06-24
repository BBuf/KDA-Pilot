# KDA Prompt: laguna_m1__void_apply_shuffle_mul_sum_kerne

Target GPU: NVIDIA B200. Optimize the SGLang kernel behind:

- `<confirm via capture; profiler family=void_apply_shuffle_mul_sum_kerne>`

**3.9% of total GPU time** on `poolside/Laguna-M.1-NVFP4` (cookbook-aligned profile, peak
`random_low`) — a genuine end-to-end target selected by profiler e2e share. Family
`void_apply_shuffle_mul_sum_kerne`, category `other`.

See `docs/profile_evidence.md` for the per-scenario %-of-GPU, GPU kernels, shapes,
the cookbook deployment, and the scenario to re-run for the e2e A/B. Follow
`llm/docs/llm_kernel_optimization_rules.md` (CUDA, no DSL) + `llm/docs/llm_correctness_contract.md`.
