# PR Discussion Digest

- Source PR: [flashinfer-ai/flashinfer#2241](https://github.com/flashinfer-ai/flashinfer/pull/2241)
- Source page: `sources/prs/flashinfer/PR-2241.md`
- Evidence bundle: `evidence/pull-bundles/flashinfer/gh-2241`
- Generated at: `2026-05-20T15:24:25.581911+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-12-18T21:36:06Z`
- Merged: `2025-12-23T00:43:04Z`

## Discussion Counts

- Issue comments: 5
- Review submissions: 3 (approved=2, commented=1)
- Inline review comments: 3
- Review threads observed: 3
- Resolved/outdated thread markers: resolved=3, outdated=0
- Human participants with discussion text: bkryu, coderabbitai, yzh119
- Automation comments/reviews omitted from high-signal summary: 7
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-12-18T21:37:41Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request updates the minimum required cuDNN version for FP8 attention from 9.18.0 to 9.17.1. ... (https://github.com/flashinfer-ai/flashinfer/pull/2241#pullrequestreview-3595168079)
- `2025-12-18T21:51:54Z` `APPROVED` by `yzh119` - LGTM (https://github.com/flashinfer-ai/flashinfer/pull/2241#pullrequestreview-3595208252)
- `2025-12-23T00:43:03Z` `APPROVED` by `bkryu` - Unit test failures are unrelated. LGTM approved (https://github.com/flashinfer-ai/flashinfer/pull/2241#pullrequestreview-3606168425)

## Inline Comment Hotspots

- `benchmarks/routines/attention.py`: 1 inline comment(s)
- `flashinfer/cudnn/prefill.py`: 1 inline comment(s)
- `tests/attention/test_cudnn_prefill.py`: 1 inline comment(s)

## High-Signal Discussion

- `2025-12-18T21:36:17Z` `issue` by `coderabbitai`; signals: accuracy, attention, benchmark, flashinfer, fp8, hang; excerpt: "Walkthrough The PR lowers the minimum cuDNN version requirement for FP8 support from 9.18.0 (backend version 91800) to 9.17.1 (backend version 91701). Version checks ..." (https://github.com/flashinfer-ai/flashinfer/pull/2241#issuecomment-3672360216)
