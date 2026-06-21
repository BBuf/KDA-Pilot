# Poolside Laguna-XS.2 FP8 / B200 — run log

| Field | Value |
|---|---|
| Status | completed on `cirrascale-gpuc5a6` with cookbook image `lmsysorg/sglang:dev-cu13-laguna-xs2` |
| Target model | `poolside/Laguna-XS.2-FP8` |
| Cookbook doc | `Poolside/Laguna-XS.2.md` |
| Required GPUs | 4 B200, TP4 retry for FP8 block alignment |
| Selected host | `cirrascale-gpuc5a6` / `bbuf@216.114.73.196` |
| Selected container | `sglang_bbuf_poolside_laguna_xs2` from `lmsysorg/sglang:dev-cu13-laguna-xs2` |
| Serve port | `30000` |
| Shape threshold | `>2%` GPU kernel time |
| Cleanup | completed; HF cache `models--poolside--Laguna-XS.2-FP8` deleted, size before cleanup 33G |

## Benchmark Summary

| Label | Dataset | Conc | Status | Shape rows |
|---|---|---:|---|---:|
| random_low | random | 1 | completed | 8 |
| random_mid | random | 32 | completed | 14 |
| random_high | random | 100 | completed | 10 |
| sharegpt_low | sharegpt | 1 | completed | 8 |
| sharegpt_mid | sharegpt | 32 | completed | 8 |
| sharegpt_high | sharegpt | 100 | completed | 7 |

## Progress Notes

- 2026-06-19: created from the live Laguna-XS.2 cookbook page. The run uses the
  FP8 checkpoint from the queue, TP8, `--trust-remote-code`, `poolside_v1`
  reasoning/tool parsers, and leaves DP attention disabled to match the default
  low-latency command.
- 2026-06-19T12:54:35Z: launched via the generic serving/profile runner in
  container `sglang_bbuf_poolside_laguna_xs2`, using GPU0-7 and port `30000`;
  runner PID `1222`.
- 2026-06-19T12:55:55Z: TP8 launch failed during FP8 weight load:
  `output_size=64` for gate/up was not divisible by quantization `block_n=128`.
  The official command generator hardcodes TP8, but the same cookbook page's
  benchmark section reports TP4. Retrying FP8 with TP4 on GPU0-3 so the shard
  output dimension aligns to the FP8 block size.
- 2026-06-19T13:03:17Z: relaunched TP4 retry in the same container; runner PID
  `3157`.
- 2026-06-19T13:11:55Z: TP4 retry completed all six workload profiles and
  cleaned 33G of Laguna-XS.2-FP8 weights. Local validation confirmed every
  recorded kernel row is `pct_of_gpu > 2%`, SGLang-relevant, and has provenance.
  `sharegpt_low` and `sharegpt_mid` include rows with `shape_status=missing`
  where torch profiler did not expose input shapes. Startup also logged missing
  B200 FP8 MoE configs for `E=256,N=128,block_shape=[128,128]`.
