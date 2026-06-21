# Kimi-K2 B200 Kernel Shape Sweep

- Target: `moonshotai/Kimi-K2-Instruct`.
- Cookbook page: `Moonshotai/Kimi-K2.md`.
- Recipe: B200 TP8 launch with `--context-length 128000` per page memory
  guidance and `--tool-call-parser kimi_k2`. The cookbook benchmark section
  also lists DP/EP variants; for this shape collection pass, start with the
  single-node TP8 path to avoid turning the run into a DP deployment search.
- Status: completed + cleaned; launched on 2026-06-20T05:36:21Z in
  `sglang_bbuf_kimi_k2`; runner host PID `3496819`, server PID `1140`.
- TP0-TP7 reached `Load weight begin` at 2026-06-20T05:37:13Z. FP8
  checkpoint detected. HF cache observed at `59G`, `180G`, `326G`, then
  `433G`, `532G`, `650G`, `778G`, `901G`, then `958G` with 2 incomplete
  shards and 59 safetensors; GPU memory about `126G` per card.
- Workloads: `random_low`, `random_mid`, `random_high`, `sharegpt_low`,
  `sharegpt_mid`, `sharegpt_high`.
- Download completed at 2026-06-20T06:17:55Z: local HF snapshot ready, 61
  safetensors, no incomplete files. TP0-TP7 finished `Load weight end`
  between 2026-06-20T06:19:09Z and 2026-06-20T06:20:28Z. Weight memory usage
  is about `121.24G` per card and memory pool remaining memory is about
  `26.4G`.
- FlashInfer autotune and cuda graph capture completed; server_ready at
  2026-06-20T06:25:08Z.
- Completed all six workloads at 2026-06-20T06:33:55Z. The first extraction
  had Torch-Compiled-Region samples with empty shape args, so
  `extract_kernel_shapes.py` was updated to fall back from external-id matches
  without shapes to same-trace timestamp/nearest shape events. After rerunning
  extraction, validated kernel shape rows: `10/7/8/11/11/12`; all rows are
  SGLang-relevant GPU kernels with `pct_of_gpu > 2`, samples, provenance, and
  `shape_status=ok`.
- Cleaned primary HF cache at 2026-06-20T06:34:43Z (`959G`), confirmed the
  cache directory is absent, removed `sglang_bbuf_kimi_k2`, and synced
  artifacts back locally.
