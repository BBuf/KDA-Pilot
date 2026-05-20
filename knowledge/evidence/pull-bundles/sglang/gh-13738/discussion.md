# PR Discussion Digest

- Source PR: [sgl-project/sglang#13738](https://github.com/sgl-project/sglang/pull/13738)
- Source page: `sources/prs/sglang/PR-13738.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-13738`
- Generated at: `2026-05-20T15:27:51.011635+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-11-21T17:01:27Z`
- Merged: `2025-12-02T06:16:25Z`

## Discussion Counts

- Issue comments: 3
- Review submissions: 3 (approved=1, changes_requested=1, commented=1)
- Inline review comments: 0
- Review threads observed: 0
- Resolved/outdated thread markers: resolved=0, outdated=0
- Human participants with discussion text: Qiaolin-Yu, b8zhong, hnyls2002
- Automation comments/reviews omitted from high-signal summary: 2
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-11-21T17:03:31Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request addresses a bug in the TRT-LLM MLA speculative decoding path by removing the ... (https://github.com/sgl-project/sglang/pull/13738#pullrequestreview-3493653465)
- `2025-11-22T02:42:48Z` `CHANGES_REQUESTED` by `Qiaolin-Yu` - Why delete this? This cache is important and was added a very long time ago. Or perhaps the ... (https://github.com/sgl-project/sglang/pull/13738#pullrequestreview-3495276876)
- `2025-11-22T04:21:38Z` `APPROVED` by `Qiaolin-Yu` (https://github.com/sgl-project/sglang/pull/13738#pullrequestreview-3495500165)

## Inline Comment Hotspots

- No inline review comments were returned by GitHub.

## High-Signal Discussion

- `2025-11-22T02:42:48Z` `review` `CHANGES_REQUESTED` by `Qiaolin-Yu`; signals: cache; excerpt: "Why delete this? This cache is important and was added a very long time ago. Or perhaps the previous usage of this cache here ..." (https://github.com/sgl-project/sglang/pull/13738#pullrequestreview-3495276876)
- `2025-11-22T18:27:07Z` `issue` by `hnyls2002`; signals: fp4; excerpt: "@Qiaolin-Yu @b8zhong Please track the CI status. After the test/srt/test deepseek v3 fp4 4gpu.py passes, add a read-to-merge label" (https://github.com/sgl-project/sglang/pull/13738#issuecomment-3566949087)
