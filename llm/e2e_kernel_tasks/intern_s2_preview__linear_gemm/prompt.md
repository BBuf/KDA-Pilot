# KDA Prompt: intern_s2_preview__linear_gemm

Target GPU: NVIDIA B200. Optimize the SGLang kernel behind:

- `<confirm via capture; profiler family=linear_gemm>`

**42.0% of total GPU time** on `internlm/Intern-S2-Preview` (cookbook-aligned profile, peak
`random_low`) — a genuine end-to-end target selected by profiler e2e share. Family
`linear_gemm`, category `quant_gemm`.

See `docs/profile_evidence.md` for the per-scenario %-of-GPU, GPU kernels, shapes,
the cookbook deployment, and the scenario to re-run for the e2e A/B. Follow
`llm/docs/llm_kernel_optimization_rules.md` (CUDA, no DSL) + `llm/docs/llm_correctness_contract.md`.
