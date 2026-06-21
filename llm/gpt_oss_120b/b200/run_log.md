# GPT-OSS 120B / B200 — run log

| Field | Value |
|---|---|
| Status | completed + cleaned; 6 workload inventories synced locally |
| Target model | `openai/gpt-oss-120b` |
| Cookbook doc | `OpenAI/GPT-OSS.md` |
| Required GPUs | 8 B200, TP8 according to the cookbook B200/120B/MXFP4 command generator |
| Selected host | `cirrascale-gpuc5a6` / `bbuf@216.114.73.196` |
| Selected container | `sglang_bbuf_gptoss` from `lmsysorg/sglang:latest` |
| Serve port | `30000` |
| Shape threshold | `>2%` GPU kernel time |
| Cleanup | completed; deleted `/root/.cache/huggingface/hub/models--openai--gpt-oss-120b`, size_before=122G, at 2026-06-19T09:58:37Z |

## Benchmark Summary

| Label | Dataset | Conc | Status | Shape rows |
|---|---|---:|---|---:|
| random_low | random | 1 | completed | 14 |
| random_mid | random | 32 | completed | 12 |
| random_high | random | 100 | completed | 10 |
| sharegpt_low | sharegpt | 1 | completed | 11 |
| sharegpt_mid | sharegpt | 32 | completed | 11 |
| sharegpt_high | sharegpt | 100 | completed | 12 |

## Progress Notes

- 2026-06-19: created from the live GPT-OSS cookbook page. Default selected
  command generator settings are B200, 120B, MXFP4, no reasoning/tool parser,
  no speculative decoding, yielding `openai/gpt-oss-120b` with TP8.
- 2026-06-19T09:43:57Z: launched via the generic serving/profile runner in
  container `sglang_bbuf_gptoss`, using all 8 B200 GPUs and port `30000`;
  runner PID `1295`.
- 2026-06-19T09:58:26Z: completed all 6 workload benchmark/profile/extraction
  runs. Local verification after sync found row counts `14/12/10/11/11/12` for
  `random_low/random_mid/random_high/sharegpt_low/sharegpt_mid/sharegpt_high`;
  every retained row has `sglang_relevant=true`, sample provenance, and
  `pct_of_gpu > 2.0`.
- 2026-06-19T09:58:37Z: cleaned the completed 122G HF snapshot and matching
  lock.
