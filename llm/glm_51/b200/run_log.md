# GLM-5.1 B200 Kernel Shape Sweep

- Target: `zai-org/GLM-5.1-FP8`
- Cookbook page: `GLM/GLM-5.1.md`
- Recipe: FP8 `tp=8` with GLM tool/reasoning parsers, EAGLE speculative
  decoding, and `mem-fraction-static=0.85`, following the cookbook command.
- Status: completed + cleaned.
- Selected host: `cirrascale-gpuc5a6` / `bbuf@216.114.73.196`.
- Selected container: `sglang_bbuf_glm_51`.
- Runner: launched 2026-06-19T19:07:53Z, runner PID `1145`,
  GPU0-7, port `30000`; log
  `glm_51/b200/logs/runner_20260619T190753Z.log`.
- Result: all six workloads completed and passed shape JSON validation.
- Row counts: `5/7/5/4/5/5` for `random_low`, `random_mid`,
  `random_high`, `sharegpt_low`, `sharegpt_mid`, `sharegpt_high`.
- Cleanup: deleted HF cache
  `/root/.cache/huggingface/hub/models--zai-org--GLM-5.1-FP8`,
  `size_before=705G`, and removed the corresponding lock directory.
- Workloads: `random_low`, `random_mid`, `random_high`, `sharegpt_low`,
  `sharegpt_mid`, `sharegpt_high`.
