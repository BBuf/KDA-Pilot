# GLM-5.2 / B200 — run log

| Field | Value |
|---|---|
| Status | completed; kernel inventories synced locally; weights cleaned |
| Target model | `zai-org/GLM-5.2-FP8` |
| Cookbook doc | `GLM/GLM-5.2.md` |
| Required GPUs | 8 |
| Selected host | `verda-b200-fin-03-1` via `ssh -J ubuntu@31.22.104.45 bbuf@verda-b200-fin-03-1` |
| Selected GPUs | GPU0-GPU7 idle at preflight |
| Serve port | `30000` |
| Current resource check | 2026-06-19: `/mnt/local_disk/bbuf` is writable, `/mnt/local_disk` has about 3.9T free at preflight, personal container `sglang_bbuf` created from `lmsysorg/sglang:latest` with SGLang `0.5.13.post1` |
| HF metadata preflight | OK, revision `a0b55e88465d1a06afece97bc8d6b366aff39089`, 141 safetensors |
| Shape threshold | `>2%` GPU kernel time |
| Cleanup | done; 704G HF snapshot and lock directory deleted by runner |
| Runner PID | `196` inside `sglang_bbuf` |
| Server PID | `228` inside `sglang_bbuf` |

## Benchmark Summary

| Label | Dataset | Conc | Status | Shape rows |
|---|---|---:|---|---:|
| random_low | random | 1 | completed | 9 |
| random_mid | random | 32 | completed | 11 |
| random_high | random | 100 | completed | 10 |
| sharegpt_low | sharegpt | 1 | completed | 9 |
| sharegpt_mid | sharegpt | 32 | completed | 4 |
| sharegpt_high | sharegpt | 100 | completed | 7 |

## Progress Notes

- 2026-06-19T05:56:48Z: runner started and downloaded ShareGPT dataset under
  `/mnt/local_disk/bbuf/kda-pilot/llm/sharegpt/`.
- 2026-06-19T05:56:56Z: launched the cookbook B200 FP8 balanced command on port
  `30000` with `CUDA_VISIBLE_DEVICES=0,1,2,3,4,5,6,7`.
- 2026-06-19T06:06:47Z: server still in `server_start`; runner PID `196`,
  server PID `228`; HF cache
  `/root/.cache/huggingface/hub/models--zai-org--GLM-5.2-FP8` had reached about
  194G, GPU memory was about 107GB per B200, and no benchmark/profile extraction
  had started yet.
- 2026-06-19T06:22:16Z: server still in `server_start`; HF cache had reached
  about 536G, GPU memory remained about 107GB per B200, and no
  benchmark/profile extraction had started yet.
- 2026-06-19T06:25:55Z: server still in `server_start`; HF cache had reached
  about 617G, runner/server remained alive, `/health` and `/health_generate`
  were not listening yet, and no benchmark/profile extraction had started yet.
- 2026-06-19T06:36:37Z: server became ready and started the benchmark/profile
  matrix.
- 2026-06-19T06:45:50Z: all six benchmark/profile/extract steps completed and
  the server began graceful shutdown.
- 2026-06-19T06:46:13Z: runner deleted
  `/root/.cache/huggingface/hub/models--zai-org--GLM-5.2-FP8`
  (`size_before=704G`) plus the matching lock directory.
- Local verification after the relevant-kernel-only re-extraction: all 6
  `docs/kernel_shapes_*.json` files are present, row counts are
  `9/11/10/9/4/7`, every retained row has `sglang_relevant=true`, and every
  retained row has `pct_of_gpu > 2.0`.
- The runner owns cleanup: on success or failure it kills the server and deletes
  the HF model cache and lock directory. Do not manually delete the GLM snapshot
  while PID `196`/`228` is alive.
