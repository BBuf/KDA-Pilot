# MiniMax-M3 / B200 — run log

| Field | Value |
|---|---|
| Status | completed + cleaned; 6 workload inventories synced locally |
| Target model | `MiniMaxAI/MiniMax-M3-MXFP8` |
| Cookbook doc | `MiniMax/MiniMax-M3.md` |
| Serve endpoint | server `:30000` |
| Required GPUs | 8 total, TP8 single server |
| Selected host | `cirrascale-gpua83e` / `bbuf@216.114.73.191` |
| Selected container | `sglang_bbuf_minimax_m3` from `lmsysorg/sglang:dev-minimax-m3` |
| Selected GPUs | GPU0-GPU7 idle at preflight |
| Current resource check | 2026-06-19: `/data/bbuf` is writable, `/data` has about 8.1T free at preflight, ports `30000/30001/8000/8998` were free |
| HF metadata preflight | OK, revision `1c4e6a69f3278df8dd6c9693fcca241efe439b7d`, 31 safetensors |
| Shape threshold | `>2%` GPU kernel time |
| Cleanup | completed; deleted `/root/.cache/huggingface/hub/models--MiniMaxAI--MiniMax-M3-MXFP8`, size_before=414G, at 2026-06-19T08:38:17Z |
| Runner PID | `11570` inside `sglang_bbuf_minimax_m3` (exited after completion) |
| Server PID | `11573` inside `sglang_bbuf_minimax_m3` (exited after completion) |

## Benchmark Summary

| Label | Dataset | Conc | Status | Shape rows |
|---|---|---:|---|---:|
| random_low | random | 1 | completed | 7 |
| random_mid | random | 32 | completed | 8 |
| random_high | random | 100 | completed | 8 |
| sharegpt_low | sharegpt | 1 | completed | 7 |
| sharegpt_mid | sharegpt | 32 | completed | 8 |
| sharegpt_high | sharegpt | 100 | completed | 8 |

## Progress Notes

- 2026-06-19T07:01:21Z: confirmed `cirrascale-gpua83e` had 8 idle B200 GPUs,
  free ports `30000/30001/8000/8998`, IB device `mlx5_0`, and about 8.1T free
  under `/data`.
- 2026-06-19T07:09:26Z: launched `run_minimax_m3_mxfp8.sh` in container
  `sglang_bbuf_minimax_m3`; runner PID `1294`, prefill PID `1299`.
- 2026-06-19T07:10:52Z: prefill server had started the cookbook
  PD-disaggregated command and was downloading/loading
  `MiniMaxAI/MiniMax-M3-MXFP8`; benchmark/profile extraction had not started.
- 2026-06-19T07:15:23Z: prefill server still in `prefill_start`; HF cache had
  reached about 168G, GPU0-GPU3 were using about 108G each, GPU4-GPU7 were still
  idle pending decode startup, and no benchmark/profile extraction had started.
- 2026-06-19T07:27:42Z: first attempt failed and cleaned the 414G partial
  snapshot. Root cause: local deploy notes used the wrong path for B200
  (`dev-cu13-minimax-m3` + PD-disagg); live cookbook B200 cell is
  `lmsysorg/sglang:dev-minimax-m3` with a single TP8 server.
- 2026-06-19T07:33:06Z: recreated `sglang_bbuf_minimax_m3` with
  `lmsysorg/sglang:dev-minimax-m3`, synced the corrected runner, and relaunched
  the single TP8 B200 command; runner PID `1288`.
- 2026-06-19T07:53:34Z: corrected TP8 attempt still failed during warmup with
  `AttributeError: Module has no function 'plan'` in `/opt/MSA/python/fmha_sm100`.
  The runner cleaned the 414G partial snapshot.
- 2026-06-19T08:03:55Z: cleared `/root/.cache/minfer/fmha_sm100` and
  single-process precompiled `plan`, `sparse_topk`, `reduction`, and FMHA
  variants `0_0_0_0_1_1_0` through `0_0_0_0_1_1_5` to avoid TP8 concurrent JIT
  writes to the shared MSA cache.
- 2026-06-19T08:04:05Z: relaunched the corrected TP8 runner after MSA JIT
  precompile; runner PID `11570`.
- 2026-06-19T08:26:07Z: server ready on port `30000`; started the six workload
  benchmark/profile/extract sequence.
- 2026-06-19T08:37:43Z: all six workloads completed and produced kernel shape
  inventories.
- 2026-06-19T08:38:17Z: cleaned the completed 414G HF snapshot and matching
  lock for `MiniMaxAI/MiniMax-M3-MXFP8`.
- Local verification after the relevant-kernel-only re-extraction: all 6
  `docs/kernel_shapes_*.json` files are present, row counts are
  `7/8/8/7/8/8`, every retained row has `sglang_relevant=true`, and every
  retained row has `pct_of_gpu > 2.0`.
