# PR Discussion Digest

- Source PR: [flashinfer-ai/flashinfer#2739](https://github.com/flashinfer-ai/flashinfer/pull/2739)
- Source page: `sources/prs/flashinfer/PR-2739.md`
- Evidence bundle: `evidence/pull-bundles/flashinfer/gh-2739`
- Generated at: `2026-05-20T15:25:28.537661+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-03-10T04:39:08Z`
- Merged: `2026-03-30T20:26:29Z`

## Discussion Counts

- Issue comments: 8
- Review submissions: 3 (approved=1, commented=2)
- Inline review comments: 2
- Review threads observed: 1
- Resolved/outdated thread markers: resolved=1, outdated=0
- Human participants with discussion text: aleozlx, coderabbitai, johnnynunez, wzhao18
- Automation comments/reviews omitted from high-signal summary: 5
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-03-10T04:41:00Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request correctly implements in-place updates for trtllm fp8 block scale routed moe by handling ... (https://github.com/flashinfer-ai/flashinfer/pull/2739#pullrequestreview-3919694499)
- `2026-03-19T03:22:47Z` `COMMENTED` by `wzhao18` (https://github.com/flashinfer-ai/flashinfer/pull/2739#pullrequestreview-3972563217)
- `2026-03-19T20:33:48Z` `APPROVED` by `aleozlx` - lgtm (https://github.com/flashinfer-ai/flashinfer/pull/2739#pullrequestreview-3977824280)

## Inline Comment Hotspots

- `flashinfer/fused_moe/core.py`: 2 inline comment(s)

## High-Signal Discussion

- `2026-03-10T04:39:27Z` `issue` by `coderabbitai`; signals: bf16, block, dtype, flashinfer, fp8, hang, memory, moe; excerpt: "📝 Walkthrough Walkthrough Updated trtllm fp8 block scale moe op to accept an optional output tensor and use it in-place after validating shape/dtype/device; when ..." (https://github.com/flashinfer-ai/flashinfer/pull/2739#issuecomment-4028617488)
- `2026-03-19T03:22:47Z` `inline` by `wzhao18` `flashinfer/fused_moe/core.py`:1695; signals: flashinfer, moe; excerpt: "done." (https://github.com/flashinfer-ai/flashinfer/pull/2739#discussion_r2957604247)
