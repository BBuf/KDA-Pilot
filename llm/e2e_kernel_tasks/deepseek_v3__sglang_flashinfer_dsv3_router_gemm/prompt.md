# KDA Prompt: deepseek_v3__sglang_flashinfer_dsv3_router_gemm

Target GPU: NVIDIA B200. Optimize the SGLang kernel behind:

- `sglang.flashinfer_dsv3_router_gemm`

**16.4% of total GPU time** on `deepseek-ai/DeepSeek-V3` (cookbook-aligned profile, peak
`sharegpt_low`) — a genuine end-to-end target selected by profiler e2e share. Family
`attention`, category `gemm`.

See `docs/profile_evidence.md` for the per-scenario %-of-GPU, GPU kernels, shapes,
the cookbook deployment, and the scenario to re-run for the e2e A/B. Follow
`llm/docs/llm_kernel_optimization_rules.md` (CUDA, no DSL) + `llm/docs/llm_correctness_contract.md`.
