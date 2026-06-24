# KDA Prompt: qwen3_coder__fp8_bmm

Target GPU: NVIDIA B200. Optimize the SGLang kernel behind:

- `<confirm via capture; profiler family=fp8_bmm>`

**34.0% of total GPU time** on `Qwen/Qwen3-Coder-480B-A35B-Instruct-FP8` (cookbook-aligned profile, peak
`random_high`) — a genuine end-to-end target selected by profiler e2e share. Family
`fp8_bmm`, category `quant_gemm`.

See `docs/profile_evidence.md` for the per-scenario %-of-GPU, GPU kernels, shapes,
the cookbook deployment, and the scenario to re-run for the e2e A/B. Follow
`llm/docs/llm_kernel_optimization_rules.md` (CUDA, no DSL) + `llm/docs/llm_correctness_contract.md`.
