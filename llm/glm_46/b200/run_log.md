# GLM-4.6 B200 Kernel Shape Sweep

- Target: `zai-org/GLM-4.6`
- Cookbook page: `GLM/GLM-4.6.md`
- Recipe: cookbook B200 default command, TP8 BF16.
- Status: blocked + cleaned.
- Selected host: `cirrascale-gpuc5a6` / `bbuf@216.114.73.196`.
- Selected container: `sglang_bbuf_glm_46`.
- Runner: launched 2026-06-19T22:58:52Z, runner PID `1315`,
  server PID `1322`, GPU0-7, port `30000`; log
  `glm_46/b200/logs/runner_20260619T225852Z.log`.
- Current stage: server_start / initialization; no substantial HF cache was
  observed at 2026-06-19T22:59:10Z.
- Current stage update: distributed init completed and weight loading started
  at 2026-06-19T22:59:47Z; observed HF cache size was `329G` at
  2026-06-19T23:09:58Z, with about `86G` allocated on each GPU.
- Current stage update: observed HF cache size was `659G` at
  2026-06-19T23:20:57Z; server was still in `server_start` / weight loading.
- Current stage update: observed HF cache size was `665G` at
  2026-06-19T23:31:50Z. Weight load and regular CUDA graph capture had
  completed; piecewise CUDA graph compile/capture was in progress.
- Outcome: server reached `/health` at 2026-06-19T23:33:07Z, then
  `random_low` started. The scheduler watchdog dumped TP ranks at
  2026-06-19T23:40:41Z while they were replaying piecewise CUDA graphs
  (`cuda_piecewise_backend.py` / `prefill_cuda_graph_runner.py` /
  `glm4_moe.py`). The runner exited with code `1`, killed the server tree, and
  cleaned `/root/.cache/huggingface/hub/models--zai-org--GLM-4.6`
  (`665G`). No `kernel_shapes_*.json` files were produced.
- Workloads: `random_low`, `random_mid`, `random_high`, `sharegpt_low`,
  `sharegpt_mid`, `sharegpt_high`.
