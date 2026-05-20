# PR Discussion Digest

- Source PR: [flashinfer-ai/flashinfer#2916](https://github.com/flashinfer-ai/flashinfer/pull/2916)
- Source page: `sources/prs/flashinfer/PR-2916.md`
- Evidence bundle: `evidence/pull-bundles/flashinfer/gh-2916`
- Generated at: `2026-05-20T15:25:53.837847+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-03-30T21:32:48Z`
- Merged: `2026-04-01T13:40:23Z`

## Discussion Counts

- Issue comments: 8
- Review submissions: 2 (approved=1, commented=1)
- Inline review comments: 0
- Review threads observed: 0
- Resolved/outdated thread markers: resolved=0, outdated=0
- Human participants with discussion text: aleozlx, bkryu, coderabbitai, nvpohanh
- Automation comments/reviews omitted from high-signal summary: 5
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-03-30T21:34:30Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request fixes a crash in the autotuner for FP4 routed MoE by ensuring that ... (https://github.com/flashinfer-ai/flashinfer/pull/2916#pullrequestreview-4033422137)
- `2026-03-30T22:12:30Z` `APPROVED` by `aleozlx` (https://github.com/flashinfer-ai/flashinfer/pull/2916#pullrequestreview-4033574130)

## Inline Comment Hotspots

- No inline review comments were returned by GitHub.

## High-Signal Discussion

- `2026-03-30T21:33:04Z` `issue` by `coderabbitai`; signals: autotune, block, flashinfer, fp4, fp8, hang, kernel, moe; excerpt: "📝 Walkthrough Walkthrough Added support for a skip routing flag in MoERunner to bypass routing computation. Updated TensorRT-LLM FP4 block-scale MoE operator to allocate ..." (https://github.com/flashinfer-ai/flashinfer/pull/2916#issuecomment-4158317904)
- `2026-03-31T01:38:27Z` `issue` by `nvpohanh`; signals: moe; excerpt: "cc @trevor-m who is working on integrating routed moe into SGL" (https://github.com/flashinfer-ai/flashinfer/pull/2916#issuecomment-4159221801)
