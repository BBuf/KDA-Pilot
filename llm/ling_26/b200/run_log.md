# Ling-2.6 B200 Kernel Shape Sweep

- Target: `inclusionAI/Ling-2.6-flash`.
- Cookbook page: `InclusionAI/Ling-2.6.md`.
- Recipe: cookbook B200 x4 baseline for Ling-2.6-flash, TP4 BF16,
  `--trust-remote-code`, 256K YaRN, and `--tool-call-parser qwen25`.
- Note: the same page also lists `inclusionAI/Ling-2.6-1T`, but the cookbook
  says B200/H200 need two nodes with `--pp-size 2`; this single 8xB200
  assignment is not enough for that variant.
- Status: completed + cleaned.
- Selected host: `cirrascale-gpuc5a6` / `bbuf@216.114.73.196`.
- Selected container: `sglang_bbuf_ling_26`.
- First launch note: the cookbook default 256K YaRN command failed before
  weight download because this runtime requires
  `SGLANG_ALLOW_OVERWRITE_LONGER_CONTEXT_LEN=1` when `--context-length 262144`
  exceeds the derived 131072 config length. The runner cleaned the 32K partial
  HF cache and the retry exports that env var.
- Retry: launched 2026-06-19T23:50:02Z, runner PID `1405`, server PID `1408`,
  GPU0-3, port `30000`. The server passed argument parsing and started TP4
  distributed init/weight loading by 2026-06-19T23:50:40Z; observed HF cache
  size was `8.3G` at 2026-06-19T23:50:57Z.
- Progress: server reached `/health` at 2026-06-19T23:58:43Z. `random_low`
  completed and extracted `4` valid `>2%` SGLang-relevant kernel rows by
  2026-06-19T23:59:19Z; `random_mid` is running.
- Outcome: all six workloads completed and validated. Row counts are
  `4/6/6/4/6/5` for `random_low`, `random_mid`, `random_high`,
  `sharegpt_low`, `sharegpt_mid`, and `sharegpt_high`. Every extracted row is
  `>2%`, SGLang-relevant, has samples, and has provenance. The runner cleaned
  `/root/.cache/huggingface/hub/models--inclusionAI--Ling-2.6-flash`
  (`201G`) at 2026-06-20T00:04:47Z.
- Workloads: `random_low`, `random_mid`, `random_high`, `sharegpt_low`,
  `sharegpt_mid`, `sharegpt_high`.
