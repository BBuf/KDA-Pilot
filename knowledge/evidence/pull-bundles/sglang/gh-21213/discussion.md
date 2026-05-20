# PR Discussion Digest

- Source PR: [sgl-project/sglang#21213](https://github.com/sgl-project/sglang/pull/21213)
- Source page: `sources/prs/sglang/PR-21213.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-21213`
- Generated at: `2026-05-20T15:29:12.023743+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-03-23T12:32:22Z`
- Merged: `2026-04-05T05:13:29Z`

## Discussion Counts

- Issue comments: 1
- Review submissions: 7 (approved=2, commented=5)
- Inline review comments: 7
- Review threads observed: 5
- Resolved/outdated thread markers: resolved=5, outdated=3
- Human participants with discussion text: 1am9trash, HaiShaw, ZiguanWang, kkHuang-amd
- Automation comments/reviews omitted from high-signal summary: 5
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-03-23T12:38:34Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request adds support for MLA with fewer than 16 heads by using head repetition, ... (https://github.com/sgl-project/sglang/pull/21213#pullrequestreview-3991428041)
- `2026-03-31T13:12:38Z` `COMMENTED` by `kkHuang-amd` (https://github.com/sgl-project/sglang/pull/21213#pullrequestreview-4037286042)
- `2026-04-01T02:46:26Z` `COMMENTED` by `ZiguanWang` (https://github.com/sgl-project/sglang/pull/21213#pullrequestreview-4041351403)
- `2026-04-01T03:20:31Z` `COMMENTED` by `1am9trash` (https://github.com/sgl-project/sglang/pull/21213#pullrequestreview-4041440244)
- `2026-04-01T03:30:22Z` `COMMENTED` by `ZiguanWang` (https://github.com/sgl-project/sglang/pull/21213#pullrequestreview-4041459158)
- `2026-04-01T05:47:28Z` `APPROVED` by `kkHuang-amd` - LGTM (https://github.com/sgl-project/sglang/pull/21213#pullrequestreview-4041815509)
- `2026-04-05T05:12:21Z` `APPROVED` by `HaiShaw` (https://github.com/sgl-project/sglang/pull/21213#pullrequestreview-4059119760)

## Inline Comment Hotspots

- `python/sglang/srt/layers/attention/aiter_backend.py`: 4 inline comment(s)
- `test/registered/amd/test_kimi_k25_mxfp4.py`: 3 inline comment(s)

## High-Signal Discussion

- `2026-03-31T13:12:38Z` `inline` by `kkHuang-amd` `python/sglang/srt/layers/attention/aiter_backend.py`:585; signals: attention, dtype, hang, mla; excerpt: "Do we need to do new empty twice, one is for o, another is for o out? Maybe we can do the similar below ..." (https://github.com/sgl-project/sglang/pull/21213#discussion_r3015826091)
- `2026-04-01T03:20:31Z` `inline` by `1am9trash` `test/registered/amd/test_kimi_k25_mxfp4.py`:38; signals: fp4, mxfp4, register; excerpt: "This comment may be outdated. Need to remove it?" (https://github.com/sgl-project/sglang/pull/21213#discussion_r3019537407)
- `2026-04-01T03:30:22Z` `inline` by `ZiguanWang` `test/registered/amd/test_kimi_k25_mxfp4.py`:38; signals: fp4, mxfp4, register; excerpt: "I‘ve already removed this comment." (https://github.com/sgl-project/sglang/pull/21213#discussion_r3019558544)
- `2026-04-01T02:46:26Z` `inline` by `ZiguanWang` `python/sglang/srt/layers/attention/aiter_backend.py`:585; signals: attention; excerpt: "I've updated the code according to your review comments and removed the redundant new empty." (https://github.com/sgl-project/sglang/pull/21213#discussion_r3019454305)
