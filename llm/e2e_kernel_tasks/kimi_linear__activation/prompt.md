# KDA Prompt: kimi_linear__activation

Target GPU: NVIDIA B200. Optimize the SGLang kernel behind:

- `<confirm via capture; profiler family=activation>`

**3.4% of total GPU time** on `moonshotai/Kimi-Linear-48B-A3B-Instruct` (cookbook-aligned profile, peak
`random_low`) — a genuine end-to-end target selected by profiler e2e share. Family
`activation`, category `other`. Activation (SiLU/GELU+mul). Prior guidance: limited headroom — deprioritize.

See `docs/profile_evidence.md` for the per-scenario %-of-GPU, GPU kernels, shapes,
the cookbook deployment, and the scenario to re-run for the e2e A/B. Follow
`llm/docs/llm_kernel_optimization_rules.md` (CUDA, no DSL) + `llm/docs/llm_correctness_contract.md`.
