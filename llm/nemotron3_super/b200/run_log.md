# Nemotron3-Super B200 Kernel Shape Sweep

- Target: `nvidia/NVIDIA-Nemotron-3-Super-120B-A12B-BF16`.
- Cookbook page: `NVIDIA/Nemotron3-Super.md`.
- Recipe: cookbook B200/Super command, TP4, `--trust-remote-code`,
  `--tool-call-parser qwen3_coder`, and `--reasoning-parser nemotron_3`.
- Status: completed + cleaned; launched on 2026-06-20T06:51:00Z in
  `sglang_bbuf_nemotron3_super`; runner host PID `3627299`, server PID `1141`.
- TP0-TP3 reached `Load weight begin` at 2026-06-20T06:51:46Z. HF cache
  observed at `78G`, then `205G` with 8 incomplete shards and 41 safetensors;
  GPU0-3 memory about `68G` per card.
- Download completed at 2026-06-20T06:58:31Z: 50 safetensors, `231G`, no
  incomplete files. TP0-TP3 finished `Load weight end` between
  2026-06-20T06:58:49Z and 2026-06-20T06:58:58Z. Weight memory usage is about
  `64.48G` per card and memory pool remaining memory is about `25.6G`.
- FlashInfer autotune and cuda graph capture completed; server_ready at
  2026-06-20T07:01:08Z. `random_low` benchmark started immediately.
- `random_low` benchmark/extraction completed at 2026-06-20T07:01:47Z.
  `random_mid` benchmark/extraction completed at 2026-06-20T07:03:22Z.
  `random_high` benchmark started at 2026-06-20T07:03:25Z.
- Workloads: `random_low`, `random_mid`, `random_high`, `sharegpt_low`,
  `sharegpt_mid`, `sharegpt_high`.
- Completed all six workloads at 2026-06-20T07:07:34Z. Validated kernel shape
  rows: `10/13/13/10/12/9`; all rows are SGLang-relevant GPU kernels with
  `pct_of_gpu > 2`, samples, provenance, and `shape_status=ok`.
- Cleaned primary HF cache at 2026-06-20T07:07:52Z (`231G`), confirmed the
  cache directory is absent, removed `sglang_bbuf_nemotron3_super`, and synced
  artifacts back locally.
