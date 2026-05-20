# PR Discussion Digest

- Source PR: [sgl-project/sglang#14311](https://github.com/sgl-project/sglang/pull/14311)
- Source page: `sources/prs/sglang/PR-14311.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-14311`
- Generated at: `2026-05-20T15:27:58.827655+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-12-02T18:53:38Z`
- Merged: `2026-01-30T05:01:58Z`

## Discussion Counts

- Issue comments: 5
- Review submissions: 2 (commented=2)
- Inline review comments: 2
- Review threads observed: 1
- Resolved/outdated thread markers: resolved=1, outdated=1
- Human participants with discussion text: heiderich, koush
- Automation comments/reviews omitted from high-signal summary: 3
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-12-02T18:55:04Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request updates the block size assignments for the sm120 (Blackwell) architecture to resolve an ... (https://github.com/sgl-project/sglang/pull/14311#pullrequestreview-3531691526)
- `2025-12-02T18:59:54Z` `COMMENTED` by `koush` (https://github.com/sgl-project/sglang/pull/14311#pullrequestreview-3531706969)

## Inline Comment Hotspots

- `python/sglang/srt/layers/attention/triton_ops/extend_attention.py`: 2 inline comment(s)

## High-Signal Discussion

- `2025-12-02T18:59:54Z` `inline` by `koush` `python/sglang/srt/layers/attention/triton_ops/extend_attention.py`:81; signals: attention, hang, triton; excerpt: "My original patch winded through to the existing 100k smem path to do this and I found it confusing to follow. Personally I think ..." (https://github.com/sgl-project/sglang/pull/14311#discussion_r2582464481)
- `2026-01-14T16:41:56Z` `issue` by `heiderich`; signals: fp4, nvfp4; excerpt: "With [sglang/nightly-dev-cu13-20260114-b8806071]( I experienced the same error for the model [tngtech/TNG-R1T-Chimera-NVFP4]( on 8 x RTX Pro 6000 with higher concurrency. This PR fixes this ..." (https://github.com/sgl-project/sglang/pull/14311#issuecomment-3750470668)
- `2026-01-23T20:55:25Z` `issue` by `koush`; signals: failing, sm120; excerpt: "This patch also fixes glm 4.7 flash failing to load on sm120. @Fridge003 @ispobock" (https://github.com/sgl-project/sglang/pull/14311#issuecomment-3792392875)
