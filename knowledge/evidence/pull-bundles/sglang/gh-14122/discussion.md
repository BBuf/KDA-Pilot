# PR Discussion Digest

- Source PR: [sgl-project/sglang#14122](https://github.com/sgl-project/sglang/pull/14122)
- Source page: `sources/prs/sglang/PR-14122.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-14122`
- Generated at: `2026-05-20T15:27:57.038880+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-11-29T06:05:22Z`
- Merged: `2025-12-01T15:07:54Z`

## Discussion Counts

- Issue comments: 7
- Review submissions: 2 (approved=1, commented=1)
- Inline review comments: 3
- Review threads observed: 3
- Resolved/outdated thread markers: resolved=3, outdated=0
- Human participants with discussion text: BBuf, ispobock, yiakwy-xpu-ml-framework-team
- Automation comments/reviews omitted from high-signal summary: 5
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 1

## Review Decisions

- `2025-11-29T06:09:28Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request introduces a new moe wna16 marlin gemm kernel and refactors related code. The ... (https://github.com/sgl-project/sglang/pull/14122#pullrequestreview-3520498865)
- `2025-12-01T15:05:32Z` `APPROVED` by `ispobock` (https://github.com/sgl-project/sglang/pull/14122#pullrequestreview-3525482910)

## Inline Comment Hotspots

- `sgl-kernel/csrc/gemm/marlin/dequant.h`: 2 inline comment(s)
- `sgl-kernel/csrc/moe/marlin_moe_wna16/ops.cu`: 1 inline comment(s)

## High-Signal Discussion

- `2025-11-29T07:10:54Z` `issue` by `ispobock`; signals: kernel; excerpt: "I built a temp image ispobock/sglang:v0.5.5.post3-cu129-amd64-ima-fix-v5 to include this new marlin kernel. The IMA issue seems cannot be reproduced in this image on my ..." (https://github.com/sgl-project/sglang/pull/14122#issuecomment-3591070639)
