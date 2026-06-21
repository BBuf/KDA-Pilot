# Incomplete B200 Run: intern_s1

- Target model: `internlm/Intern-S1-FP8`
- Cookbook page: `InternLM/Intern-S1.md`
- Completion class: `launch_failed`
- Shape JSON files captured: `0`
- Weights cleanup observed: `True`
- Resume hint: Fix launch/import/quantization failure first, then run the six-workload profiler matrix.

## Status Summary

blocked + cleaned; failed before server_ready in `fused_inplace_qknorm` / `qknorm.cuh:214`, expected `head_dim=512` got `4096`; no shape JSON; partial model cache cleaned `232G`, tokenizer cache cleaned `5.1M`

## Local Artifacts

- `llm/intern_s1/b200/logs/runner_20260620T012944Z.log`
- `llm/intern_s1/b200/logs/server.log`
- `llm/intern_s1/b200/profile_config.sh`
- `llm/intern_s1/b200/run_log.md`
- `llm/intern_s1/b200/status.json`
- `llm/intern_s1/b200/status.md`
