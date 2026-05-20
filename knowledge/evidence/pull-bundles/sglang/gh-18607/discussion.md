# PR Discussion Digest

- Source PR: [sgl-project/sglang#18607](https://github.com/sgl-project/sglang/pull/18607)
- Source page: `sources/prs/sglang/PR-18607.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-18607`
- Generated at: `2026-05-20T15:28:39.902437+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-02-11T11:00:01Z`
- Merged: `2026-02-12T09:13:16Z`

## Discussion Counts

- Issue comments: 2
- Review submissions: 5 (approved=1, commented=4)
- Inline review comments: 5
- Review threads observed: 3
- Resolved/outdated thread markers: resolved=3, outdated=1
- Human participants with discussion text: 1am9trash, HaiShaw
- Automation comments/reviews omitted from high-signal summary: 4
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-02-11T11:03:52Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request aims to fix an accuracy issue for a specific model configuration by adjusting ... (https://github.com/sgl-project/sglang/pull/18607#pullrequestreview-3784136330)
- `2026-02-12T03:43:52Z` `COMMENTED` by `HaiShaw` (https://github.com/sgl-project/sglang/pull/18607#pullrequestreview-3788590068)
- `2026-02-12T04:26:52Z` `COMMENTED` by `1am9trash` (https://github.com/sgl-project/sglang/pull/18607#pullrequestreview-3788680180)
- `2026-02-12T04:55:52Z` `COMMENTED` by `HaiShaw` (https://github.com/sgl-project/sglang/pull/18607#pullrequestreview-3788732851)
- `2026-02-12T04:56:27Z` `APPROVED` by `HaiShaw` (https://github.com/sgl-project/sglang/pull/18607#pullrequestreview-3788733978)

## Inline Comment Hotspots

- `python/sglang/srt/layers/attention/aiter_backend.py`: 5 inline comment(s)

## High-Signal Discussion

- `2026-02-12T04:26:52Z` `inline` by `1am9trash` `python/sglang/srt/layers/attention/aiter_backend.py`:199; signals: attention, cache, fp8, kernel, kv cache; excerpt: "Remove assert to make tp4 run with non-fp8 kv cache. Use non-ps kernel on tp8, and ps kernel on tp2, tp4. TP2: - fp8 ..." (https://github.com/sgl-project/sglang/pull/18607#discussion_r2796711893)
- `2026-02-12T03:43:43Z` `inline` by `HaiShaw` `python/sglang/srt/layers/attention/aiter_backend.py`:199; signals: attention, cache, kv cache; excerpt: "don't disable 16bit kv cache case." (https://github.com/sgl-project/sglang/pull/18607#discussion_r2796625554)
- `2026-02-12T04:55:52Z` `inline` by `HaiShaw` `python/sglang/srt/layers/attention/aiter_backend.py`:199; signals: accuracy, attention, fp8; excerpt: "Let's target accuracy on TP4 non-fp8 kv in separate PR." (https://github.com/sgl-project/sglang/pull/18607#discussion_r2796769917)
