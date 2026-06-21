# Kimi-K2.5 B200 Kernel Shape Sweep

- Target: `moonshotai/Kimi-K2.5`.
- Cookbook page: `Moonshotai/Kimi-K2.5.md`.
- Recipe: the live cookbook page does not expose a B200 option for Kimi-K2.5;
  NVFP4 is restricted to B300/GB300. On this 8xB200 node use the H200-style
  default INT4 TP8 command with `kimi_k2` reasoning/tool parsers enabled,
  DP attention disabled, and speculative decoding disabled.
- Cleanup note: runner is configured to delete the primary HF cache.
- Status: completed + cleaned; launched on 2026-06-20T04:58:18Z in
  `sglang_bbuf_kimi_k25`; runner host PID `3418542`, server PID `1154`.
- Startup note: the first background launch wrote the PID file from the wrong
  working directory because of shell background precedence; the runner itself
  remained alive and `/data/bbuf/kda-pilot/llm/kimi_k25/b200/runner.pid` was
  corrected to the host runner PID.
- TP0-TP7 reached `Load weight begin` at 2026-06-20T04:59:10Z. HF cache
  observed at `27G`, `92G`, `183G`, `309G`, then `466G` with 8 incomplete
  shards and 48 safetensors; GPU memory about `75.8G` per card.
- Download completed at 2026-06-20T05:16:55Z: 64 safetensors, `555G`, no
  incomplete files. Multi-thread shard loading started immediately.
- TP0-TP7 finished `Load weight end` between 2026-06-20T05:20:04Z and
  2026-06-20T05:20:13Z. Weight memory usage is about `71.99G` per card and
  memory pool remaining memory is about `37.6G`.
- FlashInfer autotune and cuda graph capture completed; server_ready at
  2026-06-20T05:22:22Z.
- `random_low` benchmark and extraction completed at 2026-06-20T05:23:05Z.
  `random_mid` benchmark started at 2026-06-20T05:23:07Z.
- `random_mid` benchmark and extraction completed at 2026-06-20T05:25:20Z.
  `random_high` benchmark started at 2026-06-20T05:25:25Z.
- `random_high` extraction started at 2026-06-20T05:27:39Z, then
  `sharegpt_low` benchmark/extraction completed. `sharegpt_mid` extraction
  started at 2026-06-20T05:29:46Z.
- Completed all six workloads at 2026-06-20T05:31:39Z. Validated kernel shape
  rows: `9/7/10/8/3/9`; all rows are SGLang-relevant GPU kernels with
  `pct_of_gpu > 2`, samples, provenance, and `shape_status=ok`.
- Cleaned primary HF cache at 2026-06-20T05:32:19Z (`555G`), confirmed the
  cache directory is absent, removed `sglang_bbuf_kimi_k25`, and synced
  artifacts back locally.
- Workloads: `random_low`, `random_mid`, `random_high`, `sharegpt_low`,
  `sharegpt_mid`, `sharegpt_high`.
