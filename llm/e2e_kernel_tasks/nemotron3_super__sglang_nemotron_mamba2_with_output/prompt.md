# KDA Prompt: nemotron3_super__sglang_nemotron_mamba2_with_output

Target GPU: NVIDIA B200. Optimize the SGLang kernel behind:

- `sglang.nemotron_mamba2_with_output`

**27.3% of total GPU time** on `nvidia/NVIDIA-Nemotron-3-Super-120B-A12B-BF16` (cookbook-aligned profile, peak
`random_high`) — a genuine end-to-end target selected by profiler e2e share. Family
`mamba2_ssm`, category `other`.

See `docs/profile_evidence.md` for the per-scenario %-of-GPU, GPU kernels, shapes,
the cookbook deployment, and the scenario to re-run for the e2e A/B. Follow
`llm/docs/llm_kernel_optimization_rules.md` (CUDA, no DSL) + `llm/docs/llm_correctness_contract.md`.
