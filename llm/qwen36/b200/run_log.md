# Qwen3.6 / B200 — run log

| Field | Value |
|---|---|
| Status | completed + cleaned; 6 workload inventories synced locally |
| Target model | `Qwen/Qwen3.6-35B-A3B-FP8` |
| Cookbook doc | `Qwen/Qwen3.6.md` |
| Required GPUs | 1 B200 according to the cookbook hardware table for FP8 |
| Selected host | `cirrascale-gpuc5a6` / `bbuf@216.114.73.196` |
| Selected container | `sglang_bbuf_qwen36` from `lmsysorg/sglang:latest` |
| Serve port | `30000` |
| Shape threshold | `>2%` GPU kernel time |
| Cleanup | completed; deleted `/root/.cache/huggingface/hub/models--Qwen--Qwen3.6-35B-A3B-FP8`, size_before=35G, at 2026-06-19T09:36:44Z |

## Benchmark Summary

| Label | Dataset | Conc | Status | Shape rows |
|---|---|---:|---|---:|
| random_low | random | 1 | completed | 8 |
| random_mid | random | 32 | completed | 8 |
| random_high | random | 100 | completed | 7 |
| sharegpt_low | sharegpt | 1 | completed | 9 |
| sharegpt_mid | sharegpt | 32 | completed | 7 |
| sharegpt_high | sharegpt | 100 | completed | 7 |

## Progress Notes

- 2026-06-19: created after expanding the cookbook-intro sweep. The live
  Qwen3.6 page lists `Qwen/Qwen3.6-35B-A3B-FP8` and a B200 hardware table with
  FP8 TP=1.
- 2026-06-19T09:25:40Z: launched `run_qwen36_fp8.sh` in container
  `sglang_bbuf_qwen36` with `CUDA_VISIBLE_DEVICES=0`, runner PID `1440`, port
  `30000`.
- 2026-06-19T09:25:54Z: first launch failed before downloading weights because
  speculative decoding for `Qwen3_5MoeForConditionalGeneration` requires radix
  cache with `--mamba-scheduler-strategy extra_buffer` and
  `SGLANG_ENABLE_SPEC_V2=1`. The runner cleaned the 76K partial HF cache/lock.
- 2026-06-19T09:26:52Z: relaunched with `--mamba-scheduler-strategy
  extra_buffer` and `SGLANG_ENABLE_SPEC_V2=1`.
- 2026-06-19T09:36:39Z: completed all 6 workload benchmark/profile/extraction
  runs. Local verification after sync found row counts `8/8/7/9/7/7` for
  `random_low/random_mid/random_high/sharegpt_low/sharegpt_mid/sharegpt_high`;
  every retained row has `sglang_relevant=true`, sample provenance, and
  `pct_of_gpu > 2.0`.
- 2026-06-19T09:36:44Z: cleaned the completed 35G HF snapshot and matching lock.
