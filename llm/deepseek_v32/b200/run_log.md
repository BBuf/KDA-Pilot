# DeepSeek-V3.2 / B200 — run log

| Field | Value |
|---|---|
| Status | completed; kernel inventories synced locally; weights cleaned |
| Target model | `nvidia/DeepSeek-V3.2-NVFP4` |
| Cookbook doc | `DeepSeek/DeepSeek-V3_2.md` |
| Required GPUs | 4 |
| Selected host | `cirrascale-gpuc5a6` / `bbuf@216.114.73.196` |
| Selected GPUs | GPU0-GPU3 idle at preflight; GPU4-GPU7 occupied by an unrelated `glm-52-nvfp4` service and left untouched |
| Serve port | `30180` because port `30000` is occupied by the unrelated service |
| Current resource check | 2026-06-19: `cirrascale-gpuc5a6` has GPU0-GPU3 assigned to this run, `/data/bbuf` writable with ~12T free, personal container `sglang_bbuf` created from `lmsysorg/sglang:latest` |
| HF metadata preflight | OK, revision `7c0f62c6da1da0c81c6e097010cc55854d206812`, 163 safetensors |
| Shape threshold | `>2%` GPU kernel time |
| Cleanup | done; 387G HF snapshot and lock directory deleted by runner |
| Runner PID | `1617` inside `sglang_bbuf` |
| Server PID | `1625` inside `sglang_bbuf` |

## Benchmark Summary

| Label | Dataset | Conc | Status | Shape rows |
|---|---|---:|---|---:|
| random_low | random | 1 | completed | 10 |
| random_mid | random | 32 | completed | 7 |
| random_high | random | 100 | completed | 12 |
| sharegpt_low | sharegpt | 1 | completed | 10 |
| sharegpt_mid | sharegpt | 32 | completed | 12 |
| sharegpt_high | sharegpt | 100 | completed | 12 |

## Progress Notes

- 2026-06-19T05:23:04Z: launched official NVIDIA/B200 NVFP4 command on port
  `30180` with `CUDA_VISIBLE_DEVICES=0,1,2,3`.
- 2026-06-19T05:38:41Z: full local HF snapshot found after download at
  `/root/.cache/huggingface/hub/models--nvidia--DeepSeek-V3.2-NVFP4`, size about
  387G.
- 2026-06-19T05:39:56Z: `Load weight end` reported for all 4 TP ranks,
  `DeepseekV32ForCausalLM`, `quant=modelopt_fp4`, `quant_algo=NVFP4`.
- 2026-06-19T05:39:57Z: KV cache allocated with dtype `torch.float8_e4m3fn`,
  `#tokens=1375168`, KV size about 55.31GB per TP rank.
- 2026-06-19T05:44:03Z: FlashInfer FP4 GEMM autotune reached 1/20 profiles;
  `/health` was not ready yet, so benchmark/profile extraction has not started.
- 2026-06-19T05:56:26Z: server became ready and started the benchmark/profile
  matrix.
- 2026-06-19T06:04:00Z: all six benchmark/profile/extract steps completed.
- 2026-06-19T06:04:18Z: runner killed the server and deleted
  `/root/.cache/huggingface/hub/models--nvidia--DeepSeek-V3.2-NVFP4`
  (`size_before=387G`) plus the matching lock directory.
- Local verification after the relevant-kernel-only re-extraction: all 6
  `docs/kernel_shapes_*.json` files are present, row counts are
  `10/7/12/10/12/12`, every retained row has `sglang_relevant=true`, and every
  retained row has `pct_of_gpu > 2.0`.
