# LFM2.5 8B-A1B / B200 — run log

| Field | Value |
|---|---|
| Status | completed on `cirrascale-gpuc5a6` with cookbook image `lmsysorg/sglang:dev-cu13` |
| Target model | `LiquidAI/LFM2.5-8B-A1B` |
| Cookbook doc | `LiquidAI/LFM2.5.md` |
| Required GPUs | 1 B200, TP1 from the verified B200 command matrix |
| Selected host | `cirrascale-gpuc5a6` / `bbuf@216.114.73.196` |
| Selected container | `sglang_bbuf_lfm25` from `lmsysorg/sglang:dev-cu13` |
| Serve port | `30000` |
| Shape threshold | `>2%` GPU kernel time |
| Cleanup | completed; HF cache `models--LiquidAI--LFM2.5-8B-A1B` deleted, size before cleanup 16G |

## Benchmark Summary

| Label | Dataset | Conc | Status | Shape rows |
|---|---|---:|---|---:|
| random_low | random | 1 | completed | 9 |
| random_mid | random | 32 | completed | 4 |
| random_high | random | 100 | completed | 3 |
| sharegpt_low | sharegpt | 1 | completed | 9 |
| sharegpt_mid | sharegpt | 32 | completed | 5 |
| sharegpt_high | sharegpt | 100 | completed | 5 |

## Progress Notes

- 2026-06-19: created from the live LFM2.5 cookbook page. The run targets the
  flagship text MoE `8B-A1B` variant because it exercises the hybrid short-conv
  plus sparse MoE path, and uses the verified B200 command: TP1,
  `--attention-backend flashinfer`, `--reasoning-parser qwen3`, and
  `--tool-call-parser lfm2`.
- 2026-06-19T11:43:44Z: launched via the generic serving/profile runner in
  container `sglang_bbuf_lfm25`, using GPU0 and port `30000`; runner PID `746`.
- 2026-06-19T12:02:20Z: completed all six workload profiles and cleaned 16G
  of LFM2.5 weights. Local validation confirmed every recorded kernel row is
  `pct_of_gpu > 2%`, SGLang-relevant, shape status `ok`, and has provenance.
  Startup log also noted a missing B200 Triton MoE kernel config for
  `E=32,N=1792`, which is worth keeping in mind when interpreting the MoE
  rows.
