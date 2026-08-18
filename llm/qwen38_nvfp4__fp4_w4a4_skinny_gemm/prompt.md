# KDA Prompt: qwen38_nvfp4__fp4_w4a4_skinny_gemm

Target GPU: NVIDIA RTX PRO 6000 Blackwell (SM120). Optimize the SGLang kernel
path behind:

- `sglang.srt.layers.quantization.modelopt_quant.fp4_gemm` (flashinfer
  `mm_fp4`, cutlass backend on SM120)
- adjacent per-call activation quant: `flashinfer.fp4_quantize` /
  `tensorrt_llm::kernels::cvt_fp16_to_fp4` + block-scale quant

**50.5% of bs=1 decode GPU time** on `RadixArk/Qwen3.8-27B-NVFP4` (7.09 ms of a
13.39 ms step, 129 calls/step: 128 MLP GEMMs + lm_head; real torch-profiler
capture on the target GPU, see `docs/profile_evidence.md`).

## Why this task

At M=1 the cutlass path runs near the weight-bandwidth floor, but with DSpark
the step moves to `M ∈ [4, 9]` verify tiers where (a) flashinfer's tactic
dispatch on SM120 is untuned for tiny M (the same family measured ~8% off the
best-known config at large M on this GPU), and (b) the two standalone
activation-quant kernels per call stay on the critical path even though at
M≤16 the GEMM is entirely weight-bound — the activation could be consumed in
bf16 directly (mm_bf16_fp4-style: dequant weight in-kernel against bf16
activations reads the same weight bytes and removes both quant kernels and the
activation block-scale handling).

## Goal

A weight-streaming NVFP4-weight × activation skinny GEMM covering
`M ∈ [1, 16]` for the three captured `(K, N)` geometries, at or under the
weight-read time bound for every tier, never slower than the production path
at M=1, and removing the standalone activation-quant kernels from the timed
path for M ≤ 16 (fold or bypass — candidate's choice, correctness gated).

## Contract

- Candidate API: `run(x, w_fp4, w_scale_interleaved, alpha) -> out_bf16`.
  `x` may be consumed as bf16 `[M, K]` (preferred; quant folded/bypassed) or as
  the production prequantized pair — but the **timed region must include
  whatever activation transformation the candidate needs**, exactly as the
  baseline timing includes `fp4_quantize` + `mm_fp4`.
- Weight: `[N, K/2]` uint8 (packed e2m1 pairs) + swizzled 128×4 block scales +
  fp32 alpha, exactly the checkpoint layout. Offline repack allowed only as a
  one-time `prepare_benchmark` transform; document any repack.
- Shapes: `bench/workloads.json` — gate_up (K=5120, N=34816), down (K=17408,
  N=5120), lm_head (K=5120, N=248320) × M ∈ {1, 2, 4, 6, 8, 16}.
- Numerics: match the production dequant path within the NVFP4 contract in
  `llm/docs/llm_correctness_contract.md` (block-scale rounding ties tolerated).
- Standalone single-GPU task; follow `llm/docs/llm_kernel_optimization_rules.md`
  (CUDA, no DSL).

## Baseline

Production pair per row: `fp4_quantize(x_bf16)` + `mm_fp4(cutlass)` timed
together, pinned upstream main at task creation. Score: geometric-mean speedup
across rows; no row regression allowed. lm_head rows are worth the most
absolute time — do not tune only the MLP geometries.
