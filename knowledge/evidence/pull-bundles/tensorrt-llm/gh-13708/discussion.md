# PR Discussion Digest

- Source PR: [NVIDIA/TensorRT-LLM#13708](https://github.com/NVIDIA/TensorRT-LLM/pull/13708)
- Source page: `sources/prs/tensorrt-llm/PR-13708.md`
- Evidence bundle: `evidence/pull-bundles/tensorrt-llm/gh-13708`
- Generated at: `2026-05-20T15:18:51.754245+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-05-02T22:08:11Z`
- Merged: `2026-05-06T01:27:50Z`

## Discussion Counts

- Issue comments: 25
- Review submissions: 2 (approved=1, commented=1)
- Inline review comments: 2
- Review threads observed: 2
- Resolved/outdated thread markers: resolved=2, outdated=0
- Human participants with discussion text: HuiGao-NV, coderabbitai, dongfengy, tensorrt-cicd
- Automation comments/reviews omitted from high-signal summary: 0
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-05-02T22:15:03Z` `COMMENTED` by `coderabbitai` - Actionable comments posted: 2 🧹 Nitpick comments (1) tensorrt llm/ torch/modules/fused moe/fused moe triton.py (1) 1124-1126: ⚡ Quick ... (https://github.com/NVIDIA/TensorRT-LLM/pull/13708#pullrequestreview-4215592016)
- `2026-05-06T00:40:18Z` `APPROVED` by `HuiGao-NV` - LGTM (https://github.com/NVIDIA/TensorRT-LLM/pull/13708#pullrequestreview-4232457755)

## Inline Comment Hotspots

- `tensorrt_llm/_torch/modules/fused_moe/fused_moe_triton.py`: 2 inline comment(s)

## High-Signal Discussion

- `2026-05-02T22:14:59Z` `issue` by `coderabbitai`; signals: cache, cuda, failing, fp4, hang, memory, moe, mxfp4; excerpt: "📝 Walkthrough Walkthrough This PR introduces a reusable static helper method swizzle and replace for MXFP4 weight deposition that performs in-place swizzling, parameter extraction, ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13708#issuecomment-4364836014)
- `2026-05-02T22:15:03Z` `review` `COMMENTED` by `coderabbitai`; signals: aligned, hang, moe, nan, tensorrt, triton; excerpt: "Actionable comments posted: 2 🧹 Nitpick comments (1) tensorrt llm/ torch/modules/fused moe/fused moe triton.py (1) 1124-1126: ⚡ Quick win Add type annotations to the ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13708#pullrequestreview-4215592016)
- `2026-05-02T22:15:02Z` `inline` by `coderabbitai` `tensorrt_llm/_torch/modules/fused_moe/fused_moe_triton.py`:1134; signals: cute, moe, tensorrt, triton; excerpt: "⚠️ Potential issue 🟠 Major 🧩 Analysis chain 🏁 Script executed: Repository: NVIDIA/TensorRT-LLM Length of output: 126 --- 🏁 Script executed: Repository: NVIDIA/TensorRT-LLM Length ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13708#discussion_r3177298452)
- `2026-05-02T22:15:02Z` `inline` by `coderabbitai` `tensorrt_llm/_torch/modules/fused_moe/fused_moe_triton.py`:1208; signals: moe, tensorrt, triton; excerpt: "⚠️ Potential issue 🟠 Major ⚡ Quick win Refresh module.quant scales after the new replacements/cleanup. setup quant scales() captured the original objects during create ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13708#discussion_r3177298456)
- `2026-05-03T02:18:11Z` `issue` by `tensorrt-cicd`; signals: pipeline; excerpt: "[PR Github 46571]( [ run ] completed with state SUCCESS. Commit: e9c1d7a [/LLM/main/L0 MergeRequest PR pipeline 36622]( completed with status: 'FAILURE' [CI Report]( ⚠️ ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13708#issuecomment-4365200033)
- `2026-05-03T06:33:54Z` `issue` by `tensorrt-cicd`; signals: pipeline; excerpt: "[PR Github 46579]( [ run ] completed with state SUCCESS. Commit: 1766894 [/LLM/main/L0 MergeRequest PR pipeline 36629]( completed with status: 'FAILURE' [CI Report]( ⚠️ ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13708#issuecomment-4365566317)
- `2026-05-03T21:32:14Z` `issue` by `tensorrt-cicd`; signals: pipeline; excerpt: "[PR Github 46606]( [ run ] completed with state SUCCESS. Commit: 322ed86 [/LLM/main/L0 MergeRequest PR pipeline 36653]( completed with status: 'FAILURE' [CI Report]( ⚠️ ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13708#issuecomment-4367222715)
- `2026-05-04T05:18:18Z` `issue` by `tensorrt-cicd`; signals: pipeline; excerpt: "[PR Github 46612]( [ run ] completed with state SUCCESS. Commit: 322ed86 [/LLM/main/L0 MergeRequest PR pipeline 36659]( completed with status: 'FAILURE' [CI Report]( ⚠️ ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13708#issuecomment-4368451912)
- `2026-05-04T17:28:57Z` `issue` by `tensorrt-cicd`; signals: pipeline; excerpt: "[PR Github 46653]( [ run ] completed with state SUCCESS. Commit: c51ee54 [/LLM/main/L0 MergeRequest PR pipeline 36695]( completed with status: 'FAILURE' [CI Report]( ⚠️ ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13708#issuecomment-4373071132)
- `2026-05-05T05:55:48Z` `issue` by `tensorrt-cicd`; signals: pipeline; excerpt: "[PR Github 46694]( [ run ] completed with state SUCCESS. Commit: c51ee54 [/LLM/main/L0 MergeRequest PR pipeline 36732]( completed with status: 'SUCCESS' [CI Report]( [Link ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13708#issuecomment-4376845306)
- `2026-05-05T21:20:34Z` `issue` by `tensorrt-cicd`; signals: pipeline; excerpt: "[PR Github 46829]( [ run ] completed with state SUCCESS. Commit: 1efd5b7 [/LLM/main/L0 MergeRequest PR pipeline 36850]( completed with status: 'FAILURE' [CI Report]( ⚠️ ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13708#issuecomment-4383156944)
- `2026-05-06T01:05:13Z` `issue` by `dongfengy`; signals: failing, hang; excerpt: "/bot skip --comment "Passed 19 hours ago. No change since then except rebase. CI failing with unrelated tests."" (https://github.com/NVIDIA/TensorRT-LLM/pull/13708#issuecomment-4384359530)
