# DeepSeek-V4 B200 Kernel Shape Sweep

- Target: `deepseek-ai/DeepSeek-V4-Flash`
- Cookbook page: `DeepSeek/DeepSeek-V4.md`
- Recipe: B200 Flash FP4 verified TP-only cell: TP4, `flashinfer_mxfp4`, EAGLE, chunked prefill 4096, SWA full-token ratio 0.1.
- Scope note: this page also exposes `DeepSeek-V4-Pro`; Flash is the single-node 284B series target in the primary queue.
- Status: completed + cleaned.
- Selected host: `cirrascale-gpuc5a6` / `bbuf@216.114.73.196`.
- Selected container: `sglang_bbuf_deepseek_v4`.
- Runner: launched 2026-06-19T15:25:28Z, runner PID `1145`,
  GPU0-3, port `30000`; log
  `deepseek_v4/b200/logs/runner_20260619T152528Z.log`.
- Result: all six workloads completed and produced validated shape files:
  `random_low/random_mid/random_high/sharegpt_low/sharegpt_mid/sharegpt_high`
  row counts `2/4/3/3/4/4`.
- Validation: every retained row has `pct_of_gpu > 2%`, is marked
  SGLang-relevant/actionable, and includes samples with provenance; all
  extracted shape statuses are `ok`.
- Cleanup: HF cache
  `/root/.cache/huggingface/hub/models--deepseek-ai--DeepSeek-V4-Flash`
  and its lock were deleted after completion; size before cleanup was `149G`.
  The dedicated container was stopped and GPUs returned to 0 MiB.
