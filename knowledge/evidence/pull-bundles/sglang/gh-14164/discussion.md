# PR Discussion Digest

- Source PR: [sgl-project/sglang#14164](https://github.com/sgl-project/sglang/pull/14164)
- Source page: `sources/prs/sglang/PR-14164.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-14164`
- Generated at: `2026-05-20T15:27:57.045021+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-11-30T10:39:20Z`
- Merged: `2025-12-19T17:59:27Z`

## Discussion Counts

- Issue comments: 5
- Review submissions: 10 (approved=1, commented=9)
- Inline review comments: 16
- Review threads observed: 12
- Resolved/outdated thread markers: resolved=2, outdated=6
- Human participants with discussion text: Oasis-Git, ch-wan, ispobock, merrymercy
- Automation comments/reviews omitted from high-signal summary: 6
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 5

## Review Decisions

- `2025-11-30T10:42:20Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request adds support for Expert Parallelism in Piecewise CUDA Graphs, which is a significant ... (https://github.com/sgl-project/sglang/pull/14164#pullrequestreview-3521227932)
- `2025-11-30T23:32:53Z` `COMMENTED` by `ch-wan` - Could you fix this issue? (https://github.com/sgl-project/sglang/pull/14164#pullrequestreview-3522690575)
- `2025-12-02T13:20:53Z` `COMMENTED` by `ispobock` (https://github.com/sgl-project/sglang/pull/14164#pullrequestreview-3530013111)
- `2025-12-02T19:19:47Z` `COMMENTED` by `Oasis-Git` (https://github.com/sgl-project/sglang/pull/14164#pullrequestreview-3531776358)
- `2025-12-02T19:20:11Z` `COMMENTED` by `Oasis-Git` (https://github.com/sgl-project/sglang/pull/14164#pullrequestreview-3531777564)
- `2025-12-02T19:30:23Z` `COMMENTED` by `Oasis-Git` (https://github.com/sgl-project/sglang/pull/14164#pullrequestreview-3531807793)
- `2025-12-03T13:52:16Z` `COMMENTED` by `ispobock` (https://github.com/sgl-project/sglang/pull/14164#pullrequestreview-3535155655)
- `2025-12-03T13:53:34Z` `APPROVED` by `ispobock` - Overall LGTM. We can merge it once all CIs passed. (https://github.com/sgl-project/sglang/pull/14164#pullrequestreview-3535165672)
- `2025-12-03T19:12:25Z` `COMMENTED` by `Oasis-Git` (https://github.com/sgl-project/sglang/pull/14164#pullrequestreview-3536541122)

## Inline Comment Hotspots

- `python/sglang/srt/layers/moe/fused_moe_triton/layer.py`: 5 inline comment(s)
- `test/srt/run_suite.py`: 4 inline comment(s)
- `python/sglang/srt/model_executor/model_runner.py`: 2 inline comment(s)
- `test/srt/test_piecewise_cuda_graph.py`: 2 inline comment(s)
- `python/sglang/srt/compilation/piecewise_context_manager.py`: 1 inline comment(s)
- `python/sglang/srt/layers/moe/ep_moe/layer.py`: 1 inline comment(s)
- `python/sglang/srt/model_executor/piecewise_cuda_graph_runner.py`: 1 inline comment(s)

## High-Signal Discussion

- `2025-12-02T13:18:20Z` `inline` by `ispobock` `python/sglang/srt/layers/moe/fused_moe_triton/layer.py`:1142; signals: moe, triton; excerpt: "use TopKOutputChecker.format is standard?" (https://github.com/sgl-project/sglang/pull/14164#discussion_r2581147494)
- `2025-12-02T19:20:11Z` `inline` by `Oasis-Git` `python/sglang/srt/layers/moe/fused_moe_triton/layer.py`:1142; signals: moe, triton; excerpt: "resolved" (https://github.com/sgl-project/sglang/pull/14164#discussion_r2582520250)
- `2025-12-02T13:06:27Z` `inline` by `ispobock` `test/srt/test_piecewise_cuda_graph.py`:434; signals: cuda; excerpt: "I think we can move it to another file, for example test piecewise cuda graph parallel.py. We can also add other parallel related test ..." (https://github.com/sgl-project/sglang/pull/14164#discussion_r2581099616)
- `2025-12-02T19:19:47Z` `inline` by `Oasis-Git` `test/srt/test_piecewise_cuda_graph.py`:434; signals: cuda; excerpt: "sounds good" (https://github.com/sgl-project/sglang/pull/14164#discussion_r2582519170)
- `2025-11-30T23:32:53Z` `review` `COMMENTED` by `ch-wan`; signals: general review; excerpt: "Could you fix this issue?" (https://github.com/sgl-project/sglang/pull/14164#pullrequestreview-3522690575)
- `2025-12-02T13:20:37Z` `inline` by `ispobock` `test/srt/run_suite.py`:152; signals: general review; excerpt: "I saw this test is already in per-commit-4-gpu." (https://github.com/sgl-project/sglang/pull/14164#discussion_r2581157368)
- `2025-12-02T19:30:23Z` `inline` by `Oasis-Git` `test/srt/run_suite.py`:152; signals: general review; excerpt: "Looks like it's added by @yuan-luo. Should we remove it to setup a new test parallel file?" (https://github.com/sgl-project/sglang/pull/14164#discussion_r2582545472)
- `2025-12-03T13:52:08Z` `inline` by `ispobock` `test/srt/run_suite.py`:161; signals: general review; excerpt: "Could you verify if it's still 1200?" (https://github.com/sgl-project/sglang/pull/14164#discussion_r2585204693)
- `2025-12-03T19:12:25Z` `inline` by `Oasis-Git` `test/srt/run_suite.py`:161; signals: general review; excerpt: "sure." (https://github.com/sgl-project/sglang/pull/14164#discussion_r2586309954)
