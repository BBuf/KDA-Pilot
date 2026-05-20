# PR Discussion Digest

- Source PR: [sgl-project/sglang#15904](https://github.com/sgl-project/sglang/pull/15904)
- Source page: `sources/prs/sglang/PR-15904.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-15904`
- Generated at: `2026-05-20T15:28:18.579617+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-12-26T15:53:49Z`
- Merged: `2026-01-28T16:55:09Z`

## Discussion Counts

- Issue comments: 3
- Review submissions: 6 (approved=3, commented=3)
- Inline review comments: 3
- Review threads observed: 2
- Resolved/outdated thread markers: resolved=2, outdated=1
- Human participants with discussion text: OrangeRedeng, iforgetmyname, ping1jing2, ssshinigami
- Automation comments/reviews omitted from high-signal summary: 3
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-12-26T15:59:16Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request introduces two main changes: adding NPU support for non-quantized Mixture-of-Experts (MoE) layers and ... (https://github.com/sgl-project/sglang/pull/15904#pullrequestreview-3613641965)
- `2026-01-19T09:41:31Z` `APPROVED` by `ssshinigami` - lgtm (https://github.com/sgl-project/sglang/pull/15904#pullrequestreview-3677184778)
- `2026-01-27T06:03:03Z` `APPROVED` by `ping1jing2` (https://github.com/sgl-project/sglang/pull/15904#pullrequestreview-3709270958)
- `2026-01-27T10:58:33Z` `COMMENTED` by `ping1jing2` (https://github.com/sgl-project/sglang/pull/15904#pullrequestreview-3710515450)
- `2026-01-27T13:04:10Z` `COMMENTED` by `OrangeRedeng` (https://github.com/sgl-project/sglang/pull/15904#pullrequestreview-3711078767)
- `2026-01-28T16:54:12Z` `APPROVED` by `iforgetmyname` (https://github.com/sgl-project/sglang/pull/15904#pullrequestreview-3717858528)

## Inline Comment Hotspots

- `test/srt/ascend/test_ascend_memory_consumption.py‎`: 2 inline comment(s)
- `python/sglang/srt/layers/quantization/unquant.py`: 1 inline comment(s)

## High-Signal Discussion

- `2026-01-27T10:58:33Z` `inline` by `ping1jing2` `test/srt/ascend/test_ascend_memory_consumption.py‎`:1; signals: memory, register; excerpt: "As you can see from maybe you should move your test file into test/manual or test/registered" (https://github.com/sgl-project/sglang/pull/15904#discussion_r2731448061)
- `2026-01-27T13:04:10Z` `inline` by `OrangeRedeng` `test/srt/ascend/test_ascend_memory_consumption.py‎`:1; signals: memory, register; excerpt: "Moved to test/registered (nightly)" (https://github.com/sgl-project/sglang/pull/15904#discussion_r2731915528)
