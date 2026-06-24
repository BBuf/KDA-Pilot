# KDA Prompt: deepseek_r1_fp4__sgl_kernel_dsv3_fused_a_gemm

Target GPU: NVIDIA B200. Optimize the SGLang kernel behind:

- `sgl_kernel.dsv3_fused_a_gemm`

**42.4% of total GPU time** on `nvidia/DeepSeek-R1-0528-FP4-v2` (cookbook-aligned profile, peak
`random_high`) — a genuine end-to-end target selected by profiler e2e share. Family
`linear_gemm`, category `quant_gemm`.

See `docs/profile_evidence.md` for the per-scenario %-of-GPU, GPU kernels, shapes,
the cookbook deployment, and the scenario to re-run for the e2e A/B. Follow
`llm/docs/llm_kernel_optimization_rules.md` (CUDA, no DSL) + `llm/docs/llm_correctness_contract.md`.
