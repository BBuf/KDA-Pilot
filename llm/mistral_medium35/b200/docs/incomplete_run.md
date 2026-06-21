# Incomplete B200 Run: mistral_medium35

- Target model: `mistralai/Mistral-Medium-3.5-128B`
- Cookbook page: `Mistral/Mistral-Medium-3.5.md`
- Completion class: `profiler_unavailable`
- Shape JSON files captured: `0`
- Weights cleanup observed: `True`
- Resume hint: Needs a container or torch/profiler path that emits Chrome trace GPU kernel events with names.

## Status Summary

blocked/profiler-unavailable + cleaned; generic `latest` failed before weights with `quant_config` string error, cookbook B200 image required; cookbook image loaded with added `--mem-fraction-static 0.85 --context-length 32768`, server_ready at 2026-06-20T03:26:27Z and `random_low` benchmark succeeded, but SGLang trace extraction failed because `torch.profiler` Chrome traces from `torch 2.9.1+cu130` contain no GPU `kernel` events; standalone matmul sanity checks showed the same `kernel_count=0`, while old autograd profiler has CUDA op time but no kernel names, so required `>2%` GPU-kernel shape rows cannot be collected from this image; cleaned primary `249G` and EAGLE draft `2.9G`

## Local Artifacts

- `llm/mistral_medium35/b200/bench/bench_random_low.log`
- `llm/mistral_medium35/b200/bench/random_low.jsonl`
- `llm/mistral_medium35/b200/logs/extract_random_low.log`
- `llm/mistral_medium35/b200/logs/runner.log`
- `llm/mistral_medium35/b200/logs/server.log`
- `llm/mistral_medium35/b200/logs_attempt_latest_failed/runner.log`
- `llm/mistral_medium35/b200/logs_attempt_latest_failed/server.log`
- `llm/mistral_medium35/b200/logs_attempt_latest_failed/status.json`
- `llm/mistral_medium35/b200/logs_attempt_latest_failed/status.md`
- `llm/mistral_medium35/b200/logs_attempt_mem_failed/runner.log`
- `llm/mistral_medium35/b200/logs_attempt_mem_failed/server.log`
- `llm/mistral_medium35/b200/logs_attempt_mem_failed/status.json`
- `llm/mistral_medium35/b200/logs_attempt_mem_failed/status.md`
- `llm/mistral_medium35/b200/profile_config.sh`
- `llm/mistral_medium35/b200/run_log.md`
- `llm/mistral_medium35/b200/status.json`
- `llm/mistral_medium35/b200/status.md`
