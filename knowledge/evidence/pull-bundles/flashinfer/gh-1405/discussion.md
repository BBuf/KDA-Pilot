# PR Discussion Digest

- Source PR: [flashinfer-ai/flashinfer#1405](https://github.com/flashinfer-ai/flashinfer/pull/1405)
- Source page: `sources/prs/flashinfer/PR-1405.md`
- Evidence bundle: `evidence/pull-bundles/flashinfer/gh-1405`
- Generated at: `2026-05-20T15:22:35.427659+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-08-07T00:00:29Z`
- Merged: `2025-08-07T03:18:37Z`

## Discussion Counts

- Issue comments: 2
- Review submissions: 7 (approved=1, commented=6)
- Inline review comments: 7
- Review threads observed: 4
- Resolved/outdated thread markers: resolved=3, outdated=2
- Human participants with discussion text: Anerudhan, dhiraj113, ttyio, yzh119
- Automation comments/reviews omitted from high-signal summary: 5
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-08-07T00:00:48Z` `COMMENTED` by `gemini-code-assist` - Summary of Changes Hello @ttyio, I'm Gemini Code Assist[^1]! I'm currently reviewing this pull request and will post ... (https://github.com/flashinfer-ai/flashinfer/pull/1405#pullrequestreview-3094663619)
- `2025-08-07T00:02:36Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request introduces a check for cuBLAS FP4 GEMM availability in cuDNN based on its ... (https://github.com/flashinfer-ai/flashinfer/pull/1405#pullrequestreview-3094665622)
- `2025-08-07T00:07:32Z` `COMMENTED` by `yzh119` (https://github.com/flashinfer-ai/flashinfer/pull/1405#pullrequestreview-3094674571)
- `2025-08-07T00:09:50Z` `COMMENTED` by `ttyio` (https://github.com/flashinfer-ai/flashinfer/pull/1405#pullrequestreview-3094677210)
- `2025-08-07T00:28:03Z` `COMMENTED` by `yzh119` (https://github.com/flashinfer-ai/flashinfer/pull/1405#pullrequestreview-3094699817)
- `2025-08-07T00:33:39Z` `COMMENTED` by `yzh119` (https://github.com/flashinfer-ai/flashinfer/pull/1405#pullrequestreview-3094706206)
- `2025-08-07T00:33:51Z` `APPROVED` by `yzh119` - LGTM (https://github.com/flashinfer-ai/flashinfer/pull/1405#pullrequestreview-3094706402)

## Inline Comment Hotspots

- `flashinfer/gemm.py`: 7 inline comment(s)

## High-Signal Discussion

- `2025-08-07T00:33:39Z` `inline` by `yzh119` `flashinfer/gemm.py`:975; signals: flashinfer, gemm, hang; excerpt: "Per offline discussion, I think I understand the changes here: 9.11.1 is a patch release that include the feature we need while 9.12 doesn't." (https://github.com/flashinfer-ai/flashinfer/pull/1405#discussion_r2258597264)
- `2025-08-07T00:07:32Z` `inline` by `yzh119` `flashinfer/gemm.py`:975; signals: flashinfer, gemm; excerpt: "Can we add a function such as cudnn version greater equal and return True when it's greater than 9.11.1?" (https://github.com/flashinfer-ai/flashinfer/pull/1405#discussion_r2258572732)
- `2025-08-07T00:09:50Z` `inline` by `ttyio` `flashinfer/gemm.py`:975; signals: flashinfer, gemm; excerpt: "Do you mean 2 functions, cudnn great equal(9.13) and cudnn equal(9.11.1) ? Thanks!" (https://github.com/flashinfer-ai/flashinfer/pull/1405#discussion_r2258574610)
- `2025-08-07T00:28:03Z` `inline` by `yzh119` `flashinfer/gemm.py`:975; signals: flashinfer, gemm; excerpt: "I may miss some context here, but why doesn't cudnn version greater equal(91101) works?" (https://github.com/flashinfer-ai/flashinfer/pull/1405#discussion_r2258592331)
- `2025-08-07T00:04:03Z` `issue` by `Anerudhan`; signals: hang; excerpt: "The change looks good from cuDNN pov" (https://github.com/flashinfer-ai/flashinfer/pull/1405#issuecomment-3161973444)
