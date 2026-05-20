# PR Discussion Digest

- Source PR: [sgl-project/sglang#21452](https://github.com/sgl-project/sglang/pull/21452)
- Source page: `sources/prs/sglang/PR-21452.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-21452`
- Generated at: `2026-05-20T15:29:15.268180+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-03-26T04:39:10Z`
- Merged: `2026-03-28T22:57:30Z`

## Discussion Counts

- Issue comments: 6
- Review submissions: 3 (approved=1, commented=2)
- Inline review comments: 2
- Review threads observed: 1
- Resolved/outdated thread markers: resolved=0, outdated=1
- Human participants with discussion text: Fridge003, Oasis-Git, ispobock, yyihuang
- Automation comments/reviews omitted from high-signal summary: 2
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-03-27T00:58:40Z` `COMMENTED` by `Oasis-Git` - In general the change is reasonable. Here is some suggestions for revision. (https://github.com/sgl-project/sglang/pull/21452#pullrequestreview-4018276963)
- `2026-03-27T20:51:04Z` `COMMENTED` by `yyihuang` (https://github.com/sgl-project/sglang/pull/21452#pullrequestreview-4023613974)
- `2026-03-28T06:55:29Z` `APPROVED` by `Fridge003` (https://github.com/sgl-project/sglang/pull/21452#pullrequestreview-4025125318)

## Inline Comment Hotspots

- `python/sglang/srt/model_executor/piecewise_cuda_graph_runner.py`: 2 inline comment(s)

## High-Signal Discussion

- `2026-03-26T22:31:37Z` `issue` by `Fridge003`; signals: perf, performance, regression; excerpt: "There is performance regression with this PR" (https://github.com/sgl-project/sglang/pull/21452#issuecomment-4138749002)
- `2026-03-27T20:51:04Z` `inline` by `yyihuang` `python/sglang/srt/model_executor/piecewise_cuda_graph_runner.py`:748; signals: block, cuda; excerpt: "Hi I take your suggestions to update the code: - Added self.num tokens: Optional[int] = None field to ForwardContext - Eliminated both .item() GPU-CPU ..." (https://github.com/sgl-project/sglang/pull/21452#discussion_r3003171535)
- `2026-03-27T00:58:40Z` `review` `COMMENTED` by `Oasis-Git`; signals: hang; excerpt: "In general the change is reasonable. Here is some suggestions for revision." (https://github.com/sgl-project/sglang/pull/21452#pullrequestreview-4018276963)
- `2026-03-27T00:57:28Z` `inline` by `Oasis-Git` `python/sglang/srt/model_executor/piecewise_cuda_graph_runner.py`:748; signals: cuda; excerpt: "I think we can move num tokens into the ForwardContext. Also to skip the computation and sync with item(), it is suggested that the ..." (https://github.com/sgl-project/sglang/pull/21452#discussion_r2998448283)
- `2026-03-27T00:26:33Z` `issue` by `Oasis-Git`; signals: h100; excerpt: "Run the test locally with h100 on tp=1 and tp=8 and gsm test passes" (https://github.com/sgl-project/sglang/pull/21452#issuecomment-4139196640)
