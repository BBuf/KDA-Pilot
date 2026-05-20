# PR Discussion Digest

- Source PR: [flashinfer-ai/flashinfer#2128](https://github.com/flashinfer-ai/flashinfer/pull/2128)
- Source page: `sources/prs/flashinfer/PR-2128.md`
- Evidence bundle: `evidence/pull-bundles/flashinfer/gh-2128`
- Generated at: `2026-05-20T15:24:11.581026+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-11-21T11:36:32Z`
- Merged: `2025-11-22T16:37:16Z`

## Discussion Counts

- Issue comments: 5
- Review submissions: 3 (approved=1, commented=2)
- Inline review comments: 2
- Review threads observed: 1
- Resolved/outdated thread markers: resolved=0, outdated=0
- Human participants with discussion text: coderabbitai, yzh119
- Automation comments/reviews omitted from high-signal summary: 5
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-11-21T11:39:07Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request fixes a critical bug where register arrays in the activationDeepSeekKernel were used without ... (https://github.com/flashinfer-ai/flashinfer/pull/2128#pullrequestreview-3492384861)
- `2025-11-21T19:46:21Z` `COMMENTED` by `yzh119` (https://github.com/flashinfer-ai/flashinfer/pull/2128#pullrequestreview-3494146301)
- `2025-11-22T07:26:35Z` `APPROVED` by `yzh119` (https://github.com/flashinfer-ai/flashinfer/pull/2128#pullrequestreview-3495996356)

## Inline Comment Hotspots

- `csrc/trtllm_fused_moe_dev_kernel.cu`: 2 inline comment(s)

## High-Signal Discussion

- `2025-11-21T11:36:46Z` `issue` by `coderabbitai`; signals: attention, block, correctness, cuda, hang, kernel, layout, moe; excerpt: "Walkthrough Modified the DeepSeek activation kernel in TensorRT-LLM's fused MOE implementation by extracting a constant for thread configuration and adding per-token state initialization loops ..." (https://github.com/flashinfer-ai/flashinfer/pull/2128#issuecomment-3562641838)
- `2025-11-21T19:46:20Z` `inline` by `yzh119` `csrc/trtllm_fused_moe_dev_kernel.cu`:248; signals: kernel, moe; excerpt: "@nekorobov do you think gemini's suggestion is reasonable?" (https://github.com/flashinfer-ai/flashinfer/pull/2128#discussion_r2550796170)
