# PR Discussion Digest

- Source PR: [vllm-project/vllm#28755](https://github.com/vllm-project/vllm/pull/28755)
- Source page: `sources/prs/vllm/PR-28755.md`
- Evidence bundle: `evidence/pull-bundles/vllm/gh-28755`
- Generated at: `2026-05-20T15:38:33.731738+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2025-11-14T21:41:45Z`
- Merged: `2025-11-15T10:13:42Z`

## Discussion Counts

- Issue comments: 4
- Review submissions: 2 (approved=1, commented=1)
- Inline review comments: 0
- Review threads observed: 0
- Resolved/outdated thread markers: resolved=0, outdated=0
- Human participants with discussion text: benchislett, mgoin, pavanimajety, vadiklyutiy
- Automation comments/reviews omitted from high-signal summary: 1
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2025-11-14T21:43:19Z` `COMMENTED` by `gemini-code-assist` - Code Review This pull request removes the max seq len <= 131072 limitation for using the TRTLLM attention ... (https://github.com/vllm-project/vllm/pull/28755#pullrequestreview-3466938646)
- `2025-11-15T10:13:40Z` `APPROVED` by `pavanimajety` - LGTM, thanks Vadim. (https://github.com/vllm-project/vllm/pull/28755#pullrequestreview-3467910683)

## Inline Comment Hotspots

- No inline review comments were returned by GitHub.

## High-Signal Discussion

- `2025-11-15T10:13:00Z` `issue` by `pavanimajety`; signals: cuda, flashinfer, kernel, perf, performance; excerpt: "I vote for removing the restriction to enable the full cuda graph path and filing a flashinfer kernel issue to improve kernel performance for ..." (https://github.com/vllm-project/vllm/pull/28755#issuecomment-3536283550)
- `2025-11-14T22:33:05Z` `issue` by `vadiklyutiy`; signals: cuda, cudagraph, perf, performance; excerpt: "I'm not 100% sure that the performance at 200K+ CTX is good enough here. Maybe getting full-cuda-graphs offsets the cost, but at 4-8 concurrency ..." (https://github.com/vllm-project/vllm/pull/28755#issuecomment-3534925449)
- `2025-11-14T22:03:18Z` `issue` by `benchislett`; signals: cuda, perf, performance; excerpt: "I'm not 100% sure that the performance at 200K+ CTX is good enough here. Maybe getting full-cuda-graphs offsets the cost, but at 4-8 concurrency ..." (https://github.com/vllm-project/vllm/pull/28755#issuecomment-3534821524)
- `2025-11-15T00:27:56Z` `issue` by `mgoin`; signals: attention, cuda, cudagraph; excerpt: "Is there anything that can be done to improve the trtllm attention for those poor cases? At this point I feel like removing the ..." (https://github.com/vllm-project/vllm/pull/28755#issuecomment-3535159263)
