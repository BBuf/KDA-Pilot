# Mistral Small 4 FP8 / B200 — run log

| Field | Value |
|---|---|
| Status | completed + cleaned |
| Target model | `mistralai/Mistral-Small-4-119B-2603` |
| Cookbook doc | `Mistral/Mistral-Small-4.md` |
| Required GPUs | 1 B200, TP1 from the cookbook B200/FP8 command generator |
| Selected host | `cirrascale-gpuc5a6` / `bbuf@216.114.73.196` |
| Selected container | `sglang_bbuf_mistral_small4` using `lmsysorg/sglang:latest` |
| Serve port | `30000` |
| Shape threshold | `>2%` GPU kernel time |
| Cleanup | completed; HF cache deleted after run (`size_before=113G`) |

## Benchmark Summary

| Label | Dataset | Conc | Status | Shape rows |
|---|---|---:|---|---:|
| random_low | random | 1 | completed | 13 |
| random_mid | random | 32 | completed | 10 |
| random_high | random | 100 | completed | 10 |
| sharegpt_low | sharegpt | 1 | completed | 13 |
| sharegpt_mid | sharegpt | 32 | completed | 11 |
| sharegpt_high | sharegpt | 100 | completed | 11 |

## Progress Notes

- 2026-06-19: created from the live Mistral Small 4 cookbook page. The run uses
  the default B200/FP8 command with TP1, `mistral` reasoning/tool parsers, and
  speculative decoding disabled.
- 2026-06-19T14:55:46Z: launched runner PID `1210` on
  `sglang_bbuf_mistral_small4`; log
  `mistral_small4/b200/logs/runner_20260619T145546Z_latest.log`.
- 2026-06-19T15:02:15Z: server ready and `random_low` profile/extract
  completed. Runner is now in `random_mid`.
- 2026-06-19T15:06:07Z: `random_mid`, `random_high`, and `sharegpt_low`
  completed with extracted shape JSON files. Runner is now in `sharegpt_mid`.
- 2026-06-19T15:10Z: all six workloads completed, HF cache was cleaned
  (`size_before=113G`), and local validation passed. Row counts are
  `13/10/10/13/11/11` for
  `random_low/random_mid/random_high/sharegpt_low/sharegpt_mid/sharegpt_high`.
  Every row has `pct_of_gpu > 2`, `sglang_relevant=true`, at least one sample,
  provenance, and `shape_status=ok`.
