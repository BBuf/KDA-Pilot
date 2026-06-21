# Incomplete B200 Run: devstral2

- Target model: `mistralai/Devstral-2-123B-Instruct-2512`
- Cookbook page: `Mistral/Devstral-2.md`
- Completion class: `runtime_blocked`
- Shape JSON files captured: `0`
- Weights cleanup observed: `True`
- Resume hint: Fix runtime kernel/server failure first; no promoted shape rows were captured.

## Status Summary

blocked + cleaned; live cookbook B200 large config uses TP2 and requires recent transformers; `lmsysorg/sglang:latest` has `transformers 5.8.1` plus valid torch profiler GPU `kernel` events, but launch fails before weight download with `AttributeError: 'str' object has no attribute 'get_quant_method'` in the Ministral3 FP8 path; explicit `--quantization fp8` probe fails the same way; no Devstral-specific `lmsysorg/sglang` image tags found; partial HF cache cleaned `17M`

## Local Artifacts

- `llm/devstral2/b200/logs/manual_quant_fp8.log`
- `llm/devstral2/b200/logs/runner.log`
- `llm/devstral2/b200/logs/server.log`
- `llm/devstral2/b200/profile_config.sh`
- `llm/devstral2/b200/run_log.md`
- `llm/devstral2/b200/status.json`
- `llm/devstral2/b200/status.md`
