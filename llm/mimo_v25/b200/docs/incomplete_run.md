# Incomplete B200 Run: mimo_v25

- Target model: `XiaomiMiMo/MiMo-V2.5`
- Cookbook page: `Xiaomi/MiMo-V2.5.md`
- Completion class: `runtime_blocked`
- Shape JSON files captured: `0`
- Weights cleanup observed: `True`
- Resume hint: Fix runtime kernel/server failure first; no promoted shape rows were captured.

## Status Summary

blocked + cleaned; official B200 `nightly-dev-cu13-20260511-044bb88a` tag not found, fallback `dev-mimo-v2.5` fails on B200 because FA3 vision attention is unsupported on Blackwell; no profiler traces

## Local Artifacts

- `llm/mimo_v25/b200/profile_config.sh`
- `llm/mimo_v25/b200/run_log.md`
