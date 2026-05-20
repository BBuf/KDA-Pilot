# PR Discussion Digest

- Source PR: [sgl-project/sglang#11812](https://github.com/sgl-project/sglang/pull/11812)
- Source page: `sources/prs/sglang/PR-11812.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-11812`
- Generated at: `2026-05-20T15:27:27.068040+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-10-18T18:13:02Z`
- Merged: `2025-11-10T01:13:48Z`

## Discussion Counts

- Issue comments: 3
- Review submissions: 4 (commented=4)
- Inline review comments: 4
- Review threads observed: 2
- Resolved/outdated thread markers: resolved=0, outdated=0
- Human participants with discussion text: Edenzzzz, Oasis-Git, ispobock
- Automation comments/reviews omitted from high-signal summary: 3
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-10-18T18:15:18Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request adds support for piecewise CUDA graphs for models with Multi-Latent Attention (MLA), which ... (https://github.com/sgl-project/sglang/pull/11812#pullrequestreview-3353712944)
- `2025-11-03T23:35:36Z` `COMMENTED` by `Edenzzzz` (https://github.com/sgl-project/sglang/pull/11812#pullrequestreview-3413347675)
- `2025-11-08T17:38:42Z` `COMMENTED` by `ispobock` (https://github.com/sgl-project/sglang/pull/11812#pullrequestreview-3438500048)
- `2025-11-08T22:42:29Z` `COMMENTED` by `Edenzzzz` (https://github.com/sgl-project/sglang/pull/11812#pullrequestreview-3438970588)

## Inline Comment Hotspots

- `python/sglang/srt/layers/attention/flashinfer_mla_backend.py`: 3 inline comment(s)
- `python/sglang/srt/layers/rotary_embedding.py`: 1 inline comment(s)

## High-Signal Discussion

- `2025-11-08T17:38:42Z` `inline` by `ispobock` `python/sglang/srt/layers/attention/flashinfer_mla_backend.py`:329; signals: attention, cuda, flashinfer, kernel, mla; excerpt: "Hi @Edenzzzz, good question! The reason is in the forward of deepseek model ( , but we can only capture one type in the ..." (https://github.com/sgl-project/sglang/pull/11812#discussion_r2507037519)
- `2025-11-03T23:35:35Z` `inline` by `Edenzzzz` `python/sglang/srt/layers/attention/flashinfer_mla_backend.py`:329; signals: attention, cuda, flashinfer, mla; excerpt: "Wonder why piecewise cuda graph can impact attention execution?" (https://github.com/sgl-project/sglang/pull/11812#discussion_r2488159125)
- `2025-11-08T22:42:28Z` `inline` by `Edenzzzz` `python/sglang/srt/layers/attention/flashinfer_mla_backend.py`:329; signals: attention, flashinfer, mla; excerpt: "got it, ragged is MHA" (https://github.com/sgl-project/sglang/pull/11812#discussion_r2507336513)
- `2025-11-03T19:16:58Z` `issue` by `Oasis-Git`; signals: mla; excerpt: "LGTM. However I suggest postponing the merge until: 1. Merge of 12518 since the overall modification on context control is heavy in this branch ..." (https://github.com/sgl-project/sglang/pull/11812#issuecomment-3482112961)
