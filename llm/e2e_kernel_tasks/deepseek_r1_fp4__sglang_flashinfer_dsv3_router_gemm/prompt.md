# KDA Prompt: deepseek_r1_fp4__sglang_flashinfer_dsv3_router_gemm

Target GPU: NVIDIA B200. Optimize the SGLang kernel behind:

- `sglang.flashinfer_dsv3_router_gemm`

**19.1% of total GPU time** on `nvidia/DeepSeek-R1-0528-FP4-v2` (cookbook-aligned profile, peak
`sharegpt_low`) — a genuine end-to-end target selected by profiler e2e share. Family
`attention`, category `gemm`.

See `docs/profile_evidence.md` for the per-scenario %-of-GPU, GPU kernels, shapes,
the cookbook deployment, and the scenario to re-run for the e2e A/B. Follow
`llm/docs/llm_kernel_optimization_rules.md` (CUDA, no DSL) + `llm/docs/llm_correctness_contract.md`.
