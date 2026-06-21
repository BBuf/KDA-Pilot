# Kimi-K2.7-Code / B200 — run log

| Field | Value |
|---|---|
| Status | completed + cleaned; 6 workload inventories synced locally |
| Target model | `moonshotai/Kimi-K2.7-Code` |
| Cookbook doc | `Moonshotai/Kimi-K2.7-Code.md` |
| Required GPUs | 8 |
| Selected host | `verda-b200-fin-03-2` via `ssh -J ubuntu@31.22.104.45 bbuf@verda-b200-fin-03-2` |
| Selected GPUs | GPU0-GPU7 idle at preflight |
| Serve port | `30000` |
| Current resource check | 2026-06-19: `/mnt/local_disk/bbuf` is writable, `/mnt/local_disk` has about 2.2T free at preflight, personal container `sglang_bbuf_kimi` created from refreshed `lmsysorg/sglang:latest` with SGLang `0.5.13.post1` |
| HF metadata preflight | OK, revision `74797c9c62378b951a1f6fcf5c4631024e9b8bef`, 64 safetensors |
| Shape threshold | `>2%` GPU kernel time |
| Cleanup | completed; runner deleted the 555G HF snapshot and lock after success |
| Runner PID | `2225` inside `sglang_bbuf_kimi` |
| Server PID | `2258` inside `sglang_bbuf_kimi` |

## Benchmark Summary

| Label | Dataset | Conc | Status | Shape rows |
|---|---|---:|---|---:|
| random_low | random | 1 | completed | 13 |
| random_mid | random | 32 | completed | 7 |
| random_high | random | 100 | completed | 11 |
| sharegpt_low | sharegpt | 1 | completed | 2 |
| sharegpt_mid | sharegpt | 32 | completed | 2 |
| sharegpt_high | sharegpt | 100 | completed | 11 |

## Progress Notes

- 2026-06-19T06:39:57Z: first launch used the wrong default `ROOT=/data/bbuf/kda-pilot/llm` on Verda; stopped before benchmark, killed the server, and manually deleted the partial 35G Kimi HF cache plus the container-overlay `/data/bbuf` run directory.
- 2026-06-19T06:43:55Z: relaunched with `ROOT=/mnt/local_disk/bbuf/kda-pilot/llm`, so run artifacts are on persistent local disk.
- 2026-06-19T06:44:04Z: launched the cookbook Kimi-K2.7-Code command on port
  `30000` with `CUDA_VISIBLE_DEVICES=0,1,2,3,4,5,6,7`; runner PID `2225`,
  server PID `2258`.
- 2026-06-19T06:51:34Z: server still in `server_start`; HF cache had reached
  about 101G, GPU memory was about 75GB per B200, and no benchmark/profile
  extraction had started yet.
- 2026-06-19T07:15:28Z: server still in `server_start`; HF cache had reached
  about 389G after resumed downloads, GPU memory was still about 75GB per B200,
  and no benchmark/profile extraction had started yet.
- 2026-06-19T07:37:29Z: completed all 6 workload benchmark/profile/extraction
  runs, then deleted
  `/root/.cache/huggingface/hub/models--moonshotai--Kimi-K2.7-Code`
  (`size_before=555G`) and the matching lock.
- 2026-06-19T07:38:00Z: synced `docs/`, `bench/`, `profile/`, `logs/`,
  `status.json`, and `status.md` back locally.
- Local verification after the relevant-kernel-only re-extraction: all 6
  `docs/kernel_shapes_*.json` files are present, row counts are
  `13/7/11/2/2/11`, every retained row has `sglang_relevant=true`, and every
  retained row has `pct_of_gpu > 2.0`.
