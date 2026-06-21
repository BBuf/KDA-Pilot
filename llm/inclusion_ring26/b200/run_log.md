# InclusionAI Ring-2.6-1T / B200 — run log

| Field | Value |
|---|---|
| Status | completed + cleaned |
| Target model | `inclusionAI/Ring-2.6-1T` |
| Cookbook doc | `InclusionAI/Ring-2.6-1T.md` |
| Required GPUs | 8 B200, TP8 from the cookbook command generator |
| Selected host | `cirrascale-gpuc5a6` / `bbuf@216.114.73.196` |
| Selected container | `sglang_bbuf_inclusion_ring26` using `lmsysorg/sglang:latest` |
| Serve port | `30000` |
| Shape threshold | `>2%` GPU kernel time |
| Cleanup | completed; HF cache deleted after run (`size_before=971G`) |

## Benchmark Summary

| Label | Dataset | Conc | Status | Shape rows |
|---|---|---:|---|---:|
| random_low | random | 1 | completed | 5 |
| random_mid | random | 32 | completed | 9 |
| random_high | random | 100 | completed | 8 |
| sharegpt_low | sharegpt | 1 | completed | 5 |
| sharegpt_mid | sharegpt | 32 | completed | 7 |
| sharegpt_high | sharegpt | 100 | completed | 8 |

## Progress Notes

- 2026-06-19: created from the live Ring-2.6-1T cookbook page. The run uses the
  verified B200 x8 command with TP8, `--mem-fraction-static 0.8`, multithreaded
  weight loading, `glm` tool parser, and `deepseek-r1` reasoning parser.
- 2026-06-19T13:23:49Z: launched runner PID `1287` on
  `sglang_bbuf_inclusion_ring26`; log
  `inclusion_ring26/b200/logs/runner_20260619T132349Z_latest.log`.
- 2026-06-19T13:32:54Z: server still in `server_start` / weight loading.
  `/health` not listening yet, no error traceback in `server.log`; HF cache grew
  to 242G and each B200 holds about 125G, indicating the large checkpoint is
  actively downloading/loading rather than failing on access.
- 2026-06-19T13:44:12Z: still in `server_start`; HF cache reached 580G, disk
  still has about 11T free, and there is still no error traceback. Continue
  waiting for checkpoint load to finish.
- 2026-06-19T13:55:47Z: HF cache reached 857G with 8 incomplete shard files.
  `server.log` reported one Hugging Face read timeout for
  `model-00126-of-00175.safetensors`; the server process stayed alive, so keep
  watching for automatic retry/progress before intervening.
- 2026-06-19T14:05:31Z: checkpoint download finished (`.incomplete=0`,
  cache about 971G). Server moved into multi-thread shard loading and reached
  `82/175` shards in the sampled log.
- 2026-06-19T14:13:39Z: server ready via `/health`; `random_low` benchmark and
  profiler completed and `docs/kernel_shapes_random_low.json` was generated.
  Runner is now in `random_mid`.
- 2026-06-19T14:19:09Z: `random_mid` benchmark/profile/extract completed and
  `docs/kernel_shapes_random_mid.json` was generated. Runner is now in
  `random_high`.
- 2026-06-19T14:22:55Z: `random_high` benchmark/profile/extract completed and
  `docs/kernel_shapes_random_high.json` was generated. Runner is now in
  `sharegpt_low`.
- 2026-06-19T14:26:43Z: `sharegpt_low` and `sharegpt_mid` completed with
  extracted shape JSON files. Runner is now in the final workload,
  `sharegpt_high`.
- 2026-06-19T14:30:34Z: all six workloads completed. Runner killed the server
  after extraction and deleted the HF cache (`size_before=971G`); GPU memory is
  back to 0 on all 8 B200s.
- 2026-06-19T14:31Z: local validation passed. Row counts are
  `5/9/8/5/7/8` for
  `random_low/random_mid/random_high/sharegpt_low/sharegpt_mid/sharegpt_high`.
  Every row has `pct_of_gpu > 2`, `sglang_relevant=true`, at least one sample,
  provenance, and `shape_status=ok`.
