# PR Discussion Digest

- Source PR: [sgl-project/sglang#13022](https://github.com/sgl-project/sglang/pull/13022)
- Source page: `sources/prs/sglang/PR-13022.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-13022`
- Generated at: `2026-05-20T15:27:42.950254+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-11-10T23:48:00Z`
- Merged: `2025-11-17T20:20:49Z`

## Discussion Counts

- Issue comments: 4
- Review submissions: 3 (approved=2, commented=1)
- Inline review comments: 9
- Review threads observed: 9
- Resolved/outdated thread markers: resolved=9, outdated=8
- Human participants with discussion text: Fridge003, hlu1
- Automation comments/reviews omitted from high-signal summary: 11
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-11-10T23:49:31Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request introduces a torch.compile'd version of torch.cat to optimize concatenation operations in the NSA ... (https://github.com/sgl-project/sglang/pull/13022#pullrequestreview-3445637191)
- `2025-11-15T19:55:37Z` `APPROVED` by `Fridge003` (https://github.com/sgl-project/sglang/pull/13022#pullrequestreview-3468315939)
- `2025-11-17T20:20:37Z` `APPROVED` by `Fridge003` (https://github.com/sgl-project/sglang/pull/13022#pullrequestreview-3474428224)

## Inline Comment Hotspots

- `python/sglang/srt/layers/attention/nsa_backend.py`: 9 inline comment(s)

## High-Signal Discussion

- `2025-11-11T06:00:12Z` `issue` by `hlu1`; signals: benchmark, compile, mla, perf; excerpt: "@hlu1 Have you tried concat mla absorb q general , like in this PR Yes, I put the perf comparison results and next steps ..." (https://github.com/sgl-project/sglang/pull/13022#issuecomment-3515123638)
- `2025-11-11T03:06:42Z` `issue` by `Fridge003`; signals: mla; excerpt: "@hlu1 Have you tried concat mla absorb q general , like in this PR" (https://github.com/sgl-project/sglang/pull/13022#issuecomment-3514807491)
