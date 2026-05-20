# PR Discussion Digest

- Source PR: [sgl-project/sglang#4887](https://github.com/sgl-project/sglang/pull/4887)
- Source page: `sources/prs/sglang/PR-4887.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-4887`
- Generated at: `2026-05-20T15:30:17.416435+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-03-29T15:40:17Z`
- Merged: `2025-04-17T08:50:48Z`

## Discussion Counts

- Issue comments: 10
- Review submissions: 5 (approved=4, commented=1)
- Inline review comments: 6
- Review threads observed: 6
- Resolved/outdated thread markers: resolved=6, outdated=6
- Human participants with discussion text: DavidBao03, FlamingoPg, Titan-p, gabinguo, ispobock, woodx9, zhyncs
- Automation comments/reviews omitted from high-signal summary: 0
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 7

## Review Decisions

- `2025-03-30T04:29:35Z` `COMMENTED` by `ispobock` (https://github.com/sgl-project/sglang/pull/4887#pullrequestreview-2727799764)
- `2025-04-09T15:16:55Z` `APPROVED` by `FlamingoPg` - LGTM to me～ (https://github.com/sgl-project/sglang/pull/4887#pullrequestreview-2753864750)
- `2025-04-10T01:22:14Z` `APPROVED` by `Titan-p` (https://github.com/sgl-project/sglang/pull/4887#pullrequestreview-2755112694)
- `2025-04-13T16:38:57Z` `APPROVED` by `ispobock` (https://github.com/sgl-project/sglang/pull/4887#pullrequestreview-2762795379)
- `2025-04-17T08:50:39Z` `APPROVED` by `zhyncs` (https://github.com/sgl-project/sglang/pull/4887#pullrequestreview-2775049501)

## Inline Comment Hotspots

- `python/sglang/srt/layers/attention/triton_ops/extend_attention.py`: 4 inline comment(s)
- `python/sglang/srt/layers/attention/flashattention_backend.py`: 1 inline comment(s)
- `python/sglang/srt/layers/radix_attention.py`: 1 inline comment(s)

## High-Signal Discussion

- `2025-03-30T04:21:39Z` `inline` by `ispobock` `python/sglang/srt/layers/attention/flashattention_backend.py`:162; signals: attention, flashinfer, triton; excerpt: "Cross attention seems only for flashinfer backend. Don't need to add this condition for flashattention and triton backend." (https://github.com/sgl-project/sglang/pull/4887#discussion_r2020061136)
- `2025-03-30T04:26:47Z` `inline` by `ispobock` `python/sglang/srt/layers/attention/triton_ops/extend_attention.py`:209; signals: attention, block, triton; excerpt: "cur block m end should adjusted for non causal case. ref:" (https://github.com/sgl-project/sglang/pull/4887#discussion_r2020061981)
- `2025-03-30T04:22:27Z` `inline` by `ispobock` `python/sglang/srt/layers/attention/triton_ops/extend_attention.py`:99; signals: attention, triton; excerpt: "Don't need to modify here? cur seq len extend = cur seq len for encoder model." (https://github.com/sgl-project/sglang/pull/4887#discussion_r2020061211)
- `2025-03-30T04:23:01Z` `inline` by `ispobock` `python/sglang/srt/layers/attention/triton_ops/extend_attention.py`:136; signals: attention, triton; excerpt: "Don't need to modify here? There is no prefix part." (https://github.com/sgl-project/sglang/pull/4887#discussion_r2020061351)
- `2025-03-30T04:27:45Z` `inline` by `ispobock` `python/sglang/srt/layers/attention/triton_ops/extend_attention.py`:268; signals: attention, triton; excerpt: "mask non causal = mask m[:, None] & mask n[None, :]" (https://github.com/sgl-project/sglang/pull/4887#discussion_r2020062103)
- `2025-04-09T11:59:53Z` `issue` by `woodx9`; signals: accuracy, attention; excerpt: "Due to embedding accuracy issues,will not use fa3 as the attention backend temporarily. @Titan-p cc" (https://github.com/sgl-project/sglang/pull/4887#issuecomment-2789462559)
- `2025-03-30T04:29:18Z` `inline` by `ispobock` `python/sglang/srt/layers/radix_attention.py`:21; signals: attention; excerpt: "Use enum type?" (https://github.com/sgl-project/sglang/pull/4887#discussion_r2020062337)
- `2025-03-31T15:25:35Z` `issue` by `woodx9`; signals: cache; excerpt: "have to --disable-radix-cache and --chunked-prefill-size -1. or some embedding can be wrong." (https://github.com/sgl-project/sglang/pull/4887#issuecomment-2766591099)
