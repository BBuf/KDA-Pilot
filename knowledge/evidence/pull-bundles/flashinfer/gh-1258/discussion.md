# PR Discussion Digest

- Source PR: [flashinfer-ai/flashinfer#1258](https://github.com/flashinfer-ai/flashinfer/pull/1258)
- Source page: `sources/prs/flashinfer/PR-1258.md`
- Evidence bundle: `evidence/pull-bundles/flashinfer/gh-1258`
- Generated at: `2026-05-20T15:22:02.582213+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-07-15T07:57:12Z`
- Merged: `2025-07-16T10:58:21Z`

## Discussion Counts

- Issue comments: 8
- Review submissions: 3 (approved=1, commented=2)
- Inline review comments: 0
- Review threads observed: 0
- Resolved/outdated thread markers: resolved=0, outdated=0
- Human participants with discussion text: nvpohanh, weireweire, yyihuang, yzh119
- Automation comments/reviews omitted from high-signal summary: 2
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 5

## Review Decisions

- `2025-07-15T07:57:46Z` `COMMENTED` by `gemini-code-assist` - Summary of Changes Hello @yyihuang, I'm Gemini Code Assist[^1]! I'm currently reviewing this pull request and will post ... (https://github.com/flashinfer-ai/flashinfer/pull/1258#pullrequestreview-3019177972)
- `2025-07-15T07:59:24Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request enables Multi-Token Parallelism (MTP) for trtllm-gen mla by updating the query tensor to ... (https://github.com/flashinfer-ai/flashinfer/pull/1258#pullrequestreview-3019184741)
- `2025-07-16T10:58:14Z` `APPROVED` by `yzh119` - LGTM, for the next step let's use the new artifacts with shared k/v layout (https://github.com/flashinfer-ai/flashinfer/pull/1258#pullrequestreview-3024301610)

## Inline Comment Hotspots

- No inline review comments were returned by GitHub.

## High-Signal Discussion

- `2025-07-16T06:11:14Z` `issue` by `weireweire`; signals: cache, kernel, tma; excerpt: "I assume "dynamic scale" here means make scale on device. I see you use runner params.scaleSoftmaxLog2 = bmm1 scale M LOG2E; this prevent us ..." (https://github.com/flashinfer-ai/flashinfer/pull/1258#issuecomment-3077006664)
- `2025-07-16T10:36:47Z` `issue` by `yzh119`; signals: attention, tma; excerpt: "I see you use runner params.scaleSoftmaxLog2 = bmm1 scale M LOG2E; this prevent us use "dynamic scale" right? Yes, I would encourage the complete ..." (https://github.com/flashinfer-ai/flashinfer/pull/1258#issuecomment-3077973461)
- `2025-07-16T06:16:32Z` `issue` by `yyihuang`; signals: cuda; excerpt: "Some other customers request for dynamic scale factors since the factors are updated dynamically even for the same model +bs, otherwise they would fail ..." (https://github.com/flashinfer-ai/flashinfer/pull/1258#issuecomment-3077027315)
- `2025-07-16T10:58:14Z` `review` `APPROVED` by `yzh119`; signals: layout; excerpt: "LGTM, for the next step let's use the new artifacts with shared k/v layout" (https://github.com/flashinfer-ai/flashinfer/pull/1258#pullrequestreview-3024301610)
