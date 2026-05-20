# PR Discussion Digest

- Source PR: [tile-ai/tilelang#2052](https://github.com/tile-ai/tilelang/pull/2052)
- Source page: `sources/prs/tilelang/PR-2052.md`
- Evidence bundle: `evidence/pull-bundles/tilelang/gh-2052`
- Generated at: `2026-05-20T15:32:53.780643+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-04-16T10:46:39Z`
- Merged: `2026-04-18T14:38:11Z`

## Discussion Counts

- Issue comments: 7
- Review submissions: 1 (commented=1)
- Inline review comments: 0
- Review threads observed: 0
- Resolved/outdated thread markers: resolved=0, outdated=0
- Human participants with discussion text: LeiWang1999, coderabbitai, copilot-pull-request-reviewer
- Automation comments/reviews omitted from high-signal summary: 2
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-04-17T05:51:06Z` `COMMENTED` by `copilot-pull-request-reviewer` - Pull request overview This PR fixes a CUDA driver memory blow-up on SM120 (e.g., RTX 5090) by changing ... (https://github.com/tile-ai/tilelang/pull/2052#pullrequestreview-4126423807)

## Inline Comment Hotspots

- No inline review comments were returned by GitHub.

## High-Signal Discussion

- `2026-04-17T05:51:06Z` `review` `COMMENTED` by `copilot-pull-request-reviewer`; signals: cuda, hang, memory, ptx, shared memory, sm120, sm90, tma; excerpt: "Pull request overview This PR fixes a CUDA driver memory blow-up on SM120 (e.g., RTX 5090) by changing unicast cp.async.bulk / TMA load PTX ..." (https://github.com/tile-ai/tilelang/pull/2052#pullrequestreview-4126423807)
- `2026-04-16T10:46:53Z` `issue` by `coderabbitai`; signals: cuda, hang, memory, ptx, register, sm120, sm90, tma; excerpt: "No actionable comments were generated in the recent review. 🎉 ℹ️ Recent review info ⚙️ Run configuration Configuration used : defaults Review profile : ..." (https://github.com/tile-ai/tilelang/pull/2052#issuecomment-4259406481)
- `2026-04-17T05:59:00Z` `issue` by `LeiWang1999`; signals: cuda, kernel; excerpt: "@qqq-tao Thanks for your contributions. However, it appears that this bug originates from the CUDA toolkit itself rather than from our program. shared::cluster is ..." (https://github.com/tile-ai/tilelang/pull/2052#issuecomment-4265788768)
- `2026-04-17T05:47:17Z` `issue` by `LeiWang1999`; signals: perf, regression; excerpt: "@regression-perf" (https://github.com/tile-ai/tilelang/pull/2052#issuecomment-4265743466)
- `2026-04-17T10:24:48Z` `issue` by `LeiWang1999`; signals: perf, regression; excerpt: "@regression-perf" (https://github.com/tile-ai/tilelang/pull/2052#issuecomment-4267208764)
