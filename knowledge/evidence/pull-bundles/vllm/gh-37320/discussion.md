# PR Discussion Digest

- Source PR: [vllm-project/vllm#37320](https://github.com/vllm-project/vllm/pull/37320)
- Source page: `sources/prs/vllm/PR-37320.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-37320`
- Generated at: `2026-05-20T15:40:19.626275+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-03-17T16:13:33Z`
- Merged: `2026-03-17T22:12:05Z`

## Discussion Counts

- Issue comments: 0
- Review submissions: 3 (approved=1, commented=2)
- Inline review comments: 2
- Review threads observed: 1
- Resolved/outdated thread markers: resolved=1, outdated=0
- Human participants with discussion text: mgoin, pavanimajety
- Automation comments/reviews omitted from high-signal summary: 2
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-03-17T16:18:54Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request adds support for non-gated Mixture-of-Experts models to the CUTLASS NVFP4 kernel. The changes ... (https://github.com/vllm-project/vllm/pull/37320#pullrequestreview-3962079474)
- `2026-03-17T16:27:41Z` `COMMENTED` by `mgoin` (https://github.com/vllm-project/vllm/pull/37320#pullrequestreview-3962140060)
- `2026-03-17T17:44:43Z` `APPROVED` by `pavanimajety` - LGTM, thanks! (https://github.com/vllm-project/vllm/pull/37320#pullrequestreview-3962607873)

## Inline Comment Hotspots

- `csrc/quantization/w8a8/cutlass/moe/moe_data.cu`: 2 inline comment(s)

## High-Signal Discussion

- `2026-03-17T16:27:40Z` `inline` by `mgoin` `csrc/quantization/w8a8/cutlass/moe/moe_data.cu`:24; signals: cutlass, moe; excerpt: "n is a dimension of the weight so it won't be that large, on the order of 10k" (https://github.com/vllm-project/vllm/pull/37320#discussion_r2948043060)
