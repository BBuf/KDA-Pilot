# PR Discussion Digest

- Source PR: [sgl-project/sglang#22258](https://github.com/sgl-project/sglang/pull/22258)
- Source page: `sources/prs/sglang/PR-22258.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-22258`
- Generated at: `2026-05-20T15:29:23.466494+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-04-07T09:32:47Z`
- Merged: `2026-04-10T08:08:32Z`

## Discussion Counts

- Issue comments: 4
- Review submissions: 3 (approved=1, changes_requested=1, commented=1)
- Inline review comments: 2
- Review threads observed: 2
- Resolved/outdated thread markers: resolved=0, outdated=2
- Human participants with discussion text: HaiShaw, Jacob0226
- Automation comments/reviews omitted from high-signal summary: 4
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-04-07T09:36:05Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request introduces support for Native Sparse Attention (NSA) with FP8 quantization on AMD (HIP) ... (https://github.com/sgl-project/sglang/pull/22258#pullrequestreview-4067126630)
- `2026-04-10T00:03:16Z` `CHANGES_REQUESTED` by `HaiShaw` - Please align the producer use use aiter and is gfx95 supported, and consumer use is hip. After 22422 ... (https://github.com/sgl-project/sglang/pull/22258#pullrequestreview-4086231547)
- `2026-04-10T07:45:01Z` `APPROVED` by `HaiShaw` (https://github.com/sgl-project/sglang/pull/22258#pullrequestreview-4088153088)

## Inline Comment Hotspots

- `python/sglang/srt/layers/attention/nsa/nsa_indexer.py`: 2 inline comment(s)

## High-Signal Discussion

- `2026-04-10T00:03:16Z` `review` `CHANGES_REQUESTED` by `HaiShaw`; signals: general review; excerpt: "Please align the producer use use aiter and is gfx95 supported, and consumer use is hip. After 22422 you can use use aiter gfx95" (https://github.com/sgl-project/sglang/pull/22258#pullrequestreview-4086231547)
- `2026-04-10T01:26:29Z` `issue` by `Jacob0226`; signals: aligned; excerpt: "Please align the producer use use aiter and is gfx95 supported, and consumer use is hip. After 22422 you can use use aiter gfx95 ..." (https://github.com/sgl-project/sglang/pull/22258#issuecomment-4219212817)
