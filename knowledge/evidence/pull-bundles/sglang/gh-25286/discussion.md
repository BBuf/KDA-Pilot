# PR Discussion Digest

- Source PR: [sgl-project/sglang#25286](https://github.com/sgl-project/sglang/pull/25286)
- Source page: `sources/prs/sglang/PR-25286.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-25286`
- Generated at: `2026-05-20T15:29:47.126376+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-05-14T13:56:20Z`
- Merged: `2026-05-19T21:00:24Z`

## Discussion Counts

- Issue comments: 5
- Review submissions: 4 (approved=1, commented=3)
- Inline review comments: 2
- Review threads observed: 1
- Resolved/outdated thread markers: resolved=1, outdated=0
- Human participants with discussion text: BBuf, Ratish1
- Automation comments/reviews omitted from high-signal summary: 3
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-05-14T13:58:27Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request introduces a helper function as column scale to normalize scale tensors into column ... (https://github.com/sgl-project/sglang/pull/25286#pullrequestreview-4290529745)
- `2026-05-14T14:11:33Z` `COMMENTED` by `Ratish1` (https://github.com/sgl-project/sglang/pull/25286#pullrequestreview-4290629503)
- `2026-05-19T02:42:32Z` `APPROVED` by `BBuf` (https://github.com/sgl-project/sglang/pull/25286#pullrequestreview-4315311127)
- `2026-05-19T02:47:04Z` `COMMENTED` by `BBuf` - Nice fix. One small test suggestion: the new regression currently only exercises square shapes (M == N == ... (https://github.com/sgl-project/sglang/pull/25286#pullrequestreview-4315325768)

## Inline Comment Hotspots

- `python/sglang/srt/layers/quantization/fp8_kernel.py`: 2 inline comment(s)

## High-Signal Discussion

- `2026-05-14T14:11:33Z` `inline` by `Ratish1` `python/sglang/srt/layers/quantization/fp8_kernel.py`:1948; signals: fp8, kernel, layout, triton, vector; excerpt: "Applied, with one additional guard: the helper now only normalizes row/column layouts when the scale is 2D, and triton scaled mm asserts the normalized ..." (https://github.com/sgl-project/sglang/pull/25286#discussion_r3241925659)
- `2026-05-19T02:47:04Z` `review` `COMMENTED` by `BBuf`; signals: regression; excerpt: "Nice fix. One small test suggestion: the new regression currently only exercises square shapes (M == N == K). Could we add a non-square ..." (https://github.com/sgl-project/sglang/pull/25286#pullrequestreview-4315325768)
- `2026-05-19T06:24:23Z` `issue` by `Ratish1`; signals: regression; excerpt: "Nice fix. One small test suggestion: the new regression currently only exercises square shapes (M == N == K). Could we add a non-square ..." (https://github.com/sgl-project/sglang/pull/25286#issuecomment-4484984580)
- `2026-05-14T14:13:47Z` `issue` by `Ratish1`; signals: register, triton; excerpt: "/rerun-test test/registered/quant/test triton scaled mm.py" (https://github.com/sgl-project/sglang/pull/25286#issuecomment-4451456507)
