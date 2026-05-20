# PR Discussion Digest

- Source PR: [NVIDIA/TensorRT-LLM#11990](https://github.com/NVIDIA/TensorRT-LLM/pull/11990)
- Source page: `sources/prs/tensorrt-llm/PR-11990.md`
- Evidence bundle: `evidence/pull-bundles/tensorrt-llm/gh-11990`
- Generated at: `2026-05-20T15:17:56.801505+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-03-06T19:51:00Z`
- Merged: `2026-03-18T04:38:40Z`

## Discussion Counts

- Issue comments: 62
- Review submissions: 48 (approved=7, changes_requested=1, commented=40)
- Inline review comments: 49
- Review threads observed: 24
- Resolved/outdated thread markers: resolved=24, outdated=24
- Human participants with discussion text: NVShreyas, StanleySun639, coderabbitai, kaiyux, leslie-fang25, longlee0622, nv-guomingz, sunnyqgg, tensorrt-cicd, xinhe-nv, yuxianq
- Automation comments/reviews omitted from high-signal summary: 1
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-03-06T20:02:18Z` `COMMENTED` by `coderabbitai` - Actionable comments posted: 8 [!CAUTION] Some comments are outside the diff and can’t be posted inline due to ... (https://github.com/NVIDIA/TensorRT-LLM/pull/11990#pullrequestreview-3905746776)
- `2026-03-09T01:50:02Z` `COMMENTED` by `nv-guomingz` (https://github.com/NVIDIA/TensorRT-LLM/pull/11990#pullrequestreview-3912451080)
- `2026-03-09T01:50:27Z` `COMMENTED` by `nv-guomingz` (https://github.com/NVIDIA/TensorRT-LLM/pull/11990#pullrequestreview-3912451711)
- `2026-03-09T01:57:52Z` `COMMENTED` by `nv-guomingz` (https://github.com/NVIDIA/TensorRT-LLM/pull/11990#pullrequestreview-3912469101)
- `2026-03-09T02:00:07Z` `COMMENTED` by `nv-guomingz` (https://github.com/NVIDIA/TensorRT-LLM/pull/11990#pullrequestreview-3912472399)
- `2026-03-09T02:01:54Z` `COMMENTED` by `nv-guomingz` (https://github.com/NVIDIA/TensorRT-LLM/pull/11990#pullrequestreview-3912475301)
- `2026-03-09T02:08:06Z` `COMMENTED` by `nv-guomingz` (https://github.com/NVIDIA/TensorRT-LLM/pull/11990#pullrequestreview-3912488375)
- `2026-03-09T02:09:21Z` `COMMENTED` by `nv-guomingz` (https://github.com/NVIDIA/TensorRT-LLM/pull/11990#pullrequestreview-3912490609)
- `2026-03-09T02:10:36Z` `COMMENTED` by `nv-guomingz` (https://github.com/NVIDIA/TensorRT-LLM/pull/11990#pullrequestreview-3912494306)
- `2026-03-09T02:10:54Z` `APPROVED` by `nv-guomingz` - LGTM on doc part. (https://github.com/NVIDIA/TensorRT-LLM/pull/11990#pullrequestreview-3912495018)
- `2026-03-09T02:15:30Z` `APPROVED` by `leslie-fang25` (https://github.com/NVIDIA/TensorRT-LLM/pull/11990#pullrequestreview-3912504122)
- `2026-03-09T02:34:31Z` `APPROVED` by `kaiyux` (https://github.com/NVIDIA/TensorRT-LLM/pull/11990#pullrequestreview-3912545699)
- `2026-03-09T04:00:51Z` `COMMENTED` by `yuxianq` (https://github.com/NVIDIA/TensorRT-LLM/pull/11990#pullrequestreview-3912742299)
- `2026-03-09T04:09:36Z` `COMMENTED` by `yuxianq` (https://github.com/NVIDIA/TensorRT-LLM/pull/11990#pullrequestreview-3912771046)
- `2026-03-09T04:16:34Z` `COMMENTED` by `yuxianq` (https://github.com/NVIDIA/TensorRT-LLM/pull/11990#pullrequestreview-3912784405)
- `2026-03-09T04:31:26Z` `COMMENTED` by `yuxianq` (https://github.com/NVIDIA/TensorRT-LLM/pull/11990#pullrequestreview-3912812841)
- `2026-03-09T04:32:11Z` `COMMENTED` by `yuxianq` (https://github.com/NVIDIA/TensorRT-LLM/pull/11990#pullrequestreview-3912814256)
- `2026-03-09T04:46:08Z` `COMMENTED` by `yuxianq` (https://github.com/NVIDIA/TensorRT-LLM/pull/11990#pullrequestreview-3912843298)
- `2026-03-09T07:47:27Z` `COMMENTED` by `sunnyqgg` (https://github.com/NVIDIA/TensorRT-LLM/pull/11990#pullrequestreview-3913468212)
- `2026-03-09T07:52:38Z` `CHANGES_REQUESTED` by `sunnyqgg` (https://github.com/NVIDIA/TensorRT-LLM/pull/11990#pullrequestreview-3913489716)
- `2026-03-09T17:44:30Z` `COMMENTED` by `NVShreyas` (https://github.com/NVIDIA/TensorRT-LLM/pull/11990#pullrequestreview-3917163427)
- `2026-03-09T17:44:47Z` `COMMENTED` by `NVShreyas` (https://github.com/NVIDIA/TensorRT-LLM/pull/11990#pullrequestreview-3917164999)
- `2026-03-09T17:46:38Z` `COMMENTED` by `NVShreyas` (https://github.com/NVIDIA/TensorRT-LLM/pull/11990#pullrequestreview-3917175633)
- `2026-03-09T17:46:51Z` `COMMENTED` by `NVShreyas` (https://github.com/NVIDIA/TensorRT-LLM/pull/11990#pullrequestreview-3917177157)
- ... 24 additional review decision entries omitted from this digest.

## Inline Comment Hotspots

- `examples/models/core/glm-5/README.md`: 18 inline comment(s)
- `tensorrt_llm/_torch/speculative/interface.py`: 10 inline comment(s)
- `tensorrt_llm/tokenizer/glm_moe_dsa/tokenizer.py`: 5 inline comment(s)
- `tensorrt_llm/_torch/pyexecutor/model_engine.py`: 4 inline comment(s)
- `tensorrt_llm/_torch/models/modeling_deepseekv3.py`: 3 inline comment(s)
- `examples/models/core/glm-5/perf.png`: 3 inline comment(s)
- `tensorrt_llm/_torch/attention_backend/trtllm.py`: 2 inline comment(s)
- `tests/integration/test_lists/test-db/l0_dgx_b200.yml`: 2 inline comment(s)
- `tensorrt_llm/_torch/model_config.py`: 1 inline comment(s)
- `tensorrt_llm/tokenizer/glm_moe_dsa/__init__.py`: 1 inline comment(s)

## High-Signal Discussion

- `2026-03-06T20:02:12Z` `issue` by `coderabbitai`; signals: attention, b200, cache, cuda, fp4, fp8, hang, kv cache; excerpt: "📝 Walkthrough Walkthrough This PR introduces GLM-Moe-Dsa model architecture support across TensorRT-LLM, including model aliasing, configuration routing, MLA rotary cache optimization, attention metadata management ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/11990#issuecomment-4013849440)
- `2026-03-06T20:02:18Z` `review` `COMMENTED` by `coderabbitai`; signals: attention, hang, mla, moe, perf, tensorrt; excerpt: "Actionable comments posted: 8 [!CAUTION] Some comments are outside the diff and can’t be posted inline due to platform limitations. ⚠️ Outside diff range ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/11990#pullrequestreview-3905746776)
- `2026-03-09T04:46:07Z` `inline` by `yuxianq` `tensorrt_llm/_torch/attention_backend/trtllm.py`:146; signals: attention, cache, layout, mla, tensorrt; excerpt: "It seems that we can implement duplicate data=True for create sinusoidal positions long rope/create sinusoidal positions for attention plugin in create rope const params ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/11990#discussion_r2903164554)
- `2026-03-10T17:00:46Z` `inline` by `NVShreyas` `examples/models/core/glm-5/README.md`:143; signals: deepgemm, fp4, fp8, gemm, nvfp4; excerpt: "There are 3 configs - FP8, FP8 + MTP, NVFP4. The first 2 use DEEPGEMM. Let me make this more clear in the doc" (https://github.com/NVIDIA/TensorRT-LLM/pull/11990#discussion_r2913174973)
- `2026-03-06T20:02:15Z` `inline` by `coderabbitai` `tensorrt_llm/_torch/model_config.py`:367; signals: fp8, hang, moe, tensorrt; excerpt: "⚠️ Potential issue 🟠 Major Keep the FP8 kv b proj exclusion consistent across both quant-config loaders. This change makes the HF quantization config ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/11990#discussion_r2897614407)
- `2026-03-06T20:02:15Z` `inline` by `coderabbitai` `tensorrt_llm/_torch/speculative/interface.py`:100; signals: attention, cache, cute, tensorrt; excerpt: "⚠️ Potential issue 🟠 Major 🧩 Analysis chain 🏁 Script executed: Repository: NVIDIA/TensorRT-LLM Length of output: 98 --- 🏁 Script executed: Repository: NVIDIA/TensorRT-LLM Length ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/11990#discussion_r2897614414)
- `2026-03-06T20:02:16Z` `inline` by `coderabbitai` `tensorrt_llm/tokenizer/glm_moe_dsa/tokenizer.py`:47; signals: cute, moe, register, tensorrt; excerpt: "⚠️ Potential issue 🟠 Major 🧩 Analysis chain 🏁 Script executed: Repository: NVIDIA/TensorRT-LLM Length of output: 45 --- 🏁 Script executed: Repository: NVIDIA/TensorRT-LLM Length ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/11990#discussion_r2897614426)
- `2026-03-06T20:02:15Z` `inline` by `coderabbitai` `tensorrt_llm/tokenizer/glm_moe_dsa/__init__.py`:5; signals: block, moe, tensorrt; excerpt: "⚠️ Potential issue 🟠 Major Add the standard NVIDIA Apache header to this new module. New source files in this repo need the copyright/license ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/11990#discussion_r2897614421)
- `2026-03-06T20:02:16Z` `inline` by `coderabbitai` `tensorrt_llm/tokenizer/glm_moe_dsa/tokenizer.py`:15; signals: block, moe, tensorrt; excerpt: "⚠️ Potential issue 🟠 Major Add the standard NVIDIA Apache header to this new module. This new Python source file is missing the required ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/11990#discussion_r2897614424)
- `2026-03-06T20:02:16Z` `inline` by `coderabbitai` `tensorrt_llm/tokenizer/glm_moe_dsa/tokenizer.py`:87; signals: cute, moe, tensorrt; excerpt: "⚠️ Potential issue 🟠 Major 🧩 Analysis chain 🏁 Script executed: Repository: NVIDIA/TensorRT-LLM Length of output: 3800 --- 🏁 Script executed: Repository: NVIDIA/TensorRT-LLM Length ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/11990#discussion_r2897614432)
- `2026-03-09T04:16:32Z` `inline` by `yuxianq` `tensorrt_llm/tokenizer/glm_moe_dsa/tokenizer.py`:17; signals: hang, moe, tensorrt; excerpt: "It seems that we don't change the handling of extra special tokens no matter it is list or dict, is this comment correct?" (https://github.com/NVIDIA/TensorRT-LLM/pull/11990#discussion_r2903106031)
- `2026-03-09T04:31:25Z` `inline` by `yuxianq` `tensorrt_llm/_torch/speculative/interface.py`:93; signals: block, cache, tensorrt; excerpt: "We create tensors and copy them in a loop, which is very slow. Can we use KVCacheManager's get block ids per seq instead to ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/11990#discussion_r2903134344)
