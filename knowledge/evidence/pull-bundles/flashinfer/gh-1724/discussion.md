# PR Discussion Digest

- Source PR: [flashinfer-ai/flashinfer#1724](https://github.com/flashinfer-ai/flashinfer/pull/1724)
- Source page: `sources/prs/flashinfer/PR-1724.md`
- Evidence bundle: `evidence/pull-bundles/flashinfer/gh-1724`
- Generated at: `2026-05-20T15:23:19.819864+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-09-19T02:51:32Z`
- Merged: `2025-09-24T18:39:25Z`

## Discussion Counts

- Issue comments: 4
- Review submissions: 2 (approved=1, commented=1)
- Inline review comments: 2
- Review threads observed: 2
- Resolved/outdated thread markers: resolved=0, outdated=0
- Human participants with discussion text: GordonGustafson, yzh119, zhyncs
- Automation comments/reviews omitted from high-signal summary: 4
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 1

## Review Decisions

- `2025-09-19T02:53:45Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request refactors the fused MoE routing kernels to remove the NumExperts template parameter, making ... (https://github.com/flashinfer-ai/flashinfer/pull/1724#pullrequestreview-3242670227)
- `2025-09-24T18:39:19Z` `APPROVED` by `yzh119` - LGTM. cc @zhyncs @GordonGustafson this PR might bring some regression for smaller number of experts, will fix in ... (https://github.com/flashinfer-ai/flashinfer/pull/1724#pullrequestreview-3264210337)

## Inline Comment Hotspots

- `csrc/trtllm_fused_moe_routing_deepseek.cu`: 2 inline comment(s)

## High-Signal Discussion

- `2025-09-19T03:21:04Z` `issue` by `yzh119`; signals: compile; excerpt: "cc @GordonGustafson for viz The compile-time NumThreads was only used in launch bounds which is optional and can we removed." (https://github.com/flashinfer-ai/flashinfer/pull/1724#issuecomment-3310379806)
- `2025-09-24T18:39:19Z` `review` `APPROVED` by `yzh119`; signals: regression; excerpt: "LGTM. cc @zhyncs @GordonGustafson this PR might bring some regression for smaller number of experts, will fix in later PRs." (https://github.com/flashinfer-ai/flashinfer/pull/1724#pullrequestreview-3264210337)
