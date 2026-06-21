# Nemotron3-Ultra NVFP4 / B200 — run log

| Field | Value |
|---|---|
| Status | completed on `cirrascale-gpuc5a6` with cookbook image `lmsysorg/sglang:dev-nemotron3-ultra` |
| Target model | `nvidia/NVIDIA-Nemotron-3-Ultra-550B-A55B-NVFP4` |
| Cookbook doc | `NVIDIA/Nemotron3-Ultra.md` |
| Required GPUs | 4 B200, TP4 from the cookbook default B200/NVFP4 command generator |
| Selected host | `cirrascale-gpuc5a6` / `bbuf@216.114.73.196` |
| Selected container | `sglang_bbuf_nemotron3_ultra` from `lmsysorg/sglang:dev-nemotron3-ultra` |
| Serve port | `30000` |
| Shape threshold | `>2%` GPU kernel time |
| Cleanup | completed; HF cache `models--nvidia--NVIDIA-Nemotron-3-Ultra-550B-A55B-NVFP4` deleted, size before cleanup 329G |

## Benchmark Summary

| Label | Dataset | Conc | Status | Shape rows |
|---|---|---:|---|---:|
| random_low | random | 1 | completed | 12 |
| random_mid | random | 32 | completed | 10 |
| random_high | random | 100 | completed | 7 |
| sharegpt_low | sharegpt | 1 | completed | 12 |
| sharegpt_mid | sharegpt | 32 | completed | 10 |
| sharegpt_high | sharegpt | 100 | completed | 8 |

## Progress Notes

- 2026-06-19: created from the live Nemotron3-Ultra cookbook page. The run uses
  the default verified B200/NVFP4 tuple emitted by the generator: TP4, MTP/EAGLE,
  `extra_buffer` mamba scheduling, `trtllm_mha` attention, `nemotron_3`
  reasoning parser, and `qwen3_coder` tool parser.
- 2026-06-19T12:08:06Z: launched via the generic serving/profile runner in
  container `sglang_bbuf_nemotron3_ultra`, using GPU0-3 and port `30000`;
  runner PID `906`.
- 2026-06-19T12:08:18Z: first launch failed before any weight download because
  image dependency versions were inconsistent: `transformers 5.8.1` imported
  HF `kernels 0.15.2`, whose `LayerRepository` / `FuncRepository` now require a
  revision or version. Patched the running container to default missing
  revision/version to `revision="main"` and verified `import sglang`.
- 2026-06-19T12:12:35Z: relaunched after the container-local dependency patch;
  new runner PID `1319`.
- 2026-06-19T12:40:31Z: completed all six workload profiles and cleaned 329G
  of Nemotron3-Ultra weights. Local validation confirmed every recorded kernel
  row is `pct_of_gpu > 2%`, SGLang-relevant, shape status `ok`, and has
  provenance.
