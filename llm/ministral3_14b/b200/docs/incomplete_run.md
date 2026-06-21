# Incomplete B200 Run: ministral3_14b

- Target model: `mistralai/Ministral-3-14B-Instruct-2512`
- Cookbook page: `Mistral/Ministral-3.md`
- Completion class: `launch_failed`
- Shape JSON files captured: `0`
- Weights cleanup observed: `True`
- Resume hint: Fix launch/import/quantization failure first, then run the six-workload profiler matrix.

## Status Summary

blocked + cleaned; no shape artifacts; HF `config.json` probe returned HTTP 200, but three launches failed before server_ready: default latest and explicit `--quantization fp8` both hit `AttributeError: 'str' object has no attribute 'get_quant_method'` in the FP8 quant path, while the cookbook `transformers==5.0.0.rc0` preinstall retry failed at SGLang import with `StrictDataclassDefinitionError`; partial cache cleaned (`17M` when present), container removed, logs synced locally

## Local Artifacts

- `llm/ministral3_14b/b200/logs/runner.log`
- `llm/ministral3_14b/b200/logs/runner_first_attempt.log`
- `llm/ministral3_14b/b200/logs/runner_preinstall_attempt.log`
- `llm/ministral3_14b/b200/logs/server.log`
- `llm/ministral3_14b/b200/logs/server_first_attempt.log`
- `llm/ministral3_14b/b200/logs/server_preinstall_attempt.log`
- `llm/ministral3_14b/b200/profile_config.sh`
- `llm/ministral3_14b/b200/status.json`
- `llm/ministral3_14b/b200/status.md`
