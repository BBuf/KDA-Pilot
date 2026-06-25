# KDA Prompt: ministral3_14b__attention

Target GPU: NVIDIA B200. Optimize the SGLang kernel behind:

- `<confirm via capture; profiler family=attention>`

**18.5% of total GPU time** on `mistralai/Ministral-3-14B-Instruct-2512` (cookbook-aligned profile, peak
`sharegpt_high`) — a genuine end-to-end target selected by profiler e2e share. Family
`attention`, category `attention`.

See `docs/profile_evidence.md` for the per-scenario %-of-GPU, GPU kernels, shapes,
the cookbook deployment, and the scenario to re-run for the e2e A/B. Follow
`llm/docs/llm_kernel_optimization_rules.md` (CUDA, no DSL) + `llm/docs/llm_correctness_contract.md`.
