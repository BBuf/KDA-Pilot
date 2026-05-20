# PR Discussion Digest

- Source PR: [vllm-project/vllm#28479](https://github.com/vllm-project/vllm/pull/28479)
- Source page: `sources/prs/vllm/PR-28479.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-28479`
- Generated at: `2026-05-20T15:38:29.437965+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-11-11T18:39:44Z`
- Merged: `2025-11-12T16:56:40Z`

## Discussion Counts

- Issue comments: 2
- Review submissions: 5 (approved=1, commented=4)
- Inline review comments: 0
- Review threads observed: 0
- Resolved/outdated thread markers: resolved=0, outdated=0
- Human participants with discussion text: LucasWilkinson, benchislett, mergify, vadiklyutiy
- Automation comments/reviews omitted from high-signal summary: 1
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-11-11T18:40:49Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request introduces a well-designed refactoring to enable more flexible and dynamic CUDA graph support ... (https://github.com/vllm-project/vllm/pull/28479#pullrequestreview-3449415049)
- `2025-11-11T20:01:38Z` `APPROVED` by `LucasWilkinson` - LGTM Id like to work towards reverting (and move back to this being an instance property) in the ... (https://github.com/vllm-project/vllm/pull/28479#pullrequestreview-3449792102)
- `2025-11-12T00:48:05Z` `COMMENTED` by `vadiklyutiy` - Before we use use trtllm attention for checking both prefill and decode. Right now seem use trtllm attention ... (https://github.com/vllm-project/vllm/pull/28479#pullrequestreview-3450752291)
- `2025-11-12T01:06:51Z` `COMMENTED` by `vadiklyutiy` - Before we use use trtllm attention for checking both prefill and decode. Right now seem use trtllm attention ... (https://github.com/vllm-project/vllm/pull/28479#pullrequestreview-3450779027)
- `2025-11-12T01:09:40Z` `COMMENTED` by `vadiklyutiy` - One more style Is there some reason to hold [ ]cudagraph support and get cudagraph support in MetaBuilder ... (https://github.com/vllm-project/vllm/pull/28479#pullrequestreview-3450788107)

## Inline Comment Hotspots

- No inline review comments were returned by GitHub.

## High-Signal Discussion

- `2025-11-12T01:09:40Z` `review` `COMMENTED` by `vadiklyutiy`; signals: attention, cuda, cudagraph; excerpt: "One more style Is there some reason to hold [ ]cudagraph support and get cudagraph support in MetaBuilder classes, maybe Backend(AttentionBackend) is better place?" (https://github.com/vllm-project/vllm/pull/28479#pullrequestreview-3450788107)
- `2025-11-12T16:54:04Z` `issue` by `benchislett`; signals: attention, cuda, hang; excerpt: "@vadiklyutiy - Currently, we have to force the use of TRTLLM attention for decodes if it is supported, so that we can statically decide ..." (https://github.com/vllm-project/vllm/pull/28479#issuecomment-3522932611)
- `2025-11-12T00:48:05Z` `review` `COMMENTED` by `vadiklyutiy`; signals: attention; excerpt: "Before we use use trtllm attention for checking both prefill and decode. Right now seem use trtllm attention is using for checking prefill only ..." (https://github.com/vllm-project/vllm/pull/28479#pullrequestreview-3450752291)
- `2025-11-12T01:06:51Z` `review` `COMMENTED` by `vadiklyutiy`; signals: attention; excerpt: "Before we use use trtllm attention for checking both prefill and decode. Right now seem use trtllm attention is using for checking prefill only ..." (https://github.com/vllm-project/vllm/pull/28479#pullrequestreview-3450779027)
- `2025-11-11T20:01:38Z` `review` `APPROVED` by `LucasWilkinson`; signals: cuda, cudagraph; excerpt: "LGTM Id like to work towards reverting (and move back to this being an instance property) in the future; but we need broader cudagraph ..." (https://github.com/vllm-project/vllm/pull/28479#pullrequestreview-3449792102)
