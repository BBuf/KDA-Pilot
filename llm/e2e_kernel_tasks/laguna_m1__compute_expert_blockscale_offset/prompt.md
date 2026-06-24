# KDA Prompt: laguna_m1__compute_expert_blockscale_offset

Target GPU: NVIDIA B200. Optimize the SGLang kernel behind:

- `<confirm via capture; profiler family=compute_expert_blockscale_offset>`

**5.7% of total GPU time** on `poolside/Laguna-M.1-NVFP4` (cookbook-aligned profile, peak
`random_low`) — a genuine end-to-end target selected by profiler e2e share. Family
`compute_expert_blockscale_offset`, category `moe`.

See `docs/profile_evidence.md` for the per-scenario %-of-GPU, GPU kernels, shapes,
the cookbook deployment, and the scenario to re-run for the e2e A/B. Follow
`llm/docs/llm_kernel_optimization_rules.md` (CUDA, no DSL) + `llm/docs/llm_correctness_contract.md`.
