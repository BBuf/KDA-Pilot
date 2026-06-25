# KDA Prompt: llama33_70b__sglang_unified_attention_with_output

Target GPU: NVIDIA B200. Optimize the SGLang kernel behind:

- `sglang.unified_attention_with_output`

**3.6% of total GPU time** on `meta-llama/Llama-3.3-70B-Instruct` (cookbook-aligned profile, peak
`sharegpt_mid`) — a genuine end-to-end target selected by profiler e2e share. Family
`attention`, category `attention`.

See `docs/profile_evidence.md` for the per-scenario %-of-GPU, GPU kernels, shapes,
the cookbook deployment, and the scenario to re-run for the e2e A/B. Follow
`llm/docs/llm_kernel_optimization_rules.md` (CUDA, no DSL) + `llm/docs/llm_correctness_contract.md`.
