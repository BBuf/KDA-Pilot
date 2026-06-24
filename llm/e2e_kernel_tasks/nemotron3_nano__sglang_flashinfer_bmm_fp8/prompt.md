# KDA Prompt: nemotron3_nano__sglang_flashinfer_bmm_fp8

Target GPU: NVIDIA B200.

Optimize the SGLang kernel behind the Python interface:

- `sglang.flashinfer_bmm_fp8`

**This kernel is 20.7% of total GPU time** on `nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B-FP8` (cookbook-aligned
profile, peak in `random_mid`) — a genuine end-to-end optimization target (selected
by profiler e2e share, not isolated micro-benchmark). Category: `gemm`.

See `docs/profile_evidence.md` for the per-scenario %-of-GPU breakdown, the GPU
kernel(s) involved, captured input shapes, and the exact cookbook deployment +
the scenario to re-run for the e2e A/B. Follow `llm/docs/llm_kernel_optimization_rules.md`
(CUDA, no DSL) and `llm/docs/llm_correctness_contract.md`.
