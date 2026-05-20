# PR Discussion Digest

- Source PR: [flashinfer-ai/flashinfer#1390](https://github.com/flashinfer-ai/flashinfer/pull/1390)
- Source page: `sources/prs/flashinfer/PR-1390.md`
- Evidence bundle: `evidence/pull-bundles/flashinfer/gh-1390`
- Generated at: `2026-05-20T15:22:33.379901+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-08-05T16:09:08Z`
- Merged: `2025-08-07T00:29:19Z`

## Discussion Counts

- Issue comments: 0
- Review submissions: 10 (approved=1, commented=9)
- Inline review comments: 11
- Review threads observed: 5
- Resolved/outdated thread markers: resolved=4, outdated=3
- Human participants with discussion text: bkryu, yzh119
- Automation comments/reviews omitted from high-signal summary: 6
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-08-05T16:09:44Z` `COMMENTED` by `gemini-code-assist` - Summary of Changes Hello @bkryu, I'm Gemini Code Assist[^1]! I'm currently reviewing this pull request and will post ... (https://github.com/flashinfer-ai/flashinfer/pull/1390#pullrequestreview-3088858203)
- `2025-08-05T16:11:59Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request adds new FP8 benchmarks for attention and matrix multiplication routines. The changes are ... (https://github.com/flashinfer-ai/flashinfer/pull/1390#pullrequestreview-3088865519)
- `2025-08-05T22:14:54Z` `COMMENTED` by `bkryu` (https://github.com/flashinfer-ai/flashinfer/pull/1390#pullrequestreview-3089866596)
- `2025-08-05T22:14:58Z` `COMMENTED` by `bkryu` (https://github.com/flashinfer-ai/flashinfer/pull/1390#pullrequestreview-3089866694)
- `2025-08-05T22:15:20Z` `COMMENTED` by `bkryu` (https://github.com/flashinfer-ai/flashinfer/pull/1390#pullrequestreview-3089867371)
- `2025-08-05T22:15:26Z` `COMMENTED` by `bkryu` (https://github.com/flashinfer-ai/flashinfer/pull/1390#pullrequestreview-3089867519)
- `2025-08-06T22:10:50Z` `COMMENTED` by `yzh119` (https://github.com/flashinfer-ai/flashinfer/pull/1390#pullrequestreview-3094471624)
- `2025-08-06T22:22:19Z` `COMMENTED` by `bkryu` (https://github.com/flashinfer-ai/flashinfer/pull/1390#pullrequestreview-3094492402)
- `2025-08-06T22:51:29Z` `COMMENTED` by `yzh119` (https://github.com/flashinfer-ai/flashinfer/pull/1390#pullrequestreview-3094534748)
- `2025-08-06T22:51:42Z` `APPROVED` by `yzh119` - LGTM, thank you @bkryu ! (https://github.com/flashinfer-ai/flashinfer/pull/1390#pullrequestreview-3094535000)

## Inline Comment Hotspots

- `benchmarks/routines/attention.py`: 7 inline comment(s)
- `benchmarks/routines/gemm.py`: 4 inline comment(s)

## High-Signal Discussion

- `2025-08-05T22:15:20Z` `inline` by `bkryu` `benchmarks/routines/attention.py`:1417; signals: attention, benchmark, mla; excerpt: "MLA requires separate testing. will not adress" (https://github.com/flashinfer-ai/flashinfer/pull/1390#discussion_r2255450963)
- `2025-08-05T22:14:54Z` `inline` by `bkryu` `benchmarks/routines/gemm.py`:290; signals: benchmark, gemm; excerpt: "Addressed in updated commit." (https://github.com/flashinfer-ai/flashinfer/pull/1390#discussion_r2255450445)
- `2025-08-05T22:14:58Z` `inline` by `bkryu` `benchmarks/routines/gemm.py`:574; signals: benchmark, gemm; excerpt: "Addressed in updated commit." (https://github.com/flashinfer-ai/flashinfer/pull/1390#discussion_r2255450516)
- `2025-08-05T22:15:26Z` `inline` by `bkryu` `benchmarks/routines/attention.py`:251; signals: attention, benchmark; excerpt: "Addressed in updated commit." (https://github.com/flashinfer-ai/flashinfer/pull/1390#discussion_r2255451078)
- `2025-08-06T22:10:29Z` `inline` by `yzh119` `benchmarks/routines/attention.py`:1600; signals: attention, benchmark; excerpt: "Is it because we directly call the trtllm gen decode functions instead of going through the wrapper?" (https://github.com/flashinfer-ai/flashinfer/pull/1390#discussion_r2258423244)
- `2025-08-06T22:22:19Z` `inline` by `bkryu` `benchmarks/routines/attention.py`:1600; signals: attention, benchmark; excerpt: "Yes. As stated in the . trtllm-gen directly needs to go to through" (https://github.com/flashinfer-ai/flashinfer/pull/1390#discussion_r2258437742)
- `2025-08-06T22:51:29Z` `inline` by `yzh119` `benchmarks/routines/attention.py`:1600; signals: attention, benchmark; excerpt: "no problem, thanks for the explaination!" (https://github.com/flashinfer-ai/flashinfer/pull/1390#discussion_r2258471862)
