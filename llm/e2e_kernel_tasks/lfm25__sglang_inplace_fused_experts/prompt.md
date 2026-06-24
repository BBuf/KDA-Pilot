# KDA Prompt: lfm25__sglang_inplace_fused_experts

Target GPU: NVIDIA B200.

Optimize the SGLang kernel behind the Python interface:

- `sglang.inplace_fused_experts`

**This kernel is 50.5% of total GPU time** on `LiquidAI/LFM2.5-8B-A1B` (cookbook-aligned
profile, peak in `random_mid`) — a genuine end-to-end optimization target (selected
by profiler e2e share, not isolated micro-benchmark). Category: `moe`.

See `docs/profile_evidence.md` for the per-scenario %-of-GPU breakdown, the GPU
kernel(s) involved, captured input shapes, and the exact cookbook deployment +
the scenario to re-run for the e2e A/B. Follow `llm/docs/llm_kernel_optimization_rules.md`
(CUDA, no DSL) and `llm/docs/llm_correctness_contract.md`.
