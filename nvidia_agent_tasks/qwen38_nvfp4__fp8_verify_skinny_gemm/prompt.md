# qwen38_nvfp4__fp8_verify_skinny_gemm

Target GPU: NVIDIA RTX PRO 6000 Blackwell Server Edition (sm_120). Model: RadixArk/Qwen3.8-27B-NVFP4 - all attention/GDN projections are per-tensor-static
FP8 (the MLP is NVFP4, a separate task).

At M=1 decode the shipped `sm120_fp8_gemv_kernel` runs this family at ~95% of copy
bandwidth (**34.0% of the step**). Under DSpark the decode step becomes a fixed **M=9**
verify forward and the kernel - which is M=1-only - disappears entirely: the DSpark
verify profile shows the family re-routed to tiny-M cuBLAS tiles at **~27% of the
verify step** (sm89 64x128 10.3% + 32x64 8.4% + epilogue 7.6%). Extending the
weight-streaming fast path to M in [1, 16] converts that cliff directly into DSpark
output throughput.

bs=1 4k-in/1k-out: no-spec 66.7 tok/s (ITL 14.78 ms); DSpark 153.3 tok/s (ITL 3.48 ms, accept 3.47) - 2.30x. Verify forwards are fixed M=T=9 (block 8 + 1).

Contract: one kernel family covering both ops' rows - never slower than
`sm120_fp8_gemv` at M=1, beat the `apply_fp8_linear` cuBLAS route at M=9. The M=1
in_proj_qkvz row ships a real captured activation payload (weight reconstructs from
checkpoint metadata: [N,K]-contiguous fp8 + per-tensor scales). Evidence:
`docs/profile_evidence.md`. Side note: the adjacent in_proj_ba bf16 5120->96 GEMV
(cuBLAS dot+reduce pair, 3.8% of M=1 decode) may be folded as a bf16 tail output if
the candidate wants it - correctness-gated, optional.
