# PR Discussion Digest

- Source PR: [NVIDIA/TensorRT-LLM#14004](https://github.com/NVIDIA/TensorRT-LLM/pull/14004)
- Source page: `sources/prs/tensorrt-llm/PR-14004.md`
- Evidence bundle: `evidence/pull-bundles/tensorrt-llm/gh-14004`
- Generated at: `2026-05-20T15:19:00.113618+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-05-11T18:11:01Z`
- Merged: `2026-05-14T17:19:27Z`

## Discussion Counts

- Issue comments: 13
- Review submissions: 10 (approved=3, commented=7)
- Inline review comments: 10
- Review threads observed: 7
- Resolved/outdated thread markers: resolved=7, outdated=4
- Human participants with discussion text: StanleySun639, arysef, coderabbitai, nvchenghaoz, suyoggupta, taylor-yb-lee, tensorrt-cicd
- Automation comments/reviews omitted from high-signal summary: 0
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-05-11T18:13:08Z` `COMMENTED` by `nvchenghaoz` (https://github.com/NVIDIA/TensorRT-LLM/pull/14004#pullrequestreview-4266206877)
- `2026-05-11T18:18:25Z` `COMMENTED` by `coderabbitai` - Actionable comments posted: 3 [!CAUTION] Some comments are outside the diff and can’t be posted inline due to ... (https://github.com/NVIDIA/TensorRT-LLM/pull/14004#pullrequestreview-4266239122)
- `2026-05-11T18:27:11Z` `COMMENTED` by `nvchenghaoz` (https://github.com/NVIDIA/TensorRT-LLM/pull/14004#pullrequestreview-4266262836)
- `2026-05-11T18:44:09Z` `COMMENTED` by `taylor-yb-lee` (https://github.com/NVIDIA/TensorRT-LLM/pull/14004#pullrequestreview-4266427600)
- `2026-05-11T18:46:44Z` `COMMENTED` by `taylor-yb-lee` (https://github.com/NVIDIA/TensorRT-LLM/pull/14004#pullrequestreview-4266449454)
- `2026-05-11T18:49:47Z` `APPROVED` by `taylor-yb-lee` (https://github.com/NVIDIA/TensorRT-LLM/pull/14004#pullrequestreview-4266474893)
- `2026-05-11T18:51:18Z` `COMMENTED` by `taylor-yb-lee` (https://github.com/NVIDIA/TensorRT-LLM/pull/14004#pullrequestreview-4266488231)
- `2026-05-11T18:51:54Z` `COMMENTED` by `taylor-yb-lee` (https://github.com/NVIDIA/TensorRT-LLM/pull/14004#pullrequestreview-4266493263)
- `2026-05-12T08:35:02Z` `APPROVED` by `StanleySun639` (https://github.com/NVIDIA/TensorRT-LLM/pull/14004#pullrequestreview-4270574348)
- `2026-05-14T17:16:58Z` `APPROVED` by `arysef` (https://github.com/NVIDIA/TensorRT-LLM/pull/14004#pullrequestreview-4291943998)

## Inline Comment Hotspots

- `tests/integration/defs/accuracy/references/gsm8k.yaml`: 3 inline comment(s)
- `tensorrt_llm/_torch/auto_deploy/custom_ops/fused_moe/mxfp4_moe.py`: 3 inline comment(s)
- `examples/auto_deploy/model_registry/models.yaml`: 2 inline comment(s)
- `tensorrt_llm/_torch/auto_deploy/models/custom/modeling_gpt_oss.py`: 1 inline comment(s)
- `tensorrt_llm/_torch/auto_deploy/transform/library/mxfp4_moe.py`: 1 inline comment(s)

## High-Signal Discussion

- `2026-05-11T18:18:25Z` `review` `COMMENTED` by `coderabbitai`; signals: accuracy, attention, fp4, hang, layout, moe, mxfp4, tensorrt; excerpt: "Actionable comments posted: 3 [!CAUTION] Some comments are outside the diff and can’t be posted inline due to platform limitations. ⚠️ Outside diff range ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/14004#pullrequestreview-4266239122)
- `2026-05-11T18:18:21Z` `issue` by `coderabbitai`; signals: accuracy, attention, benchmark, bf16, blackwell, cache, cuda, cute; excerpt: "📝 Walkthrough Walkthrough This PR adds end-to-end OpenAI GPT-OSS (20B/120B) model support to TensorRT-LLM AutoDeploy with native attention sinks and model-specific configs, alongside MXFP4 ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/14004#issuecomment-4423532290)
- `2026-05-11T18:51:18Z` `inline` by `taylor-yb-lee` `tensorrt_llm/_torch/auto_deploy/custom_ops/fused_moe/mxfp4_moe.py`:187; signals: fp4, memory, moe, mxfp4, oom, tensorrt; excerpt: "Ohh yes sorry I confused because when it was first crashed with OOM without your branch, I also tried to opt out this locally ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/14004#discussion_r3221363537)
- `2026-05-11T18:18:24Z` `inline` by `coderabbitai` `tensorrt_llm/_torch/auto_deploy/transform/library/mxfp4_moe.py`:201; signals: fp4, moe, mxfp4, register, tensorrt; excerpt: "⚠️ Potential issue 🟠 Major ⚡ Quick win Delay deleting the old expert params until every FX user is gone. register mxfp4 expert params() ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/14004#discussion_r3221159080)
- `2026-05-11T18:18:24Z` `inline` by `coderabbitai` `tensorrt_llm/_torch/auto_deploy/models/custom/modeling_gpt_oss.py`:453; signals: attention, cache, register, tensorrt; excerpt: "⚠️ Potential issue 🟠 Major ⚡ Quick win Fail fast on unsupported HF-style kwargs instead of silently dropping them. Both forward() methods accept kwargs, ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/14004#discussion_r3221159077)
- `2026-05-11T18:21:55Z` `inline` by `nvchenghaoz` `tensorrt_llm/_torch/auto_deploy/custom_ops/fused_moe/mxfp4_moe.py`:56; signals: fp4, moe, mxfp4, tensorrt; excerpt: "Move this the function." (https://github.com/NVIDIA/TensorRT-LLM/pull/14004#discussion_r3221178648)
- `2026-05-11T18:25:36Z` `inline` by `nvchenghaoz` `tensorrt_llm/_torch/auto_deploy/custom_ops/fused_moe/mxfp4_moe.py`:187; signals: fp4, moe, mxfp4, tensorrt; excerpt: "@taylor-yb-lee this is an optimization I did.. FYI" (https://github.com/NVIDIA/TensorRT-LLM/pull/14004#discussion_r3221199921)
- `2026-05-11T18:18:24Z` `inline` by `coderabbitai` `tests/integration/defs/accuracy/references/gsm8k.yaml`:314; signals: accuracy, regression; excerpt: "⚠️ Potential issue 🟠 Major ⚡ Quick win Replace the placeholder 120B GSM8K baseline before merging. accuracy: 10.0 is so low that this new ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/14004#discussion_r3221159086)
- `2026-05-11T18:12:46Z` `inline` by `nvchenghaoz` `tests/integration/defs/accuracy/references/gsm8k.yaml`:314; signals: accuracy; excerpt: "@taylor-yb-lee I did not touch the number and did not add the accuracy tests to CI since it might need a super long time ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/14004#discussion_r3221129641)
- `2026-05-11T18:44:09Z` `inline` by `taylor-yb-lee` `examples/auto_deploy/model_registry/models.yaml`:296; signals: oom; excerpt: "I think we should enable this with full model once we resolved the OOM issue (which will be part of" (https://github.com/NVIDIA/TensorRT-LLM/pull/14004#discussion_r3221316995)
- `2026-05-11T18:51:54Z` `inline` by `taylor-yb-lee` `tests/integration/defs/accuracy/references/gsm8k.yaml`:314; signals: accuracy; excerpt: "I will!" (https://github.com/NVIDIA/TensorRT-LLM/pull/14004#discussion_r3221367854)
- `2026-05-13T23:31:47Z` `issue` by `tensorrt-cicd`; signals: pipeline; excerpt: "[PR Github 48238]( [ run ] completed with state SUCCESS. Commit: aab928d [/LLM/main/L0 MergeRequest PR pipeline 38054]( completed with status: 'FAILURE' [CI Report]( ⚠️ ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/14004#issuecomment-4446001219)
