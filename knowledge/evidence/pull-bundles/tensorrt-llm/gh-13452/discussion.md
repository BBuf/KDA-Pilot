# PR Discussion Digest

- Source PR: [NVIDIA/TensorRT-LLM#13452](https://github.com/NVIDIA/TensorRT-LLM/pull/13452)
- Source page: `sources/prs/tensorrt-llm/PR-13452.md`
- Evidence bundle: `evidence/pull-bundles/tensorrt-llm/gh-13452`
- Generated at: `2026-05-20T15:18:42.393503+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-04-24T21:43:36Z`
- Merged: `2026-05-01T01:18:12Z`

## Discussion Counts

- Issue comments: 16
- Review submissions: 4 (approved=3, commented=1)
- Inline review comments: 0
- Review threads observed: 0
- Resolved/outdated thread markers: resolved=0, outdated=0
- Human participants with discussion text: coderabbitai, dc3671, longlee0622, peihu-nv, pengbowang-nv, tensorrt-cicd
- Automation comments/reviews omitted from high-signal summary: 0
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-04-24T21:51:17Z` `COMMENTED` by `coderabbitai` - 🧹 Nitpick comments (1) tensorrt llm/ torch/attention backend/sparse/dsa.py (1) 1805-1848: Consider adding a verification mechanism for TF32 dispatch. ... (https://github.com/NVIDIA/TensorRT-LLM/pull/13452#pullrequestreview-4173615840)
- `2026-04-27T00:38:52Z` `APPROVED` by `longlee0622` (https://github.com/NVIDIA/TensorRT-LLM/pull/13452#pullrequestreview-4177703342)
- `2026-04-27T02:56:14Z` `APPROVED` by `dc3671` (https://github.com/NVIDIA/TensorRT-LLM/pull/13452#pullrequestreview-4177956222)
- `2026-04-27T03:12:48Z` `APPROVED` by `pengbowang-nv` (https://github.com/NVIDIA/TensorRT-LLM/pull/13452#pullrequestreview-4177989108)

## Inline Comment Hotspots

- No inline review comments were returned by GitHub.

## High-Signal Discussion

- `2026-04-24T21:51:17Z` `review` `COMMENTED` by `coderabbitai`; signals: attention, correctness, cuda, hang, perf, performance, regression, tensorrt; excerpt: "🧹 Nitpick comments (1) tensorrt llm/ torch/attention backend/sparse/dsa.py (1) 1805-1848: Consider adding a verification mechanism for TF32 dispatch. The PR description notes "Test coverage: ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13452#pullrequestreview-4173615840)
- `2026-04-24T21:51:14Z` `issue` by `coderabbitai`; signals: attention, gemm, hang, tensorrt; excerpt: "📝 Walkthrough Walkthrough Modified the indexer pre-projection computation in the sparse attention backend to use PyTorch's F.linear within a TF32-enabled context instead of the ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13452#issuecomment-4316629278)
- `2026-04-28T04:35:51Z` `issue` by `tensorrt-cicd`; signals: pipeline; excerpt: "[PR Github 45785]( [ run ] completed with state FAILURE. Commit: 1aa7a4b [/LLM/main/L0 MergeRequest PR pipeline 35975]( completed with status: 'FAILURE' [CI Report]( ⚠️ ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13452#issuecomment-4332379631)
- `2026-04-28T08:48:51Z` `issue` by `tensorrt-cicd`; signals: pipeline; excerpt: "[PR Github 45856]( [ run ] completed with state SUCCESS. Commit: 1aa7a4b [/LLM/main/L0 MergeRequest PR pipeline 36034]( completed with status: 'FAILURE' [CI Report]( ⚠️ ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13452#issuecomment-4333720903)
- `2026-04-29T00:28:31Z` `issue` by `tensorrt-cicd`; signals: pipeline; excerpt: "[PR Github 45965]( [ run ] completed with state SUCCESS. Commit: 1aa7a4b [/LLM/main/L0 MergeRequest PR pipeline 36118]( completed with status: 'FAILURE' [CI Report]( ⚠️ ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13452#issuecomment-4340048678)
- `2026-04-30T04:32:24Z` `issue` by `tensorrt-cicd`; signals: pipeline; excerpt: "[PR Github 46215]( [ run ] completed with state SUCCESS. Commit: 89f3354 [/LLM/main/L0 MergeRequest PR pipeline 36327]( completed with status: 'FAILURE' [CI Report]( ⚠️ ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13452#issuecomment-4349701638)
- `2026-04-30T19:12:59Z` `issue` by `tensorrt-cicd`; signals: pipeline; excerpt: "[PR Github 46406]( [ run ] completed with state SUCCESS. Commit: 89f3354 [/LLM/main/L0 MergeRequest PR pipeline 36482]( completed with status: 'SUCCESS' [CI Report]( [Link ..." (https://github.com/NVIDIA/TensorRT-LLM/pull/13452#issuecomment-4355472586)
