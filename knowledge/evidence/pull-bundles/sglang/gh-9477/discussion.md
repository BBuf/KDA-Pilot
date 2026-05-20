# PR Discussion Digest

- Source PR: [sgl-project/sglang#9477](https://github.com/sgl-project/sglang/pull/9477)
- Source page: `sources/prs/sglang/PR-9477.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-9477`
- Generated at: `2026-05-20T15:31:35.106028+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-08-22T02:36:47Z`
- Merged: `2025-09-07T01:16:18Z`

## Discussion Counts

- Issue comments: 3
- Review submissions: 5 (approved=2, commented=3)
- Inline review comments: 3
- Review threads observed: 2
- Resolved/outdated thread markers: resolved=2, outdated=2
- Human participants with discussion text: Alcanderian, BBuf, yuan-luo
- Automation comments/reviews omitted from high-signal summary: 4
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-08-22T02:37:00Z` `COMMENTED` by `gemini-code-assist` - Summary of Changes Hello @yuan-luo, I'm Gemini Code Assist[^1]! I'm currently reviewing this pull request and will post ... (https://github.com/sgl-project/sglang/pull/9477#pullrequestreview-3142914844)
- `2025-08-22T02:38:29Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request introduces a significant optimization to the moe sum reduce kernel Triton kernel. The ... (https://github.com/sgl-project/sglang/pull/9477#pullrequestreview-3142916381)
- `2025-08-22T05:31:06Z` `COMMENTED` by `yuan-luo` (https://github.com/sgl-project/sglang/pull/9477#pullrequestreview-3143141080)
- `2025-08-22T15:07:31Z` `APPROVED` by `BBuf` - LGTM! I'm curious about how much performance improvement this autotune actually contributes. We generally haven't used autotune in ... (https://github.com/sgl-project/sglang/pull/9477#pullrequestreview-3144865289)
- `2025-08-25T04:56:34Z` `APPROVED` by `Alcanderian` (https://github.com/sgl-project/sglang/pull/9477#pullrequestreview-3149905855)

## Inline Comment Hotspots

- `benchmark/kernels/fused_moe_triton/benchmark_sum_scale.py`: 2 inline comment(s)
- `python/sglang/srt/layers/moe/fused_moe_triton/fused_moe.py`: 1 inline comment(s)

## High-Signal Discussion

- `2025-08-22T05:31:05Z` `inline` by `yuan-luo` `benchmark/kernels/fused_moe_triton/benchmark_sum_scale.py`:47; signals: benchmark, kernel, moe, triton; excerpt: "Fixed." (https://github.com/sgl-project/sglang/pull/9477#discussion_r2292737696)
- `2025-08-22T15:07:31Z` `review` `APPROVED` by `BBuf`; signals: autotune, perf, performance; excerpt: "LGTM! I'm curious about how much performance improvement this autotune actually contributes. We generally haven't used autotune in SGLang before, and the autotuning process ..." (https://github.com/sgl-project/sglang/pull/9477#pullrequestreview-3144865289)
