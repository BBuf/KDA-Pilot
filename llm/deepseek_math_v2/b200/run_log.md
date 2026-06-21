# DeepSeek-Math-V2 B200 Kernel Shape Sweep

- Target: `deepseek-ai/DeepSeek-Math-V2`
- Cookbook page: `DeepSeek/DeepSeek-Math-V2.md`
- Recipe: B200 BF16 `tp=8`, `ep=8`, with `deepseek-r1` reasoning parser,
  matching the cookbook B200 deployment guidance.
- Status: completed + cleaned.
- Final row counts: `7/1/10/6/12/10`
  (`random_low/random_mid/random_high/sharegpt_low/sharegpt_mid/sharegpt_high`).
- Cleanup: retry run cleaned
  `/root/.cache/huggingface/hub/models--deepseek-ai--DeepSeek-Math-V2`,
  `size_before=643G`; matching lock directory removed. GPU memory returned to
  zero.
- Selected host: `cirrascale-gpuc5a6` / `bbuf@216.114.73.196`.
- Selected container: `sglang_bbuf_deepseek_math_v2`.
- Runner: launched 2026-06-19T18:07:30Z, runner PID `1147`,
  GPU0-7, port `30000`; log
  `deepseek_math_v2/b200/logs/runner_20260619T180730Z.log`.
- First attempt: failed during HF safetensors download with
  `httpx.RemoteProtocolError: peer closed connection without sending complete
  message body`; runner cleaned
  `/root/.cache/huggingface/hub/models--deepseek-ai--DeepSeek-Math-V2`,
  `size_before=185G`, plus the matching lock directory. GPU memory returned to
  zero. Retrying with longer HF timeout environment variables.
- Retry 1: launched 2026-06-19T18:21:58Z, runner PID `3573`, GPU0-7,
  port `30000`; log
  `deepseek_math_v2/b200/logs/runner_20260619T182158Z_retry1.log`.
- Retry 1 server ready: 2026-06-19T18:54:16Z. `random_low` completed and
  shape extraction produced `kernel_shapes_random_low.json`; all six workload
  shape extractions completed by 2026-06-19T19:04:14Z.
- Note: although the cookbook page describes BF16 weights, this SGLang build
  logged `Detected fp8 checkpoint` during the first load attempt.
- Validation: all six `kernel_shapes_*.json` files pass the `>2%`,
  `sglang_relevant`, non-empty samples, and provenance checks. Some rows have
  `shape_status=missing`, but still include profiler sample provenance.
- Workloads: `random_low`, `random_mid`, `random_high`, `sharegpt_low`,
  `sharegpt_mid`, `sharegpt_high`.
