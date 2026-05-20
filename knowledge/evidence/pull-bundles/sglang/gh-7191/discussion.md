# PR Discussion Digest

- Source PR: [sgl-project/sglang#7191](https://github.com/sgl-project/sglang/pull/7191)
- Source page: `sources/prs/sglang/PR-7191.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-7191`
- Generated at: `2026-05-20T15:31:07.132322+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-06-14T22:01:44Z`
- Merged: `2025-06-14T23:54:40Z`

## Discussion Counts

- Issue comments: 0
- Review submissions: 5 (approved=2, commented=3)
- Inline review comments: 2
- Review threads observed: 2
- Resolved/outdated thread markers: resolved=2, outdated=0
- Human participants with discussion text: fzyzcjy, zhyncs
- Automation comments/reviews omitted from high-signal summary: 3
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-06-14T22:02:03Z` `COMMENTED` by `gemini-code-assist` - Summary of Changes Hello @zhijian-liu, I'm Gemini Code Assist[^1]! I'm currently reviewing this pull request and will post ... (https://github.com/sgl-project/sglang/pull/7191#pullrequestreview-2928885310)
- `2025-06-14T22:03:25Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request correctly addresses a bug related to DeepGEMM upgrades by conditionally passing the recipe ... (https://github.com/sgl-project/sglang/pull/7191#pullrequestreview-2928885832)
- `2025-06-14T22:37:27Z` `APPROVED` by `zhyncs` (https://github.com/sgl-project/sglang/pull/7191#pullrequestreview-2928897398)
- `2025-06-14T22:56:41Z` `APPROVED` by `fzyzcjy` (https://github.com/sgl-project/sglang/pull/7191#pullrequestreview-2928900383)
- `2025-06-14T23:06:49Z` `COMMENTED` by `fzyzcjy` (https://github.com/sgl-project/sglang/pull/7191#pullrequestreview-2928902138)

## Inline Comment Hotspots

- `python/sglang/srt/layers/quantization/deep_gemm_wrapper/entrypoint.py`: 2 inline comment(s)

## High-Signal Discussion

- `2025-06-14T23:06:49Z` `inline` by `fzyzcjy` `python/sglang/srt/layers/quantization/deep_gemm_wrapper/entrypoint.py`:56; signals: gemm; excerpt: "nit: if not V202506, we may need to assert recipe is None (o/w user pass in recipe and we throw away)" (https://github.com/sgl-project/sglang/pull/7191#discussion_r2147372215)
