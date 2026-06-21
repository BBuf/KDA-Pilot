# Hunyuan3 Preview / B200 — run log

| Field | Value |
|---|---|
| Status | completed on `cirrascale-gpuc5a6` with cookbook image `lmsysorg/sglang:hy3-preview` |
| Target model | `tencent/Hy3-preview` |
| Cookbook doc | `Tencent/Hunyuan3-Preview.md` |
| Required GPUs | 8 B200, TP8 BF16 |
| Selected host | `cirrascale-gpuc5a6` / `bbuf@216.114.73.196` |
| Selected container | `sglang_bbuf_hunyuan3` from `lmsysorg/sglang:hy3-preview` |
| Serve port | `30000` |
| Shape threshold | `>2%` GPU kernel time |
| Cleanup | completed; `/root/.cache/huggingface/hub/models--tencent--Hy3-preview` removed after run, size before cleanup `557G` |

## Benchmark Summary

| Label | Dataset | Conc | Status | Shape rows |
|---|---|---:|---|---:|
| random_low | random | 1 | completed | 7 |
| random_mid | random | 32 | completed | 7 |
| random_high | random | 100 | completed | 3 |
| sharegpt_low | sharegpt | 1 | completed | 5 |
| sharegpt_mid | sharegpt | 32 | completed | 5 |
| sharegpt_high | sharegpt | 100 | completed | 4 |

## Progress Notes

- 2026-06-19: created from the live Hunyuan3 Preview cookbook page. The run
  uses the B200/TP8 BF16 command with the page's MTP/EAGLE flags, `hunyuan`
  reasoning/tool parsers, `SGLANG_ENABLE_SPEC_V2=1`, and explicit Blackwell
  `--attention-backend trtllm_mha`.
- 2026-06-19T10:39:01Z: launched via the generic serving/profile runner in
  container `sglang_bbuf_hunyuan3`, using all 8 B200 GPUs and port `30000`;
  runner PID `1283`.
- 2026-06-19T10:39:01Z: first launch failed before download because this
  cookbook image does not expose the `sglang` console script; switching to the
  equivalent `python3 -m sglang.launch_server` entrypoint.
- 2026-06-19T10:41:57Z: relaunched with `python3 -m sglang.launch_server`;
  runner PID `1461`.
- 2026-06-19T10:45:24Z: server is still in `server_start`; HF cache reached
  `55G`, all 8 TP ranks passed torch distributed init and entered weight
  loading, GPU memory around `72G` per B200.
- 2026-06-19T10:50:58Z: server is still loading weights; HF cache reached
  `184G`, runner/server processes are alive, GPU memory remains around `72G`
  per B200.
- 2026-06-19T10:53:15Z: HF cache reached `235G`; still in `server_start`
  while weights download/load.
- 2026-06-19T10:58:47Z: HF cache reached `372G`; runner/server remain alive
  and the run is still in weight download/load.
- 2026-06-19T11:04:18Z: HF cache reached `495G`; still loading weights, close
  to the documented `~552GB` BF16 checkpoint size.
- 2026-06-19T11:06:49Z: HF cache reached `552G`; server is not ready yet but
  runner/server remain alive with no OOM. Continuing to monitor the post-download
  weight-load phase.
- 2026-06-19T11:10:47Z: download completed and all TP ranks finished weight
  loading. KV cache was allocated and startup moved into CUDA graph / piecewise
  CUDA graph capture; GPU memory rose to roughly `160G` per B200.
- 2026-06-19T11:13:21Z: server became ready at `11:11:37Z`; `random_low`
  completed and shape extraction produced `kernel_shapes_random_low.json`.
  `random_mid` is running with all 8 B200s near full utilization.
- 2026-06-19T11:19:46Z: completed all six workload profiles and extracted only
  SGLang-relevant/actionable GPU kernel rows with profiler share `>2%`.
- 2026-06-19T11:20:34Z: cleaned the Hunyuan3 HF model cache; local verification
  passed with row counts `7/7/3/5/5/4` and all shape rows reported
  `shape_status=ok`.
