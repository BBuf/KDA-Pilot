# Gemma 4 26B-A4B / B200 — run log

| Field | Value |
|---|---|
| Status | completed on `cirrascale-gpuc5a6` with cookbook image `lmsysorg/sglang:dev-gemma-4-12B` |
| Target model | `google/gemma-4-26B-A4B-it` |
| Cookbook doc | `Google/Gemma4.md` |
| Required GPUs | 1 B200, TP1 from the cookbook B200 command generator for 26B-A4B |
| Selected host | `cirrascale-gpuc5a6` / `bbuf@216.114.73.196` |
| Selected container | `sglang_bbuf_gemma4` from `lmsysorg/sglang:dev-gemma-4-12B` |
| Serve port | `30000` |
| Shape threshold | `>2%` GPU kernel time |
| Cleanup | completed; HF cache `models--google--gemma-4-26B-A4B-it` deleted, size before cleanup 49G |

## Benchmark Summary

| Label | Dataset | Conc | Status | Shape rows |
|---|---|---:|---|---:|
| random_low | random | 1 | completed | 11 |
| random_mid | random | 32 | completed | 10 |
| random_high | random | 100 | completed | 6 |
| sharegpt_low | sharegpt | 1 | completed | 11 |
| sharegpt_mid | sharegpt | 32 | completed | 8 |
| sharegpt_high | sharegpt | 100 | completed | 5 |

## Progress Notes

- 2026-06-19: created from the live Gemma4 cookbook page. The run targets the
  26B-A4B MoE variant for kernel coverage, uses the B200 TP1 text-generation
  command with `gemma4` reasoning/tool parsers, and leaves the separate MTP
  assistant-model path disabled for this baseline sweep.
- 2026-06-19T11:27:10Z: launched via the generic serving/profile runner in
  container `sglang_bbuf_gemma4`, using GPU0 and port `30000`; runner PID
  `1216`.
- 2026-06-19T11:36:47Z: completed all six workload profiles and cleaned 49G
  of Gemma4 weights. Local validation confirmed every recorded kernel row is
  `pct_of_gpu > 2%`, SGLang-relevant, shape status `ok`, and has provenance.
