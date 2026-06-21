# DeepSeek-V3.1 B200 Kernel Shape Sweep

- Target: `deepseek-ai/DeepSeek-V3.1`
- Cookbook page: `DeepSeek/DeepSeek-V3_1.md`
- Recipe: B200 TP8 FP8 checkpoint with EAGLE speculative decoding, matching
  the DeepSeek-V3.1 cookbook's B200 deployment guidance.
- Status: completed + cleaned.
- Selected host: `cirrascale-gpuc5a6` / `bbuf@216.114.73.196`.
- Selected container: `sglang_bbuf_deepseek_v31`.
- Runner: launched 2026-06-19T16:40:54Z, runner PID `1145`,
  GPU0-7, port `30000`; log
  `deepseek_v31/b200/logs/runner_20260619T164054Z.log`.
- Result: all six workloads completed and produced validated shape files:
  `random_low/random_mid/random_high/sharegpt_low/sharegpt_mid/sharegpt_high`
  row counts `6/6/6/5/7/6`.
- Validation: every retained row has `pct_of_gpu > 2%`, is marked
  SGLang-relevant/actionable, and includes samples with provenance; all
  extracted shape statuses are `ok`.
- Cleanup: HF cache
  `/root/.cache/huggingface/hub/models--deepseek-ai--DeepSeek-V3.1`
  and its lock were deleted after completion; size before cleanup was `642G`.
  The dedicated container was stopped and GPUs returned to 0 MiB.
