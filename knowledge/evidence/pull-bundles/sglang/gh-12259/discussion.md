# PR Discussion Digest

- Source PR: [sgl-project/sglang#12259](https://github.com/sgl-project/sglang/pull/12259)
- Source page: `sources/prs/sglang/PR-12259.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-12259`
- Generated at: `2026-05-20T15:27:34.187906+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-10-28T07:39:11Z`
- Merged: `2025-10-29T02:10:38Z`

## Discussion Counts

- Issue comments: 7
- Review submissions: 1 (commented=1)
- Inline review comments: 4
- Review threads observed: 4
- Resolved/outdated thread markers: resolved=4, outdated=3
- Human participants with discussion text: ch-wan, ishandhanani, trevor-m, wenscarl
- Automation comments/reviews omitted from high-signal summary: 6
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-10-28T07:41:32Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request addresses a bug where w13 weight fp8 and w2 weight fp8 were missing ... (https://github.com/sgl-project/sglang/pull/12259#pullrequestreview-3387090421)

## Inline Comment Hotspots

- `python/sglang/srt/layers/quantization/fp8.py`: 3 inline comment(s)
- `python/sglang/srt/layers/moe/ep_moe/layer.py`: 1 inline comment(s)

## High-Signal Discussion

- `2025-10-28T20:11:22Z` `issue` by `ch-wan`; signals: nan; excerpt: "@ishandhanani @wenscarl I have pushed a fix but I don't have a test environment. Could you take a look?" (https://github.com/sgl-project/sglang/pull/12259#issuecomment-3458286674)
- `2025-10-29T00:41:25Z` `issue` by `trevor-m`; signals: general review; excerpt: "@ch-wan I am able to successfully launch the PD disagg server (same command as @wenscarl I believe) with your latest update" (https://github.com/sgl-project/sglang/pull/12259#issuecomment-3459196298)
