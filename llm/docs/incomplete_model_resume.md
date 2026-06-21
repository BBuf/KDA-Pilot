# Incomplete Model Resume Index

- Generated at: `2026-06-21T01:30:35Z`
- Attempted text LLM targets without completed shape collection: `14`
- Deferred cookbook targets outside the text-only matrix: `12`
- Completed models with promoted shape task cards live in `completed_model_task_index.md`.

## Attempted But Not Completed

| Folder | Class | Target model | Shape JSONs | Cleaned | Resume artifact | Status summary |
|---|---|---|---:|---|---|---|
| `llama4` | `access_gated` | `meta-llama/Llama-4-Maverick-17B-128E-Instruct` | 0 | `True` | `llm/llama4/b200/docs/incomplete_run.md` | blocked/gated + cleaned; HF 401 before `config.json` download, no weights downloaded |
| `mimo_v25` | `runtime_blocked` | `XiaomiMiMo/MiMo-V2.5` | 0 | `True` | `llm/mimo_v25/b200/docs/incomplete_run.md` | blocked + cleaned; official B200 `nightly-dev-cu13-20260511-044bb88a` tag not found, fallback `dev-mimo-v2.5` fails on B200 because FA3 vision attention is unsupported on Blackwell; no profiler traces |
| `glm_47` | `runtime_blocked` | `zai-org/GLM-4.7` | 0 | `True` | `llm/glm_47/b200/docs/incomplete_run.md` | blocked + cleaned; cookbook `glm47` reasoning failed before download, `glm45` reasoning + `glm47` tool parser reached server_ready but watchdog killed CUDA graph replay during `random_low`; no shape JSON; HF cache cleaned `668G` |
| `glm_46` | `runtime_blocked` | `zai-org/GLM-4.6` | 0 | `True` | `llm/glm_46/b200/docs/incomplete_run.md` | blocked + cleaned; reached server_ready, then watchdog killed TP ranks during piecewise CUDA graph replay in `random_low`; no shape JSON; HF cache cleaned `665G` |
| `ling_25_1t` | `topology_blocked` | `inclusionAI/Ling-2.5-1T` | 0 | `False` | `llm/ling_25_1t/b200/docs/incomplete_run.md` | topology blocked; cookbook B200 command requires `--tp-size 8 --pp-size 2 --nnodes 2`, so this single-node 8xB200 assignment cannot run it; no weights downloaded |
| `intern_s1` | `launch_failed` | `internlm/Intern-S1-FP8` | 0 | `True` | `llm/intern_s1/b200/docs/incomplete_run.md` | blocked + cleaned; failed before server_ready in `fused_inplace_qknorm` / `qknorm.cuh:214`, expected `head_dim=512` got `4096`; no shape JSON; partial model cache cleaned `232G`, tokenizer cache cleaned `5.1M` |
| `mistral_medium35` | `profiler_unavailable` | `mistralai/Mistral-Medium-3.5-128B` | 0 | `True` | `llm/mistral_medium35/b200/docs/incomplete_run.md` | blocked/profiler-unavailable + cleaned; generic `latest` failed before weights with `quant_config` string error, cookbook B200 image required; cookbook image loaded with added `--mem-fraction-static 0.85 --context-length 32768`, server_ready at 2026-06-20T0... |
| `devstral2` | `runtime_blocked` | `mistralai/Devstral-2-123B-Instruct-2512` | 0 | `True` | `llm/devstral2/b200/docs/incomplete_run.md` | blocked + cleaned; live cookbook B200 large config uses TP2 and requires recent transformers; `lmsysorg/sglang:latest` has `transformers 5.8.1` plus valid torch profiler GPU `kernel` events, but launch fails before weight download with `AttributeError: 'str... |
| `nemotron3_nano_omni` | `runtime_blocked` | `nvidia/Nemotron-3-Nano-Omni-30B-A3B-Reasoning-NVFP4` | 0 | `True` | `llm/nemotron3_nano_omni/b200/docs/incomplete_run.md` | blocked + cleaned; first launch 2026-06-20T07:11:24Z failed before weight download because multimodal `ParakeetExtractor` requires missing `librosa`, partial cache cleaned `18M`; second launch after installing `librosa` loaded the 3-shard NVFP4 checkpoint t... |
| `glm_45` | `download_failed` | `zai-org/GLM-4.5` | 0 | `True` | `llm/glm_45/b200/docs/incomplete_run.md` | failed + cleaned; no shape artifacts; using live cookbook benchmark deployment command, Docker image `lmsysorg/sglang:latest`, BF16 TP8 on GPUs 0-7; official page benchmark section is AMD-oriented but command is generic SGLang TP8; launched in dedicated con... |
| `llama31_405b` | `access_gated` | `meta-llama/Llama-3.1-405B-Instruct` | 0 | `True` | `llm/llama31_405b/b200/docs/incomplete_run.md` | blocked/gated + cleaned; no shape artifacts; lightweight HF `config.json` probe returned HTTP 401 on 2026-06-20, so the TP8 B200 run was not launched and no weights were downloaded |
| `llama31_70b` | `access_gated` | `meta-llama/Llama-3.1-70B` | 0 | `True` | `llm/llama31_70b/b200/docs/incomplete_run.md` | blocked/gated + cleaned; no shape artifacts; lightweight HF `config.json` probe returned HTTP 401 on 2026-06-20, so the TP1 B200 run was not launched and no weights were downloaded |
| `llama33_70b` | `access_gated` | `meta-llama/Llama-3.3-70B-Instruct` | 0 | `True` | `llm/llama33_70b/b200/docs/incomplete_run.md` | blocked/gated + cleaned; no shape artifacts; lightweight HF `config.json` probe returned HTTP 401 on 2026-06-20, so the TP1 B200 run was not launched and no weights were downloaded |
| `ministral3_14b` | `launch_failed` | `mistralai/Ministral-3-14B-Instruct-2512` | 0 | `True` | `llm/ministral3_14b/b200/docs/incomplete_run.md` | blocked + cleaned; no shape artifacts; HF `config.json` probe returned HTTP 200, but three launches failed before server_ready: default latest and explicit `--quantization fp8` both hit `AttributeError: 'str' object has no attribute 'get_quant_method'` in t... |

## Deferred Targets

| Folder / target | Scope | Page | Reason |
|---|---|---|---|
| `internvl35` | `deferred_non_text_or_placeholder` | `InternVL/InternVL3.5.md` | VLM page is currently a cookbook-contribution placeholder |
| `minicpm_v46` | `deferred_non_text_or_placeholder` | `OpenBMB/MiniCPM-V-4_6.md` | VLM model; needs image/video workload if profiled meaningfully |
| `jina_reranker_m0` | `deferred_non_text_or_placeholder` | `Jina/Jina-reranker-m0.md` | reranker workload, not generation benchmark |
| `chroma10` | `deferred_non_text_or_placeholder` | `FlashLabs/Chroma1.0.md` | custom FlashLabs deployment, not normal SGLang text generation server |
| `ernie45_vl` | `deferred_non_text_or_placeholder` | `Ernie/Ernie4.5-VL.md` | VLM page is currently a cookbook-contribution placeholder |
| `deepseek_ocr_ocr_2` | `deferred_additional_b200_marked_page` | `DeepSeek-OCR/OCR-2` | not attempted in the text-only random/ShareGPT sweep; needs modality-specific benchmark inputs |
| `glm_4_5v_4_6v_glyph_ocr` | `deferred_additional_b200_marked_page` | `GLM-4.5V/4.6V/Glyph/OCR` | not attempted in the text-only random/ShareGPT sweep; needs modality-specific benchmark inputs |
| `diffusiongemma` | `deferred_additional_b200_marked_page` | `DiffusionGemma` | not attempted in the text-only random/ShareGPT sweep; needs modality-specific benchmark inputs |
| `qwen2_5_vl` | `deferred_additional_b200_marked_page` | `Qwen2.5-VL` | not attempted in the text-only random/ShareGPT sweep; needs modality-specific benchmark inputs |
| `qwen3_vl` | `deferred_additional_b200_marked_page` | `Qwen3-VL` | not attempted in the text-only random/ShareGPT sweep; needs modality-specific benchmark inputs |
| `step3_vl_10b` | `deferred_additional_b200_marked_page` | `Step3-VL-10B` | not attempted in the text-only random/ShareGPT sweep; needs modality-specific benchmark inputs |
| `and_other_vlm_ocr_reranker_diffusion_custom_workloads` | `deferred_additional_b200_marked_page` | `and other VLM/OCR/reranker/diffusion/custom workloads` | not attempted in the text-only random/ShareGPT sweep; needs modality-specific benchmark inputs |
