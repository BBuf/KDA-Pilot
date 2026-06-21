# Intern-S2-Preview / B200 — run log

| Field | Value |
|---|---|
| Status | completed + cleaned |
| Target model | `internLM/Intern-S2-Preview` |
| Cookbook doc | `InternLM/Intern-S2-Preview.md` |
| Required GPUs | 8 B200, TP8 from the cookbook command generator |
| Selected host | `cirrascale-gpuc5a6` / `bbuf@216.114.73.196` |
| Selected container | `sglang_bbuf_intern_s2_preview` using `lmsysorg/sglang:latest` |
| Serve port | `30000` |
| Shape threshold | `>2%` GPU kernel time |
| Cleanup | completed; HF cache deleted after run (`size_before=69G`) |

## Benchmark Summary

| Label | Dataset | Conc | Status | Shape rows |
|---|---|---:|---|---:|
| random_low | random | 1 | completed | 4 |
| random_mid | random | 32 | completed | 6 |
| random_high | random | 100 | completed | 6 |
| sharegpt_low | sharegpt | 1 | completed | 5 |
| sharegpt_mid | sharegpt | 32 | completed | 4 |
| sharegpt_high | sharegpt | 100 | completed | 4 |

## Progress Notes

- 2026-06-19: created from the live Intern-S2-Preview cookbook page. The run
  follows the default B200 command: TP8, `qwen3` reasoning parser,
  `qwen3_coder` tool parser, MTP disabled, and `--mem-fraction-static 0.8`.
- 2026-06-19T14:35:50Z: launched runner PID `1213` on
  `sglang_bbuf_intern_s2_preview`; log
  `intern_s2_preview/b200/logs/runner_20260619T143550Z_latest.log`.
- 2026-06-19T14:36:20Z: first launch failed before weight download because
  Transformers requires custom repo code for `internLM/Intern-S2-Preview`.
  Added `--trust-remote-code` to this B200 config and will retry. The partial HF
  cache was only 68K and was cleaned by the runner.
- 2026-06-19T14:37:21Z: relaunched runner with `--trust-remote-code`, PID
  `1863`; log
  `intern_s2_preview/b200/logs/runner_20260619T143721Z_retry_trust_remote_code.log`.
- 2026-06-19T14:47:10Z: retry reached benchmark stage. Download completed
  with cache about 69G; `random_low` and `random_mid` profiles were extracted.
  Runner is now in `random_high`.
- 2026-06-19T14:51Z: all six workloads completed, HF cache was cleaned
  (`size_before=69G`), and local validation passed. Row counts are
  `4/6/6/5/4/4` for
  `random_low/random_mid/random_high/sharegpt_low/sharegpt_mid/sharegpt_high`.
  Every row has `pct_of_gpu > 2`, `sglang_relevant=true`, at least one sample,
  provenance, and `shape_status=ok`.
