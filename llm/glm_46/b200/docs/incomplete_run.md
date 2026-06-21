# Incomplete B200 Run: glm_46

- Target model: `zai-org/GLM-4.6`
- Cookbook page: `GLM/GLM-4.6.md`
- Completion class: `runtime_blocked`
- Shape JSON files captured: `0`
- Weights cleanup observed: `True`
- Resume hint: Fix runtime kernel/server failure first; no promoted shape rows were captured.

## Status Summary

blocked + cleaned; reached server_ready, then watchdog killed TP ranks during piecewise CUDA graph replay in `random_low`; no shape JSON; HF cache cleaned `665G`

## Local Artifacts

- `llm/glm_46/b200/bench/bench_random_low.log`
- `llm/glm_46/b200/logs/runner_20260619T225852Z.log`
- `llm/glm_46/b200/logs/server.log`
- `llm/glm_46/b200/profile_config.sh`
- `llm/glm_46/b200/run_log.md`
- `llm/glm_46/b200/status.json`
- `llm/glm_46/b200/status.md`
