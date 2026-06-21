# GLM-4.7-Flash B200 Kernel Shape Sweep

- Target: `zai-org/GLM-4.7-Flash`
- Cookbook page: `GLM/GLM-4.7-Flash.md`
- Recipe: cookbook B200 command, TP1 BF16 with Triton attention backend.
- Status: completed + cleaned.
- Selected host: `cirrascale-gpuc5a6` / `bbuf@216.114.73.196`.
- Selected container: `sglang_bbuf_glm_47_flash`.
- Runner: launched 2026-06-19T21:53:30Z, runner PID `1313`,
  server PID `1320`, GPU0, port `30000`; log
  `glm_47_flash/b200/logs/runner_20260619T215330Z.log`.
- Current stage: server_start / initial HF download; observed cache size was
  `20M` at 2026-06-19T21:53:52Z.
- Outcome: server ready at 2026-06-19T21:57:15Z. All six workloads completed;
  shape row counts were `6/2/2/7/2/2` for `random_low`, `random_mid`,
  `random_high`, `sharegpt_low`, `sharegpt_mid`, and `sharegpt_high`. The
  runner cleaned `/root/.cache/huggingface/hub/models--zai-org--GLM-4.7-Flash`
  after the completed run, size before cleanup `59G`.
- Workloads: `random_low`, `random_mid`, `random_high`, `sharegpt_low`,
  `sharegpt_mid`, `sharegpt_high`.
