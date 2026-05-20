# PR Discussion Digest

- Source PR: [sgl-project/sglang#17450](https://github.com/sgl-project/sglang/pull/17450)
- Source page: `sources/prs/sglang/PR-17450.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-17450`
- Generated at: `2026-05-20T15:28:29.139908+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-01-21T01:40:03Z`
- Merged: `2026-03-12T00:01:02Z`

## Discussion Counts

- Issue comments: 6
- Review submissions: 4 (approved=1, commented=3)
- Inline review comments: 4
- Review threads observed: 4
- Resolved/outdated thread markers: resolved=2, outdated=2
- Human participants with discussion text: HaiShaw, hubertlu-tw, kkHuang-amd, yichiche
- Automation comments/reviews omitted from high-signal summary: 1
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-03-11T08:00:03Z` `COMMENTED` by `kkHuang-amd` (https://github.com/sgl-project/sglang/pull/17450#pullrequestreview-3927624574)
- `2026-03-11T08:00:13Z` `COMMENTED` by `kkHuang-amd` (https://github.com/sgl-project/sglang/pull/17450#pullrequestreview-3927625560)
- `2026-03-11T08:22:59Z` `COMMENTED` by `HaiShaw` - comments left inline (https://github.com/sgl-project/sglang/pull/17450#pullrequestreview-3927730064)
- `2026-03-11T23:59:57Z` `APPROVED` by `HaiShaw` - address TritonMultiStepDraftBackend later. (https://github.com/sgl-project/sglang/pull/17450#pullrequestreview-3933169923)

## Inline Comment Hotspots

- `python/sglang/srt/layers/attention/aiter_backend.py`: 2 inline comment(s)
- `python/sglang/srt/speculative/eagle_worker_v2.py`: 1 inline comment(s)
- `test/registered/amd/test_deepseek_r1_mxfp4_8gpu.py`: 1 inline comment(s)

## High-Signal Discussion

- `2026-02-26T15:09:29Z` `issue` by `yichiche`; signals: attention, benchmark, kernel, mla, perf, performance, speedup, triton; excerpt: "In benchmark , perhaps we could put a table for performance comparison to show the motivation why we would like to enable EAGLE2 although ..." (https://github.com/sgl-project/sglang/pull/17450#issuecomment-3967235211)
- `2026-02-26T18:21:44Z` `issue` by `hubertlu-tw`; signals: attention, benchmark, kernel, mla, perf, performance, speedup, triton; excerpt: "In benchmark , perhaps we could put a table for performance comparison to show the motivation why we would like to enable EAGLE2 although ..." (https://github.com/sgl-project/sglang/pull/17450#issuecomment-3968396405)
- `2026-02-25T21:50:19Z` `issue` by `hubertlu-tw`; signals: attention, benchmark, mla, perf, performance, speedup; excerpt: "In benchmark , perhaps we could put a table for performance comparison to show the motivation why we would like to enable EAGLE2 although ..." (https://github.com/sgl-project/sglang/pull/17450#issuecomment-3962307107)
- `2026-03-11T08:21:07Z` `inline` by `HaiShaw` `test/registered/amd/test_deepseek_r1_mxfp4_8gpu.py`:92; signals: fp4, mxfp4, perf, register; excerpt: "Have we seen perf benefits from overlap stream on ROCm?" (https://github.com/sgl-project/sglang/pull/17450#discussion_r2916677838)
- `2026-02-25T08:04:27Z` `issue` by `yichiche`; signals: benchmark, perf, performance; excerpt: "In benchmark , perhaps we could put a table for performance comparison to show the motivation why we would like to enable EAGLE2 although ..." (https://github.com/sgl-project/sglang/pull/17450#issuecomment-3957505028)
- `2026-03-11T08:00:03Z` `inline` by `kkHuang-amd` `python/sglang/srt/layers/attention/aiter_backend.py`:1221; signals: attention; excerpt: "Remove redundant parts" (https://github.com/sgl-project/sglang/pull/17450#discussion_r2916581313)
- `2026-03-11T08:00:13Z` `inline` by `kkHuang-amd` `python/sglang/srt/layers/attention/aiter_backend.py`:1221; signals: attention; excerpt: "Remove redundant parts" (https://github.com/sgl-project/sglang/pull/17450#discussion_r2916582111)
- `2026-03-11T08:20:03Z` `inline` by `HaiShaw` `python/sglang/srt/speculative/eagle_worker_v2.py`:285; signals: triton; excerpt: "Below, where is is hip and isinstance(self.draft attn backend, TritonMultiStepDraftBackend) case?" (https://github.com/sgl-project/sglang/pull/17450#discussion_r2916672891)
- `2026-03-11T08:22:59Z` `review` `COMMENTED` by `HaiShaw`; signals: general review; excerpt: "comments left inline" (https://github.com/sgl-project/sglang/pull/17450#pullrequestreview-3927730064)
- `2026-03-11T23:59:57Z` `review` `APPROVED` by `HaiShaw`; signals: triton; excerpt: "address TritonMultiStepDraftBackend later." (https://github.com/sgl-project/sglang/pull/17450#pullrequestreview-3933169923)
