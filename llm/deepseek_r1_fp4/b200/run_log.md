# DeepSeek-R1 FP4 B200 Kernel Shape Sweep

- Target: `nvidia/DeepSeek-R1-0528-FP4-v2`
- Cookbook page: `DeepSeek/DeepSeek-R1.md`
- Recipe: B200-recommended FP4 checkpoint, TP8, `flashinfer_cutlass` MoE
  runner, EAGLE speculative decoding.
- Status: completed + cleaned.
- Selected host: `cirrascale-gpuc5a6` / `bbuf@216.114.73.196`.
- Selected container: `sglang_bbuf_deepseek_r1_fp4`.
- Runner: launched 2026-06-19T15:53:10Z, runner PID `1148`,
  GPU0-7, port `30000`; log
  `deepseek_r1_fp4/b200/logs/runner_20260619T155310Z.log`.
- Result: all six workloads completed and produced validated shape files:
  `random_low/random_mid/random_high/sharegpt_low/sharegpt_mid/sharegpt_high`
  row counts `6/8/10/7/12/9`.
- Validation: every retained row has `pct_of_gpu > 2%`, is marked
  SGLang-relevant/actionable, and includes samples with provenance; all
  extracted shape statuses are `ok`.
- Cleanup: HF cache
  `/root/.cache/huggingface/hub/models--nvidia--DeepSeek-R1-0528-FP4-v2`
  and its lock were deleted after completion; size before cleanup was `385G`.
  The dedicated container was stopped and GPUs returned to 0 MiB.
