# PR Discussion Digest

- Source PR: [NVIDIA/TensorRT-LLM#11769](https://github.com/NVIDIA/TensorRT-LLM/pull/11769)
- Source page: `sources/prs/tensorrt-llm/PR-11769.md`
- Evidence bundle: `evidence/pull-bundles/tensorrt-llm/gh-11769`
- Generated at: `2026-05-20T15:17:51.120362+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-02-27T02:45:03Z`
- Merged: `2026-03-02T07:11:40Z`

## Discussion Counts

- Issue comments: 7
- Review submissions: 2 (approved=1, commented=1)
- Inline review comments: 1
- Review threads observed: 1
- Resolved/outdated thread markers: resolved=1, outdated=0
- Human participants with discussion text: coderabbitai, leslie-fang25, tensorrt-cicd, xxi-nv
- Automation comments/reviews omitted from high-signal summary: 0
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-02-27T02:48:58Z` `COMMENTED` by `coderabbitai` - Actionable comments posted: 1 🤖 Prompt for all review comments with AI agents --- ℹ️ Review info Configuration ... (https://github.com/NVIDIA/TensorRT-LLM/pull/11769#pullrequestreview-3864559083)
- `2026-03-02T06:06:49Z` `APPROVED` by `xxi-nv` (https://github.com/NVIDIA/TensorRT-LLM/pull/11769#pullrequestreview-3874226023)

## Inline Comment Hotspots

- `tensorrt_llm/_torch/modules/fused_moe/fused_moe_cute_dsl.py`: 1 inline comment(s)

## High-Signal Discussion

- `2026-02-27T02:48:54Z` `issue` by `coderabbitai`; signals: block, cute, fp8, hang, latency, moe, tensorrt; excerpt: "📝 Walkthrough Walkthrough In the run moe fp8 block scales function, the determination of top k now conditionally uses the shape of token selected ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/11769#issuecomment-3970415156)
- `2026-02-27T02:48:58Z` `review` `COMMENTED` by `coderabbitai`; signals: cute, hang, moe, tensorrt; excerpt: "Actionable comments posted: 1 🤖 Prompt for all review comments with AI agents --- ℹ️ Review info Configuration used : Path: .coderabbit.yaml Review profile ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/11769#pullrequestreview-3864559083)
- `2026-02-27T02:48:57Z` `inline` by `coderabbitai` `tensorrt_llm/_torch/modules/fused_moe/fused_moe_cute_dsl.py`:688; signals: cute, moe, tensorrt; excerpt: "⚠️ Potential issue 🟡 Minor 🧩 Analysis chain 🏁 Script executed: Repository: NVIDIA/TensorRT-LLM Length of output: 131 --- 🏁 Script executed: Repository: NVIDIA/TensorRT-LLM Length ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/11769#discussion_r2862227288)
- `2026-02-27T10:04:42Z` `issue` by `tensorrt-cicd`; signals: pipeline; excerpt: "[PR Github 37004]( [ run ] completed with state SUCCESS. Commit: 924ec1f [/LLM/main/L0 MergeRequest PR pipeline 28652]( completed with status: 'FAILURE' ⚠️ Action Required: ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/11769#issuecomment-3971961043)
- `2026-02-27T16:06:17Z` `issue` by `tensorrt-cicd`; signals: pipeline; excerpt: "[PR Github 37062]( [ run ] completed with state SUCCESS. Commit: 924ec1f [/LLM/main/L0 MergeRequest PR pipeline 28695]( completed with status: 'SUCCESS' [Link to invocation](" (https://github.com/NVIDIA/TensorRT-LLM/pull/11769#issuecomment-3973751727)
