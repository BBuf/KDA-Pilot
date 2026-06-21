# Step-3.7-Flash / B200 — run log

| Field | Value |
|---|---|
| Status | completed on `cirrascale-gpuc5a6` with `lmsysorg/sglang:latest` fallback |
| Target model | `stepfun-ai/Step-3.7-Flash-NVFP4` |
| Cookbook doc | `StepFun/Step-3.7-Flash.md` |
| Required GPUs | 8 B200, TP8/EP8 from the cookbook command generator for B200/B300 + NVFP4 |
| Selected host | `cirrascale-gpuc5a6` / `bbuf@216.114.73.196` |
| Selected container | `sglang_bbuf_step37` from `lmsysorg/sglang:latest`; cookbook recommends `lmsysorg/sglang:dev-step-3.7-flash`, but Docker pull returned not found on 2026-06-19 |
| Serve port | `30000` |
| Shape threshold | `>2%` GPU kernel time |
| Cleanup | completed; `/root/.cache/huggingface/hub/models--stepfun-ai--Step-3.7-Flash-NVFP4` removed after run, size before cleanup `121G` |

## Benchmark Summary

| Label | Dataset | Conc | Status | Shape rows |
|---|---|---:|---|---:|
| random_low | random | 1 | completed | 4 |
| random_mid | random | 32 | completed | 6 |
| random_high | random | 100 | completed | 5 |
| sharegpt_low | sharegpt | 1 | completed | 3 |
| sharegpt_mid | sharegpt | 32 | completed | 4 |
| sharegpt_high | sharegpt | 100 | completed | 3 |

## Progress Notes

- 2026-06-19: created from the live Step-3.7-Flash cookbook page. The text tips
  say B200/B300 are supported, while the command generator emits TP8 for
  B200/B300 and TP4 for GB200/GB300. This run follows the command generator
  with the NVFP4 option and records the discrepancy here for traceability.
- 2026-06-19T10:02Z: `docker pull lmsysorg/sglang:dev-step-3.7-flash` failed
  with `not found`; trying `lmsysorg/sglang:latest` with the same serve args.
- 2026-06-19T10:06:51Z: launched via the generic serving/profile runner in
  container `sglang_bbuf_step37`, using all 8 B200 GPUs and port `30000`;
  runner PID `1283`.
- 2026-06-19T10:22:46Z: completed all six workload profiles and extracted only
  SGLang-relevant/actionable GPU kernel rows with profiler share `>2%`.
- 2026-06-19T10:22:56Z: cleaned the Step-3.7-Flash HF model cache; local
  verification passed with row counts `4/6/5/3/4/3` and all shape rows
  reported `shape_status=ok`.
