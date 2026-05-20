# PR Discussion Digest

- Source PR: [flashinfer-ai/flashinfer#2956](https://github.com/flashinfer-ai/flashinfer/pull/2956)
- Source page: `sources/prs/flashinfer/PR-2956.md`
- Evidence bundle: `evidence/pull-bundles/flashinfer/gh-2956`
- Generated at: `2026-05-20T15:25:59.998035+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-04-02T09:30:07Z`
- Merged: `2026-04-03T23:00:26Z`

## Discussion Counts

- Issue comments: 10
- Review submissions: 4 (approved=2, commented=2)
- Inline review comments: 3
- Review threads observed: 3
- Resolved/outdated thread markers: resolved=3, outdated=2
- Human participants with discussion text: PerkzZheng, bkryu, coderabbitai, yzh119
- Automation comments/reviews omitted from high-signal summary: 9
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-04-02T09:33:00Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request updates artifact paths and introduces TMA box widening logic for K/V and Scale ... (https://github.com/flashinfer-ai/flashinfer/pull/2956#pullrequestreview-4049493724)
- `2026-04-02T09:39:25Z` `COMMENTED` by `coderabbitai` - Actionable comments posted: 1 🤖 Prompt for all review comments with AI agents 🪄 Autofix (Beta) Fix all ... (https://github.com/flashinfer-ai/flashinfer/pull/2956#pullrequestreview-4049526503)
- `2026-04-03T21:36:00Z` `APPROVED` by `yzh119` (https://github.com/flashinfer-ai/flashinfer/pull/2956#pullrequestreview-4057390900)
- `2026-04-03T22:36:36Z` `APPROVED` by `bkryu` - CI results look good to me. I can also confirm that locally on a B300 that test trtllm ... (https://github.com/flashinfer-ai/flashinfer/pull/2956#pullrequestreview-4057540990)

## Inline Comment Hotspots

- `include/flashinfer/trtllm/fmha/kernelParams.h`: 3 inline comment(s)

## High-Signal Discussion

- `2026-04-02T09:30:21Z` `issue` by `coderabbitai`; signals: attention, blackwell, deadlock, flashinfer, fp4, hang, kernel, layout; excerpt: "No actionable comments were generated in the recent review. 🎉 ℹ️ Recent review info ⚙️ Run configuration Configuration used : defaults Review profile : ..." (https://github.com/flashinfer-ai/flashinfer/pull/2956#issuecomment-4175927450)
- `2026-04-02T09:39:24Z` `inline` by `coderabbitai` `include/flashinfer/trtllm/fmha/kernelParams.h`:763; signals: flashinfer, fp4, kernel, tile, tma; excerpt: "⚠️ Potential issue 🔴 Critical Cap the SF reshape factor by the pre-reshape SF column count. The SF descriptor’s unreshaped dim1 is already numKeysPerTile ..." (https://github.com/flashinfer-ai/flashinfer/pull/2956#discussion_r3026993297)
- `2026-04-02T09:39:25Z` `review` `COMMENTED` by `coderabbitai`; signals: flashinfer, hang, kernel; excerpt: "Actionable comments posted: 1 🤖 Prompt for all review comments with AI agents 🪄 Autofix (Beta) Fix all unresolved CodeRabbit comments on this PR: ..." (https://github.com/flashinfer-ai/flashinfer/pull/2956#pullrequestreview-4049526503)
- `2026-04-03T22:36:36Z` `review` `APPROVED` by `bkryu`; signals: attention, hang; excerpt: "CI results look good to me. I can also confirm that locally on a B300 that test trtllm gen attention.py that used to hang ..." (https://github.com/flashinfer-ai/flashinfer/pull/2956#pullrequestreview-4057540990)
