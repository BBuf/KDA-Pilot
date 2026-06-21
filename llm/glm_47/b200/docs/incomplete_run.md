# Incomplete B200 Run: glm_47

- Target model: `zai-org/GLM-4.7`
- Cookbook page: `GLM/GLM-4.7.md`
- Completion class: `runtime_blocked`
- Shape JSON files captured: `0`
- Weights cleanup observed: `True`
- Resume hint: Fix runtime kernel/server failure first; no promoted shape rows were captured.

## Status Summary

blocked + cleaned; cookbook `glm47` reasoning failed before download, `glm45` reasoning + `glm47` tool parser reached server_ready but watchdog killed CUDA graph replay during `random_low`; no shape JSON; HF cache cleaned `668G`

## Local Artifacts

- `llm/glm_47/b200/bench/bench_random_low.log`
- `llm/glm_47/b200/logs/runner_20260619T221021Z.log`
- `llm/glm_47/b200/logs/runner_20260619T221423Z.log`
- `llm/glm_47/b200/logs/server.log`
- `llm/glm_47/b200/profile_config.sh`
- `llm/glm_47/b200/run_log.md`
- `llm/glm_47/b200/status.json`
- `llm/glm_47/b200/status.md`
