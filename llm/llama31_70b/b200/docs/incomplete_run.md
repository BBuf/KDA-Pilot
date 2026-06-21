# Incomplete B200 Run: llama31_70b

- Target model: `meta-llama/Llama-3.1-70B`
- Cookbook page: `Llama/Llama3.1.md`
- Completion class: `access_gated`
- Shape JSON files captured: `0`
- Weights cleanup observed: `True`
- Resume hint: Need HF access token/approval before rerunning; no useful shape artifacts are expected until config probe succeeds.

## Status Summary

blocked/gated + cleaned; no shape artifacts; lightweight HF `config.json` probe returned HTTP 401 on 2026-06-20, so the TP1 B200 run was not launched and no weights were downloaded

## Local Artifacts

- `llm/llama31_70b/b200/profile_config.sh`
