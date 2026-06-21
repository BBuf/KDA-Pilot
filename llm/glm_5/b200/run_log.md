# GLM-5 B200 Kernel Shape Sweep

- Target: `nvidia/GLM-5-NVFP4`
- Cookbook page: `GLM/GLM-5.md`
- Recipe: cookbook B200 default NVFP4 command, TP4, ModelOpt FP4
  quantization, FP8 KV cache, TRT-LLM NSA decode/prefill backends, and
  FlashInfer TRT-LLM MoE backend.
- Status: completed + cleaned.
- Selected host: `cirrascale-gpuc5a6` / `bbuf@216.114.73.196`.
- Selected container: `sglang_bbuf_glm_5`.
- Runner: launched 2026-06-19T19:58:00Z, runner PID `1182`,
  server PID `1186`, GPU0-3, port `30000`; log
  `glm_5/b200/logs/runner_20260619T195800Z.log`.
- Current stage: server_start / weight loading. The first snapshot was
  incomplete, so SGLang is downloading missing safetensors; observed HF cache
  size was `60G` at 2026-06-19T20:00:51Z and `232G` at
  2026-06-19T20:07:16Z, then `432G` at 2026-06-19T20:18:06Z.
- Current stage update: weights finished loading at 2026-06-19T20:25:13Z
  after `1584s`; final observed HF cache was `448G`. Server is running
  FlashInfer FP4 GEMM autotune (`1/17` observed at 2026-06-19T20:29:34Z).
- Retry note: the cookbook-default `mem-fraction-static=0.9` run reached
  `server_ready` and produced `random_low`/`random_mid`, but `random_high`
  OOMed in FlashInfer TRT-LLM FP4 MoE (`3.02GiB` allocation with only
  about `2.4-2.7GiB` free per active GPU). The failed log was preserved as
  `logs/server_mem09_random_high_oom.log`. The next retry uses
  `mem-fraction-static=0.85` to leave enough non-KV workspace for the
  high-concurrency workload.
- Retry runner: launched 2026-06-19T20:47:39Z, runner PID `10051`,
  server PID `10055`, log `glm_5/b200/logs/runner_20260619T204739Z.log`.
- Retry stage: loaded from local HF cache without re-download; weight loading
  took `55.8s`, KV cache was reduced to `842624` tokens / `43.34G`, leaving
  about `24.6G` free per active GPU. FlashInfer autotune cache completed in
  about `15s`; CUDA graph capture / warmup was still running at
  2026-06-19T20:54Z.
- Retry outcome: the second run exited during startup health checks and the
  runner cleaned the `448G` HF cache. Post-mortem showed stale tokenizer
  workers from the first crashed run were still listening on port `30000` in
  the container. The dirty container `sglang_bbuf_glm_5` was removed; GPU
  memory and port `30000` were confirmed free before the next retry.
- Fresh-container retry: launched 2026-06-19T21:02:39Z in a new
  `sglang_bbuf_glm_5` container, runner PID `1159`, server PID `1163`,
  log `glm_5/b200/logs/runner_20260619T210239Z.log`.
- Fresh-container retry progress: clean startup reached weight download;
  observed HF cache size was `168G` at 2026-06-19T21:08:36Z and `440G`
  at 2026-06-19T21:19:35Z.
- Fresh-container retry update: weights finished downloading/loading at
  2026-06-19T21:23:10Z, final cache `448G`, load time about `1183s`;
  KV cache is `842624` tokens / `43.34G`. FlashInfer FP4 GEMM autotune
  restarted in the new container.
- Fresh-container retry progress: at 2026-06-19T21:28Z the server was still
  healthy in `server_start`; FlashInfer FP4 GEMM autotune reached `1/17`
  profiles, with roughly `24.6G` free per active GPU after KV allocation.
- Fresh-container retry outcome: server became ready at
  2026-06-19T21:39:41Z. All six workloads completed; `random_high` passed
  with `mem-fraction-static=0.85`. Shape row counts were
  `12/10/8/11/12/10` for `random_low`, `random_mid`, `random_high`,
  `sharegpt_low`, `sharegpt_mid`, and `sharegpt_high`. The runner cleaned
  `/root/.cache/huggingface/hub/models--nvidia--GLM-5-NVFP4` after the
  completed run, size before cleanup `448G`.
- Workloads: `random_low`, `random_mid`, `random_high`, `sharegpt_low`,
  `sharegpt_mid`, `sharegpt_high`.
