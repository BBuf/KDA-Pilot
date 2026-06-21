# DeepSeek-V3 B200 Kernel Shape Sweep

- Target: `deepseek-ai/DeepSeek-V3`
- Cookbook page: `DeepSeek/DeepSeek-V3.md`
- Recipe: B200 TP8 FP8 checkpoint with EAGLE speculative decoding, matching
  the DeepSeek-V3 cookbook's B200 deployment guidance.
- Status: completed + cleaned.
- Final row counts: `6/6/6/7/6/7`
  (`random_low/random_mid/random_high/sharegpt_low/sharegpt_mid/sharegpt_high`).
- Cleanup: HF cache `/root/.cache/huggingface/hub/models--deepseek-ai--DeepSeek-V3`
  deleted after profiling, `size_before=642G`; matching lock directory removed.
- Selected host: `cirrascale-gpuc5a6` / `bbuf@216.114.73.196`.
- Selected container: `sglang_bbuf_deepseek_v3`.
- Runner: launched 2026-06-19T17:23:31Z, runner PID `1148`,
  GPU0-7, port `30000`; log
  `deepseek_v3/b200/logs/runner_20260619T172331Z.log`.
- Validation: all six `kernel_shapes_*.json` files pass the `>2%`,
  `sglang_relevant`, non-empty samples, and provenance checks.
