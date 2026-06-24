# KDA Prompt: step35_flash__sgl_kernel_gemma_rmsnorm

Target GPU: NVIDIA B200. Optimize the SGLang kernel behind:

- `sgl_kernel.gemma_rmsnorm`

**3.1% of total GPU time** on `stepfun-ai/Step-3.5-Flash` (cookbook-aligned profile, peak
`sharegpt_high`) — a genuine end-to-end target selected by profiler e2e share. Family
`rmsnorm`, category `norm`.

See `docs/profile_evidence.md` for the per-scenario %-of-GPU, GPU kernels, shapes,
the cookbook deployment, and the scenario to re-run for the e2e A/B. Follow
`llm/docs/llm_kernel_optimization_rules.md` (CUDA, no DSL) + `llm/docs/llm_correctness_contract.md`.
