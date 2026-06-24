# KDA Prompt: mistral_small4__sgl_kernel_fp8_scaled_mm

Target GPU: NVIDIA B200. Optimize the SGLang kernel behind:

- `sgl_kernel.fp8_scaled_mm`

**28.4% of total GPU time** on `mistralai/Mistral-Small-4-119B-2603` (cookbook-aligned profile, peak
`sharegpt_low`) — a genuine end-to-end target selected by profiler e2e share. Family
`linear_gemm`, category `gemm`.

See `docs/profile_evidence.md` for the per-scenario %-of-GPU, GPU kernels, shapes,
the cookbook deployment, and the scenario to re-run for the e2e A/B. Follow
`llm/docs/llm_kernel_optimization_rules.md` (CUDA, no DSL) + `llm/docs/llm_correctness_contract.md`.
