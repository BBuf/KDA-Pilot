# PR Discussion Digest

- Source PR: [sgl-project/sglang#5822](https://github.com/sgl-project/sglang/pull/5822)
- Source page: `sources/prs/sglang/PR-5822.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-5822`
- Generated at: `2026-05-20T15:30:31.344040+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-04-28T07:20:16Z`
- Merged: `2025-05-09T06:17:14Z`

## Discussion Counts

- Issue comments: 1
- Review submissions: 3 (approved=1, commented=2)
- Inline review comments: 2
- Review threads observed: 1
- Resolved/outdated thread markers: resolved=1, outdated=0
- Human participants with discussion text: ispobock, lambert0312, xu-yfei
- Automation comments/reviews omitted from high-signal summary: 0
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-04-28T12:40:18Z` `COMMENTED` by `ispobock` (https://github.com/sgl-project/sglang/pull/5822#pullrequestreview-2799155857)
- `2025-04-28T13:38:22Z` `COMMENTED` by `xu-yfei` (https://github.com/sgl-project/sglang/pull/5822#pullrequestreview-2799337502)
- `2025-05-01T12:57:27Z` `APPROVED` by `ispobock` - LGTM. (https://github.com/sgl-project/sglang/pull/5822#pullrequestreview-2809742513)

## Inline Comment Hotspots

- `python/sglang/srt/layers/attention/flashinfer_mla_backend.py`: 2 inline comment(s)

## High-Signal Discussion

- `2025-04-28T13:38:22Z` `inline` by `xu-yfei` `python/sglang/srt/layers/attention/flashinfer_mla_backend.py`:396; signals: attention, flashinfer, mla; excerpt: "in flashinfer run: out will has the same strides and shape with q nope even if q nope is not contiguous, it will report ..." (https://github.com/sgl-project/sglang/pull/5822#discussion_r2063679841)
- `2025-04-28T12:39:23Z` `inline` by `ispobock` `python/sglang/srt/layers/attention/flashinfer_mla_backend.py`:396; signals: attention, flashinfer, mla; excerpt: "o is returned, why do we need to pass it in?" (https://github.com/sgl-project/sglang/pull/5822#discussion_r2063572425)
- `2025-04-28T08:56:43Z` `issue` by `lambert0312`; signals: general review; excerpt: "I pulled the latest commit and did some experiments, and it seems to be consistent with the optimizations mentioned above." (https://github.com/sgl-project/sglang/pull/5822#issuecomment-2834508087)
