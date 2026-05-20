# PR Discussion Digest

- Source PR: [sgl-project/sglang#6627](https://github.com/sgl-project/sglang/pull/6627)
- Source page: `sources/prs/sglang/PR-6627.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-6627`
- Generated at: `2026-05-20T15:30:43.505110+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-05-26T12:52:17Z`
- Merged: `2025-05-28T07:15:23Z`

## Discussion Counts

- Issue comments: 7
- Review submissions: 4 (approved=2, commented=2)
- Inline review comments: 2
- Review threads observed: 1
- Resolved/outdated thread markers: resolved=0, outdated=1
- Human participants with discussion text: Alcanderian, BBuf, yuan-luo
- Automation comments/reviews omitted from high-signal summary: 0
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-05-27T03:51:47Z` `COMMENTED` by `BBuf` (https://github.com/sgl-project/sglang/pull/6627#pullrequestreview-2869489348)
- `2025-05-27T06:26:02Z` `COMMENTED` by `yuan-luo` (https://github.com/sgl-project/sglang/pull/6627#pullrequestreview-2869752063)
- `2025-05-27T06:47:34Z` `APPROVED` by `BBuf` - Please rename benchmark script to benchmark ep pre reorder triton.py (https://github.com/sgl-project/sglang/pull/6627#pullrequestreview-2869806595)
- `2025-05-28T01:41:39Z` `APPROVED` by `Alcanderian` (https://github.com/sgl-project/sglang/pull/6627#pullrequestreview-2873266951)

## Inline Comment Hotspots

- `benchmark/kernels/fused_moe_triton/benchmark_pre_reorder_triton.py`: 2 inline comment(s)

## High-Signal Discussion

- `2025-05-27T03:51:46Z` `inline` by `BBuf` `benchmark/kernels/fused_moe_triton/benchmark_pre_reorder_triton.py`:12; signals: benchmark, kernel, moe, triton; excerpt: "The batch size (bs) and topk can be combined using the product function. Refer to for more details." (https://github.com/sgl-project/sglang/pull/6627#discussion_r2108103906)
- `2025-05-27T06:26:02Z` `inline` by `yuan-luo` `benchmark/kernels/fused_moe_triton/benchmark_pre_reorder_triton.py`:12; signals: benchmark, kernel, moe, triton; excerpt: "Revised to use product." (https://github.com/sgl-project/sglang/pull/6627#discussion_r2108287334)
- `2025-05-27T06:47:34Z` `review` `APPROVED` by `BBuf`; signals: benchmark, triton; excerpt: "Please rename benchmark script to benchmark ep pre reorder triton.py" (https://github.com/sgl-project/sglang/pull/6627#pullrequestreview-2869806595)
- `2025-05-27T07:06:24Z` `issue` by `yuan-luo`; signals: benchmark, triton; excerpt: "Please rename benchmark script to benchmark ep pre reorder triton.py Done." (https://github.com/sgl-project/sglang/pull/6627#issuecomment-2911391752)
- `2025-05-26T13:40:38Z` `issue` by `BBuf`; signals: benchmark; excerpt: "The benchmark script: Before the fix result: After fix result: Good job. Can you add the benchmark script to" (https://github.com/sgl-project/sglang/pull/6627#issuecomment-2909801247)
- `2025-05-26T14:48:32Z` `issue` by `yuan-luo`; signals: benchmark; excerpt: "The benchmark script: Before the fix result: After fix result: Good job. Can you add the benchmark script to Hi @BBuf, thanks for the ..." (https://github.com/sgl-project/sglang/pull/6627#issuecomment-2909993782)
- `2025-05-26T12:55:17Z` `issue` by `yuan-luo`; signals: benchmark; excerpt: "The benchmark script: Before the fix result: After fix result:" (https://github.com/sgl-project/sglang/pull/6627#issuecomment-2909662320)
- `2025-05-27T03:39:36Z` `issue` by `yuan-luo`; signals: general review; excerpt: "Refactored the test case according to @BBuf 's comments. Before fix, the result is: After fix, the result is:" (https://github.com/sgl-project/sglang/pull/6627#issuecomment-2911003155)
