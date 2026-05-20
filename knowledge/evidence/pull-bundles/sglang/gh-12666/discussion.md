# PR Discussion Digest

- Source PR: [sgl-project/sglang#12666](https://github.com/sgl-project/sglang/pull/12666)
- Source page: `sources/prs/sglang/PR-12666.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-12666`
- Generated at: `2026-05-20T15:27:41.368556+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-11-05T03:20:34Z`
- Merged: `2025-11-12T05:23:25Z`

## Discussion Counts

- Issue comments: 1
- Review submissions: 4 (approved=1, commented=3)
- Inline review comments: 5
- Review threads observed: 4
- Resolved/outdated thread markers: resolved=2, outdated=1
- Human participants with discussion text: Fridge003, HydraQYH
- Automation comments/reviews omitted from high-signal summary: 5
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-11-05T03:22:43Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request introduces support for Expert Specialization Grouped GEMM in the CUTLASS MoE kernels, controlled ... (https://github.com/sgl-project/sglang/pull/12666#pullrequestreview-3419550888)
- `2025-11-10T02:25:04Z` `COMMENTED` by `Fridge003` (https://github.com/sgl-project/sglang/pull/12666#pullrequestreview-3440595955)
- `2025-11-10T02:41:44Z` `COMMENTED` by `HydraQYH` (https://github.com/sgl-project/sglang/pull/12666#pullrequestreview-3440615090)
- `2025-11-12T01:05:38Z` `APPROVED` by `Fridge003` (https://github.com/sgl-project/sglang/pull/12666#pullrequestreview-3450777331)

## Inline Comment Hotspots

- `python/sglang/srt/layers/moe/cutlass_moe.py`: 4 inline comment(s)
- `python/sglang/test/test_cutlass_moe.py`: 1 inline comment(s)

## High-Signal Discussion

- `2025-11-10T02:41:44Z` `inline` by `HydraQYH` `python/sglang/srt/layers/moe/cutlass_moe.py`:127; signals: cutlass, kernel, moe; excerpt: "There are still two optimizations that haven't been implemented: 1. Based on arithmetic intensity combined with MNK, a suitable kernel is dynamically selected to ..." (https://github.com/sgl-project/sglang/pull/12666#discussion_r2508557889)
- `2025-11-10T02:25:02Z` `inline` by `Fridge003` `python/sglang/srt/layers/moe/cutlass_moe.py`:127; signals: cutlass, moe; excerpt: "How can user pass enable es to cutlass moe? Do we need an environment variable?" (https://github.com/sgl-project/sglang/pull/12666#discussion_r2508540681)
