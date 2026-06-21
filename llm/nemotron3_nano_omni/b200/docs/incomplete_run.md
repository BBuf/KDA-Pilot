# Incomplete B200 Run: nemotron3_nano_omni

- Target model: `nvidia/Nemotron-3-Nano-Omni-30B-A3B-Reasoning-NVFP4`
- Cookbook page: `NVIDIA/Nemotron3-Nano-Omni.md`
- Completion class: `runtime_blocked`
- Shape JSON files captured: `0`
- Weights cleanup observed: `True`
- Resume hint: Fix runtime kernel/server failure first; no promoted shape rows were captured.

## Status Summary

blocked + cleaned; first launch 2026-06-20T07:11:24Z failed before weight download because multimodal `ParakeetExtractor` requires missing `librosa`, partial cache cleaned `18M`; second launch after installing `librosa` loaded the 3-shard NVFP4 checkpoint then failed during FlashInfer autotune/warmup in `cutlass_moe_fp4` with `AssertionError: mismatch in expected n`, cache cleaned `21G`, GPUs idle; third launch with `--moe-runner-backend flashinfer_cutedsl` failed before download because CuteDSL currently accepts only `modelopt_fp4` while this checkpoint is `modelopt_mixed`; fourth launch with `--disable-flashinfer-autotune` got past weight load but hit the same assert during CUDA graph capture bs=512, cache cleaned `21G`; fifth launch added `--disable-cuda-graph` and reached cache build, then failed because `MambaRadixCache` requires `page_size=1` but default `trtllm_mha` forced page size 64, cache cleaned `21G`; sixth launch used `--attention-backend flashinfer --page-size 1 --disable-flashinfer-autotune --disable-cuda-graph`, reached Uvicorn and initialized `MambaRadixCache`, then the first real generation path failed again in `cutlass_moe_fp4` with `AssertionError: mismatch in expected n`; no profiler shape rows, final HF cache cleaned `21G`, container removed

## Local Artifacts

- `llm/nemotron3_nano_omni/b200/logs/runner.log`
- `llm/nemotron3_nano_omni/b200/logs/runner_fifth_page64_assert_20260620T073325Z.log`
- `llm/nemotron3_nano_omni/b200/logs/runner_first_missing_librosa.log`
- `llm/nemotron3_nano_omni/b200/logs/runner_fourth_graph_assert_20260620T073033Z.log`
- `llm/nemotron3_nano_omni/b200/logs/runner_second_cutlass_assert_20260620T072516Z.log`
- `llm/nemotron3_nano_omni/b200/logs/runner_third_cutedsl_invalid_20260620T072739Z.log`
- `llm/nemotron3_nano_omni/b200/logs/server.log`
- `llm/nemotron3_nano_omni/b200/logs/server_fifth_page64_assert_20260620T073325Z.log`
- `llm/nemotron3_nano_omni/b200/logs/server_first_missing_librosa.log`
- `llm/nemotron3_nano_omni/b200/logs/server_fourth_graph_assert_20260620T073033Z.log`
- `llm/nemotron3_nano_omni/b200/logs/server_second_cutlass_assert_20260620T072516Z.log`
- `llm/nemotron3_nano_omni/b200/logs/server_third_cutedsl_invalid_20260620T072739Z.log`
- `llm/nemotron3_nano_omni/b200/profile_config.sh`
- `llm/nemotron3_nano_omni/b200/run_log.md`
- `llm/nemotron3_nano_omni/b200/status.json`
- `llm/nemotron3_nano_omni/b200/status.md`
