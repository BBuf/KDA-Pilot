# KDA Prompt: nemotron3_nano__fused_add_rmsnorm

Target GPU: NVIDIA B200.

Optimize the SGLang kernel behind the Python interface:

- `<confirm via capture; profiler role=fused_add_rmsnorm>`

**This kernel is 4.4% of total GPU time** on `nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B-FP8` (cookbook-aligned
profile, peak in `sharegpt_low`) — a genuine end-to-end optimization target (selected
by profiler e2e share, not isolated micro-benchmark). Category: `gemm`.

See `docs/profile_evidence.md` for the per-scenario %-of-GPU breakdown, the GPU
kernel(s) involved, captured input shapes, and the exact cookbook deployment +
the scenario to re-run for the e2e A/B. Follow `llm/docs/llm_kernel_optimization_rules.md`
(CUDA, no DSL) and `llm/docs/llm_correctness_contract.md`.
