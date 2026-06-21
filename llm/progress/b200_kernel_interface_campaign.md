# B200 LLM Kernel Interface Campaign

Last updated: 2026-06-21T05:06:19Z.

Source baseline:

- SGLang cookbook: `sgl-project/sgl-cookbook@7b5bd9c05e3d86da5161ac2be9b91c19a34bf49d`
- Runtime SGLang checkout: `/data/bbuf/repos/sglang-main`
- Remote B200 node: `cirrascale-gpua83e` / `GPUA83E`
- Capture matrix: `random_low`, `random_mid`, `random_high`, `sharegpt_low`, `sharegpt_mid`, `sharegpt_high`
- Evidence source: SGLang kernel Python-interface logging with `SGLANG_KERNEL_API_LOGLEVEL=3`

## Queue

| Requested model | Slug | Status | Cookbook/source mapping | Selected model path | PR |
|---|---|---|---|---|---|
| Qwen3.6 | `qwen_36` | completed; local validation passed | `docs/autoregressive/Qwen/Qwen3.6.md` | `Qwen/Qwen3.6-35B-A3B-FP8` | #55 |
| DeepSeek-V4 | `deepseek_v4` | pending launch validation | Present on live docs at `docs.sglang.io/cookbook/autoregressive/DeepSeek/DeepSeek-V4`; absent from cloned cookbook `7b5bd9c`. | `deepseek-ai/DeepSeek-V4-Flash` as single-node B200 primary | pending |
| DeepSeek-V3_2 | `deepseek_v3_2` | pending | `docs/autoregressive/DeepSeek/DeepSeek-V3_2.md` B200 section | `deepseek-ai/DeepSeek-V3.2-Exp` | pending |
| Llama4 | `llama4` | pending | `docs/autoregressive/Llama/Llama4.md`; page covers Scout and Maverick variants. | TBD page variant | pending |
| Gemma4 | `gemma4` | pending | `docs/autoregressive/Google/Gemma4.md`; page covers E2B/E4B/31B/26B-A4B variants. | TBD page variant | pending |
| GPT-OSS | `gpt_oss` | pending | `docs/autoregressive/OpenAI/GPT-OSS.md` | `openai/gpt-oss-120b` | pending |
| Kimi-K2.7-Code | `kimi_k2_7_code` | pending launch validation | Not present in cloned cookbook `7b5bd9c`; HF deployment guide says K2.6/K2.5 launch method is reused. | `moonshotai/Kimi-K2.7-Code` | pending |
| Kimi-K2.6 | `kimi_k2_6` | pending | `docs/autoregressive/Moonshotai/Kimi-K2.6.md` | `moonshotai/Kimi-K2.6` | pending |
| MiniMax-M3 | `minimax_m3` | pending launch validation | Not present in cloned cookbook `7b5bd9c`; HF model exists. | `MiniMaxAI/MiniMax-M3` | pending |
| Nemotron3-Ultra | `nemotron3_ultra` | pending launch validation | Not present in cloned cookbook `7b5bd9c`; HF BF16 and NVFP4 variants exist. | `nvidia/NVIDIA-Nemotron-3-Ultra-550B-A55B-NVFP4` | pending |
| Ernie4.5 | `ernie_45` | pending | `docs/autoregressive/Ernie/Ernie4.5.md` | `baidu/ERNIE-4.5-21B-A3B-PT` | pending |
| Step-3.7-Flash | `step_37_flash` | pending launch validation | Not present in cloned cookbook `7b5bd9c`; HF model exists. | `stepfun-ai/Step-3.7-Flash` | pending |
| Ring-2.6-1T | `ring_26_1t` | pending launch validation | Not present in cloned cookbook `7b5bd9c`; HF model exists and is the successor of Ring-2.5-1T cookbook page. | `inclusionAI/Ring-2.6-1T` | pending |
| Intern-S2-Preview | `intern_s2_preview` | pending launch validation | Not present in cloned cookbook `7b5bd9c`; HF model and deployment guide exist. | `internlm/Intern-S2-Preview-FP8` | pending |
| Ministral-3 | `ministral_3` | pending | `docs/autoregressive/Mistral/Ministral-3.md` | `mistralai/Ministral-3-14B-Instruct-2512` | pending |
| MiMo-V2.5 | `mimo_v25` | pending launch validation | Not present in cloned cookbook `7b5bd9c`; HF model exists and follows MiMo-V2-Flash family. | `XiaomiMiMo/MiMo-V2.5` | pending |
| Hunyuan3-Preview | `hunyuan3_preview` | pending via SGLang docs | Not present in cookbook `7b5bd9c`; SGLang docs page `docs/basic_usage/hy3_preview.md`. | `tencent/Hy3-preview` | pending |
| Chroma1.0 | `chroma_10` | special deployment | `docs/autoregressive/FlashLabs/Chroma1.0.md`; hybrid Chroma-SGLang API server, not direct `sglang serve`. | `FlashLabs/Chroma-4B` plus Chroma-SGLang code | pending |

## Completed PRs

- GLM-5.2 reference implementation: PR #53, merged.
- Workload coverage wording fix: PR #54, merged.

## Current Notes

- Qwen3.6 default B200 attention path (`trtllm_mha`) failed during server warmup with a FlashInfer ABI mismatch: `trtllm_paged_attention_decode` expected 27 arguments but got 30. The Qwen3.6 wrapper now uses `--attention-backend triton --disable-flashinfer-autotune` to complete interface shape capture while preserving the cookbook FP8 model path, EAGLE parameters, and B200 `fa4` multimodal attention backend. A follow-up OOM during EAGLE draft torch.compile autotune required lowering `--mem-fraction-static` from `0.8` to `0.7`.
- Qwen3.6 generated 13 kernel interface tasks from 47,479 runtime Python-interface records. All task cards have non-empty direct interface shapes, non-zero calls/variants, and observed coverage for `random_low`, `random_mid`, `random_high`, `sharegpt_low`, `sharegpt_mid`, and `sharegpt_high`. The Qwen3.6 weight cache was manually removed after pulling artifacts.
