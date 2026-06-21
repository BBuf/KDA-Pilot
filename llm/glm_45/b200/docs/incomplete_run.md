# Incomplete B200 Run: glm_45

- Target model: `zai-org/GLM-4.5`
- Cookbook page: `GLM/GLM-4.5.md`
- Completion class: `download_failed`
- Shape JSON files captured: `0`
- Weights cleanup observed: `True`
- Resume hint: Resume from a clean HF cache or retry download; previous partial cache was cleaned.

## Status Summary

failed + cleaned; no shape artifacts; using live cookbook benchmark deployment command, Docker image `lmsysorg/sglang:latest`, BF16 TP8 on GPUs 0-7; official page benchmark section is AMD-oriented but command is generic SGLang TP8; launched in dedicated container `sglang_bbuf_glm_45` at 2026-06-20T10:33:55Z; progressed to HF cache `576G` / snapshot links `76/93`, then failed at 2026-06-20T12:07:26Z during HF download of `model-00084-of-00093.safetensors` with `httpx.RemoteProtocolError: peer closed connection without sending complete message body`; runner cleaned partial HF cache `584G` at 2026-06-20T12:07:49Z; container removed, GPU/cache clear, logs synced locally

## Local Artifacts

- `llm/glm_45/b200/logs/runner.log`
- `llm/glm_45/b200/logs/server.log`
- `llm/glm_45/b200/profile_config.sh`
- `llm/glm_45/b200/status.json`
- `llm/glm_45/b200/status.md`
