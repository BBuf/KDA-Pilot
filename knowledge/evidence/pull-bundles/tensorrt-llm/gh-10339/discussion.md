# PR Discussion Digest

- Source PR: [NVIDIA/TensorRT-LLM#10339](https://github.com/NVIDIA/TensorRT-LLM/pull/10339)
- Source page: `sources/prs/tensorrt-llm/PR-10339.md`
- Evidence bundle: `evidence/pull-bundles/tensorrt-llm/gh-10339`
- Generated at: `2026-05-20T15:17:37.023455+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-12-30T09:24:01Z`
- Merged: `2026-01-08T02:21:02Z`

## Discussion Counts

- Issue comments: 23
- Review submissions: 11 (approved=4, commented=7)
- Inline review comments: 6
- Review threads observed: 2
- Resolved/outdated thread markers: resolved=2, outdated=2
- Human participants with discussion text: coderabbitai, hyukn, limin2021, longlee0622, questa-wang, tensorrt-cicd, xxi-nv, yizhang-nv
- Automation comments/reviews omitted from high-signal summary: 0
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-12-30T09:26:55Z` `COMMENTED` by `coderabbitai` - Actionable comments posted: 0 🧹 Nitpick comments (1) tensorrt llm/ torch/modules/linear.py (1) 2108-2111: Consider creating a defensive copy ... (https://github.com/NVIDIA/TensorRT-LLM/pull/10339#pullrequestreview-3617689313)
- `2026-01-04T01:11:24Z` `APPROVED` by `limin2021` (https://github.com/NVIDIA/TensorRT-LLM/pull/10339#pullrequestreview-3624619535)
- `2026-01-05T00:57:48Z` `COMMENTED` by `longlee0622` (https://github.com/NVIDIA/TensorRT-LLM/pull/10339#pullrequestreview-3625269859)
- `2026-01-05T00:58:07Z` `COMMENTED` by `longlee0622` (https://github.com/NVIDIA/TensorRT-LLM/pull/10339#pullrequestreview-3625270044)
- `2026-01-05T05:49:34Z` `COMMENTED` by `hyukn` (https://github.com/NVIDIA/TensorRT-LLM/pull/10339#pullrequestreview-3625561100)
- `2026-01-05T05:52:59Z` `COMMENTED` by `hyukn` (https://github.com/NVIDIA/TensorRT-LLM/pull/10339#pullrequestreview-3625566306)
- `2026-01-05T07:01:32Z` `COMMENTED` by `questa-wang` (https://github.com/NVIDIA/TensorRT-LLM/pull/10339#pullrequestreview-3625692432)
- `2026-01-06T06:46:51Z` `APPROVED` by `longlee0622` (https://github.com/NVIDIA/TensorRT-LLM/pull/10339#pullrequestreview-3629649211)
- `2026-01-06T06:47:08Z` `COMMENTED` by `longlee0622` (https://github.com/NVIDIA/TensorRT-LLM/pull/10339#pullrequestreview-3629649817)
- `2026-01-08T01:13:45Z` `APPROVED` by `xxi-nv` (https://github.com/NVIDIA/TensorRT-LLM/pull/10339#pullrequestreview-3637347523)
- `2026-01-08T02:13:38Z` `APPROVED` by `yizhang-nv` (https://github.com/NVIDIA/TensorRT-LLM/pull/10339#pullrequestreview-3637428386)

## Inline Comment Hotspots

- `tensorrt_llm/_torch/custom_ops/cute_dsl_custom_ops.py`: 4 inline comment(s)
- `tensorrt_llm/_torch/modules/linear.py`: 2 inline comment(s)

## High-Signal Discussion

- `2025-12-30T09:26:55Z` `review` `COMMENTED` by `coderabbitai`; signals: block, cute, fp4, hang, nvfp4, perf, performance, tensorrt; excerpt: "Actionable comments posted: 0 🧹 Nitpick comments (1) tensorrt llm/ torch/modules/linear.py (1) 2108-2111: Consider creating a defensive copy to avoid mutating shared lists. The ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/10339#pullrequestreview-3617689313)
- `2025-12-30T09:26:52Z` `issue` by `coderabbitai`; signals: cute, fp4, gemm, hang, kernel, nvfp4, tensorrt; excerpt: "📝 Walkthrough Walkthrough These changes optimize kernel tactic exploration and backend selection logic. The first modifies prefetch option experimentation to target larger K values. ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/10339#issuecomment-3698787878)
- `2026-01-05T07:01:32Z` `inline` by `questa-wang` `tensorrt_llm/_torch/custom_ops/cute_dsl_custom_ops.py`:459; signals: cute, kernel, latency, perf, tensorrt, tma; excerpt: "Yes, TMA prefetch would only bring benefit for cases really bound at DRAM latency. If mainloop is not that large, we can't see perf ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/10339#discussion_r2660479388)
- `2026-01-05T05:49:34Z` `inline` by `hyukn` `tensorrt_llm/_torch/custom_ops/cute_dsl_custom_ops.py`:459; signals: cute, perf, tensorrt; excerpt: "This is based on some perf data collected by offline prefetch tuning. It illustrates that prefetch dose not bring noticable perf gain for some ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/10339#discussion_r2660356349)
- `2026-01-05T00:57:49Z` `inline` by `longlee0622` `tensorrt_llm/_torch/modules/linear.py`:2110; signals: cute, tensorrt; excerpt: "Why adding one more backend helps to "further reduce tuning time"? BTW, this will introduce cutedsl even if it is not allowed in the ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/10339#discussion_r2660059940)
- `2026-01-05T00:58:07Z` `inline` by `longlee0622` `tensorrt_llm/_torch/custom_ops/cute_dsl_custom_ops.py`:459; signals: cute, tensorrt; excerpt: "How is 16384 chosen?" (https://github.com/NVIDIA/TensorRT-LLM/pull/10339#discussion_r2660060161)
- `2026-01-05T05:52:59Z` `inline` by `hyukn` `tensorrt_llm/_torch/modules/linear.py`:2110; signals: tensorrt; excerpt: "Correct. I shall remove this logic. Currently we should still rely on the user's specification." (https://github.com/NVIDIA/TensorRT-LLM/pull/10339#discussion_r2660361513)
- `2025-12-30T10:56:55Z` `issue` by `tensorrt-cicd`; signals: pipeline; excerpt: "[PR Github 30162]( [ run ] completed with state SUCCESS. Commit: e9fb82a [/LLM/main/L0 MergeRequest PR pipeline 23210]( completed with status: 'FAILURE' ⚠️ Action Required: ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/10339#issuecomment-3699010161)
- `2025-12-31T04:54:10Z` `issue` by `tensorrt-cicd`; signals: pipeline; excerpt: "[PR Github 30211]( [ run ] completed with state SUCCESS. Commit: a256ba9 [/LLM/main/L0 MergeRequest PR pipeline 23255]( completed with status: 'FAILURE' ⚠️ Action Required: ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/10339#issuecomment-3701444180)
- `2025-12-31T08:06:08Z` `issue` by `tensorrt-cicd`; signals: pipeline; excerpt: "[PR Github 30245]( [ run ] completed with state SUCCESS. Commit: a256ba9 [/LLM/main/L0 MergeRequest PR pipeline 23286]( completed with status: 'FAILURE' ⚠️ Action Required: ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/10339#issuecomment-3701689888)
- `2025-12-31T09:00:06Z` `issue` by `tensorrt-cicd`; signals: pipeline; excerpt: "[PR Github 30261]( [ run ] completed with state SUCCESS. Commit: a256ba9 [/LLM/main/L0 MergeRequest PR pipeline 23297]( completed with status: 'FAILURE' ⚠️ Action Required: ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/10339#issuecomment-3701779819)
- `2026-01-03T04:57:49Z` `issue` by `tensorrt-cicd`; signals: pipeline; excerpt: "[PR Github 30423]( [ run ] completed with state SUCCESS. Commit: 3895a4a [/LLM/main/L0 MergeRequest PR pipeline 23451]( completed with status: 'FAILURE' ⚠️ Action Required: ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/10339#issuecomment-3706701135)
