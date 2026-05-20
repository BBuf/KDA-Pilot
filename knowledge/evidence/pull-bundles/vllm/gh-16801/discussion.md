# PR Discussion Digest

- Source PR: [vllm-project/vllm#16801](https://github.com/vllm-project/vllm/pull/16801)
- Source page: `sources/prs/vllm/PR-16801.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-16801`
- Generated at: `2026-05-20T15:35:02.447753+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-04-17T19:27:07Z`
- Merged: `2025-04-18T05:13:29Z`

## Discussion Counts

- Issue comments: 3
- Review submissions: 4 (approved=1, commented=3)
- Inline review comments: 3
- Review threads observed: 1
- Resolved/outdated thread markers: resolved=0, outdated=1
- Human participants with discussion text: LucasWilkinson, liuzijing2014, mgoin
- Automation comments/reviews omitted from high-signal summary: 1
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 1

## Review Decisions

- `2025-04-17T20:46:06Z` `COMMENTED` by `liuzijing2014` (https://github.com/vllm-project/vllm/pull/16801#pullrequestreview-2776887703)
- `2025-04-17T21:00:05Z` `COMMENTED` by `LucasWilkinson` (https://github.com/vllm-project/vllm/pull/16801#pullrequestreview-2776912438)
- `2025-04-17T21:10:11Z` `COMMENTED` by `liuzijing2014` (https://github.com/vllm-project/vllm/pull/16801#pullrequestreview-2776936767)
- `2025-04-17T23:49:40Z` `APPROVED` by `mgoin` - Thanks so much for this bundle of fixes, LGTM! cc @jinzhen-lin for the moe wna16 cuda update (https://github.com/vllm-project/vllm/pull/16801#pullrequestreview-2777137554)

## Inline Comment Hotspots

- `csrc/moe/moe_wna16.cu`: 3 inline comment(s)

## High-Signal Discussion

- `2025-04-17T21:00:05Z` `inline` by `LucasWilkinson` `csrc/moe/moe_wna16.cu`:214; signals: block, moe; excerpt: "its a bit weird but the way it works is that token index ranges between 0 and topk num tokens, then topk weights is ..." (https://github.com/vllm-project/vllm/pull/16801#discussion_r2049640324)
- `2025-04-17T20:45:52Z` `inline` by `liuzijing2014` `csrc/moe/moe_wna16.cu`:214; signals: moe; excerpt: "If top k = 2, then for each token, we would have 2 top k weights to be applied. Looking at the line here, ..." (https://github.com/vllm-project/vllm/pull/16801#discussion_r2049624856)
- `2025-04-17T21:10:11Z` `inline` by `liuzijing2014` `csrc/moe/moe_wna16.cu`:214; signals: moe; excerpt: "I see so basically for topk=2, the outer loop of for (int m = 0; m < num valid tokens; ++m) would iterate each ..." (https://github.com/vllm-project/vllm/pull/16801#discussion_r2049653676)
- `2025-04-17T23:49:40Z` `review` `APPROVED` by `mgoin`; signals: cuda, moe; excerpt: "Thanks so much for this bundle of fixes, LGTM! cc @jinzhen-lin for the moe wna16 cuda update" (https://github.com/vllm-project/vllm/pull/16801#pullrequestreview-2777137554)
- `2025-04-17T21:41:58Z` `issue` by `liuzijing2014`; signals: accuracy; excerpt: "Confirmed the fix recover llama4 int4 checkpoint accuracy back to normal." (https://github.com/vllm-project/vllm/pull/16801#issuecomment-2814078194)
