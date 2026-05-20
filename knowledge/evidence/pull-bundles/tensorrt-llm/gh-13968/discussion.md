# PR Discussion Digest

- Source PR: [NVIDIA/TensorRT-LLM#13968](https://github.com/NVIDIA/TensorRT-LLM/pull/13968)
- Source page: `sources/prs/tensorrt-llm/PR-13968.md`
- Evidence bundle: `evidence/pull-bundles/tensorrt-llm/gh-13968`
- Generated at: `2026-05-20T15:19:00.091519+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-05-11T05:39:46Z`
- Merged: `2026-05-18T06:13:17Z`

## Discussion Counts

- Issue comments: 29
- Review submissions: 3 (approved=2, commented=1)
- Inline review comments: 2
- Review threads observed: 2
- Resolved/outdated thread markers: resolved=2, outdated=0
- Human participants with discussion text: Wanli-Jiang, coderabbitai, lowsfer, syuoni, tensorrt-cicd
- Automation comments/reviews omitted from high-signal summary: 0
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-05-11T05:43:32Z` `COMMENTED` by `coderabbitai` - Actionable comments posted: 2 🧹 Nitpick comments (1) tests/unittest/llmapi/test llm pytorch.py (1) 620-620: LGTM — tightening max tokens ... (https://github.com/NVIDIA/TensorRT-LLM/pull/13968#pullrequestreview-4260977924)
- `2026-05-11T07:30:36Z` `APPROVED` by `syuoni` (https://github.com/NVIDIA/TensorRT-LLM/pull/13968#pullrequestreview-4261484249)
- `2026-05-13T04:51:58Z` `APPROVED` by `lowsfer` (https://github.com/NVIDIA/TensorRT-LLM/pull/13968#pullrequestreview-4278394266)

## Inline Comment Hotspots

- `tensorrt_llm/_torch/models/checkpoints/__init__.py`: 1 inline comment(s)
- `tensorrt_llm/_torch/models/checkpoints/hf/nemotron_nas_weight_mapper.py`: 1 inline comment(s)

## High-Signal Discussion

- `2026-05-11T05:43:28Z` `issue` by `coderabbitai`; signals: block, cache, fp4, hang, kv cache, nvfp4, tensorrt, tma; excerpt: "📝 Walkthrough Walkthrough This PR introduces a new Hugging Face weight mapper for the Nemotron NAS model (DeciLMForCausalLM) that handles per-layer KV-head configurations, exports ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13968#issuecomment-4417878612)
- `2026-05-11T05:43:32Z` `review` `COMMENTED` by `coderabbitai`; signals: cache, hang, tensorrt; excerpt: "Actionable comments posted: 2 🧹 Nitpick comments (1) tests/unittest/llmapi/test llm pytorch.py (1) 620-620: LGTM — tightening max tokens here is a reasonable stabilization for ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13968#pullrequestreview-4260977924)
- `2026-05-11T05:43:31Z` `inline` by `coderabbitai` `tensorrt_llm/_torch/models/checkpoints/__init__.py`:10; signals: tensorrt; excerpt: "⚠️ Potential issue 🟠 Major ⚡ Quick win Add/update the NVIDIA copyright header for this modified file. This file is modified in the PR ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13968#discussion_r3216570724)
- `2026-05-11T05:43:31Z` `inline` by `coderabbitai` `tensorrt_llm/_torch/models/checkpoints/hf/nemotron_nas_weight_mapper.py`:1; signals: tensorrt; excerpt: "⚠️ Potential issue 🟠 Major ⚡ Quick win Add the required NVIDIA copyright header to this new file. This new Python source file is ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13968#discussion_r3216570727)
- `2026-05-11T16:26:48Z` `issue` by `tensorrt-cicd`; signals: pipeline; excerpt: "[PR Github 47669]( [ run ] completed with state SUCCESS. Commit: 6b641f1 [/LLM/main/L0 MergeRequest PR pipeline 37569]( completed with status: 'FAILURE' [CI Report]( ⚠️ ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13968#issuecomment-4422634021)
- `2026-05-12T11:22:45Z` `issue` by `tensorrt-cicd`; signals: pipeline; excerpt: "[PR Github 47825]( [ run ] completed with state SUCCESS. Commit: 67e0a3a [/LLM/main/L0 MergeRequest PR pipeline 37710]( completed with status: 'FAILURE' [CI Report]( ⚠️ ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13968#issuecomment-4429998039)
- `2026-05-13T15:07:03Z` `issue` by `tensorrt-cicd`; signals: pipeline; excerpt: "[PR Github 48101]( [ run ] completed with state FAILURE. Commit: 1b44911 [/LLM/main/L0 MergeRequest PR pipeline 37931]( completed with status: 'FAILURE' [CI Report]( ⚠️ ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13968#issuecomment-4442425161)
- `2026-05-14T21:27:28Z` `issue` by `tensorrt-cicd`; signals: pipeline; excerpt: "[PR Github 48343]( [ run ] completed with state SUCCESS. Commit: be7b388 [/LLM/main/L0 MergeRequest PR pipeline 38151]( completed with status: 'FAILURE' [CI Report]( ⚠️ ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13968#issuecomment-4454877982)
- `2026-05-15T23:28:38Z` `issue` by `tensorrt-cicd`; signals: pipeline; excerpt: "[PR Github 48524]( [ run ] completed with state FAILURE. Commit: be7b388 [/LLM/main/L0 MergeRequest PR pipeline 38317]( completed with status: 'FAILURE' [CI Report]( ⚠️ ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13968#issuecomment-4464501084)
- `2026-05-16T10:46:46Z` `issue` by `tensorrt-cicd`; signals: pipeline; excerpt: "[PR Github 48668]( [ run ] completed with state SUCCESS. Commit: f00123d [/LLM/main/L0 MergeRequest PR pipeline 38449]( completed with status: 'FAILURE' [CI Report]( ⚠️ ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13968#issuecomment-4466619337)
- `2026-05-18T05:46:17Z` `issue` by `tensorrt-cicd`; signals: pipeline; excerpt: "[PR Github 48815]( [ run ] completed with state SUCCESS. Commit: f00123d [/LLM/main/L0 MergeRequest PR pipeline 38577]( completed with status: 'FAILURE' [CI Report]( ⚠️ ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13968#issuecomment-4474750552)
- `2026-05-18T06:13:13Z` `issue` by `tensorrt-cicd`; signals: general review; excerpt: "[PR Github 48842]( [ skip ] completed with state SUCCESS. Commit: f00123d Skipping testing for commit f00123d [Link to invocation](" (https://github.com/NVIDIA/TensorRT-LLM/pull/13968#issuecomment-4474870809)
