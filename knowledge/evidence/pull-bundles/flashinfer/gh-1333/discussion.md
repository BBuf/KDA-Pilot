# PR Discussion Digest

- Source PR: [flashinfer-ai/flashinfer#1333](https://github.com/flashinfer-ai/flashinfer/pull/1333)
- Source page: `sources/prs/flashinfer/PR-1333.md`
- Evidence bundle: `evidence/pull-bundles/flashinfer/gh-1333`
- Generated at: `2026-05-20T15:22:20.895628+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-07-25T18:19:54Z`
- Merged: `2025-07-25T19:09:15Z`

## Discussion Counts

- Issue comments: 0
- Review submissions: 8 (approved=1, commented=7)
- Inline review comments: 6
- Review threads observed: 2
- Resolved/outdated thread markers: resolved=1, outdated=1
- Human participants with discussion text: ttyio, yzh119
- Automation comments/reviews omitted from high-signal summary: 3
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-07-25T18:20:10Z` `COMMENTED` by `gemini-code-assist` - Summary of Changes Hello @ttyio, I'm Gemini Code Assist[^1]! I'm currently reviewing this pull request and will post ... (https://github.com/flashinfer-ai/flashinfer/pull/1333#pullrequestreview-3056415699)
- `2025-07-25T18:20:40Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request adds a necessary check for the torch.float4 e2m1fn x2 data type, which is ... (https://github.com/flashinfer-ai/flashinfer/pull/1333#pullrequestreview-3056417164)
- `2025-07-25T18:40:28Z` `COMMENTED` by `yzh119` (https://github.com/flashinfer-ai/flashinfer/pull/1333#pullrequestreview-3056460801)
- `2025-07-25T18:44:15Z` `COMMENTED` by `ttyio` (https://github.com/flashinfer-ai/flashinfer/pull/1333#pullrequestreview-3056468526)
- `2025-07-25T18:45:42Z` `COMMENTED` by `yzh119` (https://github.com/flashinfer-ai/flashinfer/pull/1333#pullrequestreview-3056471258)
- `2025-07-25T18:45:58Z` `COMMENTED` by `ttyio` (https://github.com/flashinfer-ai/flashinfer/pull/1333#pullrequestreview-3056471742)
- `2025-07-25T18:46:55Z` `COMMENTED` by `ttyio` (https://github.com/flashinfer-ai/flashinfer/pull/1333#pullrequestreview-3056474859)
- `2025-07-25T19:09:04Z` `APPROVED` by `yzh119` - LGTM, thanks for the hotfix! (https://github.com/flashinfer-ai/flashinfer/pull/1333#pullrequestreview-3056530236)

## Inline Comment Hotspots

- `flashinfer/gemm.py`: 6 inline comment(s)

## High-Signal Discussion

- `2025-07-25T18:46:55Z` `inline` by `ttyio` `flashinfer/gemm.py`:779; signals: flashinfer, fp4, gemm; excerpt: "I see, so this check is designed specifically only for cudnn backend of fp4 gemm? Yes, this check is added inside check cudnn fp4 ..." (https://github.com/flashinfer-ai/flashinfer/pull/1333#discussion_r2231798169)
- `2025-07-25T18:45:42Z` `inline` by `yzh119` `flashinfer/gemm.py`:779; signals: flashinfer, fp4, gemm; excerpt: "I see, so this check is designed specifically only for cudnn backend of fp4 gemm?" (https://github.com/flashinfer-ai/flashinfer/pull/1333#discussion_r2231795890)
- `2025-07-25T18:40:28Z` `inline` by `yzh119` `flashinfer/gemm.py`:779; signals: flashinfer, gemm; excerpt: "Per our discussion we can fallback to uint8/int8 as container for torch 2.7.1 right? Why is it a hard constraint here?" (https://github.com/flashinfer-ai/flashinfer/pull/1333#discussion_r2231788211)
- `2025-07-25T18:44:15Z` `inline` by `ttyio` `flashinfer/gemm.py`:779; signals: flashinfer, gemm; excerpt: "We hit issue that in torch 2.7, even upgrade cudnn to latest version, we still cannot generate engine from cudnn api. from @Anerudhan's comment: ..." (https://github.com/flashinfer-ai/flashinfer/pull/1333#discussion_r2231793915)
- `2025-07-25T18:45:58Z` `inline` by `ttyio` `flashinfer/gemm.py`:779; signals: flashinfer, gemm; excerpt: "BTW, we tested: - cudnn 9.11 + torch 2.7 not works - cudnn 9.11 + torch 2.8 works" (https://github.com/flashinfer-ai/flashinfer/pull/1333#discussion_r2231796238)
