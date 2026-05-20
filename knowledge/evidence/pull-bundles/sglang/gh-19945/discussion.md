# PR Discussion Digest

- Source PR: [sgl-project/sglang#19945](https://github.com/sgl-project/sglang/pull/19945)
- Source page: `sources/prs/sglang/PR-19945.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-19945`
- Generated at: `2026-05-20T15:28:57.802992+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-03-05T12:26:19Z`
- Merged: `2026-03-24T09:01:40Z`

## Discussion Counts

- Issue comments: 7
- Review submissions: 8 (approved=3, commented=5)
- Inline review comments: 6
- Review threads observed: 3
- Resolved/outdated thread markers: resolved=3, outdated=1
- Human participants with discussion text: 1am9trash, HaiShaw, hubertlu-tw
- Automation comments/reviews omitted from high-signal summary: 5
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-03-05T12:35:25Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request refactors the sparse attention forward pass for AMD GPUs, enabling a new tilelang ... (https://github.com/sgl-project/sglang/pull/19945#pullrequestreview-3896179971)
- `2026-03-06T04:11:46Z` `COMMENTED` by `1am9trash` (https://github.com/sgl-project/sglang/pull/19945#pullrequestreview-3901176615)
- `2026-03-06T04:12:22Z` `COMMENTED` by `1am9trash` (https://github.com/sgl-project/sglang/pull/19945#pullrequestreview-3901177793)
- `2026-03-06T04:12:39Z` `COMMENTED` by `1am9trash` (https://github.com/sgl-project/sglang/pull/19945#pullrequestreview-3901178385)
- `2026-03-19T08:55:56Z` `APPROVED` by `HaiShaw` (https://github.com/sgl-project/sglang/pull/19945#pullrequestreview-3973674215)
- `2026-03-20T18:49:16Z` `APPROVED` by `hubertlu-tw` - LGTM (https://github.com/sgl-project/sglang/pull/19945#pullrequestreview-3983446290)
- `2026-03-24T08:50:50Z` `COMMENTED` by `HaiShaw` - Let revert the removal of sparse attention fwd kernel v1, kept for other/document purpose (https://github.com/sgl-project/sglang/pull/19945#pullrequestreview-3997334337)
- `2026-03-24T09:01:26Z` `APPROVED` by `HaiShaw` (https://github.com/sgl-project/sglang/pull/19945#pullrequestreview-3997416481)

## Inline Comment Hotspots

- `python/sglang/srt/layers/attention/nsa/tilelang_kernel.py`: 6 inline comment(s)

## High-Signal Discussion

- `2026-03-06T04:11:46Z` `inline` by `1am9trash` `python/sglang/srt/layers/attention/nsa/tilelang_kernel.py`:891; signals: attention, kernel, tile, tma; excerpt: "In practice we didn’t see crashes because in python, index -1 is the last element, so KV[b i, -1, ...] is still in-bounds. Those ..." (https://github.com/sgl-project/sglang/pull/19945#discussion_r2893712819)
- `2026-03-06T04:12:22Z` `inline` by `1am9trash` `python/sglang/srt/layers/attention/nsa/tilelang_kernel.py`:896; signals: attention, kernel, tile; excerpt: "Same the previous one comment." (https://github.com/sgl-project/sglang/pull/19945#discussion_r2893714157)
- `2026-03-06T04:12:38Z` `inline` by `1am9trash` `python/sglang/srt/layers/attention/nsa/tilelang_kernel.py`:753; signals: attention, kernel, tile; excerpt: "Remove redundancy max loop." (https://github.com/sgl-project/sglang/pull/19945#discussion_r2893714740)
- `2026-03-24T08:50:50Z` `review` `COMMENTED` by `HaiShaw`; signals: attention, kernel; excerpt: "Let revert the removal of sparse attention fwd kernel v1, kept for other/document purpose" (https://github.com/sgl-project/sglang/pull/19945#pullrequestreview-3997334337)
- `2026-03-06T01:14:20Z` `issue` by `1am9trash`; signals: speedup; excerpt: "@1am9trash please provide commands for the speedup section. server cmd: client cmd: Also update in PR introduction." (https://github.com/sgl-project/sglang/pull/19945#issuecomment-4008848803)
- `2026-03-05T15:14:29Z` `issue` by `HaiShaw`; signals: speedup; excerpt: "@1am9trash please provide commands for the speedup section." (https://github.com/sgl-project/sglang/pull/19945#issuecomment-4005793524)
