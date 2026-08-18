# KDA Prompt: qwen38_nvfp4__gdn_ba_proj_fold

Target GPU: NVIDIA RTX PRO 6000 Blackwell (SM120). Optimize the SGLang path
behind the GDN `in_proj_ba` projection of Qwen3.5-family hybrids
(`sglang.srt.models.qwen3_5`, bf16 `[5120 → 96]` linear).

**3.8% of bs=1 decode GPU time and 96 of ~1060 launches/step** on
`RadixArk/Qwen3.8-27B-NVFP4`: cuBLAS lowers this M=1, N=96 GEMV to a
`dot_kernel` + `reduce_1Block_kernel` pair per call (48 calls/step, 0.54 ms;
real capture, see `docs/profile_evidence.md`).

## Why this task

N=96 is far too narrow for any cuBLAS tile: the pair re-reads the full 5120-dim
activation and 5120×96 weight at trivial occupancy, twice per layer step
(dot + reduce). The same activation row is already being streamed by the
adjacent fp8 `in_proj_qkvz` GEMV (K=5120, N=16384) in the same layer. Every
verify step pays this flat cost regardless of accept length.

## Goal

Either of two acceptable shapes (candidate's choice):

1. **Dedicated skinny GEMV**: one kernel per call, single launch, activation
   read once, `M ∈ [1, 16]` × (K=5120, N=96), beating the cuBLAS pair at every
   tier.
2. **Folded variant**: extend the multi-row fp8 GEMV of
   `qwen38_nvfp4__sm120_fp8_gemv_multirow` with a bf16 side-output tail that
   computes the 96 extra columns while the activation tile is resident
   (weights for ba stay bf16 — do not quantize them). The benchmark for this
   variant times the fused kernel against baseline(qkvz GEMV) +
   baseline(cuBLAS ba pair).

## Contract

- Candidate API (variant 1): `run(x_bf16, w_ba_bf16) -> out_bf16[M, 96]`.
  Variant 2: the fused signature documented alongside the multirow task.
- Weight layout: `[K, N]` view of `[N, K]`-contiguous, bf16 (this projection is
  excluded from quantization in the checkpoint).
- Shapes: `bench/workloads.json`, M ∈ {1, 2, 4, 6, 8, 16}.
- Numerics: bf16 GEMV contract per `llm/docs/llm_correctness_contract.md`.
- Standalone single-GPU task; `llm/docs/llm_kernel_optimization_rules.md`
  applies (CUDA, no DSL).

## Baseline

`torch.nn.functional.linear` on the captured shapes (which lowers to the same
cuBLAS dot/reduce pair observed in production), pinned environment at task
creation. Score: geometric-mean speedup; no row regression.
