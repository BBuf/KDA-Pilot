# PR Discussion Digest

- Source PR: [flashinfer-ai/flashinfer#2217](https://github.com/flashinfer-ai/flashinfer/pull/2217)
- Source page: `sources/prs/flashinfer/PR-2217.md`
- Evidence bundle: `evidence/pull-bundles/flashinfer/gh-2217`
- Generated at: `2026-05-20T15:24:22.957995+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-12-14T13:08:22Z`
- Merged: `2025-12-16T21:08:09Z`

## Discussion Counts

- Issue comments: 7
- Review submissions: 7 (approved=1, commented=6)
- Inline review comments: 5
- Review threads observed: 3
- Resolved/outdated thread markers: resolved=1, outdated=0
- Human participants with discussion text: coderabbitai, elvischenv, yzh119
- Automation comments/reviews omitted from high-signal summary: 6
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-12-14T13:09:56Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request introduces support for unpadded output hidden sizes in trtllm fp4 block scale moe, ... (https://github.com/flashinfer-ai/flashinfer/pull/2217#pullrequestreview-3575216608)
- `2025-12-14T13:11:55Z` `COMMENTED` by `coderabbitai` - Actionable comments posted: 0 🧹 Nitpick comments (1) flashinfer/fused moe/core.py (1) 1756-1765: Consider additional validation for edge cases. ... (https://github.com/flashinfer-ai/flashinfer/pull/2217#pullrequestreview-3575223592)
- `2025-12-15T05:05:39Z` `COMMENTED` by `yzh119` (https://github.com/flashinfer-ai/flashinfer/pull/2217#pullrequestreview-3576380130)
- `2025-12-15T07:36:35Z` `COMMENTED` by `elvischenv` (https://github.com/flashinfer-ai/flashinfer/pull/2217#pullrequestreview-3576827613)
- `2025-12-15T07:38:59Z` `COMMENTED` by `elvischenv` (https://github.com/flashinfer-ai/flashinfer/pull/2217#pullrequestreview-3576837237)
- `2025-12-16T05:08:41Z` `COMMENTED` by `yzh119` (https://github.com/flashinfer-ai/flashinfer/pull/2217#pullrequestreview-3581335896)
- `2025-12-16T21:08:01Z` `APPROVED` by `yzh119` - Failed UT are not relevant and let's merge this first. (https://github.com/flashinfer-ai/flashinfer/pull/2217#pullrequestreview-3584947041)

## Inline Comment Hotspots

- `flashinfer/fused_moe/core.py`: 5 inline comment(s)

## High-Signal Discussion

- `2025-12-14T13:08:33Z` `issue` by `coderabbitai`; signals: aligned, block, cuda, dtype, flashinfer, fp4, hang, kernel; excerpt: "Walkthrough The changes modify the FP4 block-scale MoE kernel and Python wrapper to derive output dimensions directly from the actual output tensor shape rather ..." (https://github.com/flashinfer-ai/flashinfer/pull/2217#issuecomment-3650960006)
- `2025-12-14T13:11:55Z` `review` `COMMENTED` by `coderabbitai`; signals: dtype, flashinfer, hang, kernel, moe, overflow; excerpt: "Actionable comments posted: 0 🧹 Nitpick comments (1) flashinfer/fused moe/core.py (1) 1756-1765: Consider additional validation for edge cases. The validation logic correctly ensures the ..." (https://github.com/flashinfer-ai/flashinfer/pull/2217#pullrequestreview-3575223592)
- `2025-12-15T07:36:35Z` `inline` by `elvischenv` `flashinfer/fused_moe/core.py`:1912; signals: flashinfer, kernel, moe; excerpt: "I don't think so. hidden states.shape[1] is already padded, the input should be padded before the MoE kernel. Before this PR, the API does ..." (https://github.com/flashinfer-ai/flashinfer/pull/2217#discussion_r2618308129)
- `2025-12-15T05:05:39Z` `inline` by `yzh119` `flashinfer/fused_moe/core.py`:1912; signals: flashinfer, moe; excerpt: "Hi @elvischenv just want to make sure my understanding is right, does this mean hidden states.shape[1] is the effective hidden dimension where output.shape[1] could ..." (https://github.com/flashinfer-ai/flashinfer/pull/2217#discussion_r2617954069)
- `2025-12-15T07:38:54Z` `inline` by `elvischenv` `flashinfer/fused_moe/core.py`:1765; signals: flashinfer, moe; excerpt: "We do this assertion since the output could be unpadded so that smaller than the (padded) hidden size." (https://github.com/flashinfer-ai/flashinfer/pull/2217#discussion_r2618315144)
- `2025-12-16T05:08:41Z` `inline` by `yzh119` `flashinfer/fused_moe/core.py`:1912; signals: flashinfer, moe; excerpt: "Thank you for the explanation!" (https://github.com/flashinfer-ai/flashinfer/pull/2217#discussion_r2621805088)
