# PR Discussion Digest

- Source PR: [NVIDIA/TensorRT-LLM#14074](https://github.com/NVIDIA/TensorRT-LLM/pull/14074)
- Source page: `sources/prs/tensorrt-llm/PR-14074.md`
- Evidence bundle: `evidence/pull-bundles/tensorrt-llm/gh-14074`
- Generated at: `2026-05-20T15:19:02.333983+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-05-13T06:44:04Z`
- Merged: `2026-05-15T02:14:56Z`

## Discussion Counts

- Issue comments: 18
- Review submissions: 3 (approved=1, commented=2)
- Inline review comments: 2
- Review threads observed: 1
- Resolved/outdated thread markers: resolved=1, outdated=1
- Human participants with discussion text: qiaoxj07, tensorrt-cicd, xxi-nv
- Automation comments/reviews omitted from high-signal summary: 0
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-05-13T06:56:07Z` `APPROVED` by `xxi-nv` (https://github.com/NVIDIA/TensorRT-LLM/pull/14074#pullrequestreview-4279084521)
- `2026-05-13T23:30:21Z` `COMMENTED` by `xxi-nv` (https://github.com/NVIDIA/TensorRT-LLM/pull/14074#pullrequestreview-4286035205)
- `2026-05-14T00:48:59Z` `COMMENTED` by `qiaoxj07` (https://github.com/NVIDIA/TensorRT-LLM/pull/14074#pullrequestreview-4286369204)

## Inline Comment Hotspots

- `tensorrt_llm/_torch/modules/fused_moe/routing.py`: 2 inline comment(s)

## High-Signal Discussion

- `2026-05-14T00:48:59Z` `inline` by `qiaoxj07` `tensorrt_llm/_torch/modules/fused_moe/routing.py`:1197; signals: layout, moe, tensorrt; excerpt: "Addressed in b80ff77: pushed the layout abstraction into the routing-method classes themselves. DeepSeekV3MoeRoutingMethod now exposes n group / topk group via @property (delegating to ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/14074#discussion_r3238308836)
- `2026-05-13T23:30:21Z` `inline` by `xxi-nv` `tensorrt_llm/_torch/modules/fused_moe/routing.py`:1197; signals: moe, tensorrt; excerpt: "It is suggested to only return one value which represents the topk group, so the user doesn't have to recognize it whether V3 or ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/14074#discussion_r3238030409)
- `2026-05-13T10:30:48Z` `issue` by `tensorrt-cicd`; signals: pipeline; excerpt: "[PR Github 48126]( [ run ] completed with state SUCCESS. Commit: e54555b [/LLM/main/L0 MergeRequest PR pipeline 37952]( completed with status: 'FAILURE' [CI Report]( ⚠️ ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/14074#issuecomment-4439949786)
- `2026-05-14T15:00:47Z` `issue` by `tensorrt-cicd`; signals: pipeline; excerpt: "[PR Github 48345]( [ run ] completed with state SUCCESS. Commit: 459224a [/LLM/main/L0 MergeRequest PR pipeline 38152]( completed with status: 'FAILURE' [CI Report]( ⚠️ ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/14074#issuecomment-4451875040)
- `2026-05-14T16:16:43Z` `issue` by `tensorrt-cicd`; signals: pipeline; excerpt: "[PR Github 48395]( [ run ] completed with state FAILURE. Commit: 459224a [/LLM/main/L0 MergeRequest PR pipeline 38198]( completed with status: 'FAILURE' [CI Report]( ⚠️ ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/14074#issuecomment-4452483315)
- `2026-05-14T19:23:20Z` `issue` by `tensorrt-cicd`; signals: pipeline; excerpt: "[PR Github 48418]( [ run ] completed with state SUCCESS. Commit: 459224a [/LLM/main/L0 MergeRequest PR pipeline 38219]( completed with status: 'SUCCESS' [CI Report]( [Link ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/14074#issuecomment-4454016290)
