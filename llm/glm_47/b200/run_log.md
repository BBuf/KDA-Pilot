# GLM-4.7 B200 Kernel Shape Sweep

- Target: `zai-org/GLM-4.7`
- Cookbook page: `GLM/GLM-4.7.md`
- Recipe: generic cookbook invocation, TP8 BF16. The page's interactive
  generator is AMD-oriented, so this is marked as a B200 attempt rather than a
  B200-default command.
- Recipe correction: the local/live cookbook page lists
  `--reasoning-parser glm47`, but the current SGLang runtime rejects that as
  an invalid reasoning parser. The retry uses `--reasoning-parser glm45`
  with `--tool-call-parser glm47`, matching the GLM-5/GLM-5.1 and
  GLM-4.7-Flash parser pattern in current docs/runtime.
- Status: blocked + cleaned.
- Selected host: `cirrascale-gpuc5a6` / `bbuf@216.114.73.196`.
- Selected container: `sglang_bbuf_glm_47`.
- First attempt: launched 2026-06-19T22:10:21Z, failed before weight download
  because `glm47` is not a valid reasoning parser in the current runtime;
  cleanup reported cache size `absent`.
- Retry runner: launched 2026-06-19T22:14:23Z, runner PID `1506`,
  server PID `1513`, GPU0-7, port `30000`; log
  `glm_47/b200/logs/runner_20260619T221423Z.log`.
- Retry stage: server_start / distributed init and initial HF download;
  observed cache size was `20M` at 2026-06-19T22:15:02Z.
- Retry progress: weight loading started at 2026-06-19T22:15:12Z; observed
  HF cache size was `364G` at 2026-06-19T22:26:28Z, with about `86G`
  allocated on each GPU.
- Retry progress: observed HF cache size was `668G` at
  2026-06-19T22:37:14Z. Server log showed safetensor loading in progress
  (`11/93` shards), still in `server_start`.
- Retry progress: weights finished loading by 2026-06-19T22:43:00Z
  (`elapsed=1668s`), KV cache allocated `1,528,320` BF16 tokens, and
  piecewise CUDA graph capture completed at 2026-06-19T22:46:14Z. Server
  became ready at 2026-06-19T22:46:23Z and started `random_low`.
- Retry outcome: `random_low` did not complete. At 2026-06-19T22:53:58Z the
  server watchdog dumped all TP ranks while they were in CUDA graph replay
  (`cuda_piecewise_backend.py` / `prefill_cuda_graph_runner.py` path), waited
  for coredumps, and killed the server at 2026-06-19T22:54:58Z. The runner
  exited with code 1 and cleaned
  `/root/.cache/huggingface/hub/models--zai-org--GLM-4.7`, size before
  cleanup `668G`. No workload produced a completed shape JSON.
- Workloads: `random_low`, `random_mid`, `random_high`, `sharegpt_low`,
  `sharegpt_mid`, `sharegpt_high`.
