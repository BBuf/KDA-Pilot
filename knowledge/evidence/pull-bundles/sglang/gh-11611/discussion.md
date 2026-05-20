# PR Discussion Digest

- Source PR: [sgl-project/sglang#11611](https://github.com/sgl-project/sglang/pull/11611)
- Source page: `sources/prs/sglang/PR-11611.md`
- Evidence bundle: `evidence/pull-bundles/sglang/gh-11611`
- Generated at: `2026-05-20T15:27:25.287401+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-10-14T12:50:43Z`
- Merged: `2025-10-17T23:59:40Z`

## Discussion Counts

- Issue comments: 2
- Review submissions: 3 (approved=1, commented=2)
- Inline review comments: 2
- Review threads observed: 2
- Resolved/outdated thread markers: resolved=0, outdated=0
- Human participants with discussion text: fzyzcjy, trevor-m
- Automation comments/reviews omitted from high-signal summary: 4
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-10-14T12:52:22Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request introduces an optimization for MoE layers by enabling the overlap of shared expert ... (https://github.com/sgl-project/sglang/pull/11611#pullrequestreview-3335455309)
- `2025-10-14T17:19:49Z` `COMMENTED` by `trevor-m` - Hi @fzyzcjy - this looks like it's doing the same overlap as forward normal dual stream(). Could you ... (https://github.com/sgl-project/sglang/pull/11611#pullrequestreview-3336728566)
- `2025-10-15T23:22:10Z` `APPROVED` by `trevor-m` - Thank you for the explanation, and it looks good to me. (https://github.com/sgl-project/sglang/pull/11611#pullrequestreview-3342632770)

## Inline Comment Hotspots

- `python/sglang/srt/layers/quantization/modelopt_quant.py`: 2 inline comment(s)

## High-Signal Discussion

- `2025-10-14T17:19:49Z` `review` `COMMENTED` by `trevor-m`; signals: general review; excerpt: "Hi @fzyzcjy - this looks like it's doing the same overlap as forward normal dual stream(). Could you help explain the difference?" (https://github.com/sgl-project/sglang/pull/11611#pullrequestreview-3336728566)
- `2025-10-14T23:17:10Z` `issue` by `fzyzcjy`; signals: gemm; excerpt: "@trevor-m forward normal dual stream seems to overlap shared experts w/ routed experts, thus it is likely shared is oervlapped with dispatch and the ..." (https://github.com/sgl-project/sglang/pull/11611#issuecomment-3403946542)
