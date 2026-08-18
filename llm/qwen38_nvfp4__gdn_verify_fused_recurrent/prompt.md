# KDA Prompt: qwen38_nvfp4__gdn_verify_fused_recurrent

Target GPU: NVIDIA RTX PRO 6000 Blackwell (SM120). Optimize the SGLang GDN
**speculative-verify** path (`--linear-attn-verify-backend triton`) of
Qwen3.5-family hybrids: the gated-delta-rule state update + output for a
short draft window `T ∈ [2, 9]`, plus the causal-conv1d update feeding it.

At M=1 decode this family is only ~2.3% of the step
(`fused_recurrent_gated_delta_rule_packed_decode` + conv-update + gated-LN,
see `docs/profile_evidence.md`), but the recurrent update is **sequential in
T**: under DSpark verify the same kernels either loop T times or fall to a
chunked prefill kernel built for T≥64, and the family is projected at 10-15%
of the verify step. This is the only non-GEMM family that grows with draft
length, so it caps the useful DSpark block size.

## Goal

A packed multi-token verify kernel: given the layer state
(`ssm_state [48, 128, 128]`, `conv_state [16384, 4]`) and `T ≤ 9` draft tokens
of q/k/v/b/a, produce the T outputs and the final states in one launch per
layer (or one launch per layer for conv + one for the delta rule), with the
in-T loop kept in registers/smem instead of T kernel launches or a
chunk-64-padded prefill call.

## Contract

- Candidate API: `run(q, k, v, b, a, ssm_state, conv_state_qkv) ->
  (out[1, T, 48, 128], ssm_state', conv_state')`. States update functionally
  (return fresh tensors) so rejected drafts can roll back — mutation in place
  is a correctness failure.
- Geometry (exact, from model config): 16 k-heads × 128, 48 v-heads × 128
  (head-group ratio 3), hidden 5120, conv kernel 4. `T ∈ {2, 4, 8}` tiers in
  `bench/workloads.json`.
- Numerics: match the pinned SGLang triton verify path within the contract in
  `llm/docs/llm_correctness_contract.md`; state tensors are correctness
  outputs, including the bf16 rounding of the stored state
  (`--mamba-ssm-dtype bfloat16`).
- **Shape provenance**: `workloads.json` geometry is exact but the verify-tier
  distribution is `derived_pending_capture`; refresh from the real DSpark
  capture per `llm/_INDEX_qwen38_nvfp4_dspark.md` before final scoring.
- Standalone single-GPU task; `llm/docs/llm_kernel_optimization_rules.md`
  applies. CUDA preferred; a Triton candidate is acceptable for this task
  only if it beats the baseline by the gate margin (the baseline itself is
  Triton).

## Baseline

The pinned SGLang triton verify path invoked exactly as production does for a
T-token verify (per-token recurrent loop or chunked call, whichever the pinned
revision dispatches), including the conv1d update. Score: geometric-mean
speedup across T tiers; the T=8 tier is the headline number.
