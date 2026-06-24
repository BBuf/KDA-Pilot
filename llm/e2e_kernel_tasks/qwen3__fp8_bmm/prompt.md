# KDA Prompt: qwen3__fp8_bmm

Target GPU: NVIDIA B200. Optimize the SGLang kernel behind:

- `<confirm via capture; profiler family=fp8_bmm>`

**32.0% of total GPU time** on `Qwen/Qwen3-235B-A22B-Instruct-2507` (cookbook-aligned profile, peak
`random_mid`) — a genuine end-to-end target selected by profiler e2e share. Family
`fp8_bmm`, category `other`.

See `docs/profile_evidence.md` for the per-scenario %-of-GPU, GPU kernels, shapes,
the cookbook deployment, and the scenario to re-run for the e2e A/B. Follow
`llm/docs/llm_kernel_optimization_rules.md` (CUDA, no DSL) + `llm/docs/llm_correctness_contract.md`.
