# Kimi-K2.6 B200 Kernel Shape Sweep

- Target: `moonshotai/Kimi-K2.6`.
- Cookbook page: `Moonshotai/Kimi-K2.6.md`.
- Recipe: live cookbook does not list B200 explicitly, but the native INT4
  checkpoint supports 8x >=140GB GPUs. On this 8xB200 node use the H200-style
  TP8 INT4 command with reasoning/tool parsers enabled and
  `--context-length 128000` per cookbook memory tip.
- Status: completed + cleaned; launched on 2026-06-20T03:47:03Z in
  `sglang_bbuf_kimi_k26`; runner PID `1147`, server PID `1150`.
- TP0-TP7 reached Load weight at 2026-06-20T03:47:54Z. HF cache
  observed at `270G`, then `524G`, then `540G`, then `551G`; still
  downloading/loading slowly under unauthenticated HF.
- Download completed: 64 safetensors, about `595.2G`, no incomplete files.
  Current phase: loading/autotuning FlashInfer TRTLLM MXINT4 MoE; GPU memory
  around `151G` per card.
- Server ready at 2026-06-20T04:37:12Z. Extracted `random_low` and
  `random_mid`; `random_high` benchmark started at 2026-06-20T04:40:14Z.
- Workloads: `random_low`, `random_mid`, `random_high`, `sharegpt_low`,
  `sharegpt_mid`, `sharegpt_high`.
- Completed all six workloads at 2026-06-20T04:46:28Z. Validated kernel shape
  rows: `8/7/9/8/7/8`; all rows are SGLang-relevant GPU kernels with
  `pct_of_gpu > 2`, samples, provenance, and `shape_status=ok`.
- Cleaned primary HF cache at 2026-06-20T04:47:08Z (`555G`) and confirmed the
  cache directory is absent. Artifacts were synced back locally.
