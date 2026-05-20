# PR Discussion Digest

- Source PR: [Dao-AILab/flash-attention#2441](https://github.com/Dao-AILab/flash-attention/pull/2441)
- Source page: `sources/prs/flash-attention/PR-2441.md`
- Evidence bundle: `evidence/pull-bundles/flash-attention/gh-2441`
- Generated at: `2026-05-20T15:16:57.935179+00:00`
- Fetch scope: GitHub PR conversation comments, PR review submissions, and inline review-thread comments were fetched with pagination-aware GraphQL plus REST overflow fallback.
- Completeness: issue comments `complete`, reviews `complete`, inline comments `complete`.

## Timeline

- Opened: `2026-04-06T20:51:38Z`
- Merged: `2026-04-15T03:42:40Z`

## Discussion Counts

- Issue comments: 8
- Review submissions: 1 (approved=1)
- Inline review comments: 0
- Review threads observed: 0
- Resolved/outdated thread markers: resolved=0, outdated=0
- Human participants with discussion text: jayhshah, tridao
- Automation comments/reviews omitted from high-signal summary: 0
- Post-merge comments/reviews fetched but excluded from pre-merge high-signal summary: 0

## Review Decisions

- `2026-04-14T22:47:03Z` `APPROVED` by `tridao` (https://github.com/Dao-AILab/flash-attention/pull/2441#pullrequestreview-4109676113)

## Inline Comment Hotspots

- No inline review comments were returned by GitHub.

## High-Signal Discussion

- `2026-04-14T10:47:50Z` `issue` by `tridao`; signals: benchmark, perf; excerpt: "Can you add the benchmark script as well? Will be useful later when we refactor (while making sure perf stays the same). Can you ..." (https://github.com/Dao-AILab/flash-attention/pull/2441#issuecomment-4243284584)
- `2026-04-15T02:20:31Z` `issue` by `jayhshah`; signals: cuda, mla; excerpt: "On B300 and CUDA 13.1: compute-bound s q=s k MQA 16 decode s q=1 MQA 128 -- we see how MLA shape nicely balances ..." (https://github.com/Dao-AILab/flash-attention/pull/2441#issuecomment-4248669904)
- `2026-04-15T03:42:32Z` `issue` by `jayhshah`; signals: benchmark, hang; excerpt: "I've made the interface changes (removing topk indices maybe oob and changing variable names to be more generic) and added qv and gather kv ..." (https://github.com/Dao-AILab/flash-attention/pull/2441#issuecomment-4248943230)
- `2026-04-14T19:36:46Z` `issue` by `jayhshah`; signals: perf; excerpt: "I'm mostly concerned w the interface. We're adding qv (makes sense), topk indices, topk indices maybe oob and min seqlenk. Do we need topk ..." (https://github.com/Dao-AILab/flash-attention/pull/2441#issuecomment-4246627017)
- `2026-04-14T22:47:28Z` `issue` by `tridao`; signals: benchmark; excerpt: "we can merge once the benchmark script is added" (https://github.com/Dao-AILab/flash-attention/pull/2441#issuecomment-4247688961)
- `2026-04-14T10:35:44Z` `issue` by `tridao`; signals: general review; excerpt: "I'm mostly concerned w the interface. We're adding qv (makes sense), topk indices, topk indices maybe oob and min seqlenk. Do we need topk ..." (https://github.com/Dao-AILab/flash-attention/pull/2441#issuecomment-4243219340)
