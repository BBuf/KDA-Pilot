## Fresh captured kernel API shapes

- Shape source: `docs/captured_kernel_api_shapes.json`
- Standalone workloads: `bench/workloads.json`
- Workload count: 9
- Capture note: Captured on a 2x4 GB300 devbox (sm_103, aarch64), sglang kimi-k3 @32e2db02d, moonshotai/Kimi-K3 tp=8 across 2 nodes, CUDA graphs disabled so every kernel keeps a Python launcher, 2026-07-28. Records are Python kernel-interface call contracts (tensor metadata only; no tensor values). Kimi-K3 issues 92 MoE and 93 attention layers per forward pass, so the hook's 256-calls-per-interface cap fills during the readiness generation that precedes the marked scenarios: entries are labelled 'unmarked' rather than carrying a scenario name. The set still spans both regimes - M=1 decode rows (TGV GEMM 1x7168) and M=76 batched rows (attention-residual, KDA fused decode).

Functions covered:
- `sglang.kernels.ops.gemm.cutedsl_bf16_gemm.cutedsl_bf16_gemm`
- `sglang.kernels.ops.gemm.cutedsl_bf16_gemm.cutedsl_bf16_gemm_out`
- `sglang.kernels.ops.gemm.tiny_gemm.tiny_k_gemm_bf16`
- `sglang.kernels.ops.gemm.tiny_gemm.tiny_n_gemm_bf16`

The old profiler `input_shapes` strings were noisy and are no longer an acceptance source.
Use the task-local workload file above for standalone single-GPU correctness and benchmark work.

## Validation Policy

Normal RLCR kernel work is a standalone single-GPU optimization task. Use the
captured workload set above for correctness and benchmark acceptance on one idle
target GPU, and keep external runtime-readiness or fleet-level A/B gates out of
the task loop.
