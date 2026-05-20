# PR Discussion Digest

- Source PR: [vllm-project/vllm#22991](https://github.com/vllm-project/vllm/pull/22991)
- Source page: `sources/prs/vllm/PR-22991.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-22991`
- Generated at: `2026-05-20T15:37:14.275325+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-08-15T15:53:51Z`
- Merged: `2025-08-15T21:02:13Z`

## Discussion Counts

- Issue comments: 1
- Review submissions: 3 (approved=2, commented=1)
- Inline review comments: 2
- Review threads observed: 2
- Resolved/outdated thread markers: resolved=2, outdated=0
- Human participants with discussion text: bnellnm, simon-mo
- Automation comments/reviews omitted from high-signal summary: 4
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-08-15T15:55:39Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request enables the swap ab optimization for PPLX problem size computation, which is a ... (https://github.com/vllm-project/vllm/pull/22991#pullrequestreview-3124362397)
- `2025-08-15T20:46:44Z` `APPROVED` by `bnellnm` - LGTM. Afaik the unit tests you've run are the only ones that explicitly exercise this code. (https://github.com/vllm-project/vllm/pull/22991#pullrequestreview-3125117207)
- `2025-08-15T21:01:42Z` `APPROVED` by `simon-mo` - stamping for bill (https://github.com/vllm-project/vllm/pull/22991#pullrequestreview-3125156151)

## Inline Comment Hotspots

- `csrc/quantization/cutlass_w8a8/moe/moe_data.cu`: 2 inline comment(s)

## High-Signal Discussion

- `2025-08-15T20:46:44Z` `review` `APPROVED` by `bnellnm`; signals: general review; excerpt: "LGTM. Afaik the unit tests you've run are the only ones that explicitly exercise this code." (https://github.com/vllm-project/vllm/pull/22991#pullrequestreview-3125117207)
- `2025-08-15T21:01:42Z` `review` `APPROVED` by `simon-mo`; signals: general review; excerpt: "stamping for bill" (https://github.com/vllm-project/vllm/pull/22991#pullrequestreview-3125156151)
