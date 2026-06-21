# Qwen3.5 B200 Kernel Shape Sweep

- Target: `nvidia/Qwen3.5-397B-A17B-NVFP4`.
- Cookbook page: `Qwen/Qwen3.5.md`.
- Recipe: live cookbook B200 FP4/NVFP4 path, TP4, `modelopt_fp4`,
  `trtllm_mha`, `flashinfer_cutlass` FP4 GEMM, `flashinfer_trtllm` MoE,
  FP8 KV cache, Qwen reasoning/tool parsers, and 32768-token prefill chunks.
- Status: pending.
- Workloads: `random_low`, `random_mid`, `random_high`, `sharegpt_low`,
  `sharegpt_mid`, `sharegpt_high`.
